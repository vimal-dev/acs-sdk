# services/volume.py
from typing import Dict

from acs_sdk.schemas.request.volume import (
    AssignVolumeRequest,
    AttachVolumeRequest,
    ChangeOfferingForVolumeRequest,
    CheckVolumeRequest,
    CreateVolumeRequest,
    DeleteVolumeRequest,
    DestroyVolumeRequest,
    DetachVolumeRequest,
    ExtractVolumeRequest,
    GetUploadParamsForVolumeRequest,
    GetVolumeIscsiNameRequest,
    GetVolumeRequest,
    ImportVolumeRequest,
    ListElastistorVolumesRequest,
    ListVolumesForImportRequest,
    ListVolumesRequest,
    ListVolumesUsageHistoryRequest,
    MigrateVolumeRequest,
    RecoverVolumeRequest,
    ResizeVolumeFromBackupAndAttachToVMRequest,
    ResizeVolumeRequest,
    UnmanageVolumeRequest,
    UpdateVolumeRequest,
    UploadVolumeRequest,
)

from .base import BaseService
from ..schemas.response.base import APIResponse


class Volume(BaseService):
    def assign_volume(self, payload: AssignVolumeRequest) -> APIResponse[Dict]:
        """Changes ownership of a Volume from one account to another."""
        return self._execute(
            "assignVolume",
            payload,
            envelope="assignvolumeresponse",
        )

    async def assign_volume_async(self, payload: AssignVolumeRequest) -> APIResponse[Dict]:
        """Changes ownership of a Volume from one account to another."""
        return await self._execute_async(
            "assignVolume",
            payload,
            envelope="assignvolumeresponse",
        )

    def attach_volume(self, payload: AttachVolumeRequest) -> APIResponse[Dict]:
        """Attaches a Volume to a Compute Instance."""
        return self._execute(
            "attachVolume",
            payload,
            envelope="attachvolumeresponse",
        )

    async def attach_volume_async(self, payload: AttachVolumeRequest) -> APIResponse[Dict]:
        """Attaches a Volume to a Compute Instance."""
        return await self._execute_async(
            "attachVolume",
            payload,
            envelope="attachvolumeresponse",
        )

    def change_offering(self, payload: ChangeOfferingForVolumeRequest) -> APIResponse[Dict]:
        """Change disk offering of the volume and also an option to auto migrate if required to apply the new disk offering."""
        return self._execute(
            "changeOfferingForVolume",
            payload,
            envelope="changeofferingforvolumeresponse",
        )

    async def change_offering_async(
        self, payload: ChangeOfferingForVolumeRequest
    ) -> APIResponse[Dict]:
        """Change disk offering of the volume and also an option to auto migrate if required to apply the new disk offering."""
        return await self._execute_async(
            "changeOfferingForVolume",
            payload,
            envelope="changeofferingforvolumeresponse",
        )

    def check_volume(self, payload: CheckVolumeRequest) -> APIResponse[Dict]:
        """Check the volume for any errors or leaks and also repairs when repair parameter is passed, this is currently supported for KVM only."""
        return self._execute(
            "checkVolume",
            payload,
            envelope="checkvolumeresponse",
        )

    async def check_volume_async(self, payload: CheckVolumeRequest) -> APIResponse[Dict]:
        """Check the volume for any errors or leaks and also repairs when repair parameter is passed, this is currently supported for KVM only."""
        return await self._execute_async(
            "checkVolume",
            payload,
            envelope="checkvolumeresponse",
        )

    def create_volume(self, payload: CreateVolumeRequest) -> APIResponse[Dict]:
        """Creates a disk volume from a disk offering. This disk volume must still be attached to a virtual machine to make use of it."""
        return self._execute(
            "createVolume",
            payload,
            envelope="createvolumeresponse",
        )

    async def create_volume_async(self, payload: CreateVolumeRequest) -> APIResponse[Dict]:
        """Creates a disk volume from a disk offering. This disk volume must still be attached to a virtual machine to make use of it."""
        return await self._execute_async(
            "createVolume",
            payload,
            envelope="createvolumeresponse",
        )

    def delete_volume(self, payload: DeleteVolumeRequest) -> APIResponse[Dict]:
        """Deletes a detached disk volume."""
        return self._execute(
            "deleteVolume",
            payload,
            envelope="deletevolumeresponse",
        )

    async def delete_volume_async(self, payload: DeleteVolumeRequest) -> APIResponse[Dict]:
        """Deletes a detached disk volume."""
        return await self._execute_async(
            "deleteVolume",
            payload,
            envelope="deletevolumeresponse",
        )

    def destroy_volume(self, payload: DestroyVolumeRequest) -> APIResponse[Dict]:
        """Destroys a detached disk volume."""
        return self._execute(
            "destroyVolume",
            payload,
            envelope="destroyvolumeresponse",
        )

    async def destroy_volume_async(self, payload: DestroyVolumeRequest) -> APIResponse[Dict]:
        """Destroys a detached disk volume."""
        return await self._execute_async(
            "destroyVolume",
            payload,
            envelope="destroyvolumeresponse",
        )

    def detach_volume(self, payload: DetachVolumeRequest) -> APIResponse[Dict]:
        """Detaches a volume from a virtual machine."""
        return self._execute(
            "detachVolume",
            payload,
            envelope="detachvolumeresponse",
        )

    async def detach_volume_async(self, payload: DetachVolumeRequest) -> APIResponse[Dict]:
        """Detaches a volume from a virtual machine."""
        return await self._execute_async(
            "detachVolume",
            payload,
            envelope="detachvolumeresponse",
        )

    def extract_volume(self, payload: ExtractVolumeRequest) -> APIResponse[Dict]:
        """Extracts a volume. Used for backup or migration purposes."""
        return self._execute(
            "extractVolume",
            payload,
            envelope="extractvolumeresponse",
        )

    async def extract_volume_async(self, payload: ExtractVolumeRequest) -> APIResponse[Dict]:
        """Extracts a volume. Used for backup or migration purposes."""
        return await self._execute_async(
            "extractVolume",
            payload,
            envelope="extractvolumeresponse",
        )

    def get_path_for_volume(self, payload: GetVolumeRequest) -> APIResponse[Dict]:
        """Gets the path of a volume."""
        return self._execute(
            "getPathForVolume",
            payload,
            envelope="getpathforvolumeresponse",
        )

    async def get_path_for_volume_async(self, payload: GetVolumeRequest) -> APIResponse[Dict]:
        """Asyncronously Gets the path of a volume."""
        return await self._execute_async(
            "getPathForVolume",
            payload,
            envelope="getpathforvolumeresponse",
        )

    def get_upload_params_for_volume(
        self, payload: GetUploadParamsForVolumeRequest
    ) -> APIResponse[Dict]:
        """Gets the upload parameters for a volume."""
        return self._execute(
            "getUploadParamsForVolume",
            payload,
            envelope="getuploadparamsforvolumeresponse",
        )

    async def get_upload_params_for_volume_async(
        self, payload: GetUploadParamsForVolumeRequest
    ) -> APIResponse[Dict]:
        """Asyncronously Gets the upload parameters for a volume."""
        return await self._execute_async(
            "getUploadParamsForVolume",
            payload,
            envelope="getuploadparamsforvolumeresponse",
        )

    def get_volume_iscsi_name(self, payload: GetVolumeIscsiNameRequest) -> APIResponse[Dict]:
        """Get Volume's iSCSI Name."""
        return self._execute(
            "getVolumeiScsiName",
            payload,
            envelope="getvolumeiscsinameresponse",
        )

    async def get_volume_iscsi_name_async(
        self, payload: GetVolumeIscsiNameRequest
    ) -> APIResponse[Dict]:
        """Asyncronously Get Volume's iSCSI Name."""
        return await self._execute_async(
            "getVolumeiScsiName",
            payload,
            envelope="getvolumeiscsinameresponse",
        )

    def import_volume(self, payload: ImportVolumeRequest) -> APIResponse[Dict]:
        """Import an unmanaged volume from a storage pool on a host into CloudStack."""
        return self._execute(
            "importVolume",
            payload,
            envelope="importvolumeresponse",
        )

    async def import_volume_async(self, payload: ImportVolumeRequest) -> APIResponse[Dict]:
        """Asyncronously Import an unmanaged volume from a storage pool on a host into CloudStack."""
        return await self._execute_async(
            "importVolume",
            payload,
            envelope="importvolumeresponse",
        )

    def list_elastistor_volumes(self, payload: ListElastistorVolumesRequest) -> APIResponse[Dict]:
        """Lists the volumes of elastistor."""
        return self._execute(
            "listElastistorVolume",
            payload,
            envelope="listelastistorvolumeresponse",
            entity="volume",
        )

    async def list_elastistor_volumes_async(
        self, payload: ListElastistorVolumesRequest
    ) -> APIResponse[Dict]:
        """Asyncronously Lists the volumes of elastistor."""
        return await self._execute_async(
            "listElastistorVolume",
            payload,
            envelope="listelastistorvolumeresponse",
            entity="volume",
        )

    def list(self, payload: ListVolumesRequest) -> APIResponse[Dict]:
        """Lists all volumes."""
        return self._execute(
            "listVolumes",
            payload,
            envelope="listvolumesresponse",
            entity="volume",
        )

    async def list_async(self, payload: ListVolumesRequest) -> APIResponse[Dict]:
        """Asyncronously Lists all volumes."""
        return await self._execute_async(
            "listVolumes",
            payload,
            envelope="listvolumesresponse",
            entity="volume",
        )

    def list_volumes_for_import(self, payload: ListVolumesForImportRequest) -> APIResponse[Dict]:
        """Lists unmanaged volumes on a storage pool."""
        return self._execute(
            "listVolumesForImport",
            payload,
            envelope="listvolumesforimportresponse",
            entity="volume",
        )

    async def list_volumes_for_import_async(
        self, payload: ListVolumesForImportRequest
    ) -> APIResponse[Dict]:
        """Asyncronously Lists unmanaged volumes on a storage pool."""
        return await self._execute_async(
            "listVolumesForImport",
            payload,
            envelope="listvolumesforimportresponse",
            entity="volume",
        )

    def list_volumes_usage_history(
        self, payload: ListVolumesUsageHistoryRequest
    ) -> APIResponse[Dict]:
        """Lists volume stats."""
        return self._execute(
            "listVolumesUsageHistory",
            payload,
            envelope="listvolumesusagehistoryresponse",
            entity="volumesusagehistory",
        )

    async def list_volumes_usage_history_async(
        self, payload: ListVolumesUsageHistoryRequest
    ) -> APIResponse[Dict]:
        """Asyncronously Lists volume stats."""
        return await self._execute_async(
            "listVolumesUsageHistory",
            payload,
            envelope="listvolumesusagehistoryresponse",
            entity="volumesusagehistory",
        )

    def migrate_volume(self, payload: MigrateVolumeRequest) -> APIResponse[Dict]:
        """Migrate a volume to a different storage pool."""
        return self._execute(
            "migrateVolume",
            payload,
            envelope="migratevolumeresponse",
        )

    async def migrate_volume_async(self, payload: MigrateVolumeRequest) -> APIResponse[Dict]:
        """Asyncronously Migrate a volume to a different storage pool."""
        return await self._execute_async(
            "migrateVolume",
            payload,
            envelope="migratevolumeresponse",
        )

    def recover_volume(self, payload: RecoverVolumeRequest) -> APIResponse[Dict]:
        """Recover a volume."""
        return self._execute(
            "recoverVolume",
            payload,
            envelope="recovervolumeresponse",
        )

    async def recover_volume_async(self, payload: RecoverVolumeRequest) -> APIResponse[Dict]:
        """Asyncronously Recover a volume."""
        return await self._execute_async(
            "recoverVolume",
            payload,
            envelope="recovervolumeresponse",
        )

    def resize_volume(self, payload: ResizeVolumeRequest) -> APIResponse[Dict]:
        """Resize a volume."""
        return self._execute(
            "resizeVolume",
            payload,
            envelope="resizevolumeresponse",
        )

    async def resize_volume_async(self, payload: ResizeVolumeRequest) -> APIResponse[Dict]:
        """Asyncronously Resize a volume."""
        return await self._execute_async(
            "resizeVolume",
            payload,
            envelope="resizevolumeresponse",
        )

    def resize_volume_from_backup_and_attach_to_vm(
        self, payload: ResizeVolumeFromBackupAndAttachToVMRequest
    ) -> APIResponse[Dict]:
        """Restore and attach a backed up volume to VM."""
        return self._execute(
            "restoreVolumeFromBackupAndAttachToVM",
            payload,
            envelope="resizevolumeresponse",
        )

    async def resize_volume_from_backup_and_attach_to_vm_async(
        self, payload: ResizeVolumeFromBackupAndAttachToVMRequest
    ) -> APIResponse[Dict]:
        """Asyncronously Restore and attach a backed up volume to VM."""
        return await self._execute_async(
            "restoreVolumeFromBackupAndAttachToVM",
            payload,
            envelope="resizevolumeresponse",
        )

    def unmanage_volume(self, payload: UnmanageVolumeRequest) -> APIResponse[Dict]:
        """Unmanage a volume on storage pool."""
        return self._execute(
            "unmanageVolume",
            payload,
            envelope="unmanagevolumeresponse",
        )

    async def unmanage_volume_async(self, payload: UnmanageVolumeRequest) -> APIResponse[Dict]:
        """Asyncronously Unmanage a volume on storage pool."""
        return await self._execute_async(
            "unmanageVolume",
            payload,
            envelope="unmanagevolumeresponse",
        )

    def update_volume(self, payload: UpdateVolumeRequest) -> APIResponse[Dict]:
        """Update a volume."""
        return self._execute(
            "updateVolume",
            payload,
            envelope="updatevolumeresponse",
        )

    async def update_volume_async(self, payload: UpdateVolumeRequest) -> APIResponse[Dict]:
        """Asyncronously Update a volume."""
        return await self._execute_async(
            "updateVolume",
            payload,
            envelope="updatevolumeresponse",
        )

    def upload_volume(self, payload: UploadVolumeRequest) -> APIResponse[Dict]:
        """Upload a volume."""
        return self._execute(
            "uploadVolume",
            payload,
            envelope="uploadvolumeresponse",
        )

    async def upload_volume_async(self, payload: UploadVolumeRequest) -> APIResponse[Dict]:
        """Asyncronously Upload a volume."""
        return await self._execute_async(
            "uploadVolume",
            payload,
            envelope="uploadvolumeresponse",
        )
