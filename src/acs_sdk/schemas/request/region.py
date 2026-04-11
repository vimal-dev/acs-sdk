from typing import Optional
from pydantic import Field
from acs_sdk.schemas.request.base import APIRequest


class ListRegionsRequest(APIRequest):
    id: Optional[str] = Field(
        None, description="List regions by ID"
    )
    name: Optional[str] = Field(
        None, description="List regions by name"
    )
    keyword: Optional[str] = Field(
        None, description="List regions by keyword"
    )
    page: Optional[int] = Field(
        1, ge=1, description="Page number"
    )
    pagesize: Optional[int] = Field(
        50, ge=1, le=500, description="Number of results per page"
    )