# services/virtual_machine.py
import pprint
from typing import Dict, List

from acs_sdk.schemas.request.virtual_machine import AddNICToVirtualMachineRequest, AssignVirtualMachineToBackupOfferingRequest, CreateVMScheduleRequest, DeleteVMScheduleRequest, DeployVirtualMachineRequest, DestroyVirtualMachineRequest, ListVirtualMachinesRequest, UpdateVMScheduleRequest

from .base import BaseService
from ..schemas.response.base import APIResponse


class VirtualMachine(BaseService):
    def list(self, payload: ListVirtualMachinesRequest) -> APIResponse[List[Dict]]:
        """List all available virtual machines."""
        response = self.client.call("listVirtualMachines", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listvirtualmachinesresponse' in response:
            response = response['listvirtualmachinesresponse']
        if 'virtualmachine' in response and response['virtualmachine']:
            data = response['virtualmachine']
            count = response['count']
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    async def list_async(self, payload: ListVirtualMachinesRequest) -> APIResponse[List[Dict]]:
        """Asynchronously list all available virtual machines."""
        response = await self.client.call_async("listVirtualMachines", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listvirtualmachinesresponse' in response:
            response = response['listvirtualmachinesresponse']
        if 'virtualmachine' in response and response['virtualmachine']:
            data = response['virtualmachine']
            count = response['count']
        return APIResponse[List[Dict]](**{"data": data, "count": count})
    

    def add_nic_to_virtual_machine(self, payload: AddNICToVirtualMachineRequest) -> APIResponse[Dict]:
        """Add a NIC to a virtual machine."""
        response = self.client.call("addNicToVirtualMachine", payload.model_dump(exclude_none=True))
        data = {}
        if 'addnictovirtualmachineresponse' in response:
            data = response['addnictovirtualmachineresponse']
        return APIResponse[Dict](**{"data": data})

    async def add_nic_to_virtual_machine_async(self, payload: AddNICToVirtualMachineRequest) -> APIResponse[Dict]:
        """Asynchronously add a NIC to a virtual machine."""
        response = await self.client.call_async("addNicToVirtualMachine", payload.model_dump(exclude_none=True))
        data = {}
        if 'addnictovirtualmachineresponse' in response:
            data = response['addnictovirtualmachineresponse']
        return APIResponse[Dict](**{"data": data})
    
    def assign_virtual_machine_to_backup_offering(self, payload: AssignVirtualMachineToBackupOfferingRequest) -> APIResponse[Dict]:
        """Assign a virtual machine to a backup offering."""
        response = self.client.call("assignVirtualMachineToBackupOffering", payload.model_dump(exclude_none=True))
        data = {}
        if 'assignvirtualmachinetobackupofferingresponse' in response:
            data = response['assignvirtualmachinetobackupofferingresponse']
        return APIResponse[Dict](**{"data": data})

    async def assign_virtual_machine_to_backup_offering_async(self, payload: AssignVirtualMachineToBackupOfferingRequest) -> APIResponse[Dict]:
        """Asynchronously assign a virtual machine to a backup offering."""
        response = await self.client.call_async("assignVirtualMachineToBackupOffering", payload.model_dump(exclude_none=True))
        data = {}
        if 'assignvirtualmachinetobackupofferingresponse' in response:
            data = response['assignvirtualmachinetobackupofferingresponse']
        return APIResponse[Dict](**{"data": data})
    
    def clean_vm_reservations(self) -> APIResponse[Dict]:
        """Cleanups VM reservations in the database."""
        response = self.client.call("cleanVMReservations")
        data = {}
        if 'cleanvmreservationresponse' in response:
            data = response['cleanvmreservationresponse']
        return APIResponse[Dict](**{"data": data})

    async def clean_vm_reservations_async(self) -> APIResponse[Dict]:
        """Cleanups VM reservations in the database.."""
        response = await self.client.call_async("cleanVMReservations")
        data = {}
        if 'cleanvmreservationresponse' in response:
            data = response['cleanvmreservationresponse']
        return APIResponse[Dict](**{"data": data})
    
    def create_vm_schedule(self, payload: CreateVMScheduleRequest) -> APIResponse[Dict]:
        """Creates a VM schedule."""
        response = self.client.call("createVMSchedule", payload.model_dump(exclude_none=True))
        data = {}
        if 'createvmscheduleresponse' in response:
            data = response['createvmscheduleresponse']
        return APIResponse[Dict](**{"data": data})

    async def create_vm_schedule_async(self, payload: CreateVMScheduleRequest) -> APIResponse[Dict]:
        """Asynchronously creates a VM schedule."""
        response = await self.client.call_async("createVMSchedule", payload.model_dump(exclude_none=True))
        data = {}
        if 'createvmscheduleresponse' in response:
            data = response['createvmscheduleresponse']
        return APIResponse[Dict](**{"data": data})

    def update_vm_schedule(self, payload: UpdateVMScheduleRequest) -> APIResponse[Dict]:
        """Updates a VM schedule."""
        response = self.client.call("updateVMSchedule", payload.model_dump(exclude_none=True))
        data = {}
        if 'updatevmscheduleresponse' in response:
            data = response['updatevmscheduleresponse']
        return APIResponse[Dict](**{"data": data})

    async def update_vm_schedule_async(self, payload: UpdateVMScheduleRequest) -> APIResponse[Dict]:
        """Asynchronously updates a VM schedule."""
        response = await self.client.call_async("updateVMSchedule", payload.model_dump(exclude_none=True))
        data = {}
        if 'updatevmscheduleresponse' in response:
            data = response['updatevmscheduleresponse']
        return APIResponse[Dict](**{"data": data})
    
    def delete_vm_schedule(self, payload: DeleteVMScheduleRequest) -> APIResponse[Dict]:
        """Deletes a VM schedule."""
        response = self.client.call("deleteVMSchedule", payload.model_dump(exclude_none=True))
        data = {}
        if 'deletevmscheduleresponse' in response:
            data = response['deletevmscheduleresponse']
        return APIResponse[Dict](**{"data": data})

    async def delete_vm_schedule_async(self, payload: DeleteVMScheduleRequest) -> APIResponse[Dict]:
        """Asynchronously deletes a VM schedule."""
        response = await self.client.call_async("deleteVMSchedule", payload.model_dump(exclude_none=True))
        data = {}
        if 'deletevmscheduleresponse' in response:
            data = response['deletevmscheduleresponse']
        return APIResponse[Dict](**{"data": data})
    
    def deploy_vm(self, payload: DeployVirtualMachineRequest) -> APIResponse[Dict]:
        """Creates and automatically starts a virtual machine based on a service offering, disk offering, and template."""
        response = self.client.call("deployVirtualMachine", payload.model_dump(exclude_none=True))
        data = {}
        if 'deployvirtualmachineresponse' in response:
            data = response['deployvirtualmachineresponse']
        return APIResponse[Dict](**{"data": data})

    async def deploy_vm_async(self, payload: DeployVirtualMachineRequest) -> APIResponse[Dict]:
        """Asynchronously Creates and automatically starts a virtual machine based on a service offering, disk offering, and template."""
        response = await self.client.call_async("deployVirtualMachine", payload.model_dump(exclude_none=True))
        data = {}
        if 'deployvirtualmachineresponse' in response:
            data = response['deployvirtualmachineresponse']
        return APIResponse[Dict](**{"data": data})
    
    def destroy_vm(self, payload: DestroyVirtualMachineRequest) -> APIResponse[Dict]:
        """Destroys a virtual machine. Once destroyed, only the administrator can recover it.."""
        response = self.client.call("destroyVirtualMachine", payload.model_dump(exclude_none=True))
        data = {}
        if 'destroyvirtualmachineresponse' in response:
            data = response['destroyvirtualmachineresponse']
        return APIResponse[Dict](**{"data": data})

    async def destroy_vm_async(self, payload: DestroyVirtualMachineRequest) -> APIResponse[Dict]:
        """Asynchronously destroys a virtual machine. Once destroyed, only the administrator can recover it.."""
        response = await self.client.call_async("destroyVirtualMachine", payload.model_dump(exclude_none=True))
        data = {}
        if 'destroyvirtualmachineresponse' in response:
            data = response['destroyvirtualmachineresponse']
        return APIResponse[Dict](**{"data": data})
    

    def expunge_vm(self, id: str) -> APIResponse[Dict]:
        """Expunge a virtual machine. Once expunged, it cannot be recovered."""
        response = self.client.call("expungeVirtualMachine", {"id": id})
        data = {}
        if 'expungevirtualmachineresponse' in response:
            data = response['expungevirtualmachineresponse']
        return APIResponse[Dict](**{"data": data})

    async def expunge_vm_async(self, id: str) -> APIResponse[Dict]:
        """Asynchronously expunges a virtual machine. Once expunged, it cannot be recovered."""
        response = await self.client.call_async("expungeVirtualMachine", {"id": id})
        data = {}
        if 'expungevirtualmachineresponse' in response:
            data = response['expungevirtualmachineresponse']
        return APIResponse[Dict](**{"data": data})
    
    def get_vm_password(self, id: str) -> APIResponse[Dict]:
        """Returns the base64 encoded encrypted password for the VM."""
        response = self.client.call("getVMPassword", {"id": id})
        data = {}
        if 'getvmpasswordresponse' in response:
            data = response['getvmpasswordresponse']
        return APIResponse[Dict](**{"data": data})

    async def get_vm_password_async(self, id: str) -> APIResponse[Dict]:
        """Asynchronously returns the base64 encoded encrypted password for the VM."""
        response = await self.client.call_async("getVMPassword", {"id": id})
        data = {}
        if 'getvmpasswordresponse' in response:
            data = response['getvmpasswordresponse']
        return APIResponse[Dict](**{"data": data})
    
    def get_vm_userdata(self, id: str) -> APIResponse[Dict]:
        """Returns the base64 encoded encrypted userdata for the VM."""
        response = self.client.call("getVMUserData", {"id": id})
        data = {}
        if 'getvmuserdataresponse' in response:
            data = response['getvmuserdataresponse']
        return APIResponse[Dict](**{"data": data})

    async def get_vm_userdata_async(self, id: str) -> APIResponse[Dict]:
        """Asynchronously returns the base64 encoded encrypted userdata for the VM."""
        response = await self.client.call_async("getVMUserData", {"id": id})
        data = {}
        if 'getvmuserdataresponse' in response:
            data = response['getvmuserdataresponse']
        return APIResponse[Dict](**{"data": data})
    
    
