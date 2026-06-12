# services/vpc_offering.py
from typing import Dict, List

from acs_sdk.schemas.request.vpc_offering import (
    CreateVPCOfferingRequest,
    DeleteVPCOfferingRequest,
    ListVPCOfferingRequest,
    UpdateVPCOfferingRequest,
)

from .base import BaseService
from ..schemas.response.base import APIResponse


class VPCOffering(BaseService):
    def list(self, payload: ListVPCOfferingRequest) -> APIResponse[List[Dict]]:
        """Lists VPC offerings."""
        return self._execute(
            "listVPCOfferings",
            payload,
            envelope="listvpcofferingsresponse",
            entity="vpcoffering",
        )

    async def list_async(self, payload: ListVPCOfferingRequest) -> APIResponse[List[Dict]]:
        """Asynchronously lists VPC offerings."""
        return await self._execute_async(
            "listVPCOfferings",
            payload,
            envelope="listvpcofferingsresponse",
            entity="vpcoffering",
        )

    def create(self, payload: CreateVPCOfferingRequest) -> APIResponse[Dict]:
        """Creates a new VPC offering."""
        return self._execute(
            "createVPCOffering",
            payload,
            envelope="createvpcofferingresponse",
        )

    async def create_async(self, payload: CreateVPCOfferingRequest) -> APIResponse[Dict]:
        """Asynchronously creates a new VPC offering."""
        return await self._execute_async(
            "createVPCOffering",
            payload,
            envelope="createvpcofferingresponse",
        )

    def delete(self, payload: DeleteVPCOfferingRequest) -> APIResponse[Dict]:
        """Deletes a VPC offering."""
        return self._execute(
            "deleteVPCOffering",
            payload,
            envelope="deletevpcofferingresponse",
        )

    async def delete_async(self, payload: DeleteVPCOfferingRequest) -> APIResponse[Dict]:
        """Asynchronously deletes a VPC offering."""
        return await self._execute_async(
            "deleteVPCOffering",
            payload,
            envelope="deletevpcofferingresponse",
        )

    def update(self, payload: UpdateVPCOfferingRequest) -> APIResponse[Dict]:
        """Updates a VPC offering."""
        return self._execute(
            "updateVPCOffering",
            payload,
            envelope="updatevpcofferingresponse",
        )

    async def update_async(self, payload: UpdateVPCOfferingRequest) -> APIResponse[Dict]:
        """Asynchronously updates a VPC offering."""
        return await self._execute_async(
            "updateVPCOffering",
            payload,
            envelope="updatevpcofferingresponse",
        )
