# services/console_session.py
from typing import Dict, List

from acs_sdk.schemas.request.console_session import (
    CreateConsoleEndpointRequest,
    ListConsoleSessionsRequest,
)

from .base import BaseService
from ..schemas.response.base import APIResponse


class ConsoleSession(BaseService):
    def create_endpoint(self, payload: CreateConsoleEndpointRequest) -> APIResponse[Dict]:
        """Create a console endpoint for a virtual machine."""
        return self._execute(
            "createConsoleEndpoint",
            payload,
            envelope="createconsoleendpointresponse",
        )

    async def create_endpoint_async(
        self, payload: CreateConsoleEndpointRequest
    ) -> APIResponse[Dict]:
        """Asynchronously create a console endpoint for a virtual machine."""
        return await self._execute_async(
            "createConsoleEndpoint",
            payload,
            envelope="createconsoleendpointresponse",
        )

    def list(self, payload: ListConsoleSessionsRequest) -> APIResponse[List[Dict]]:
        """List console sessions."""
        return self._execute(
            "listConsoleSessions",
            payload,
            envelope="listconsolesessionsresponse",
            entity="consolesession",
        )

    async def list_async(self, payload: ListConsoleSessionsRequest) -> APIResponse[List[Dict]]:
        """Asynchronously list console sessions."""
        return await self._execute_async(
            "listConsoleSessions",
            payload,
            envelope="listconsolesessionsresponse",
            entity="consolesession",
        )
