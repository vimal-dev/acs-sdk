
from pydantic import Field, model_validator
from typing import Optional
from datetime import datetime

from acs_sdk.schemas.request.base import APIRequest


class ListAsyncJobsRequest(APIRequest):
    account: Optional[str] = Field(
        None, description="List resources by account (requires domainid)"
    )
    domainid: Optional[str] = Field(
        None, alias="domainId", description="Filter by domain ID"
    )
    isrecursive: Optional[bool] = Field(
        False, alias="isRecursive", description="Include subdomains recursively"
    )
    keyword: Optional[str] = Field(
        None, description="Search keyword"
    )
    listall: Optional[bool] = Field(
        False,
        alias="listAll",
        description="List all resources caller is authorized to see"
    )
    managementserverid: Optional[int] = Field(
        None, alias="managementServerId", description="Management server ID"
    )
    page: Optional[int] = Field(
        1, ge=1, description="Page number"
    )
    pagesize: Optional[int] = Field(
        50, ge=1, le=500, description="Number of results per page"
    )
    startdate: Optional[datetime] = Field(
        None,
        alias="startDate",
        description="Start date of async job (ISO format)"
    )

    @model_validator(mode="after")
    def validate_account_domain_dependency(self):
        if self.account and not self.domainid:
            raise ValueError("domainid is required when account is provided")
        return self


class QueryAsyncJobRequest(APIRequest):
    jobid: str = Field(
        ...,
        alias="jobId",
        description="The ID of the asynchronous job to query.",
    )