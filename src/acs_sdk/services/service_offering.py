# services/service_offering.py
from typing import Dict, List

from acs_sdk.schemas.request.service_offering import (
    CreateServiceOfferingRequest,
    DeleteServiceOfferingRequest,
    ListServiceOfferingRequest,
    UpdateServiceOfferingRequest,
)

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
        """Asynchronously lists service offerings."""
        return await self._execute_async(
            "listServiceOfferings",
            payload,
            envelope="listserviceofferingsresponse",
            entity="serviceoffering",
        )

    def create(self, payload: CreateServiceOfferingRequest) -> APIResponse[Dict]:
        """Creates a new service offering."""
        return self._execute(
            "createServiceOffering",
            payload,
            envelope="createserviceofferingresponse",
        )

    async def create_async(self, payload: CreateServiceOfferingRequest) -> APIResponse[Dict]:
        """Asynchronously creates a new service offering."""
        return await self._execute_async(
            "createServiceOffering",
            payload,
            envelope="createserviceofferingresponse",
        )

    def delete(self, payload: DeleteServiceOfferingRequest) -> APIResponse[Dict]:
        """Deletes a service offering."""
        return self._execute(
            "deleteServiceOffering",
            payload,
            envelope="deleteserviceofferingresponse",
        )

    async def delete_async(self, payload: DeleteServiceOfferingRequest) -> APIResponse[Dict]:
        """Asynchronously deletes a service offering."""
        return await self._execute_async(
            "deleteServiceOffering",
            payload,
            envelope="deleteserviceofferingresponse",
        )

    def update(self, payload: UpdateServiceOfferingRequest) -> APIResponse[Dict]:
        """Updates a service offering."""
        return self._execute(
            "updateServiceOffering",
            payload,
            envelope="updateserviceofferingresponse",
        )

    async def update_async(self, payload: UpdateServiceOfferingRequest) -> APIResponse[Dict]:
        """Asynchronously updates a service offering."""
        return await self._execute_async(
            "updateServiceOffering",
            payload,
            envelope="updateserviceofferingresponse",
        )
