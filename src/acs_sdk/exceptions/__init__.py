"""CloudStack API exceptions."""

from typing import Optional


class CloudStackAPIError(Exception):
    """Exception raised for CloudStack API errors.

    Attributes:
        error_code (Optional[str | int]): CloudStack's ``cserrorcode``/``errorcode``,
            or the HTTP status when the body carries none.
        error_text (Optional[str]): CloudStack's ``errortext`` or a fallback message.
        response (Optional[dict]): The error payload, when the body was JSON.
        status_code (Optional[int]): The HTTP status of the failed response.
    """

    def __init__(
        self,
        error_code: Optional[str | int] = None,
        error_text: Optional[str] = None,
        response: Optional[dict] = None,
        status_code: Optional[int] = None,
    ):
        self.error_code = error_code
        self.error_text = error_text
        self.response = response
        self.status_code = status_code
        message = "[CloudStack API Error]"
        if status_code:
            message += f" (HTTP {status_code})"
        if error_code:
            message += f" {error_code}"
        if error_text:
            message += f": {error_text}"
        super().__init__(message)
