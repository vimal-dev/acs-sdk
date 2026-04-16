from typing import Optional

from pydantic import Field

from acs_sdk.schemas.request.base import APIRequest


class ListPublicIpAddressesRequest(APIRequest):
    id: Optional[str] = Field(
        None, description="List IP address by ID"
    )
    ipaddress: Optional[str] = Field(
        None, alias="ipAddress", description="List IP address by IP address"
    )
    allocatedonly: Optional[bool] = Field(
        False, alias="allocatedOnly", description="Limits the search to allocated IP addresses"
    )
    associatednetworkid: Optional[str] = Field(
        None, alias="associatedNetworkId", description="List IP addresses by associated network ID"
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
    vpcid: Optional[str] = Field(
        None, alias="vpcId", description="List IP addresses by VPC ID"
    )
    zoneid: Optional[str] = Field(
        None, alias="zoneId", description="List IP addresses by zone ID"
    )
    page: Optional[int] = Field(
        1, ge=1, description="Page number"
    )
    pagesize: Optional[int] = Field(
        50, ge=1, le=500, description="Number of results per page"
    )


class AssociateIpAddressRequest(APIRequest):
    networkid: Optional[str] = Field(
        None, alias="networkId", description="The ID of the network to associate the IP address with"
    )
    zoneid: Optional[str] = Field(
        None, alias="zoneId", description="The ID of the zone to associate the IP address with"
    )


class DisassociateIpAddressRequest(APIRequest):
    id: str = Field(
        ..., description="The ID of the public IP address"
    )


class UpdateIpAddressRequest(APIRequest):
    id: str = Field(
        ..., description="The ID of the public IP address"
    )
    customid: Optional[str] = Field(
        None, alias="customId", description="An optional field, in case you want to set a custom id to the resource. Allowed to Root Admins only"
    )
    fordisplay: Optional[bool] = Field(
        None, alias="forDisplay", description="An optional field, whether to the display the IP address to the end user or not"
    )


class ReleaseIpAddressRequest(APIRequest):
    id: str = Field(
        ..., description="The ID of the public IP address"
    )


class ReserveIpAddressRequest(APIRequest):
    networkid: str = Field(
        ..., alias="networkId", description="The network ID of the network to reserve the IP address in"
    )


class AcquirePodIpAddressRequest(APIRequest):
    podid: str = Field(
        ..., alias="podId", description="The ID of the pod to acquire the IP address in"
    )


class ReleasePodIpAddressRequest(APIRequest):
    id: str = Field(
        ..., description="The ID of the pod IP address"
    )