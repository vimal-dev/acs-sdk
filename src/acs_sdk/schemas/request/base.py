from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class APIRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True, use_enum_values=True)


class PaginationMixin:
    page: Optional[int] = Field(1, ge=1, description="Page number")
    pagesize: Optional[int] = Field(50, ge=1, le=500, description="Number of results per page")
