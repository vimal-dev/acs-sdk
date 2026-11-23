# services/template.py
from typing import Dict, List

from ..schemas.request.template import (
    CopyTemplateRequest,
    CreateTemplateRequest,
    DeleteTemplateRequest,
    ExtractTemplateRequest,
    GetUploadParamsForTemplateRequest,
    ListTemplatePermissionsRequest,
    ListTemplatesRequest,
    PrepareTemplateRequest,
    RegisterTemplateRequest,
    UpdateTemplatePermissionsRequest,
    UpdateTemplateRequest,
)

from .base import BaseService
from ..schemas.response.base import APIResponse


class Template(BaseService):
    """Service class for managing templates in Apache CloudStack."""

    # -------------------------------------------------------------------------
    # Query / list
    # -------------------------------------------------------------------------

    def list(self, payload: ListTemplatesRequest) -> APIResponse[List[Dict]]:
        """List all public, private, and privileged templates based on the specified filters."""
        return self._execute(
            "listTemplates",
            payload,
            envelope="listtemplatesresponse",
            entity="template",
        )

    async def list_async(self, payload: ListTemplatesRequest) -> APIResponse[List[Dict]]:
        """List all public, private, and privileged templates based on the specified filters."""
        return await self._execute_async(
            "listTemplates",
            payload,
            envelope="listtemplatesresponse",
            entity="template",
        )

    def list_permissions(self, payload: ListTemplatePermissionsRequest) -> APIResponse[Dict]:
        """List permission details for a template."""
        return self._execute(
            "listTemplatePermissions",
            payload,
            envelope="listtemplatepermissionsresponse",
            entity="templatepermission",
        )

    async def list_permissions_async(
        self, payload: ListTemplatePermissionsRequest
    ) -> APIResponse[Dict]:
        """Asynchronously list permission details for a template."""
        return await self._execute_async(
            "listTemplatePermissions",
            payload,
            envelope="listtemplatepermissionsresponse",
            entity="templatepermission",
        )

    # -------------------------------------------------------------------------
    # Register / create / update / delete
    # -------------------------------------------------------------------------

    def register(self, payload: RegisterTemplateRequest) -> APIResponse[List[Dict]]:
        """Register an existing template into the CloudStack cloud."""
        return self._execute(
            "registerTemplate",
            payload,
            envelope="registertemplateresponse",
            entity="template",
        )

    async def register_async(self, payload: RegisterTemplateRequest) -> APIResponse[List[Dict]]:
        """Asynchronously register an existing template into the CloudStack cloud."""
        return await self._execute_async(
            "registerTemplate",
            payload,
            envelope="registertemplateresponse",
            entity="template",
        )

    def create(self, payload: CreateTemplateRequest) -> APIResponse[Dict]:
        """Create a template from a volume or snapshot. (async CloudStack operation)"""
        return self._execute(
            "createTemplate",
            payload,
            envelope="createtemplateresponse",
        )

    async def create_async(self, payload: CreateTemplateRequest) -> APIResponse[Dict]:
        """Asynchronously create a template from a volume or snapshot. (async CloudStack operation)"""
        return await self._execute_async(
            "createTemplate",
            payload,
            envelope="createtemplateresponse",
        )

    def update(self, payload: UpdateTemplateRequest) -> APIResponse[Dict]:
        """Update attributes of a template."""
        return self._execute(
            "updateTemplate",
            payload,
            envelope="updatetemplateresponse",
            entity="template",
        )

    async def update_async(self, payload: UpdateTemplateRequest) -> APIResponse[Dict]:
        """Asynchronously update attributes of a template."""
        return await self._execute_async(
            "updateTemplate",
            payload,
            envelope="updatetemplateresponse",
            entity="template",
        )

    def delete(self, payload: DeleteTemplateRequest) -> APIResponse[Dict]:
        """Delete a template from the system. (async CloudStack operation)"""
        return self._execute(
            "deleteTemplate",
            payload,
            envelope="deletetemplateresponse",
        )

    async def delete_async(self, payload: DeleteTemplateRequest) -> APIResponse[Dict]:
        """Asynchronously delete a template from the system. (async CloudStack operation)"""
        return await self._execute_async(
            "deleteTemplate",
            payload,
            envelope="deletetemplateresponse",
        )

    def update_permissions(self, payload: UpdateTemplatePermissionsRequest) -> APIResponse[Dict]:
        """Update permissions for a template."""
        return self._execute(
            "updateTemplatePermissions",
            payload,
            envelope="updatetemplatepermissionsresponse",
        )

    async def update_permissions_async(
        self, payload: UpdateTemplatePermissionsRequest
    ) -> APIResponse[Dict]:
        """Asynchronously update permissions for a template."""
        return await self._execute_async(
            "updateTemplatePermissions",
            payload,
            envelope="updatetemplatepermissionsresponse",
        )

    # -------------------------------------------------------------------------
    # Copy / extract / upload / prepare
    # -------------------------------------------------------------------------

    def copy(self, payload: CopyTemplateRequest) -> APIResponse[Dict]:
        """Copy a template from one zone to one or more other zones. (async CloudStack operation)"""
        return self._execute(
            "copyTemplate",
            payload,
            envelope="copytemplateresponse",
            entity="template",
        )

    async def copy_async(self, payload: CopyTemplateRequest) -> APIResponse[Dict]:
        """Asynchronously copy a template from one zone to one or more other zones. (async CloudStack operation)"""
        return await self._execute_async(
            "copyTemplate",
            payload,
            envelope="copytemplateresponse",
            entity="template",
        )

    def extract(self, payload: ExtractTemplateRequest) -> APIResponse[Dict]:
        """Extract a template to a download URL. (async CloudStack operation)"""
        return self._execute(
            "extractTemplate",
            payload,
            envelope="extracttemplateresponse",
            entity="template",
        )

    async def extract_async(self, payload: ExtractTemplateRequest) -> APIResponse[Dict]:
        """Asynchronously extract a template to a download URL. (async CloudStack operation)"""
        return await self._execute_async(
            "extractTemplate",
            payload,
            envelope="extracttemplateresponse",
            entity="template",
        )

    def get_upload_params(self, payload: GetUploadParamsForTemplateRequest) -> APIResponse[Dict]:
        """Retrieve upload parameters for registering a template via direct upload."""
        return self._execute(
            "getUploadParamsForTemplate",
            payload,
            envelope="getuploadparamsfortemplateresponse",
            entity="getuploadparams",
        )

    async def get_upload_params_async(
        self, payload: GetUploadParamsForTemplateRequest
    ) -> APIResponse[Dict]:
        """Asynchronously retrieve upload parameters for registering a template via direct upload."""
        return await self._execute_async(
            "getUploadParamsForTemplate",
            payload,
            envelope="getuploadparamsfortemplateresponse",
            entity="getuploadparams",
        )

    def prepare(self, payload: PrepareTemplateRequest) -> APIResponse[Dict]:
        """Load a template into primary storage."""
        return self._execute(
            "prepareTemplate",
            payload,
            envelope="preparetemplateresponse",
            entity="template",
        )

    async def prepare_async(self, payload: PrepareTemplateRequest) -> APIResponse[Dict]:
        """Asynchronously load a template into primary storage."""
        return await self._execute_async(
            "prepareTemplate",
            payload,
            envelope="preparetemplateresponse",
            entity="template",
        )
