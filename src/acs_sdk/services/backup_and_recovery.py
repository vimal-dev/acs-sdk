# services/backup_and_recovery.py
from typing import Dict, List

from acs_sdk.schemas.request.backup_and_recovery import (
    AddBackupRepositoryRequest,
    CreateBackupRequest,
    CreateBackupScheduleRequest,
    CreateVMFromBackupRequest,
    DeleteBackupOfferingRequest,
    DeleteBackupRepositoryRequest,
    DeleteBackupRequest,
    ListBackupOfferingsRequest,
    ListBackupProvidersRequest,
    ListBackupProviderOfferingsRequest,
    ListBackupRepositoriesRequest,
    ListBackupScheduleRequest,
    ListBackupsRequest,
    RestoreBackupRequest,
    UpdateBackupOfferingRequest,
    UpdateBackupRepositoryRequest,
    UpdateBackupScheduleRequest,
)

from .base import BaseService
from ..schemas.response.base import APIResponse


class BackupAndRecovery(BaseService):
    def add_backup_repository(self, payload: AddBackupRepositoryRequest) -> APIResponse[Dict]:
        """Add a backup repository."""
        response = self.client.call("addBackupRepository", payload.model_dump(exclude_none=True))
        data = {}
        if 'addbackuprepositoryresponse' in response:
            data = response['addbackuprepositoryresponse']
        return APIResponse[Dict](**{"data": data})

    async def add_backup_repository_async(self, payload: AddBackupRepositoryRequest) -> APIResponse[Dict]:
        """Asynchronously add a backup repository."""
        response = await self.client.call_async("addBackupRepository", payload.model_dump(exclude_none=True))
        data = {}
        if 'addbackuprepositoryresponse' in response:
            data = response['addbackuprepositoryresponse']
        return APIResponse[Dict](**{"data": data})

    def create_backup(self, payload: CreateBackupRequest) -> APIResponse[Dict]:
        """Create a backup."""
        response = self.client.call("createBackup", payload.model_dump(exclude_none=True))
        data = {}
        if 'createbackupresponse' in response:
            data = response['createbackupresponse']
        return APIResponse[Dict](**{"data": data})

    async def create_backup_async(self, payload: CreateBackupRequest) -> APIResponse[Dict]:
        """Asynchronously create a backup."""
        response = await self.client.call_async("createBackup", payload.model_dump(exclude_none=True))
        data = {}
        if 'createbackupresponse' in response:
            data = response['createbackupresponse']
        return APIResponse[Dict](**{"data": data})

    def create_vm_from_backup(self, payload: CreateVMFromBackupRequest) -> APIResponse[Dict]:
        """Create a VM from a backup."""
        response = self.client.call("createVMFromBackup", payload.model_dump(exclude_none=True))
        data = {}
        if 'createvmfrombackupresponse' in response:
            data = response['createvmfrombackupresponse']
        return APIResponse[Dict](**{"data": data})

    async def create_vm_from_backup_async(self, payload: CreateVMFromBackupRequest) -> APIResponse[Dict]:
        """Asynchronously create a VM from a backup."""
        response = await self.client.call_async("createVMFromBackup", payload.model_dump(exclude_none=True))
        data = {}
        if 'createvmfrombackupresponse' in response:
            data = response['createvmfrombackupresponse']
        return APIResponse[Dict](**{"data": data})

    def delete_backup(self, payload: DeleteBackupRequest) -> APIResponse[Dict]:
        """Delete a backup."""
        response = self.client.call("deleteBackup", payload.model_dump(exclude_none=True))
        data = {}
        if 'deletebackupresponse' in response:
            data = response['deletebackupresponse']
        return APIResponse[Dict](**{"data": data})

    async def delete_backup_async(self, payload: DeleteBackupRequest) -> APIResponse[Dict]:
        """Asynchronously delete a backup."""
        response = await self.client.call_async("deleteBackup", payload.model_dump(exclude_none=True))
        data = {}
        if 'deletebackupresponse' in response:
            data = response['deletebackupresponse']
        return APIResponse[Dict](**{"data": data})

    def restore_backup(self, payload: RestoreBackupRequest) -> APIResponse[Dict]:
        """Restore a backup."""
        response = self.client.call("restoreBackup", payload.model_dump(exclude_none=True))
        data = {}
        if 'restorebackupresponse' in response:
            data = response['restorebackupresponse']
        return APIResponse[Dict](**{"data": data})

    async def restore_backup_async(self, payload: RestoreBackupRequest) -> APIResponse[Dict]:
        """Asynchronously restore a backup."""
        response = await self.client.call_async("restoreBackup", payload.model_dump(exclude_none=True))
        data = {}
        if 'restorebackupresponse' in response:
            data = response['restorebackupresponse']
        return APIResponse[Dict](**{"data": data})

    def list_backups(self, payload: ListBackupsRequest) -> APIResponse[List[Dict]]:
        """List backups."""
        response = self.client.call("listBackups", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listbackupsresponse' in response:
            response = response['listbackupsresponse']
        if 'backup' in response and response['backup']:
            data = response['backup']
            count = response['count']
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    async def list_backups_async(self, payload: ListBackupsRequest) -> APIResponse[List[Dict]]:
        """Asynchronously list backups."""
        response = await self.client.call_async("listBackups", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listbackupsresponse' in response:
            response = response['listbackupsresponse']
        if 'backup' in response and response['backup']:
            data = response['backup']
            count = response['count']
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    def list_backup_offerings(self, payload: ListBackupOfferingsRequest) -> APIResponse[List[Dict]]:
        """List backup offerings."""
        response = self.client.call("listBackupOfferings", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listbackupofferingsresponse' in response:
            response = response['listbackupofferingsresponse']
        if 'backupoffering' in response and response['backupoffering']:
            data = response['backupoffering']
            count = response['count']
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    async def list_backup_offerings_async(self, payload: ListBackupOfferingsRequest) -> APIResponse[List[Dict]]:
        """Asynchronously list backup offerings."""
        response = await self.client.call_async("listBackupOfferings", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listbackupofferingsresponse' in response:
            response = response['listbackupofferingsresponse']
        if 'backupoffering' in response and response['backupoffering']:
            data = response['backupoffering']
            count = response['count']
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    def list_backup_provider_offerings(self, payload: ListBackupProviderOfferingsRequest) -> APIResponse[List[Dict]]:
        """List backup provider offerings."""
        response = self.client.call("listBackupProviderOfferings", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listbackupproviderofferingsresponse' in response:
            response = response['listbackupproviderofferingsresponse']
        if 'backupprovideroffering' in response and response['backupprovideroffering']:
            data = response['backupprovideroffering']
            count = response['count']
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    async def list_backup_provider_offerings_async(self, payload: ListBackupProviderOfferingsRequest) -> APIResponse[List[Dict]]:
        """Asynchronously list backup provider offerings."""
        response = await self.client.call_async("listBackupProviderOfferings", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listbackupproviderofferingsresponse' in response:
            response = response['listbackupproviderofferingsresponse']
        if 'backupprovideroffering' in response and response['backupprovideroffering']:
            data = response['backupprovideroffering']
            count = response['count']
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    def list_backup_providers(self, payload: ListBackupProvidersRequest) -> APIResponse[List[Dict]]:
        """List backup providers."""
        response = self.client.call("listBackupProviders", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listbackupprovidersresponse' in response:
            response = response['listbackupprovidersresponse']
        if 'backupprovider' in response and response['backupprovider']:
            data = response['backupprovider']
            count = response['count']
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    async def list_backup_providers_async(self, payload: ListBackupProvidersRequest) -> APIResponse[List[Dict]]:
        """Asynchronously list backup providers."""
        response = await self.client.call_async("listBackupProviders", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listbackupprovidersresponse' in response:
            response = response['listbackupprovidersresponse']
        if 'backupprovider' in response and response['backupprovider']:
            data = response['backupprovider']
            count = response['count']
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    def list_backup_repositories(self, payload: ListBackupRepositoriesRequest) -> APIResponse[List[Dict]]:
        """List backup repositories."""
        response = self.client.call("listBackupRepositories", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listbackuprepositoriesresponse' in response:
            response = response['listbackuprepositoriesresponse']
        if 'backuprepository' in response and response['backuprepository']:
            data = response['backuprepository']
            count = response['count']
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    async def list_backup_repositories_async(self, payload: ListBackupRepositoriesRequest) -> APIResponse[List[Dict]]:
        """Asynchronously list backup repositories."""
        response = await self.client.call_async("listBackupRepositories", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listbackuprepositoriesresponse' in response:
            response = response['listbackuprepositoriesresponse']
        if 'backuprepository' in response and response['backuprepository']:
            data = response['backuprepository']
            count = response['count']
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    def list_backup_schedule(self, payload: ListBackupScheduleRequest) -> APIResponse[List[Dict]]:
        """List backup schedules."""
        response = self.client.call("listBackupSchedule", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listbackupscheduleresponse' in response:
            response = response['listbackupscheduleresponse']
        if 'backupschedule' in response and response['backupschedule']:
            data = response['backupschedule']
            count = response['count']
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    async def list_backup_schedule_async(self, payload: ListBackupScheduleRequest) -> APIResponse[List[Dict]]:
        """Asynchronously list backup schedules."""
        response = await self.client.call_async("listBackupSchedule", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listbackupscheduleresponse' in response:
            response = response['listbackupscheduleresponse']
        if 'backupschedule' in response and response['backupschedule']:
            data = response['backupschedule']
            count = response['count']
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    def delete_backup_offering(self, payload: DeleteBackupOfferingRequest) -> APIResponse[Dict]:
        """Delete a backup offering."""
        response = self.client.call("deleteBackupOffering", payload.model_dump(exclude_none=True))
        data = {}
        if 'deletebackupofferingresponse' in response:
            data = response['deletebackupofferingresponse']
        return APIResponse[Dict](**{"data": data})

    async def delete_backup_offering_async(self, payload: DeleteBackupOfferingRequest) -> APIResponse[Dict]:
        """Asynchronously delete a backup offering."""
        response = await self.client.call_async("deleteBackupOffering", payload.model_dump(exclude_none=True))
        data = {}
        if 'deletebackupofferingresponse' in response:
            data = response['deletebackupofferingresponse']
        return APIResponse[Dict](**{"data": data})

    def update_backup_offering(self, payload: UpdateBackupOfferingRequest) -> APIResponse[Dict]:
        """Update a backup offering."""
        response = self.client.call("updateBackupOffering", payload.model_dump(exclude_none=True))
        data = {}
        if 'updatebackupofferingresponse' in response:
            data = response['updatebackupofferingresponse']
        return APIResponse[Dict](**{"data": data})

    async def update_backup_offering_async(self, payload: UpdateBackupOfferingRequest) -> APIResponse[Dict]:
        """Asynchronously update a backup offering."""
        response = await self.client.call_async("updateBackupOffering", payload.model_dump(exclude_none=True))
        data = {}
        if 'updatebackupofferingresponse' in response:
            data = response['updatebackupofferingresponse']
        return APIResponse[Dict](**{"data": data})

    def update_backup_repository(self, payload: UpdateBackupRepositoryRequest) -> APIResponse[Dict]:
        """Update a backup repository."""
        response = self.client.call("updateBackupRepository", payload.model_dump(exclude_none=True))
        data = {}
        if 'updatebackuprepositoryresponse' in response:
            data = response['updatebackuprepositoryresponse']
        return APIResponse[Dict](**{"data": data})

    async def update_backup_repository_async(self, payload: UpdateBackupRepositoryRequest) -> APIResponse[Dict]:
        """Asynchronously update a backup repository."""
        response = await self.client.call_async("updateBackupRepository", payload.model_dump(exclude_none=True))
        data = {}
        if 'updatebackuprepositoryresponse' in response:
            data = response['updatebackuprepositoryresponse']
        return APIResponse[Dict](**{"data": data})

    def create_backup_schedule(self, payload: CreateBackupScheduleRequest) -> APIResponse[Dict]:
        """Create a backup schedule."""
        response = self.client.call("createBackupSchedule", payload.model_dump(exclude_none=True))
        data = {}
        if 'createbackupscheduleresponse' in response:
            data = response['createbackupscheduleresponse']
        return APIResponse[Dict](**{"data": data})

    async def create_backup_schedule_async(self, payload: CreateBackupScheduleRequest) -> APIResponse[Dict]:
        """Asynchronously create a backup schedule."""
        response = await self.client.call_async("createBackupSchedule", payload.model_dump(exclude_none=True))
        data = {}
        if 'createbackupscheduleresponse' in response:
            data = response['createbackupscheduleresponse']
        return APIResponse[Dict](**{"data": data})

    def update_backup_schedule(self, payload: UpdateBackupScheduleRequest) -> APIResponse[Dict]:
        """Update a backup schedule."""
        response = self.client.call("updateBackupSchedule", payload.model_dump(exclude_none=True))
        data = {}
        if 'updatebackupscheduleresponse' in response:
            data = response['updatebackupscheduleresponse']
        return APIResponse[Dict](**{"data": data})

    async def update_backup_schedule_async(self, payload: UpdateBackupScheduleRequest) -> APIResponse[Dict]:
        """Asynchronously update a backup schedule."""
        response = await self.client.call_async("updateBackupSchedule", payload.model_dump(exclude_none=True))
        data = {}
        if 'updatebackupscheduleresponse' in response:
            data = response['updatebackupscheduleresponse']
        return APIResponse[Dict](**{"data": data})
