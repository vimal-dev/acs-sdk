"""CloudStack configuration schema module.

This module defines the Pydantic configuration model for Apache CloudStack
connection parameters and credentials.
"""

from typing import Optional

from pydantic import BaseModel, ConfigDict, computed_field, Field


class ApacheCloudStackConfig(BaseModel):
    """Configuration for Apache CloudStack API connections.

    This Pydantic model validates and manages the configuration needed to
    connect to an Apache CloudStack environment. All fields are required
    to establish a valid connection.

    Attributes:
        api_endpoint (str): The complete CloudStack API endpoint URL
            (e.g., 'https://api.cloudstack.example.com/client/api').
        api_key (str): The CloudStack API key for authentication.
        api_secret (str): The CloudStack API secret for request signing.
        timeout (Optional[int]): HTTP request timeout in seconds. Must be
            positive. Defaults to 30 seconds.

    Example:
        >>> config = ApacheCloudStackConfig(
        ...     api_endpoint='https://api.cloudstack.com/client/api',
        ...     api_key='your-api-key',
        ...     api_secret='your-api-secret',
        ...     timeout=60
        ... )
    """

    api_endpoint: str = Field(..., min_length=1)
    api_key: str = Field(..., min_length=1)
    api_secret: str = Field(..., min_length=1)
    timeout: Optional[int] = Field(default=30, gt=0)

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "api_endpoint": "https://api.cloudstack.example.com/client/api",
                    "api_key": "key",
                    "api_secret": "secret",
                    "timeout": 30,
                }
            ]
        }
    )

    @computed_field
    @property
    def endpoint(self) -> str:
        """Get the API endpoint URL.

        Returns:
            str: The CloudStack API endpoint URL.
        """
        return self.api_endpoint
