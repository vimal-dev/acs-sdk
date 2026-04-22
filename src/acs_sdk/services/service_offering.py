# services/service_offering.py
from typing import Dict, List

from acs_sdk.schemas.request.service_offering import ListServiceOfferingRequest

from .base import BaseService
from ..schemas.response.base import APIResponse


class ServiceOffering(BaseService):
    
    
    def list(self, payload: ListServiceOfferingRequest) -> APIResponse[List[Dict]]:
        """Lists all available service offerings."""
        response = self.client.call("listServiceOfferings", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listserviceofferingsresponse' in response:
            response = response['listserviceofferingsresponse']
        if 'serviceoffering' in response and response['serviceoffering']:
            data = response['serviceoffering']
            count = response['count']
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    async def list_async(self, payload: ListServiceOfferingRequest) -> APIResponse[List[Dict]]:
        """Asynchronously Lists service offerings."""
        response = await self.client.call_async("listServiceOfferings", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listserviceofferingsresponse' in response:
            response = response['listserviceofferingsresponse']
        if 'serviceoffering' in response and response['serviceoffering']:
            data = response['serviceoffering']
            count = response['count']
        return APIResponse[List[Dict]](**{"data": data, "count": count})