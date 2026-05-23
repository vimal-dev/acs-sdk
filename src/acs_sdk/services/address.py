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
    def list_public_ip_addresses(
        self, payload: ListPublicIpAddressesRequest
    ) -> APIResponse[List[Dict]]:
        """List all public IP addresses."""
        return self._execute(
            "listPublicIpAddresses",
            payload,
            envelope="listpublicipaddressesresponse",
            entity="publicipaddress",
        )

    async def list_public_ip_addresses_async(
        self, payload: ListPublicIpAddressesRequest
    ) -> APIResponse[List[Dict]]:
        """Asynchronously list all public IP addresses."""
        return await self._execute_async(
            "listPublicIpAddresses",
            payload,
            envelope="listpublicipaddressesresponse",
            entity="publicipaddress",
        )

    def associate_ip_address(self, payload: AssociateIpAddressRequest) -> APIResponse[Dict]:
        """Associate an IP address."""
        return self._execute(
            "associateIpAddress",
            payload,
            envelope="associateipaddressresponse",
            entity="publicipaddress",
        )

    async def associate_ip_address_async(
        self, payload: AssociateIpAddressRequest
    ) -> APIResponse[Dict]:
        """Asynchronously associate an IP address."""
        return await self._execute_async(
            "associateIpAddress",
            payload,
            envelope="associateipaddressresponse",
            entity="publicipaddress",
        )

    def disassociate_ip_address(self, payload: DisassociateIpAddressRequest) -> APIResponse[Dict]:
        """Disassociate an IP address."""
        return self._execute(
            "disassociateIpAddress",
            payload,
            envelope="disassociateipaddressresponse",
        )

    async def disassociate_ip_address_async(
        self, payload: DisassociateIpAddressRequest
    ) -> APIResponse[Dict]:
        """Asynchronously disassociate an IP address."""
        return await self._execute_async(
            "disassociateIpAddress",
            payload,
            envelope="disassociateipaddressresponse",
        )

    def update_ip_address(self, payload: UpdateIpAddressRequest) -> APIResponse[Dict]:
        """Update an IP address."""
        return self._execute(
            "updateIpAddress",
            payload,
            envelope="updateipaddressresponse",
            entity="publicipaddress",
        )

    async def update_ip_address_async(self, payload: UpdateIpAddressRequest) -> APIResponse[Dict]:
        """Asynchronously update an IP address."""
        return await self._execute_async(
            "updateIpAddress",
            payload,
            envelope="updateipaddressresponse",
            entity="publicipaddress",
        )

    def release_ip_address(self, payload: ReleaseIpAddressRequest) -> APIResponse[Dict]:
        """Release an IP address."""
        return self._execute(
            "releaseIpAddress",
            payload,
            envelope="releaseipaddressresponse",
        )

    async def release_ip_address_async(self, payload: ReleaseIpAddressRequest) -> APIResponse[Dict]:
        """Asynchronously release an IP address."""
        return await self._execute_async(
            "releaseIpAddress",
            payload,
            envelope="releaseipaddressresponse",
        )

    def reserve_ip_address(self, payload: ReserveIpAddressRequest) -> APIResponse[Dict]:
        """Reserve an IP address."""
        return self._execute(
            "reserveIpAddress",
            payload,
            envelope="reserveipaddressresponse",
            entity="ipaddress",
        )

    async def reserve_ip_address_async(self, payload: ReserveIpAddressRequest) -> APIResponse[Dict]:
        """Asynchronously reserve an IP address."""
        return await self._execute_async(
            "reserveIpAddress",
            payload,
            envelope="reserveipaddressresponse",
            entity="ipaddress",
        )

    def acquire_pod_ip_address(self, payload: AcquirePodIpAddressRequest) -> APIResponse[Dict]:
        """Acquire a pod IP address."""
        return self._execute(
            "acquirePodIpAddress",
            payload,
            envelope="acquirepodipaddressresponse",
        )

    async def acquire_pod_ip_address_async(
        self, payload: AcquirePodIpAddressRequest
    ) -> APIResponse[Dict]:
        """Asynchronously acquire a pod IP address."""
        return await self._execute_async(
            "acquirePodIpAddress",
            payload,
            envelope="acquirepodipaddressresponse",
        )

    def release_pod_ip_address(self, payload: ReleasePodIpAddressRequest) -> APIResponse[Dict]:
        """Release a pod IP address."""
        return self._execute(
            "releasePodIpAddress",
            payload,
            envelope="releasepodipaddressresponse",
        )

    async def release_pod_ip_address_async(
        self, payload: ReleasePodIpAddressRequest
    ) -> APIResponse[Dict]:
        """Asynchronously release a pod IP address."""
        return await self._execute_async(
            "releasePodIpAddress",
            payload,
            envelope="releasepodipaddressresponse",
        )
