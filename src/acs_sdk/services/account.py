# services/job.py
from typing import Dict

from acs_sdk.schemas.request.account import CreateAccountRequest, EnableAccountRequest, DisableAccountRequest, ListAccountsRequest, MarkDefaultZoneForAccountRequest, UpdateAccountRequest

from .base import BaseService
from ..schemas.response.base import APIResponse


class Account(BaseService):

    def create_account(self, payload: CreateAccountRequest) -> APIResponse[Dict]:
        """Creates a new account."""
        data = self.client.call("createAccount", payload.model_dump(exclude_none=True))
        return APIResponse[Dict](**data)

    async def create_account_async(self, payload: CreateAccountRequest) -> APIResponse[Dict]:
        """Creates a new account."""
        data = await self.client.call_async("createAccount", payload.model_dump(exclude_none=True))
        return APIResponse[Dict](**data)

    def list(self, payload: ListAccountsRequest) -> APIResponse[Dict]:
        """List accounts in CloudStack."""
        data = self.client.call("listAccounts", payload.model_dump(exclude_none=True))
        return APIResponse[Dict](**data)

    async def list_async(self, payload: ListAccountsRequest) -> APIResponse[Dict]:
        """Asynchronously list accounts in CloudStack."""
        data = await self.client.async_call("listAccounts", payload.model_dump(exclude_none=True))
        return APIResponse[Dict](**data)
    
    def delete_account(self, id: str) -> APIResponse[Dict]:
        """Deletes an account."""
        data = self.client.call("deleteAccount", {"id": id})
        return APIResponse[Dict](**data)

    async def delete_account_async(self, id: str) -> APIResponse[Dict]:
        """Deletes an account."""
        data = await self.client.call_async("deleteAccount", {"id": id})
        return APIResponse[Dict](**data)
    
    def disable_account(self, payload: DisableAccountRequest) -> APIResponse[Dict]:
        """Disables an account."""
        data = self.client.call("disableAccount", payload.model_dump(exclude_none=True))
        return APIResponse[Dict](**data)

    async def disable_account_async(self, payload: DisableAccountRequest) -> APIResponse[Dict]:
        """Disables an account."""
        data = await self.client.call_async("disableAccount", payload.model_dump(exclude_none=True))
        return APIResponse[Dict](**data)
    
    def enable_account(self, payload: EnableAccountRequest) -> APIResponse[Dict]:
        """Enables an account."""
        data = self.client.call("enableAccount", payload.model_dump(exclude_none=True))
        return APIResponse[Dict](**data)

    async def enable_account_async(self, payload: EnableAccountRequest) -> APIResponse[Dict]:
        """Enables an account."""
        data = await self.client.call_async("enableAccount", payload.model_dump(exclude_none=True))
        return APIResponse[Dict](**data)
    
    def is_account_allowed_to_create_offerings_with_tags(self, id: str) -> APIResponse[Dict]:
        """Checks if an account is allowed to create offerings with tags."""
        data = self.client.call("isAccountAllowedToCreateOfferingsWithTags", {"id": id})
        return APIResponse[Dict](**data)

    async def is_account_allowed_to_create_offerings_with_tags_async(self, id: str) -> APIResponse[Dict]:
        """Checks if an account is allowed to create offerings with tags."""
        data = await self.client.call_async("isAccountAllowedToCreateOfferingsWithTags", {"id": id})
        return APIResponse[Dict](**data)
    
    def mark_default_zone_for_account(self, payload: MarkDefaultZoneForAccountRequest) -> APIResponse[Dict]:
        """Marks the default zone for an account."""
        data = self.client.call("markDefaultZoneForAccount", payload.model_dump(exclude_none=True))
        return APIResponse[Dict](**data)

    async def mark_default_zone_for_account_async(self, payload: MarkDefaultZoneForAccountRequest) -> APIResponse[Dict]:
        """Marks the default zone for an account."""
        data = await self.client.call_async("markDefaultZoneForAccount", payload.model_dump(exclude_none=True))
        return APIResponse[Dict](**data)
    
    def update_account(self, payload: UpdateAccountRequest) -> APIResponse[Dict]:
        """Updates an account."""
        data = self.client.call("updateAccount", payload.model_dump(exclude_none=True))
        return APIResponse[Dict](**data)

    async def update_account_async(self, payload: UpdateAccountRequest) -> APIResponse[Dict]:
        """Updates an account."""
        data = await self.client.call_async("updateAccount", payload.model_dump(exclude_none=True))
        return APIResponse[Dict](**data)
