from pydantic import BaseModel, Field, model_validator
from typing import Optional


class AssignVolumeRequest(BaseModel):
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


class AttachVolumeRequest(BaseModel):
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


class ChangeOfferingForVolumeRequest(BaseModel):
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

class CheckVolumeRequest(BaseModel):
    id: str = Field(
        ..., description="ID of the volume to be checked"
    )

    repair: str = Field(
        ...,
        description="Flag to indicate if the volume should be repaired if any issues are found during the check"
    )

class CreateVolumeRequest(BaseModel):
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
    

class DestroyVolumeRequest(BaseModel):
    id: str = Field(
        ..., description="ID of the volume"
    )

    repair: Optional[bool] = Field(
        None
        expunge="If true is passed, the volume is expunged immediately."
    )

class DetachVolumeRequest(BaseModel):
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


class ExtractVolumeRequest(BaseModel):
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