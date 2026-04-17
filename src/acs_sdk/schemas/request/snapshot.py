from typing import Optional

from pydantic import Field

from acs_sdk.schemas.request.base import APIRequest


class ListSnapshotsRequest(APIRequest):
    id: Optional[str] = Field(
        None, description="List snapshots by ID"
    )
    volumeid: Optional[str] = Field(
        None, alias="volumeId", description="List snapshots by volume ID"
    )
    account: Optional[str] = Field(
        None, description="List resources by account. Must be used with the domainId parameter."
    )
    domainid: Optional[str] = Field(
        None, alias="domainId", description="List only resources belonging to the domain specified"
    )
    isrecursive: Optional[bool] = Field(
        False, alias="isRecursive", description="Include subdomains recursively"
    )
    keyword: Optional[str] = Field(
        None, description="Search keyword"
    )
    listall: Optional[bool] = Field(
        False,
        alias="listAll",
        description="List all resources caller is authorized to see"
    )
    projectid: Optional[str] = Field(
        None, alias="projectId", description="List objects by project"
    )
    tags: Optional[str] = Field(
        None, description="List resources by tags (key/value pairs)"
    )
    page: Optional[int] = Field(
        1, ge=1, description="Page number"
    )
    pagesize: Optional[int] = Field(
        50, ge=1, le=500, description="Number of results per page"
    )


class CreateSnapshotRequest(APIRequest):
    volumeid: str = Field(
        ..., alias="volumeId", description="Volume ID for the snapshot"
    )
    name: Optional[str] = Field(
        None, description="Optional name for the snapshot"
    )
    description: Optional[str] = Field(
        None, description="Optional description for the snapshot"
    )


class DeleteSnapshotRequest(APIRequest):
    id: str = Field(
        ..., description="Snapshot ID to delete"
    )


class CreateVMSnapshotRequest(APIRequest):
    virtualmachineid: str = Field(
        ..., alias="virtualMachineId", description="Virtual machine ID for the VM snapshot"
    )
    name: Optional[str] = Field(
        None, description="Optional name for the VM snapshot"
    )
    description: Optional[str] = Field(
        None, description="Optional description for the VM snapshot"
    )
    snapshotmemory: Optional[bool] = Field(
        False, alias="snapshotMemory", description="If true, include VM memory state in the snapshot"
    )


class DeleteVMSnapshotRequest(APIRequest):
    id: str = Field(
        ..., description="VM snapshot ID to delete"
    )


class ListVMSnapshotRequest(APIRequest):
    id: Optional[str] = Field(
        None, description="List VM snapshots by ID"
    )
    virtualmachineid: Optional[str] = Field(
        None, alias="virtualMachineId", description="List VM snapshots by virtual machine ID"
    )
    account: Optional[str] = Field(
        None, description="List resources by account. Must be used with the domainId parameter."
    )
    domainid: Optional[str] = Field(
        None, alias="domainId", description="List only resources belonging to the domain specified"
    )
    isrecursive: Optional[bool] = Field(
        False, alias="isRecursive", description="Include subdomains recursively"
    )
    keyword: Optional[str] = Field(
        None, description="Search keyword"
    )
    listall: Optional[bool] = Field(
        False,
        alias="listAll",
        description="List all resources caller is authorized to see"
    )
    projectid: Optional[str] = Field(
        None, alias="projectId", description="List objects by project"
    )
    tags: Optional[str] = Field(
        None, description="List resources by tags (key/value pairs)"
    )
    page: Optional[int] = Field(
        1, ge=1, description="Page number"
    )
    pagesize: Optional[int] = Field(
        50, ge=1, le=500, description="Number of results per page"
    )


class RevertSnapshotRequest(APIRequest):
    id: str = Field(
        ..., description="Snapshot ID to revert to"
    )


class CreateSnapshotPolicyRequest(APIRequest):
    volumeid: str = Field(
        ..., alias="volumeId", description="Volume ID for the snapshot policy"
    )
    schedule: str = Field(
        ..., description="Snapshot policy schedule"
    )
    intervaltype: int = Field(
        ..., alias="intervalType", description="Interval type for the snapshot policy"
    )
    timezone: Optional[str] = Field(
        None, description="Timezone for the snapshot policy"
    )


class DeleteSnapshotPoliciesRequest(APIRequest):
    id: str = Field(
        ..., description="Snapshot policy ID to delete"
    )


class ListSnapshotPoliciesRequest(APIRequest):
    id: Optional[str] = Field(
        None, description="List snapshot policies by ID"
    )
    volumeid: Optional[str] = Field(
        None, alias="volumeId", description="List snapshot policies by volume ID"
    )
    page: Optional[int] = Field(
        1, ge=1, description="Page number"
    )
    pagesize: Optional[int] = Field(
        50, ge=1, le=500, description="Number of results per page"
    )


class UpdateSnapshotPolicyRequest(APIRequest):
    id: str = Field(
        ..., description="Snapshot policy ID to update"
    )
    schedule: Optional[str] = Field(
        None, description="Updated snapshot policy schedule"
    )
    intervaltype: Optional[int] = Field(
        None, alias="intervalType", description="Updated interval type for the snapshot policy"
    )
    timezone: Optional[str] = Field(
        None, description="Updated timezone for the snapshot policy"
    )
