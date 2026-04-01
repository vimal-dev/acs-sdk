from typing import Generic, List, Optional, TypeVar, Union

from pydantic import BaseModel, ConfigDict, Field


T = TypeVar("T")


class APIError(BaseModel):
    number: str = Field(..., alias="Number")
    text: str = Field(...)


class ErrorsWrapper(BaseModel):
    error: Union[List[APIError], APIError] = Field(..., alias="Error")


class APIResponse(BaseModel, Generic[T]):
    model_config = ConfigDict(populate_by_name=True, use_enum_values=True)

    status: str = Field(
        ...,
        alias="Status",
        description="The status of the API response, typically 'OK' or 'ERROR'.",
    )
    errors: Optional[ErrorsWrapper] | None = Field(
        None,
        alias="Errors",
        description="A list of error messages if the API call was not successful.",
    )
    warnings: list[dict] | None = Field(
        None,
        alias="Warnings",
        description="A list of warning messages if there are any issues with the API call.",
    )

    @property
    def is_ok(self) -> bool:
        """
        Check if the API response indicates a successful call.
        """
        return self.status.upper() == "OK"

    @property
    def is_error(self) -> bool:
        """
        Check if the API response indicates an error.
        """
        return self.status.upper() == "ERROR"

    def error_messages(self) -> list[str]:
        """Extract error messages from the API response, if any."""
        if not self.errors:
            return []

        err = self.errors.error

        if isinstance(err, list):
            return [e.text for e in err]

        return [err.text]



