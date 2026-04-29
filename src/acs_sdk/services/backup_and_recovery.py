# services/backup_and_recovery.py
from typing import Dict, List

from acs_sdk.schemas.request.backup_and_recovery import (
    AddBackupRepositoryRequest,
    CreateBackupRequest,
    CreateBackupScheduleRequest,
    CreateVMFromBackupRequest,
    DeleteBackupOfferingRequest,
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
        return self._execute(
            "addBackupRepository",
            payload,
            envelope="addbackuprepositoryresponse",
        )

    async def add_backup_repository_async(
        self, payload: AddBackupRepositoryRequest
    ) -> APIResponse[Dict]:
        """Asynchronously add a backup repository."""
        return await self._execute_async(
            "addBackupRepository",
            payload,
            envelope="addbackuprepositoryresponse",
        )

    def create_backup(self, payload: CreateBackupRequest) -> APIResponse[Dict]:
        """Create a backup."""
        return self._execute(
            "createBackup",
            payload,
            envelope="createbackupresponse",
        )

    async def create_backup_async(self, payload: CreateBackupRequest) -> APIResponse[Dict]:
        """Asynchronously create a backup."""
        return await self._execute_async(
            "createBackup",
            payload,
            envelope="createbackupresponse",
        )

    def create_vm_from_backup(self, payload: CreateVMFromBackupRequest) -> APIResponse[Dict]:
        """Create a VM from a backup."""
        return self._execute(
            "createVMFromBackup",
            payload,
            envelope="createvmfrombackupresponse",
        )

    async def create_vm_from_backup_async(
        self, payload: CreateVMFromBackupRequest
    ) -> APIResponse[Dict]:
        """Asynchronously create a VM from a backup."""
        return await self._execute_async(
            "createVMFromBackup",
            payload,
            envelope="createvmfrombackupresponse",
        )

    def delete_backup(self, payload: DeleteBackupRequest) -> APIResponse[Dict]:
        """Delete a backup."""
        return self._execute(
            "deleteBackup",
            payload,
            envelope="deletebackupresponse",
        )

    async def delete_backup_async(self, payload: DeleteBackupRequest) -> APIResponse[Dict]:
        """Asynchronously delete a backup."""
        return await self._execute_async(
            "deleteBackup",
            payload,
            envelope="deletebackupresponse",
        )

    def restore_backup(self, payload: RestoreBackupRequest) -> APIResponse[Dict]:
        """Restore a backup."""
        return self._execute(
            "restoreBackup",
            payload,
            envelope="restorebackupresponse",
        )

    async def restore_backup_async(self, payload: RestoreBackupRequest) -> APIResponse[Dict]:
        """Asynchronously restore a backup."""
        return await self._execute_async(
            "restoreBackup",
            payload,
            envelope="restorebackupresponse",
        )

    def list_backups(self, payload: ListBackupsRequest) -> APIResponse[List[Dict]]:
        """List backups."""
        return self._execute(
            "listBackups",
            payload,
            envelope="listbackupsresponse",
            entity="backup",
        )

    async def list_backups_async(self, payload: ListBackupsRequest) -> APIResponse[List[Dict]]:
        """Asynchronously list backups."""
        return await self._execute_async(
            "listBackups",
            payload,
            envelope="listbackupsresponse",
            entity="backup",
        )

    def list_backup_offerings(self, payload: ListBackupOfferingsRequest) -> APIResponse[List[Dict]]:
        """List backup offerings."""
        return self._execute(
            "listBackupOfferings",
            payload,
            envelope="listbackupofferingsresponse",
            entity="backupoffering",
        )

    async def list_backup_offerings_async(
        self, payload: ListBackupOfferingsRequest
    ) -> APIResponse[List[Dict]]:
        """Asynchronously list backup offerings."""
        return await self._execute_async(
            "listBackupOfferings",
            payload,
            envelope="listbackupofferingsresponse",
            entity="backupoffering",
        )

    def list_backup_provider_offerings(
        self, payload: ListBackupProviderOfferingsRequest
    ) -> APIResponse[List[Dict]]:
        """List backup provider offerings."""
        return self._execute(
            "listBackupProviderOfferings",
            payload,
            envelope="listbackupproviderofferingsresponse",
            entity="backupprovideroffering",
        )

    async def list_backup_provider_offerings_async(
        self, payload: ListBackupProviderOfferingsRequest
    ) -> APIResponse[List[Dict]]:
        """Asynchronously list backup provider offerings."""
        return await self._execute_async(
            "listBackupProviderOfferings",
            payload,
            envelope="listbackupproviderofferingsresponse",
            entity="backupprovideroffering",
        )

    def list_backup_providers(self, payload: ListBackupProvidersRequest) -> APIResponse[List[Dict]]:
        """List backup providers."""
        return self._execute(
            "listBackupProviders",
            payload,
            envelope="listbackupprovidersresponse",
            entity="backupprovider",
        )

    async def list_backup_providers_async(
        self, payload: ListBackupProvidersRequest
    ) -> APIResponse[List[Dict]]:
        """Asynchronously list backup providers."""
        return await self._execute_async(
            "listBackupProviders",
            payload,
            envelope="listbackupprovidersresponse",
            entity="backupprovider",
        )

    def list_backup_repositories(
        self, payload: ListBackupRepositoriesRequest
    ) -> APIResponse[List[Dict]]:
        """List backup repositories."""
        return self._execute(
            "listBackupRepositories",
            payload,
            envelope="listbackuprepositoriesresponse",
            entity="backuprepository",
        )

    async def list_backup_repositories_async(
        self, payload: ListBackupRepositoriesRequest
    ) -> APIResponse[List[Dict]]:
        """Asynchronously list backup repositories."""
        return await self._execute_async(
            "listBackupRepositories",
            payload,
            envelope="listbackuprepositoriesresponse",
            entity="backuprepository",
        )

    def list_backup_schedule(self, payload: ListBackupScheduleRequest) -> APIResponse[List[Dict]]:
        """List backup schedules."""
        return self._execute(
            "listBackupSchedule",
            payload,
            envelope="listbackupscheduleresponse",
            entity="backupschedule",
        )

    async def list_backup_schedule_async(
        self, payload: ListBackupScheduleRequest
    ) -> APIResponse[List[Dict]]:
        """Asynchronously list backup schedules."""
        return await self._execute_async(
            "listBackupSchedule",
            payload,
            envelope="listbackupscheduleresponse",
            entity="backupschedule",
        )

    def delete_backup_offering(self, payload: DeleteBackupOfferingRequest) -> APIResponse[Dict]:
        """Delete a backup offering."""
        return self._execute(
            "deleteBackupOffering",
            payload,
            envelope="deletebackupofferingresponse",
            entity="backupoffering",
        )

    async def delete_backup_offering_async(
        self, payload: DeleteBackupOfferingRequest
    ) -> APIResponse[Dict]:
        """Asynchronously delete a backup offering."""
        return await self._execute_async(
            "deleteBackupOffering",
            payload,
            envelope="deletebackupofferingresponse",
            entity="backupoffering",
        )

    def update_backup_offering(self, payload: UpdateBackupOfferingRequest) -> APIResponse[Dict]:
        """Update a backup offering."""
        return self._execute(
            "updateBackupOffering",
            payload,
            envelope="updatebackupofferingresponse",
            entity="backupoffering",
        )

    async def update_backup_offering_async(
        self, payload: UpdateBackupOfferingRequest
    ) -> APIResponse[Dict]:
        """Asynchronously update a backup offering."""
        return await self._execute_async(
            "updateBackupOffering",
            payload,
            envelope="updatebackupofferingresponse",
            entity="backupoffering",
        )

    def update_backup_repository(self, payload: UpdateBackupRepositoryRequest) -> APIResponse[Dict]:
        """Update a backup repository."""
        return self._execute(
            "updateBackupRepository",
            payload,
            envelope="updatebackuprepositoryresponse",
            entity="backuprepository",
        )

    async def update_backup_repository_async(
        self, payload: UpdateBackupRepositoryRequest
    ) -> APIResponse[Dict]:
        """Asynchronously update a backup repository."""
        return await self._execute_async(
            "updateBackupRepository",
            payload,
            envelope="updatebackuprepositoryresponse",
            entity="backuprepository",
        )

    def create_backup_schedule(self, payload: CreateBackupScheduleRequest) -> APIResponse[Dict]:
        """Create a backup schedule."""
        return self._execute(
            "createBackupSchedule",
            payload,
            envelope="createbackupscheduleresponse",
            entity="backupschedule",
        )

    async def create_backup_schedule_async(
        self, payload: CreateBackupScheduleRequest
    ) -> APIResponse[Dict]:
        """Asynchronously create a backup schedule."""
        return await self._execute_async(
            "createBackupSchedule",
            payload,
            envelope="createbackupscheduleresponse",
            entity="backupschedule",
        )

    def update_backup_schedule(self, payload: UpdateBackupScheduleRequest) -> APIResponse[Dict]:
        """Update a backup schedule."""
        return self._execute(
            "updateBackupSchedule",
            payload,
            envelope="updatebackupscheduleresponse",
            entity="backupschedule",
        )

    async def update_backup_schedule_async(
        self, payload: UpdateBackupScheduleRequest
    ) -> APIResponse[Dict]:
        """Asynchronously update a backup schedule."""
        return await self._execute_async(
            "updateBackupSchedule",
            payload,
            envelope="updatebackupscheduleresponse",
            entity="backupschedule",
        )
