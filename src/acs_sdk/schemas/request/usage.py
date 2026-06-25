from pydantic import BaseModel, Field, field_validator, field_serializer
from typing import Optional
from datetime import datetime

from acs_sdk.schemas.request.base import PaginationMixin


class ListUsageRecordsRequest(BaseModel, PaginationMixin):
    # Required
    startdate: datetime = Field(
        ...,
        description="Start date range for usage record query.",
    )
    enddate: datetime = Field(
        ...,
        description="End date range for usage record query.",
    )

    # Filters
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
        description="List usage records for specified project.",
    )
    # Resource filters
    usageid: Optional[str] = Field(
        None,
        alias="usageId",
        description="List usage records for the specified usage UUID. Can be used only together with type parameter.",
    )
    type: Optional[int] = Field(
        None, description="List usage records for the specified usage type."
    )

    # Advanced filters
    keyword: Optional[str] = Field(None, description="List by keyword.")
    includetags: Optional[bool] = Field(
        None,
        alias="includeTags",
        description="Flag to enable display of Tags for a resource.",
    )
    isrecursive: Optional[bool] = Field(
        None,
        alias="isRecursive",
        description="Specify if usage records should be fetched recursively per domain. If an account id is passed, records will be limited to that account.",
    )
    oldformat: Optional[bool] = Field(
        None,
        alias="oldFormat",
        description="Flag to enable description rendered in old format which uses internal database IDs instead of UUIDs. False by default.",
    )

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
    startdate: Optional[datetime] = Field(
        None,
        description="Start date range for usage record query. Use yyyy-MM-dd as the date format.",
    )
    enddate: Optional[datetime] = Field(
        None,
        description="End date range for usage record query. Use yyyy-MM-dd as the date format.",
    )
    domainid: Optional[str] = Field(
        None,
        alias="domainId",
        description="List events for the specified domain.",
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
            return value.strftime("%Y-%m-%d")
        return value


class RemoveRawUsageRecordsRequest(BaseModel):
    interval: int = Field(
        ...,
        description="Specify the number of days (greater than zero) to remove records that are older than those number of days from today.",
    )
