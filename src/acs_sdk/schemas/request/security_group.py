


from typing import Optional

from pydantic import Field

from acs_sdk.schemas.request.base import APIRequest


class ListSecurityGroupRequest(APIRequest):
    id: Optional[str] = Field(
        None, description="List security groups by ID"
    )
    account: Optional[str] = Field(
        None, description="List security groups by account. Must be used with domainId."
    )
    domainid: Optional[str] = Field(
        None, alias="domainId", description="List only resources belonging to the domain specified"
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
    projectid: Optional[str] = Field(
        None, alias="projectId", description="List objects by project; if projectid=-1 lists All VMs"
    )
    securitygroupname: Optional[str] = Field(
        None, alias="securityGroupName", description="List security groups by name"
    )
    tags:Optional[str] = Field(
        None, description="List security groups by tags (key/value pairs)"
    )
    page: Optional[int] = Field(
        1, ge=1, description="Page number"
    )
    pagesize: Optional[int] = Field(
        50, ge=1, le=500, description="Number of results per page"
    )