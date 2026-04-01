"""Base service module for CloudStack resource operations.

This module provides the BaseService class that acts as a foundation for
service implementations that communicate with the CloudStack API.
"""

from acs_sdk.client.contract import ClientContract


class BaseService:
    """Base class for CloudStack service implementations.

    This abstract base class is intended to be subclassed for specific
    CloudStack resource services (e.g., UserService, VMService, etc.).
    It provides a common interface for accessing the CloudStack client.

    Attributes:
        client (ClientContract): The CloudStack API client used to execute
            commands on the CloudStack endpoint.

    Example:
        >>> class UserService(BaseService):
        ...     def get_user(self, user_id):
        ...         return self.client.call('getUser', {'id': user_id})
    """

    def __init__(self, client: ClientContract):
        """Initialize the service with a CloudStack client.

        Args:
            client (ClientContract): The CloudStack API client for making
                API calls.
        """
        self.client = client
