# services/virtual_machine.py
import pprint
from typing import Dict, List

from acs_sdk.schemas.request.virtual_machine import AddNICToVirtualMachineRequest, AssignVirtualMachineToBackupOfferingRequest, ListVirtualMachinesRequest

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
        response = await self.client.async_call("listVirtualMachines", payload.model_dump(exclude_none=True))
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
        response = await self.client.async_call("addNicToVirtualMachine", payload.model_dump(exclude_none=True))
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
        response = await self.client.async_call("assignVirtualMachineToBackupOffering", payload.model_dump(exclude_none=True))
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
        response = await self.client.async_call("cleanVMReservations")
        data = {}
        if 'cleanvmreservationresponse' in response:
            data = response['cleanvmreservationresponse']
        return APIResponse[Dict](**{"data": data})
    
    
