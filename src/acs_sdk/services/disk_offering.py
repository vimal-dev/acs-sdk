# services/disk_offering.py
from typing import Dict, List

from acs_sdk.schemas.request.disk_offering import ListDiskOfferingRequest

from .base import BaseService
from ..schemas.response.base import APIResponse


class DiskOffering(BaseService):
    def list(self, payload: ListDiskOfferingRequest) -> APIResponse[List[Dict]]:
        """Lists all available disk offerings."""
        return self._execute(
            "listDiskOfferings",
            payload,
            envelope="listdiskofferingsresponse",
            entity="diskoffering",
        )

    async def list_async(self, payload: ListDiskOfferingRequest) -> APIResponse[List[Dict]]:
        """Asynchronously Lists all available disk offerings."""
        return await self._execute_async(
            "listDiskOfferings",
            payload,
            envelope="listdiskofferingsresponse",
            entity="diskoffering",
        )
