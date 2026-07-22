# services/instance_group.py
from typing import Dict, List

from acs_sdk.schemas.request.instance_group import (
    CreateInstanceGroupRequest,
    DeleteInstanceGroupRequest,
    ListInstanceGroupsRequest,
    UpdateInstanceGroupRequest,
)

from .base import BaseService
from ..schemas.response.base import APIResponse


class InstanceGroup(BaseService):
    def list(self, payload: ListInstanceGroupsRequest) -> APIResponse[List[Dict]]:
        """List all available instance groups."""
        return self._execute(
            "listInstanceGroups",
            payload,
            envelope="listinstancegroupsresponse",
            entity="instancegroup",
        )

    async def list_async(self, payload: ListInstanceGroupsRequest) -> APIResponse[List[Dict]]:
        """Asynchronously list all available instance groups."""
        return await self._execute_async(
            "listInstanceGroups",
            payload,
            envelope="listinstancegroupsresponse",
            entity="instancegroup",
        )

    def create(self, payload: CreateInstanceGroupRequest) -> APIResponse[Dict]:
        """Create an instance group."""
        return self._execute(
            "createInstanceGroup",
            payload,
            envelope="createinstancegroupresponse",
        )

    async def create_async(self, payload: CreateInstanceGroupRequest) -> APIResponse[Dict]:
        """Asynchronously create an instance group."""
        return await self._execute_async(
            "createInstanceGroup",
            payload,
            envelope="createinstancegroupresponse",
        )

    def update(self, payload: UpdateInstanceGroupRequest) -> APIResponse[Dict]:
        """Update an instance group."""
        return self._execute(
            "updateInstanceGroup",
            payload,
            envelope="updateinstancegroupresponse",
        )

    async def update_async(self, payload: UpdateInstanceGroupRequest) -> APIResponse[Dict]:
        """Asynchronously update an instance group."""
        return await self._execute_async(
            "updateInstanceGroup",
            payload,
            envelope="updateinstancegroupresponse",
        )

    def delete(self, payload: DeleteInstanceGroupRequest) -> APIResponse[Dict]:
        """Delete an instance group."""
        return self._execute(
            "deleteInstanceGroup",
            payload,
            envelope="deleteinstancegroupresponse",
        )

    async def delete_async(self, payload: DeleteInstanceGroupRequest) -> APIResponse[Dict]:
        """Asynchronously delete an instance group."""
        return await self._execute_async(
            "deleteInstanceGroup",
            payload,
            envelope="deleteinstancegroupresponse",
        )
