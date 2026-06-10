from enum import StrEnum
from typing import Any, Optional

from pydantic import Field, UUID4, model_validator, field_serializer

from acs_sdk.schemas.request.base import APIRequest, PaginationMixin


# ---------------------------------------------------------------------------
# Enums
# ---------------------------------------------------------------------------


class IntervalType(StrEnum):
    HOURLY = "HOURLY"
    DAILY = "DAILY"
    WEEKLY = "WEEKLY"
    MONTHLY = "MONTHLY"


class SnapshotType(StrEnum):
    MANUAL = "MANUAL"
    RECURRING = "RECURRING"


class LocationType(StrEnum):
    PRIMARY = "primary"
    SECONDARY = "secondary"


class VMSnapshotState(StrEnum):
    CREATING = "Creating"
    READY = "Ready"
    REVERTING = "Reverting"
    EXPUNGING = "Expunging"
    ERROR = "Error"
    ALLOCATED = "Allocated"
    MIGRATING = "Migrating"


# ---------------------------------------------------------------------------
# Snapshot Requests
# ---------------------------------------------------------------------------


class ArchiveSnapshotRequest(APIRequest):
    """Request parameters for ``archiveSnapshot``. Asynchronous.

    Reference: https://cloudstack.apache.org/api/apidocs-4.22/apis/archiveSnapshot.html
    """

    id: UUID4 = Field(..., description="The ID of the snapshot to archive.")


class CopySnapshotRequest(APIRequest):
    """Request parameters for ``copySnapshot``. Asynchronous.

    Either ``destzoneid`` or ``destzoneids`` must be provided (not both).

    Reference: https://cloudstack.apache.org/api/apidocs-4.22/apis/copySnapshot.html
    """

    id: UUID4 = Field(..., description="The ID of the snapshot.")

    destzoneid: Optional[UUID4] = Field(
        default=None,
        description="Destination zone ID. Mutually exclusive with destzoneids.",
    )
    destzoneids: Optional[list[UUID4]] = Field(
        default=None,
        description=(
            "Comma-separated destination zone IDs for multi-zone copying. "
            "Mutually exclusive with destzoneid."
        ),
    )
    sourcezoneid: Optional[UUID4] = Field(
        default=None,
        description=(
            "Zone ID where the snapshot currently resides. "
            "Defaults to the snapshot volume's zone when omitted."
        ),
    )
    storageids: Optional[list[UUID4]] = Field(
        default=None,
        description="Storage pool IDs in other zones. Currently supported for StorPool only.",
    )
    usestoragereplication: Optional[bool] = Field(
        default=None,
        description="If True, copy the snapshot to supported primary storage via storage replication.",
    )

    @model_validator(mode="after")
    def check_destzone(self) -> "CopySnapshotRequest":
        if self.destzoneid is not None and self.destzoneids is not None:
            raise ValueError("'destzoneid' and 'destzoneids' are mutually exclusive.")
        if self.destzoneid is None and self.destzoneids is None:
            raise ValueError("One of 'destzoneid' or 'destzoneids' must be provided.")
        return self

    @field_serializer("destzoneids", "storageids")
    def serialize_csv(self, value: list[Any] | None) -> str | None:
        if value is None:
            return None
        return ",".join(str(v) for v in value)


class CreateSnapshotRequest(APIRequest):
    """Request parameters for ``createSnapshot``. Asynchronous.

    Reference: https://cloudstack.apache.org/api/apidocs-4.22/apis/createSnapshot.html
    """

    # --- required -----------------------------------------------------------

    volumeid: UUID4 = Field(..., description="UUID of the disk volume to snapshot.")

    # --- optional -----------------------------------------------------------

    account: Optional[str] = Field(
        default=None,
        description="Assign the snapshot to this account name. Must be used together with domainid.",
    )
    asyncbackup: Optional[bool] = Field(
        default=None,
        description=(
            "If True, perform the backup asynchronously. The snapshot is created on primary "
            "storage immediately and backed up to secondary storage in the background."
        ),
    )
    domainid: Optional[UUID4] = Field(
        default=None,
        description=(
            "Domain UUID for the snapshot. When combined with account, "
            "scopes the snapshot to that account's domain."
        ),
    )
    locationtype: Optional[LocationType] = Field(
        default=None,
        description=(
            "Storage location for the snapshot. Only applicable for managed storage. "
            "Allowed values: 'primary' (default), 'secondary'."
        ),
    )
    name: Optional[str] = Field(default=None, description="Human-readable name for the snapshot.")
    policyid: Optional[UUID4] = Field(
        default=None,
        description="UUID of the snapshot policy to associate. Defaults to MANUAL_POLICY if omitted.",
    )
    quiescevm: Optional[bool] = Field(
        default=None,
        description="If True, quiesce the VM before snapshotting for filesystem/application consistency.",
    )
    storageids: Optional[list[UUID4]] = Field(
        default=None,
        description="Storage pool UUIDs in other zones where the snapshot should also be available.",
    )
    tags: Optional[dict[str, str]] = Field(
        default=None,
        description="Arbitrary key/value tag pairs to attach to the snapshot.",
    )
    usestoragereplication: Optional[bool] = Field(
        default=None,
        description="If True, copy the snapshot to supported primary storage via storage replication.",
    )
    zoneids: Optional[list[UUID4]] = Field(
        default=None,
        description="Zone UUIDs where the snapshot should also be made available.",
    )

    @model_validator(mode="after")
    def account_requires_domainid(self) -> "CreateSnapshotRequest":
        if self.account is not None and self.domainid is None:
            raise ValueError("'account' must be used together with 'domainid'.")
        return self

    @field_serializer("storageids", "zoneids")
    def serialize_csv(self, value: list[Any] | None) -> str | None:
        if value is None:
            return None
        return ",".join(str(v) for v in value)


class CreateSnapshotFromVMSnapshotRequest(APIRequest):
    """Request parameters for ``createSnapshotFromVMSnapshot``. Asynchronous.

    Reference: https://cloudstack.apache.org/api/apidocs-4.22/apis/createSnapshotFromVMSnapshot.html
    """

    vmsnapshotid: UUID4 = Field(..., description="The ID of the VM snapshot.")
    volumeid: UUID4 = Field(..., description="The ID of the disk volume.")

    name: Optional[str] = Field(default=None, description="Name for the resulting snapshot.")


class CreateSnapshotPolicyRequest(APIRequest):
    """Request parameters for ``createSnapshotPolicy``.

    Reference: https://cloudstack.apache.org/api/apidocs-4.22/apis/createSnapshotPolicy.html
    """

    # --- required -----------------------------------------------------------

    intervaltype: IntervalType = Field(
        ...,
        description="Interval type: HOURLY, DAILY, WEEKLY, or MONTHLY.",
    )
    maxsnaps: int = Field(
        ...,
        ge=1,
        description="Maximum number of snapshots to retain.",
    )
    schedule: str = Field(
        ...,
        description=(
            "Execution schedule. Format varies by interval: "
            "MM for HOURLY, MM:HH for DAILY, MM:HH:DD for WEEKLY/MONTHLY."
        ),
    )
    timezone: str = Field(
        ...,
        description="Timezone for this schedule (see CloudStack Time Zone Format).",
    )
    volumeid: UUID4 = Field(..., description="The ID of the disk volume.")

    # --- optional -----------------------------------------------------------

    fordisplay: Optional[bool] = Field(
        default=None,
        description="Whether to display the policy to the end user.",
    )
    storageids: Optional[list[UUID4]] = Field(
        default=None,
        description="Storage pool IDs in other zones where the snapshot will be made available.",
    )
    tags: Optional[dict[str, str]] = Field(
        default=None,
        description="Map of tags (key/value pairs) to attach to the policy.",
    )
    usestoragereplication: Optional[bool] = Field(
        default=None,
        description="If True, copy snapshots to supported primary storage via storage replication.",
    )
    zoneids: Optional[list[UUID4]] = Field(
        default=None,
        description="Zone IDs where snapshots will be made available.",
    )

    @field_serializer("storageids", "zoneids")
    def serialize_csv(self, value: list[Any] | None) -> str | None:
        if value is None:
            return None
        return ",".join(str(v) for v in value)


class CreateVMSnapshotRequest(APIRequest):
    """Request parameters for ``createVMSnapshot``. Asynchronous.

    Reference: https://cloudstack.apache.org/api/apidocs-4.22/apis/createVMSnapshot.html
    """

    virtualmachineid: UUID4 = Field(..., description="The ID of the VM.")

    description: Optional[str] = Field(default=None, description="Description of the snapshot.")
    name: Optional[str] = Field(default=None, description="Display name of the snapshot.")
    quiescevm: Optional[bool] = Field(
        default=None,
        description="If True, quiesce the VM before taking the snapshot.",
    )
    snapshotmemory: Optional[bool] = Field(
        default=None,
        description="If True, include VM memory state in the snapshot.",
    )


class DeleteSnapshotRequest(APIRequest):
    """Request parameters for ``deleteSnapshot``. Asynchronous.

    Reference: https://cloudstack.apache.org/api/apidocs-4.22/apis/deleteSnapshot.html
    """

    id: UUID4 = Field(..., description="The ID of the snapshot to delete.")


class DeleteSnapshotPoliciesRequest(APIRequest):
    """Request parameters for ``deleteSnapshotPolicies``.

    Either ``id`` or ``ids`` must be provided (not both).

    Reference: https://cloudstack.apache.org/api/apidocs-4.22/apis/deleteSnapshotPolicies.html
    """

    id: Optional[UUID4] = Field(
        default=None,
        description="The ID of the snapshot policy. Mutually exclusive with ids.",
    )
    ids: Optional[list[UUID4]] = Field(
        default=None,
        description="Comma-separated list of snapshot policy IDs. Mutually exclusive with id.",
    )

    @model_validator(mode="after")
    def check_id_mutex(self) -> "DeleteSnapshotPoliciesRequest":
        if self.id is None and self.ids is None:
            raise ValueError("At least one of 'id' or 'ids' must be provided.")
        if self.id is not None and self.ids is not None:
            raise ValueError("'id' and 'ids' are mutually exclusive.")
        return self

    @field_serializer("ids")
    def serialize_csv(self, value: list[Any] | None) -> str | None:
        if value is None:
            return None
        return ",".join(str(v) for v in value)


class DeleteVMSnapshotRequest(APIRequest):
    """Request parameters for ``deleteVMSnapshot``. Asynchronous.

    Reference: https://cloudstack.apache.org/api/apidocs-4.22/apis/deleteVMSnapshot.html
    """

    vmsnapshotid: UUID4 = Field(..., description="The ID of the VM snapshot to delete.")


class ExtractSnapshotRequest(APIRequest):
    """Request parameters for ``extractSnapshot``. Asynchronous.

    Reference: https://cloudstack.apache.org/api/apidocs-4.22/apis/extractSnapshot.html
    """

    id: UUID4 = Field(..., description="The ID of the snapshot.")
    zoneid: UUID4 = Field(..., description="The ID of the zone where the snapshot is located.")


class GetVolumeSnapshotDetailsRequest(APIRequest):
    """Request parameters for ``getVolumeSnapshotDetails``.

    Reference: https://cloudstack.apache.org/api/apidocs-4.22/apis/getVolumeSnapshotDetails.html
    """

    snapshotid: UUID4 = Field(..., description="CloudStack Snapshot UUID.")


class ListSnapshotPoliciesRequest(APIRequest, PaginationMixin):
    """Request parameters for ``listSnapshotPolicies``.

    Reference: https://cloudstack.apache.org/api/apidocs-4.22/apis/listSnapshotPolicies.html
    """

    account: Optional[str] = Field(
        default=None,
        description="List resources by account name. Must be used together with domainid.",
    )
    domainid: Optional[UUID4] = Field(
        default=None,
        description="List only resources belonging to this domain.",
    )
    fordisplay: Optional[bool] = Field(
        default=None,
        description="Filter by display flag. Only ROOT admins may use this parameter.",
    )
    id: Optional[UUID4] = Field(
        default=None,
        description="Filter by snapshot policy ID.",
    )
    isrecursive: Optional[bool] = Field(
        default=None,
        description=(
            "If True, list all resources from the domain specified by domainid "
            "down to every leaf subdomain."
        ),
    )
    keyword: Optional[str] = Field(default=None, description="List by keyword.")
    listall: Optional[bool] = Field(
        default=None,
        description=(
            "If False, list only resources owned by the caller. "
            "If True, list all resources the caller is authorised to see."
        ),
    )
    projectid: Optional[str] = Field(
        default=None,
        description="List objects by project UUID. Pass '-1' to list across all projects.",
    )
    volumeid: Optional[UUID4] = Field(
        default=None,
        description="Filter by disk volume ID.",
    )

    @model_validator(mode="after")
    def account_requires_domainid(self) -> "ListSnapshotPoliciesRequest":
        if self.account is not None and self.domainid is None:
            raise ValueError("'account' must be used together with 'domainid'.")
        return self


class ListSnapshotsRequest(APIRequest, PaginationMixin):
    """Request parameters for ``listSnapshots``.

    All fields are optional — the API returns all snapshots visible to the
    caller when no filters are supplied.

    Reference: https://cloudstack.apache.org/api/apidocs-4.22/apis/listSnapshots.html
    """

    account: Optional[str] = Field(
        default=None,
        description="List resources by account name. Must be used together with domainid.",
    )
    domainid: Optional[UUID4] = Field(
        default=None,
        description="List only resources belonging to this domain.",
    )
    id: Optional[UUID4] = Field(
        default=None,
        description="Filter by a single snapshot UUID. Mutually exclusive with ids.",
    )
    ids: Optional[list[UUID4]] = Field(
        default=None,
        description="Filter by a list of snapshot UUIDs. Mutually exclusive with id.",
    )
    imagestoreid: Optional[UUID4] = Field(
        default=None,
        description="Filter by image store or image cache store UUID.",
    )
    intervaltype: Optional[IntervalType] = Field(
        default=None,
        description="Filter by snapshot schedule interval type.",
    )
    isrecursive: Optional[bool] = Field(
        default=None,
        description=(
            "If True, list all resources from the domain specified by domainid "
            "down to every leaf subdomain."
        ),
    )
    keyword: Optional[str] = Field(
        default=None,
        description="Free-text keyword filter applied across searchable fields.",
    )
    listall: Optional[bool] = Field(
        default=None,
        description=(
            "If False (default), list only resources owned by the caller. "
            "If True, list all resources the caller is authorised to see. "
            "Project-dedicated resources are included only when projectid is set."
        ),
    )
    locationtype: Optional[LocationType] = Field(
        default=None,
        description=("Filter by storage location type. Only effective when showunique=False."),
    )
    name: Optional[str] = Field(default=None, description="Filter by snapshot name.")
    projectid: Optional[str] = Field(
        default=None,
        description="List snapshots for this project UUID. Pass '-1' to list across all projects.",
    )
    showunique: Optional[bool] = Field(
        default=None,
        description="If False, list snapshots across all zones and their backing stores.",
    )
    snapshottype: Optional[SnapshotType] = Field(
        default=None,
        description="Filter by snapshot type: MANUAL or RECURRING.",
    )
    storageid: Optional[UUID4] = Field(
        default=None,
        description="Filter by storage pool UUID.",
    )
    tags: Optional[dict[str, str]] = Field(
        default=None,
        description="Filter by tag key/value pairs (all supplied tags must match).",
    )
    volumeid: Optional[UUID4] = Field(
        default=None,
        description="Filter by the UUID of the source disk volume.",
    )
    zoneid: Optional[UUID4] = Field(
        default=None,
        description="Filter by availability zone UUID.",
    )

    @model_validator(mode="after")
    def check_id_mutex(self) -> "ListSnapshotsRequest":
        if self.id is not None and self.ids is not None:
            raise ValueError("'id' and 'ids' are mutually exclusive.")
        return self

    @model_validator(mode="after")
    def check_account_requires_domainid(self) -> "ListSnapshotsRequest":
        if self.account is not None and self.domainid is None:
            raise ValueError("'account' must be used together with 'domainid'.")
        return self

    @field_serializer("ids")
    def serialize_csv(self, value: list[Any] | None) -> str | None:
        if value is None:
            return None
        return ",".join(str(v) for v in value)


class ListVMSnapshotRequest(APIRequest, PaginationMixin):
    """Request parameters for ``listVMSnapshot``.

    Reference: https://cloudstack.apache.org/api/apidocs-4.22/apis/listVMSnapshot.html
    """

    account: Optional[str] = Field(
        default=None,
        description="List resources by account name. Must be used together with domainid.",
    )
    domainid: Optional[UUID4] = Field(
        default=None,
        description="List only resources belonging to this domain.",
    )
    isrecursive: Optional[bool] = Field(
        default=None,
        description=(
            "If True, list all resources from the domain specified by domainid "
            "down to every leaf subdomain."
        ),
    )
    keyword: Optional[str] = Field(default=None, description="List by keyword.")
    listall: Optional[bool] = Field(
        default=None,
        description=(
            "If False, list only resources owned by the caller. "
            "If True, list all resources the caller is authorised to see."
        ),
    )
    name: Optional[str] = Field(
        default=None,
        description="Filter by VM snapshot name or display name.",
    )
    projectid: Optional[str] = Field(
        default=None,
        description="List objects by project UUID. Pass '-1' to list across all projects.",
    )
    state: Optional[VMSnapshotState] = Field(
        default=None,
        description="Filter by VM snapshot state.",
    )
    tags: Optional[dict[str, str]] = Field(
        default=None,
        description="Filter by tag key/value pairs.",
    )
    virtualmachineid: Optional[UUID4] = Field(
        default=None,
        description="Filter by VM ID.",
    )
    vmsnapshotid: Optional[UUID4] = Field(
        default=None,
        description="Filter by VM snapshot ID. Mutually exclusive with vmsnapshotids.",
    )
    vmsnapshotids: Optional[list[UUID4]] = Field(
        default=None,
        description="Filter by multiple VM snapshot IDs. Mutually exclusive with vmsnapshotid.",
    )

    @model_validator(mode="after")
    def check_vmsnapshot_mutex(self) -> "ListVMSnapshotRequest":
        if self.vmsnapshotid is not None and self.vmsnapshotids is not None:
            raise ValueError("'vmsnapshotid' and 'vmsnapshotids' are mutually exclusive.")
        return self

    @model_validator(mode="after")
    def account_requires_domainid(self) -> "ListVMSnapshotRequest":
        if self.account is not None and self.domainid is None:
            raise ValueError("'account' must be used together with 'domainid'.")
        return self

    @field_serializer("vmsnapshotids")
    def serialize_csv(self, value: list[Any] | None) -> str | None:
        if value is None:
            return None
        return ",".join(str(v) for v in value)


class RevertSnapshotRequest(APIRequest):
    """Request parameters for ``revertSnapshot``. Asynchronous.

    Reference: https://cloudstack.apache.org/api/apidocs-4.22/apis/revertSnapshot.html
    """

    id: UUID4 = Field(..., description="The ID of the snapshot to revert to.")


class UpdateSnapshotPolicyRequest(APIRequest):
    """Request parameters for ``updateSnapshotPolicy``. Asynchronous.

    Reference: https://cloudstack.apache.org/api/apidocs-4.22/apis/updateSnapshotPolicy.html
    """

    customid: Optional[str] = Field(
        default=None,
        description="Custom ID for the resource. Root Admins only.",
    )
    fordisplay: Optional[bool] = Field(
        default=None,
        description="Whether to display the snapshot policy to the end user.",
    )
    id: Optional[UUID4] = Field(
        default=None,
        description="The ID of the snapshot policy to update.",
    )
