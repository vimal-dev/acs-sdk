# services/regions.py
from typing import Dict, List

from acs_sdk.schemas.request.region import ListRegionsRequest

from .base import BaseService
from ..schemas.response.base import APIResponse


class Region(BaseService):
    def list(self, payload: ListRegionsRequest) -> APIResponse[List[Dict]]:
        response = self.client.call("listRegions", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listregionsresponse' in response:
            response = response['listregionsresponse']
        if 'region' in response and response['region']:
            data = response['region']
            count = response['count']
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    async def list_async(self, payload: ListRegionsRequest) -> APIResponse[List[Dict]]:
        response = await self.client.async_call("listRegions", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listregionsresponse' in response:
            response = response['listregionsresponse']
        if 'region' in response and response['region']:
            data = response['region']
            count = response['count']
        return APIResponse[List[Dict]](**{"data": data, "count": count})
