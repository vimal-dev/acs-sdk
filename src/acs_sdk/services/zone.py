# services/zone.py
from typing import Dict, List

from .base import BaseService
from ..schemas.response.base import APIResponse
from ..schemas.request.zone import ListZonesRequest


class Zone(BaseService):
    def list(self, payload: ListZonesRequest) -> APIResponse[List[Dict]]:
        return self._execute(
            "listZones",
            payload,
            envelope="listzonesresponse",
            entity="zone",
        )

    async def list_async(self, payload: ListZonesRequest) -> APIResponse[List[Dict]]:
        return await self._execute_async(
            "listZones",
            payload,
            envelope="listzonesresponse",
            entity="zone",
        )
