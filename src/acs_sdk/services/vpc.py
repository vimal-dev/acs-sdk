# services/vpc.py
from typing import Dict, List

from acs_sdk.schemas.request.vpc import (
    CreatePrivateGatewayRequest,
    CreateStaticRouteRequest,
    CreateVPCRequest,
    DeletePrivateGatewayRequest,
    DeleteStaticRouteRequest,
    DeleteVPCRequest,
    ListPrivateGatewayRequest,
    ListStaticRouteRequest,
    ListVPCRequest,
    MigrateVPCRequest,
    RestartVPCRequest,
    UpdateVPCRequest,
)

from .base import BaseService
from ..schemas.response.base import APIResponse


class VPC(BaseService):
    def create_private_gateway(self, payload: CreatePrivateGatewayRequest) -> APIResponse[Dict]:
        """Creates a private gateway."""
        return self._execute(
            "createPrivateGateway",
            payload,
            envelope="createprivategatewayresponse",
        )

    async def create_private_gateway_async(
        self, payload: CreatePrivateGatewayRequest
    ) -> APIResponse[Dict]:
        """Asynchronously Creates a private gateway."""
        return await self._execute_async(
            "createPrivateGateway",
            payload,
            envelope="createprivategatewayresponse",
        )

    def create_static_route(self, payload: CreateStaticRouteRequest) -> APIResponse[Dict]:
        """Creates a static route."""
        return self._execute(
            "createStaticRoute",
            payload,
            envelope="createstaticrouteresponse",
        )

    async def create_static_route_async(
        self, payload: CreateStaticRouteRequest
    ) -> APIResponse[Dict]:
        """Asynchronously Creates a static route."""
        return await self._execute_async(
            "createStaticRoute",
            payload,
            envelope="createstaticrouteresponse",
        )

    def create_vpc(self, payload: CreateVPCRequest) -> APIResponse[Dict]:
        """Creates a VPC."""
        return self._execute(
            "createVPC",
            payload,
            envelope="createvpcresponse",
        )

    async def create_vpc_async(self, payload: CreateVPCRequest) -> APIResponse[Dict]:
        """Asynchronously Creates a VPC."""
        return await self._execute_async(
            "createVPC",
            payload,
            envelope="createvpcresponse",
        )

    def delete_private_gateway(self, payload: DeletePrivateGatewayRequest) -> APIResponse[Dict]:
        """Deletes a Private gateway."""
        return self._execute(
            "deletePrivateGateway",
            payload,
            envelope="deleteprivategatewayresponse",
        )

    async def delete_private_gateway_async(
        self, payload: DeletePrivateGatewayRequest
    ) -> APIResponse[Dict]:
        """Asynchronously deletes a private gateway."""
        return await self._execute_async(
            "deletePrivateGateway",
            payload,
            envelope="deleteprivategatewayresponse",
        )

    def delete_static_route(self, payload: DeleteStaticRouteRequest) -> APIResponse[Dict]:
        """Deletes a Static route."""
        return self._execute(
            "deleteStaticRoute",
            payload,
            envelope="deletestaticrouteresponse",
        )

    async def delete_static_route_async(
        self, payload: DeleteStaticRouteRequest
    ) -> APIResponse[Dict]:
        """Asynchronously deletes a static route."""
        return await self._execute_async(
            "deleteStaticRoute",
            payload,
            envelope="deletestaticrouteresponse",
        )

    def delete_vpc(self, payload: DeleteVPCRequest) -> APIResponse[Dict]:
        """Deletes a VPC."""
        return self._execute(
            "deleteVPC",
            payload,
            envelope="deletevpcresponse",
        )

    async def delete_vpc_async(self, payload: DeleteVPCRequest) -> APIResponse[Dict]:
        """Asynchronously deletes a VPC."""
        return await self._execute_async(
            "deleteVPC",
            payload,
            envelope="deletevpcresponse",
        )

    def list_private_gateways(self, payload: ListPrivateGatewayRequest) -> APIResponse[List[Dict]]:
        """Lists Private Gateways."""
        return self._execute(
            "listPrivateGateways",
            payload,
            envelope="listprivategatewaysresponse",
            entity="privategateway",
        )

    async def list_private_gateways_async(
        self, payload: ListPrivateGatewayRequest
    ) -> APIResponse[List[Dict]]:
        """Asynchronously Lists Private Gateways."""
        return await self._execute_async(
            "listPrivateGateways",
            payload,
            envelope="listprivategatewaysresponse",
            entity="privategateway",
        )

    def list_static_routes(self, payload: ListStaticRouteRequest) -> APIResponse[List[Dict]]:
        """Lists Static Routes."""
        return self._execute(
            "listStaticRoutes",
            payload,
            envelope="liststaticroutesresponse",
            entity="staticroute",
        )

    async def list_static_routes_async(
        self, payload: ListStaticRouteRequest
    ) -> APIResponse[List[Dict]]:
        """Asynchronously Lists Static Routes."""
        return await self._execute_async(
            "listStaticRoutes",
            payload,
            envelope="liststaticroutesresponse",
            entity="staticroute",
        )

    def list_vpc(self, payload: ListVPCRequest) -> APIResponse[List[Dict]]:
        """Lists VPCs."""
        return self._execute(
            "listVPCs",
            payload,
            envelope="listvpcsresponse",
            entity="vpc",
        )

    async def list_vpc_async(self, payload: ListVPCRequest) -> APIResponse[List[Dict]]:
        """Asynchronously Lists VPCs."""
        return await self._execute_async(
            "listVPCs",
            payload,
            envelope="listvpcsresponse",
            entity="vpc",
        )

    def migrate_vpc(self, payload: MigrateVPCRequest) -> APIResponse[Dict]:
        """Migrates a VPC."""
        return self._execute(
            "migrateVPC",
            payload,
            envelope="migratevpcresponse",
        )

    async def migrate_vpc_async(self, payload: MigrateVPCRequest) -> APIResponse[Dict]:
        """Asynchronously Migrates a VPC."""
        return await self._execute_async(
            "migrateVPC",
            payload,
            envelope="migratevpcresponse",
        )

    def restart_vpc(self, payload: RestartVPCRequest) -> APIResponse[Dict]:
        """Restarts a VPC."""
        return self._execute(
            "restartVPC",
            payload,
            envelope="restartvpcresponse",
        )

    async def restart_vpc_async(self, payload: RestartVPCRequest) -> APIResponse[Dict]:
        """Asynchronously Restarts a VPC."""
        return await self._execute_async(
            "restartVPC",
            payload,
            envelope="restartvpcresponse",
        )

    def update_vpc(self, payload: UpdateVPCRequest) -> APIResponse[Dict]:
        """Updates a VPC."""
        return self._execute(
            "updateVPC",
            payload,
            envelope="updatevpcresponse",
        )

    async def update_vpc_async(self, payload: UpdateVPCRequest) -> APIResponse[Dict]:
        """Asynchronously Updates a VPC."""
        return await self._execute_async(
            "updateVPC",
            payload,
            envelope="updatevpcresponse",
        )
