"""Retry logic and configuration for resilient API communications.

This module provides retry mechanisms for handling transient failures in API
requests. It implements exponential backoff to avoid overwhelming the API
server during temporary outages.

Only failures where the request is known not to have been processed are
retried. CloudStack business errors (e.g. 431 parameter errors or 53x codes)
and ambiguous failures such as read timeouts are raised immediately, so a
mutating command like ``deployVirtualMachine`` is never executed twice.
"""

import asyncio
import functools
import inspect
import time

import httpx

DEFAULT_RETRY_STATUSES = (429, 502, 503)

# Errors raised before the request reached the server, so retrying is safe.
_RETRYABLE_TRANSPORT_ERRORS = (httpx.ConnectError, httpx.ConnectTimeout, httpx.PoolTimeout)


class RetryConfig:
    """Configuration for retry behavior with exponential backoff.

    This class defines how many times failed requests should be retried and
    the backoff strategy between attempts.

    Attributes:
        retries (int): Maximum number of attempts (default: 3).
        backoff (float): Initial backoff multiplier in seconds (default: 0.5).
        retry_on (tuple[int, ...]): HTTP status codes considered transient
            (default: 429, 502, 503).
    """

    def __init__(self, retries=3, backoff=0.5, retry_on=DEFAULT_RETRY_STATUSES):
        """Initialize retry configuration.

        Args:
            retries (int): Maximum number of attempts. Defaults to 3.
            backoff (float): Initial backoff value in seconds for exponential
                backoff calculation. Defaults to 0.5.
            retry_on (tuple[int, ...]): HTTP status codes that should be retried.
        """
        self.retries = retries
        self.backoff = backoff
        self.retry_on = tuple(retry_on)


def is_retryable(exc: BaseException, retry_on=DEFAULT_RETRY_STATUSES) -> bool:
    """Return True if ``exc`` is a transient failure that is safe to retry.

    Args:
        exc: The exception raised by the request.
        retry_on: HTTP status codes considered transient.

    Returns:
        bool: True for connection-phase transport errors and for HTTP status
            errors whose status code is in ``retry_on``.
    """
    if isinstance(exc, _RETRYABLE_TRANSPORT_ERRORS):
        return True
    if isinstance(exc, httpx.HTTPStatusError):
        return exc.response.status_code in retry_on
    return False


def with_retry(func):
    """Decorator that adds retry logic with exponential backoff to a function.

    This decorator wraps a sync or async method to automatically retry on
    transient failures (see :func:`is_retryable`) using exponential backoff.
    It reads the retry configuration from the instance (self.retry) of the
    decorated method.

    The backoff time between retries follows the formula:
        backoff_time = retry.backoff * (2 ** attempt_number)

    Args:
        func: The function to decorate. Must be a method where the first
            argument (self) has a 'retry' attribute of type RetryConfig.

    Returns:
        function: The wrapped function that implements retry logic.

    Example:
        >>> class MyService:
        ...     def __init__(self):
        ...         self.retry = RetryConfig(retries=3, backoff=0.5)
        ...     @with_retry
        ...     def make_request(self):
        ...         # Request logic here
        ...         pass
    """

    def _should_retry(config: RetryConfig, exc: Exception, attempt: int) -> bool:
        return attempt < config.retries - 1 and is_retryable(exc, config.retry_on)

    if inspect.iscoroutinefunction(func):

        @functools.wraps(func)
        async def async_wrapper(self, *args, **kwargs):
            for attempt in range(self.retry.retries):
                try:
                    return await func(self, *args, **kwargs)
                except Exception as exc:
                    if not _should_retry(self.retry, exc, attempt):
                        raise
                    await asyncio.sleep(self.retry.backoff * (2**attempt))

        return async_wrapper

    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        for attempt in range(self.retry.retries):
            try:
                return func(self, *args, **kwargs)
            except Exception as exc:
                if not _should_retry(self.retry, exc, attempt):
                    raise
                time.sleep(self.retry.backoff * (2**attempt))

    return wrapper
