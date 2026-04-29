# services/vpc_offering.py
from typing import Dict, List

from acs_sdk.schemas.request.vpc_offering import ListVPCOfferingRequest

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
        """Asynchronously Lists VPC offerings."""
        return await self._execute_async(
            "listVPCOfferings",
            payload,
            envelope="listvpcofferingsresponse",
            entity="vpcoffering",
        )
