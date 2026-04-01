# services/regions.py
from typing import Dict

from .base import BaseService
from ..schemas.response.base import APIResponse


class RegionsService(BaseService):
    
    def list(self) -> APIResponse[Dict]:
        data = self.client.call("listRegions")
        return APIResponse[Dict](**data)

    # async def list_async(self) -> RegionListResponse:
    #     data = await self.client.async_call("listRegions")
    #     return RegionListResponse(**data["listregionsresponse"])