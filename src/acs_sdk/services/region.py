# services/regions.py
from typing import Dict, List

from acs_sdk.schemas.request.region import ListRegionsRequest

from .base import BaseService
from ..schemas.response.base import APIResponse


class Region(BaseService):
    def list(self, payload: ListRegionsRequest) -> APIResponse[List[Dict]]:
        return self._execute(
            "listRegions",
            payload,
            envelope="listregionsresponse",
            entity="region",
        )

    async def list_async(self, payload: ListRegionsRequest) -> APIResponse[List[Dict]]:
        return await self._execute_async(
            "listRegions",
            payload,
            envelope="listregionsresponse",
            entity="region",
        )
