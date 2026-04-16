


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


class CreateSecurityGroupRequest(APIRequest):
    name: str = Field(
        ..., description="Name of the security group"
    )
    description: Optional[str] = Field(
        None, description="Description of the security group"
    )


class UpdateSecurityGroupRequest(APIRequest):
    id: str = Field(
        ..., description="The ID of the security group"
    )
    name: Optional[str] = Field(
        None, description="Name of the security group"
    )
    description: Optional[str] = Field(
        None, description="Description of the security group"
    )


class DeleteSecurityGroupRequest(APIRequest):
    id: str = Field(
        ..., description="The ID of the security group"
    )


class AuthorizeSecurityGroupIngressRequest(APIRequest):
    securitygroupid: str = Field(
        ..., alias="securityGroupId", description="The ID of the security group"
    )
    protocol: str = Field(
        ..., description="The protocol for the ingress rule. Valid values are TCP, UDP, ICMP, ALL"
    )
    cidrlist: Optional[str] = Field(
        None, alias="cidrList", description="The CIDR list to allow access from. Multiple entries must be separated by a single comma character (,)."
    )
    startport: Optional[int] = Field(
        None, alias="startPort", description="The starting port of the ingress rule"
    )
    endport: Optional[int] = Field(
        None, alias="endPort", description="The ending port of the ingress rule"
    )
    icmpcode: Optional[int] = Field(
        None, alias="icmpCode", description="Error code for this ICMP message. Only valid if protocol is ICMP"
    )
    icmptype: Optional[int] = Field(
        None, alias="icmpType", description="Type of the ICMP message being sent. Only valid if protocol is ICMP"
    )
    securitygroupname: Optional[str] = Field(
        None, alias="securityGroupName", description="Name of the security group. Either securitygroupname or cidrlist must be specified"
    )
    account: Optional[str] = Field(
        None, description="Account the security group belongs to. Must be used with domainId."
    )
    domainid: Optional[str] = Field(
        None, alias="domainId", description="Domain ID where the security group belongs to"
    )


class AuthorizeSecurityGroupEgressRequest(APIRequest):
    securitygroupid: str = Field(
        ..., alias="securityGroupId", description="The ID of the security group"
    )
    protocol: str = Field(
        ..., description="The protocol for the egress rule. Valid values are TCP, UDP, ICMP, ALL"
    )
    cidrlist: Optional[str] = Field(
        None, alias="cidrList", description="The CIDR list to allow access to. Multiple entries must be separated by a single comma character (,)."
    )
    startport: Optional[int] = Field(
        None, alias="startPort", description="The starting port of the egress rule"
    )
    endport: Optional[int] = Field(
        None, alias="endPort", description="The ending port of the egress rule"
    )
    icmpcode: Optional[int] = Field(
        None, alias="icmpCode", description="Error code for this ICMP message. Only valid if protocol is ICMP"
    )
    icmptype: Optional[int] = Field(
        None, alias="icmpType", description="Type of the ICMP message being sent. Only valid if protocol is ICMP"
    )
    securitygroupname: Optional[str] = Field(
        None, alias="securityGroupName", description="Name of the security group. Either securitygroupname or cidrlist must be specified"
    )
    account: Optional[str] = Field(
        None, description="Account the security group belongs to. Must be used with domainId."
    )
    domainid: Optional[str] = Field(
        None, alias="domainId", description="Domain ID where the security group belongs to"
    )


class RevokeSecurityGroupIngressRequest(APIRequest):
    id: str = Field(
        ..., description="The ID of the ingress rule"
    )


class RevokeSecurityGroupEgressRequest(APIRequest):
    id: str = Field(
        ..., description="The ID of the egress rule"
    )