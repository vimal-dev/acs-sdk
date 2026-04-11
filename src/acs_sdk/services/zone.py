# services/zone.py
from typing import Dict, List

from .base import BaseService
from ..schemas.response.base import APIResponse
from ..schemas.request.zone import ListZonesRequest


class Zone(BaseService):
    def list(self, payload: ListZonesRequest) -> APIResponse[List[Dict]]:
        response = self.client.call("listZones", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listzonesresponse' in response:
            response = response['listzonesresponse']
        if 'zone' in response and response['zone']:
            data = response['zone']
            count = response['count']
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    async def list_async(self, payload: ListZonesRequest) -> APIResponse[List[Dict]]:
        response = await self.client.async_call("listRegions", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listzonesresponse' in response:
            response = response['listzonesresponse']
        if 'zone' in response and response['zone']:
            data = response['zone']
            count = response['count']
        return APIResponse[List[Dict]](**{"data": data, "count": count})
