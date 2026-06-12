# services/iso.py
from typing import Dict, List

from .base import BaseService
from ..schemas.response.base import APIResponse
from ..schemas.request.iso import (
    AttachIsoRequest,
    CopyIsoRequest,
    DeleteIsoRequest,
    DetachIsoRequest,
    ExtractIsoRequest,
    GetUploadParamsForIsoRequest,
    ListIsoPermissionsRequest,
    ListIsosRequest,
    RegisterIsoRequest,
    UpdateIsoRequest,
    UpdateIsoPermissionsRequest,
)


class ISO(BaseService):
    """Service class for managing ISOs in Apache CloudStack."""

    # -------------------------------------------------------------------------
    # Query / list
    # -------------------------------------------------------------------------

    def list(self, payload: ListIsosRequest) -> APIResponse[List[Dict]]:
        """List available ISOs based on the specified filters."""
        return self._execute(
            "listIsos",
            payload,
            envelope="listisosresponse",
            entity="iso",
        )

    async def list_async(self, payload: ListIsosRequest) -> APIResponse[List[Dict]]:
        """Asynchronously list available ISOs based on the specified filters."""
        return await self._execute_async(
            "listIsos",
            payload,
            envelope="listisosresponse",
            entity="iso",
        )

    def list_permissions(self, payload: ListIsoPermissionsRequest) -> APIResponse[Dict]:
        """List permission details for an ISO."""
        return self._execute(
            "listIsoPermissions",
            payload,
            envelope="listisopermissionsresponse",
            entity="isopermission",
        )

    async def list_permissions_async(self, payload: ListIsoPermissionsRequest) -> APIResponse[Dict]:
        """Asynchronously list permission details for an ISO."""
        return await self._execute_async(
            "listIsoPermissions",
            payload,
            envelope="listisopermissionsresponse",
            entity="isopermission",
        )

    # -------------------------------------------------------------------------
    # Register / update / delete
    # -------------------------------------------------------------------------

    def register(self, payload: RegisterIsoRequest) -> APIResponse[Dict]:
        """Register an existing ISO into the CloudStack cloud."""
        return self._execute(
            "registerIso",
            payload,
            envelope="registerisoresponse",
            entity="iso",
        )

    async def register_async(self, payload: RegisterIsoRequest) -> APIResponse[Dict]:
        """Asynchronously register an existing ISO into the CloudStack cloud."""
        return await self._execute_async(
            "registerIso",
            payload,
            envelope="registerisoresponse",
            entity="iso",
        )

    def update(self, payload: UpdateIsoRequest) -> APIResponse[Dict]:
        """Update properties of an ISO."""
        return self._execute(
            "updateIso",
            payload,
            envelope="updateisoresponse",
            entity="iso",
        )

    async def update_async(self, payload: UpdateIsoRequest) -> APIResponse[Dict]:
        """Asynchronously update properties of an ISO."""
        return await self._execute_async(
            "updateIso",
            payload,
            envelope="updateisoresponse",
            entity="iso",
        )

    def delete(self, payload: DeleteIsoRequest) -> APIResponse[Dict]:
        """Delete an ISO from the cloud. (async CloudStack operation)"""
        return self._execute(
            "deleteIso",
            payload,
            envelope="deleteisoresponse",
        )

    async def delete_async(self, payload: DeleteIsoRequest) -> APIResponse[Dict]:
        """Asynchronously delete an ISO from the cloud. (async CloudStack operation)"""
        return await self._execute_async(
            "deleteIso",
            payload,
            envelope="deleteisoresponse",
        )

    def update_permissions(self, payload: UpdateIsoPermissionsRequest) -> APIResponse[Dict]:
        """Update permissions for an ISO."""
        return self._execute(
            "updateIsoPermissions",
            payload,
            envelope="updateisopermissionsresponse",
        )

    async def update_permissions_async(self, payload: UpdateIsoPermissionsRequest) -> APIResponse[Dict]:
        """Asynchronously update permissions for an ISO."""
        return await self._execute_async(
            "updateIsoPermissions",
            payload,
            envelope="updateisopermissionsresponse",
        )

    # -------------------------------------------------------------------------
    # Attach / detach
    # -------------------------------------------------------------------------

    def attach(self, payload: AttachIsoRequest) -> APIResponse[Dict]:
        """Attach an ISO to a virtual machine. (async CloudStack operation)"""
        return self._execute(
            "attachIso",
            payload,
            envelope="attachisoresponse",
            entity="virtualmachine",
        )

    async def attach_async(self, payload: AttachIsoRequest) -> APIResponse[Dict]:
        """Asynchronously attach an ISO to a virtual machine. (async CloudStack operation)"""
        return await self._execute_async(
            "attachIso",
            payload,
            envelope="attachisoresponse",
            entity="virtualmachine",
        )

    def detach(self, payload: DetachIsoRequest) -> APIResponse[Dict]:
        """Detach any ISO file (if any) currently attached to a virtual machine. (async CloudStack operation)"""
        return self._execute(
            "detachIso",
            payload,
            envelope="detachisoresponse",
            entity="virtualmachine",
        )

    async def detach_async(self, payload: DetachIsoRequest) -> APIResponse[Dict]:
        """Asynchronously detach any ISO file currently attached to a virtual machine. (async CloudStack operation)"""
        return await self._execute_async(
            "detachIso",
            payload,
            envelope="detachisoresponse",
            entity="virtualmachine",
        )

    # -------------------------------------------------------------------------
    # Copy / extract / upload
    # -------------------------------------------------------------------------

    def copy(self, payload: CopyIsoRequest) -> APIResponse[Dict]:
        """Copy an ISO from one zone to one or more other zones. (async CloudStack operation)"""
        return self._execute(
            "copyIso",
            payload,
            envelope="copyisoresponse",
            entity="template",
        )

    async def copy_async(self, payload: CopyIsoRequest) -> APIResponse[Dict]:
        """Asynchronously copy an ISO from one zone to one or more other zones. (async CloudStack operation)"""
        return await self._execute_async(
            "copyIso",
            payload,
            envelope="copyisoresponse",
            entity="template",
        )

    def extract(self, payload: ExtractIsoRequest) -> APIResponse[Dict]:
        """Extract an ISO to a download URL. (async CloudStack operation)"""
        return self._execute(
            "extractIso",
            payload,
            envelope="extractisoresponse",
            entity="template",
        )

    async def extract_async(self, payload: ExtractIsoRequest) -> APIResponse[Dict]:
        """Asynchronously extract an ISO to a download URL. (async CloudStack operation)"""
        return await self._execute_async(
            "extractIso",
            payload,
            envelope="extractisoresponse",
            entity="template",
        )

    def get_upload_params(self, payload: GetUploadParamsForIsoRequest) -> APIResponse[Dict]:
        """Retrieve upload parameters for registering an ISO via direct upload."""
        return self._execute(
            "getUploadParamsForIso",
            payload,
            envelope="getuploadparamsforisoresponse",
            entity="getuploadparams",
        )

    async def get_upload_params_async(self, payload: GetUploadParamsForIsoRequest) -> APIResponse[Dict]:
        """Asynchronously retrieve upload parameters for registering an ISO via direct upload."""
        return await self._execute_async(
            "getUploadParamsForIso",
            payload,
            envelope="getuploadparamsforisoresponse",
            entity="getuploadparams",
        )
