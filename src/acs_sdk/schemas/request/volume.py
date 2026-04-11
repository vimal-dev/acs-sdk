from pydantic import Field, model_validator
from typing import List, Optional

from acs_sdk.schemas.request.base import APIRequest


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
    id: str = Field(
        ..., description="ID of the volume to be attached"
    )

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
        description="ID of the new disk offering to apply to the volume"
    )

    automigrate: Optional[bool] = Field(
        None,
        alias="autoMigrate",
        description="Flag for automatic migration of the volume with new disk offering whenever migration is required to apply the offering"
    )

    maxiops: Optional[int] = Field(
        None,
        description="New maximum number of IOPS for the custom disk offering"
    )

    miniops: Optional[int] = Field(
        None,
        description="New minimum number of IOPS for the custom disk offering"
    )

    shrinkok: Optional[int] = Field(
        None,
        description="Flag to indicate if the volume can be shrunk"
    )

    size: Optional[int] = Field(
        None,
        description="New volume size in GB for the custom disk offering"
    )

class CheckVolumeRequest(APIRequest):
    id: str = Field(
        ..., description="ID of the volume to be checked"
    )

    repair: str = Field(
        ...,
        description="Flag to indicate if the volume should be repaired if any issues are found during the check"
    )

class CreateVolumeRequest(APIRequest):
    name: str = Field(
        ..., description="Name of the volume to be created"
    )

    diskofferingid: str = Field(
        ...,
        alias="diskOfferingId",
        description="ID of the disk offering."
    )

    snapshotid: Optional[str] = Field(
        None,
        alias="snapshotId",
        description="ID of the snapshot"
    )

    zoneid: str = Field(
        ...,
        alias="zoneId",
        description="ID of the zone in which to create the volume"
    )

    virtualmachineid: Optional[str] = Field(
        None,
        alias="instanceId",
        description="ID of the compute instance to which the volume will be attached",
    )

    displayvolume: Optional[bool] = Field(
        None,
        alias="displayVolume",
        description="Flag to indicate if the volume should be displayed to endusers or not"
    )

    size: Optional[int] = Field(
        None,
        description="Size of the volume in GB. If not specified, the default size of the disk offering will be used."
    )

    maxiops: Optional[int] = Field(
        None,
        description="New maximum number of IOPS for the custom disk offering"
    )

    miniops: Optional[int] = Field(
        None,
        description="New minimum number of IOPS for the custom disk offering"
    )

    account: Optional[str] = Field(
        None,
        alias="accountId",
        description="Account ID (requires domainid)"
    )

    domainid: Optional[str] = Field(
        None,
        alias="domainId",
        description="Account name (requires domainid)"
    )

    projectid: Optional[str] = Field(
        None,
        description="Project ID (mutually exclusive with account)"
    )

    @model_validator(mode="after")
    def validate_source(self):
        if not self.diskofferingid and not self.snapshotid:
            raise ValueError(
                "Either 'diskofferingid' or 'snapshotid' must be provided"
            )
        return self

    @model_validator(mode="after")
    def validate_account_project(self):
        if self.account and self.projectid:
            raise ValueError(
                "'accountid' and 'projectid' are mutually exclusive"
            )
        return self

    @model_validator(mode="after")
    def validate_account_domain(self):
        if self.account and not self.domainid:
            raise ValueError(
                "'domainid' must be provided when 'accountid' is used"
            )
        return self
    

class DestroyVolumeRequest(APIRequest):
    id: str = Field(
        ..., description="ID of the volume"
    )

    repair: Optional[bool] = Field(
        None,
        description="If true is passed, the volume is expunged immediately."
    )

class DetachVolumeRequest(APIRequest):
    id: str = Field(
        ..., description="ID of the volume to be detached"
    )

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
    id: str = Field(
        ..., description="ID of the volume to be extracted"
    )

    mode: str = Field(
        ...,
        description="The mode of extraction (e.g., 'HTTP_DOWNLOAD' or 'FTP_UPLOAD')"
    )

    zoneid: str = Field(
        ...,
        alias="zoneId",
        description="ID of the zone where the volume is located"
    )

    url: Optional[str] = Field(
        None,
        description="The URL of the secondary storage where the volume will be extracted to. This parameter is required when mode is FTP_UPLOAD."
    )


class ListVolumesRequest(APIRequest):
    command: str = Field(default="listVolumes", frozen=True)

    # 🔍 Basic filters
    id: Optional[str] = Field(None, description="ID of the disk volume")
    ids: Optional[List[str]] = Field(
        None,
        description="List of volume IDs (mutually exclusive with id)"
    )
    name: Optional[str] = Field(None, description="Name of the volume")
    keyword: Optional[str] = Field(None, description="Search keyword")

    # 👤 Account / Domain / Project
    account: Optional[str] = Field(
        None,
        description="List resources by account (requires domainid)"
    )
    domainid: Optional[str] = Field(None, description="Domain ID")
    isrecursive: Optional[bool] = Field(
        None,
        description="Include subdomains"
    )
    projectid: Optional[str] = Field(None, description="Project ID")

    # 📦 Resource filters
    virtualmachineid: Optional[str] = Field(
        None,
        description="Filter volumes attached to VM"
    )
    diskofferingid: Optional[str] = Field(
        None,
        description="Filter by disk offering"
    )
    serviceofferingid: Optional[str] = Field(
        None,
        description="Filter by service offering disk offering"
    )

    storageid: Optional[str] = Field(
        None,
        description="Storage pool ID (admin only)"
    )
    clusterid: Optional[str] = Field(None, description="Cluster ID")
    podid: Optional[str] = Field(None, description="Pod ID")
    hostid: Optional[str] = Field(None, description="Host ID")
    zoneid: Optional[str] = Field(None, description="Zone ID")

    # 🔐 State / type filters
    type: Optional[str] = Field(
        None,
        description="Volume type (ROOT or DATADISK)"
    )
    state: Optional[str] = Field(
        None,
        description="Volume state (Ready, Allocated, Destroy, Expunging, Expunged)"
    )
    isencrypted: Optional[bool] = Field(
        None,
        description="Filter encrypted volumes"
    )

    # 👁️ Visibility / admin flags
    listall: Optional[bool] = Field(
        None,
        description="List all accessible resources"
    )
    displayvolume: Optional[bool] = Field(
        None,
        description="Filter by display flag (admin only)"
    )
    listsystemvms: Optional[bool] = Field(
        None,
        description="List system VM volumes (admin only)"
    )

    # 🏷️ Tags
    tags: Optional[str] = Field(
        None,
        description="Filter by tags (key/value pairs)"
    )

    # 📊 Special flags
    retrieveonlyresourcecount: Optional[bool] = Field(
        None,
        description="Return only resource count"
    )

    # 📄 Pagination
    page: Optional[int] = Field(None, ge=1)
    pagesize: Optional[int] = Field(None, ge=1)