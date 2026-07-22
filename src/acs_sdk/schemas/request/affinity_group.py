# schemas/request/affinity_group.py
from typing import Optional

from pydantic import Field, model_validator

from acs_sdk.schemas.request.base import APIRequest, PaginationMixin


class CreateAffinityGroupRequest(APIRequest):
    name: str = Field(..., description="Name of the affinity group")
    type: str = Field(
        ...,
        description="Type of the affinity group from the available affinity/anti-affinity group types",
    )
    account: Optional[str] = Field(
        None, description="An account for the affinity group. Must be used with domainId."
    )
    description: Optional[str] = Field(
        None, description="Optional description of the affinity group"
    )
    domainid: Optional[str] = Field(
        None, alias="domainId", description="DomainId of the account owning the affinity group"
    )
    projectid: Optional[str] = Field(
        None, alias="projectId", description="Create affinity group for project"
    )


class DeleteAffinityGroupRequest(APIRequest):
    id: Optional[str] = Field(
        None, description="The ID of the affinity group. Mutually exclusive with name parameter"
    )
    name: Optional[str] = Field(
        None, description="The name of the affinity group. Mutually exclusive with ID parameter"
    )
    account: Optional[str] = Field(
        None, description="The account of the affinity group. Must be specified with domain ID"
    )
    domainid: Optional[str] = Field(
        None, alias="domainId", description="The domain ID of account owning the affinity group"
    )
    projectid: Optional[str] = Field(
        None, alias="projectId", description="The project of the affinity group"
    )

    @model_validator(mode="after")
    def validate_identifier(self) -> "DeleteAffinityGroupRequest":
        if self.id and self.name:
            raise ValueError("id and name are mutually exclusive")
        return self


class ListAffinityGroupTypesRequest(APIRequest, PaginationMixin):
    keyword: Optional[str] = Field(None, description="List by keyword")


class ListAffinityGroupsRequest(APIRequest, PaginationMixin):
    account: Optional[str] = Field(
        None, description="List resources by account. Must be used with the domainId parameter."
    )
    domainid: Optional[str] = Field(
        None, alias="domainId", description="List only resources belonging to the domain specified"
    )
    id: Optional[str] = Field(None, description="List the affinity group by the ID provided")
    isrecursive: Optional[bool] = Field(
        False,
        alias="isRecursive",
        description="Defaults to false, but if true, lists all resources from the parent specified by the domainId till leaves.",
    )
    keyword: Optional[str] = Field(None, description="Search by keyword")
    listall: Optional[bool] = Field(
        False,
        alias="listAll",
        description="If set to false, list only resources belonging to the command's caller; if set to true - list resources that the caller is authorized to see.",
    )
    name: Optional[str] = Field(None, description="Lists affinity groups by name")
    projectid: Optional[str] = Field(
        None,
        alias="projectId",
        description="List objects by project; if projectid=-1 lists All VMs",
    )
    type: Optional[str] = Field(None, description="Lists affinity groups by type")
    virtualmachineid: Optional[str] = Field(
        None, alias="virtualMachineId", description="Lists affinity groups by virtual machine ID"
    )


class UpdateVMAffinityGroupRequest(APIRequest):
    id: str = Field(..., description="The ID of the virtual machine")
    affinitygroupids: Optional[str] = Field(
        None,
        alias="affinityGroupIds",
        description="Comma separated list of affinity groups id that are going to be applied to the virtual machine. "
        "Mutually exclusive with affinitygroupnames parameter",
    )
    affinitygroupnames: Optional[str] = Field(
        None,
        alias="affinityGroupNames",
        description="Comma separated list of affinity groups names that are going to be applied to the virtual "
        "machine. Mutually exclusive with affinitygroupids parameter",
    )

    @model_validator(mode="after")
    def validate_identifier(self) -> "UpdateVMAffinityGroupRequest":
        if self.affinitygroupids and self.affinitygroupnames:
            raise ValueError("affinitygroupids and affinitygroupnames are mutually exclusive")
        return self
