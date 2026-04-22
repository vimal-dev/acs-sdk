# services/vpc_offering.py
from typing import Dict, List

from acs_sdk.schemas.request.vpc_offering import ListVPCOfferingRequest

from .base import BaseService
from ..schemas.response.base import APIResponse


class VPCOffering(BaseService):
    
    
    def list(self, payload: ListVPCOfferingRequest) -> APIResponse[List[Dict]]:
        """Lists VPC offerings."""
        response = self.client.call("listVPCOfferings", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listvpcofferingsresponse' in response:
            response = response['listvpcofferingsresponse']
        if 'vpc' in response and response['vpc']:
            data = response['vpc']
            count = response['count']
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    async def list_async(self, payload: ListVPCOfferingRequest) -> APIResponse[List[Dict]]:
        """Asynchronously Lists VPC offerings."""
        response = await self.client.call_async("listVPCOfferings", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listvpcofferingsresponse' in response:
            response = response['listvpcofferingsresponse']
        if 'vpc' in response and response['vpc']:
            data = response['vpc']
            count = response['count']
        return APIResponse[List[Dict]](**{"data": data, "count": count})