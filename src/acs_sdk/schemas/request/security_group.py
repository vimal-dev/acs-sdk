from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field, model_validator

from acs_sdk.schemas.request.base import APIRequest, PaginationMixin


class UserSecurityGroupEntry(BaseModel):
    """One entry in usersecuritygrouplist[]"""

    account: str = Field(..., description="Account owning the security group")
    group: str = Field(..., description="Name of the security group")


def _flatten_user_security_group_list(data: Dict[str, Any]) -> Dict[str, Any]:
    entries = data.pop("usersecuritygrouplist", None)
    if not entries:
        return data
    for idx, entry in enumerate(entries):
        data[f"usersecuritygrouplist[{idx}].account"] = entry["account"]
        data[f"usersecuritygrouplist[{idx}].group"] = entry["group"]
    return data


class ListSecurityGroupRequest(APIRequest, PaginationMixin):
    id: Optional[str] = Field(None, description="List security groups by ID")
    account: Optional[str] = Field(
        None, description="List security groups by account. Must be used with domainId."
    )
    domainid: Optional[str] = Field(
        None, alias="domainId", description="List only resources belonging to the domain specified"
    )
    isrecursive: Optional[bool] = Field(
        False, alias="isRecursive", description="Include subdomains recursively"
    )
    keyword: Optional[str] = Field(None, description="Search keyword")
    listall: Optional[bool] = Field(
        False, alias="listAll", description="List all resources caller is authorized to see"
    )
    projectid: Optional[str] = Field(
        None,
        alias="projectId",
        description="List objects by project; if projectid=-1 lists All VMs",
    )
    securitygroupname: Optional[str] = Field(
        None, alias="securityGroupName", description="List security groups by name"
    )
    tags: Optional[str] = Field(None, description="List security groups by tags (key/value pairs)")
    virtualmachineid: Optional[str] = Field(
        None, alias="virtualMachineId", description="Lists security groups by virtual machine ID"
    )


class CreateSecurityGroupRequest(APIRequest):
    name: str = Field(..., description="Name of the security group")
    description: Optional[str] = Field(None, description="Description of the security group")
    account: Optional[str] = Field(
        None, description="An optional account for the security group. Must be used with domainId."
    )
    domainid: Optional[str] = Field(
        None, alias="domainId", description="An optional domainId for the security group."
    )
    projectid: Optional[str] = Field(
        None, alias="projectId", description="Create security group for project"
    )


class UpdateSecurityGroupRequest(APIRequest):
    id: str = Field(..., description="The ID of the security group")
    name: Optional[str] = Field(None, description="The new name of the security group")
    customid: Optional[str] = Field(
        None,
        alias="customId",
        description="An optional field, in case you want to set a custom id to the resource. Allowed to Root Admins only",
    )


class DeleteSecurityGroupRequest(APIRequest):
    id: Optional[str] = Field(
        None, description="The ID of the security group. Mutually exclusive with name parameter"
    )
    name: Optional[str] = Field(
        None, description="The name of the security group. Mutually exclusive with id parameter"
    )
    account: Optional[str] = Field(
        None, description="The account of the security group. Must be specified with domain ID"
    )
    domainid: Optional[str] = Field(
        None, alias="domainId", description="The domain ID of account owning the security group"
    )
    projectid: Optional[str] = Field(
        None, alias="projectId", description="The project of the security group"
    )

    @model_validator(mode="after")
    def validate_identifier(self) -> "DeleteSecurityGroupRequest":
        if self.id and self.name:
            raise ValueError("id and name are mutually exclusive")
        return self


class AuthorizeSecurityGroupIngressRequest(APIRequest):
    securitygroupid: Optional[str] = Field(
        None,
        alias="securityGroupId",
        description="The ID of the security group. Mutually exclusive with securitygroupname parameter",
    )
    securitygroupname: Optional[str] = Field(
        None,
        alias="securityGroupName",
        description="The name of the security group. Mutually exclusive with securitygroupid parameter",
    )
    protocol: Optional[str] = Field(
        None,
        description="The protocol for the ACL rule. Valid values are TCP/UDP/ICMP/ALL or a valid protocol number. ALL is default.",
    )
    cidrlist: Optional[str] = Field(
        None,
        alias="cidrList",
        description="The CIDR list to allow access from. Multiple entries must be separated by a single comma character (,).",
    )
    startport: Optional[int] = Field(
        None, alias="startPort", description="The starting port of the ingress rule"
    )
    endport: Optional[int] = Field(
        None, alias="endPort", description="The ending port of the ingress rule"
    )
    icmpcode: Optional[int] = Field(
        None,
        alias="icmpCode",
        description="Error code for this ICMP message. Only valid if protocol is ICMP",
    )
    icmptype: Optional[int] = Field(
        None,
        alias="icmpType",
        description="Type of the ICMP message being sent. Only valid if protocol is ICMP",
    )
    account: Optional[str] = Field(
        None, description="Account the security group belongs to. Must be used with domainId."
    )
    domainid: Optional[str] = Field(
        None, alias="domainId", description="Domain ID where the security group belongs to"
    )
    projectid: Optional[str] = Field(
        None, alias="projectId", description="An optional project of the security group"
    )
    usersecuritygrouplist: Optional[List[UserSecurityGroupEntry]] = Field(
        None, alias="userSecurityGroupList", description="User to security group mapping"
    )

    @model_validator(mode="after")
    def validate_identifier(self) -> "AuthorizeSecurityGroupIngressRequest":
        if self.securitygroupid and self.securitygroupname:
            raise ValueError("securitygroupid and securitygroupname are mutually exclusive")
        return self

    def model_dump(self, *args, **kwargs) -> Dict[str, Any]:
        data = super().model_dump(*args, **kwargs)
        return _flatten_user_security_group_list(data)


class AuthorizeSecurityGroupEgressRequest(APIRequest):
    securitygroupid: Optional[str] = Field(
        None,
        alias="securityGroupId",
        description="The ID of the security group. Mutually exclusive with securitygroupname parameter",
    )
    securitygroupname: Optional[str] = Field(
        None,
        alias="securityGroupName",
        description="The name of the security group. Mutually exclusive with securitygroupid parameter",
    )
    protocol: Optional[str] = Field(
        None, description="TCP is default. UDP is the other supported protocol"
    )
    cidrlist: Optional[str] = Field(
        None,
        alias="cidrList",
        description="The CIDR list to allow access to. Multiple entries must be separated by a single comma character (,).",
    )
    startport: Optional[int] = Field(
        None, alias="startPort", description="The starting port of the egress rule"
    )
    endport: Optional[int] = Field(
        None, alias="endPort", description="The ending port of the egress rule"
    )
    icmpcode: Optional[int] = Field(
        None,
        alias="icmpCode",
        description="Error code for this ICMP message. Only valid if protocol is ICMP",
    )
    icmptype: Optional[int] = Field(
        None,
        alias="icmpType",
        description="Type of the ICMP message being sent. Only valid if protocol is ICMP",
    )
    account: Optional[str] = Field(
        None, description="Account the security group belongs to. Must be used with domainId."
    )
    domainid: Optional[str] = Field(
        None, alias="domainId", description="Domain ID where the security group belongs to"
    )
    projectid: Optional[str] = Field(
        None, alias="projectId", description="An optional project of the security group"
    )
    usersecuritygrouplist: Optional[List[UserSecurityGroupEntry]] = Field(
        None, alias="userSecurityGroupList", description="User to security group mapping"
    )

    @model_validator(mode="after")
    def validate_identifier(self) -> "AuthorizeSecurityGroupEgressRequest":
        if self.securitygroupid and self.securitygroupname:
            raise ValueError("securitygroupid and securitygroupname are mutually exclusive")
        return self

    def model_dump(self, *args, **kwargs) -> Dict[str, Any]:
        data = super().model_dump(*args, **kwargs)
        return _flatten_user_security_group_list(data)


class RevokeSecurityGroupIngressRequest(APIRequest):
    id: str = Field(..., description="The ID of the ingress rule")


class RevokeSecurityGroupEgressRequest(APIRequest):
    id: str = Field(..., description="The ID of the egress rule")
