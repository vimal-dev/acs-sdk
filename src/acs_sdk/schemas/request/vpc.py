from typing import List, Optional
from pydantic import BaseModel, Field, model_validator
from acs_sdk.schemas.request.base import APIRequest, PaginationMixin


class CreatePrivateGatewayRequest(APIRequest):
    vpcid: Optional[str] = Field(None, alias="vpcId", description="VPC ID")
    gateway: str = Field(..., description="The gateway of the Private gateway")
    ipaddress: str = Field(..., description="The IP address of the Private gateaway")
    netmask: str = Field(..., description="The netmask of the Private gateway")


class CreateStaticRouteRequest(APIRequest):
    cidr: str = Field(..., description="Static route CIDR")
    vpcid: Optional[str] = Field(None, alias="vpcId", description="VPC ID")
    gatewayid: Optional[str] = Field(
        None,
        alias="gatewayId",
        description="The gateway id we are creating static route for. Mutually exclusive with the nexthop parameter",
    )
    nexthop: Optional[str] = Field(
        None,
        alias="nextHop",
        description="The next hop of static route. Mutually exclusive with the gatewayid parameter",
    )

    @model_validator(mode="after")
    def validate_model_dependency(self):
        if self.gatewayid and self.nexthop:
            raise ValueError("Gateway ID and Next hop are mutually exclusive")


class CreateVPCRequest(APIRequest):
    # Required fields
    name: str = Field(..., description="Name of the VPC")
    vpcofferingid: str = Field(..., description="ID of the VPC offering")
    zoneid: str = Field(..., description="Zone ID")

    # CIDR (depends on version / mode)
    cidr: Optional[str] = Field(None, description="CIDR of the VPC (required in most setups)")
    cidrsize: Optional[int] = Field(None, description="CIDR size (used in routed mode VPCs)")

    # Metadata
    displaytext: Optional[str] = Field(
        None, description="Display text of the VPC (defaults to name)"
    )

    networkdomain: Optional[str] = Field(None, description="Network domain for the VPC")

    # Account / Domain / Project
    account: Optional[str] = Field(
        None, description="Account associated with the VPC (requires domainid)"
    )
    domainid: Optional[str] = Field(None, description="Domain ID")
    projectid: Optional[str] = Field(None, description="Project ID")

    # Visibility
    fordisplay: Optional[bool] = Field(None, description="Whether VPC is visible to end users")

    # DNS
    dns1: Optional[str] = Field(None, description="Primary IPv4 DNS")
    dns2: Optional[str] = Field(None, description="Secondary IPv4 DNS")
    ip6dns1: Optional[str] = Field(None, description="Primary IPv6 DNS")
    ip6dns2: Optional[str] = Field(None, description="Secondary IPv6 DNS")

    # Advanced networking
    publicmtu: Optional[int] = Field(None, description="MTU for public interfaces")

    sourcenatipaddress: Optional[str] = Field(
        None, description="Custom source NAT IP for VPC router"
    )

    userouteripresolver: Optional[bool] = Field(None, description="Use router IP as DNS resolver")

    # BGP / routing (advanced setups)
    asnumber: Optional[int] = Field(None, description="AS number for VPC tiers")

    bgppeerids: Optional[List[str]] = Field(None, description="List of BGP peer IDs")

    # Lifecycle
    start: Optional[bool] = Field(None, description="Start VPC immediately (default: True)")


class DeletePrivateGatewayRequest(APIRequest):
    id: str = Field(..., description="ID of the Private Gateway to delete")


class DeleteStaticRouteRequest(APIRequest):
    id: str = Field(..., description="ID of the Static Route to delete")


class DeleteVPCRequest(APIRequest):
    id: str = Field(..., description="ID of the VPC to delete")


class ListVPCRequest(APIRequest, PaginationMixin):
    id: Optional[str] = Field(None, description="List VPC by ID")
    name: Optional[str] = Field(None, description="List VPC by name")
    keyword: Optional[str] = Field(None, description="List VPC by keyword")
    cidr: Optional[str] = Field(None, description="List VPC by CIDR")
    displaytext: Optional[str] = Field(
        None, alias="displayText", description="List VPC by Display text"
    )

    tags: Optional[str] = Field(None, description="List VPCs by tags (key/value pairs)")

    listall: Optional[bool] = Field(None, description="List all VPCs available to the caller")

    state: Optional[str] = Field(None, description="VPC state")
    restartrequired: Optional[str] = Field(
        None, alias="restartRequired", description="VPC restart required"
    )

    supportedservices: Optional[str] = Field(
        None, alias="supportedServices", description="VPC supported services"
    )

    tags: Optional[str] = Field(None, description="List VPCs by tags (key/value pairs)")

    vpcofferingid: Optional[str] = Field(
        None, alias="vpcOfferingId", description="list by ID of the VPC offering"
    )
    account: Optional[str] = Field(
        None, alias="accountId", description="Account ID (requires domainid)"
    )

    domainid: Optional[str] = Field(
        None, alias="domainId", description="Account name (requires domainid)"
    )

    isrecursive: Optional[bool] = Field(
        None, alias="isRecursive", description="Include subdomains (used with domainid)"
    )

    projectid: Optional[str] = Field(
        None, description="Project ID (mutually exclusive with account)"
    )

    zoneid: Optional[str] = Field(
        None, alias="zoneId", description="ID of the zone in which to create the volume"
    )

    @model_validator(mode="after")
    def validate_account_domain(self):
        if self.account and not self.domainid:
            raise ValueError("'domainid' must be provided when 'account' is used")
        return self


class ListPrivateGatewayRequest(APIRequest, PaginationMixin):
    id: Optional[str] = Field(None, description="List Private Gateway by ID")
    ipaddress: Optional[str] = Field(None, description="List Private Gateway by IP address")
    isrecursive: Optional[bool] = Field(
        None, alias="isRecursive", description="Include subdomains (used with domainid)"
    )
    keyword: Optional[str] = Field(None, description="List Private Gateway by keyword")
    listall: Optional[bool] = Field(
        None, description="List all Private Gateways available to the caller"
    )
    state: Optional[str] = Field(None, description="Private Gateway state")
    vpcid: Optional[str] = Field(None, alias="vpcId", description="list by ID of the VPC")
    vlan: Optional[str] = Field(None, description="list by VLAN of the Private Gateway")
    account: Optional[str] = Field(
        None, alias="accountId", description="Account ID (requires domainid)"
    )
    domainid: Optional[str] = Field(
        None, alias="domainId", description="Account name (requires domainid)"
    )

    projectid: Optional[str] = Field(
        None, description="Project ID (mutually exclusive with account)"
    )

    @model_validator(mode="after")
    def validate_account_domain(self):
        if self.account and not self.domainid:
            raise ValueError("'domainid' must be provided when 'account' is used")
        return self


class ListStaticRouteRequest(APIRequest, PaginationMixin):
    id: Optional[str] = Field(None, description="List Static Route by ID")
    isrecursive: Optional[bool] = Field(
        None, alias="isRecursive", description="Include subdomains (used with domainid)"
    )
    keyword: Optional[str] = Field(None, description="List Static Route by keyword")
    listall: Optional[bool] = Field(
        None, description="List all Static Routes available to the caller"
    )
    state: Optional[str] = Field(None, description="Static Route state")
    vpcid: Optional[str] = Field(None, alias="vpcId", description="list by ID of the VPC")
    gatewayid: Optional[str] = Field(
        None, alias="gatewayId", description="list by ID of the Gateway"
    )
    account: Optional[str] = Field(
        None, alias="accountId", description="Account ID (requires domainid)"
    )
    domainid: Optional[str] = Field(
        None, alias="domainId", description="Account name (requires domainid)"
    )

    projectid: Optional[str] = Field(
        None, description="Project ID (mutually exclusive with account)"
    )

    tags: Optional[str] = Field(None, description="List Static Routes by tags (key/value pairs)")

    @model_validator(mode="after")
    def validate_account_domain(self):
        if self.account and not self.domainid:
            raise ValueError("'domainid' must be provided when 'account' is used")
        return self


class TierNetworkOffering(BaseModel):
    networkid: str = Field(..., description="ID of the network inside the VPC")
    networkofferingid: str = Field(..., description="New network offering ID for the network")


class MigrateVPCRequest(APIRequest):
    # Required
    vpcid: str = Field(..., description="ID of the VPC to migrate")
    vpcofferingid: str = Field(..., description="Target VPC offering ID")

    # Optional
    resume: Optional[bool] = Field(None, description="Resume previous failed migration")

    tiernetworkofferings: Optional[List[TierNetworkOffering]] = Field(
        None,
        description=(
            "List of network offering mappings for each tier (networkid → new networkofferingid)"
        ),
    )


class RestartVPCRequest(APIRequest):
    # Required
    id: str = Field(..., description="ID of the VPC to restart")

    # Optional
    cleanup: Optional[bool] = Field(None, description="Cleanup old network elements before restart")

    livepatch: Optional[bool] = Field(
        None,
        description=(
            "Apply live patch to router without full restart (only works when cleanup=False)"
        ),
    )

    makeredundant: Optional[bool] = Field(
        None, description="Convert single VPC router to redundant routers"
    )


class UpdateVPCRequest(APIRequest):
    command: str = Field(default="updateVPC", frozen=True)

    # Required
    id: str = Field(..., description="ID of the VPC to update")

    # Updatable fields
    customid: Optional[str] = Field(None, alias="customId", description="New custom ID of the VPC")
    name: Optional[str] = Field(None, description="New name of the VPC")

    displaytext: Optional[str] = Field(None, description="New display text of the VPC")

    # Visibility
    fordisplay: Optional[bool] = Field(None, description="Whether the VPC is visible to end users")

    # Advanced networking
    publicmtu: Optional[int] = Field(
        None, description="MTU to be configured on the network VR's public facing interfaces"
    )

    sourcenatipaddress: Optional[str] = Field(
        None,
        description=(
            "IPV4 address to be assigned to the public interface of the network router.",
            "This address must already be acquired for this VPC",
        ),
    )
