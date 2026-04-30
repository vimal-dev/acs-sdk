from datetime import datetime

from pydantic import Field, field_serializer, field_validator, model_validator
from typing import List, Literal, Optional

from acs_sdk.schemas.request.base import APIRequest, PaginationMixin


class AssignVolumeRequest(APIRequest):
    volumeid: str = Field(
        ..., alias="id", description="ID of the volume to be reassigned"
    )

    accountid: Optional[str] = Field(
        None,
        alias="accountId",
        description="Account ID to assign the volume (mutually exclusive with projectid)",
    )

    projectid: Optional[str] = Field(
        None,
        alias="projectId",
        description="Project ID to assign the volume (mutually exclusive with accountid)",
    )

    @model_validator(mode="after")
    def validate_account_or_project(self):
        if not self.accountid and not self.projectid:
            raise ValueError("Either 'accountid' or 'projectid' must be provided")

        if self.accountid and self.projectid:
            raise ValueError("'accountid' and 'projectid' cannot be used together")

        return self


class AttachVolumeRequest(APIRequest):
    id: str = Field(..., description="ID of the volume to be attached")

    virtualmachineid: str = Field(
        ...,
        alias="instanceId",
        description="ID of the compute instance to which the volume will be attached",
    )

    deviceid: Optional[str] = Field(
        None,
        alias="deviceId",
        description="The ID of the device to map the volume to the guest OS. If no deviceID is informed, the next available deviceID will be chosen. Use 0 when volume needs to be attached as ROOT.",
    )


class ChangeOfferingForVolumeRequest(APIRequest):
    id: str = Field(
        ..., description="ID of the volume for which to change the offering"
    )

    diskofferingid: str = Field(
        ...,
        alias="diskOfferingId",
        description="ID of the new disk offering to apply to the volume",
    )

    automigrate: Optional[bool] = Field(
        None,
        alias="autoMigrate",
        description="Flag for automatic migration of the volume with new disk offering whenever migration is required to apply the offering",
    )

    maxiops: Optional[int] = Field(
        None, description="New maximum number of IOPS for the custom disk offering"
    )

    miniops: Optional[int] = Field(
        None, description="New minimum number of IOPS for the custom disk offering"
    )

    shrinkok: Optional[int] = Field(
        None, description="Flag to indicate if the volume can be shrunk"
    )

    size: Optional[int] = Field(
        None, description="New volume size in GB for the custom disk offering"
    )


class CheckVolumeRequest(APIRequest):
    id: str = Field(..., description="ID of the volume to be checked")

    repair: str = Field(
        ...,
        description="Flag to indicate if the volume should be repaired if any issues are found during the check",
    )


class CreateVolumeRequest(APIRequest):
    name: str = Field(..., description="Name of the volume to be created")

    diskofferingid: str = Field(
        ..., alias="diskOfferingId", description="ID of the disk offering."
    )

    snapshotid: Optional[str] = Field(
        None, alias="snapshotId", description="ID of the snapshot"
    )

    zoneid: str = Field(
        ..., alias="zoneId", description="ID of the zone in which to create the volume"
    )

    virtualmachineid: Optional[str] = Field(
        None,
        alias="instanceId",
        description="ID of the compute instance to which the volume will be attached",
    )

    displayvolume: Optional[bool] = Field(
        None,
        alias="displayVolume",
        description="Flag to indicate if the volume should be displayed to endusers or not",
    )

    size: Optional[int] = Field(
        None,
        description="Size of the volume in GB. If not specified, the default size of the disk offering will be used.",
    )

    maxiops: Optional[int] = Field(
        None, description="New maximum number of IOPS for the custom disk offering"
    )

    miniops: Optional[int] = Field(
        None, description="New minimum number of IOPS for the custom disk offering"
    )

    account: Optional[str] = Field(
        None, alias="accountId", description="Account ID (requires domainid)"
    )

    domainid: Optional[str] = Field(
        None, alias="domainId", description="Account name (requires domainid)"
    )

    projectid: Optional[str] = Field(
        None, description="Project ID (mutually exclusive with account)"
    )

    @model_validator(mode="after")
    def validate_source(self):
        if not self.diskofferingid and not self.snapshotid:
            raise ValueError("Either 'diskofferingid' or 'snapshotid' must be provided")
        return self

    @model_validator(mode="after")
    def validate_account_project(self):
        if self.account and self.projectid:
            raise ValueError("'accountid' and 'projectid' are mutually exclusive")
        return self

    @model_validator(mode="after")
    def validate_account_domain(self):
        if self.account and not self.domainid:
            raise ValueError("'domainid' must be provided when 'accountid' is used")
        return self


class DeleteVolumeRequest(APIRequest):
    id: str = Field(..., description="ID of the volume")


class DestroyVolumeRequest(APIRequest):
    id: str = Field(..., description="ID of the volume")

    repair: Optional[bool] = Field(
        None, description="If true is passed, the volume is expunged immediately."
    )


class DetachVolumeRequest(APIRequest):
    id: str = Field(..., description="ID of the volume to be detached")

    virtualmachineid: str = Field(
        ...,
        alias="instanceId",
        description="ID of the compute instance to which the volume will be attached",
    )

    deviceid: Optional[str] = Field(
        None,
        alias="deviceId",
        description="The ID of the device to map the volume to the guest OS. If no deviceID is informed, the next available deviceID will be chosen. Use 0 when volume needs to be attached as ROOT.",
    )


class ExtractVolumeRequest(APIRequest):
    id: str = Field(..., description="ID of the volume to be extracted")

    mode: str = Field(
        ...,
        description="The mode of extraction (e.g., 'HTTP_DOWNLOAD' or 'FTP_UPLOAD')",
    )

    zoneid: str = Field(
        ..., alias="zoneId", description="ID of the zone where the volume is located"
    )

    url: Optional[str] = Field(
        None,
        description="The URL of the secondary storage where the volume will be extracted to. This parameter is required when mode is FTP_UPLOAD.",
    )


class GetVolumeRequest(APIRequest):
    id: str = Field(..., description="ID of the volume")


class GetVolumeIscsiNameRequest(APIRequest):
    volumeid: str = Field(..., alias="volumeId", description="ID of the volume")


class GetUploadParamsForVolumeRequest(APIRequest):
    # Required
    name: str = Field(..., min_length=1, max_length=255)
    format: Literal["QCOW2", "OVA", "VHD"]
    zoneid: str

    # Optional
    diskofferingid: Optional[str] = None
    checksum: Optional[str] = None

    account: Optional[str] = None
    domainid: Optional[str] = None

    imagestoreuuid: Optional[str] = None
    projectid: Optional[str] = None

    # ---------------------------
    # Validators
    # ---------------------------

    @field_validator("checksum")
    @classmethod
    def validate_checksum(cls, v):
        if v is None:
            return v

        # Accept MD5 or {SHA-256} prefixed format
        if v.startswith("{SHA-256}"):
            return v

        if len(v) == 32:  # basic MD5 check
            return v

        raise ValueError("checksum must be MD5 or '{SHA-256}...' format")

    @field_validator("domainid")
    @classmethod
    def validate_account_domain(cls, v, info):
        account = info.data.get("account")
        if account and not v:
            raise ValueError("domainid is required when account is provided")
        return v


class ImportVolumeRequest(APIRequest):
    # ---------------------------
    # REQUIRED
    # ---------------------------
    path: str = Field(..., description="Path of the volume on storage")
    storageid: str = Field(..., alias="storageId", description="Storage pool ID")

    # ---------------------------
    # OPTIONAL
    # ---------------------------
    name: Optional[str] = Field(
        None,
        max_length=255,
        description="Volume name (defaults to path if not provided)",
    )

    diskofferingid: Optional[str] = Field(
        None, alias="diskOfferingId", description="Disk offering ID"
    )

    account: Optional[str] = Field(None, description="Account name (requires domainid)")

    domainid: Optional[str] = Field(
        None,
        alias="domainId",
        description="Domain ID (required if account is provided)",
    )

    projectid: Optional[str] = Field(None, alias="projectId", description="Project ID")

    # ---------------------------
    # VALIDATIONS
    # ---------------------------

    @field_validator("path")
    @classmethod
    def validate_path(cls, v):
        if not v.strip():
            raise ValueError("path cannot be empty")
        return v

    @model_validator(mode="after")
    def validate_account_domain(self):
        if self.account and not self.domainid:
            raise ValueError("domainid is required when account is provided")
        return self


class ListElastistorVolumesRequest(APIRequest):
    id: str = Field(
        ..., alias="accountId", description="the ID of the account to list volumes for"
    )


class ListVolumesRequest(APIRequest, PaginationMixin):

    # Basic filters
    id: Optional[str] = Field(None, description="ID of the disk volume")
    ids: Optional[List[str]] = Field(
        None, description="List of volume IDs (mutually exclusive with id)"
    )
    name: Optional[str] = Field(None, description="Name of the volume")
    keyword: Optional[str] = Field(None, description="Search keyword")

    # Account / Domain / Project
    account: Optional[str] = Field(
        None, description="List resources by account (requires domainid)"
    )
    domainid: Optional[str] = Field(None, alias="domainId", description="Domain ID")
    isrecursive: Optional[bool] = Field(
        None, alias="isRecursive", description="Include subdomains"
    )
    projectid: Optional[str] = Field(None, alias="projectId", description="Project ID")

    # Resource filters
    virtualmachineid: Optional[str] = Field(
        None, alias="virtualMachineId", description="Filter volumes attached to VM"
    )
    diskofferingid: Optional[str] = Field(
        None, alias="diskOfferingId", description="Filter by disk offering"
    )
    serviceofferingid: Optional[str] = Field(
        None,
        alias="serviceOfferingId",
        description="Filter by service offering disk offering",
    )

    storageid: Optional[str] = Field(
        None, alias="storageId", description="Storage pool ID (admin only)"
    )
    clusterid: Optional[str] = Field(None, alias="clusterId", description="Cluster ID")
    podid: Optional[str] = Field(None, alias="podId", description="Pod ID")
    hostid: Optional[str] = Field(None, alias="hostId", description="Host ID")
    zoneid: Optional[str] = Field(None, alias="zoneId", description="Zone ID")

    # State / type filters
    type: Optional[str] = Field(None, description="Volume type (ROOT or DATADISK)")
    state: Optional[str] = Field(
        None,
        description="Volume state (Ready, Allocated, Destroy, Expunging, Expunged)",
    )
    isencrypted: Optional[bool] = Field(
        None, alias="isEncrypted", description="Filter encrypted volumes"
    )

    # Visibility / admin flags
    listall: Optional[bool] = Field(
        None, alias="listAll", description="List all accessible resources"
    )
    displayvolume: Optional[bool] = Field(
        None, alias="displayVolume", description="Filter by display flag (admin only)"
    )
    listsystemvms: Optional[bool] = Field(
        None, alias="listSystemVms", description="List system VM volumes (admin only)"
    )

    # Tags
    tags: Optional[str] = Field(None, description="Filter by tags (key/value pairs)")

    # Special flags
    retrieveonlyresourcecount: Optional[bool] = Field(
        None,
        alias="retrieveOnlyResourceCount",
        description="Return only resource count",
    )


class ListVolumesForImportRequest(APIRequest, PaginationMixin):
    storageid: str = Field(
        ..., alias="storageId", description="Storage pool ID (admin only)"
    )

    # Basic filters
    keyword: Optional[str] = Field(None, description="Search keyword")
    path: Optional[str] = Field(None, description="Path of the volume on storage pool")


class ListVolumesUsageHistoryRequest(APIRequest, PaginationMixin):

    # Basic filters
    id: Optional[str] = Field(None, description="ID of the disk volume")
    ids: Optional[List[str]] = Field(
        None, description="List of volume IDs (mutually exclusive with id)"
    )
    name: Optional[str] = Field(None, description="Name of the volume")
    keyword: Optional[str] = Field(None, description="Search keyword")

    startdate: Optional[datetime] = Field(None, description="Start date")
    enddate: Optional[datetime] = Field(None, description="End date")

    # --------------------------------------------------
    # Validators
    # --------------------------------------------------

    @field_validator("enddate")
    @classmethod
    def validate_date_range(cls, v, info):
        if isinstance(v, datetime):
            start = info.data.get("startdate")
            if start and v < start:
                raise ValueError("enddate must be >= startdate")
        return v

    @field_serializer("startdate", "enddate")
    def serialize_date(self, value: datetime, _info):
        if isinstance(value, datetime):
            return value.strftime("%Y-%m-%dT%H:%M:%S%z")
        return value


class MigrateVolumeRequest(APIRequest):
    storageid: str = Field(
        ..., alias="storageId", description="Storage pool ID to migrate the volume to"
    )
    volumeid: str = Field(..., alias="volumeId", description="ID of the disk volume")
    newdiskofferingid: Optional[str] = Field(
        None,
        alias="newDiskOfferingId",
        description="New disk offering id to migrate the volume to",
    )
    livemigrate: Optional[bool] = Field(
        None, alias="liveMigrate", description="Whether to live migrate the volume"
    )


class RecoverVolumeRequest(APIRequest):
    id: str = Field(..., alias="volumeId", description="ID of the disk volume")


class ResizeVolumeRequest(APIRequest):
    id: str = Field(..., alias="volumeId", description="ID of the disk volume")
    diskofferingid: Optional[str] = Field(
        None,
        alias="diskOfferingId",
        description="New disk offering id to migrate the volume to",
    )
    automigrate: Optional[bool] = Field(
        None,
        alias="autoMigrate",
        description="Flag to allow automatic migration of the volume to another suitable storage pool that accommodates the new size",
    )
    size: Optional[int] = Field(
        None,
        description="Size of the volume in GB. If not specified, the default size of the disk offering will be used.",
    )

    maxiops: Optional[int] = Field(
        None, description="New maximum number of IOPS for the custom disk offering"
    )

    miniops: Optional[int] = Field(
        None, description="New minimum number of IOPS for the custom disk offering"
    )

    shrinkok: Optional[int] = Field(
        None, description="Flag to indicate if the volume can be shrunk"
    )

    @field_validator("maxiops")
    @classmethod
    def validate_iops_range(cls, v, info):
        start = info.data.get("miniops")
        if start and v < start:
            raise ValueError("maxiops must be >= miniops")
        return v


class ResizeVolumeFromBackupAndAttachToVMRequest(APIRequest):
    backupid: str = Field(
        ..., alias="backupId", description="ID of the backup to restore the volume from"
    )
    volumeid: str = Field(..., alias="volumeId", description="ID of the disk volume")
    virtualmachineid: Optional[str] = Field(
        None,
        alias="virtualMachineId",
        description="ID of the virtual machine to attach the volume to",
    )


class UnmanageVolumeRequest(APIRequest):
    id: str = Field(
        ..., alias="volumeId", description="The ID of the volume to unmanage"
    )


class UpdateVolumeRequest(APIRequest):
    # ---------------------------
    # IDENTIFIER (recommended)
    # ---------------------------
    id: Optional[str] = Field(None, description="ID of the disk volume")

    # ---------------------------
    # OPTIONAL FIELDS
    # ---------------------------

    name: Optional[str] = Field(None, description="Name of the volume")

    path: Optional[str] = Field(None, description="New path of the volume")

    deleteprotection: Optional[bool] = Field(
        None,
        alias="deleteProtection",
        description="Flag to indicate if the volume has delete protection enabled or not",
    )

    displayvolume: Optional[bool] = Field(
        None, alias="displayVolume", description="Whether to display volume to end user"
    )

    chaininfo: Optional[str] = Field(None, description="Chain info of the volume")

    customid: Optional[str] = Field(
        None, description="Custom resource ID (Root Admin only)"
    )

    state: Optional[str] = Field(None, description="State of the volume")

    storageid: Optional[str] = Field(None, description="Destination storage pool UUID")

    # ---------------------------
    # VALIDATIONS
    # ---------------------------

    @field_validator("path")
    @classmethod
    def validate_path(cls, v):
        if v is not None and not v.strip():
            raise ValueError("path cannot be empty")
        return v


class UploadVolumeRequest(APIRequest):
    # ---------------------------
    # REQUIRED
    # ---------------------------
    name: str = Field(..., min_length=1, max_length=255)
    format: Literal["QCOW2", "OVA", "VHD"] = Field(
        ..., description="Format of the volume being uploaded"
    )
    url: str = Field(..., description="HTTP/HTTPS URL of volume")
    zoneid: str = Field(
        ..., alias="zoneId", description="ID of the zone the volume is to be hosted on"
    )

    # ---------------------------
    # OPTIONAL
    # ---------------------------
    checksum: Optional[str] = Field(
        None, description="MD5 or {SHA-256} prefixed checksum"
    )

    diskofferingid: Optional[str] = Field(
        None, description="Must be custom disk offering"
    )

    account: Optional[str] = Field(None, description="Account name (requires domainid)")

    domainid: Optional[str] = Field(
        None,
        alias="domainId",
        description="Domain ID (required if account is provided)",
    )

    imagestoreuuid: Optional[str] = Field(
        None, alias="imageStoreUuid", description="Image store UUID for the volume"
    )
    projectid: Optional[str] = Field(
        None,
        alias="projectId",
        description="Project ID (mutually exclusive with account)",
    )

    # ---------------------------
    # VALIDATIONS
    # ---------------------------

    @field_validator("url")
    @classmethod
    def validate_url(cls, v):
        if not (v.startswith("http://") or v.startswith("https://")):
            raise ValueError("url must start with http:// or https://")
        return v

    # @field_validator("checksum")
    # @classmethod
    # def validate_checksum(cls, v):
    #     if v is None:
    #         return v

    #     md5_regex = re.compile(r"^[a-fA-F0-9]{32}$")
    #     sha256_regex = re.compile(r"^\{SHA-256\}[a-fA-F0-9]{64}$")

    #     if md5_regex.match(v) or sha256_regex.match(v):
    #         return v

    #     raise ValueError(
    #         "checksum must be MD5 (32 hex) or '{SHA-256}...' format"
    #     )

    @model_validator(mode="after")
    def validate_account_domain(self):
        if self.account and not self.domainid:
            raise ValueError("domainid is required when account is provided")
        return self
