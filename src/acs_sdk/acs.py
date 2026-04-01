"""Main module for Apache CloudStack SDK.

This module provides the top-level ApacheCloudStack class that serves as
the primary interface for interacting with Apache CloudStack environments.
"""

from acs_sdk.schemas.config import ApacheCloudStackConfig
from acs_sdk.client.client import ApacheCloudStackClient


class ApacheCloudStack:
    """High-level interface for Apache CloudStack API interactions.

    This class wraps the CloudStack client and provides a convenient entry point
    for working with CloudStack resources. It handles initialization of the
    client with provided configuration.

    Attributes:
        config (ApacheCloudStackConfig): CloudStack configuration with endpoint
            and API credentials.
        client (ApacheCloudStackClient): The underlying HTTP client for API
            communication.

    Example:
        >>> config = ApacheCloudStackConfig(
        ...     api_key='your-key',
        ...     api_secret='your-secret',
        ...     endpoint='https://cloudstack.example.com'
        ... )
        >>> acs = ApacheCloudStack(config)
        >>> response = acs.client.call('listUsers')
    """
    def __init__(self, config: ApacheCloudStackConfig):
        """Initialize the ApacheCloudStack SDK.

        Args:
            config (ApacheCloudStackConfig): Configuration object containing
                CloudStack endpoint URL and API credentials.
        """
        self.config = config
        self.client = ApacheCloudStackClient(config)
