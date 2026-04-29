# services/network_acl.py
from typing import Dict, List

from acs_sdk.schemas.request.network_acl import (
    CreateNetworkACLRequest,
    CreateNetworkACLListRequest,
    DeleteNetworkACLRequest,
    DeleteNetworkACLListRequest,
    ListNetworkACLListsRequest,
    ListNetworkACLsRequest,
    MoveNetworkAclItemRequest,
    ReplaceNetworkACLListRequest,
    UpdateNetworkACLItemRequest,
    UpdateNetworkACLListRequest,
)

from .base import BaseService
from ..schemas.response.base import APIResponse


class NetworkACL(BaseService):
    """Service for CloudStack Network ACL operations."""

    # Create operations

    def create(self, payload: CreateNetworkACLRequest) -> APIResponse[Dict]:
        """Create a network ACL rule."""
        return self._execute(
            "createNetworkACL",
            payload,
            envelope="createnetworkaclresponse",
        )

    async def create_async(self, payload: CreateNetworkACLRequest) -> APIResponse[Dict]:
        """Asynchronously create a network ACL rule."""
        return await self._execute_async(
            "createNetworkACL",
            payload,
            envelope="createnetworkaclresponse",
        )

    def create_acl_list(self, payload: CreateNetworkACLListRequest) -> APIResponse[Dict]:
        """Create a network ACL list."""
        return self._execute(
            "createNetworkACLList",
            payload,
            envelope="createnetworkacllistresponse",
        )

    async def create_acl_list_async(
        self, payload: CreateNetworkACLListRequest
    ) -> APIResponse[Dict]:
        """Asynchronously create a network ACL list."""
        return await self._execute_async(
            "createNetworkACLList",
            payload,
            envelope="createnetworkacllistresponse",
        )

    # Delete operations

    def delete(self, payload: DeleteNetworkACLRequest) -> APIResponse[Dict]:
        """Delete a network ACL rule."""
        return self._execute(
            "deleteNetworkACL",
            payload,
            envelope="deletenetworkaclresponse",
        )

    async def delete_async(self, payload: DeleteNetworkACLRequest) -> APIResponse[Dict]:
        """Asynchronously delete a network ACL rule."""
        return await self._execute_async(
            "deleteNetworkACL",
            payload,
            envelope="deletenetworkaclresponse",
        )

    def delete_acl_list(self, payload: DeleteNetworkACLListRequest) -> APIResponse[Dict]:
        """Delete a network ACL list."""
        return self._execute(
            "deleteNetworkACLList",
            payload,
            envelope="deletenetworkacllistresponse",
        )

    async def delete_acl_list_async(
        self, payload: DeleteNetworkACLListRequest
    ) -> APIResponse[Dict]:
        """Asynchronously delete a network ACL list."""
        return await self._execute_async(
            "deleteNetworkACLList",
            payload,
            envelope="deletenetworkacllistresponse",
        )

    # List operations

    def list_acl_lists(self, payload: ListNetworkACLListsRequest) -> APIResponse[List[Dict]]:
        """List network ACL lists."""
        return self._execute(
            "listNetworkACLLists",
            payload,
            envelope="listnetworkacllistsresponse",
            entity="networkacllist",
        )

    async def list_acl_lists_async(
        self, payload: ListNetworkACLListsRequest
    ) -> APIResponse[List[Dict]]:
        """Asynchronously list network ACL lists."""
        return await self._execute_async(
            "listNetworkACLLists",
            payload,
            envelope="listnetworkacllistsresponse",
            entity="networkacllist",
        )

    def list(self, payload: ListNetworkACLsRequest) -> APIResponse[List[Dict]]:
        """List network ACL items."""
        return self._execute(
            "listNetworkACLs",
            payload,
            envelope="listnetworkaclsresponse",
            entity="networkacl",
        )

    async def list_async(self, payload: ListNetworkACLsRequest) -> APIResponse[List[Dict]]:
        """Asynchronously list network ACL items."""
        return await self._execute_async(
            "listNetworkACLs",
            payload,
            envelope="listnetworkaclsresponse",
            entity="networkacl",
        )

    # Move operation

    def move_acl_item(self, payload: MoveNetworkAclItemRequest) -> APIResponse[Dict]:
        """Move a network ACL item to a new position."""
        return self._execute(
            "moveNetworkAclItem",
            payload,
            envelope="movenetworkaclitemresponse",
        )

    async def move_acl_item_async(self, payload: MoveNetworkAclItemRequest) -> APIResponse[Dict]:
        """Asynchronously move a network ACL item to a new position."""
        return await self._execute_async(
            "moveNetworkAclItem",
            payload,
            envelope="movenetworkaclitemresponse",
        )

    # Replace operation

    def replace_acl_list(self, payload: ReplaceNetworkACLListRequest) -> APIResponse[Dict]:
        """Replace ACL associated with a network or private gateway."""
        return self._execute(
            "replaceNetworkACLList",
            payload,
            envelope="replacenetworkacllistresponse",
        )

    async def replace_acl_list_async(
        self, payload: ReplaceNetworkACLListRequest
    ) -> APIResponse[Dict]:
        """Asynchronously replace ACL associated with a network or private gateway."""
        return await self._execute_async(
            "replaceNetworkACLList",
            payload,
            envelope="replacenetworkacllistresponse",
        )

    # Update operations

    def update_acl_item(self, payload: UpdateNetworkACLItemRequest) -> APIResponse[Dict]:
        """Update a network ACL item."""
        return self._execute(
            "updateNetworkACLItem",
            payload,
            envelope="updatenetworkaclitemresponse",
        )

    async def update_acl_item_async(
        self, payload: UpdateNetworkACLItemRequest
    ) -> APIResponse[Dict]:
        """Asynchronously update a network ACL item."""
        return await self._execute_async(
            "updateNetworkACLItem",
            payload,
            envelope="updatenetworkaclitemresponse",
        )

    def update_acl_list(self, payload: UpdateNetworkACLListRequest) -> APIResponse[Dict]:
        """Update a network ACL list."""
        return self._execute(
            "updateNetworkACLList",
            payload,
            envelope="updatenetworkacllistresponse",
        )

    async def update_acl_list_async(
        self, payload: UpdateNetworkACLListRequest
    ) -> APIResponse[Dict]:
        """Asynchronously update a network ACL list."""
        return await self._execute_async(
            "updateNetworkACLList",
            payload,
            envelope="updatenetworkacllistresponse",
        )
