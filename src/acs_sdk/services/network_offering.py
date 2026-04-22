# services/network_offering.py
from typing import Dict, List

from acs_sdk.schemas.request.network_offering import ListNetworkOfferingRequest

from .base import BaseService
from ..schemas.response.base import APIResponse


class NetworkOffering(BaseService):
    
    
    def list(self, payload: ListNetworkOfferingRequest) -> APIResponse[List[Dict]]:
        """Lists all available network offerings."""
        response = self.client.call("listNetworkOfferings", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listnetworkofferingsresponse' in response:
            response = response['listnetworkofferingsresponse']
        if 'networkoffering' in response and response['networkoffering']:
            data = response['networkoffering']
            count = response['count']
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    async def list_async(self, payload: ListNetworkOfferingRequest) -> APIResponse[List[Dict]]:
        """Asynchronously Lists network offerings."""
        response = await self.client.call_async("listNetworkOfferings", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listnetworkofferingsresponse' in response:
            response = response['listnetworkofferingsresponse']
        if 'networkoffering' in response and response['networkoffering']:
            data = response['networkoffering']
            count = response['count']
        return APIResponse[List[Dict]](**{"data": data, "count": count})