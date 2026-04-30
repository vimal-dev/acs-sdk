from pydantic import BaseModel, Field, field_validator, field_serializer
from typing import Optional
from datetime import datetime

from acs_sdk.schemas.request.base import PaginationMixin


class ListUsageRecordsRequest(BaseModel, PaginationMixin):
    # Required
    startdate: datetime = Field(..., description="Start date")
    enddate: datetime = Field(..., description="End date")

    # 🔍 Filters
    account: Optional[str] = Field(None, description="List usage records for the specified user.")
    accountid: Optional[str] = Field(
        None,
        alias="accountId",
        description="List usage records for the specified account.",
    )
    domainid: Optional[str] = Field(
        None,
        alias="domainId",
        description="List usage records for the specified domain.",
    )
    projectid: Optional[str] = Field(
        None,
        alias="projectId",
        description="List usage records for the specified project.",
    )
    zoneid: Optional[str] = Field(
        None, alias="zoneId", description="List usage records for the specified zone."
    )

    # Resource filters
    usageid: Optional[str] = Field(
        None, alias="usageId", description="List usage records by usage ID."
    )
    type: Optional[int] = Field(None, description="Usage type ID")

    # Advanced filters
    keyword: Optional[str] = Field(None, alias="keyword", description="Search keyword")

    # --------------------------------------------------
    # Validators (Pydantic v2 style)
    # --------------------------------------------------

    @field_validator("enddate")
    @classmethod
    def validate_date_range(cls, v, info):
        start = info.data.get("startdate")
        if start and v < start:
            raise ValueError("enddate must be >= startdate")
        return v

    @field_serializer("startdate", "enddate")
    def serialize_date(self, value: datetime, _info):
        return value.strftime("%Y-%m-%dT%H:%M:%S%z")


class GenerateUsageRecordsRequest(BaseModel):
    startdate: Optional[datetime] = Field(None, description="Start date")
    enddate: Optional[datetime] = Field(None, description="End date")
    domainid: Optional[str] = Field(
        None,
        alias="domainId",
        description="Generate usage records for the specified domain.",
    )

    # --------------------------------------------------
    # Validators
    # --------------------------------------------------

    @field_validator("enddate")
    @classmethod
    def validate_date_range(cls, v, info):
        if isinstance(v, datetime):
            start = info.data.get("startdate")
            if start and v < start:
                raise ValueError("enddate must be >= startdate")
        return v

    @field_serializer("startdate", "enddate")
    def serialize_date(self, value: datetime, _info):
        if isinstance(value, datetime):
            return value.strftime("%Y-%m-%dT%H:%M:%S%z")
        return value


class RemoveRawUsageRecordsRequest(BaseModel):
    interval: int = Field(
        ...,
        description=("Interval in days. Usage records older than this interval will be removed."),
    )
