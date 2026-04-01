"""Apache CloudStack API client implementation.

This module provides the main client for executing API commands against
an Apache CloudStack endpoint with automatic request signing, retries,
and response parsing. Supports both sync and async operations.
"""

from typing import Any, Dict, Optional
import httpx

from acs_sdk.client.contract import ClientContract
from acs_sdk.core.retry import RetryConfig, with_retry
from acs_sdk.core.signer import RequestSigner
from acs_sdk.schemas.config import ApacheCloudStackConfig


class ApacheCloudStackClient(ClientContract):
    def __init__(
        self,
        config: ApacheCloudStackConfig,
        client: Optional[httpx.Client] = None,
    ):
        self.config = config
        self.signer = RequestSigner(config.api_key, config.api_secret)
        self.retry = RetryConfig()
        self.client = client or httpx.Client(
            base_url=config.endpoint,
            timeout=config.timeout,
        )

    # 🔹 Public API call
    @with_retry
    def call(self, command: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Execute an Apache CloudStack API command (sync).

        This is the main entry point for making API requests. The method builds
        the complete request parameters (including signing), sends the HTTP GET
        request, and returns the parsed JSON response.

        This method is decorated with @with_retry to automatically retry on
        transient failures with exponential backoff.

        Args:
            command (str): The CloudStack API command to execute (e.g., 'listUsers',
                'createUser', etc.)
            params (Optional[Dict[str, Any]]): Optional command-specific parameters
                as a dictionary. Defaults to None.

        Returns:
            Dict[str, Any]: The parsed JSON response from the API as a dictionary.

        Raises:
            httpx.HTTPStatusError: If the HTTP request returns an error status code.
            Various exceptions on network errors or request signing failures.

        Example:
            >>> client = ApacheCloudStackClient(config)
            >>> response = client.call('listUsers')
            >>> user_response = client.call('getUser', {'userid': '123'})
        """
        payload = self._build_params(command, params)
        return self._request(payload)

    # 🔹 Async API call
    @with_retry
    async def call_async(self, command: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Execute an Apache CloudStack API command (async).

        Async version of the call method for use with asyncio. Provides the same
        functionality with non-blocking I/O operations.

        Args:
            command (str): The CloudStack API command to execute.
            params (Optional[Dict[str, Any]]): Optional command-specific parameters.

        Returns:
            Dict[str, Any]: The parsed JSON response from the API as a dictionary.

        Raises:
            httpx.HTTPStatusError: If the HTTP request returns an error status code.

        Example:
            >>> async with ApacheCloudStackAsyncClient(config) as client:
            ...     response = await client.call_async('listUsers')
            ...     user = await client.call_async('getUser', {'userid': '123'})
        """
        payload = self._build_params(command, params)
        return await self._request_async(payload)

    # 🔹 Build params (isolated logic)
    def _build_params(self, command: str, params: Optional[Dict[str, Any]]) -> Dict[str, Any]:
        """Build and sign request parameters.

        This internal method prepares the request by:
        1. Creating base parameters with the command and response format
        2. Merging in any additional command-specific parameters
        3. Signing the complete parameter set with HMAC-SHA1

        Args:
            command (str): The CloudStack API command.
            params (Optional[Dict[str, Any]]): Optional command-specific parameters.

        Returns:
            Dict[str, Any]: The complete, signed parameter dictionary ready
                for HTTP transmission.
        """
        base_params = {"command": command, "response": "json"}

        if params:
            base_params.update(params)
        signed_params = self.signer.sign(base_params)
        return signed_params

    # 🔹 HTTP layer (sync)
    def _request(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Send signed HTTP GET request to CloudStack endpoint (sync).

        This internal method handles the low-level HTTP communication,
        enforces successful status codes, and parses the JSON response.

        Args:
            params (Dict[str, Any]): The complete signed parameter dictionary.

        Returns:
            Dict[str, Any]: The parsed JSON response from the API.

        Raises:
            httpx.HTTPStatusError: If the HTTP response has a non-success status code.
        """
        response = self.client.get("", params=params)
        response.raise_for_status()
        return response.json()

    # 🔹 HTTP layer (async)
    async def _request_async(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Send signed HTTP GET request to CloudStack endpoint (async).

        Async version of _request for non-blocking I/O operations.

        Args:
            params (Dict[str, Any]): The complete signed parameter dictionary.

        Returns:
            Dict[str, Any]: The parsed JSON response from the API.

        Raises:
            httpx.HTTPStatusError: If the HTTP response has a non-success status code.
        """
        async with httpx.AsyncClient(
            base_url=self.config.endpoint,
            timeout=self.config.timeout,
        ) as async_client:
            response = await async_client.get("", params=params)
            response.raise_for_status()
            return response.json()

    def close(self):
        """Close the HTTP client connection.

        Properly closes the underlying httpx.Client to release resources
        and connections. Call this method when you're done using the client.

        Example:
            >>> try:
            ...     response = client.call('listUsers')
            ... finally:
            ...     client.close()
        """
        self.client.close()


class ApacheCloudStackAsyncClient(ClientContract):
    """Async-only CloudStack API client for modern async/await patterns."""

    def __init__(
        self,
        config: ApacheCloudStackConfig,
        client: Optional[httpx.AsyncClient] = None,
    ):
        self.config = config
        self.signer = RequestSigner(config.api_key, config.api_secret)
        self.retry = RetryConfig()
        self.client = client

    async def __aenter__(self):
        """Async context manager entry."""
        if self.client is None:
            self.client = httpx.AsyncClient(
                base_url=self.config.endpoint,
                timeout=self.config.timeout,
            )
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        await self.close()

    @with_retry
    async def call_async(self, command: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Execute an Apache CloudStack API command asynchronously.

        Args:
            command (str): The CloudStack API command to execute.
            params (Optional[Dict[str, Any]]): Optional command-specific parameters.

        Returns:
            Dict[str, Any]: The parsed JSON response from the API.

        Example:
            >>> async with ApacheCloudStackAsyncClient(config) as client:
            ...     response = await client.call_async('listUsers')
        """
        payload = self._build_params(command, params)
        return await self._request_async(payload)

    def _build_params(self, command: str, params: Optional[Dict[str, Any]]) -> Dict[str, Any]:
        """Build and sign request parameters."""
        base_params = {"command": command, "response": "json"}
        if params:
            base_params.update(params)
        return self.signer.sign(base_params)

    async def _request_async(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Send signed HTTP GET request asynchronously."""
        response = await self.client.get("", params=params)
        response.raise_for_status()
        return response.json()

    async def close(self):
        """Close the async HTTP client connection."""
        if self.client:
            await self.client.aclose()
