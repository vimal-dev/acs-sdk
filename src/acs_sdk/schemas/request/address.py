from typing import Optional

from pydantic import Field, model_validator

from acs_sdk.schemas.request.base import APIRequest, PaginationMixin


class ListPublicIpAddressesRequest(APIRequest, PaginationMixin):
    id: Optional[str] = Field(None, description="List IP address by ID")
    ipaddress: Optional[str] = Field(
        None, alias="ipAddress", description="List IP address by IP address"
    )
    account: Optional[str] = Field(
        None, description="List resources by account. Must be used with the domainId parameter."
    )
    allocatedonly: Optional[bool] = Field(
        False, alias="allocatedOnly", description="Limits the search to allocated IP addresses"
    )
    associatednetworkid: Optional[str] = Field(
        None, alias="associatedNetworkId", description="List IP addresses by associated network ID"
    )
    domainid: Optional[str] = Field(
        None, alias="domainId", description="List only resources belonging to the domain specified"
    )
    fordisplay: Optional[bool] = Field(
        None,
        alias="forDisplay",
        description="list resources by display flag; only ROOT admin is eligible to pass this parameter.",
    )
    forloadbalancing: Optional[bool] = Field(
        None,
        alias="forLoadBalancing",
        description="List only IPs used for load balancing",
    )
    forprovider: Optional[bool] = Field(
        None,
        alias="forProvider",
        description="True if range is dedicated for external network provider",
    )
    forsystemvms: Optional[bool] = Field(
        None,
        alias="forSystemVMs",
        description="true if range is dedicated for system VMs",
    )
    forvirtualnetwork: Optional[bool] = Field(
        None,
        alias="forVirtualNetwork",
        description="List only IPs used for virtual network",
    )
    ipaddress: Optional[str] = Field(
        None, alias="ipAddress", description="List IP address by IP address"
    )
    isrecursive: Optional[bool] = Field(
        False, alias="isRecursive", description="Include subdomains recursively"
    )
    issourcenat: Optional[bool] = Field(
        None,
        alias="isSourceNat",
        description="List only source NAT IP addresses. If false, list only non-source NAT IP",
    )
    isstaticnat: Optional[bool] = Field(
        None,
        alias="isStaticNat",
        description="List only static NAT IP addresses. If false, list only non-static NAT IPs",
    )
    keyword: Optional[str] = Field(None, description="Search keyword")
    listall: Optional[bool] = Field(
        False, alias="listAll", description="List all resources caller is authorized to see"
    )
    networkid: Optional[str] = Field(
        None, alias="networkId", description="List IP addresses by network ID"
    )
    physicalnetworkid: Optional[str] = Field(
        None, alias="physicalNetworkId", description="List IP addresses by physical network ID"
    )
    projectid: Optional[str] = Field(None, alias="projectId", description="List objects by project")
    retrieveonlyresourcecount: Optional[bool] = Field(
        False,
        alias="retrieveOnlyResourceCount",
        description="If true, lists resource count instead of the resources themselves",
    )
    state: Optional[str] = Field(None, description="List IP addresses by state")
    tags: Optional[str] = Field(None, description="List resources by tags (key/value pairs)")
    vlanid: Optional[str] = Field(None, alias="vlanId", description="List IP addresses by VLAN ID")
    vpcid: Optional[str] = Field(None, alias="vpcId", description="List IP addresses by VPC ID")
    zoneid: Optional[str] = Field(None, alias="zoneId", description="List IP addresses by zone ID")


class AssociateIpAddressRequest(APIRequest):
    """Request to associate an IP address to a network."""

    account: Optional[str] = Field(None, description="The account that will own the IP")
    domainid: Optional[str] = Field(None, alias="domainId", description="The domain ID")
    fordisplay: Optional[bool] = Field(
        None,
        alias="forDisplay",
        description="an optional field, whether to the display the IP to the end user or not.",
    )
    ipaddress: Optional[str] = Field(
        None, alias="ipAddress", description="IP Address to be associated"
    )
    isportable: Optional[bool] = Field(
        None,
        alias="isPortable",
        description="should be set to true if public IP is required to be transferable across zones, if not specified defaults to false",
    )
    networkid: Optional[str] = Field(
        None, alias="networkId", description="The network this IP address should be associated to."
    )
    projectid: Optional[str] = Field(
        None, alias="projectId", description="Deploy VM for the project"
    )
    regionid: Optional[str] = Field(
        None,
        alias="regionId",
        description="The region ID from where portable IP is to be associated.",
    )
    vpcid: Optional[str] = Field(
        None, alias="vpcId", description="The VPC you want the IP address to be associated with"
    )
    zoneid: Optional[str] = Field(
        None,
        alias="zoneId",
        description="The ID of the availability zone you want to acquire an public IP address from",
    )


class DisassociateIpAddressRequest(APIRequest):
    """Request to disassociate an IP address."""

    id: str = Field(
        ...,
        description="The ID of the public IP address to disassociate. Mutually exclusive with the ipaddress parameter",
    )
    ipaddress: Optional[str] = Field(
        None,
        alias="ipAddress",
        description="IP Address to be disassociated. Mutually exclusive with the id parameter",
    )

    @model_validator(mode="after")
    def validate_mutually_exclusive(self):
        if self.id and self.ipaddress:
            raise ValueError("id and ipaddress are mutually exclusive")

        if not self.id and not self.ipaddress:
            raise ValueError("either id or ipaddress must be provided")

        return self


class UpdateIpAddressRequest(APIRequest):
    id: str = Field(..., description="The ID of the public IP address")
    customid: Optional[str] = Field(
        None,
        alias="customId",
        description="An optional field, in case you want to set a custom id to the resource. Allowed to Root Admins only",
    )
    fordisplay: Optional[bool] = Field(
        None,
        alias="forDisplay",
        description="An optional field, whether to the display the IP address to the end user or not",
    )


class ReleaseIpAddressRequest(APIRequest):
    id: str = Field(..., description="The ID of the public IP address to release")


class ReserveIpAddressRequest(APIRequest):
    id: str = Field(..., description="The ID of the public IP address to release")
    account: Optional[str] = Field(None, description="The account to reserve with this IP address")
    domainid: Optional[str] = Field(
        None, alias="domainId", description="The ID of the domain to reserve with this IP address"
    )
    fordisplay: Optional[bool] = Field(
        None,
        alias="forDisplay",
        description="an optional field, whether to the display the IP to the end user or not.",
    )
    projectid: Optional[str] = Field(
        None, alias="projectId", description="The ID of the project to reserve with this IP address"
    )


class AcquirePodIpAddressRequest(APIRequest):
    zoneid: Optional[str] = Field(
        None,
        alias="zoneId",
        description="The ID of the availability zone you want to acquire an public IP address from",
    )
    podid: Optional[str] = Field(
        None, alias="podId", description="The ID of the pod to acquire the IP address in"
    )


class ReleasePodIpAddressRequest(APIRequest):
    id: str = Field(..., description="The ID of the pod IP address")
