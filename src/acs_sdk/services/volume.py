# services/volume.py
from typing import Dict, List

from acs_sdk.schemas.request.volume import (
    AssignVolumeRequest,
    AttachVolumeRequest,
    ChangeOfferingForVolumeRequest,
    CheckVolumeRequest,
    CreateVolumeRequest,
    DestroyVolumeRequest,
    DetachVolumeRequest,
    ExtractVolumeRequest,
    ListVolumesRequest,
)

from .base import BaseService
from ..schemas.response.base import APIResponse


class Volume(BaseService):

    def assign_volume(self, payload: AssignVolumeRequest) -> APIResponse[Dict]:
        """Changes ownership of a Volume from one account to another."""
        response = self.client.call("assignVolume", payload.model_dump(exclude_none=True))
        data = {}
        if 'assignvolumeresponse' in response:
            data = response['assignvolumeresponse']
        return APIResponse[Dict](**{"data": data})

    async def assign_volume_async(
        self, payload: AssignVolumeRequest
    ) -> APIResponse[Dict]:
        """Changes ownership of a Volume from one account to another."""
        response = await self.client.call_async(
            "assignVolume", payload.model_dump(exclude_none=True)
        )
        data = {}
        if 'assignvolumeresponse' in response:
            data = response['assignvolumeresponse']
        return APIResponse[Dict](**{"data": data})

    def attach_volume(self, payload: AttachVolumeRequest) -> APIResponse[Dict]:
        """Attaches a Volume to a Compute Instance."""
        response = self.client.call("attachVolume", payload.model_dump(exclude_none=True))
        data = {}
        if 'attachvolumeresponse' in response:
            data = response['attachvolumeresponse']
        return APIResponse[Dict](**{"data": data})

    async def attach_volume_async(
        self, payload: AttachVolumeRequest
    ) -> APIResponse[Dict]:
        """Attaches a Volume to a Compute Instance."""
        response = await self.client.call_async(
            "attachVolume", payload.model_dump(exclude_none=True)
        )
        data = {}
        if 'attachvolumeresponse' in response:
            data = response['attachvolumeresponse']
        return APIResponse[Dict](**{"data": data})

    def change_offering(
        self, payload: ChangeOfferingForVolumeRequest
    ) -> APIResponse[Dict]:
        """Change disk offering of the volume and also an option to auto migrate if required to apply the new disk offering."""
        response = self.client.call(
            "changeOfferingForVolume", payload.model_dump(exclude_none=True)
        )
        data = {}
        if 'changeofferingforvolumeresponse' in response:
            data = response['changeofferingforvolumeresponse']
        return APIResponse[Dict](**{"data": data})

    async def change_offering_async(
        self, payload: ChangeOfferingForVolumeRequest
    ) -> APIResponse[Dict]:
        """Change disk offering of the volume and also an option to auto migrate if required to apply the new disk offering."""
        response = await self.client.call_async(
            "changeOfferingForVolume", payload.model_dump(exclude_none=True)
        )
        data = {}
        if 'changeofferingforvolumeresponse' in response:
            data = response['changeofferingforvolumeresponse']
        return APIResponse[Dict](**{"data": data})

    def check_volume(self, payload: CheckVolumeRequest) -> APIResponse[Dict]:
        """Check the volume for any errors or leaks and also repairs when repair parameter is passed, this is currently supported for KVM only."""
        response = self.client.call("checkVolume", payload.model_dump(exclude_none=True))
        data = {}
        if 'checkvolumeresponse' in response:
            data = response['checkvolumeresponse']
        return APIResponse[Dict](**{"data": data})

    async def check_volume_async(
        self, payload: CheckVolumeRequest
    ) -> APIResponse[Dict]:
        """Check the volume for any errors or leaks and also repairs when repair parameter is passed, this is currently supported for KVM only."""
        response = await self.client.call_async(
            "checkVolume", payload.model_dump(exclude_none=True)
        )
        data = {}
        if 'checkvolumeresponse' in response:
            data = response['checkvolumeresponse']
        return APIResponse[Dict](**{"data": data})

    def create_volume(self, payload: CreateVolumeRequest) -> APIResponse[Dict]:
        """Creates a disk volume from a disk offering. This disk volume must still be attached to a virtual machine to make use of it."""
        response = self.client.call("createVolume", payload.model_dump(exclude_none=True))
        data = {}
        if 'createvolumeresponse' in response:
            data = response['createvolumeresponse']
        return APIResponse[Dict](**{"data": data})

    async def create_volume_async(
        self, payload: CreateVolumeRequest
    ) -> APIResponse[Dict]:
        """Creates a disk volume from a disk offering. This disk volume must still be attached to a virtual machine to make use of it."""
        response = await self.client.call_async(
            "createVolume", payload.model_dump(exclude_none=True)
        )
        data = {}
        if 'createvolumeresponse' in response:
            data = response['createvolumeresponse']
        return APIResponse[Dict](**{"data": data})

    def delete_volume(self, id: str) -> APIResponse[Dict]:
        """Deletes a detached disk volume."""
        response = self.client.call("deleteVolume", {"id": id})
        data = {}
        if 'deletevolumeresponse' in response:
            data = response['deletevolumeresponse']
        return APIResponse[Dict](**{"data": data})

    async def delete_volume_async(self, id: str) -> APIResponse[Dict]:
        """Deletes a detached disk volume."""
        response = await self.client.call_async("deleteVolume", {"id": id})
        data = {}
        if 'deletevolumeresponse' in response:
            data = response['deletevolumeresponse']
        return APIResponse[Dict](**{"data": data})

    def destroy_volume(self, payload: DestroyVolumeRequest) -> APIResponse[Dict]:
        """Destroys a detached disk volume."""
        response = self.client.call("destroyVolume", payload.model_dump(exclude_none=True))
        data = {}
        if 'destroyvolumeresponse' in response:
            data = response['destroyvolumeresponse']
        return APIResponse[Dict](**{"data": data})

    async def destroy_volume_async(
        self, payload: DestroyVolumeRequest
    ) -> APIResponse[Dict]:
        """Destroys a detached disk volume."""
        response = await self.client.call_async(
            "destroyVolume", payload.model_dump(exclude_none=True)
        )
        data = {}
        if 'destroyvolumeresponse' in response:
            data = response['destroyvolumeresponse']
        return APIResponse[Dict](**{"data": data})

    def detach_volume(self, payload: DetachVolumeRequest) -> APIResponse[Dict]:
        """Detaches a volume from a virtual machine."""
        response = self.client.call("detachVolume", payload.model_dump(exclude_none=True))
        data = {}
        if 'detachvolumeresponse' in response:
            data = response['detachvolumeresponse']
        return APIResponse[Dict](**{"data": data})

    async def detach_volume_async(
        self, payload: DetachVolumeRequest
    ) -> APIResponse[Dict]:
        """Detaches a volume from a virtual machine."""
        response = await self.client.call_async(
            "detachVolume", payload.model_dump(exclude_none=True)
        )
        data = {}
        if 'detachvolumeresponse' in response:
            data = response['detachvolumeresponse']
        return APIResponse[Dict](**{"data": data})

    def extract_volume(self, payload: ExtractVolumeRequest) -> APIResponse[Dict]:
        """Extracts a volume. Used for backup or migration purposes."""
        response = self.client.call("extractVolume", payload.model_dump(exclude_none=True))
        data = {}
        if 'extractvolumeresponse' in response:
            data = response['extractvolumeresponse']
        return APIResponse[Dict](**{"data": data})

    async def extract_volume_async(
        self, payload: ExtractVolumeRequest
    ) -> APIResponse[Dict]:
        """Extracts a volume. Used for backup or migration purposes."""
        response = await self.client.call_async(
            "extractVolume", payload.model_dump(exclude_none=True)
        )
        data = {}
        if 'extractvolumeresponse' in response:
            data = response['extractvolumeresponse']
        return APIResponse[Dict](**{"data": data})
    
    def get_volume_path(self, id: str) -> APIResponse[Dict]:
        """Gets the path of a volume."""
        response = self.client.call("getPathForVolume", {"id": id})
        data = {}
        if 'getpathforvolumeresponse' in response:
            data = response['getpathforvolumeresponse']
        return APIResponse[Dict](**{"data": data})

    async def get_volume_path_async(self, id: str) -> APIResponse[Dict]:
        """Gets the path of a volume."""
        response = await self.client.call_async("getPathForVolume", {"volumeid": id})
        data = {}
        if 'getpathforvolumeresponse' in response:
            data = response['getpathforvolumeresponse']
        return APIResponse[Dict](**{"data": data})

    def list(self, payload: ListVolumesRequest) -> APIResponse[Dict]:
        """Lists all volumes."""
        response = self.client.call("listVolumes", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listvolumesresponse' in response:
            response = response['listvolumesresponse']
        if 'volume' in response and response['volume']:
            data = response['volume']
            count = response['count']
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    async def list_async(self, payload: ListVolumesRequest) -> APIResponse[Dict]:
        """Lists all volumes."""
        data = await self.client.call_async("listVolumes", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listvolumesresponse' in response:
            response = response['listvolumesresponse']
        if 'volume' in response and response['volume']:
            data = response['volume']
            count = response['count']
        return APIResponse[List[Dict]](**{"data": data, "count": count})
