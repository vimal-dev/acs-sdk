# services/virtual_machine.py
from typing import Dict, List

from acs_sdk.schemas.request.virtual_machine import (
    AddNICToVirtualMachineRequest,
    AssignVirtualMachineRequest,
    AssignVirtualMachineToBackupOfferingRequest,
    CleanVMReservationsRequest,
    CreateVMScheduleRequest,
    DeleteVMScheduleRequest,
    DeployVirtualMachineRequest,
    DestroyVirtualMachineRequest,
    ExpungeVirtualMachineRequest,
    GetVMPasswordRequest,
    GetVMUserdataRequest,
    ImportUnmanagedInstanceRequest,
    ImportVmRequest,
    ListUnmanagedInstancesRequest,
    ListVirtualMachinesMetricsRequest,
    ListVirtualMachinesRequest,
    ListVirtualMachinesUsageHistoryRequest,
    ListVMScheduleRequest,
    ListVmsForImportRequest,
    MigrateVirtualMachineRequest,
    MigrateVirtualMachineWithVolumeRequest,
    RebootVirtualMachineRequest,
    RecoverVirtualMachineRequest,
    RemoveNICFromVirtualMachineRequest,
    RemoveVirtualMachineFromBackupOfferingRequest,
    ResetPasswordForVirtualMachineRequest,
    ResetSSHKeyForVirtualMachineRequest,
    ResetUserDataForVirtualMachineRequest,
    RestoreVirtualMachineRequest,
    RevertToVMSnapshotRequest,
    ScaleVirtualMachineRequest,
    StartVirtualMachineRequest,
    StopVirtualMachineRequest,
    UnmanageVirtualMachineRequest,
    UpdateDefaultNICForVirtualMachineRequest,
    UpdateVirtualMachineRequest,
    UpdateVMScheduleRequest,
)

from .base import BaseService
from ..schemas.response.base import APIResponse


class VirtualMachine(BaseService):

    # -------------------------------------------------------------------------
    # List / query
    # -------------------------------------------------------------------------

    def list(self, payload: ListVirtualMachinesRequest) -> APIResponse[List[Dict]]:
        """List virtual machines."""
        return self._execute(
            "listVirtualMachines",
            payload,
            envelope="listvirtualmachinesresponse",
            entity="virtualmachine",
        )

    async def list_async(self, payload: ListVirtualMachinesRequest) -> APIResponse[List[Dict]]:
        """Asynchronously list virtual machines."""
        return await self._execute_async(
            "listVirtualMachines",
            payload,
            envelope="listvirtualmachinesresponse",
            entity="virtualmachine",
        )

    def list_metrics(self, payload: ListVirtualMachinesMetricsRequest) -> APIResponse[List[Dict]]:
        """List virtual machines with metrics data."""
        return self._execute(
            "listVirtualMachinesMetrics",
            payload,
            envelope="listvirtualmachinesmetricsresponse",
            entity="virtualmachine",
        )

    async def list_metrics_async(
        self, payload: ListVirtualMachinesMetricsRequest
    ) -> APIResponse[List[Dict]]:
        """Asynchronously list virtual machines with metrics data."""
        return await self._execute_async(
            "listVirtualMachinesMetrics",
            payload,
            envelope="listvirtualmachinesmetricsresponse",
            entity="virtualmachine",
        )

    def list_usage_history(
        self, payload: ListVirtualMachinesUsageHistoryRequest
    ) -> APIResponse[List[Dict]]:
        """List virtual machines usage history."""
        return self._execute(
            "listVirtualMachinesUsageHistory",
            payload,
            envelope="listvirtualmachinesusagehistoryresponse",
            entity="virtualmachine",
        )

    async def list_usage_history_async(
        self, payload: ListVirtualMachinesUsageHistoryRequest
    ) -> APIResponse[List[Dict]]:
        """Asynchronously list virtual machines usage history."""
        return await self._execute_async(
            "listVirtualMachinesUsageHistory",
            payload,
            envelope="listvirtualmachinesusagehistoryresponse",
            entity="virtualmachine",
        )

    def list_unmanaged_instances(
        self, payload: ListUnmanagedInstancesRequest
    ) -> APIResponse[List[Dict]]:
        """List unmanaged instances in a cluster."""
        return self._execute(
            "listUnmanagedInstances",
            payload,
            envelope="listunmanagedinstancesresponse",
            entity="unmanagedinstance",
        )

    async def list_unmanaged_instances_async(
        self, payload: ListUnmanagedInstancesRequest
    ) -> APIResponse[List[Dict]]:
        """Asynchronously list unmanaged instances in a cluster."""
        return await self._execute_async(
            "listUnmanagedInstances",
            payload,
            envelope="listunmanagedinstancesresponse",
            entity="unmanagedinstance",
        )

    def list_vms_for_import(self, payload: ListVmsForImportRequest) -> APIResponse[List[Dict]]:
        """List VMs available for import from an external host."""
        return self._execute(
            "listVmsForImport",
            payload,
            envelope="listvmsforimportresponse",
            entity="virtualmachine",
        )

    async def list_vms_for_import_async(
        self, payload: ListVmsForImportRequest
    ) -> APIResponse[List[Dict]]:
        """Asynchronously list VMs available for import from an external host."""
        return await self._execute_async(
            "listVmsForImport",
            payload,
            envelope="listvmsforimportresponse",
            entity="virtualmachine",
        )

    # -------------------------------------------------------------------------
    # Schedule
    # -------------------------------------------------------------------------

    def list_vm_schedule(self, payload: ListVMScheduleRequest) -> APIResponse[List[Dict]]:
        """List VM schedules."""
        return self._execute(
            "listVMSchedule",
            payload,
            envelope="listvmscheduleresponse",
            entity="vmschedule",
        )

    async def list_vm_schedule_async(
        self, payload: ListVMScheduleRequest
    ) -> APIResponse[List[Dict]]:
        """Asynchronously list VM schedules."""
        return await self._execute_async(
            "listVMSchedule",
            payload,
            envelope="listvmscheduleresponse",
            entity="vmschedule",
        )

    def create_vm_schedule(self, payload: CreateVMScheduleRequest) -> APIResponse[Dict]:
        """Create a VM schedule."""
        return self._execute(
            "createVMSchedule",
            payload,
            envelope="createvmscheduleresponse",
        )

    async def create_vm_schedule_async(
        self, payload: CreateVMScheduleRequest
    ) -> APIResponse[Dict]:
        """Asynchronously create a VM schedule."""
        return await self._execute_async(
            "createVMSchedule",
            payload,
            envelope="createvmscheduleresponse",
        )

    def update_vm_schedule(self, payload: UpdateVMScheduleRequest) -> APIResponse[Dict]:
        """Update a VM schedule."""
        return self._execute(
            "updateVMSchedule",
            payload,
            envelope="updatevmscheduleresponse",
        )

    async def update_vm_schedule_async(
        self, payload: UpdateVMScheduleRequest
    ) -> APIResponse[Dict]:
        """Asynchronously update a VM schedule."""
        return await self._execute_async(
            "updateVMSchedule",
            payload,
            envelope="updatevmscheduleresponse",
        )

    def delete_vm_schedule(self, payload: DeleteVMScheduleRequest) -> APIResponse[Dict]:
        """Delete a VM schedule."""
        return self._execute(
            "deleteVMSchedule",
            payload,
            envelope="deletevmscheduleresponse",
        )

    async def delete_vm_schedule_async(
        self, payload: DeleteVMScheduleRequest
    ) -> APIResponse[Dict]:
        """Asynchronously delete a VM schedule."""
        return await self._execute_async(
            "deleteVMSchedule",
            payload,
            envelope="deletevmscheduleresponse",
        )

    # -------------------------------------------------------------------------
    # Lifecycle
    # -------------------------------------------------------------------------

    def deploy_vm(self, payload: DeployVirtualMachineRequest) -> APIResponse[Dict]:
        """Deploy a virtual machine."""
        return self._execute(
            "deployVirtualMachine",
            payload,
            envelope="deployvirtualmachineresponse",
        )

    async def deploy_vm_async(self, payload: DeployVirtualMachineRequest) -> APIResponse[Dict]:
        """Asynchronously deploy a virtual machine."""
        return await self._execute_async(
            "deployVirtualMachine",
            payload,
            envelope="deployvirtualmachineresponse",
        )

    def start_vm(self, payload: StartVirtualMachineRequest) -> APIResponse[Dict]:
        """Start a virtual machine."""
        return self._execute(
            "startVirtualMachine",
            payload,
            envelope="startvirtualmachineresponse",
        )

    async def start_vm_async(self, payload: StartVirtualMachineRequest) -> APIResponse[Dict]:
        """Asynchronously start a virtual machine."""
        return await self._execute_async(
            "startVirtualMachine",
            payload,
            envelope="startvirtualmachineresponse",
        )

    def stop_vm(self, payload: StopVirtualMachineRequest) -> APIResponse[Dict]:
        """Stop a virtual machine."""
        return self._execute(
            "stopVirtualMachine",
            payload,
            envelope="stopvirtualmachineresponse",
        )

    async def stop_vm_async(self, payload: StopVirtualMachineRequest) -> APIResponse[Dict]:
        """Asynchronously stop a virtual machine."""
        return await self._execute_async(
            "stopVirtualMachine",
            payload,
            envelope="stopvirtualmachineresponse",
        )

    def reboot_vm(self, payload: RebootVirtualMachineRequest) -> APIResponse[Dict]:
        """Reboot a virtual machine."""
        return self._execute(
            "rebootVirtualMachine",
            payload,
            envelope="rebootvirtualmachineresponse",
        )

    async def reboot_vm_async(self, payload: RebootVirtualMachineRequest) -> APIResponse[Dict]:
        """Asynchronously reboot a virtual machine."""
        return await self._execute_async(  # FIX: was self._execute
            "rebootVirtualMachine",
            payload,
            envelope="rebootvirtualmachineresponse",
        )

    def destroy_vm(self, payload: DestroyVirtualMachineRequest) -> APIResponse[Dict]:
        """Destroy a virtual machine."""
        return self._execute(
            "destroyVirtualMachine",
            payload,
            envelope="destroyvirtualmachineresponse",
        )

    async def destroy_vm_async(self, payload: DestroyVirtualMachineRequest) -> APIResponse[Dict]:
        """Asynchronously destroy a virtual machine."""
        return await self._execute_async(
            "destroyVirtualMachine",
            payload,
            envelope="destroyvirtualmachineresponse",
        )

    def recover_vm(self, payload: RecoverVirtualMachineRequest) -> APIResponse[Dict]:
        """Recover a destroyed virtual machine."""
        return self._execute(
            "recoverVirtualMachine",
            payload,
            envelope="recovervirtualmachineresponse",
        )

    async def recover_vm_async(self, payload: RecoverVirtualMachineRequest) -> APIResponse[Dict]:
        """Asynchronously recover a destroyed virtual machine."""
        return await self._execute_async(  # FIX: was self._execute
            "recoverVirtualMachine",
            payload,
            envelope="recovervirtualmachineresponse",
        )

    def expunge_vm(self, payload: ExpungeVirtualMachineRequest) -> APIResponse[Dict]:
        """Expunge a virtual machine."""
        return self._execute(
            "expungeVirtualMachine",
            payload,
            envelope="expungevirtualmachineresponse",
        )

    async def expunge_vm_async(
        self, payload: ExpungeVirtualMachineRequest
    ) -> APIResponse[Dict]:
        """Asynchronously expunge a virtual machine."""
        return await self._execute_async(
            "expungeVirtualMachine",
            payload,
            envelope="expungevirtualmachineresponse",
        )

    def restore_vm(self, payload: RestoreVirtualMachineRequest) -> APIResponse[Dict]:
        """Restore a VM to original template/ISO or new template/ISO."""
        return self._execute(
            "restoreVirtualMachine",
            payload,
            envelope="restorevirtualmachineresponse",
        )

    async def restore_vm_async(self, payload: RestoreVirtualMachineRequest) -> APIResponse[Dict]:
        """Asynchronously restore a VM to original or new template/ISO."""
        return await self._execute_async(
            "restoreVirtualMachine",
            payload,
            envelope="restorevirtualmachineresponse",
        )

    def scale_vm(self, payload: ScaleVirtualMachineRequest) -> APIResponse[Dict]:
        """Scale a virtual machine to a new service offering."""
        return self._execute(
            "scaleVirtualMachine",
            payload,
            envelope="scalevirtualmachineresponse",
        )

    async def scale_vm_async(self, payload: ScaleVirtualMachineRequest) -> APIResponse[Dict]:
        """Asynchronously scale a virtual machine to a new service offering."""
        return await self._execute_async(
            "scaleVirtualMachine",
            payload,
            envelope="scalevirtualmachineresponse",
        )

    def migrate_vm(self, payload: MigrateVirtualMachineRequest) -> APIResponse[Dict]:
        """Migrate a virtual machine to a different host or storage pool."""
        return self._execute(
            "migrateVirtualMachine",
            payload,
            envelope="migratevirtualmachineresponse",
        )

    async def migrate_vm_async(
        self, payload: MigrateVirtualMachineRequest
    ) -> APIResponse[Dict]:
        """Asynchronously migrate a virtual machine."""
        return await self._execute_async(
            "migrateVirtualMachine",
            payload,
            envelope="migratevirtualmachineresponse",
        )

    def migrate_vm_with_volume(
        self, payload: MigrateVirtualMachineWithVolumeRequest
    ) -> APIResponse[Dict]:
        """Migrate a virtual machine with explicit volume-to-pool mappings."""
        return self._execute(
            "migrateVirtualMachineWithVolume",
            payload,
            envelope="migratevirtualmachinewithvolumeresponse",
        )

    async def migrate_vm_with_volume_async(
        self, payload: MigrateVirtualMachineWithVolumeRequest
    ) -> APIResponse[Dict]:
        """Asynchronously migrate a virtual machine with explicit volume-to-pool mappings."""
        return await self._execute_async(
            "migrateVirtualMachineWithVolume",
            payload,
            envelope="migratevirtualmachinewithvolumeresponse",
        )

    def unmanage_vm(self, payload: UnmanageVirtualMachineRequest) -> APIResponse[Dict]:
        """Unmanage a virtual machine from CloudStack."""
        return self._execute(
            "unmanageVirtualMachine",
            payload,
            envelope="unmanagervirtualmachineresponse",
        )

    async def unmanage_vm_async(
        self, payload: UnmanageVirtualMachineRequest
    ) -> APIResponse[Dict]:
        """Asynchronously unmanage a virtual machine from CloudStack."""
        return await self._execute_async(
            "unmanageVirtualMachine",
            payload,
            envelope="unmanagervirtualmachineresponse",
        )

    # -------------------------------------------------------------------------
    # Import
    # -------------------------------------------------------------------------

    def import_unmanaged_instance(
        self, payload: ImportUnmanagedInstanceRequest
    ) -> APIResponse[Dict]:
        """Import an unmanaged instance into CloudStack management."""
        return self._execute(
            "importUnmanagedInstance",
            payload,
            envelope="importunmanagedinstanceresponse",
        )

    async def import_unmanaged_instance_async(
        self, payload: ImportUnmanagedInstanceRequest
    ) -> APIResponse[Dict]:
        """Asynchronously import an unmanaged instance into CloudStack management."""
        return await self._execute_async(
            "importUnmanagedInstance",
            payload,
            envelope="importunmanagedinstanceresponse",
        )

    def import_vm(self, payload: ImportVmRequest) -> APIResponse[Dict]:
        """Import a VM from an external source."""
        return self._execute(
            "importVm",
            payload,
            envelope="importvmresponse",
        )

    async def import_vm_async(self, payload: ImportVmRequest) -> APIResponse[Dict]:
        """Asynchronously import a VM from an external source."""
        return await self._execute_async(
            "importVm",
            payload,
            envelope="importvmresponse",
        )

    # -------------------------------------------------------------------------
    # Ownership / assignment
    # -------------------------------------------------------------------------

    def assign_virtual_machine(
        self, payload: AssignVirtualMachineRequest
    ) -> APIResponse[Dict]:
        """Change ownership of a VM from one account to another."""
        return self._execute(
            "assignVirtualMachine",
            payload,
            envelope="assignvirtualmachineresponse",
        )

    async def assign_virtual_machine_async(
        self, payload: AssignVirtualMachineRequest
    ) -> APIResponse[Dict]:
        """Asynchronously change ownership of a VM."""
        return await self._execute_async(
            "assignVirtualMachine",
            payload,
            envelope="assignvirtualmachineresponse",
        )

    def assign_virtual_machine_to_backup_offering(
        self, payload: AssignVirtualMachineToBackupOfferingRequest
    ) -> APIResponse[Dict]:
        """Assign a virtual machine to a backup offering."""
        return self._execute(
            "assignVirtualMachineToBackupOffering",
            payload,
            envelope="assignvirtualmachinetobackupofferingresponse",
        )

    async def assign_virtual_machine_to_backup_offering_async(
        self, payload: AssignVirtualMachineToBackupOfferingRequest
    ) -> APIResponse[Dict]:
        """Asynchronously assign a virtual machine to a backup offering."""
        return await self._execute_async(
            "assignVirtualMachineToBackupOffering",
            payload,
            envelope="assignvirtualmachinetobackupofferingresponse",
        )

    def remove_virtual_machine_from_backup_offering(
        self, payload: RemoveVirtualMachineFromBackupOfferingRequest
    ) -> APIResponse[Dict]:
        """Remove a VM from any existing backup offering."""
        return self._execute(
            "removeVirtualMachineFromBackupOffering",
            payload,
            envelope="removevirtualmachinefrombackupofferingresponse",
        )

    async def remove_virtual_machine_from_backup_offering_async(
        self, payload: RemoveVirtualMachineFromBackupOfferingRequest
    ) -> APIResponse[Dict]:
        """Asynchronously remove a VM from any existing backup offering."""
        return await self._execute_async(
            "removeVirtualMachineFromBackupOffering",
            payload,
            envelope="removevirtualmachinefrombackupofferingresponse",
        )

    # -------------------------------------------------------------------------
    # NIC management
    # -------------------------------------------------------------------------

    def add_nic_to_virtual_machine(
        self, payload: AddNICToVirtualMachineRequest
    ) -> APIResponse[Dict]:
        """Add a NIC to a virtual machine."""
        return self._execute(
            "addNicToVirtualMachine",
            payload,
            envelope="addnictovirtualmachineresponse",
        )

    async def add_nic_to_virtual_machine_async(
        self, payload: AddNICToVirtualMachineRequest
    ) -> APIResponse[Dict]:
        """Asynchronously add a NIC to a virtual machine."""
        return await self._execute_async(
            "addNicToVirtualMachine",
            payload,
            envelope="addnictovirtualmachineresponse",
        )

    def remove_nic_from_virtual_machine(
        self, payload: RemoveNICFromVirtualMachineRequest
    ) -> APIResponse[Dict]:
        """Remove VM from a specified network by deleting a NIC."""
        return self._execute(
            "removeNicFromVirtualMachine",
            payload,
            envelope="removenicfromvirtualmachineresponse",
        )

    async def remove_nic_from_virtual_machine_async(
        self, payload: RemoveNICFromVirtualMachineRequest
    ) -> APIResponse[Dict]:
        """Asynchronously remove a NIC from a virtual machine."""
        return await self._execute_async(
            "removeNicFromVirtualMachine",
            payload,
            envelope="removenicfromvirtualmachineresponse",
        )

    def update_default_nic_for_vm(
        self, payload: UpdateDefaultNICForVirtualMachineRequest
    ) -> APIResponse[Dict]:
        """Change the default NIC on a VM."""
        return self._execute(
            "updateDefaultNicForVirtualMachine",
            payload,
            envelope="updatedefaultnicforvirtualmachineresponse",
        )

    async def update_default_nic_for_vm_async(
        self, payload: UpdateDefaultNICForVirtualMachineRequest
    ) -> APIResponse[Dict]:
        """Asynchronously change the default NIC on a VM."""
        return await self._execute_async(
            "updateDefaultNicForVirtualMachine",
            payload,
            envelope="updatedefaultnicforvirtualmachineresponse",
        )

    # -------------------------------------------------------------------------
    # Password / SSH / userdata
    # -------------------------------------------------------------------------

    def get_vm_password(self, payload: GetVMPasswordRequest) -> APIResponse[Dict]:
        """Return the base64 encoded encrypted password for the VM."""
        return self._execute(
            "getVMPassword",
            payload,
            envelope="getvmpasswordresponse",
        )

    async def get_vm_password_async(self, payload: GetVMPasswordRequest) -> APIResponse[Dict]:
        """Asynchronously return the base64 encoded encrypted password for the VM."""
        return await self._execute_async(
            "getVMPassword",
            payload,
            envelope="getvmpasswordresponse",
        )

    def get_vm_userdata(self, payload: GetVMUserdataRequest) -> APIResponse[Dict]:
        """Return the userdata for the VM."""
        return self._execute(
            "getVirtualMachineUserData",  # FIX: was "getVMUserData"
            payload,
            envelope="getvirtualmachineuserdata response",
        )

    async def get_vm_userdata_async(self, payload: GetVMUserdataRequest) -> APIResponse[Dict]:
        """Asynchronously return the userdata for the VM."""
        return await self._execute_async(
            "getVirtualMachineUserData",  # FIX: was "getVMUserData"
            payload,
            envelope="getvirtualmachineuserdata response",
        )

    def reset_password_for_vm(
        self, payload: ResetPasswordForVirtualMachineRequest  # FIX: was wrong type
    ) -> APIResponse[Dict]:
        """Reset the password for a virtual machine."""
        return self._execute(
            "resetPasswordForVirtualMachine",
            payload,
            envelope="resetpasswordforvirtualmachineresponse",
        )

    async def reset_password_for_vm_async(
        self, payload: ResetPasswordForVirtualMachineRequest  # FIX: was wrong type
    ) -> APIResponse[Dict]:
        """Asynchronously reset the password for a virtual machine."""
        return await self._execute_async(
            "resetPasswordForVirtualMachine",
            payload,
            envelope="resetpasswordforvirtualmachineresponse",
        )

    def reset_sshkey_for_vm(
        self, payload: ResetSSHKeyForVirtualMachineRequest
    ) -> APIResponse[Dict]:
        """Reset the SSH key for a virtual machine."""
        return self._execute(
            "resetSSHKeyForVirtualMachine",
            payload,
            envelope="resetsshkeyforvirtualmachineresponse",
        )

    async def reset_sshkey_for_vm_async(
        self, payload: ResetSSHKeyForVirtualMachineRequest
    ) -> APIResponse[Dict]:
        """Asynchronously reset the SSH key for a virtual machine."""
        return await self._execute_async(
            "resetSSHKeyForVirtualMachine",
            payload,
            envelope="resetsshkeyforvirtualmachineresponse",
        )

    def reset_userdata_for_vm(
        self, payload: ResetUserDataForVirtualMachineRequest
    ) -> APIResponse[Dict]:
        """Reset the userdata for a virtual machine."""
        return self._execute(
            "resetUserDataForVirtualMachine",
            payload,
            envelope="resetuserdataforvirtualmachineresponse",
        )

    async def reset_userdata_for_vm_async(
        self, payload: ResetUserDataForVirtualMachineRequest
    ) -> APIResponse[Dict]:
        """Asynchronously reset the userdata for a virtual machine."""
        return await self._execute_async(
            "resetUserDataForVirtualMachine",
            payload,
            envelope="resetuserdataforvirtualmachineresponse",
        )

    # -------------------------------------------------------------------------
    # Snapshot
    # -------------------------------------------------------------------------

    def revert_to_vm_snapshot(
        self, payload: RevertToVMSnapshotRequest  # FIX: renamed from revert_to_vm_sanpshot
    ) -> APIResponse[Dict]:
        """Revert a VM to a VM snapshot."""
        return self._execute(
            "revertToVMSnapshot",
            payload,
            envelope="reverttovmsnapshotresponse",
        )

    async def revert_to_vm_snapshot_async(
        self, payload: RevertToVMSnapshotRequest  # FIX: renamed from revert_to_vm_sanpshot_async
    ) -> APIResponse[Dict]:
        """Asynchronously revert a VM to a VM snapshot."""
        return await self._execute_async(
            "revertToVMSnapshot",
            payload,
            envelope="reverttovmsnapshotresponse",
        )

    # -------------------------------------------------------------------------
    # Update / misc
    # -------------------------------------------------------------------------

    def update_vm(self, payload: UpdateVirtualMachineRequest) -> APIResponse[Dict]:
        """Update properties of a virtual machine."""
        return self._execute(
            "updateVirtualMachine",
            payload,
            envelope="updatevirtualmachineresponse",
        )

    async def update_vm_async(self, payload: UpdateVirtualMachineRequest) -> APIResponse[Dict]:
        """Asynchronously update properties of a virtual machine."""
        return await self._execute_async(
            "updateVirtualMachine",
            payload,
            envelope="updatevirtualmachineresponse",
        )

    def clean_vm_reservations(self, payload: CleanVMReservationsRequest) -> APIResponse[Dict]:
        """Clean up VM reservations in the database."""
        return self._execute(
            "cleanVMReservations",
            payload,
            envelope="cleanvmreservationresponse",
        )

    async def clean_vm_reservations_async(
        self, payload: CleanVMReservationsRequest
    ) -> APIResponse[Dict]:
        """Asynchronously clean up VM reservations in the database."""
        return await self._execute_async(
            "cleanVMReservations",
            payload,
            envelope="cleanvmreservationresponse",
        )
