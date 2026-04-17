# services/vpc.py
from pprint import pprint
from typing import Dict, List

from acs_sdk.schemas.request.vpc import CreatePrivateGatewayRequest, CreateStaticRouteRequest, ListPrivateGatewayRequest, ListStaticRouteRequest, ListVPCRequest, MigrateVPCRequest, RestartVPCRequest, UpdateVPCRequest

from .base import BaseService
from ..schemas.response.base import APIResponse


class VPC(BaseService):
    
    
    def create_private_gateway(self, payload: CreatePrivateGatewayRequest) -> APIResponse[Dict]:
        """Creates a private gateway."""
        response = self.client.call("createPrivateGateway", payload.model_dump(exclude_none=True))
        data = {}
        if 'createprivategatewayresponse' in response:
            data = response['createprivategatewayresponse']
        return APIResponse[Dict](**{"data": data})

    async def create_private_gateway_async(self, payload: CreatePrivateGatewayRequest) -> APIResponse[Dict]:
        """Asynchronously Creates a private gateway."""
        response = await self.client.call_async("createPrivateGateway", payload.model_dump(exclude_none=True))
        data = {}
        if 'createprivategatewayresponse' in response:
            data = response['createprivategatewayresponse']
        return APIResponse[Dict](**{"data": data})
    
    def create_static_route(self, payload: CreateStaticRouteRequest) -> APIResponse[Dict]:
        """Creates a static route."""
        response = self.client.call("createStaticRoute", payload.model_dump(exclude_none=True))
        data = {}
        if 'createstaticrouteresponse' in response:
            data = response['createstaticrouteresponse']
        return APIResponse[Dict](**{"data": data})

    async def create_static_route_async(self, payload: CreateStaticRouteRequest) -> APIResponse[Dict]:
        """Asynchronously Creates a static route."""
        response = await self.client.call_async("createStaticRoute", payload.model_dump(exclude_none=True))
        data = {}
        if 'createstaticrouteresponse' in response:
            data = response['createstaticrouteresponse']
        return APIResponse[Dict](**{"data": data})
    

    def create_vpc(self, payload: CreateStaticRouteRequest) -> APIResponse[Dict]:
        """Creates a VPC."""
        response = self.client.call("createVPC", payload.model_dump(exclude_none=True))
        data = {}
        if 'createvpcresponse' in response:
            data = response['createvpcresponse']
        return APIResponse[Dict](**{"data": data})

    async def create_vpc_async(self, payload: CreateStaticRouteRequest) -> APIResponse[Dict]:
        """Asynchronously Creates a VPC."""
        response = await self.client.call_async("createVPC", payload.model_dump(exclude_none=True))
        data = {}
        if 'createvpcresponse' in response:
            data = response['createvpcresponse']
        return APIResponse[Dict](**{"data": data})
    
    def delete_private_gateway(self, id: str) -> APIResponse[Dict]:
        """Deletes a Private gateway."""
        response = self.client.call("deletePrivateGateway", {"id": id})
        data = {}
        if 'deleteprivategatewayresponse' in response:
            data = response['deleteprivategatewayresponse']
        return APIResponse[Dict](**{"data": data})

    async def delete_private_gateway_async(self, id: str) -> APIResponse[Dict]:
        """Asynchronously deletes a private gateway."""
        response = await self.client.call_async("deletePrivateGateway", {"id": id})
        data = {}
        if 'deleteprivategatewayresponse' in response:
            data = response['deleteprivategatewayresponse']
        return APIResponse[Dict](**{"data": data})
    
    def delete_static_route(self, id: str) -> APIResponse[Dict]:
        """Deletes a Static route."""
        response = self.client.call("deleteStaticRoute", {"id": id})
        data = {}
        if 'deletestaticrouteresponse' in response:
            data = response['deletestaticrouteresponse']
        return APIResponse[Dict](**{"data": data})

    async def delete_static_route_async(self, id: str) -> APIResponse[Dict]:
        """Asynchronously deletes a static route."""
        response = await self.client.call_async("deleteStaticRoute", {"id": id})
        data = {}
        if 'deletestaticrouteresponse' in response:
            data = response['deletestaticrouteresponse']
        return APIResponse[Dict](**{"data": data})
    
    def delete_vpc(self, id: str) -> APIResponse[Dict]:
        """Deletes a VPC."""
        response = self.client.call("deleteVPC", {"id": id})
        data = {}
        if 'deletevpc' in response:
            data = response['deletevpc']
        return APIResponse[Dict](**{"data": data})

    async def delete_vpc_async(self, id: str) -> APIResponse[Dict]:
        """Asynchronously deletes a VPC."""
        response = await self.client.call_async("deleteVPC", {"id": id})
        data = {}
        if 'deletevpc' in response:
            data = response['deletevpc']
        return APIResponse[Dict](**{"data": data})
    

    def list_private_gateways(self, payload: ListPrivateGatewayRequest) -> APIResponse[List[Dict]]:
        """Lists Private Gateways."""
        response = self.client.call("listPrivateGateways", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listprivategatewaysresponse' in response:
            response = response['listprivategatewaysresponse']
        if 'privategateway' in response and response['privategateway']:
            data = response['privategateway']
            count = response['count']
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    async def list_private_gateways_async(self, payload: ListPrivateGatewayRequest) -> APIResponse[List[Dict]]:
        """Asynchronously Lists Private Gateways."""
        response = await self.client.call_async("listPrivateGateways", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listprivategatewaysresponse' in response:
            response = response['listprivategatewaysresponse']
        if 'privategateway' in response and response['privategateway']:
            data = response['privategateway']
            count = response['count']
        return APIResponse[List[Dict]](**{"data": data, "count": count})
    

    def list_static_routes(self, payload: ListStaticRouteRequest) -> APIResponse[List[Dict]]:
        """Lists Static Routes."""
        response = self.client.call("listStaticRoutes", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'liststaticroutesresponse' in response:
            response = response['liststaticroutesresponse']
        if 'staticroute' in response and response['staticroute']:
            data = response['staticroute']
            count = response['count']
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    async def list_static_routes_async(self, payload: ListStaticRouteRequest) -> APIResponse[List[Dict]]:
        """Asynchronously Lists Static Routes."""
        response = await self.client.call_async("listStaticRoutes", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'liststaticroutesresponse' in response:
            response = response['liststaticroutesresponse']
        if 'staticroute' in response and response['staticroute']:
            data = response['staticroute']
            count = response['count']
        return APIResponse[List[Dict]](**{"data": data, "count": count})
    
    def list_vpc(self, payload: ListVPCRequest) -> APIResponse[List[Dict]]:
        """Lists VPCs."""
        response = self.client.call("listVPCs", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listvpcsresponse' in response:
            response = response['listvpcsresponse']
        if 'vpc' in response and response['vpc']:
            data = response['vpc']
            count = response['count']
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    async def list_vpc_async(self, payload: ListVPCRequest) -> APIResponse[List[Dict]]:
        """Asynchronously Lists VPCs."""
        response = await self.client.call_async("listVPCs", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listvpcsresponse' in response:
            response = response['listvpcsresponse']
        if 'vpc' in response and response['vpc']:
            data = response['vpc']
            count = response['count']
        return APIResponse[List[Dict]](**{"data": data, "count": count})
    
    def migrate_vpc(self, payload: MigrateVPCRequest) -> APIResponse[Dict]:
        """Migrates a VPC."""
        response = self.client.call("migrateVPC", payload.model_dump(exclude_none=True))
        data = {}
        if 'migratevpcresponse' in response:
            data = response['migratevpcresponse']
        return APIResponse[Dict](**{"data": data})

    async def migrate_vpc_async(self, payload: MigrateVPCRequest) -> APIResponse[Dict]:
        """Asynchronously Migrates a VPC."""
        response = await self.client.call_async("migrateVPC", payload.model_dump(exclude_none=True))
        data = {}
        if 'migratevpcresponse' in response:
            data = response['migratevpcresponse']
        return APIResponse[Dict](**{"data": data})
    
    def restart_vpc(self, payload: RestartVPCRequest) -> APIResponse[Dict]:
        """Restarts a VPC."""
        response = self.client.call("restartVPC", payload.model_dump(exclude_none=True))
        data = {}
        if 'restartvpcresponse' in response:
            data = response['restartvpcresponse']
        return APIResponse[Dict](**{"data": data})

    async def restart_vpc_async(self, payload: RestartVPCRequest) -> APIResponse[Dict]:
        """Asynchronously Restarts a VPC."""
        response = await self.client.call_async("restartVPC", payload.model_dump(exclude_none=True))
        data = {}
        if 'restartvpcresponse' in response:
            data = response['restartvpcresponse']
        return APIResponse[Dict](**{"data": data})
    
    def update_vpc(self, payload: UpdateVPCRequest) -> APIResponse[Dict]:
        """Updates a VPC."""
        response = self.client.call("updateVPC", payload.model_dump(exclude_none=True))
        data = {}
        if 'updatevpcresponse' in response:
            data = response['updatevpcresponse']
        return APIResponse[Dict](**{"data": data})

    async def update_vpc_async(self, payload: UpdateVPCRequest) -> APIResponse[Dict]:
        """Asynchronously Updates a VPC."""
        response = await self.client.call_async("updateVPC", payload.model_dump(exclude_none=True))
        data = {}
        if 'updatevpcresponse' in response:
            data = response['updatevpcresponse']
        return APIResponse[Dict](**{"data": data})