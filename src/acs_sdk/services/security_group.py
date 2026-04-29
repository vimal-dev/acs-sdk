# services/security_group.py
from typing import Dict, List

from acs_sdk.schemas.request.security_group import (
    AuthorizeSecurityGroupEgressRequest,
    AuthorizeSecurityGroupIngressRequest,
    CreateSecurityGroupRequest,
    DeleteSecurityGroupRequest,
    ListSecurityGroupRequest,
    RevokeSecurityGroupEgressRequest,
    RevokeSecurityGroupIngressRequest,
    UpdateSecurityGroupRequest,
)

from .base import BaseService
from ..schemas.response.base import APIResponse


class SecurityGroup(BaseService):
    def list(self, payload: ListSecurityGroupRequest) -> APIResponse[List[Dict]]:
        """List all available security groups."""
        return self._execute(
            "listSecurityGroups",
            payload,
            envelope="listsecuritygroupsresponse",
            entity="securitygroup",
        )

    async def list_async(self, payload: ListSecurityGroupRequest) -> APIResponse[List[Dict]]:
        """Asynchronously list all available security groups."""
        return await self._execute_async(
            "listSecurityGroups",
            payload,
            envelope="listsecuritygroupsresponse",
            entity="securitygroup",
        )

    def create(self, payload: CreateSecurityGroupRequest) -> APIResponse[Dict]:
        """Create a security group."""
        return self._execute(
            "createSecurityGroup",
            payload,
            envelope="createsecuritygroupresponse",
        )

    async def create_async(self, payload: CreateSecurityGroupRequest) -> APIResponse[Dict]:
        """Asynchronously create a security group."""
        return await self._execute_async(
            "createSecurityGroup",
            payload,
            envelope="createsecuritygroupresponse",
        )

    def update(self, payload: UpdateSecurityGroupRequest) -> APIResponse[Dict]:
        """Update a security group."""
        return self._execute(
            "updateSecurityGroup",
            payload,
            envelope="updatesecuritygroupresponse",
        )

    async def update_async(self, payload: UpdateSecurityGroupRequest) -> APIResponse[Dict]:
        """Asynchronously update a security group."""
        return await self._execute_async(
            "updateSecurityGroup",
            payload,
            envelope="updatesecuritygroupresponse",
        )

    def delete(self, payload: DeleteSecurityGroupRequest) -> APIResponse[Dict]:
        """Delete a security group."""
        return self._execute(
            "deleteSecurityGroup",
            payload,
            envelope="deletesecuritygroupresponse",
        )

    async def delete_async(self, payload: DeleteSecurityGroupRequest) -> APIResponse[Dict]:
        """Asynchronously delete a security group."""
        return await self._execute_async(
            "deleteSecurityGroup",
            payload,
            envelope="deletesecuritygroupresponse",
        )

    def authorize_ingress(self, payload: AuthorizeSecurityGroupIngressRequest) -> APIResponse[Dict]:
        """Authorize ingress rule for a security group."""
        return self._execute(
            "authorizeSecurityGroupIngress",
            payload,
            envelope="authorizesecuritygroupingressresponse",
        )

    async def authorize_ingress_async(
        self, payload: AuthorizeSecurityGroupIngressRequest
    ) -> APIResponse[Dict]:
        """Asynchronously authorize ingress rule for a security group."""
        return await self._execute_async(
            "authorizeSecurityGroupIngress",
            payload,
            envelope="authorizesecuritygroupingressresponse",
        )

    def authorize_egress(self, payload: AuthorizeSecurityGroupEgressRequest) -> APIResponse[Dict]:
        """Authorize egress rule for a security group."""
        return self._execute(
            "authorizeSecurityGroupEgress",
            payload,
            envelope="authorizesecuritygroupegressresponse",
        )

    async def authorize_egress_async(
        self, payload: AuthorizeSecurityGroupEgressRequest
    ) -> APIResponse[Dict]:
        """Asynchronously authorize egress rule for a security group."""
        return await self._execute_async(
            "authorizeSecurityGroupEgress",
            payload,
            envelope="authorizesecuritygroupegressresponse",
        )

    def revoke_ingress(self, payload: RevokeSecurityGroupIngressRequest) -> APIResponse[Dict]:
        """Revoke ingress rule from a security group."""
        return self._execute(
            "revokeSecurityGroupIngress",
            payload,
            envelope="revokesecuritygroupingressresponse",
        )

    async def revoke_ingress_async(
        self, payload: RevokeSecurityGroupIngressRequest
    ) -> APIResponse[Dict]:
        """Asynchronously revoke ingress rule from a security group."""
        return await self._execute_async(
            "revokeSecurityGroupIngress",
            payload,
            envelope="revokesecuritygroupingressresponse",
        )

    def revoke_egress(self, payload: RevokeSecurityGroupEgressRequest) -> APIResponse[Dict]:
        """Revoke egress rule from a security group."""
        return self._execute(
            "revokeSecurityGroupEgress",
            payload,
            envelope="revokesecuritygroupegressresponse",
        )

    async def revoke_egress_async(
        self, payload: RevokeSecurityGroupEgressRequest
    ) -> APIResponse[Dict]:
        """Asynchronously revoke egress rule from a security group."""
        return await self._execute_async(
            "revokeSecurityGroupEgress",
            payload,
            envelope="revokesecuritygroupegressresponse",
        )
