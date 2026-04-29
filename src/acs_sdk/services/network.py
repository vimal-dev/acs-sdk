# services/network.py
from typing import Dict, List

from acs_sdk.schemas.request.network import (
    AddGloboDnsHostRequest,
    AddNetworkServiceProviderRequest,
    AddOpenDaylightControllerRequest,
    AddTrafficMonitorRequest,
    AddTrafficTypeRequest,
    ChangeBgpPeersForNetworkRequest,
    CreateGuestNetworkIpv6PrefixRequest,
    CreateIpv4SubnetForGuestNetworkRequest,
    CreateNetworkRequest,
    CreateNetworkPermissionsRequest,
    CreatePhysicalNetworkRequest,
    CreateServiceInstanceRequest,
    CreateStorageNetworkIpRangeRequest,
    DeleteCiscoNexusVSMRequest,
    DeleteGuestNetworkIpv6PrefixRequest,
    DeleteIpv4SubnetForGuestNetworkRequest,
    DeleteNetworkRequest,
    DeleteNetworkServiceProviderRequest,
    DeleteOpenDaylightControllerRequest,
    DeletePhysicalNetworkRequest,
    DeleteStorageNetworkIpRangeRequest,
    DeleteTrafficMonitorRequest,
    DeleteTrafficTypeRequest,
    DisableCiscoNexusVSMRequest,
    EnableCiscoNexusVSMRequest,
    ListCiscoNexusVSMsRequest,
    ListGuestNetworkIpv6PrefixesRequest,
    ListIpv4SubnetsForGuestNetworkRequest,
    ListNetworkIsolationMethodsRequest,
    ListNetworkPermissionsRequest,
    ListNetworkProtocolsRequest,
    ListNetworkRequest,
    ListNetworkServiceProvidersRequest,
    ListNetworkServicesRequest,
    ListOpenDaylightControllersRequest,
    ListPhysicalNetworksRequest,
    ListStorageNetworkIpRangeRequest,
    ListSupportedNetworkServicesRequest,
    ListTrafficMonitorsRequest,
    ListTrafficTypeImplementorsRequest,
    ListTrafficTypesRequest,
    MigrateNetworkRequest,
    ReleaseNetworkRequest,
    ReleasePublicIpRangeRequest,
    RemoveNetworkPermissionsRequest,
    ResetNetworkPermissionsRequest,
    RestartNetworkRequest,
    UpdateNetworkRequest,
    UpdateNetworkServiceProviderRequest,
    UpdatePhysicalNetworkRequest,
    UpdateStorageNetworkIpRangeRequest,
    UpdateTrafficTypeRequest,
)

from .base import BaseService
from ..schemas.response.base import APIResponse


class Network(BaseService):
    """Service for CloudStack Network operations."""

    def list(self, payload: ListNetworkRequest) -> APIResponse[List[Dict]]:
        """List all available networks.

        Args:
            payload (ListNetworkRequest): The request payload containing filter options.

        Returns:
            APIResponse[List[Dict]]: A response containing a list of networks.
        """
        return self._execute(
            "listNetworks",
            payload,
            envelope="listnetworksresponse",
            entity="network",
        )

    async def list_async(self, payload: ListNetworkRequest) -> APIResponse[List[Dict]]:
        """Asynchronously list all available networks.

        Args:
            payload (ListNetworkRequest): The request payload containing filter options.

        Returns:
            APIResponse[List[Dict]]: A response containing a list of networks.
        """
        return await self._execute_async(
            "listNetworks",
            payload,
            envelope="listnetworksresponse",
            entity="network",
        )

    def create(self, payload: CreateNetworkRequest) -> APIResponse[Dict]:
        """Create a new network.

        Args:
            payload (CreateNetworkRequest): The request payload containing network creation parameters.

        Returns:
            APIResponse[Dict]: A response containing the created network.
        """
        return self._execute(
            "createNetwork",
            payload,
            envelope="createnetworkresponse",
        )

    async def create_async(self, payload: CreateNetworkRequest) -> APIResponse[Dict]:
        """Asynchronously create a new network.

        Args:
            payload (CreateNetworkRequest): The request payload containing network creation parameters.

        Returns:
            APIResponse[Dict]: A response containing the created network.
        """
        return await self._execute_async(
            "createNetwork",
            payload,
            envelope="createnetworkresponse",
        )

    def delete(self, payload: DeleteNetworkRequest) -> APIResponse[Dict]:
        """Delete a network.

        Args:
            payload (DeleteNetworkRequest): The request payload containing the network ID to delete.

        Returns:
            APIResponse[Dict]: A response indicating success or failure.
        """
        return self._execute(
            "deleteNetwork",
            payload,
            envelope="deletenetworkresponse",
        )

    async def delete_async(self, payload: DeleteNetworkRequest) -> APIResponse[Dict]:
        """Asynchronously delete a network.

        Args:
            payload (DeleteNetworkRequest): The request payload containing the network ID to delete.

        Returns:
            APIResponse[Dict]: A response indicating success or failure.
        """
        return await self._execute_async(
            "deleteNetwork",
            payload,
            envelope="deletenetworkresponse",
        )

    def update(self, payload: UpdateNetworkRequest) -> APIResponse[Dict]:
        """Update a network.

        Args:
            payload (UpdateNetworkRequest): The request payload containing network update parameters.

        Returns:
            APIResponse[Dict]: A response containing the updated network.
        """
        return self._execute(
            "updateNetwork",
            payload,
            envelope="updatenetworkresponse",
        )

    async def update_async(self, payload: UpdateNetworkRequest) -> APIResponse[Dict]:
        """Asynchronously update a network.

        Args:
            payload (UpdateNetworkRequest): The request payload containing network update parameters.

        Returns:
            APIResponse[Dict]: A response containing the updated network.
        """
        return await self._execute_async(
            "updateNetwork",
            payload,
            envelope="updatenetworkresponse",
        )

    def restart(self, payload: RestartNetworkRequest) -> APIResponse[Dict]:
        """Restart a network. This operation stops and starts the network.

        Args:
            payload (RestartNetworkRequest): The request payload containing the network ID to restart.

        Returns:
            APIResponse[Dict]: A response indicating the restart operation status.
        """
        return self._execute(
            "restartNetwork",
            payload,
            envelope="restartnetworkresponse",
        )

    async def restart_async(self, payload: RestartNetworkRequest) -> APIResponse[Dict]:
        """Asynchronously restart a network.

        Args:
            payload (RestartNetworkRequest): The request payload containing the network ID to restart.

        Returns:
            APIResponse[Dict]: A response indicating the restart operation status.
        """
        return await self._execute_async(
            "restartNetwork",
            payload,
            envelope="restartnetworkresponse",
        )

    def migrate(self, payload: MigrateNetworkRequest) -> APIResponse[Dict]:
        """Migrate a network to a different physical network.

        Args:
            payload (MigrateNetworkRequest): The request payload containing migration parameters.

        Returns:
            APIResponse[Dict]: A response containing the migrated network.
        """
        return self._execute(
            "migrateNetwork",
            payload,
            envelope="migratenetworkresponse",
        )

    async def migrate_async(self, payload: MigrateNetworkRequest) -> APIResponse[Dict]:
        """Asynchronously migrate a network to a different physical network.

        Args:
            payload (MigrateNetworkRequest): The request payload containing migration parameters.

        Returns:
            APIResponse[Dict]: A response containing the migrated network.
        """
        return await self._execute_async(
            "migrateNetwork",
            payload,
            envelope="migratenetworkresponse",
        )

    def release(self, payload: ReleaseNetworkRequest) -> APIResponse[Dict]:
        """Release a network. This deallocates and removes the network.

        Args:
            payload (ReleaseNetworkRequest): The request payload containing the network ID to release.

        Returns:
            APIResponse[Dict]: A response indicating success or failure.
        """
        return self._execute(
            "releaseNetwork",
            payload,
            envelope="releasenetworkresponse",
        )

    async def release_async(self, payload: ReleaseNetworkRequest) -> APIResponse[Dict]:
        """Asynchronously release a network.

        Args:
            payload (ReleaseNetworkRequest): The request payload containing the network ID to release.

        Returns:
            APIResponse[Dict]: A response indicating success or failure.
        """
        return await self._execute_async(
            "releaseNetwork",
            payload,
            envelope="releasenetworkresponse",
        )

    def list_service_providers(
        self, payload: ListNetworkServiceProvidersRequest
    ) -> APIResponse[List[Dict]]:
        """List network service providers.

        Args:
            payload (ListNetworkServiceProvidersRequest): The request payload containing filter options.

        Returns:
            APIResponse[List[Dict]]: A response containing a list of network service providers.
        """
        return self._execute(
            "listNetworkServiceProviders",
            payload,
            envelope="listnetworkserviceprovidersresponse",
            entity="networkserviceprovider",
        )

    async def list_service_providers_async(
        self, payload: ListNetworkServiceProvidersRequest
    ) -> APIResponse[List[Dict]]:
        """Asynchronously list network service providers.

        Args:
            payload (ListNetworkServiceProvidersRequest): The request payload containing filter options.

        Returns:
            APIResponse[List[Dict]]: A response containing a list of network service providers.
        """
        return await self._execute_async(
            "listNetworkServiceProviders",
            payload,
            envelope="listnetworkserviceprovidersresponse",
            entity="networkserviceprovider",
        )

    def list_services(self, payload: ListNetworkServicesRequest) -> APIResponse[List[Dict]]:
        """List network services.

        Args:
            payload (ListNetworkServicesRequest): The request payload containing filter options.

        Returns:
            APIResponse[List[Dict]]: A response containing a list of network services.
        """
        return self._execute(
            "listNetworkServices",
            payload,
            envelope="listnetworkservicesresponse",
            entity="networkservice",
        )

    async def list_services_async(
        self, payload: ListNetworkServicesRequest
    ) -> APIResponse[List[Dict]]:
        """Asynchronously list network services.

        Args:
            payload (ListNetworkServicesRequest): The request payload containing filter options.

        Returns:
            APIResponse[List[Dict]]: A response containing a list of network services.
        """
        return await self._execute_async(
            "listNetworkServices",
            payload,
            envelope="listnetworkservicesresponse",
            entity="networkservice",
        )

    # Add operations

    def add_globo_dns_host(self, payload: AddGloboDnsHostRequest) -> APIResponse[Dict]:
        """Add a Globo DNS host."""
        return self._execute(
            "addGloboDnsHost",
            payload,
            envelope="addglobodnshostresponse",
        )

    async def add_globo_dns_host_async(self, payload: AddGloboDnsHostRequest) -> APIResponse[Dict]:
        """Asynchronously add a Globo DNS host."""
        return await self._execute_async(
            "addGloboDnsHost",
            payload,
            envelope="addglobodnshostresponse",
        )

    def add_network_service_provider(
        self, payload: AddNetworkServiceProviderRequest
    ) -> APIResponse[Dict]:
        """Add a network service provider."""
        return self._execute(
            "addNetworkServiceProvider",
            payload,
            envelope="addnetworkserviceproviderresponse",
        )

    async def add_network_service_provider_async(
        self, payload: AddNetworkServiceProviderRequest
    ) -> APIResponse[Dict]:
        """Asynchronously add a network service provider."""
        return await self._execute_async(
            "addNetworkServiceProvider",
            payload,
            envelope="addnetworkserviceproviderresponse",
        )

    def add_opendaylight_controller(
        self, payload: AddOpenDaylightControllerRequest
    ) -> APIResponse[Dict]:
        """Add an OpenDaylight controller."""
        return self._execute(
            "addOpenDaylightController",
            payload,
            envelope="addopendaylightcontrollerresponse",
        )

    async def add_opendaylight_controller_async(
        self, payload: AddOpenDaylightControllerRequest
    ) -> APIResponse[Dict]:
        """Asynchronously add an OpenDaylight controller."""
        return await self._execute_async(
            "addOpenDaylightController",
            payload,
            envelope="addopendaylightcontrollerresponse",
        )

    def add_traffic_monitor(self, payload: AddTrafficMonitorRequest) -> APIResponse[Dict]:
        """Add a traffic monitor."""
        return self._execute(
            "addTrafficMonitor",
            payload,
            envelope="addtrafficmonitorresponse",
        )

    async def add_traffic_monitor_async(
        self, payload: AddTrafficMonitorRequest
    ) -> APIResponse[Dict]:
        """Asynchronously add a traffic monitor."""
        return await self._execute_async(
            "addTrafficMonitor",
            payload,
            envelope="addtrafficmonitorresponse",
        )

    def add_traffic_type(self, payload: AddTrafficTypeRequest) -> APIResponse[Dict]:
        """Add a traffic type to a physical network."""
        return self._execute(
            "addTrafficType",
            payload,
            envelope="addtraffictyperesponse",
        )

    async def add_traffic_type_async(self, payload: AddTrafficTypeRequest) -> APIResponse[Dict]:
        """Asynchronously add a traffic type to a physical network."""
        return await self._execute_async(
            "addTrafficType",
            payload,
            envelope="addtraffictyperesponse",
        )

    # Create operations

    def change_bgp_peers_for_network(
        self, payload: ChangeBgpPeersForNetworkRequest
    ) -> APIResponse[Dict]:
        """Change BGP peers for a network."""
        return self._execute(
            "changeBgpPeersForNetwork",
            payload,
            envelope="changebgppeersfornetworkresponse",
        )

    async def change_bgp_peers_for_network_async(
        self, payload: ChangeBgpPeersForNetworkRequest
    ) -> APIResponse[Dict]:
        """Asynchronously change BGP peers for a network."""
        return await self._execute_async(
            "changeBgpPeersForNetwork",
            payload,
            envelope="changebgppeersfornetworkresponse",
        )

    def create_guest_network_ipv6_prefix(
        self, payload: CreateGuestNetworkIpv6PrefixRequest
    ) -> APIResponse[Dict]:
        """Create a guest network IPv6 prefix."""
        return self._execute(
            "createGuestNetworkIpv6Prefix",
            payload,
            envelope="createguestnetworkipv6prefixresponse",
        )

    async def create_guest_network_ipv6_prefix_async(
        self, payload: CreateGuestNetworkIpv6PrefixRequest
    ) -> APIResponse[Dict]:
        """Asynchronously create a guest network IPv6 prefix."""
        return await self._execute_async(
            "createGuestNetworkIpv6Prefix",
            payload,
            envelope="createguestnetworkipv6prefixresponse",
        )

    def create_ipv4_subnet_for_guest_network(
        self, payload: CreateIpv4SubnetForGuestNetworkRequest
    ) -> APIResponse[Dict]:
        """Create an IPv4 subnet for a guest network."""
        return self._execute(
            "createIpv4SubnetForGuestNetwork",
            payload,
            envelope="createipv4subnetforguestnetworkresponse",
        )

    async def create_ipv4_subnet_for_guest_network_async(
        self, payload: CreateIpv4SubnetForGuestNetworkRequest
    ) -> APIResponse[Dict]:
        """Asynchronously create an IPv4 subnet for a guest network."""
        return await self._execute_async(
            "createIpv4SubnetForGuestNetwork",
            payload,
            envelope="createipv4subnetforguestnetworkresponse",
        )

    def create_network_permissions(
        self, payload: CreateNetworkPermissionsRequest
    ) -> APIResponse[Dict]:
        """Create network permissions."""
        return self._execute(
            "createNetworkPermissions",
            payload,
            envelope="createnetworkpermissionsresponse",
        )

    async def create_network_permissions_async(
        self, payload: CreateNetworkPermissionsRequest
    ) -> APIResponse[Dict]:
        """Asynchronously create network permissions."""
        return await self._execute_async(
            "createNetworkPermissions",
            payload,
            envelope="createnetworkpermissionsresponse",
        )

    def create_physical_network(self, payload: CreatePhysicalNetworkRequest) -> APIResponse[Dict]:
        """Create a physical network."""
        return self._execute(
            "createPhysicalNetwork",
            payload,
            envelope="createphysicalnetworkresponse",
        )

    async def create_physical_network_async(
        self, payload: CreatePhysicalNetworkRequest
    ) -> APIResponse[Dict]:
        """Asynchronously create a physical network."""
        return await self._execute_async(
            "createPhysicalNetwork",
            payload,
            envelope="createphysicalnetworkresponse",
        )

    def create_service_instance(self, payload: CreateServiceInstanceRequest) -> APIResponse[Dict]:
        """Create a service instance."""
        return self._execute(
            "createServiceInstance",
            payload,
            envelope="createserviceinstanceresponse",
        )

    async def create_service_instance_async(
        self, payload: CreateServiceInstanceRequest
    ) -> APIResponse[Dict]:
        """Asynchronously create a service instance."""
        return await self._execute_async(
            "createServiceInstance",
            payload,
            envelope="createserviceinstanceresponse",
        )

    def create_storage_network_ip_range(
        self, payload: CreateStorageNetworkIpRangeRequest
    ) -> APIResponse[Dict]:
        """Create a storage network IP range."""
        return self._execute(
            "createStorageNetworkIpRange",
            payload,
            envelope="createstoragenetworkiprangeresponse",
        )

    async def create_storage_network_ip_range_async(
        self, payload: CreateStorageNetworkIpRangeRequest
    ) -> APIResponse[Dict]:
        """Asynchronously create a storage network IP range."""
        return await self._execute_async(
            "createStorageNetworkIpRange",
            payload,
            envelope="createstoragenetworkiprangeresponse",
        )

    # Delete operations

    def delete_cisco_nexus_vsm(self, payload: DeleteCiscoNexusVSMRequest) -> APIResponse[Dict]:
        """Delete a Cisco Nexus VSM."""
        return self._execute(
            "deleteCiscoNexusVSM",
            payload,
            envelope="deletecisconexusvsmresponse",
        )

    async def delete_cisco_nexus_vsm_async(
        self, payload: DeleteCiscoNexusVSMRequest
    ) -> APIResponse[Dict]:
        """Asynchronously delete a Cisco Nexus VSM."""
        return await self._execute_async(
            "deleteCiscoNexusVSM",
            payload,
            envelope="deletecisconexusvsmresponse",
        )

    def delete_guest_network_ipv6_prefix(
        self, payload: DeleteGuestNetworkIpv6PrefixRequest
    ) -> APIResponse[Dict]:
        """Delete a guest network IPv6 prefix."""
        return self._execute(
            "deleteGuestNetworkIpv6Prefix",
            payload,
            envelope="deleteguestnetworkipv6prefixresponse",
        )

    async def delete_guest_network_ipv6_prefix_async(
        self, payload: DeleteGuestNetworkIpv6PrefixRequest
    ) -> APIResponse[Dict]:
        """Asynchronously delete a guest network IPv6 prefix."""
        return await self._execute_async(
            "deleteGuestNetworkIpv6Prefix",
            payload,
            envelope="deleteguestnetworkipv6prefixresponse",
        )

    def delete_ipv4_subnet_for_guest_network(
        self, payload: DeleteIpv4SubnetForGuestNetworkRequest
    ) -> APIResponse[Dict]:
        """Delete an IPv4 subnet for a guest network."""
        return self._execute(
            "deleteIpv4SubnetForGuestNetwork",
            payload,
            envelope="deleteipv4subnetforguestnetworkresponse",
        )

    async def delete_ipv4_subnet_for_guest_network_async(
        self, payload: DeleteIpv4SubnetForGuestNetworkRequest
    ) -> APIResponse[Dict]:
        """Asynchronously delete an IPv4 subnet for a guest network."""
        return await self._execute_async(
            "deleteIpv4SubnetForGuestNetwork",
            payload,
            envelope="deleteipv4subnetforguestnetworkresponse",
        )

    def delete_network_service_provider(
        self, payload: DeleteNetworkServiceProviderRequest
    ) -> APIResponse[Dict]:
        """Delete a network service provider."""
        return self._execute(
            "deleteNetworkServiceProvider",
            payload,
            envelope="deletenetworkserviceproviderresponse",
        )

    async def delete_network_service_provider_async(
        self, payload: DeleteNetworkServiceProviderRequest
    ) -> APIResponse[Dict]:
        """Asynchronously delete a network service provider."""
        return await self._execute_async(
            "deleteNetworkServiceProvider",
            payload,
            envelope="deletenetworkserviceproviderresponse",
        )

    def delete_opendaylight_controller(
        self, payload: DeleteOpenDaylightControllerRequest
    ) -> APIResponse[Dict]:
        """Delete an OpenDaylight controller."""
        return self._execute(
            "deleteOpenDaylightController",
            payload,
            envelope="deleteopendaylightcontrollerresponse",
        )

    async def delete_opendaylight_controller_async(
        self, payload: DeleteOpenDaylightControllerRequest
    ) -> APIResponse[Dict]:
        """Asynchronously delete an OpenDaylight controller."""
        return await self._execute_async(
            "deleteOpenDaylightController",
            payload,
            envelope="deleteopendaylightcontrollerresponse",
        )

    def delete_physical_network(self, payload: DeletePhysicalNetworkRequest) -> APIResponse[Dict]:
        """Delete a physical network."""
        return self._execute(
            "deletePhysicalNetwork",
            payload,
            envelope="deletephysicalnetworkresponse",
        )

    async def delete_physical_network_async(
        self, payload: DeletePhysicalNetworkRequest
    ) -> APIResponse[Dict]:
        """Asynchronously delete a physical network."""
        return await self._execute_async(
            "deletePhysicalNetwork",
            payload,
            envelope="deletephysicalnetworkresponse",
        )

    def delete_storage_network_ip_range(
        self, payload: DeleteStorageNetworkIpRangeRequest
    ) -> APIResponse[Dict]:
        """Delete a storage network IP range."""
        return self._execute(
            "deleteStorageNetworkIpRange",
            payload,
            envelope="deletestoragenetworkiprangeresponse",
        )

    async def delete_storage_network_ip_range_async(
        self, payload: DeleteStorageNetworkIpRangeRequest
    ) -> APIResponse[Dict]:
        """Asynchronously delete a storage network IP range."""
        return await self._execute_async(
            "deleteStorageNetworkIpRange",
            payload,
            envelope="deletestoragenetworkiprangeresponse",
        )

    def delete_traffic_monitor(self, payload: DeleteTrafficMonitorRequest) -> APIResponse[Dict]:
        """Delete a traffic monitor."""
        return self._execute(
            "deleteTrafficMonitor",
            payload,
            envelope="deletetrafficmonitorresponse",
        )

    async def delete_traffic_monitor_async(
        self, payload: DeleteTrafficMonitorRequest
    ) -> APIResponse[Dict]:
        """Asynchronously delete a traffic monitor."""
        return await self._execute_async(
            "deleteTrafficMonitor",
            payload,
            envelope="deletetrafficmonitorresponse",
        )

    def delete_traffic_type(self, payload: DeleteTrafficTypeRequest) -> APIResponse[Dict]:
        """Delete a traffic type."""
        return self._execute(
            "deleteTrafficType",
            payload,
            envelope="deletetraffictyperesponse",
        )

    async def delete_traffic_type_async(
        self, payload: DeleteTrafficTypeRequest
    ) -> APIResponse[Dict]:
        """Asynchronously delete a traffic type."""
        return await self._execute_async(
            "deleteTrafficType",
            payload,
            envelope="deletetraffictyperesponse",
        )

    # Disable/Enable operations

    def disable_cisco_nexus_vsm(self, payload: DisableCiscoNexusVSMRequest) -> APIResponse[Dict]:
        """Disable a Cisco Nexus VSM."""
        return self._execute(
            "disableCiscoNexusVSM",
            payload,
            envelope="disablecisconexusvsmresponse",
        )

    async def disable_cisco_nexus_vsm_async(
        self, payload: DisableCiscoNexusVSMRequest
    ) -> APIResponse[Dict]:
        """Asynchronously disable a Cisco Nexus VSM."""
        return await self._execute_async(
            "disableCiscoNexusVSM",
            payload,
            envelope="disablecisconexusvsmresponse",
        )

    def enable_cisco_nexus_vsm(self, payload: EnableCiscoNexusVSMRequest) -> APIResponse[Dict]:
        """Enable a Cisco Nexus VSM."""
        return self._execute(
            "enableCiscoNexusVSM",
            payload,
            envelope="enablecisconexusvsmresponse",
        )

    async def enable_cisco_nexus_vsm_async(
        self, payload: EnableCiscoNexusVSMRequest
    ) -> APIResponse[Dict]:
        """Asynchronously enable a Cisco Nexus VSM."""
        return await self._execute_async(
            "enableCiscoNexusVSM",
            payload,
            envelope="enablecisconexusvsmresponse",
        )

    # List operations

    def list_cisco_nexus_vsms(self, payload: ListCiscoNexusVSMsRequest) -> APIResponse[List[Dict]]:
        """List Cisco Nexus VSMs."""
        return self._execute(
            "listCiscoNexusVSMs",
            payload,
            envelope="listcisconexusvsmsresponse",
            entity="cisconexusvsm",
        )

    async def list_cisco_nexus_vsms_async(
        self, payload: ListCiscoNexusVSMsRequest
    ) -> APIResponse[List[Dict]]:
        """Asynchronously list Cisco Nexus VSMs."""
        return await self._execute_async(
            "listCiscoNexusVSMs",
            payload,
            envelope="listcisconexusvsmsresponse",
            entity="cisconexusvsm",
        )

    def list_guest_network_ipv6_prefixes(
        self, payload: ListGuestNetworkIpv6PrefixesRequest
    ) -> APIResponse[List[Dict]]:
        """List guest network IPv6 prefixes."""
        return self._execute(
            "listGuestNetworkIpv6Prefixes",
            payload,
            envelope="listguestnetworkipv6prefixesresponse",
            entity="guestnetworkipv6prefix",
        )

    async def list_guest_network_ipv6_prefixes_async(
        self, payload: ListGuestNetworkIpv6PrefixesRequest
    ) -> APIResponse[List[Dict]]:
        """Asynchronously list guest network IPv6 prefixes."""
        return await self._execute_async(
            "listGuestNetworkIpv6Prefixes",
            payload,
            envelope="listguestnetworkipv6prefixesresponse",
            entity="guestnetworkipv6prefix",
        )

    def list_ipv4_subnets_for_guest_network(
        self, payload: ListIpv4SubnetsForGuestNetworkRequest
    ) -> APIResponse[List[Dict]]:
        """List IPv4 subnets for a guest network."""
        return self._execute(
            "listIpv4SubnetsForGuestNetwork",
            payload,
            envelope="listipv4subnetsforguestnetworkresponse",
            entity="ipv4subnet",
        )

    async def list_ipv4_subnets_for_guest_network_async(
        self, payload: ListIpv4SubnetsForGuestNetworkRequest
    ) -> APIResponse[List[Dict]]:
        """Asynchronously list IPv4 subnets for a guest network."""
        return await self._execute_async(
            "listIpv4SubnetsForGuestNetwork",
            payload,
            envelope="listipv4subnetsforguestnetworkresponse",
            entity="ipv4subnet",
        )

    def list_network_isolation_methods(
        self, payload: ListNetworkIsolationMethodsRequest
    ) -> APIResponse[List[Dict]]:
        """List network isolation methods."""
        return self._execute(
            "listNetworkIsolationMethods",
            payload,
            envelope="listnetworkisolationmethodsresponse",
            entity="isolationmethod",
        )

    async def list_network_isolation_methods_async(
        self, payload: ListNetworkIsolationMethodsRequest
    ) -> APIResponse[List[Dict]]:
        """Asynchronously list network isolation methods."""
        return await self._execute_async(
            "listNetworkIsolationMethods",
            payload,
            envelope="listnetworkisolationmethodsresponse",
            entity="isolationmethod",
        )

    def list_network_permissions(
        self, payload: ListNetworkPermissionsRequest
    ) -> APIResponse[List[Dict]]:
        """List network permissions."""
        return self._execute(
            "listNetworkPermissions",
            payload,
            envelope="listnetworkpermissionsresponse",
            entity="networkpermission",
        )

    async def list_network_permissions_async(
        self, payload: ListNetworkPermissionsRequest
    ) -> APIResponse[List[Dict]]:
        """Asynchronously list network permissions."""
        return await self._execute_async(
            "listNetworkPermissions",
            payload,
            envelope="listnetworkpermissionsresponse",
            entity="networkpermission",
        )

    def list_network_protocols(
        self, payload: ListNetworkProtocolsRequest
    ) -> APIResponse[List[Dict]]:
        """List network protocols."""
        return self._execute(
            "listNetworkProtocols",
            payload,
            envelope="listnetworkprotocolsresponse",
            entity="networkprotocol",
        )

    async def list_network_protocols_async(
        self, payload: ListNetworkProtocolsRequest
    ) -> APIResponse[List[Dict]]:
        """Asynchronously list network protocols."""
        return await self._execute_async(
            "listNetworkProtocols",
            payload,
            envelope="listnetworkprotocolsresponse",
            entity="networkprotocol",
        )

    def list_opendaylight_controllers(
        self, payload: ListOpenDaylightControllersRequest
    ) -> APIResponse[List[Dict]]:
        """List OpenDaylight controllers."""
        return self._execute(
            "listOpenDaylightControllers",
            payload,
            envelope="listopendaylightcontrollersresponse",
            entity="opendaylightcontroller",
        )

    async def list_opendaylight_controllers_async(
        self, payload: ListOpenDaylightControllersRequest
    ) -> APIResponse[List[Dict]]:
        """Asynchronously list OpenDaylight controllers."""
        return await self._execute_async(
            "listOpenDaylightControllers",
            payload,
            envelope="listopendaylightcontrollersresponse",
            entity="opendaylightcontroller",
        )

    def list_physical_networks(
        self, payload: ListPhysicalNetworksRequest
    ) -> APIResponse[List[Dict]]:
        """List physical networks."""
        return self._execute(
            "listPhysicalNetworks",
            payload,
            envelope="listphysicalnetworksresponse",
            entity="physicalnetwork",
        )

    async def list_physical_networks_async(
        self, payload: ListPhysicalNetworksRequest
    ) -> APIResponse[List[Dict]]:
        """Asynchronously list physical networks."""
        return await self._execute_async(
            "listPhysicalNetworks",
            payload,
            envelope="listphysicalnetworksresponse",
            entity="physicalnetwork",
        )

    def list_storage_network_ip_range(
        self, payload: ListStorageNetworkIpRangeRequest
    ) -> APIResponse[List[Dict]]:
        """List storage network IP ranges."""
        return self._execute(
            "listStorageNetworkIpRange",
            payload,
            envelope="liststoragenetworkiprangeresponse",
            entity="storagenetworkiprange",
        )

    async def list_storage_network_ip_range_async(
        self, payload: ListStorageNetworkIpRangeRequest
    ) -> APIResponse[List[Dict]]:
        """Asynchronously list storage network IP ranges."""
        return await self._execute_async(
            "listStorageNetworkIpRange",
            payload,
            envelope="liststoragenetworkiprangeresponse",
            entity="storagenetworkiprange",
        )

    def list_supported_network_services(
        self, payload: ListSupportedNetworkServicesRequest
    ) -> APIResponse[List[Dict]]:
        """List supported network services."""
        return self._execute(
            "listSupportedNetworkServices",
            payload,
            envelope="listsupportednetworkservicesresponse",
            entity="networkservice",
        )

    async def list_supported_network_services_async(
        self, payload: ListSupportedNetworkServicesRequest
    ) -> APIResponse[List[Dict]]:
        """Asynchronously list supported network services."""
        return await self._execute_async(
            "listSupportedNetworkServices",
            payload,
            envelope="listsupportednetworkservicesresponse",
            entity="networkservice",
        )

    def list_traffic_monitors(self, payload: ListTrafficMonitorsRequest) -> APIResponse[List[Dict]]:
        """List traffic monitors."""
        return self._execute(
            "listTrafficMonitors",
            payload,
            envelope="listtrafficmonitorsresponse",
            entity="trafficmonitor",
        )

    async def list_traffic_monitors_async(
        self, payload: ListTrafficMonitorsRequest
    ) -> APIResponse[List[Dict]]:
        """Asynchronously list traffic monitors."""
        return await self._execute_async(
            "listTrafficMonitors",
            payload,
            envelope="listtrafficmonitorsresponse",
            entity="trafficmonitor",
        )

    def list_traffic_type_implementors(
        self, payload: ListTrafficTypeImplementorsRequest
    ) -> APIResponse[List[Dict]]:
        """List traffic type implementors."""
        return self._execute(
            "listTrafficTypeImplementors",
            payload,
            envelope="listtraffictypeimplementorsresponse",
            entity="traffictype",
        )

    async def list_traffic_type_implementors_async(
        self, payload: ListTrafficTypeImplementorsRequest
    ) -> APIResponse[List[Dict]]:
        """Asynchronously list traffic type implementors."""
        return await self._execute_async(
            "listTrafficTypeImplementors",
            payload,
            envelope="listtraffictypeimplementorsresponse",
            entity="traffictype",
        )

    def list_traffic_types(self, payload: ListTrafficTypesRequest) -> APIResponse[List[Dict]]:
        """List traffic types."""
        return self._execute(
            "listTrafficTypes",
            payload,
            envelope="listtraffictypesresponse",
            entity="traffictype",
        )

    async def list_traffic_types_async(
        self, payload: ListTrafficTypesRequest
    ) -> APIResponse[List[Dict]]:
        """Asynchronously list traffic types."""
        return await self._execute_async(
            "listTrafficTypes",
            payload,
            envelope="listtraffictypesresponse",
            entity="traffictype",
        )

    # Release operation

    def release_public_ip_range(self, payload: ReleasePublicIpRangeRequest) -> APIResponse[Dict]:
        """Release a public IP range."""
        return self._execute(
            "releasePublicIpRange",
            payload,
            envelope="releasepubliciprangeresponse",
        )

    async def release_public_ip_range_async(
        self, payload: ReleasePublicIpRangeRequest
    ) -> APIResponse[Dict]:
        """Asynchronously release a public IP range."""
        return await self._execute_async(
            "releasePublicIpRange",
            payload,
            envelope="releasepubliciprangeresponse",
        )

    # Remove/Reset operations

    def remove_network_permissions(
        self, payload: RemoveNetworkPermissionsRequest
    ) -> APIResponse[Dict]:
        """Remove network permissions."""
        return self._execute(
            "removeNetworkPermissions",
            payload,
            envelope="removenetworkpermissionsresponse",
        )

    async def remove_network_permissions_async(
        self, payload: RemoveNetworkPermissionsRequest
    ) -> APIResponse[Dict]:
        """Asynchronously remove network permissions."""
        return await self._execute_async(
            "removeNetworkPermissions",
            payload,
            envelope="removenetworkpermissionsresponse",
        )

    def reset_network_permissions(
        self, payload: ResetNetworkPermissionsRequest
    ) -> APIResponse[Dict]:
        """Reset network permissions."""
        return self._execute(
            "resetNetworkPermissions",
            payload,
            envelope="resetnetworkpermissionsresponse",
        )

    async def reset_network_permissions_async(
        self, payload: ResetNetworkPermissionsRequest
    ) -> APIResponse[Dict]:
        """Asynchronously reset network permissions."""
        return await self._execute_async(
            "resetNetworkPermissions",
            payload,
            envelope="resetnetworkpermissionsresponse",
        )

    # Update operations

    def update_network_service_provider(
        self, payload: UpdateNetworkServiceProviderRequest
    ) -> APIResponse[Dict]:
        """Update a network service provider."""
        return self._execute(
            "updateNetworkServiceProvider",
            payload,
            envelope="updatenetworkserviceproviderresponse",
        )

    async def update_network_service_provider_async(
        self, payload: UpdateNetworkServiceProviderRequest
    ) -> APIResponse[Dict]:
        """Asynchronously update a network service provider."""
        return await self._execute_async(
            "updateNetworkServiceProvider",
            payload,
            envelope="updatenetworkserviceproviderresponse",
        )

    def update_physical_network(self, payload: UpdatePhysicalNetworkRequest) -> APIResponse[Dict]:
        """Update a physical network."""
        return self._execute(
            "updatePhysicalNetwork",
            payload,
            envelope="updatephysicalnetworkresponse",
        )

    async def update_physical_network_async(
        self, payload: UpdatePhysicalNetworkRequest
    ) -> APIResponse[Dict]:
        """Asynchronously update a physical network."""
        return await self._execute_async(
            "updatePhysicalNetwork",
            payload,
            envelope="updatephysicalnetworkresponse",
        )

    def update_storage_network_ip_range(
        self, payload: UpdateStorageNetworkIpRangeRequest
    ) -> APIResponse[Dict]:
        """Update a storage network IP range."""
        return self._execute(
            "updateStorageNetworkIpRange",
            payload,
            envelope="updatestoragenetworkiprangeresponse",
        )

    async def update_storage_network_ip_range_async(
        self, payload: UpdateStorageNetworkIpRangeRequest
    ) -> APIResponse[Dict]:
        """Asynchronously update a storage network IP range."""
        return await self._execute_async(
            "updateStorageNetworkIpRange",
            payload,
            envelope="updatestoragenetworkiprangeresponse",
        )

    def update_traffic_type(self, payload: UpdateTrafficTypeRequest) -> APIResponse[Dict]:
        """Update a traffic type."""
        return self._execute(
            "updateTrafficType",
            payload,
            envelope="updatetraffictyperesponse",
        )

    async def update_traffic_type_async(
        self, payload: UpdateTrafficTypeRequest
    ) -> APIResponse[Dict]:
        """Asynchronously update a traffic type."""
        return await self._execute_async(
            "updateTrafficType",
            payload,
            envelope="updatetraffictyperesponse",
        )
