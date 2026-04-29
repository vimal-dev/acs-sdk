# services/usage.py
from typing import Dict, List

from .base import BaseService
from ..schemas.response.base import APIResponse
from ..schemas.request.zone import ListZonesRequest


class Usage(BaseService):
    def list(self, payload: ListZonesRequest) -> APIResponse[List[Dict]]:
        return self._execute(
            "listUsageRecords",
            payload,
            envelope="listusagerecordsresponse",
            entity="usagerecord",
        )

    async def list_async(self, payload: ListZonesRequest) -> APIResponse[List[Dict]]:
        return await self._execute_async(
            "listUsageRecords",
            payload,
            envelope="listusagerecordsresponse",
            entity="usagerecord",
        )
