# services/zone.py
from pprint import pprint
from typing import Dict

from .base import BaseService
from ..schemas.response.base import APIResponse


class VirtualMachine(BaseService):
    def list(self) -> APIResponse[Dict]:
        data = self.client.call("listVirtualMachines")
        pprint(data)
        return APIResponse[Dict](**data)

    async def list_async(self) -> APIResponse[Dict]:
        data = await self.client.async_call("listVirtualMachines")
        return APIResponse[Dict](**data)
