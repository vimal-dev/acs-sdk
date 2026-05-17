# services/virtual_machine.py
from typing import Dict, List

from acs_sdk.schemas.request.virtual_machine import (
    AddNICToVirtualMachineRequest,
    AssignVirtualMachineToBackupOfferingRequest,
    CreateVMScheduleRequest,
    DeleteVMScheduleRequest,
    DeployVirtualMachineRequest,
    DestroyVirtualMachineRequest,
    ListVirtualMachinesRequest,
    UpdateVMScheduleRequest,
    CleanVMReservationsRequest,
    ExpungeVirtualMachineRequest,
    GetVMPasswordRequest,
    GetVMUserdataRequest,
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
