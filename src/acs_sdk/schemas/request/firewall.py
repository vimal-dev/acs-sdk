from typing import Optional

from pydantic import Field

from acs_sdk.schemas.request.base import APIRequest


class CreateFirewallRuleRequest(APIRequest):
    ipaddressid: str = Field(
        ...,
        alias="ipAddressId",
        description="The public IP address ID for the port forwarding rule",
    )
    protocol: str = Field(
        ..., description="The protocol for the firewall rule. Valid values are TCP, UDP, ICMP, ALL"
    )
    cidrlist: Optional[str] = Field(
        None,
        alias="cidrList",
        description="The CIDR list to allow access from. Multiple entries must be separated by a single comma character (,).",
    )
    startport: Optional[int] = Field(
        None, alias="startPort", description="The starting port of firewall rule"
    )
    endport: Optional[int] = Field(
        None, alias="endPort", description="The ending port of firewall rule"
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


class CreateEgressFirewallRuleRequest(APIRequest):
    networkid: str = Field(
        ..., alias="networkId", description="The network ID for the egress firewall rule"
    )
    protocol: str = Field(
        ...,
        description="The protocol for the egress firewall rule. Valid values are TCP, UDP, ICMP, ALL",
    )
    cidrlist: Optional[str] = Field(
        None,
        alias="cidrList",
        description="The CIDR list to allow access to. Multiple entries must be separated by a single comma character (,).",
    )
    startport: Optional[int] = Field(
        None, alias="startPort", description="The starting port of egress firewall rule"
    )
    endport: Optional[int] = Field(
        None, alias="endPort", description="The ending port of egress firewall rule"
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


class CreateIpv6FirewallRuleRequest(APIRequest):
    ipaddressid: str = Field(
        ..., alias="ipAddressId", description="The IPv6 address ID for the firewall rule"
    )
    protocol: str = Field(
        ...,
        description="The protocol for the IPv6 firewall rule. Valid values are TCP, UDP, ICMP, ALL",
    )
    cidrlist: Optional[str] = Field(
        None,
        alias="cidrList",
        description="The CIDR list to allow access from. Multiple entries must be separated by a single comma character (,).",
    )
    startport: Optional[int] = Field(
        None, alias="startPort", description="The starting port of IPv6 firewall rule"
    )
    endport: Optional[int] = Field(
        None, alias="endPort", description="The ending port of IPv6 firewall rule"
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


class CreatePortForwardingRuleRequest(APIRequest):
    ipaddressid: str = Field(
        ...,
        alias="ipAddressId",
        description="The public IP address ID for the port forwarding rule",
    )
    privateport: int = Field(
        ..., alias="privatePort", description="The starting port of the private IP address"
    )
    protocol: str = Field(
        ..., description="The protocol for the port forwarding rule. Valid values are TCP, UDP"
    )
    publicport: int = Field(
        ..., alias="publicPort", description="The starting port of the public IP address"
    )
    virtualmachineid: str = Field(
        ...,
        alias="virtualMachineId",
        description="The ID of the virtual machine for the port forwarding rule",
    )
    privateendport: Optional[int] = Field(
        None, alias="privateEndPort", description="The ending port of the private IP address"
    )
    publicendport: Optional[int] = Field(
        None, alias="publicEndPort", description="The ending port of the public IP address"
    )
    networkid: Optional[str] = Field(
        None, alias="networkId", description="The network of the virtual machine"
    )
    vmguestip: Optional[str] = Field(
        None,
        alias="vmGuestIp",
        description="VM guest NIC secondary IP address for the port forwarding rule",
    )
    openfirewall: Optional[bool] = Field(
        False,
        alias="openFirewall",
        description="If true, firewall rule for source/end public port is automatically created; if false - firewall rule not created; default is false",
    )


class CreateRoutingFirewallRuleRequest(APIRequest):
    networkid: str = Field(
        ..., alias="networkId", description="The network ID for the routing firewall rule"
    )
    protocol: str = Field(
        ...,
        description="The protocol for the routing firewall rule. Valid values are TCP, UDP, ICMP, ALL",
    )
    cidrlist: Optional[str] = Field(
        None,
        alias="cidrList",
        description="The CIDR list to allow access to. Multiple entries must be separated by a single comma character (,).",
    )
    startport: Optional[int] = Field(
        None, alias="startPort", description="The starting port of routing firewall rule"
    )
    endport: Optional[int] = Field(
        None, alias="endPort", description="The ending port of routing firewall rule"
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


class ListFirewallRulesRequest(APIRequest):
    id: Optional[str] = Field(None, description="Lists firewall rule by ID")
    ipaddressid: Optional[str] = Field(
        None, alias="ipAddressId", description="List firewall rules by IP address ID"
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
    keyword: Optional[str] = Field(None, description="Search keyword")
    listall: Optional[bool] = Field(
        False, alias="listAll", description="List all resources caller is authorized to see"
    )
    projectid: Optional[str] = Field(None, alias="projectId", description="List objects by project")
    tags: Optional[str] = Field(None, description="List resources by tags (key/value pairs)")
    page: Optional[int] = Field(1, ge=1, description="Page number")
    pagesize: Optional[int] = Field(50, ge=1, le=500, description="Number of results per page")


class ListEgressFirewallRulesRequest(APIRequest):
    id: Optional[str] = Field(None, description="Lists egress firewall rule by ID")
    networkid: Optional[str] = Field(
        None, alias="networkId", description="List egress firewall rules by network ID"
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
    keyword: Optional[str] = Field(None, description="Search keyword")
    listall: Optional[bool] = Field(
        False, alias="listAll", description="List all resources caller is authorized to see"
    )
    projectid: Optional[str] = Field(None, alias="projectId", description="List objects by project")
    tags: Optional[str] = Field(None, description="List resources by tags (key/value pairs)")
    page: Optional[int] = Field(1, ge=1, description="Page number")
    pagesize: Optional[int] = Field(50, ge=1, le=500, description="Number of results per page")


class ListIpv6FirewallRulesRequest(APIRequest):
    id: Optional[str] = Field(None, description="Lists IPv6 firewall rule by ID")
    ipaddressid: Optional[str] = Field(
        None, alias="ipAddressId", description="List IPv6 firewall rules by IP address ID"
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
    keyword: Optional[str] = Field(None, description="Search keyword")
    listall: Optional[bool] = Field(
        False, alias="listAll", description="List all resources caller is authorized to see"
    )
    projectid: Optional[str] = Field(None, alias="projectId", description="List objects by project")
    tags: Optional[str] = Field(None, description="List resources by tags (key/value pairs)")
    page: Optional[int] = Field(1, ge=1, description="Page number")
    pagesize: Optional[int] = Field(50, ge=1, le=500, description="Number of results per page")


class ListPortForwardingRulesRequest(APIRequest):
    id: Optional[str] = Field(None, description="Lists port forwarding rule by ID")
    ipaddressid: Optional[str] = Field(
        None, alias="ipAddressId", description="List port forwarding rules by IP address ID"
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
    keyword: Optional[str] = Field(None, description="Search keyword")
    listall: Optional[bool] = Field(
        False, alias="listAll", description="List all resources caller is authorized to see"
    )
    projectid: Optional[str] = Field(None, alias="projectId", description="List objects by project")
    tags: Optional[str] = Field(None, description="List resources by tags (key/value pairs)")
    page: Optional[int] = Field(1, ge=1, description="Page number")
    pagesize: Optional[int] = Field(50, ge=1, le=500, description="Number of results per page")


class ListRoutingFirewallRulesRequest(APIRequest):
    id: Optional[str] = Field(None, description="Lists routing firewall rule by ID")
    networkid: Optional[str] = Field(
        None, alias="networkId", description="List routing firewall rules by network ID"
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
    keyword: Optional[str] = Field(None, description="Search keyword")
    listall: Optional[bool] = Field(
        False, alias="listAll", description="List all resources caller is authorized to see"
    )
    projectid: Optional[str] = Field(None, alias="projectId", description="List objects by project")
    tags: Optional[str] = Field(None, description="List resources by tags (key/value pairs)")
    page: Optional[int] = Field(1, ge=1, description="Page number")
    pagesize: Optional[int] = Field(50, ge=1, le=500, description="Number of results per page")


class UpdateFirewallRuleRequest(APIRequest):
    id: str = Field(..., description="The ID of the firewall rule")
    customid: Optional[str] = Field(
        None,
        alias="customId",
        description="An optional field, in case you want to set a custom id to the resource. Allowed to Root Admins only",
    )
    fordisplay: Optional[bool] = Field(
        None,
        alias="forDisplay",
        description="An optional field, whether to the display the rule to the end user or not",
    )


class UpdateEgressFirewallRuleRequest(APIRequest):
    id: str = Field(..., description="The ID of the egress firewall rule")
    customid: Optional[str] = Field(
        None,
        alias="customId",
        description="An optional field, in case you want to set a custom id to the resource. Allowed to Root Admins only",
    )
    fordisplay: Optional[bool] = Field(
        None,
        alias="forDisplay",
        description="An optional field, whether to the display the rule to the end user or not",
    )


class UpdateIpv6FirewallRuleRequest(APIRequest):
    id: str = Field(..., description="The ID of the IPv6 firewall rule")
    customid: Optional[str] = Field(
        None,
        alias="customId",
        description="An optional field, in case you want to set a custom id to the resource. Allowed to Root Admins only",
    )
    fordisplay: Optional[bool] = Field(
        None,
        alias="forDisplay",
        description="An optional field, whether to the display the rule to the end user or not",
    )


class UpdatePortForwardingRuleRequest(APIRequest):
    id: str = Field(..., description="The ID of the port forwarding rule")
    customid: Optional[str] = Field(
        None,
        alias="customId",
        description="An optional field, in case you want to set a custom id to the resource. Allowed to Root Admins only",
    )
    fordisplay: Optional[bool] = Field(
        None,
        alias="forDisplay",
        description="An optional field, whether to the display the rule to the end user or not",
    )
    privateport: Optional[int] = Field(
        None, alias="privatePort", description="The starting port of the private IP address"
    )
    privateendport: Optional[int] = Field(
        None, alias="privateEndPort", description="The ending port of the private IP address"
    )
    publicport: Optional[int] = Field(
        None, alias="publicPort", description="The starting port of the public IP address"
    )
    publicendport: Optional[int] = Field(
        None, alias="publicEndPort", description="The ending port of the public IP address"
    )
    protocol: Optional[str] = Field(
        None, description="The protocol for the port forwarding rule. Valid values are TCP, UDP"
    )
    virtualmachineid: Optional[str] = Field(
        None,
        alias="virtualMachineId",
        description="The ID of the virtual machine for the port forwarding rule",
    )
    vmguestip: Optional[str] = Field(
        None,
        alias="vmGuestIp",
        description="VM guest NIC secondary IP address for the port forwarding rule",
    )


class UpdateRoutingFirewallRuleRequest(APIRequest):
    id: str = Field(..., description="The ID of the routing firewall rule")
    customid: Optional[str] = Field(
        None,
        alias="customId",
        description="An optional field, in case you want to set a custom id to the resource. Allowed to Root Admins only",
    )
    fordisplay: Optional[bool] = Field(
        None,
        alias="forDisplay",
        description="An optional field, whether to the display the rule to the end user or not",
    )


class DeleteFirewallRuleRequest(APIRequest):
    id: str = Field(..., description="The ID of the firewall rule")


class DeleteEgressFirewallRuleRequest(APIRequest):
    id: str = Field(..., description="The ID of the egress firewall rule")


class DeleteIpv6FirewallRuleRequest(APIRequest):
    id: str = Field(..., description="The ID of the IPv6 firewall rule")


class DeletePortForwardingRuleRequest(APIRequest):
    id: str = Field(..., description="The ID of the port forwarding rule")


class DeleteRoutingFirewallRuleRequest(APIRequest):
    id: str = Field(..., description="The ID of the routing firewall rule")
