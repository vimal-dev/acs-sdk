"""Retry logic and configuration for resilient API communications.

This module provides retry mechanisms for handling transient failures in API
requests. It implements exponential backoff to avoid overwhelming the API
server during temporary outages.
"""

import time


class RetryConfig:
    """Configuration for retry behavior with exponential backoff.

    This class defines how many times failed requests should be retried and
    the backoff strategy between attempts.

    Attributes:
        retries (int): Maximum number of retry attempts (default: 3).
        backoff (float): Initial backoff multiplier in seconds (default: 0.5).
    """
    def __init__(self, retries=3, backoff=0.5):
        """Initialize retry configuration.

        Args:
            retries (int): Maximum number of retry attempts. Defaults to 3.
            backoff (float): Initial backoff value in seconds for exponential
                backoff calculation. Defaults to 0.5.
        """
        self.retries = retries
        self.backoff = backoff


def with_retry(func):
    """Decorator that adds retry logic with exponential backoff to a function.

    This decorator wraps a function to automatically retry on exceptions using
    exponential backoff. It accesses the retry configuration from the instance
    (self.retry) of the decorated method.

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
    def wrapper(*args, **kwargs):
        self = args[0]
        for attempt in range(self.retry.retries):
            try:
                return func(*args, **kwargs)
            except Exception:
                if attempt == self.retry.retries - 1:
                    raise
                time.sleep(self.retry.backoff * (2 ** attempt))
    return wrapper