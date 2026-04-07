"""Main module for Apache CloudStack SDK.

This module provides the top-level ApacheCloudStack class that serves as
the primary interface for interacting with Apache CloudStack environments.
"""

import logging
from opentelemetry import trace

from acs_sdk.schemas.config import ApacheCloudStackConfig
from acs_sdk.client.client import ApacheCloudStackClient
from acs_sdk.services.job import Job
from acs_sdk.services.region import Region
from acs_sdk.services.virtual_machine import VirtualMachine
from acs_sdk.services.zone import Zone


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

    _service_map = {
        "job": Job,
        "region": Region,
        "vm": VirtualMachine,
        "zone": Zone,
    }

    def __init__(
        self,
        config: ApacheCloudStackConfig,
        tracer: trace.Tracer = None,
        logger: logging.Logger = None,
    ):
        """Initialize the ApacheCloudStack SDK.

        Args:
            config (ApacheCloudStackConfig): Configuration object containing
                CloudStack endpoint URL and API credentials.
            tracer (trace.Tracer, optional): Tracer for API call tracing.
            logger (logging.Logger, optional): Logger for API call logging.

        """
        tracer = tracer or trace.get_tracer(__name__)
        logger = logger or logging.getLogger("cloudstack")
        self.client = ApacheCloudStackClient(config, tracer=tracer, logger=logger)
        self._cache = {}

    def __getattr__(self, name):
        """Dynamically load service classes on demand."""
        if name in self._service_map:
            if name not in self._cache:
                self._cache[name] = self._service_map[name](self.client)
            return self._cache[name]

        raise AttributeError(f"{name} not found")
