# services/snapshot.py
from typing import Dict, List

from acs_sdk.schemas.request.snapshot import (
    CreateSnapshotPolicyRequest,
    CreateSnapshotRequest,
    CreateVMSnapshotRequest,
    DeleteSnapshotPoliciesRequest,
    DeleteSnapshotRequest,
    DeleteVMSnapshotRequest,
    ListSnapshotPoliciesRequest,
    ListSnapshotsRequest,
    ListVMSnapshotRequest,
    RevertSnapshotRequest,
    UpdateSnapshotPolicyRequest,
)

from .base import BaseService
from ..schemas.response.base import APIResponse


class Snapshot(BaseService):
    def list(self, payload: ListSnapshotsRequest) -> APIResponse[List[Dict]]:
        """List snapshots."""
        return self._execute(
            "listSnapshots",
            payload,
            envelope="listsnapshotsresponse",
            entity="snapshot",
        )

    async def list_async(self, payload: ListSnapshotsRequest) -> APIResponse[List[Dict]]:
        """Asynchronously list snapshots."""
        return await self._execute_async(
            "listSnapshots",
            payload,
            envelope="listsnapshotsresponse",
            entity="snapshot",
        )

    def create(self, payload: CreateSnapshotRequest) -> APIResponse[Dict]:
        """Create a snapshot."""
        return self._execute(
            "createSnapshot",
            payload,
            envelope="createsnapshotresponse",
        )

    async def create_async(self, payload: CreateSnapshotRequest) -> APIResponse[Dict]:
        """Asynchronously create a snapshot."""
        return await self._execute_async(
            "createSnapshot",
            payload,
            envelope="createsnapshotresponse",
        )

    def delete(self, payload: DeleteSnapshotRequest) -> APIResponse[Dict]:
        """Delete a snapshot."""
        return self._execute(
            "deleteSnapshot",
            payload,
            envelope="deletesnapshotresponse",
        )

    async def delete_async(self, payload: DeleteSnapshotRequest) -> APIResponse[Dict]:
        """Asynchronously delete a snapshot."""
        return await self._execute_async(
            "deleteSnapshot",
            payload,
            envelope="deletesnapshotresponse",
        )

    def create_vm_snapshot(self, payload: CreateVMSnapshotRequest) -> APIResponse[Dict]:
        """Create a VM snapshot."""
        return self._execute(
            "createVMSnapshot",
            payload,
            envelope="createvmsnapshotresponse",
        )

    async def create_vm_snapshot_async(self, payload: CreateVMSnapshotRequest) -> APIResponse[Dict]:
        """Asynchronously create a VM snapshot."""
        return await self._execute_async(
            "createVMSnapshot",
            payload,
            envelope="createvmsnapshotresponse",
        )

    def delete_vm_snapshot(self, payload: DeleteVMSnapshotRequest) -> APIResponse[Dict]:
        """Delete a VM snapshot."""
        return self._execute(
            "deleteVMSnapshot",
            payload,
            envelope="deletevmsnapshotresponse",
        )

    async def delete_vm_snapshot_async(self, payload: DeleteVMSnapshotRequest) -> APIResponse[Dict]:
        """Asynchronously delete a VM snapshot."""
        return await self._execute_async(
            "deleteVMSnapshot",
            payload,
            envelope="deletevmsnapshotresponse",
        )

    def list_vm_snapshot(self, payload: ListVMSnapshotRequest) -> APIResponse[List[Dict]]:
        """List VM snapshots."""
        return self._execute(
            "listVMSnapshot",
            payload,
            envelope="listvmsnapshotresponse",
            entity="vmsnapshot",
        )

    async def list_vm_snapshot_async(
        self, payload: ListVMSnapshotRequest
    ) -> APIResponse[List[Dict]]:
        """Asynchronously list VM snapshots."""
        return await self._execute_async(
            "listVMSnapshot",
            payload,
            envelope="listvmsnapshotresponse",
            entity="vmsnapshot",
        )

    def revert(self, payload: RevertSnapshotRequest) -> APIResponse[Dict]:
        """Revert to a snapshot."""
        return self._execute(
            "revertSnapshot",
            payload,
            envelope="revertsnapshotresponse",
        )

    async def revert_async(self, payload: RevertSnapshotRequest) -> APIResponse[Dict]:
        """Asynchronously revert to a snapshot."""
        return await self._execute_async(
            "revertSnapshot",
            payload,
            envelope="revertsnapshotresponse",
        )

    def create_policy(self, payload: CreateSnapshotPolicyRequest) -> APIResponse[Dict]:
        """Create a snapshot policy."""
        return self._execute(
            "createSnapshotPolicy",
            payload,
            envelope="createsnapshotpolicyresponse",
        )

    async def create_policy_async(self, payload: CreateSnapshotPolicyRequest) -> APIResponse[Dict]:
        """Asynchronously create a snapshot policy."""
        return await self._execute_async(
            "createSnapshotPolicy",
            payload,
            envelope="createsnapshotpolicyresponse",
        )

    def delete_policy(self, payload: DeleteSnapshotPoliciesRequest) -> APIResponse[Dict]:
        """Delete a snapshot policy."""
        return self._execute(
            "deleteSnapshotPolicies",
            payload,
            envelope="deletesnapshotpoliciesresponse",
        )

    async def delete_policy_async(
        self, payload: DeleteSnapshotPoliciesRequest
    ) -> APIResponse[Dict]:
        """Asynchronously delete a snapshot policy."""
        return await self._execute_async(
            "deleteSnapshotPolicies",
            payload,
            envelope="deletesnapshotpoliciesresponse",
        )

    def list_policies(self, payload: ListSnapshotPoliciesRequest) -> APIResponse[List[Dict]]:
        """List snapshot policies."""
        return self._execute(
            "listSnapshotPolicies",
            payload,
            envelope="listsnapshotpoliciesresponse",
            entity="snapshotpolicy",
        )

    async def list_policies_async(
        self, payload: ListSnapshotPoliciesRequest
    ) -> APIResponse[List[Dict]]:
        """Asynchronously list snapshot policies."""
        return await self._execute_async(
            "listSnapshotPolicies",
            payload,
            envelope="listsnapshotpoliciesresponse",
            entity="snapshotpolicy",
        )

    def update_policy(self, payload: UpdateSnapshotPolicyRequest) -> APIResponse[Dict]:
        """Update a snapshot policy."""
        return self._execute(
            "updateSnapshotPolicy",
            payload,
            envelope="updatesnapshotpolicyresponse",
        )

    async def update_policy_async(self, payload: UpdateSnapshotPolicyRequest) -> APIResponse[Dict]:
        """Asynchronously update a snapshot policy."""
        return await self._execute_async(
            "updateSnapshotPolicy",
            payload,
            envelope="updatesnapshotpolicyresponse",
        )
