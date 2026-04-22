# services/disk_offering.py
from typing import Dict, List

from acs_sdk.schemas.request.disk_offering import ListDiskOfferingRequest

from .base import BaseService
from ..schemas.response.base import APIResponse


class DiskOffering(BaseService):
    
    
    def list(self, payload: ListDiskOfferingRequest) -> APIResponse[List[Dict]]:
        """Lists all available disk offerings."""
        response = self.client.call("listDiskOfferings", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listdiskofferingsresponse' in response:
            response = response['listdiskofferingsresponse']
        if 'diskoffering' in response and response['diskoffering']:
            data = response['diskoffering']
            count = response['count']
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    async def list_async(self, payload: ListDiskOfferingRequest) -> APIResponse[List[Dict]]:
        """Asynchronously Lists all available disk offerings."""
        response = await self.client.call_async("listDiskOfferings", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listdiskofferingsresponse' in response:
            response = response['listdiskofferingsresponse']
        if 'diskoffering' in response and response['diskoffering']:
            data = response['diskoffering']
            count = response['count']
        return APIResponse[List[Dict]](**{"data": data, "count": count})