from pydantic import Field
from typing import Optional
from .base import APIRequest, PaginationMixin


class ListNetworkOfferingRequest(APIRequest, PaginationMixin):

    # Basic filters
    id: Optional[str] = Field(None, description="List network offerings by ID")
    name: Optional[str] = Field(None, description="List network offerings by name")
    keyword: Optional[str] = Field(None, description="List by keyword")
    displaytext: Optional[str] = Field(None, description="List network offerings by display text")

    # Network type and configuration
    forvpc: Optional[bool] = Field(
        None,
        description="The network offering can be used only for network creation inside the VPC"
    )

    guestiptype: Optional[str] = Field(
        None,
        alias="guestIpType",
        description="List network offerings by guest type: shared or isolated"
    )

    availability: Optional[str] = Field(
        None,
        description="The availability of network offering. Default value is required"
    )

    isdefault: Optional[bool] = Field(
        None,
        alias="isDefault",
        description="True if need to list only default network offerings. Default value is false"
    )

    istagged: Optional[bool] = Field(
        None,
        alias="isTagged",
        description="True if offering has tags specified"
    )

    # Network and zone availability
    networkid: Optional[str] = Field(
        None,
        alias="networkId",
        description="The ID of the network. Pass this in if you want to see the available network offering that a network can be changed to"
    )

    zoneid: Optional[str] = Field(
        None,
        alias="zoneId",
        description="List network offerings available for network creation in specific zone"
    )

    domainid: Optional[str] = Field(
        None,
        alias="domainId",
        description="List network offerings available for network creation in specific domain"
    )

    # Routing and services
    routingmode: Optional[str] = Field(
        None,
        alias="routingMode",
        description="The routing mode for the network offering. Supported types are: Static or Dynamic"
    )

    sourcenatsupported: Optional[bool] = Field(
        None,
        alias="sourceNatSupported",
        description="True if need to list only network offerings where source NAT is supported, false otherwise"
    )

    specifyipranges: Optional[bool] = Field(
        None,
        alias="specifyIpRanges",
        description="True if need to list only network offerings which support specifying ip ranges"
    )

    specifyvlan: Optional[str] = Field(
        None,
        alias="specifyVlan",
        description="The tags for the network offering"
    )

    state: Optional[str] = Field(
        None,
        description="List network offerings by state"
    )

    supportedservices: Optional[str] = Field(
        None,
        alias="supportedServices",
        description="List network offerings supporting certain services"
    )

    tags: Optional[str] = Field(
        None,
        description="List network offerings by tags"
    )

    traffictype: Optional[str] = Field(
        None,
        alias="trafficType",
        description="List by traffic type"
    )