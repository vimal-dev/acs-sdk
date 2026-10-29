"""CloudStack configuration schema module.

This module defines the Pydantic configuration model for Apache CloudStack
connection parameters and credentials.
"""

from typing import Optional, Tuple

from pydantic import BaseModel, ConfigDict, computed_field, Field

from acs_sdk.core.retry import DEFAULT_RETRY_STATUSES


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
            positive. Defaults to 10 seconds.
        retries (int): Maximum number of attempts per request, including the
            first one (1 disables retries). Defaults to 3.
        backoff (float): Initial backoff in seconds for exponential backoff
            between attempts. Defaults to 0.5.
        retry_on (Tuple[int, ...]): HTTP status codes treated as transient
            and retried. Defaults to (429, 502, 503).

    Example:
        >>> config = ApacheCloudStackConfig(
        ...     api_endpoint='https://api.cloudstack.com/client/api',
        ...     api_key='your-api-key',
        ...     api_secret='your-api-secret',
        ...     timeout=10,
        ...     retries=5,
        ...     backoff=1.0
        ... )
    """

    api_endpoint: str = Field(..., min_length=1)
    api_key: str = Field(..., min_length=1)
    api_secret: str = Field(..., min_length=1)
    timeout: Optional[int] = Field(default=10, gt=0)
    retries: int = Field(default=3, ge=1)
    backoff: float = Field(default=0.5, ge=0)
    retry_on: Tuple[int, ...] = Field(default=DEFAULT_RETRY_STATUSES)

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "api_endpoint": "https://api.cloudstack.example.com/client/api",
                    "api_key": "key",
                    "api_secret": "secret",
                    "timeout": 10,
                    "retries": 3,
                    "backoff": 0.5,
                    "retry_on": [429, 502, 503],
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
