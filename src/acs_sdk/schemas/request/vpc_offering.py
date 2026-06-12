from typing import Optional
from pydantic import Field
from acs_sdk.schemas.request.base import APIRequest, PaginationMixin


class CreateVPCOfferingRequest(APIRequest):
    """Request parameters for ``createVPCOffering``. Asynchronous.

    Reference: https://cloudstack.apache.org/api/apidocs-4.22/apis/createVPCOffering.html
    """

    # --- required -----------------------------------------------------------

    name: str = Field(..., description="The name of the VPC offering")

    # --- optional -----------------------------------------------------------

    displaytext: Optional[str] = Field(
        None, alias="displayText", description="The display text of the VPC offering, defaults to 'name'"
    )
    domainid: Optional[str] = Field(
        None, alias="domainId", description="ID of the containing domain(s); null for public offerings"
    )
    zoneid: Optional[str] = Field(
        None, alias="zoneId", description="ID of the containing zone(s); null for public offerings"
    )
    enable: Optional[bool] = Field(
        None, description="Set to true to enable the offering during creation. Default is false"
    )
    supportedservices: Optional[str] = Field(
        None, alias="supportedServices", description="Comma-separated services supported by the VPC offering"
    )
    serviceofferingid: Optional[str] = Field(
        None, alias="serviceOfferingId", description="ID of the service offering for the VPC router appliance"
    )
    serviceproviderlist: Optional[str] = Field(
        None, alias="serviceProviderList", description="Provider-to-service mapping; defaults to the default provider"
    )
    servicecapabilitylist: Optional[str] = Field(
        None, alias="serviceCapabilityList", description="Desired service capabilities as part of the VPC offering"
    )
    provider: Optional[str] = Field(None, description="Name of the provider supplying the service")
    routingmode: Optional[str] = Field(
        None, alias="routingMode", description="Routing mode for the VPC offering: 'Static' or 'Dynamic'"
    )
    networkmode: Optional[str] = Field(
        None, alias="networkMode", description="Network operation mode: 'NATTED' or 'ROUTED'"
    )
    internetprotocol: Optional[str] = Field(
        None, alias="internetProtocol", description="Internet protocol: 'ipv4' (default) or 'dualstack'"
    )
    fornsx: Optional[bool] = Field(
        None, alias="forNsx", description="True if the offering is for NSX, false otherwise"
    )
    nsxsupportlb: Optional[bool] = Field(
        None, alias="nsxSupportLb", description="True if the NSX VPC offering supports load balancer service"
    )
    specifyasnumber: Optional[bool] = Field(
        None, alias="specifyAsNumber", description="True if the VPC offering supports choosing an AS number"
    )


class DeleteVPCOfferingRequest(APIRequest):
    """Request parameters for ``deleteVPCOffering``. Asynchronous.

    Reference: https://cloudstack.apache.org/api/apidocs-4.22/apis/deleteVPCOffering.html
    """

    id: str = Field(..., description="The ID of the VPC offering to delete")


class UpdateVPCOfferingRequest(APIRequest):
    """Request parameters for ``updateVPCOffering``. Asynchronous.

    Reference: https://cloudstack.apache.org/api/apidocs-4.22/apis/updateVPCOffering.html
    """

    # --- required -----------------------------------------------------------

    id: str = Field(..., description="The ID of the VPC offering to update")

    # --- optional -----------------------------------------------------------

    name: Optional[str] = Field(None, description="New name for the VPC offering")
    displaytext: Optional[str] = Field(
        None, alias="displayText", description="New display text for the VPC offering"
    )
    domainid: Optional[str] = Field(
        None, alias="domainId", description="Containing domain ID(s) as comma-separated string; 'public' for public offerings"
    )
    zoneid: Optional[str] = Field(
        None, alias="zoneId", description="Containing zone ID(s) as comma-separated string; 'all' for all zones"
    )
    state: Optional[str] = Field(None, description="New state for the VPC offering: 'Enabled' or 'Disabled'")
    sortkey: Optional[int] = Field(None, alias="sortKey", description="Sort key of the VPC offering")


class ListVPCOfferingRequest(APIRequest, PaginationMixin):
    """Request schema for listing VPC offerings."""

    id: Optional[str] = Field(None, description="The ID of the VPC offering.")
    name: Optional[str] = Field(None, description="The name of the VPC offering.")
    displaytext: Optional[str] = Field(
        None, alias="displayText", description="The display text of the VPC offering."
    )
    domainid: Optional[str] = Field(
        None, alias="domainId", description="The domain ID of the VPC offering."
    )
    state: Optional[str] = Field(None, description="The state of the VPC offering.")
    isdefault: Optional[bool] = Field(
        None, alias="isDefault", description="Whether the VPC offering is default."
    )
    issystem: Optional[bool] = Field(
        None, alias="isSystem", description="Whether the VPC offering is system."
    )
    keyword: Optional[str] = Field(None, description="List by keyword.")
    supportedservices: Optional[str] = Field(
        None, alias="supportedServices", description="The supported services of the VPC offering."
    )
    zoneid: Optional[str] = Field(
        None, alias="zoneId", description="The zone ID of the VPC offering."
    )
