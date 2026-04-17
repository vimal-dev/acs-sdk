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
        response = self.client.call("listSnapshots", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listsnapshotsresponse' in response:
            response = response['listsnapshotsresponse']
        if 'snapshot' in response and response['snapshot']:
            data = response['snapshot']
            count = response['count']
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    async def list_async(self, payload: ListSnapshotsRequest) -> APIResponse[List[Dict]]:
        """Asynchronously list snapshots."""
        response = await self.client.call_async("listSnapshots", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listsnapshotsresponse' in response:
            response = response['listsnapshotsresponse']
        if 'snapshot' in response and response['snapshot']:
            data = response['snapshot']
            count = response['count']
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    def create(self, payload: CreateSnapshotRequest) -> APIResponse[Dict]:
        """Create a snapshot."""
        response = self.client.call("createSnapshot", payload.model_dump(exclude_none=True))
        data = {}
        if 'createsnapshotresponse' in response:
            data = response['createsnapshotresponse']
        return APIResponse[Dict](**{"data": data})

    async def create_async(self, payload: CreateSnapshotRequest) -> APIResponse[Dict]:
        """Asynchronously create a snapshot."""
        response = await self.client.call_async("createSnapshot", payload.model_dump(exclude_none=True))
        data = {}
        if 'createsnapshotresponse' in response:
            data = response['createsnapshotresponse']
        return APIResponse[Dict](**{"data": data})

    def delete(self, payload: DeleteSnapshotRequest) -> APIResponse[Dict]:
        """Delete a snapshot."""
        response = self.client.call("deleteSnapshot", payload.model_dump(exclude_none=True))
        data = {}
        if 'deletesnapshotresponse' in response:
            data = response['deletesnapshotresponse']
        return APIResponse[Dict](**{"data": data})

    async def delete_async(self, payload: DeleteSnapshotRequest) -> APIResponse[Dict]:
        """Asynchronously delete a snapshot."""
        response = await self.client.call_async("deleteSnapshot", payload.model_dump(exclude_none=True))
        data = {}
        if 'deletesnapshotresponse' in response:
            data = response['deletesnapshotresponse']
        return APIResponse[Dict](**{"data": data})

    def create_vm_snapshot(self, payload: CreateVMSnapshotRequest) -> APIResponse[Dict]:
        """Create a VM snapshot."""
        response = self.client.call("createVMSnapshot", payload.model_dump(exclude_none=True))
        data = {}
        if 'createvmsnapshotresponse' in response:
            data = response['createvmsnapshotresponse']
        return APIResponse[Dict](**{"data": data})

    async def create_vm_snapshot_async(self, payload: CreateVMSnapshotRequest) -> APIResponse[Dict]:
        """Asynchronously create a VM snapshot."""
        response = await self.client.call_async("createVMSnapshot", payload.model_dump(exclude_none=True))
        data = {}
        if 'createvmsnapshotresponse' in response:
            data = response['createvmsnapshotresponse']
        return APIResponse[Dict](**{"data": data})

    def delete_vm_snapshot(self, payload: DeleteVMSnapshotRequest) -> APIResponse[Dict]:
        """Delete a VM snapshot."""
        response = self.client.call("deleteVMSnapshot", payload.model_dump(exclude_none=True))
        data = {}
        if 'deletevmsnapshotresponse' in response:
            data = response['deletevmsnapshotresponse']
        return APIResponse[Dict](**{"data": data})

    async def delete_vm_snapshot_async(self, payload: DeleteVMSnapshotRequest) -> APIResponse[Dict]:
        """Asynchronously delete a VM snapshot."""
        response = await self.client.call_async("deleteVMSnapshot", payload.model_dump(exclude_none=True))
        data = {}
        if 'deletevmsnapshotresponse' in response:
            data = response['deletevmsnapshotresponse']
        return APIResponse[Dict](**{"data": data})

    def list_vm_snapshot(self, payload: ListVMSnapshotRequest) -> APIResponse[List[Dict]]:
        """List VM snapshots."""
        response = self.client.call("listVMSnapshot", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listvmsnapshotresponse' in response:
            response = response['listvmsnapshotresponse']
        if 'vmsnapshot' in response and response['vmsnapshot']:
            data = response['vmsnapshot']
            count = response['count']
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    async def list_vm_snapshot_async(self, payload: ListVMSnapshotRequest) -> APIResponse[List[Dict]]:
        """Asynchronously list VM snapshots."""
        response = await self.client.call_async("listVMSnapshot", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listvmsnapshotresponse' in response:
            response = response['listvmsnapshotresponse']
        if 'vmsnapshot' in response and response['vmsnapshot']:
            data = response['vmsnapshot']
            count = response['count']
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    def revert(self, payload: RevertSnapshotRequest) -> APIResponse[Dict]:
        """Revert to a snapshot."""
        response = self.client.call("revertSnapshot", payload.model_dump(exclude_none=True))
        data = {}
        if 'revertsnapshotresponse' in response:
            data = response['revertsnapshotresponse']
        return APIResponse[Dict](**{"data": data})

    async def revert_async(self, payload: RevertSnapshotRequest) -> APIResponse[Dict]:
        """Asynchronously revert to a snapshot."""
        response = await self.client.call_async("revertSnapshot", payload.model_dump(exclude_none=True))
        data = {}
        if 'revertsnapshotresponse' in response:
            data = response['revertsnapshotresponse']
        return APIResponse[Dict](**{"data": data})

    def create_policy(self, payload: CreateSnapshotPolicyRequest) -> APIResponse[Dict]:
        """Create a snapshot policy."""
        response = self.client.call("createSnapshotPolicy", payload.model_dump(exclude_none=True))
        data = {}
        if 'createsnapshotpolicyresponse' in response:
            data = response['createsnapshotpolicyresponse']
        return APIResponse[Dict](**{"data": data})

    async def create_policy_async(self, payload: CreateSnapshotPolicyRequest) -> APIResponse[Dict]:
        """Asynchronously create a snapshot policy."""
        response = await self.client.call_async("createSnapshotPolicy", payload.model_dump(exclude_none=True))
        data = {}
        if 'createsnapshotpolicyresponse' in response:
            data = response['createsnapshotpolicyresponse']
        return APIResponse[Dict](**{"data": data})

    def delete_policy(self, payload: DeleteSnapshotPoliciesRequest) -> APIResponse[Dict]:
        """Delete a snapshot policy."""
        response = self.client.call("deleteSnapshotPolicies", payload.model_dump(exclude_none=True))
        data = {}
        if 'deletesnapshotpoliciesresponse' in response:
            data = response['deletesnapshotpoliciesresponse']
        return APIResponse[Dict](**{"data": data})

    async def delete_policy_async(self, payload: DeleteSnapshotPoliciesRequest) -> APIResponse[Dict]:
        """Asynchronously delete a snapshot policy."""
        response = await self.client.call_async("deleteSnapshotPolicies", payload.model_dump(exclude_none=True))
        data = {}
        if 'deletesnapshotpoliciesresponse' in response:
            data = response['deletesnapshotpoliciesresponse']
        return APIResponse[Dict](**{"data": data})

    def list_policies(self, payload: ListSnapshotPoliciesRequest) -> APIResponse[List[Dict]]:
        """List snapshot policies."""
        response = self.client.call("listSnapshotPolicies", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listsnapshotpoliciesresponse' in response:
            response = response['listsnapshotpoliciesresponse']
        if 'snapshotpolicy' in response and response['snapshotpolicy']:
            data = response['snapshotpolicy']
            count = response['count']
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    async def list_policies_async(self, payload: ListSnapshotPoliciesRequest) -> APIResponse[List[Dict]]:
        """Asynchronously list snapshot policies."""
        response = await self.client.call_async("listSnapshotPolicies", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listsnapshotpoliciesresponse' in response:
            response = response['listsnapshotpoliciesresponse']
        if 'snapshotpolicy' in response and response['snapshotpolicy']:
            data = response['snapshotpolicy']
            count = response['count']
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    def update_policy(self, payload: UpdateSnapshotPolicyRequest) -> APIResponse[Dict]:
        """Update a snapshot policy."""
        response = self.client.call("updateSnapshotPolicy", payload.model_dump(exclude_none=True))
        data = {}
        if 'updatesnapshotpolicyresponse' in response:
            data = response['updatesnapshotpolicyresponse']
        return APIResponse[Dict](**{"data": data})

    async def update_policy_async(self, payload: UpdateSnapshotPolicyRequest) -> APIResponse[Dict]:
        """Asynchronously update a snapshot policy."""
        response = await self.client.call_async("updateSnapshotPolicy", payload.model_dump(exclude_none=True))
        data = {}
        if 'updatesnapshotpolicyresponse' in response:
            data = response['updatesnapshotpolicyresponse']
        return APIResponse[Dict](**{"data": data})
