# schemas/request/instance_group.py
from typing import Optional

from pydantic import Field

from acs_sdk.schemas.request.base import APIRequest, PaginationMixin


class CreateInstanceGroupRequest(APIRequest):
    name: str = Field(..., description="The name of the instance group")
    account: Optional[str] = Field(
        None, description="The account of the instance group. Must be used with domainId."
    )
    domainid: Optional[str] = Field(
        None, alias="domainId", description="The domain ID of account owning the instance group"
    )
    projectid: Optional[str] = Field(
        None, alias="projectId", description="The project of the instance group"
    )


class UpdateInstanceGroupRequest(APIRequest):
    id: str = Field(..., description="Instance group ID")
    name: Optional[str] = Field(None, description="New instance group name")


class DeleteInstanceGroupRequest(APIRequest):
    id: str = Field(..., description="The ID of the instance group")


class ListInstanceGroupsRequest(APIRequest, PaginationMixin):
    account: Optional[str] = Field(
        None, description="List resources by account. Must be used with the domainId parameter."
    )
    domainid: Optional[str] = Field(
        None, alias="domainId", description="List only resources belonging to the domain specified"
    )
    id: Optional[str] = Field(None, description="List instance groups by ID")
    isrecursive: Optional[bool] = Field(
        False,
        alias="isRecursive",
        description="Defaults to false, but if true, lists all resources from the parent specified by the domainId till leaves.",
    )
    keyword: Optional[str] = Field(None, description="List by keyword")
    listall: Optional[bool] = Field(
        False,
        alias="listAll",
        description="If set to false, list only resources belonging to the command's caller; if set to true - list resources that the caller is authorized to see.",
    )
    name: Optional[str] = Field(None, description="List instance groups by name")
    projectid: Optional[str] = Field(
        None,
        alias="projectId",
        description="List objects by project; if projectid=-1 lists All VMs",
    )
