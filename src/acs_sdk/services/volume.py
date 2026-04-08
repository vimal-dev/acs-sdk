# services/volume.py
from typing import Dict

from acs_sdk.schemas.request.volume import (
    AssignVolumeRequest,
    AttachVolumeRequest,
    ChangeOfferingForVolumeRequest,
    CheckVolumeRequest,
    CreateVolumeRequest,
    DestroyVolumeRequest,
    DetachVolumeRequest,
    ExtractVolumeRequest,
)

from .base import BaseService
from ..schemas.response.base import APIResponse


class Volume(BaseService):

    def assign_volume(self, payload: AssignVolumeRequest) -> APIResponse[Dict]:
        """Changes ownership of a Volume from one account to another."""
        data = self.client.call("assignVolume", payload.model_dump(exclude_none=True))
        return APIResponse[Dict](**data)

    async def assign_volume_async(
        self, payload: AssignVolumeRequest
    ) -> APIResponse[Dict]:
        """Changes ownership of a Volume from one account to another."""
        data = await self.client.call_async(
            "assignVolume", payload.model_dump(exclude_none=True)
        )
        return APIResponse[Dict](**data)

    def attach_volume(self, payload: AttachVolumeRequest) -> APIResponse[Dict]:
        """Attaches a Volume to a Compute Instance."""
        data = self.client.call("attachVolume", payload.model_dump(exclude_none=True))
        return APIResponse[Dict](**data)

    async def attach_volume_async(
        self, payload: AttachVolumeRequest
    ) -> APIResponse[Dict]:
        """Attaches a Volume to a Compute Instance."""
        data = await self.client.call_async(
            "attachVolume", payload.model_dump(exclude_none=True)
        )
        return APIResponse[Dict](**data)

    def change_offering(
        self, payload: ChangeOfferingForVolumeRequest
    ) -> APIResponse[Dict]:
        """Change disk offering of the volume and also an option to auto migrate if required to apply the new disk offering."""
        data = self.client.call(
            "changeOfferingForVolume", payload.model_dump(exclude_none=True)
        )
        return APIResponse[Dict](**data)

    async def change_offering_async(
        self, payload: ChangeOfferingForVolumeRequest
    ) -> APIResponse[Dict]:
        """Change disk offering of the volume and also an option to auto migrate if required to apply the new disk offering."""
        data = await self.client.call_async(
            "changeOfferingForVolume", payload.model_dump(exclude_none=True)
        )
        return APIResponse[Dict](**data)

    def check_volume(self, payload: CheckVolumeRequest) -> APIResponse[Dict]:
        """Check the volume for any errors or leaks and also repairs when repair parameter is passed, this is currently supported for KVM only."""
        data = self.client.call("checkVolume", payload.model_dump(exclude_none=True))
        return APIResponse[Dict](**data)

    async def check_volume_async(
        self, payload: CheckVolumeRequest
    ) -> APIResponse[Dict]:
        """Check the volume for any errors or leaks and also repairs when repair parameter is passed, this is currently supported for KVM only."""
        data = await self.client.call_async(
            "checkVolume", payload.model_dump(exclude_none=True)
        )
        return APIResponse[Dict](**data)

    def create_volume(self, payload: CreateVolumeRequest) -> APIResponse[Dict]:
        """Creates a disk volume from a disk offering. This disk volume must still be attached to a virtual machine to make use of it."""
        data = self.client.call("createVolume", payload.model_dump(exclude_none=True))
        return APIResponse[Dict](**data)

    async def create_volume_async(
        self, payload: CreateVolumeRequest
    ) -> APIResponse[Dict]:
        """Creates a disk volume from a disk offering. This disk volume must still be attached to a virtual machine to make use of it."""
        data = await self.client.call_async(
            "createVolume", payload.model_dump(exclude_none=True)
        )
        return APIResponse[Dict](**data)

    def delete_volume(self, id: str) -> APIResponse[Dict]:
        """Deletes a detached disk volume."""
        data = self.client.call("deleteVolume", {"id": id})
        return APIResponse[Dict](**data)

    async def delete_volume_async(self, id: str) -> APIResponse[Dict]:
        """Deletes a detached disk volume."""
        data = await self.client.call_async("deleteVolume", {"id": id})
        return APIResponse[Dict](**data)

    def destroy_volume(self, payload: DestroyVolumeRequest) -> APIResponse[Dict]:
        """Destroys a detached disk volume."""
        data = self.client.call("destroyVolume", payload.model_dump(exclude_none=True))
        return APIResponse[Dict](**data)

    async def destroy_volume_async(
        self, payload: DestroyVolumeRequest
    ) -> APIResponse[Dict]:
        """Destroys a detached disk volume."""
        data = await self.client.call_async(
            "destroyVolume", payload.model_dump(exclude_none=True)
        )
        return APIResponse[Dict](**data)

    def detach_volume(self, payload: DetachVolumeRequest) -> APIResponse[Dict]:
        """Detaches a volume from a virtual machine."""
        data = self.client.call("detachVolume", payload.model_dump(exclude_none=True))
        return APIResponse[Dict](**data)

    async def detach_volume_async(
        self, payload: DetachVolumeRequest
    ) -> APIResponse[Dict]:
        """Detaches a volume from a virtual machine."""
        data = await self.client.call_async(
            "detachVolume", payload.model_dump(exclude_none=True)
        )
        return APIResponse[Dict](**data)

    def extract_volume(self, payload: ExtractVolumeRequest) -> APIResponse[Dict]:
        """Extracts a volume. Used for backup or migration purposes."""
        data = self.client.call("extractVolume", payload.model_dump(exclude_none=True))
        return APIResponse[Dict](**data)

    async def extract_volume_async(
        self, payload: ExtractVolumeRequest
    ) -> APIResponse[Dict]:
        """Extracts a volume. Used for backup or migration purposes."""
        data = await self.client.call_async(
            "extractVolume", payload.model_dump(exclude_none=True)
        )
        return APIResponse[Dict](**data)
    
    def get_volume_path(self, id: str) -> APIResponse[Dict]:
        """Gets the path of a volume."""
        data = self.client.call("getPathForVolume", {"id": id})
        return APIResponse[Dict](**data)

    async def get_volume_path_async(self, id: str) -> APIResponse[Dict]:
        """Gets the path of a volume."""
        data = await self.client.call_async("getPathForVolume", {"volumeid": id})
        return APIResponse[Dict](**data)

    def list(self) -> APIResponse[Dict]:
        """Lists all volumes."""
        data = self.client.call("listVolumes")
        return APIResponse[Dict](**data)

    async def list_async(self) -> APIResponse[Dict]:
        """Lists all volumes."""
        data = await self.client.call_async("listVolumes")
        return APIResponse[Dict](**data)
