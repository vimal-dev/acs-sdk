# services/service_offering.py
from typing import Dict, List

from acs_sdk.schemas.request.service_offering import ListServiceOfferingRequest

from .base import BaseService
from ..schemas.response.base import APIResponse


class ServiceOffering(BaseService):
    def list(self, payload: ListServiceOfferingRequest) -> APIResponse[List[Dict]]:
        """Lists all available service offerings."""
        return self._execute(
            "listServiceOfferings",
            payload,
            envelope="listserviceofferingsresponse",
            entity="serviceoffering",
        )

    async def list_async(self, payload: ListServiceOfferingRequest) -> APIResponse[List[Dict]]:
        """Asynchronously Lists service offerings."""
        return await self._execute_async(
            "listServiceOfferings",
            payload,
            envelope="listserviceofferingsresponse",
            entity="serviceoffering",
        )
