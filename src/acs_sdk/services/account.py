# services/job.py
from typing import Dict, List

from acs_sdk.schemas.request.account import CreateAccountRequest, EnableAccountRequest, DisableAccountRequest, ListAccountsRequest, MarkDefaultZoneForAccountRequest, UpdateAccountRequest

from .base import BaseService
from ..schemas.response.base import APIResponse


class Account(BaseService):

    def create_account(self, payload: CreateAccountRequest) -> APIResponse[Dict]:
        """Creates a new account."""
        response = self.client.call("createAccount", payload.model_dump(exclude_none=True))
        data = {}
        if 'createaccountresponse' in response:
            data = response['createaccountresponse']
        return APIResponse[Dict](**{"data": data})

    async def create_account_async(self, payload: CreateAccountRequest) -> APIResponse[Dict]:
        """Creates a new account."""
        response = await self.client.call_async("createAccount", payload.model_dump(exclude_none=True))
        data = {}
        if 'createaccountresponse' in response:
            data = response['createaccountresponse']
        return APIResponse[Dict](**{"data": data})

    def list(self, payload: ListAccountsRequest) -> APIResponse[List[Dict]]:
        """List accounts in CloudStack."""
        response = self.client.call("listAccounts", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listaccountsresponse' in response:
            response = response['listaccountsresponse']
        if 'account' in response and response['account']:
            data = response['account']
            count = response['count']
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    async def list_async(self, payload: ListAccountsRequest) -> APIResponse[List[Dict]]:
        """Asynchronously list accounts in CloudStack."""
        response = await self.client.async_call("listAccounts", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listaccountsresponse' in response:
            response = response['listaccountsresponse']
        if 'account' in response and response['account']:
            data = response['account']
            count = response['count']
        return APIResponse[List[Dict]](**{"data": data, "count": count})
    
    def delete_account(self, id: str) -> APIResponse[Dict]:
        """Deletes an account."""
        response = self.client.call("deleteAccount", {"id": id})
        data = {}
        if 'deleteaccountresponse' in response:
            data = response['deleteaccountresponse']
        return APIResponse[Dict](**{"data": data})

    async def delete_account_async(self, id: str) -> APIResponse[Dict]:
        """Deletes an account."""
        response = await self.client.call_async("deleteAccount", {"id": id})
        data = {}
        if 'deleteaccountresponse' in response:
            data = response['deleteaccountresponse']
        return APIResponse[Dict](**{"data": data})
    
    def disable_account(self, payload: DisableAccountRequest) -> APIResponse[Dict]:
        """Disables an account."""
        response = self.client.call("disableAccount", payload.model_dump(exclude_none=True))
        data = {}
        if 'disableaccountresponse' in response:
            data = response['disableaccountresponse']
        return APIResponse[Dict](**{"data": data})

    async def disable_account_async(self, payload: DisableAccountRequest) -> APIResponse[Dict]:
        """Disables an account."""
        response = await self.client.call_async("disableAccount", payload.model_dump(exclude_none=True))
        data = {}
        if 'disableaccountresponse' in response:
            data = response['disableaccountresponse']
        return APIResponse[Dict](**{"data": data})
    
    def enable_account(self, payload: EnableAccountRequest) -> APIResponse[Dict]:
        """Enables an account."""
        response = self.client.call("enableAccount", payload.model_dump(exclude_none=True))
        data = {}
        if 'enableaccountresponse' in response:
            data = response['enableaccountresponse']
        return APIResponse[Dict](**{"data": data})

    async def enable_account_async(self, payload: EnableAccountRequest) -> APIResponse[Dict]:
        """Enables an account."""
        response = await self.client.call_async("enableAccount", payload.model_dump(exclude_none=True))
        data = {}
        if 'enableaccountresponse' in response:
            data = response['enableaccountresponse']
        return APIResponse[Dict](**{"data": data})

    def is_account_allowed_to_create_offerings_with_tags(self, id: str) -> APIResponse[Dict]:
        """Checks if an account is allowed to create offerings with tags."""
        response = self.client.call("isAccountAllowedToCreateOfferingsWithTags", {"id": id})
        data = {}
        if 'isaccountallowedtocreateofferingswithtagsresponse' in response:
            data = response['isaccountallowedtocreateofferingswithtagsresponse']
        return APIResponse[Dict](**{"data": data})

    async def is_account_allowed_to_create_offerings_with_tags_async(self, id: str) -> APIResponse[Dict]:
        """Checks if an account is allowed to create offerings with tags."""
        response = await self.client.call_async("isAccountAllowedToCreateOfferingsWithTags", {"id": id})
        data = {}
        if 'isaccountallowedtocreateofferingswithtagsresponse' in response:
            data = response['isaccountallowedtocreateofferingswithtagsresponse']
        return APIResponse[Dict](**{"data": data})

    def mark_default_zone_for_account(self, payload: MarkDefaultZoneForAccountRequest) -> APIResponse[Dict]:
        """Marks the default zone for an account."""
        response = self.client.call("markDefaultZoneForAccount", payload.model_dump(exclude_none=True))
        data = {}
        if 'markdefaultzoneforaccountresponse' in response:
            data = response['markdefaultzoneforaccountresponse']
        return APIResponse[Dict](**{"data": data})

    async def mark_default_zone_for_account_async(self, payload: MarkDefaultZoneForAccountRequest) -> APIResponse[Dict]:
        """Marks the default zone for an account."""
        response = await self.client.call_async("markDefaultZoneForAccount", payload.model_dump(exclude_none=True))
        data = {}
        if 'markdefaultzoneforaccountresponse' in response:
            data = response['markdefaultzoneforaccountresponse']
        return APIResponse[Dict](**{"data": data})

    def update_account(self, payload: UpdateAccountRequest) -> APIResponse[Dict]:
        """Updates an account."""
        response = self.client.call("updateAccount", payload.model_dump(exclude_none=True))
        data = {}
        if 'updateaccountresponse' in response:
            data = response['updateaccountresponse']
        return APIResponse[Dict](**{"data": data})

    async def update_account_async(self, payload: UpdateAccountRequest) -> APIResponse[Dict]:
        """Updates an account."""
        response = await self.client.call_async("updateAccount", payload.model_dump(exclude_none=True))
        data = {}
        if 'updateaccountresponse' in response:
            data = response['updateaccountresponse']
        return APIResponse[Dict](**{"data": data})
