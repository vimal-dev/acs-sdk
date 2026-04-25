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
        response = self.client.call("listNetworks", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listnetworksresponse' in response:
            response = response['listnetworksresponse']
        if 'network' in response and response['network']:
            data = response['network']
            count = response.get('count', 0)
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    async def list_async(self, payload: ListNetworkRequest) -> APIResponse[List[Dict]]:
        """Asynchronously list all available networks.
        
        Args:
            payload (ListNetworkRequest): The request payload containing filter options.
            
        Returns:
            APIResponse[List[Dict]]: A response containing a list of networks.
        """
        response = await self.client.call_async("listNetworks", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listnetworksresponse' in response:
            response = response['listnetworksresponse']
        if 'network' in response and response['network']:
            data = response['network']
            count = response.get('count', 0)
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    def create(self, payload: CreateNetworkRequest) -> APIResponse[Dict]:
        """Create a new network.
        
        Args:
            payload (CreateNetworkRequest): The request payload containing network creation parameters.
            
        Returns:
            APIResponse[Dict]: A response containing the created network.
        """
        response = self.client.call("createNetwork", payload.model_dump(exclude_none=True))
        data = {}
        if 'createnetworkresponse' in response:
            data = response['createnetworkresponse']
        return APIResponse[Dict](**{"data": data})

    async def create_async(self, payload: CreateNetworkRequest) -> APIResponse[Dict]:
        """Asynchronously create a new network.
        
        Args:
            payload (CreateNetworkRequest): The request payload containing network creation parameters.
            
        Returns:
            APIResponse[Dict]: A response containing the created network.
        """
        response = await self.client.call_async("createNetwork", payload.model_dump(exclude_none=True))
        data = {}
        if 'createnetworkresponse' in response:
            data = response['createnetworkresponse']
        return APIResponse[Dict](**{"data": data})

    def delete(self, payload: DeleteNetworkRequest) -> APIResponse[Dict]:
        """Delete a network.
        
        Args:
            payload (DeleteNetworkRequest): The request payload containing the network ID to delete.
            
        Returns:
            APIResponse[Dict]: A response indicating success or failure.
        """
        response = self.client.call("deleteNetwork", payload.model_dump(exclude_none=True))
        data = {}
        if 'deletenetworkresponse' in response:
            data = response['deletenetworkresponse']
        return APIResponse[Dict](**{"data": data})

    async def delete_async(self, payload: DeleteNetworkRequest) -> APIResponse[Dict]:
        """Asynchronously delete a network.
        
        Args:
            payload (DeleteNetworkRequest): The request payload containing the network ID to delete.
            
        Returns:
            APIResponse[Dict]: A response indicating success or failure.
        """
        response = await self.client.call_async("deleteNetwork", payload.model_dump(exclude_none=True))
        data = {}
        if 'deletenetworkresponse' in response:
            data = response['deletenetworkresponse']
        return APIResponse[Dict](**{"data": data})

    def update(self, payload: UpdateNetworkRequest) -> APIResponse[Dict]:
        """Update a network.
        
        Args:
            payload (UpdateNetworkRequest): The request payload containing network update parameters.
            
        Returns:
            APIResponse[Dict]: A response containing the updated network.
        """
        response = self.client.call("updateNetwork", payload.model_dump(exclude_none=True))
        data = {}
        if 'updatenetworkresponse' in response:
            data = response['updatenetworkresponse']
        return APIResponse[Dict](**{"data": data})

    async def update_async(self, payload: UpdateNetworkRequest) -> APIResponse[Dict]:
        """Asynchronously update a network.
        
        Args:
            payload (UpdateNetworkRequest): The request payload containing network update parameters.
            
        Returns:
            APIResponse[Dict]: A response containing the updated network.
        """
        response = await self.client.call_async("updateNetwork", payload.model_dump(exclude_none=True))
        data = {}
        if 'updatenetworkresponse' in response:
            data = response['updatenetworkresponse']
        return APIResponse[Dict](**{"data": data})

    def restart(self, payload: RestartNetworkRequest) -> APIResponse[Dict]:
        """Restart a network. This operation stops and starts the network.
        
        Args:
            payload (RestartNetworkRequest): The request payload containing the network ID to restart.
            
        Returns:
            APIResponse[Dict]: A response indicating the restart operation status.
        """
        response = self.client.call("restartNetwork", payload.model_dump(exclude_none=True))
        data = {}
        if 'restartnetworkresponse' in response:
            data = response['restartnetworkresponse']
        return APIResponse[Dict](**{"data": data})

    async def restart_async(self, payload: RestartNetworkRequest) -> APIResponse[Dict]:
        """Asynchronously restart a network.
        
        Args:
            payload (RestartNetworkRequest): The request payload containing the network ID to restart.
            
        Returns:
            APIResponse[Dict]: A response indicating the restart operation status.
        """
        response = await self.client.call_async("restartNetwork", payload.model_dump(exclude_none=True))
        data = {}
        if 'restartnetworkresponse' in response:
            data = response['restartnetworkresponse']
        return APIResponse[Dict](**{"data": data})

    def migrate(self, payload: MigrateNetworkRequest) -> APIResponse[Dict]:
        """Migrate a network to a different physical network.
        
        Args:
            payload (MigrateNetworkRequest): The request payload containing migration parameters.
            
        Returns:
            APIResponse[Dict]: A response containing the migrated network.
        """
        response = self.client.call("migrateNetwork", payload.model_dump(exclude_none=True))
        data = {}
        if 'migratenetworkresponse' in response:
            data = response['migratenetworkresponse']
        return APIResponse[Dict](**{"data": data})

    async def migrate_async(self, payload: MigrateNetworkRequest) -> APIResponse[Dict]:
        """Asynchronously migrate a network to a different physical network.
        
        Args:
            payload (MigrateNetworkRequest): The request payload containing migration parameters.
            
        Returns:
            APIResponse[Dict]: A response containing the migrated network.
        """
        response = await self.client.call_async("migrateNetwork", payload.model_dump(exclude_none=True))
        data = {}
        if 'migratenetworkresponse' in response:
            data = response['migratenetworkresponse']
        return APIResponse[Dict](**{"data": data})

    def release(self, payload: ReleaseNetworkRequest) -> APIResponse[Dict]:
        """Release a network. This deallocates and removes the network.
        
        Args:
            payload (ReleaseNetworkRequest): The request payload containing the network ID to release.
            
        Returns:
            APIResponse[Dict]: A response indicating success or failure.
        """
        response = self.client.call("releaseNetwork", payload.model_dump(exclude_none=True))
        data = {}
        if 'releasenetworkresponse' in response:
            data = response['releasenetworkresponse']
        return APIResponse[Dict](**{"data": data})

    async def release_async(self, payload: ReleaseNetworkRequest) -> APIResponse[Dict]:
        """Asynchronously release a network.
        
        Args:
            payload (ReleaseNetworkRequest): The request payload containing the network ID to release.
            
        Returns:
            APIResponse[Dict]: A response indicating success or failure.
        """
        response = await self.client.call_async("releaseNetwork", payload.model_dump(exclude_none=True))
        data = {}
        if 'releasenetworkresponse' in response:
            data = response['releasenetworkresponse']
        return APIResponse[Dict](**{"data": data})

    def list_service_providers(self, payload: ListNetworkServiceProvidersRequest) -> APIResponse[List[Dict]]:
        """List network service providers.
        
        Args:
            payload (ListNetworkServiceProvidersRequest): The request payload containing filter options.
            
        Returns:
            APIResponse[List[Dict]]: A response containing a list of network service providers.
        """
        response = self.client.call("listNetworkServiceProviders", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listnetworkserviceprovidersresponse' in response:
            response = response['listnetworkserviceprovidersresponse']
        if 'networkserviceprovider' in response and response['networkserviceprovider']:
            data = response['networkserviceprovider']
            count = response.get('count', 0)
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    async def list_service_providers_async(self, payload: ListNetworkServiceProvidersRequest) -> APIResponse[List[Dict]]:
        """Asynchronously list network service providers.
        
        Args:
            payload (ListNetworkServiceProvidersRequest): The request payload containing filter options.
            
        Returns:
            APIResponse[List[Dict]]: A response containing a list of network service providers.
        """
        response = await self.client.call_async("listNetworkServiceProviders", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listnetworkserviceprovidersresponse' in response:
            response = response['listnetworkserviceprovidersresponse']
        if 'networkserviceprovider' in response and response['networkserviceprovider']:
            data = response['networkserviceprovider']
            count = response.get('count', 0)
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    def list_services(self, payload: ListNetworkServicesRequest) -> APIResponse[List[Dict]]:
        """List network services.
        
        Args:
            payload (ListNetworkServicesRequest): The request payload containing filter options.
            
        Returns:
            APIResponse[List[Dict]]: A response containing a list of network services.
        """
        response = self.client.call("listNetworkServices", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listnetworkservicesresponse' in response:
            response = response['listnetworkservicesresponse']
        if 'networkservice' in response and response['networkservice']:
            data = response['networkservice']
            count = response.get('count', 0)
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    async def list_services_async(self, payload: ListNetworkServicesRequest) -> APIResponse[List[Dict]]:
        """Asynchronously list network services.
        
        Args:
            payload (ListNetworkServicesRequest): The request payload containing filter options.
            
        Returns:
            APIResponse[List[Dict]]: A response containing a list of network services.
        """
        response = await self.client.call_async("listNetworkServices", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listnetworkservicesresponse' in response:
            response = response['listnetworkservicesresponse']
        if 'networkservice' in response and response['networkservice']:
            data = response['networkservice']
            count = response.get('count', 0)
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    # Add operations

    def add_globo_dns_host(self, payload: AddGloboDnsHostRequest) -> APIResponse[Dict]:
        """Add a Globo DNS host."""
        response = self.client.call("addGloboDnsHost", payload.model_dump(exclude_none=True))
        data = {}
        if 'addglobodnshostresponse' in response:
            data = response['addglobodnshostresponse']
        return APIResponse[Dict](**{"data": data})

    async def add_globo_dns_host_async(self, payload: AddGloboDnsHostRequest) -> APIResponse[Dict]:
        """Asynchronously add a Globo DNS host."""
        response = await self.client.call_async("addGloboDnsHost", payload.model_dump(exclude_none=True))
        data = {}
        if 'addglobodnshostresponse' in response:
            data = response['addglobodnshostresponse']
        return APIResponse[Dict](**{"data": data})

    def add_network_service_provider(self, payload: AddNetworkServiceProviderRequest) -> APIResponse[Dict]:
        """Add a network service provider."""
        response = self.client.call("addNetworkServiceProvider", payload.model_dump(exclude_none=True))
        data = {}
        if 'addnetworkserviceproviderresponse' in response:
            data = response['addnetworkserviceproviderresponse']
        return APIResponse[Dict](**{"data": data})

    async def add_network_service_provider_async(self, payload: AddNetworkServiceProviderRequest) -> APIResponse[Dict]:
        """Asynchronously add a network service provider."""
        response = await self.client.call_async("addNetworkServiceProvider", payload.model_dump(exclude_none=True))
        data = {}
        if 'addnetworkserviceproviderresponse' in response:
            data = response['addnetworkserviceproviderresponse']
        return APIResponse[Dict](**{"data": data})

    def add_opendaylight_controller(self, payload: AddOpenDaylightControllerRequest) -> APIResponse[Dict]:
        """Add an OpenDaylight controller."""
        response = self.client.call("addOpenDaylightController", payload.model_dump(exclude_none=True))
        data = {}
        if 'addopendaylightcontrollerresponse' in response:
            data = response['addopendaylightcontrollerresponse']
        return APIResponse[Dict](**{"data": data})

    async def add_opendaylight_controller_async(self, payload: AddOpenDaylightControllerRequest) -> APIResponse[Dict]:
        """Asynchronously add an OpenDaylight controller."""
        response = await self.client.call_async("addOpenDaylightController", payload.model_dump(exclude_none=True))
        data = {}
        if 'addopendaylightcontrollerresponse' in response:
            data = response['addopendaylightcontrollerresponse']
        return APIResponse[Dict](**{"data": data})

    def add_traffic_monitor(self, payload: AddTrafficMonitorRequest) -> APIResponse[Dict]:
        """Add a traffic monitor."""
        response = self.client.call("addTrafficMonitor", payload.model_dump(exclude_none=True))
        data = {}
        if 'addtrafficmonitorresponse' in response:
            data = response['addtrafficmonitorresponse']
        return APIResponse[Dict](**{"data": data})

    async def add_traffic_monitor_async(self, payload: AddTrafficMonitorRequest) -> APIResponse[Dict]:
        """Asynchronously add a traffic monitor."""
        response = await self.client.call_async("addTrafficMonitor", payload.model_dump(exclude_none=True))
        data = {}
        if 'addtrafficmonitorresponse' in response:
            data = response['addtrafficmonitorresponse']
        return APIResponse[Dict](**{"data": data})

    def add_traffic_type(self, payload: AddTrafficTypeRequest) -> APIResponse[Dict]:
        """Add a traffic type to a physical network."""
        response = self.client.call("addTrafficType", payload.model_dump(exclude_none=True))
        data = {}
        if 'addtraffictyperesponse' in response:
            data = response['addtraffictyperesponse']
        return APIResponse[Dict](**{"data": data})

    async def add_traffic_type_async(self, payload: AddTrafficTypeRequest) -> APIResponse[Dict]:
        """Asynchronously add a traffic type to a physical network."""
        response = await self.client.call_async("addTrafficType", payload.model_dump(exclude_none=True))
        data = {}
        if 'addtraffictyperesponse' in response:
            data = response['addtraffictyperesponse']
        return APIResponse[Dict](**{"data": data})

    # Create operations

    def change_bgp_peers_for_network(self, payload: ChangeBgpPeersForNetworkRequest) -> APIResponse[Dict]:
        """Change BGP peers for a network."""
        response = self.client.call("changeBgpPeersForNetwork", payload.model_dump(exclude_none=True))
        data = {}
        if 'changebgppeersfornetworkresponse' in response:
            data = response['changebgppeersfornetworkresponse']
        return APIResponse[Dict](**{"data": data})

    async def change_bgp_peers_for_network_async(self, payload: ChangeBgpPeersForNetworkRequest) -> APIResponse[Dict]:
        """Asynchronously change BGP peers for a network."""
        response = await self.client.call_async("changeBgpPeersForNetwork", payload.model_dump(exclude_none=True))
        data = {}
        if 'changebgppeersfornetworkresponse' in response:
            data = response['changebgppeersfornetworkresponse']
        return APIResponse[Dict](**{"data": data})

    def create_guest_network_ipv6_prefix(self, payload: CreateGuestNetworkIpv6PrefixRequest) -> APIResponse[Dict]:
        """Create a guest network IPv6 prefix."""
        response = self.client.call("createGuestNetworkIpv6Prefix", payload.model_dump(exclude_none=True))
        data = {}
        if 'createguestnetworkipv6prefixresponse' in response:
            data = response['createguestnetworkipv6prefixresponse']
        return APIResponse[Dict](**{"data": data})

    async def create_guest_network_ipv6_prefix_async(self, payload: CreateGuestNetworkIpv6PrefixRequest) -> APIResponse[Dict]:
        """Asynchronously create a guest network IPv6 prefix."""
        response = await self.client.call_async("createGuestNetworkIpv6Prefix", payload.model_dump(exclude_none=True))
        data = {}
        if 'createguestnetworkipv6prefixresponse' in response:
            data = response['createguestnetworkipv6prefixresponse']
        return APIResponse[Dict](**{"data": data})

    def create_ipv4_subnet_for_guest_network(self, payload: CreateIpv4SubnetForGuestNetworkRequest) -> APIResponse[Dict]:
        """Create an IPv4 subnet for a guest network."""
        response = self.client.call("createIpv4SubnetForGuestNetwork", payload.model_dump(exclude_none=True))
        data = {}
        if 'createipv4subnetforguestnetworkresponse' in response:
            data = response['createipv4subnetforguestnetworkresponse']
        return APIResponse[Dict](**{"data": data})

    async def create_ipv4_subnet_for_guest_network_async(self, payload: CreateIpv4SubnetForGuestNetworkRequest) -> APIResponse[Dict]:
        """Asynchronously create an IPv4 subnet for a guest network."""
        response = await self.client.call_async("createIpv4SubnetForGuestNetwork", payload.model_dump(exclude_none=True))
        data = {}
        if 'createipv4subnetforguestnetworkresponse' in response:
            data = response['createipv4subnetforguestnetworkresponse']
        return APIResponse[Dict](**{"data": data})

    def create_network_permissions(self, payload: CreateNetworkPermissionsRequest) -> APIResponse[Dict]:
        """Create network permissions."""
        response = self.client.call("createNetworkPermissions", payload.model_dump(exclude_none=True))
        data = {}
        if 'createnetworkpermissionsresponse' in response:
            data = response['createnetworkpermissionsresponse']
        return APIResponse[Dict](**{"data": data})

    async def create_network_permissions_async(self, payload: CreateNetworkPermissionsRequest) -> APIResponse[Dict]:
        """Asynchronously create network permissions."""
        response = await self.client.call_async("createNetworkPermissions", payload.model_dump(exclude_none=True))
        data = {}
        if 'createnetworkpermissionsresponse' in response:
            data = response['createnetworkpermissionsresponse']
        return APIResponse[Dict](**{"data": data})

    def create_physical_network(self, payload: CreatePhysicalNetworkRequest) -> APIResponse[Dict]:
        """Create a physical network."""
        response = self.client.call("createPhysicalNetwork", payload.model_dump(exclude_none=True))
        data = {}
        if 'createphysicalnetworkresponse' in response:
            data = response['createphysicalnetworkresponse']
        return APIResponse[Dict](**{"data": data})

    async def create_physical_network_async(self, payload: CreatePhysicalNetworkRequest) -> APIResponse[Dict]:
        """Asynchronously create a physical network."""
        response = await self.client.call_async("createPhysicalNetwork", payload.model_dump(exclude_none=True))
        data = {}
        if 'createphysicalnetworkresponse' in response:
            data = response['createphysicalnetworkresponse']
        return APIResponse[Dict](**{"data": data})

    def create_service_instance(self, payload: CreateServiceInstanceRequest) -> APIResponse[Dict]:
        """Create a service instance."""
        response = self.client.call("createServiceInstance", payload.model_dump(exclude_none=True))
        data = {}
        if 'createserviceinstanceresponse' in response:
            data = response['createserviceinstanceresponse']
        return APIResponse[Dict](**{"data": data})

    async def create_service_instance_async(self, payload: CreateServiceInstanceRequest) -> APIResponse[Dict]:
        """Asynchronously create a service instance."""
        response = await self.client.call_async("createServiceInstance", payload.model_dump(exclude_none=True))
        data = {}
        if 'createserviceinstanceresponse' in response:
            data = response['createserviceinstanceresponse']
        return APIResponse[Dict](**{"data": data})

    def create_storage_network_ip_range(self, payload: CreateStorageNetworkIpRangeRequest) -> APIResponse[Dict]:
        """Create a storage network IP range."""
        response = self.client.call("createStorageNetworkIpRange", payload.model_dump(exclude_none=True))
        data = {}
        if 'createstoragenetworkiprangeresponse' in response:
            data = response['createstoragenetworkiprangeresponse']
        return APIResponse[Dict](**{"data": data})

    async def create_storage_network_ip_range_async(self, payload: CreateStorageNetworkIpRangeRequest) -> APIResponse[Dict]:
        """Asynchronously create a storage network IP range."""
        response = await self.client.call_async("createStorageNetworkIpRange", payload.model_dump(exclude_none=True))
        data = {}
        if 'createstoragenetworkiprangeresponse' in response:
            data = response['createstoragenetworkiprangeresponse']
        return APIResponse[Dict](**{"data": data})

    # Delete operations

    def delete_cisco_nexus_vsm(self, payload: DeleteCiscoNexusVSMRequest) -> APIResponse[Dict]:
        """Delete a Cisco Nexus VSM."""
        response = self.client.call("deleteCiscoNexusVSM", payload.model_dump(exclude_none=True))
        data = {}
        if 'deletecisconexusvsmresponse' in response:
            data = response['deletecisconexusvsmresponse']
        return APIResponse[Dict](**{"data": data})

    async def delete_cisco_nexus_vsm_async(self, payload: DeleteCiscoNexusVSMRequest) -> APIResponse[Dict]:
        """Asynchronously delete a Cisco Nexus VSM."""
        response = await self.client.call_async("deleteCiscoNexusVSM", payload.model_dump(exclude_none=True))
        data = {}
        if 'deletecisconexusvsmresponse' in response:
            data = response['deletecisconexusvsmresponse']
        return APIResponse[Dict](**{"data": data})

    def delete_guest_network_ipv6_prefix(self, payload: DeleteGuestNetworkIpv6PrefixRequest) -> APIResponse[Dict]:
        """Delete a guest network IPv6 prefix."""
        response = self.client.call("deleteGuestNetworkIpv6Prefix", payload.model_dump(exclude_none=True))
        data = {}
        if 'deleteguestnetworkipv6prefixresponse' in response:
            data = response['deleteguestnetworkipv6prefixresponse']
        return APIResponse[Dict](**{"data": data})

    async def delete_guest_network_ipv6_prefix_async(self, payload: DeleteGuestNetworkIpv6PrefixRequest) -> APIResponse[Dict]:
        """Asynchronously delete a guest network IPv6 prefix."""
        response = await self.client.call_async("deleteGuestNetworkIpv6Prefix", payload.model_dump(exclude_none=True))
        data = {}
        if 'deleteguestnetworkipv6prefixresponse' in response:
            data = response['deleteguestnetworkipv6prefixresponse']
        return APIResponse[Dict](**{"data": data})

    def delete_ipv4_subnet_for_guest_network(self, payload: DeleteIpv4SubnetForGuestNetworkRequest) -> APIResponse[Dict]:
        """Delete an IPv4 subnet for a guest network."""
        response = self.client.call("deleteIpv4SubnetForGuestNetwork", payload.model_dump(exclude_none=True))
        data = {}
        if 'deleteipv4subnetforguestnetworkresponse' in response:
            data = response['deleteipv4subnetforguestnetworkresponse']
        return APIResponse[Dict](**{"data": data})

    async def delete_ipv4_subnet_for_guest_network_async(self, payload: DeleteIpv4SubnetForGuestNetworkRequest) -> APIResponse[Dict]:
        """Asynchronously delete an IPv4 subnet for a guest network."""
        response = await self.client.call_async("deleteIpv4SubnetForGuestNetwork", payload.model_dump(exclude_none=True))
        data = {}
        if 'deleteipv4subnetforguestnetworkresponse' in response:
            data = response['deleteipv4subnetforguestnetworkresponse']
        return APIResponse[Dict](**{"data": data})

    def delete_network_service_provider(self, payload: DeleteNetworkServiceProviderRequest) -> APIResponse[Dict]:
        """Delete a network service provider."""
        response = self.client.call("deleteNetworkServiceProvider", payload.model_dump(exclude_none=True))
        data = {}
        if 'deletenetworkserviceproviderresponse' in response:
            data = response['deletenetworkserviceproviderresponse']
        return APIResponse[Dict](**{"data": data})

    async def delete_network_service_provider_async(self, payload: DeleteNetworkServiceProviderRequest) -> APIResponse[Dict]:
        """Asynchronously delete a network service provider."""
        response = await self.client.call_async("deleteNetworkServiceProvider", payload.model_dump(exclude_none=True))
        data = {}
        if 'deletenetworkserviceproviderresponse' in response:
            data = response['deletenetworkserviceproviderresponse']
        return APIResponse[Dict](**{"data": data})

    def delete_opendaylight_controller(self, payload: DeleteOpenDaylightControllerRequest) -> APIResponse[Dict]:
        """Delete an OpenDaylight controller."""
        response = self.client.call("deleteOpenDaylightController", payload.model_dump(exclude_none=True))
        data = {}
        if 'deleteopendaylightcontrollerresponse' in response:
            data = response['deleteopendaylightcontrollerresponse']
        return APIResponse[Dict](**{"data": data})

    async def delete_opendaylight_controller_async(self, payload: DeleteOpenDaylightControllerRequest) -> APIResponse[Dict]:
        """Asynchronously delete an OpenDaylight controller."""
        response = await self.client.call_async("deleteOpenDaylightController", payload.model_dump(exclude_none=True))
        data = {}
        if 'deleteopendaylightcontrollerresponse' in response:
            data = response['deleteopendaylightcontrollerresponse']
        return APIResponse[Dict](**{"data": data})

    def delete_physical_network(self, payload: DeletePhysicalNetworkRequest) -> APIResponse[Dict]:
        """Delete a physical network."""
        response = self.client.call("deletePhysicalNetwork", payload.model_dump(exclude_none=True))
        data = {}
        if 'deletephysicalnetworkresponse' in response:
            data = response['deletephysicalnetworkresponse']
        return APIResponse[Dict](**{"data": data})

    async def delete_physical_network_async(self, payload: DeletePhysicalNetworkRequest) -> APIResponse[Dict]:
        """Asynchronously delete a physical network."""
        response = await self.client.call_async("deletePhysicalNetwork", payload.model_dump(exclude_none=True))
        data = {}
        if 'deletephysicalnetworkresponse' in response:
            data = response['deletephysicalnetworkresponse']
        return APIResponse[Dict](**{"data": data})

    def delete_storage_network_ip_range(self, payload: DeleteStorageNetworkIpRangeRequest) -> APIResponse[Dict]:
        """Delete a storage network IP range."""
        response = self.client.call("deleteStorageNetworkIpRange", payload.model_dump(exclude_none=True))
        data = {}
        if 'deletestoragenetworkiprangeresponse' in response:
            data = response['deletestoragenetworkiprangeresponse']
        return APIResponse[Dict](**{"data": data})

    async def delete_storage_network_ip_range_async(self, payload: DeleteStorageNetworkIpRangeRequest) -> APIResponse[Dict]:
        """Asynchronously delete a storage network IP range."""
        response = await self.client.call_async("deleteStorageNetworkIpRange", payload.model_dump(exclude_none=True))
        data = {}
        if 'deletestoragenetworkiprangeresponse' in response:
            data = response['deletestoragenetworkiprangeresponse']
        return APIResponse[Dict](**{"data": data})

    def delete_traffic_monitor(self, payload: DeleteTrafficMonitorRequest) -> APIResponse[Dict]:
        """Delete a traffic monitor."""
        response = self.client.call("deleteTrafficMonitor", payload.model_dump(exclude_none=True))
        data = {}
        if 'deletetrafficmonitorresponse' in response:
            data = response['deletetrafficmonitorresponse']
        return APIResponse[Dict](**{"data": data})

    async def delete_traffic_monitor_async(self, payload: DeleteTrafficMonitorRequest) -> APIResponse[Dict]:
        """Asynchronously delete a traffic monitor."""
        response = await self.client.call_async("deleteTrafficMonitor", payload.model_dump(exclude_none=True))
        data = {}
        if 'deletetrafficmonitorresponse' in response:
            data = response['deletetrafficmonitorresponse']
        return APIResponse[Dict](**{"data": data})

    def delete_traffic_type(self, payload: DeleteTrafficTypeRequest) -> APIResponse[Dict]:
        """Delete a traffic type."""
        response = self.client.call("deleteTrafficType", payload.model_dump(exclude_none=True))
        data = {}
        if 'deletetraffictyperesponse' in response:
            data = response['deletetraffictyperesponse']
        return APIResponse[Dict](**{"data": data})

    async def delete_traffic_type_async(self, payload: DeleteTrafficTypeRequest) -> APIResponse[Dict]:
        """Asynchronously delete a traffic type."""
        response = await self.client.call_async("deleteTrafficType", payload.model_dump(exclude_none=True))
        data = {}
        if 'deletetraffictyperesponse' in response:
            data = response['deletetraffictyperesponse']
        return APIResponse[Dict](**{"data": data})

    # Disable/Enable operations

    def disable_cisco_nexus_vsm(self, payload: DisableCiscoNexusVSMRequest) -> APIResponse[Dict]:
        """Disable a Cisco Nexus VSM."""
        response = self.client.call("disableCiscoNexusVSM", payload.model_dump(exclude_none=True))
        data = {}
        if 'disablecisconexusvsmresponse' in response:
            data = response['disablecisconexusvsmresponse']
        return APIResponse[Dict](**{"data": data})

    async def disable_cisco_nexus_vsm_async(self, payload: DisableCiscoNexusVSMRequest) -> APIResponse[Dict]:
        """Asynchronously disable a Cisco Nexus VSM."""
        response = await self.client.call_async("disableCiscoNexusVSM", payload.model_dump(exclude_none=True))
        data = {}
        if 'disablecisconexusvsmresponse' in response:
            data = response['disablecisconexusvsmresponse']
        return APIResponse[Dict](**{"data": data})

    def enable_cisco_nexus_vsm(self, payload: EnableCiscoNexusVSMRequest) -> APIResponse[Dict]:
        """Enable a Cisco Nexus VSM."""
        response = self.client.call("enableCiscoNexusVSM", payload.model_dump(exclude_none=True))
        data = {}
        if 'enablecisconexusvsmresponse' in response:
            data = response['enablecisconexusvsmresponse']
        return APIResponse[Dict](**{"data": data})

    async def enable_cisco_nexus_vsm_async(self, payload: EnableCiscoNexusVSMRequest) -> APIResponse[Dict]:
        """Asynchronously enable a Cisco Nexus VSM."""
        response = await self.client.call_async("enableCiscoNexusVSM", payload.model_dump(exclude_none=True))
        data = {}
        if 'enablecisconexusvsmresponse' in response:
            data = response['enablecisconexusvsmresponse']
        return APIResponse[Dict](**{"data": data})

    # List operations

    def list_cisco_nexus_vsms(self, payload: ListCiscoNexusVSMsRequest) -> APIResponse[List[Dict]]:
        """List Cisco Nexus VSMs."""
        response = self.client.call("listCiscoNexusVSMs", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listcisconexusvsmsresponse' in response:
            response = response['listcisconexusvsmsresponse']
        if 'cisconexusvsm' in response and response['cisconexusvsm']:
            data = response['cisconexusvsm']
            count = response.get('count', 0)
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    async def list_cisco_nexus_vsms_async(self, payload: ListCiscoNexusVSMsRequest) -> APIResponse[List[Dict]]:
        """Asynchronously list Cisco Nexus VSMs."""
        response = await self.client.call_async("listCiscoNexusVSMs", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listcisconexusvsmsresponse' in response:
            response = response['listcisconexusvsmsresponse']
        if 'cisconexusvsm' in response and response['cisconexusvsm']:
            data = response['cisconexusvsm']
            count = response.get('count', 0)
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    def list_guest_network_ipv6_prefixes(self, payload: ListGuestNetworkIpv6PrefixesRequest) -> APIResponse[List[Dict]]:
        """List guest network IPv6 prefixes."""
        response = self.client.call("listGuestNetworkIpv6Prefixes", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listguestnetworkipv6prefixesresponse' in response:
            response = response['listguestnetworkipv6prefixesresponse']
        if 'guestnetworkipv6prefix' in response and response['guestnetworkipv6prefix']:
            data = response['guestnetworkipv6prefix']
            count = response.get('count', 0)
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    async def list_guest_network_ipv6_prefixes_async(self, payload: ListGuestNetworkIpv6PrefixesRequest) -> APIResponse[List[Dict]]:
        """Asynchronously list guest network IPv6 prefixes."""
        response = await self.client.call_async("listGuestNetworkIpv6Prefixes", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listguestnetworkipv6prefixesresponse' in response:
            response = response['listguestnetworkipv6prefixesresponse']
        if 'guestnetworkipv6prefix' in response and response['guestnetworkipv6prefix']:
            data = response['guestnetworkipv6prefix']
            count = response.get('count', 0)
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    def list_ipv4_subnets_for_guest_network(self, payload: ListIpv4SubnetsForGuestNetworkRequest) -> APIResponse[List[Dict]]:
        """List IPv4 subnets for a guest network."""
        response = self.client.call("listIpv4SubnetsForGuestNetwork", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listipv4subnetsforguestnetworkresponse' in response:
            response = response['listipv4subnetsforguestnetworkresponse']
        if 'ipv4subnet' in response and response['ipv4subnet']:
            data = response['ipv4subnet']
            count = response.get('count', 0)
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    async def list_ipv4_subnets_for_guest_network_async(self, payload: ListIpv4SubnetsForGuestNetworkRequest) -> APIResponse[List[Dict]]:
        """Asynchronously list IPv4 subnets for a guest network."""
        response = await self.client.call_async("listIpv4SubnetsForGuestNetwork", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listipv4subnetsforguestnetworkresponse' in response:
            response = response['listipv4subnetsforguestnetworkresponse']
        if 'ipv4subnet' in response and response['ipv4subnet']:
            data = response['ipv4subnet']
            count = response.get('count', 0)
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    def list_network_isolation_methods(self, payload: ListNetworkIsolationMethodsRequest) -> APIResponse[List[Dict]]:
        """List network isolation methods."""
        response = self.client.call("listNetworkIsolationMethods", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listnetworkisolationmethodsresponse' in response:
            response = response['listnetworkisolationmethodsresponse']
        if 'isolationmethod' in response and response['isolationmethod']:
            data = response['isolationmethod']
            count = response.get('count', 0)
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    async def list_network_isolation_methods_async(self, payload: ListNetworkIsolationMethodsRequest) -> APIResponse[List[Dict]]:
        """Asynchronously list network isolation methods."""
        response = await self.client.call_async("listNetworkIsolationMethods", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listnetworkisolationmethodsresponse' in response:
            response = response['listnetworkisolationmethodsresponse']
        if 'isolationmethod' in response and response['isolationmethod']:
            data = response['isolationmethod']
            count = response.get('count', 0)
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    def list_network_permissions(self, payload: ListNetworkPermissionsRequest) -> APIResponse[List[Dict]]:
        """List network permissions."""
        response = self.client.call("listNetworkPermissions", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listnetworkpermissionsresponse' in response:
            response = response['listnetworkpermissionsresponse']
        if 'networkpermission' in response and response['networkpermission']:
            data = response['networkpermission']
            count = response.get('count', 0)
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    async def list_network_permissions_async(self, payload: ListNetworkPermissionsRequest) -> APIResponse[List[Dict]]:
        """Asynchronously list network permissions."""
        response = await self.client.call_async("listNetworkPermissions", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listnetworkpermissionsresponse' in response:
            response = response['listnetworkpermissionsresponse']
        if 'networkpermission' in response and response['networkpermission']:
            data = response['networkpermission']
            count = response.get('count', 0)
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    def list_network_protocols(self, payload: ListNetworkProtocolsRequest) -> APIResponse[List[Dict]]:
        """List network protocols."""
        response = self.client.call("listNetworkProtocols", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listnetworkprotocolsresponse' in response:
            response = response['listnetworkprotocolsresponse']
        if 'networkprotocol' in response and response['networkprotocol']:
            data = response['networkprotocol']
            count = response.get('count', 0)
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    async def list_network_protocols_async(self, payload: ListNetworkProtocolsRequest) -> APIResponse[List[Dict]]:
        """Asynchronously list network protocols."""
        response = await self.client.call_async("listNetworkProtocols", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listnetworkprotocolsresponse' in response:
            response = response['listnetworkprotocolsresponse']
        if 'networkprotocol' in response and response['networkprotocol']:
            data = response['networkprotocol']
            count = response.get('count', 0)
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    def list_opendaylight_controllers(self, payload: ListOpenDaylightControllersRequest) -> APIResponse[List[Dict]]:
        """List OpenDaylight controllers."""
        response = self.client.call("listOpenDaylightControllers", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listopendaylightcontrollersresponse' in response:
            response = response['listopendaylightcontrollersresponse']
        if 'opendaylightcontroller' in response and response['opendaylightcontroller']:
            data = response['opendaylightcontroller']
            count = response.get('count', 0)
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    async def list_opendaylight_controllers_async(self, payload: ListOpenDaylightControllersRequest) -> APIResponse[List[Dict]]:
        """Asynchronously list OpenDaylight controllers."""
        response = await self.client.call_async("listOpenDaylightControllers", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listopendaylightcontrollersresponse' in response:
            response = response['listopendaylightcontrollersresponse']
        if 'opendaylightcontroller' in response and response['opendaylightcontroller']:
            data = response['opendaylightcontroller']
            count = response.get('count', 0)
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    def list_physical_networks(self, payload: ListPhysicalNetworksRequest) -> APIResponse[List[Dict]]:
        """List physical networks."""
        response = self.client.call("listPhysicalNetworks", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listphysicalnetworksresponse' in response:
            response = response['listphysicalnetworksresponse']
        if 'physicalnetwork' in response and response['physicalnetwork']:
            data = response['physicalnetwork']
            count = response.get('count', 0)
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    async def list_physical_networks_async(self, payload: ListPhysicalNetworksRequest) -> APIResponse[List[Dict]]:
        """Asynchronously list physical networks."""
        response = await self.client.call_async("listPhysicalNetworks", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listphysicalnetworksresponse' in response:
            response = response['listphysicalnetworksresponse']
        if 'physicalnetwork' in response and response['physicalnetwork']:
            data = response['physicalnetwork']
            count = response.get('count', 0)
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    def list_storage_network_ip_range(self, payload: ListStorageNetworkIpRangeRequest) -> APIResponse[List[Dict]]:
        """List storage network IP ranges."""
        response = self.client.call("listStorageNetworkIpRange", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'liststoragenetworkiprangeresponse' in response:
            response = response['liststoragenetworkiprangeresponse']
        if 'storagenetworkiprange' in response and response['storagenetworkiprange']:
            data = response['storagenetworkiprange']
            count = response.get('count', 0)
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    async def list_storage_network_ip_range_async(self, payload: ListStorageNetworkIpRangeRequest) -> APIResponse[List[Dict]]:
        """Asynchronously list storage network IP ranges."""
        response = await self.client.call_async("listStorageNetworkIpRange", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'liststoragenetworkiprangeresponse' in response:
            response = response['liststoragenetworkiprangeresponse']
        if 'storagenetworkiprange' in response and response['storagenetworkiprange']:
            data = response['storagenetworkiprange']
            count = response.get('count', 0)
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    def list_supported_network_services(self, payload: ListSupportedNetworkServicesRequest) -> APIResponse[List[Dict]]:
        """List supported network services."""
        response = self.client.call("listSupportedNetworkServices", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listsupportednetworkservicesresponse' in response:
            response = response['listsupportednetworkservicesresponse']
        if 'networkservice' in response and response['networkservice']:
            data = response['networkservice']
            count = response.get('count', 0)
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    async def list_supported_network_services_async(self, payload: ListSupportedNetworkServicesRequest) -> APIResponse[List[Dict]]:
        """Asynchronously list supported network services."""
        response = await self.client.call_async("listSupportedNetworkServices", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listsupportednetworkservicesresponse' in response:
            response = response['listsupportednetworkservicesresponse']
        if 'networkservice' in response and response['networkservice']:
            data = response['networkservice']
            count = response.get('count', 0)
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    def list_traffic_monitors(self, payload: ListTrafficMonitorsRequest) -> APIResponse[List[Dict]]:
        """List traffic monitors."""
        response = self.client.call("listTrafficMonitors", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listtrafficmonitorsresponse' in response:
            response = response['listtrafficmonitorsresponse']
        if 'trafficmonitor' in response and response['trafficmonitor']:
            data = response['trafficmonitor']
            count = response.get('count', 0)
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    async def list_traffic_monitors_async(self, payload: ListTrafficMonitorsRequest) -> APIResponse[List[Dict]]:
        """Asynchronously list traffic monitors."""
        response = await self.client.call_async("listTrafficMonitors", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listtrafficmonitorsresponse' in response:
            response = response['listtrafficmonitorsresponse']
        if 'trafficmonitor' in response and response['trafficmonitor']:
            data = response['trafficmonitor']
            count = response.get('count', 0)
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    def list_traffic_type_implementors(self, payload: ListTrafficTypeImplementorsRequest) -> APIResponse[List[Dict]]:
        """List traffic type implementors."""
        response = self.client.call("listTrafficTypeImplementors", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listtraffictypeimplementorsresponse' in response:
            response = response['listtraffictypeimplementorsresponse']
        if 'traffictype' in response and response['traffictype']:
            data = response['traffictype']
            count = response.get('count', 0)
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    async def list_traffic_type_implementors_async(self, payload: ListTrafficTypeImplementorsRequest) -> APIResponse[List[Dict]]:
        """Asynchronously list traffic type implementors."""
        response = await self.client.call_async("listTrafficTypeImplementors", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listtraffictypeimplementorsresponse' in response:
            response = response['listtraffictypeimplementorsresponse']
        if 'traffictype' in response and response['traffictype']:
            data = response['traffictype']
            count = response.get('count', 0)
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    def list_traffic_types(self, payload: ListTrafficTypesRequest) -> APIResponse[List[Dict]]:
        """List traffic types."""
        response = self.client.call("listTrafficTypes", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listtraffictypesresponse' in response:
            response = response['listtraffictypesresponse']
        if 'traffictype' in response and response['traffictype']:
            data = response['traffictype']
            count = response.get('count', 0)
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    async def list_traffic_types_async(self, payload: ListTrafficTypesRequest) -> APIResponse[List[Dict]]:
        """Asynchronously list traffic types."""
        response = await self.client.call_async("listTrafficTypes", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listtraffictypesresponse' in response:
            response = response['listtraffictypesresponse']
        if 'traffictype' in response and response['traffictype']:
            data = response['traffictype']
            count = response.get('count', 0)
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    # Release operation

    def release_public_ip_range(self, payload: ReleasePublicIpRangeRequest) -> APIResponse[Dict]:
        """Release a public IP range."""
        response = self.client.call("releasePublicIpRange", payload.model_dump(exclude_none=True))
        data = {}
        if 'releasepubliciprangeresponse' in response:
            data = response['releasepubliciprangeresponse']
        return APIResponse[Dict](**{"data": data})

    async def release_public_ip_range_async(self, payload: ReleasePublicIpRangeRequest) -> APIResponse[Dict]:
        """Asynchronously release a public IP range."""
        response = await self.client.call_async("releasePublicIpRange", payload.model_dump(exclude_none=True))
        data = {}
        if 'releasepubliciprangeresponse' in response:
            data = response['releasepubliciprangeresponse']
        return APIResponse[Dict](**{"data": data})

    # Remove/Reset operations

    def remove_network_permissions(self, payload: RemoveNetworkPermissionsRequest) -> APIResponse[Dict]:
        """Remove network permissions."""
        response = self.client.call("removeNetworkPermissions", payload.model_dump(exclude_none=True))
        data = {}
        if 'removenetworkpermissionsresponse' in response:
            data = response['removenetworkpermissionsresponse']
        return APIResponse[Dict](**{"data": data})

    async def remove_network_permissions_async(self, payload: RemoveNetworkPermissionsRequest) -> APIResponse[Dict]:
        """Asynchronously remove network permissions."""
        response = await self.client.call_async("removeNetworkPermissions", payload.model_dump(exclude_none=True))
        data = {}
        if 'removenetworkpermissionsresponse' in response:
            data = response['removenetworkpermissionsresponse']
        return APIResponse[Dict](**{"data": data})

    def reset_network_permissions(self, payload: ResetNetworkPermissionsRequest) -> APIResponse[Dict]:
        """Reset network permissions."""
        response = self.client.call("resetNetworkPermissions", payload.model_dump(exclude_none=True))
        data = {}
        if 'resetnetworkpermissionsresponse' in response:
            data = response['resetnetworkpermissionsresponse']
        return APIResponse[Dict](**{"data": data})

    async def reset_network_permissions_async(self, payload: ResetNetworkPermissionsRequest) -> APIResponse[Dict]:
        """Asynchronously reset network permissions."""
        response = await self.client.call_async("resetNetworkPermissions", payload.model_dump(exclude_none=True))
        data = {}
        if 'resetnetworkpermissionsresponse' in response:
            data = response['resetnetworkpermissionsresponse']
        return APIResponse[Dict](**{"data": data})

    # Update operations

    def update_network_service_provider(self, payload: UpdateNetworkServiceProviderRequest) -> APIResponse[Dict]:
        """Update a network service provider."""
        response = self.client.call("updateNetworkServiceProvider", payload.model_dump(exclude_none=True))
        data = {}
        if 'updatenetworkserviceproviderresponse' in response:
            data = response['updatenetworkserviceproviderresponse']
        return APIResponse[Dict](**{"data": data})

    async def update_network_service_provider_async(self, payload: UpdateNetworkServiceProviderRequest) -> APIResponse[Dict]:
        """Asynchronously update a network service provider."""
        response = await self.client.call_async("updateNetworkServiceProvider", payload.model_dump(exclude_none=True))
        data = {}
        if 'updatenetworkserviceproviderresponse' in response:
            data = response['updatenetworkserviceproviderresponse']
        return APIResponse[Dict](**{"data": data})

    def update_physical_network(self, payload: UpdatePhysicalNetworkRequest) -> APIResponse[Dict]:
        """Update a physical network."""
        response = self.client.call("updatePhysicalNetwork", payload.model_dump(exclude_none=True))
        data = {}
        if 'updatephysicalnetworkresponse' in response:
            data = response['updatephysicalnetworkresponse']
        return APIResponse[Dict](**{"data": data})

    async def update_physical_network_async(self, payload: UpdatePhysicalNetworkRequest) -> APIResponse[Dict]:
        """Asynchronously update a physical network."""
        response = await self.client.call_async("updatePhysicalNetwork", payload.model_dump(exclude_none=True))
        data = {}
        if 'updatephysicalnetworkresponse' in response:
            data = response['updatephysicalnetworkresponse']
        return APIResponse[Dict](**{"data": data})

    def update_storage_network_ip_range(self, payload: UpdateStorageNetworkIpRangeRequest) -> APIResponse[Dict]:
        """Update a storage network IP range."""
        response = self.client.call("updateStorageNetworkIpRange", payload.model_dump(exclude_none=True))
        data = {}
        if 'updatestoragenetworkiprangeresponse' in response:
            data = response['updatestoragenetworkiprangeresponse']
        return APIResponse[Dict](**{"data": data})

    async def update_storage_network_ip_range_async(self, payload: UpdateStorageNetworkIpRangeRequest) -> APIResponse[Dict]:
        """Asynchronously update a storage network IP range."""
        response = await self.client.call_async("updateStorageNetworkIpRange", payload.model_dump(exclude_none=True))
        data = {}
        if 'updatestoragenetworkiprangeresponse' in response:
            data = response['updatestoragenetworkiprangeresponse']
        return APIResponse[Dict](**{"data": data})

    def update_traffic_type(self, payload: UpdateTrafficTypeRequest) -> APIResponse[Dict]:
        """Update a traffic type."""
        response = self.client.call("updateTrafficType", payload.model_dump(exclude_none=True))
        data = {}
        if 'updatetraffictyperesponse' in response:
            data = response['updatetraffictyperesponse']
        return APIResponse[Dict](**{"data": data})

    async def update_traffic_type_async(self, payload: UpdateTrafficTypeRequest) -> APIResponse[Dict]:
        """Asynchronously update a traffic type."""
        response = await self.client.call_async("updateTrafficType", payload.model_dump(exclude_none=True))
        data = {}
        if 'updatetraffictyperesponse' in response:
            data = response['updatetraffictyperesponse']
        return APIResponse[Dict](**{"data": data})
