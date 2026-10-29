"""Apache CloudStack API client implementation.

This module provides the main client for executing API commands against
an Apache CloudStack endpoint with automatic request signing, retries,
and response parsing. Supports both sync and async operations.
"""

import contextlib
import logging
import re
from typing import Any, Dict, Iterator, Optional
import httpx
from opentelemetry import trace
from opentelemetry.trace import SpanKind, Status, StatusCode

from acs_sdk.client.contract import ClientContract
from acs_sdk.core.retry import RetryConfig, with_retry
from acs_sdk.core.signer import RequestSigner
from acs_sdk.schemas.config import ApacheCloudStackConfig

_SECRET_PARAMS = re.compile(r"((?:signature|apikey|sessionkey)=)[^&\s'\"]*", re.IGNORECASE)


def _redact(text: str) -> str:
    """Mask credential query parameters (apikey, signature, sessionkey) in ``text``."""
    return _SECRET_PARAMS.sub(r"\1***", text)


class _BaseCloudStackClient(ClientContract):
    """Shared request building, tracing and async transport for CloudStack clients.

    Subclasses provide the public surface: ``ApacheCloudStackClient`` adds the
    sync ``call`` on top of ``call_async``, ``ApacheCloudStackAsyncClient`` is
    async-only.
    """

    def __init__(
        self,
        config: ApacheCloudStackConfig,
        tracer: Optional[trace.Tracer] = None,
        logger: Optional[logging.Logger] = None,
        async_client: Optional[httpx.AsyncClient] = None,
        retry: Optional[RetryConfig] = None,
    ):
        self.config = config
        self.signer = RequestSigner(config.api_key, config.api_secret)
        self.retry = retry or RetryConfig()
        self.tracer = tracer or trace.get_tracer(__name__)
        self.logger = logger or logging.getLogger("cloudstack")
        self._async_client = async_client

    async def __aenter__(self):
        self._get_async_client()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.aclose()

    @with_retry
    async def call_async(
        self, command: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Execute an Apache CloudStack API command (async).

        Requests share one ``httpx.AsyncClient`` connection pool, and transient
        failures are retried according to ``self.retry``.

        Args:
            command (str): The CloudStack API command to execute.
            params (Optional[Dict[str, Any]]): Optional command-specific parameters.

        Returns:
            Dict[str, Any]: The parsed JSON response from the API as a dictionary.

        Raises:
            httpx.HTTPStatusError: If the HTTP request returns an error status code.
            httpx.RequestError: On network errors.

        Example:
            >>> async with ApacheCloudStackAsyncClient(config) as client:
            ...     response = await client.call_async('listUsers')
            ...     user = await client.call_async('getUser', {'userid': '123'})
        """
        with self._span(command):
            return await self._request_async(self._build_params(command, params))

    async def aclose(self):
        """Close the shared async HTTP client, if one was created."""
        if self._async_client is not None:
            await self._async_client.aclose()
            self._async_client = None

    @contextlib.contextmanager
    def _span(self, command: str) -> Iterator[trace.Span]:
        """Open the client span for a CloudStack command."""
        with self.tracer.start_as_current_span(
            f"CloudStack {command}", kind=SpanKind.CLIENT
        ) as span:
            span.set_attribute("cloudstack.command", command)
            span.set_attribute("cloudstack.endpoint", self.config.endpoint)
            self.logger.debug("Executing CloudStack command: %s", command)
            yield span

    def _build_params(self, command: str, params: Optional[Dict[str, Any]]) -> Dict[str, Any]:
        """Merge ``command`` and ``params`` into a signed (HMAC-SHA1) parameter dict."""
        base_params = {"command": command, "response": "json"}
        if params:
            base_params.update(params)
        return self.signer.sign(base_params)

    def _http_options(self) -> Dict[str, Any]:
        """Common keyword arguments for the underlying httpx clients."""
        return {"base_url": self.config.endpoint, "timeout": self.config.timeout}

    def _get_async_client(self) -> httpx.AsyncClient:
        """Return the shared AsyncClient, creating it on first use.

        A lazily created client is bound to the event loop it is first used
        on; pass ``async_client`` to the constructor to manage it yourself.
        """
        if self._async_client is None:
            self._async_client = httpx.AsyncClient(**self._http_options())
        return self._async_client

    async def _request_async(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Send the signed GET request asynchronously and return the parsed JSON."""
        try:
            response = await self._get_async_client().get("", params=params)
            response.raise_for_status()
            return self._on_success(response)
        except Exception as exc:
            raise self._on_error(exc, params.get("command")) from None

    def _on_success(self, response: httpx.Response) -> Dict[str, Any]:
        """Mark the current span successful and return the parsed JSON body."""
        span = trace.get_current_span()
        span.set_attribute("http.status_code", response.status_code)
        span.set_status(Status(StatusCode.OK))
        self.logger.debug(
            "CloudStack request completed: %s %s", response.status_code, response.url.path
        )
        return response.json()

    def _on_error(self, exc: Exception, command: Optional[str]) -> Exception:
        """Record a failed request on the current span and log it without credentials.

        The signed request URL carries the API key and signature, and httpx embeds
        that URL in its exception messages. This builds an equivalent exception
        with a redacted message so it can be re-raised (``from None``) without
        leaking secrets into logs, traces or tracebacks.

        Args:
            exc (Exception): The exception raised by the HTTP request.
            command (Optional[str]): The CloudStack command that failed.

        Returns:
            Exception: The sanitized exception to raise in place of ``exc``.
        """
        message = _redact(str(exc))
        if isinstance(exc, httpx.HTTPStatusError):
            sanitized = httpx.HTTPStatusError(message, request=exc.request, response=exc.response)
        elif isinstance(exc, httpx.RequestError):
            try:
                request = exc.request
            except RuntimeError:  # raised by httpx when no request is attached
                request = None
            sanitized = type(exc)(message, request=request)
        else:
            sanitized = exc

        span = trace.get_current_span()
        span.set_status(Status(StatusCode.ERROR, message))
        span.set_attribute("exception.type", type(exc).__name__)
        if isinstance(exc, httpx.HTTPStatusError):
            span.set_attribute("http.status_code", exc.response.status_code)
            span.set_attribute("http.error_message", _redact(exc.response.text[:1000]))
        self.logger.error("CloudStack %s failed: %s", command, message)
        return sanitized


class ApacheCloudStackClient(_BaseCloudStackClient):
    """CloudStack API client supporting both sync (``call``) and async (``call_async``) use.

    Use it as a context manager to release connections: ``with`` closes the
    sync connection pool, ``async with`` closes both pools.

    Example:
        >>> with ApacheCloudStackClient(config) as client:
        ...     response = client.call('listUsers')
    """

    def __init__(
        self,
        config: ApacheCloudStackConfig,
        client: Optional[httpx.Client] = None,
        tracer: Optional[trace.Tracer] = None,
        logger: Optional[logging.Logger] = None,
        async_client: Optional[httpx.AsyncClient] = None,
        retry: Optional[RetryConfig] = None,
    ):
        super().__init__(
            config, tracer=tracer, logger=logger, async_client=async_client, retry=retry
        )
        self.client = client or httpx.Client(**self._http_options())

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @with_retry
    def call(self, command: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Execute an Apache CloudStack API command (sync).

        Signs the request, sends it as an HTTP GET and returns the parsed JSON.
        Transient failures are retried according to ``self.retry``.

        Args:
            command (str): The CloudStack API command to execute (e.g. 'listUsers').
            params (Optional[Dict[str, Any]]): Optional command-specific parameters.

        Returns:
            Dict[str, Any]: The parsed JSON response from the API as a dictionary.

        Raises:
            httpx.HTTPStatusError: If the HTTP request returns an error status code.
            httpx.RequestError: On network errors.

        Example:
            >>> response = client.call('listUsers')
            >>> user_response = client.call('getUser', {'userid': '123'})
        """
        with self._span(command):
            return self._request(self._build_params(command, params))

    def close(self):
        """Close the sync HTTP client.

        If ``call_async`` was used, use ``await client.aclose()`` (or
        ``async with``) instead, which closes both connection pools.
        """
        self.client.close()

    async def aclose(self):
        """Close both the async and the sync HTTP clients."""
        await super().aclose()
        self.client.close()

    def _request(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Send the signed GET request and return the parsed JSON."""
        try:
            response = self.client.get("", params=params)
            response.raise_for_status()
            return self._on_success(response)
        except Exception as exc:
            raise self._on_error(exc, params.get("command")) from None


class ApacheCloudStackAsyncClient(_BaseCloudStackClient):
    """Async-only CloudStack API client for modern async/await patterns.

    Example:
        >>> async with ApacheCloudStackAsyncClient(config) as client:
        ...     response = await client.call_async('listUsers')
    """

    def __init__(
        self,
        config: ApacheCloudStackConfig,
        client: Optional[httpx.AsyncClient] = None,
        tracer: Optional[trace.Tracer] = None,
        logger: Optional[logging.Logger] = None,
        retry: Optional[RetryConfig] = None,
    ):
        super().__init__(config, tracer=tracer, logger=logger, async_client=client, retry=retry)

    @property
    def client(self) -> Optional[httpx.AsyncClient]:
        """The underlying ``httpx.AsyncClient``; ``None`` until first use."""
        return self._async_client

    def call(self, command: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Not supported: this client is async-only, use ``call_async``."""
        raise NotImplementedError(
            "ApacheCloudStackAsyncClient is async-only; use `await client.call_async(...)`"
        )

    async def close(self):
        """Close the async HTTP client connection (alias of ``aclose``)."""
        await self.aclose()
