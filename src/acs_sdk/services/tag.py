# services/tag.py
from typing import Dict, List

from acs_sdk.schemas.request.tag import (
    CreateTagsRequest,
    DeleteTagsRequest,
    ListStorageTagsRequest,
    ListTagsRequest,
)

from .base import BaseService
from ..schemas.response.base import APIResponse


class Tag(BaseService):
    def create(self, payload: CreateTagsRequest) -> APIResponse[Dict]:
        """Create tags for a resource."""
        return self._execute(
            "createTags",
            payload,
            envelope="createtagsresponse",
        )

    async def create_async(self, payload: CreateTagsRequest) -> APIResponse[Dict]:
        """Asynchronously create tags for a resource."""
        return await self._execute_async(
            "createTags",
            payload,
            envelope="createtagsresponse",
        )

    def delete(self, payload: DeleteTagsRequest) -> APIResponse[Dict]:
        """Delete tags from a resource."""
        return self._execute(
            "deleteTags",
            payload,
            envelope="deletetagsresponse",
        )

    async def delete_async(self, payload: DeleteTagsRequest) -> APIResponse[Dict]:
        """Asynchronously delete tags from a resource."""
        return await self._execute_async(
            "deleteTags",
            payload,
            envelope="deletetagsresponse",
        )

    def list_storage_tags(self, payload: ListStorageTagsRequest) -> APIResponse[List[Dict]]:
        """List storage tags."""
        return self._execute(
            "listStorageTags",
            payload,
            envelope="liststoragetagsresponse",
            entity="storagetag",
        )

    async def list_storage_tags_async(
        self, payload: ListStorageTagsRequest
    ) -> APIResponse[List[Dict]]:
        """Asynchronously list storage tags."""
        return await self._execute_async(
            "listStorageTags",
            payload,
            envelope="liststoragetagsresponse",
            entity="storagetag",
        )

    def list(self, payload: ListTagsRequest) -> APIResponse[List[Dict]]:
        """List resource tags."""
        return self._execute(
            "listTags",
            payload,
            envelope="listtagsresponse",
            entity="tag",
        )

    async def list_async(self, payload: ListTagsRequest) -> APIResponse[List[Dict]]:
        """Asynchronously list resource tags."""
        return await self._execute_async(
            "listTags",
            payload,
            envelope="listtagsresponse",
            entity="tag",
        )
