# services/job.py
from typing import Dict, List

from acs_sdk.schemas.request.account import (
    CreateAccountRequest,
    EnableAccountRequest,
    DisableAccountRequest,
    ListAccountsRequest,
    LockAccountRequest,
    MarkDefaultZoneForAccountRequest,
    UpdateAccountRequest,
    DeleteAccountRequest,
    IsAccountAllowedToCreateOfferingsWithTagsRequest,
)

from .base import BaseService
from ..schemas.response.base import APIResponse


class Account(BaseService):
    def create_account(self, payload: CreateAccountRequest) -> APIResponse[Dict]:
        """Creates a new account."""
        return self._execute(
            "createAccount",
            payload,
            envelope="createaccountresponse",
        )

    async def create_account_async(self, payload: CreateAccountRequest) -> APIResponse[Dict]:
        """Creates a new account."""
        return await self._execute_async(
            "createAccount",
            payload,
            envelope="createaccountresponse",
        )

    def list(self, payload: ListAccountsRequest) -> APIResponse[List[Dict]]:
        """List accounts in CloudStack."""
        return self._execute(
            "listAccounts",
            payload,
            envelope="listaccountsresponse",
            entity="account",
        )

    async def list_async(self, payload: ListAccountsRequest) -> APIResponse[List[Dict]]:
        """Asynchronously list accounts in CloudStack."""
        return await self._execute_async(
            "listAccounts",
            payload,
            envelope="listaccountsresponse",
            entity="account",
        )

    def delete_account(self, payload: DeleteAccountRequest) -> APIResponse[Dict]:
        """Deletes an account."""
        return self._execute(
            "deleteAccount",
            payload,
            envelope="deleteaccountresponse",
        )

    async def delete_account_async(self, payload: DeleteAccountRequest) -> APIResponse[Dict]:
        """Deletes an account."""
        return await self._execute_async(
            "deleteAccount",
            payload,
            envelope="deleteaccountresponse",
        )

    def disable_account(self, payload: DisableAccountRequest) -> APIResponse[Dict]:
        """Disables an account."""
        return self._execute(
            "disableAccount",
            payload,
            envelope="disableaccountresponse",
        )

    async def disable_account_async(self, payload: DisableAccountRequest) -> APIResponse[Dict]:
        """Disables an account."""
        return await self._execute_async(
            "disableAccount",
            payload,
            envelope="disableaccountresponse",
        )

    def enable_account(self, payload: EnableAccountRequest) -> APIResponse[Dict]:
        """Enables an account."""
        return self._execute(
            "enableAccount",
            payload,
            envelope="enableaccountresponse",
        )

    async def enable_account_async(self, payload: EnableAccountRequest) -> APIResponse[Dict]:
        """Enables an account."""
        return await self._execute_async(
            "enableAccount",
            payload,
            envelope="enableaccountresponse",
        )

    def is_account_allowed_to_create_offerings_with_tags(
        self, payload: IsAccountAllowedToCreateOfferingsWithTagsRequest
    ) -> APIResponse[Dict]:
        """Checks if an account is allowed to create offerings with tags."""
        return self._execute(
            "isAccountAllowedToCreateOfferingsWithTags",
            payload,
            envelope="isaccountallowedtocreateofferingswithtagsresponse",
        )

    async def is_account_allowed_to_create_offerings_with_tags_async(
        self, payload: IsAccountAllowedToCreateOfferingsWithTagsRequest
    ) -> APIResponse[Dict]:
        """Checks if an account is allowed to create offerings with tags."""
        return await self._execute_async(
            "isAccountAllowedToCreateOfferingsWithTags",
            payload,
            envelope="isaccountallowedtocreateofferingswithtagsresponse",
        )

    def mark_default_zone_for_account(
        self, payload: MarkDefaultZoneForAccountRequest
    ) -> APIResponse[Dict]:
        """Marks the default zone for an account."""
        return self._execute(
            "markDefaultZoneForAccount",
            payload,
            envelope="markdefaultzoneforaccountresponse",
        )

    async def mark_default_zone_for_account_async(
        self, payload: MarkDefaultZoneForAccountRequest
    ) -> APIResponse[Dict]:
        """Marks the default zone for an account."""
        return await self._execute_async(
            "markDefaultZoneForAccount",
            payload,
            envelope="markdefaultzoneforaccountresponse",
        )

    def update_account(self, payload: UpdateAccountRequest) -> APIResponse[Dict]:
        """Updates an account."""
        return self._execute(
            "updateAccount",
            payload,
            envelope="updateaccountresponse",
        )

    async def update_account_async(self, payload: UpdateAccountRequest) -> APIResponse[Dict]:
        """Updates an account."""
        return await self._execute_async(
            "updateAccount",
            payload,
            envelope="updateaccountresponse",
        )

    def lock_account(self, payload: LockAccountRequest) -> APIResponse[Dict]:
        """Locks an account."""
        return self._execute(
            "lockAccount",
            payload,
            envelope="lockaccountresponse",
        )

    async def lock_account_async(self, payload: LockAccountRequest) -> APIResponse[Dict]:
        """Locks an account."""
        return await self._execute_async(
            "lockAccount",
            payload,
            envelope="lockaccountresponse",
        )
