# services/address.py
from typing import Dict, List

from acs_sdk.schemas.request.address import (
    AcquirePodIpAddressRequest,
    AssociateIpAddressRequest,
    DisassociateIpAddressRequest,
    ListPublicIpAddressesRequest,
    ReleaseIpAddressRequest,
    ReleasePodIpAddressRequest,
    ReserveIpAddressRequest,
    UpdateIpAddressRequest,
)

from .base import BaseService
from ..schemas.response.base import APIResponse


class Address(BaseService):
    def list_public_ip_addresses(self, payload: ListPublicIpAddressesRequest) -> APIResponse[List[Dict]]:
        """List all public IP addresses."""
        response = self.client.call("listPublicIpAddresses", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listpublicipaddressesresponse' in response:
            response = response['listpublicipaddressesresponse']
        if 'publicipaddress' in response and response['publicipaddress']:
            data = response['publicipaddress']
            count = response['count']
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    async def list_public_ip_addresses_async(self, payload: ListPublicIpAddressesRequest) -> APIResponse[List[Dict]]:
        """Asynchronously list all public IP addresses."""
        response = await self.client.call_async("listPublicIpAddresses", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listpublicipaddressesresponse' in response:
            response = response['listpublicipaddressesresponse']
        if 'publicipaddress' in response and response['publicipaddress']:
            data = response['publicipaddress']
            count = response['count']
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    def associate_ip_address(self, payload: AssociateIpAddressRequest) -> APIResponse[Dict]:
        """Associate an IP address."""
        response = self.client.call("associateIpAddress", payload.model_dump(exclude_none=True))
        data = {}
        if 'associateipaddressresponse' in response:
            data = response['associateipaddressresponse']
        return APIResponse[Dict](**{"data": data})

    async def associate_ip_address_async(self, payload: AssociateIpAddressRequest) -> APIResponse[Dict]:
        """Asynchronously associate an IP address."""
        response = await self.client.call_async("associateIpAddress", payload.model_dump(exclude_none=True))
        data = {}
        if 'associateipaddressresponse' in response:
            data = response['associateipaddressresponse']
        return APIResponse[Dict](**{"data": data})

    def disassociate_ip_address(self, payload: DisassociateIpAddressRequest) -> APIResponse[Dict]:
        """Disassociate an IP address."""
        response = self.client.call("disassociateIpAddress", payload.model_dump(exclude_none=True))
        data = {}
        if 'disassociateipaddressresponse' in response:
            data = response['disassociateipaddressresponse']
        return APIResponse[Dict](**{"data": data})

    async def disassociate_ip_address_async(self, payload: DisassociateIpAddressRequest) -> APIResponse[Dict]:
        """Asynchronously disassociate an IP address."""
        response = await self.client.call_async("disassociateIpAddress", payload.model_dump(exclude_none=True))
        data = {}
        if 'disassociateipaddressresponse' in response:
            data = response['disassociateipaddressresponse']
        return APIResponse[Dict](**{"data": data})

    def update_ip_address(self, payload: UpdateIpAddressRequest) -> APIResponse[Dict]:
        """Update an IP address."""
        response = self.client.call("updateIpAddress", payload.model_dump(exclude_none=True))
        data = {}
        if 'updateipaddressresponse' in response:
            data = response['updateipaddressresponse']
        return APIResponse[Dict](**{"data": data})

    async def update_ip_address_async(self, payload: UpdateIpAddressRequest) -> APIResponse[Dict]:
        """Asynchronously update an IP address."""
        response = await self.client.call_async("updateIpAddress", payload.model_dump(exclude_none=True))
        data = {}
        if 'updateipaddressresponse' in response:
            data = response['updateipaddressresponse']
        return APIResponse[Dict](**{"data": data})

    def release_ip_address(self, payload: ReleaseIpAddressRequest) -> APIResponse[Dict]:
        """Release an IP address."""
        response = self.client.call("releaseIpAddress", payload.model_dump(exclude_none=True))
        data = {}
        if 'releaseipaddressresponse' in response:
            data = response['releaseipaddressresponse']
        return APIResponse[Dict](**{"data": data})

    async def release_ip_address_async(self, payload: ReleaseIpAddressRequest) -> APIResponse[Dict]:
        """Asynchronously release an IP address."""
        response = await self.client.call_async("releaseIpAddress", payload.model_dump(exclude_none=True))
        data = {}
        if 'releaseipaddressresponse' in response:
            data = response['releaseipaddressresponse']
        return APIResponse[Dict](**{"data": data})

    def reserve_ip_address(self, payload: ReserveIpAddressRequest) -> APIResponse[Dict]:
        """Reserve an IP address."""
        response = self.client.call("reserveIpAddress", payload.model_dump(exclude_none=True))
        data = {}
        if 'reserveipaddressresponse' in response:
            data = response['reserveipaddressresponse']
        return APIResponse[Dict](**{"data": data})

    async def reserve_ip_address_async(self, payload: ReserveIpAddressRequest) -> APIResponse[Dict]:
        """Asynchronously reserve an IP address."""
        response = await self.client.call_async("reserveIpAddress", payload.model_dump(exclude_none=True))
        data = {}
        if 'reserveipaddressresponse' in response:
            data = response['reserveipaddressresponse']
        return APIResponse[Dict](**{"data": data})

    def acquire_pod_ip_address(self, payload: AcquirePodIpAddressRequest) -> APIResponse[Dict]:
        """Acquire a pod IP address."""
        response = self.client.call("acquirePodIpAddress", payload.model_dump(exclude_none=True))
        data = {}
        if 'acquirepodipaddressresponse' in response:
            data = response['acquirepodipaddressresponse']
        return APIResponse[Dict](**{"data": data})

    async def acquire_pod_ip_address_async(self, payload: AcquirePodIpAddressRequest) -> APIResponse[Dict]:
        """Asynchronously acquire a pod IP address."""
        response = await self.client.call_async("acquirePodIpAddress", payload.model_dump(exclude_none=True))
        data = {}
        if 'acquirepodipaddressresponse' in response:
            data = response['acquirepodipaddressresponse']
        return APIResponse[Dict](**{"data": data})

    def release_pod_ip_address(self, payload: ReleasePodIpAddressRequest) -> APIResponse[Dict]:
        """Release a pod IP address."""
        response = self.client.call("releasePodIpAddress", payload.model_dump(exclude_none=True))
        data = {}
        if 'releasepodipaddressresponse' in response:
            data = response['releasepodipaddressresponse']
        return APIResponse[Dict](**{"data": data})

    async def release_pod_ip_address_async(self, payload: ReleasePodIpAddressRequest) -> APIResponse[Dict]:
        """Asynchronously release a pod IP address."""
        response = await self.client.call_async("releasePodIpAddress", payload.model_dump(exclude_none=True))
        data = {}
        if 'releasepodipaddressresponse' in response:
            data = response['releasepodipaddressresponse']
        return APIResponse[Dict](**{"data": data})