# services/zone.py
from typing import Dict

from .base import BaseService
from ..schemas.response.base import APIResponse


class Zone(BaseService):
    def list(self) -> APIResponse[Dict]:
        data = self.client.call("listZones")
        return APIResponse[Dict](**data)

    async def list_async(self) -> APIResponse[Dict]:
        data = await self.client.async_call("listZones")
        return APIResponse[Dict](**data)
