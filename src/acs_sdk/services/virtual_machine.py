# services/virtual_machine.py
from typing import Dict, List

from acs_sdk.schemas.request.virtual_machine import (
    AddNICToVirtualMachineRequest,
    AssignVirtualMachineRequest,
    AssignVirtualMachineToBackupOfferingRequest,
    CreateVMScheduleRequest,
    DeleteVMScheduleRequest,
    DeployVirtualMachineRequest,
    DestroyVirtualMachineRequest,
    ListVMScheduleRequest,
    ListVirtualMachinesRequest,
    RebootVirtualMachineRequest,
    RecoverVirtualMachineRequest,
    RemoveNICFromVirtualMachineRequest,
    RemoveVirtualMachineFromBackupOfferingRequest,
    ResetSSHKeyForVirtualMachineRequest,
    ResetUserDataForVirtualMachineRequest,
    RestoreVirtualMachineRequest,
    RevertTOVMSanpshotRequest,
    ScaleVirtualMachineRequest,
    StartVirtualMachineRequest,
    StopVirtualMachineRequest,
    UpdateDefaultNICForVirtualMachineRequest,
    UpdateVMScheduleRequest,
    CleanVMReservationsRequest,
    ExpungeVirtualMachineRequest,
    GetVMPasswordRequest,
    GetVMUserdataRequest,
    UpdateVirtualMachineRequest,
)

from .base import BaseService
from ..schemas.response.base import APIResponse


class VirtualMachine(BaseService):
    def list(self, payload: ListVirtualMachinesRequest) -> APIResponse[List[Dict]]:
        """List all available virtual machines."""
        return self._execute(
            "listVirtualMachines",
            payload,
            envelope="listvirtualmachinesresponse",
            entity="virtualmachine",
        )

    async def list_async(self, payload: ListVirtualMachinesRequest) -> APIResponse[List[Dict]]:
        """Asynchronously list all available virtual machines."""
        return await self._execute_async(
            "listVirtualMachines",
            payload,
            envelope="listvirtualmachinesresponse",
            entity="virtualmachine",
        )

    def list_vm_schedule(self, payload: ListVMScheduleRequest) -> APIResponse[List[Dict]]:
        """List all available virtual machines."""
        return self._execute(
            "listVMSchedule",
            payload,
            envelope="listvmscheduleresponse",
            entity="vmschedule",
        )

    async def list_vm_schedule_async(
        self, payload: ListVMScheduleRequest
    ) -> APIResponse[List[Dict]]:
        """Asynchronously list all available virtual machines."""
        return await self._execute_async(
            "listVMSchedule",
            payload,
            envelope="listvmscheduleresponse",
            entity="vmschedule",
        )

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

    def assign_virtual_machine(self, payload: AssignVirtualMachineRequest) -> APIResponse[Dict]:
        """Change ownership of a VM from one account to another."""
        return self._execute(
            "assignVirtualMachine",
            payload,
            envelope="assignvirtualmachineresponse",
        )

    async def assign_virtual_machine_async(
        self, payload: AssignVirtualMachineRequest
    ) -> APIResponse[Dict]:
        """Asynchronously Change ownership of a VM from one account to another."""
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

    def clean_vm_reservations(self, payload: CleanVMReservationsRequest) -> APIResponse[Dict]:
        """Cleanups VM reservations in the database."""
        return self._execute(
            "cleanVMReservations",
            payload,
            envelope="cleanvmreservationresponse",
        )

    async def clean_vm_reservations_async(
        self, payload: CleanVMReservationsRequest
    ) -> APIResponse[Dict]:
        """Cleanups VM reservations in the database."""
        return await self._execute_async(
            "cleanVMReservations",
            payload,
            envelope="cleanvmreservationresponse",
        )

    def create_vm_schedule(self, payload: CreateVMScheduleRequest) -> APIResponse[Dict]:
        """Creates a VM schedule."""
        return self._execute(
            "createVMSchedule",
            payload,
            envelope="createvmscheduleresponse",
        )

    async def create_vm_schedule_async(self, payload: CreateVMScheduleRequest) -> APIResponse[Dict]:
        """Asynchronously creates a VM schedule."""
        return await self._execute_async(
            "createVMSchedule",
            payload,
            envelope="createvmscheduleresponse",
        )

    def update_vm_schedule(self, payload: UpdateVMScheduleRequest) -> APIResponse[Dict]:
        """Updates a VM schedule."""
        return self._execute(
            "updateVMSchedule",
            payload,
            envelope="updatevmscheduleresponse",
        )

    async def update_vm_schedule_async(self, payload: UpdateVMScheduleRequest) -> APIResponse[Dict]:
        """Asynchronously updates a VM schedule."""
        return await self._execute_async(
            "updateVMSchedule",
            payload,
            envelope="updatevmscheduleresponse",
        )

    def delete_vm_schedule(self, payload: DeleteVMScheduleRequest) -> APIResponse[Dict]:
        """Deletes a VM schedule."""
        return self._execute(
            "deleteVMSchedule",
            payload,
            envelope="deletevmscheduleresponse",
        )

    async def delete_vm_schedule_async(self, payload: DeleteVMScheduleRequest) -> APIResponse[Dict]:
        """Asynchronously deletes a VM schedule."""
        return await self._execute_async(
            "deleteVMSchedule",
            payload,
            envelope="deletevmscheduleresponse",
        )

    def deploy_vm(self, payload: DeployVirtualMachineRequest) -> APIResponse[Dict]:
        """Creates and automatically starts a virtual machine based on a service offering, disk offering, and template."""
        return self._execute(
            "deployVirtualMachine",
            payload,
            envelope="deployvirtualmachineresponse",
        )

    async def deploy_vm_async(self, payload: DeployVirtualMachineRequest) -> APIResponse[Dict]:
        """Asynchronously Creates and automatically starts a virtual machine based on a service offering, disk offering, and template."""
        return await self._execute_async(
            "deployVirtualMachine",
            payload,
            envelope="deployvirtualmachineresponse",
        )

    def destroy_vm(self, payload: DestroyVirtualMachineRequest) -> APIResponse[Dict]:
        """Destroys a virtual machine. Once destroyed, only the administrator can recover it."""
        return self._execute(
            "destroyVirtualMachine",
            payload,
            envelope="destroyvirtualmachineresponse",
        )

    async def destroy_vm_async(self, payload: DestroyVirtualMachineRequest) -> APIResponse[Dict]:
        """Asynchronously destroys a virtual machine. Once destroyed, only the administrator can recover it."""
        return await self._execute_async(
            "destroyVirtualMachine",
            payload,
            envelope="destroyvirtualmachineresponse",
        )

    def expunge_vm(self, payload: ExpungeVirtualMachineRequest) -> APIResponse[Dict]:
        """Expunge a virtual machine. Once expunged, it cannot be recovered."""
        return self._execute(
            "expungeVirtualMachine",
            payload,
            envelope="expungevirtualmachineresponse",
        )

    async def expunge_vm_async(self, payload: ExpungeVirtualMachineRequest) -> APIResponse[Dict]:
        """Asynchronously expunges a virtual machine. Once expunged, it cannot be recovered."""
        return await self._execute_async(
            "expungeVirtualMachine",
            payload,
            envelope="expungevirtualmachineresponse",
        )

    def get_vm_password(self, payload: GetVMPasswordRequest) -> APIResponse[Dict]:
        """Returns the base64 encoded encrypted password for the VM."""
        return self._execute(
            "getVMPassword",
            payload,
            envelope="getvmpasswordresponse",
        )

    async def get_vm_password_async(self, payload: GetVMPasswordRequest) -> APIResponse[Dict]:
        """Asynchronously returns the base64 encoded encrypted password for the VM."""
        return await self._execute_async(
            "getVMPassword",
            payload,
            envelope="getvmpasswordresponse",
        )

    def get_vm_userdata(self, payload: GetVMUserdataRequest) -> APIResponse[Dict]:
        """Returns the base64 encoded encrypted userdata for the VM."""
        return self._execute(
            "getVMUserData",
            payload,
            envelope="getvmuserdataresponse",
        )

    async def get_vm_userdata_async(self, payload: GetVMUserdataRequest) -> APIResponse[Dict]:
        """Asynchronously returns the base64 encoded encrypted userdata for the VM."""
        return await self._execute_async(
            "getVMUserData",
            payload,
            envelope="getvmuserdataresponse",
        )

    def reboot_vm(self, payload: RebootVirtualMachineRequest) -> APIResponse[Dict]:
        """Reboots a virtual machine."""
        return self._execute(
            "rebootVirtualMachine",
            payload,
            envelope="rebootvirtualmachineresponse",
        )

    async def reboot_vm_async(self, payload: RebootVirtualMachineRequest) -> APIResponse[Dict]:
        """Asynchronously Reboots a virtual machine."""
        return self._execute(
            "rebootVirtualMachine",
            payload,
            envelope="rebootvirtualmachineresponse",
        )

    def recover_vm(self, payload: RecoverVirtualMachineRequest) -> APIResponse[Dict]:
        """Recovers a virtual machine."""
        return self._execute(
            "recoverVirtualMachine",
            payload,
            envelope="recovervirtualmachineresponse",
        )

    async def recover_vm_async(self, payload: RecoverVirtualMachineRequest) -> APIResponse[Dict]:
        """Asynchronously Recovers a virtual machine."""
        return self._execute(
            "recoverVirtualMachine",
            payload,
            envelope="recovervirtualmachineresponse",
        )

    def remove_nic_from_virtual_machine(
        self, payload: RemoveNICFromVirtualMachineRequest
    ) -> APIResponse[Dict]:
        """Removes VM from specified network by deleting a NIC."""
        return self._execute(
            "removeNicFromVirtualMachine",
            payload,
            envelope="removenicfromvirtualmachineresponse",
        )

    async def remove_nic_from_virtual_machine_async(
        self, payload: RemoveNICFromVirtualMachineRequest
    ) -> APIResponse[Dict]:
        """Asynchronously Removes VM from specified network by deleting a NIC."""
        return await self._execute_async(
            "removeNicFromVirtualMachine",
            payload,
            envelope="removenicfromvirtualmachineresponse",
        )

    def remove_virtual_machine_from_backup_offering(
        self, payload: RemoveVirtualMachineFromBackupOfferingRequest
    ) -> APIResponse[Dict]:
        """Removes a VM from any existing backup offering."""
        return self._execute(
            "removeVirtualMachineFromBackupOffering",
            payload,
            envelope="removevirtualmachinefrombackupofferingresponse",
        )

    async def remove_virtual_machine_from_backup_offering_async(
        self, payload: RemoveVirtualMachineFromBackupOfferingRequest
    ) -> APIResponse[Dict]:
        """Asynchronously Removes a VM from any existing backup offering."""
        return await self._execute_async(
            "removeVirtualMachineFromBackupOffering",
            payload,
            envelope="removevirtualmachinefrombackupofferingresponse",
        )

    def reset_password_for_vm(
        self, payload: RemoveVirtualMachineFromBackupOfferingRequest
    ) -> APIResponse[Dict]:
        """Resets the password for virtual machine. The virtual machine must be in a "Stopped" state and the template must already support this feature for this command to take effect."""
        return self._execute(
            "resetPasswordForVirtualMachine",
            payload,
            envelope="resetpasswordforvirtualmachineresponse",
        )

    async def reset_password_for_vm_async(
        self, payload: RemoveVirtualMachineFromBackupOfferingRequest
    ) -> APIResponse[Dict]:
        """Asynchronously Resets the password for virtual machine. The virtual machine must be in a "Stopped" state and the template must already support this feature for this command to take effect."""
        return await self._execute_async(
            "resetPasswordForVirtualMachine",
            payload,
            envelope="resetpasswordforvirtualmachineresponse",
        )

    def reset_sshkey_for_vm(
        self, payload: ResetSSHKeyForVirtualMachineRequest
    ) -> APIResponse[Dict]:
        """Resets the SSH Key for virtual machine. The virtual machine must be in a "Stopped" state."""
        return self._execute(
            "resetSSHKeyForVirtualMachine",
            payload,
            envelope="resetsshkeyforvirtualmachineresponse",
        )

    async def reset_sshkey_for_vm_async(
        self, payload: ResetSSHKeyForVirtualMachineRequest
    ) -> APIResponse[Dict]:
        """Asynchronously Resets the SSH Key for virtual machine. The virtual machine must be in a "Stopped" state."""
        return await self._execute_async(
            "resetSSHKeyForVirtualMachine",
            payload,
            envelope="resetsshkeyforvirtualmachineresponse",
        )

    def reset_userdata_for_vm(
        self, payload: ResetUserDataForVirtualMachineRequest
    ) -> APIResponse[Dict]:
        """Resets the UserData for virtual machine. The virtual machine must be in a "Stopped" state."""
        return self._execute(
            "resetUserDataForVirtualMachine",
            payload,
            envelope="resetuserdataforvirtualmachineresponse",
        )

    async def reset_userdata_for_vm_async(
        self, payload: ResetUserDataForVirtualMachineRequest
    ) -> APIResponse[Dict]:
        """Asynchronously Resets the UserData for virtual machine. The virtual machine must be in a "Stopped" state."""
        return await self._execute_async(
            "resetUserDataForVirtualMachine",
            payload,
            envelope="resetuserdataforvirtualmachineresponse",
        )

    def restore_vm(self, payload: RestoreVirtualMachineRequest) -> APIResponse[Dict]:
        """Restore a VM to original template/ISO or new template/ISO."""
        return self._execute(
            "restoreVirtualMachine",
            payload,
            envelope="restorevirtualmachineresponse",
        )

    async def restore_vm_async(self, payload: RestoreVirtualMachineRequest) -> APIResponse[Dict]:
        """Asynchronously Restore a VM to original template/ISO or new template/ISO."""
        return await self._execute_async(
            "restoreVirtualMachine",
            payload,
            envelope="restorevirtualmachineresponse",
        )

    def revert_to_vm_sanpshot(self, payload: RevertTOVMSanpshotRequest) -> APIResponse[Dict]:
        """Revert VM from a vmsnapshot."""
        return self._execute(
            "revertToVMSnapshot",
            payload,
            envelope="reverttovmsnapshotresponse",
        )

    async def revert_to_vm_sanpshot_async(
        self, payload: RevertTOVMSanpshotRequest
    ) -> APIResponse[Dict]:
        """Asynchronously Revert VM from a vmsnapshot."""
        return await self._execute_async(
            "revertToVMSnapshot",
            payload,
            envelope="reverttovmsnapshotresponse",
        )

    def scale_vm(self, payload: ScaleVirtualMachineRequest) -> APIResponse[Dict]:
        """Scales the virtual machine to a new service offering."""
        return self._execute(
            "scaleVirtualMachine",
            payload,
            envelope="scalevirtualmachineresponse",
        )

    async def scale_vm_async(self, payload: ScaleVirtualMachineRequest) -> APIResponse[Dict]:
        """Asynchronously Scales the virtual machine to a new service offering."""
        return await self._execute_async(
            "scaleVirtualMachine",
            payload,
            envelope="scalevirtualmachineresponse",
        )

    def start_vm(self, payload: StartVirtualMachineRequest) -> APIResponse[Dict]:
        """Starts a virtual machine."""
        return self._execute(
            "startVirtualMachine",
            payload,
            envelope="startvirtualmachineresponse",
        )

    async def start_vm_async(self, payload: StartVirtualMachineRequest) -> APIResponse[Dict]:
        """Asynchronously Starts a virtual machine."""
        return await self._execute_async(
            "startVirtualMachine",
            payload,
            envelope="startvirtualmachineresponse",
        )

    def stop_vm(self, payload: StopVirtualMachineRequest) -> APIResponse[Dict]:
        """Stops a virtual machine."""
        return self._execute(
            "stopVirtualMachine",
            payload,
            envelope="stopvirtualmachineresponse",
        )

    async def stop_vm_async(self, payload: StopVirtualMachineRequest) -> APIResponse[Dict]:
        """Asynchronously Stops a virtual machine."""
        return await self._execute_async(
            "stopVirtualMachine",
            payload,
            envelope="stopvirtualmachineresponse",
        )

    def update_default_nic_for_vm(
        self, payload: UpdateDefaultNICForVirtualMachineRequest
    ) -> APIResponse[Dict]:
        """Changes the default NIC on a VM."""
        return self._execute(
            "updateDefaultNicForVirtualMachine",
            payload,
            envelope="updatedefaultnicforvirtualmachineresponse",
        )

    async def update_default_nic_for_vm_async(
        self, payload: UpdateDefaultNICForVirtualMachineRequest
    ) -> APIResponse[Dict]:
        """Asynchronously Changes the default NIC on a VM."""
        return await self._execute_async(
            "updateDefaultNicForVirtualMachine",
            payload,
            envelope="updatedefaultnicforvirtualmachineresponse",
        )

    def update_vm(self, payload: UpdateVirtualMachineRequest) -> APIResponse[Dict]:
        """Updates properties of a virtual machine. The VM has to be stopped and restarted for the new properties to take effect."""
        return self._execute(
            "updateVirtualMachine",
            payload,
            envelope="updatevirtualmachineresponse",
        )

    async def update_vm_async(self, payload: UpdateVirtualMachineRequest) -> APIResponse[Dict]:
        """Asynchronously Updates properties of a virtual machine. The VM has to be stopped and restarted for the new properties to take effect."""
        return await self._execute_async(
            "updateVirtualMachine",
            payload,
            envelope="updatevirtualmachineresponse",
        )
