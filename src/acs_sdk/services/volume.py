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
    GetVolumeRequest,
    ListVolumesRequest,
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

    def get_volume_path(self, payload: GetVolumeRequest) -> APIResponse[Dict]:
        """Gets the path of a volume."""
        return self._execute(
            "getPathForVolume",
            payload,
            envelope="getpathforvolumeresponse",
        )

    async def get_volume_path_async(self, payload: GetVolumeRequest) -> APIResponse[Dict]:
        """Gets the path of a volume."""
        return await self._execute_async(
            "getPathForVolume",
            payload,
            envelope="getpathforvolumeresponse",
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
        """Lists all volumes."""
        return await self._execute_async(
            "listVolumes",
            payload,
            envelope="listvolumesresponse",
            entity="volume",
        )
