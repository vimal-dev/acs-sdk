# services/usage.py
from typing import Dict, List

from acs_sdk.schemas.request.base import APIRequest

from .base import BaseService
from ..schemas.response.base import APIResponse
from ..schemas.request.usage import (
    GenerateUsageRecordsRequest,
    ListUsageRecordsRequest,
    RemoveRawUsageRecordsRequest,
    RemoveRawUsageRecordsRequest,
)


class Usage(BaseService):
    """Service class for managing usage records in Apache CloudStack."""

    def list(self, payload: ListUsageRecordsRequest) -> APIResponse[List[Dict]]:
        """Lists usage records based on the specified filters."""
        return self._execute(
            "listUsageRecords",
            payload,
            envelope="listusagerecordsresponse",
            entity="usagerecord",
        )

    async def list_async(self, payload: ListUsageRecordsRequest) -> APIResponse[List[Dict]]:
        """Asynchronously lists usage records based on the specified filters."""
        return await self._execute_async(
            "listUsageRecords",
            payload,
            envelope="listusagerecordsresponse",
            entity="usagerecord",
        )

    def list_usage_types(self) -> APIResponse[List[Dict]]:
        """Lists all available usage types."""
        return self._execute(
            "listUsageTypes",
            APIRequest(),  # No payload for this command
            envelope="listusagetypesresponse",
            entity="usagetype",
        )

    async def list_usage_types_async(self) -> APIResponse[List[Dict]]:
        """Asynchronously lists all available usage types."""
        return await self._execute_async(
            "listUsageTypes",
            APIRequest(),  # No payload for this command
            envelope="listusagetypesresponse",
            entity="usagetype",
        )

    def generate_usage_records(self, payload: GenerateUsageRecordsRequest) -> APIResponse[Dict]:
        """Generates usage records for the specified date range."""
        return self._execute(
            "generateUsageRecords", payload, envelope="generateusagerecordsresponse"
        )

    async def generate_usage_records_async(
        self, payload: GenerateUsageRecordsRequest
    ) -> APIResponse[Dict]:
        """Asynchronously generates usage records for the specified date range."""
        return await self._execute_async(
            "generateUsageRecords", payload, envelope="generateusagerecordsresponse"
        )

    def remove_raw_usage_records(self, payload: RemoveRawUsageRecordsRequest) -> APIResponse[Dict]:
        """Removes raw usage records older than the specified interval in days."""
        return self._execute(
            "removeRawUsageRecords", payload, envelope="removerawusagerecordsresponse"
        )

    async def remove_raw_usage_records_async(
        self, payload: RemoveRawUsageRecordsRequest
    ) -> APIResponse[Dict]:
        """Asynchronously removes raw usage records older than the specified interval in days."""
        return await self._execute_async(
            "removeRawUsageRecords", payload, envelope="removerawusagerecordsresponse"
        )
