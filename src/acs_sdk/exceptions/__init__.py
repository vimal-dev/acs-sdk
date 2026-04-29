"""CloudStack API exceptions."""

from typing import Optional


class CloudStackAPIError(Exception):
    """Exception raised for CloudStack API errors."""

    def __init__(
        self,
        error_code: Optional[str] = None,
        error_text: Optional[str] = None,
        response: Optional[dict] = None,
    ):
        self.error_code = error_code
        self.error_text = error_text
        self.response = response
        message = "CloudStack API Error"
        if error_code:
            message += f" {error_code}"
        if error_text:
            message += f": {error_text}"
        super().__init__(message)
