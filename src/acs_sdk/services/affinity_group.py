# services/affinity_group.py
from typing import Dict, List

from acs_sdk.schemas.request.affinity_group import (
    CreateAffinityGroupRequest,
    DeleteAffinityGroupRequest,
    ListAffinityGroupsRequest,
    ListAffinityGroupTypesRequest,
    UpdateVMAffinityGroupRequest,
)

from .base import BaseService
from ..schemas.response.base import APIResponse


class AffinityGroup(BaseService):
    def create(self, payload: CreateAffinityGroupRequest) -> APIResponse[Dict]:
        """Create an affinity/anti-affinity group."""
        return self._execute(
            "createAffinityGroup",
            payload,
            envelope="createaffinitygroupresponse",
        )

    async def create_async(self, payload: CreateAffinityGroupRequest) -> APIResponse[Dict]:
        """Asynchronously create an affinity/anti-affinity group."""
        return await self._execute_async(
            "createAffinityGroup",
            payload,
            envelope="createaffinitygroupresponse",
        )

    def delete(self, payload: DeleteAffinityGroupRequest) -> APIResponse[Dict]:
        """Delete an affinity group."""
        return self._execute(
            "deleteAffinityGroup",
            payload,
            envelope="deleteaffinitygroupresponse",
        )

    async def delete_async(self, payload: DeleteAffinityGroupRequest) -> APIResponse[Dict]:
        """Asynchronously delete an affinity group."""
        return await self._execute_async(
            "deleteAffinityGroup",
            payload,
            envelope="deleteaffinitygroupresponse",
        )

    def list_types(self, payload: ListAffinityGroupTypesRequest) -> APIResponse[List[Dict]]:
        """List all available affinity/anti-affinity group types."""
        return self._execute(
            "listAffinityGroupTypes",
            payload,
            envelope="listaffinitygrouptypesresponse",
            entity="affinitygrouptype",
        )

    async def list_types_async(
        self, payload: ListAffinityGroupTypesRequest
    ) -> APIResponse[List[Dict]]:
        """Asynchronously list all available affinity/anti-affinity group types."""
        return await self._execute_async(
            "listAffinityGroupTypes",
            payload,
            envelope="listaffinitygrouptypesresponse",
            entity="affinitygrouptype",
        )

    def list(self, payload: ListAffinityGroupsRequest) -> APIResponse[List[Dict]]:
        """List affinity groups."""
        return self._execute(
            "listAffinityGroups",
            payload,
            envelope="listaffinitygroupsresponse",
            entity="affinitygroup",
        )

    async def list_async(self, payload: ListAffinityGroupsRequest) -> APIResponse[List[Dict]]:
        """Asynchronously list affinity groups."""
        return await self._execute_async(
            "listAffinityGroups",
            payload,
            envelope="listaffinitygroupsresponse",
            entity="affinitygroup",
        )

    def update_vm_affinity_group(
        self, payload: UpdateVMAffinityGroupRequest
    ) -> APIResponse[Dict]:
        """Update the affinity/anti-affinity group associations of a virtual machine."""
        return self._execute(
            "updateVMAffinityGroup",
            payload,
            envelope="updatevmaffinitygroupresponse",
        )

    async def update_vm_affinity_group_async(
        self, payload: UpdateVMAffinityGroupRequest
    ) -> APIResponse[Dict]:
        """Asynchronously update the affinity/anti-affinity group associations of a virtual machine."""
        return await self._execute_async(
            "updateVMAffinityGroup",
            payload,
            envelope="updatevmaffinitygroupresponse",
        )
