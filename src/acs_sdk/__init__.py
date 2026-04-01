"""Apache CloudStack Python SDK.

This package provides a type-safe, modern Python interface for interacting
with Apache CloudStack environments. It handles request signing, retries,
and response parsing automatically.

Main Components:
    - ApacheCloudStack: High-level entry point for SDK usage
    - ApacheCloudStackConfig: Configuration management
    - ApacheCloudStackClient: Low-level HTTP client

Example:
    >>> from acs_sdk import ApacheCloudStack, ApacheCloudStackConfig
    >>> config = ApacheCloudStackConfig(
    ...     api_endpoint='https://api.cloudstack.com/client/api',
    ...     api_key='your-key',
    ...     api_secret='your-secret'
    ... )
    >>> acs = ApacheCloudStack(config)
    >>> response = acs.client.call('listUsers')
"""

from .acs import ApacheCloudStack
from .schemas.config import ApacheCloudStackConfig

__all__ = ["ApacheCloudStack", "ApacheCloudStackConfig"]
