from typing import Optional

from pydantic import Field

from acs_sdk.schemas.request.base import APIRequest


class ListIpForwardingRulesRequest(APIRequest):
    id: Optional[str] = Field(
        None, description="Lists IP forwarding rule by ID"
    )
    ipaddressid: Optional[str] = Field(
        None, alias="ipAddressId", description="List IP forwarding rules by IP address ID"
    )
    account: Optional[str] = Field(
        None, description="List resources by account. Must be used with the domainId parameter."
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
        None, alias="projectId", description="List objects by project"
    )
    tags: Optional[str] = Field(
        None, description="List resources by tags (key/value pairs)"
    )
    page: Optional[int] = Field(
        1, ge=1, description="Page number"
    )
    pagesize: Optional[int] = Field(
        50, ge=1, le=500, description="Number of results per page"
    )


class CreateIpForwardingRuleRequest(APIRequest):
    ipaddressid: str = Field(
        ..., alias="ipAddressId", description="The public IP address ID for the forwarding rule"
    )
    protocol: str = Field(
        ..., description="The protocol for the forwarding rule. Valid values are TCP, UDP, ICMP"
    )
    startport: int = Field(
        ..., alias="startPort", description="The starting port of the rule"
    )
    endport: Optional[int] = Field(
        None, alias="endPort", description="The ending port of the rule"
    )
    openfirewall: Optional[bool] = Field(
        False, alias="openFirewall", description="If true, firewall rule for source/end public port is automatically created; if false - firewall rule not created; default is false"
    )


class DeleteIpForwardingRuleRequest(APIRequest):
    id: str = Field(
        ..., description="The ID of the forwarding rule"
    )


class EnableStaticNatRequest(APIRequest):
    ipaddressid: str = Field(
        ..., alias="ipAddressId", description="The public IP address ID for which static NAT will be enabled"
    )
    virtualmachineid: str = Field(
        ..., alias="virtualMachineId", description="The ID of the virtual machine for static NAT"
    )
    networkid: Optional[str] = Field(
        None, alias="networkId", description="The network of the virtual machine"
    )
    vmguestip: Optional[str] = Field(
        None, alias="vmGuestIp", description="VM guest NIC secondary IP address for the static NAT rule"
    )


class DisableStaticNatRequest(APIRequest):
    ipaddressid: str = Field(
        ..., alias="ipAddressId", description="The public IP address ID for which static NAT will be disabled"
    )