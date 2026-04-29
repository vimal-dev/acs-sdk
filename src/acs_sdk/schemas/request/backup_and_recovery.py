from typing import Optional

from pydantic import Field

from acs_sdk.schemas.request.base import APIRequest


class AddBackupRepositoryRequest(APIRequest):
    name: str = Field(..., description="Name of the backup repository")
    url: str = Field(..., description="Repository URL")
    provider: str = Field(..., description="Backup provider name")
    zoneid: str = Field(..., alias="zoneId", description="Zone ID of the repository")


class CreateBackupRequest(APIRequest):
    volumeid: str = Field(..., alias="volumeId", description="Volume ID to back up")
    backupofferingid: Optional[str] = Field(
        None, alias="backupOfferingId", description="Backup offering ID"
    )
    snapshotid: Optional[str] = Field(
        None, alias="snapshotId", description="Snapshot ID to back up"
    )
    name: Optional[str] = Field(None, description="Optional name for the backup")


class CreateVMFromBackupRequest(APIRequest):
    backupid: str = Field(..., alias="backupId", description="Backup ID to restore from")
    zoneid: str = Field(..., alias="zoneId", description="Zone ID for the new VM")
    serviceofferingid: str = Field(
        ..., alias="serviceOfferingId", description="Service offering ID for the new VM"
    )
    templateid: str = Field(..., alias="templateId", description="Template ID for the new VM")
    name: Optional[str] = Field(None, description="Name of the new VM")


class DeleteBackupRequest(APIRequest):
    id: str = Field(..., description="Backup ID to delete")


class DeleteBackupOfferingRequest(APIRequest):
    id: str = Field(..., description="Backup offering ID to delete")


class DeleteBackupRepositoryRequest(APIRequest):
    id: str = Field(..., description="Backup repository ID to delete")


class ListBackupOfferingsRequest(APIRequest):
    id: Optional[str] = Field(None, description="List backup offerings by ID")
    name: Optional[str] = Field(None, description="List backup offerings by name")
    page: Optional[int] = Field(1, ge=1, description="Page number")
    pagesize: Optional[int] = Field(50, ge=1, le=500, description="Number of results per page")


class ListBackupProviderOfferingsRequest(APIRequest):
    id: Optional[str] = Field(None, description="List backup provider offerings by ID")
    provider: Optional[str] = Field(None, description="Filter by provider name")
    page: Optional[int] = Field(1, ge=1, description="Page number")
    pagesize: Optional[int] = Field(50, ge=1, le=500, description="Number of results per page")


class ListBackupProvidersRequest(APIRequest):
    id: Optional[str] = Field(None, description="List backup providers by ID")
    name: Optional[str] = Field(None, description="List backup providers by name")
    page: Optional[int] = Field(1, ge=1, description="Page number")
    pagesize: Optional[int] = Field(50, ge=1, le=500, description="Number of results per page")


class ListBackupRepositoriesRequest(APIRequest):
    id: Optional[str] = Field(None, description="List backup repositories by ID")
    name: Optional[str] = Field(None, description="List backup repositories by name")
    page: Optional[int] = Field(1, ge=1, description="Page number")
    pagesize: Optional[int] = Field(50, ge=1, le=500, description="Number of results per page")


class ListBackupScheduleRequest(APIRequest):
    id: Optional[str] = Field(None, description="List backup schedules by ID")
    backupofferingid: Optional[str] = Field(
        None, alias="backupOfferingId", description="List backup schedules by backup offering ID"
    )
    page: Optional[int] = Field(1, ge=1, description="Page number")
    pagesize: Optional[int] = Field(50, ge=1, le=500, description="Number of results per page")


class ListBackupsRequest(APIRequest):
    id: Optional[str] = Field(None, description="List backups by ID")
    volumeid: Optional[str] = Field(None, alias="volumeId", description="List backups by volume ID")
    backupofferingid: Optional[str] = Field(
        None, alias="backupOfferingId", description="List backups by offering ID"
    )
    page: Optional[int] = Field(1, ge=1, description="Page number")
    pagesize: Optional[int] = Field(50, ge=1, le=500, description="Number of results per page")


class RestoreBackupRequest(APIRequest):
    backupid: str = Field(..., alias="backupId", description="Backup ID to restore")


class UpdateBackupOfferingRequest(APIRequest):
    id: str = Field(..., description="Backup offering ID to update")
    name: Optional[str] = Field(None, description="New name for the backup offering")


class UpdateBackupRepositoryRequest(APIRequest):
    id: str = Field(..., description="Backup repository ID to update")
    name: Optional[str] = Field(None, description="New name for the backup repository")
    url: Optional[str] = Field(None, description="New repository URL")
    provider: Optional[str] = Field(None, description="New backup provider name")


class CreateBackupScheduleRequest(APIRequest):
    backupofferingid: str = Field(
        ..., alias="backupOfferingId", description="Backup offering ID to schedule"
    )
    schedule: str = Field(..., description="Backup schedule definition")
    timezone: Optional[str] = Field(None, description="Timezone for the schedule")


class UpdateBackupScheduleRequest(APIRequest):
    id: str = Field(..., description="Backup schedule ID to update")
    schedule: Optional[str] = Field(None, description="Updated backup schedule definition")
    timezone: Optional[str] = Field(None, description="Updated timezone for the schedule")
