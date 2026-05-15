# services/template.py
from typing import Dict, List

from ..schemas.request.template import ListTemplatesRequest

from .base import BaseService
from ..schemas.response.base import APIResponse


class Template(BaseService):
    """Service class for managing templates in Apache CloudStack."""

    def list(self, payload: ListTemplatesRequest) -> APIResponse[List[Dict]]:
        """List all public, private, and privileged templates based on the specified filters."""
        return self._execute(
            "listTemplates",
            payload,
            envelope="listtemplatesresponse",
            entity="template",
        )

    async def list_async(self, payload: ListTemplatesRequest) -> APIResponse[List[Dict]]:
        """List all public, private, and privileged templates based on the specified filters."""
        return await self._execute_async(
            "listTemplates",
            payload,
            envelope="listtemplatesresponse",
            entity="template",
        )
