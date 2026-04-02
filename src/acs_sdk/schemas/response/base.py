from typing import Generic, List, Optional, TypeVar, Union

from pydantic import BaseModel, ConfigDict, Field


T = TypeVar("T")


class APIError(BaseModel):
    number: str = Field(..., alias="Number", description="The error code number returned by the API.")
    text: str = Field(..., alias="Text", description="The error message returned by the API.")


class APIResponse(BaseModel, Generic[T]):
    model_config = ConfigDict(populate_by_name=True, use_enum_values=True)

    status: str = Field(
        ...,
        description="The status of the API response, typically 'OK' or 'ERROR'.",
    )
    errors: Optional[Union[List[APIError], APIError]] = Field(
        None,
        description="A list of error messages if the API call was not successful.",
    )
    data: Optional[T] = Field(None, description="The data returned from the API call, if any.")

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

        err = self.errors

        if isinstance(err, list):
            return [e.text for e in err]

        return [err.text]
