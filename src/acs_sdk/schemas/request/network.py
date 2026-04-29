from typing import Optional
from pydantic import Field
from acs_sdk.schemas.request.base import APIRequest, PaginationMixin


class CreateNetworkRequest(APIRequest):
    """Request to create a network."""

    # Required fields
    name: str = Field(..., description="The name of the network")
    displaytext: str = Field(
        ..., alias="displayText", description="The display text of the network"
    )
    networkofferingid: str = Field(
        ..., alias="networkOfferingId", description="The network offering ID"
    )
    zoneid: str = Field(..., alias="zoneId", description="The zone ID")

    # Optional fields
    vpcid: Optional[str] = Field(None, alias="vpcId", description="The VPC ID")
    gateway: Optional[str] = Field(None, description="The gateway of the network")
    netmask: Optional[str] = Field(None, description="The netmask of the network")
    startip: Optional[str] = Field(None, alias="startIp", description="The start IP of the network")
    endip: Optional[str] = Field(None, alias="endIp", description="The end IP of the network")
    aclid: Optional[str] = Field(None, alias="aclId", description="The ACL ID")
    domainid: Optional[str] = Field(None, alias="domainId", description="The domain ID")
    account: Optional[str] = Field(None, description="The account that will own the network")
    projectid: Optional[str] = Field(None, alias="projectId", description="The project ID")
    tags: Optional[str] = Field(None, description="Tag key and value pairs separated by comma")


class DeleteNetworkRequest(APIRequest):
    """Request to delete a network."""

    id: str = Field(..., description="The network ID to delete")
    forced: Optional[bool] = Field(None, description="Force delete the network")


class ListNetworkRequest(APIRequest, PaginationMixin):
    """Request to list networks."""

    # Filter by ID
    id: Optional[str] = Field(None, description="The network ID to retrieve")

    # Filter by name
    name: Optional[str] = Field(None, description="The name of the network")

    # Filter by zone
    zoneid: Optional[str] = Field(None, alias="zoneId", description="The zone ID")

    # Filter by VPC
    vpcid: Optional[str] = Field(None, alias="vpcId", description="The VPC ID")

    # Filter by physical network
    physicalnetworkid: Optional[str] = Field(
        None, alias="physicalNetworkId", description="The physical network ID"
    )

    # Filter by domain/account
    domainid: Optional[str] = Field(None, alias="domainId", description="The domain ID")

    account: Optional[str] = Field(None, description="The account")

    projectid: Optional[str] = Field(None, alias="projectId", description="The project ID")

    # Filter by state
    state: Optional[str] = Field(
        None, description="The state of the network (Setup, Implemented, etc.)"
    )

    issystem: Optional[bool] = Field(
        None, alias="isSystem", description="Return only system networks"
    )

    isrecursive: Optional[bool] = Field(
        None,
        alias="isRecursive",
        description="Defaults to false, but if true, lists networks from the parent domain and all its children domains.",
    )

    listall: Optional[bool] = Field(None, alias="listAll", description="List all networks")

    type: Optional[str] = Field(
        None, description="The type of the network (Isolated, Shared, etc.)"
    )


class UpdateNetworkRequest(APIRequest):
    """Request to update a network."""

    id: str = Field(..., description="The network ID to update")

    # Updatable fields
    name: Optional[str] = Field(None, description="The new name of the network")

    displaytext: Optional[str] = Field(
        None, alias="displayText", description="The new display text of the network"
    )

    guestiptype: Optional[str] = Field(
        None, alias="guestIpType", description="The guest IP type (IPv4, IPv6, Dual)"
    )

    customized: Optional[bool] = Field(
        None, description="Specify whether to allow customized offerings"
    )


class RestartNetworkRequest(APIRequest):
    """Request to restart a network."""

    id: str = Field(..., description="The network ID to restart")

    cleanup: Optional[bool] = Field(None, description="Cleanup network before restart")

    makeredundant: Optional[bool] = Field(
        None, alias="makeRedundant", description="Make network redundant"
    )


class MigrateNetworkRequest(APIRequest):
    """Request to migrate a network."""

    id: str = Field(..., description="The network ID to migrate")

    physicalnetworkid: str = Field(
        ..., alias="physicalNetworkId", description="The physical network ID to migrate to"
    )

    vpcid: Optional[str] = Field(None, alias="vpcId", description="The VPC ID")


class ReleaseNetworkRequest(APIRequest):
    """Request to release a network."""

    id: str = Field(..., description="The network ID to release")

    forced: Optional[bool] = Field(None, description="Force release the network")


class ListNetworkServiceProvidersRequest(APIRequest, PaginationMixin):
    """Request to list network service providers."""

    id: Optional[str] = Field(None, description="The network service provider ID")

    name: Optional[str] = Field(None, description="The network service provider name")

    physicalnetworkid: Optional[str] = Field(
        None, alias="physicalNetworkId", description="The physical network ID"
    )

    state: Optional[str] = Field(
        None, description="The state of the provider (Enabled, Disabled, etc.)"
    )


class ListNetworkServicesRequest(APIRequest, PaginationMixin):
    """Request to list network services."""

    provider: Optional[str] = Field(None, description="The network service provider")

    service: Optional[str] = Field(None, description="The network service name")

    physicalnetworkid: Optional[str] = Field(
        None, alias="physicalNetworkId", description="The physical network ID"
    )


# Add operations


class AddGloboDnsHostRequest(APIRequest):
    """Request to add a Globo DNS host."""

    url: str = Field(..., description="The URL of the Globo DNS host")

    password: str = Field(..., description="The password for the Globo DNS host")

    username: Optional[str] = Field(None, description="The username for the Globo DNS host")


class AddNetworkServiceProviderRequest(APIRequest):
    """Request to add a network service provider."""

    name: str = Field(..., description="The name of the network service provider")

    physicalnetworkid: str = Field(
        ..., alias="physicalNetworkId", description="The physical network ID"
    )


class AddOpenDaylightControllerRequest(APIRequest):
    """Request to add an OpenDaylight controller."""

    url: str = Field(..., description="The URL of the OpenDaylight controller")

    username: str = Field(..., description="The username for the OpenDaylight controller")

    password: str = Field(..., description="The password for the OpenDaylight controller")


class AddTrafficMonitorRequest(APIRequest):
    """Request to add a traffic monitor."""

    url: str = Field(..., description="The URL of the traffic monitor")

    zoneid: str = Field(..., alias="zoneId", description="The zone ID")


class AddTrafficTypeRequest(APIRequest):
    """Request to add a traffic type to a physical network."""

    traffictype: str = Field(..., alias="trafficType", description="The traffic type")

    physicalnetworkid: str = Field(
        ..., alias="physicalNetworkId", description="The physical network ID"
    )

    xennetworklabel: Optional[str] = Field(
        None, alias="xenNetworkLabel", description="The Xen network label"
    )

    kvmnetworklabel: Optional[str] = Field(
        None, alias="kvmNetworkLabel", description="The KVM network label"
    )

    vmwarenetworklabel: Optional[str] = Field(
        None, alias="vmwareNetworkLabel", description="The VMware network label"
    )

    hypervnetworklabel: Optional[str] = Field(
        None, alias="hypervNetworkLabel", description="The Hyper-V network label"
    )

    simulatorlabel: Optional[str] = Field(
        None, alias="simulatorLabel", description="The simulator network label"
    )

    ovsnetworklabel: Optional[str] = Field(
        None, alias="ovsNetworkLabel", description="The OVS network label"
    )

    baremetal_network_label: Optional[str] = Field(
        None, alias="baremetalNetworkLabel", description="The bare metal network label"
    )


# Create operations


class ChangeBgpPeersForNetworkRequest(APIRequest):
    """Request to change BGP peers for a network."""

    id: str = Field(..., description="The network ID")


class CreateGuestNetworkIpv6PrefixRequest(APIRequest):
    """Request to create a guest network IPv6 prefix."""

    networkid: str = Field(..., alias="networkId", description="The network ID")

    prefix: str = Field(..., description="The IPv6 prefix")

    length: Optional[int] = Field(None, description="The prefix length")


class CreateIpv4SubnetForGuestNetworkRequest(APIRequest):
    """Request to create an IPv4 subnet for a guest network."""

    networkid: str = Field(..., alias="networkId", description="The network ID")

    gateway: str = Field(..., description="The gateway IP address")

    netmask: str = Field(..., description="The netmask")


class CreateNetworkPermissionsRequest(APIRequest):
    """Request to create network permissions."""

    networkid: str = Field(..., alias="networkId", description="The network ID")

    domainid: Optional[str] = Field(None, alias="domainId", description="The domain ID")

    account: Optional[str] = Field(None, description="The account name")


class CreatePhysicalNetworkRequest(APIRequest):
    """Request to create a physical network."""

    name: str = Field(..., description="The name of the physical network")

    zoneid: str = Field(..., alias="zoneId", description="The zone ID")

    vlan: Optional[str] = Field(None, description="The VLAN range")

    broadcastdomainrange: Optional[str] = Field(
        None, alias="broadcastDomainRange", description="The broadcast domain range"
    )

    domainid: Optional[str] = Field(None, alias="domainId", description="The domain ID")

    networkspeed: Optional[str] = Field(None, alias="networkSpeed", description="The network speed")

    tags: Optional[str] = Field(None, description="Tags for the physical network")


class CreateServiceInstanceRequest(APIRequest):
    """Request to create a service instance."""

    name: str = Field(..., description="The name of the service instance")

    serviceofferingid: str = Field(
        ..., alias="serviceOfferingId", description="The service offering ID"
    )

    templateid: str = Field(..., alias="templateId", description="The template ID")

    zoneid: str = Field(..., alias="zoneId", description="The zone ID")


class CreateStorageNetworkIpRangeRequest(APIRequest):
    """Request to create a storage network IP range."""

    networkid: str = Field(..., alias="networkId", description="The network ID")

    gateway: str = Field(..., description="The gateway IP address")

    netmask: str = Field(..., description="The netmask")

    startip: str = Field(..., alias="startIp", description="The start IP address")

    endip: Optional[str] = Field(None, alias="endIp", description="The end IP address")

    vlan: Optional[str] = Field(None, description="The VLAN ID")

    podid: Optional[str] = Field(None, alias="podId", description="The pod ID")


# Delete operations


class DeleteCiscoNexusVSMRequest(APIRequest):
    """Request to delete a Cisco Nexus VSM."""

    id: str = Field(..., description="The Cisco Nexus VSM ID")


class DeleteGuestNetworkIpv6PrefixRequest(APIRequest):
    """Request to delete a guest network IPv6 prefix."""

    id: str = Field(..., description="The IPv6 prefix ID")


class DeleteIpv4SubnetForGuestNetworkRequest(APIRequest):
    """Request to delete an IPv4 subnet for a guest network."""

    id: str = Field(..., description="The IPv4 subnet ID")


class DeleteNetworkServiceProviderRequest(APIRequest):
    """Request to delete a network service provider."""

    id: str = Field(..., description="The network service provider ID")


class DeleteOpenDaylightControllerRequest(APIRequest):
    """Request to delete an OpenDaylight controller."""

    id: str = Field(..., description="The OpenDaylight controller ID")


class DeletePhysicalNetworkRequest(APIRequest):
    """Request to delete a physical network."""

    id: str = Field(..., description="The physical network ID")


class DeleteStorageNetworkIpRangeRequest(APIRequest):
    """Request to delete a storage network IP range."""

    id: str = Field(..., description="The storage network IP range ID")


class DeleteTrafficMonitorRequest(APIRequest):
    """Request to delete a traffic monitor."""

    id: str = Field(..., description="The traffic monitor ID")


class DeleteTrafficTypeRequest(APIRequest):
    """Request to delete a traffic type."""

    id: str = Field(..., description="The traffic type ID")


# Disable/Enable operations


class DisableCiscoNexusVSMRequest(APIRequest):
    """Request to disable a Cisco Nexus VSM."""

    id: str = Field(..., description="The Cisco Nexus VSM ID")


class EnableCiscoNexusVSMRequest(APIRequest):
    """Request to enable a Cisco Nexus VSM."""

    id: str = Field(..., description="The Cisco Nexus VSM ID")


# List operations


class ListCiscoNexusVSMsRequest(APIRequest, PaginationMixin):
    """Request to list Cisco Nexus VSMs."""

    id: Optional[str] = Field(None, description="The Cisco Nexus VSM ID")

    keyword: Optional[str] = Field(None, description="List by keyword")


class ListGuestNetworkIpv6PrefixesRequest(APIRequest, PaginationMixin):
    """Request to list guest network IPv6 prefixes."""

    id: Optional[str] = Field(None, description="The IPv6 prefix ID")

    networkid: Optional[str] = Field(None, alias="networkId", description="The network ID")


class ListIpv4SubnetsForGuestNetworkRequest(APIRequest, PaginationMixin):
    """Request to list IPv4 subnets for a guest network."""

    networkid: str = Field(..., alias="networkId", description="The network ID")

    id: Optional[str] = Field(None, description="The IPv4 subnet ID")


class ListNetworkIsolationMethodsRequest(APIRequest, PaginationMixin):
    """Request to list network isolation methods."""

    keyword: Optional[str] = Field(None, description="List by keyword")


class ListNetworkPermissionsRequest(APIRequest, PaginationMixin):
    """Request to list network permissions."""

    networkid: str = Field(..., alias="networkId", description="The network ID")


class ListNetworkProtocolsRequest(APIRequest, PaginationMixin):
    """Request to list network protocols."""

    keyword: Optional[str] = Field(None, description="List by keyword")


class ListOpenDaylightControllersRequest(APIRequest, PaginationMixin):
    """Request to list OpenDaylight controllers."""

    id: Optional[str] = Field(None, description="The OpenDaylight controller ID")

    keyword: Optional[str] = Field(None, description="List by keyword")

    physicalnetworkid: Optional[str] = Field(
        None, alias="physicalNetworkId", description="The physical network ID"
    )


class ListPhysicalNetworksRequest(APIRequest, PaginationMixin):
    """Request to list physical networks."""

    id: Optional[str] = Field(None, description="The physical network ID")

    name: Optional[str] = Field(None, description="The physical network name")

    zoneid: Optional[str] = Field(None, alias="zoneId", description="The zone ID")

    keyword: Optional[str] = Field(None, description="List by keyword")


class ListStorageNetworkIpRangeRequest(APIRequest, PaginationMixin):
    """Request to list storage network IP ranges."""

    id: Optional[str] = Field(None, description="The storage network IP range ID")

    networkid: Optional[str] = Field(None, alias="networkId", description="The network ID")

    podid: Optional[str] = Field(None, alias="podId", description="The pod ID")


class ListSupportedNetworkServicesRequest(APIRequest, PaginationMixin):
    """Request to list supported network services."""

    keyword: Optional[str] = Field(None, description="List by keyword")


class ListTrafficMonitorsRequest(APIRequest, PaginationMixin):
    """Request to list traffic monitors."""

    id: Optional[str] = Field(None, description="The traffic monitor ID")

    keyword: Optional[str] = Field(None, description="List by keyword")

    zoneid: Optional[str] = Field(None, alias="zoneId", description="The zone ID")


class ListTrafficTypeImplementorsRequest(APIRequest, PaginationMixin):
    """Request to list traffic type implementors."""

    keyword: Optional[str] = Field(None, description="List by keyword")

    traffictype: Optional[str] = Field(None, alias="trafficType", description="The traffic type")


class ListTrafficTypesRequest(APIRequest, PaginationMixin):
    """Request to list traffic types."""

    physicalnetworkid: str = Field(
        ..., alias="physicalNetworkId", description="The physical network ID"
    )

    keyword: Optional[str] = Field(None, description="List by keyword")


# Release operation


class ReleasePublicIpRangeRequest(APIRequest):
    """Request to release a public IP range."""

    id: str = Field(..., description="The public IP range ID")

    forced: Optional[bool] = Field(None, description="Force release the IP range")


# Remove/Reset operations


class RemoveNetworkPermissionsRequest(APIRequest):
    """Request to remove network permissions."""

    networkid: str = Field(..., alias="networkId", description="The network ID")

    domainid: Optional[str] = Field(None, alias="domainId", description="The domain ID")

    account: Optional[str] = Field(None, description="The account name")


class ResetNetworkPermissionsRequest(APIRequest):
    """Request to reset network permissions."""

    networkid: str = Field(..., alias="networkId", description="The network ID")


# Update operations


class UpdateNetworkServiceProviderRequest(APIRequest):
    """Request to update a network service provider."""

    id: str = Field(..., description="The network service provider ID")

    state: Optional[str] = Field(None, description="The state (Enabled, Disabled)")


class UpdatePhysicalNetworkRequest(APIRequest):
    """Request to update a physical network."""

    id: str = Field(..., description="The physical network ID")

    tags: Optional[str] = Field(None, description="Tags for the physical network")

    vlan: Optional[str] = Field(None, description="The VLAN range")


class UpdateStorageNetworkIpRangeRequest(APIRequest):
    """Request to update a storage network IP range."""

    id: str = Field(..., description="The storage network IP range ID")

    startip: Optional[str] = Field(None, alias="startIp", description="The start IP address")

    endip: Optional[str] = Field(None, alias="endIp", description="The end IP address")

    netmask: Optional[str] = Field(None, description="The netmask")

    gateway: Optional[str] = Field(None, description="The gateway IP address")

    vlan: Optional[str] = Field(None, description="The VLAN ID")


class UpdateTrafficTypeRequest(APIRequest):
    """Request to update a traffic type."""

    id: str = Field(..., description="The traffic type ID")

    xennetworklabel: Optional[str] = Field(
        None, alias="xenNetworkLabel", description="The Xen network label"
    )

    kvmnetworklabel: Optional[str] = Field(
        None, alias="kvmNetworkLabel", description="The KVM network label"
    )

    vmwarenetworklabel: Optional[str] = Field(
        None, alias="vmwareNetworkLabel", description="The VMware network label"
    )

    hypervnetworklabel: Optional[str] = Field(
        None, alias="hypervNetworkLabel", description="The Hyper-V network label"
    )

    simulatorlabel: Optional[str] = Field(
        None, alias="simulatorLabel", description="The simulator network label"
    )

    ovsnetworklabel: Optional[str] = Field(
        None, alias="ovsNetworkLabel", description="The OVS network label"
    )

    baremetal_network_label: Optional[str] = Field(
        None, alias="baremetalNetworkLabel", description="The bare metal network label"
    )
