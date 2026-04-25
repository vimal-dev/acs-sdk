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
        response = self.client.call("createNetworkACL", payload.model_dump(exclude_none=True))
        data = {}
        if 'createnetworkaclresponse' in response:
            data = response['createnetworkaclresponse']
        return APIResponse[Dict](**{"data": data})

    async def create_async(self, payload: CreateNetworkACLRequest) -> APIResponse[Dict]:
        """Asynchronously create a network ACL rule."""
        response = await self.client.call_async("createNetworkACL", payload.model_dump(exclude_none=True))
        data = {}
        if 'createnetworkaclresponse' in response:
            data = response['createnetworkaclresponse']
        return APIResponse[Dict](**{"data": data})

    def create_acl_list(self, payload: CreateNetworkACLListRequest) -> APIResponse[Dict]:
        """Create a network ACL list."""
        response = self.client.call("createNetworkACLList", payload.model_dump(exclude_none=True))
        data = {}
        if 'createnetworkacllistresponse' in response:
            data = response['createnetworkacllistresponse']
        return APIResponse[Dict](**{"data": data})

    async def create_acl_list_async(self, payload: CreateNetworkACLListRequest) -> APIResponse[Dict]:
        """Asynchronously create a network ACL list."""
        response = await self.client.call_async("createNetworkACLList", payload.model_dump(exclude_none=True))
        data = {}
        if 'createnetworkacllistresponse' in response:
            data = response['createnetworkacllistresponse']
        return APIResponse[Dict](**{"data": data})

    # Delete operations

    def delete(self, payload: DeleteNetworkACLRequest) -> APIResponse[Dict]:
        """Delete a network ACL rule."""
        response = self.client.call("deleteNetworkACL", payload.model_dump(exclude_none=True))
        data = {}
        if 'deletenetworkaclresponse' in response:
            data = response['deletenetworkaclresponse']
        return APIResponse[Dict](**{"data": data})

    async def delete_async(self, payload: DeleteNetworkACLRequest) -> APIResponse[Dict]:
        """Asynchronously delete a network ACL rule."""
        response = await self.client.call_async("deleteNetworkACL", payload.model_dump(exclude_none=True))
        data = {}
        if 'deletenetworkaclresponse' in response:
            data = response['deletenetworkaclresponse']
        return APIResponse[Dict](**{"data": data})

    def delete_acl_list(self, payload: DeleteNetworkACLListRequest) -> APIResponse[Dict]:
        """Delete a network ACL list."""
        response = self.client.call("deleteNetworkACLList", payload.model_dump(exclude_none=True))
        data = {}
        if 'deletenetworkacllistresponse' in response:
            data = response['deletenetworkacllistresponse']
        return APIResponse[Dict](**{"data": data})

    async def delete_acl_list_async(self, payload: DeleteNetworkACLListRequest) -> APIResponse[Dict]:
        """Asynchronously delete a network ACL list."""
        response = await self.client.call_async("deleteNetworkACLList", payload.model_dump(exclude_none=True))
        data = {}
        if 'deletenetworkacllistresponse' in response:
            data = response['deletenetworkacllistresponse']
        return APIResponse[Dict](**{"data": data})

    # List operations

    def list_acl_lists(self, payload: ListNetworkACLListsRequest) -> APIResponse[List[Dict]]:
        """List network ACL lists."""
        response = self.client.call("listNetworkACLLists", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listnetworkacllistsresponse' in response:
            response = response['listnetworkacllistsresponse']
        if 'networkacllist' in response and response['networkacllist']:
            data = response['networkacllist']
            count = response.get('count', 0)
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    async def list_acl_lists_async(self, payload: ListNetworkACLListsRequest) -> APIResponse[List[Dict]]:
        """Asynchronously list network ACL lists."""
        response = await self.client.call_async("listNetworkACLLists", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listnetworkacllistsresponse' in response:
            response = response['listnetworkacllistsresponse']
        if 'networkacllist' in response and response['networkacllist']:
            data = response['networkacllist']
            count = response.get('count', 0)
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    def list(self, payload: ListNetworkACLsRequest) -> APIResponse[List[Dict]]:
        """List network ACL items."""
        response = self.client.call("listNetworkACLs", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listnetworkaclsresponse' in response:
            response = response['listnetworkaclsresponse']
        if 'networkacl' in response and response['networkacl']:
            data = response['networkacl']
            count = response.get('count', 0)
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    async def list_async(self, payload: ListNetworkACLsRequest) -> APIResponse[List[Dict]]:
        """Asynchronously list network ACL items."""
        response = await self.client.call_async("listNetworkACLs", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listnetworkaclsresponse' in response:
            response = response['listnetworkaclsresponse']
        if 'networkacl' in response and response['networkacl']:
            data = response['networkacl']
            count = response.get('count', 0)
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    # Move operation

    def move_acl_item(self, payload: MoveNetworkAclItemRequest) -> APIResponse[Dict]:
        """Move a network ACL item to a new position."""
        response = self.client.call("moveNetworkAclItem", payload.model_dump(exclude_none=True))
        data = {}
        if 'movenetworkaclitemresponse' in response:
            data = response['movenetworkaclitemresponse']
        return APIResponse[Dict](**{"data": data})

    async def move_acl_item_async(self, payload: MoveNetworkAclItemRequest) -> APIResponse[Dict]:
        """Asynchronously move a network ACL item to a new position."""
        response = await self.client.call_async("moveNetworkAclItem", payload.model_dump(exclude_none=True))
        data = {}
        if 'movenetworkaclitemresponse' in response:
            data = response['movenetworkaclitemresponse']
        return APIResponse[Dict](**{"data": data})

    # Replace operation

    def replace_acl_list(self, payload: ReplaceNetworkACLListRequest) -> APIResponse[Dict]:
        """Replace ACL associated with a network or private gateway."""
        response = self.client.call("replaceNetworkACLList", payload.model_dump(exclude_none=True))
        data = {}
        if 'replacenetworkacllistresponse' in response:
            data = response['replacenetworkacllistresponse']
        return APIResponse[Dict](**{"data": data})

    async def replace_acl_list_async(self, payload: ReplaceNetworkACLListRequest) -> APIResponse[Dict]:
        """Asynchronously replace ACL associated with a network or private gateway."""
        response = await self.client.call_async("replaceNetworkACLList", payload.model_dump(exclude_none=True))
        data = {}
        if 'replacenetworkacllistresponse' in response:
            data = response['replacenetworkacllistresponse']
        return APIResponse[Dict](**{"data": data})

    # Update operations

    def update_acl_item(self, payload: UpdateNetworkACLItemRequest) -> APIResponse[Dict]:
        """Update a network ACL item."""
        response = self.client.call("updateNetworkACLItem", payload.model_dump(exclude_none=True))
        data = {}
        if 'updatenetworkaclitemresponse' in response:
            data = response['updatenetworkaclitemresponse']
        return APIResponse[Dict](**{"data": data})

    async def update_acl_item_async(self, payload: UpdateNetworkACLItemRequest) -> APIResponse[Dict]:
        """Asynchronously update a network ACL item."""
        response = await self.client.call_async("updateNetworkACLItem", payload.model_dump(exclude_none=True))
        data = {}
        if 'updatenetworkaclitemresponse' in response:
            data = response['updatenetworkaclitemresponse']
        return APIResponse[Dict](**{"data": data})

    def update_acl_list(self, payload: UpdateNetworkACLListRequest) -> APIResponse[Dict]:
        """Update a network ACL list."""
        response = self.client.call("updateNetworkACLList", payload.model_dump(exclude_none=True))
        data = {}
        if 'updatenetworkacllistresponse' in response:
            data = response['updatenetworkacllistresponse']
        return APIResponse[Dict](**{"data": data})

    async def update_acl_list_async(self, payload: UpdateNetworkACLListRequest) -> APIResponse[Dict]:
        """Asynchronously update a network ACL list."""
        response = await self.client.call_async("updateNetworkACLList", payload.model_dump(exclude_none=True))
        data = {}
        if 'updatenetworkacllistresponse' in response:
            data = response['updatenetworkacllistresponse']
        return APIResponse[Dict](**{"data": data})
