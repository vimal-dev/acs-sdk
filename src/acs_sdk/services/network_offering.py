# services/network_offering.py
from typing import Dict, List

from acs_sdk.schemas.request.network_offering import ListNetworkOfferingRequest

from .base import BaseService
from ..schemas.response.base import APIResponse


class NetworkOffering(BaseService):
    def list(self, payload: ListNetworkOfferingRequest) -> APIResponse[List[Dict]]:
        """Lists all available network offerings."""
        return self._execute(
            "listNetworkOfferings",
            payload,
            envelope="listnetworkofferingsresponse",
            entity="networkoffering",
        )

    async def list_async(self, payload: ListNetworkOfferingRequest) -> APIResponse[List[Dict]]:
        """Asynchronously Lists network offerings."""
        return await self._execute_async(
            "listNetworkOfferings",
            payload,
            envelope="listnetworkofferingsresponse",
            entity="networkoffering",
        )
