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
        response = self.client.call("listSecurityGroups", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listsecuritygroupsresponse' in response:
            response = response['listsecuritygroupsresponse']
        if 'securitygroup' in response and response['securitygroup']:
            data = response['securitygroup']
            count = response['count']
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    async def list_async(self, payload: ListSecurityGroupRequest) -> APIResponse[List[Dict]]:
        """Asynchronously list all available security groups."""
        response = await self.client.call_async("listSecurityGroups", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listsecuritygroupsresponse' in response:
            response = response['listsecuritygroupsresponse']
        if 'securitygroup' in response and response['securitygroup']:
            data = response['securitygroup']
            count = response['count']
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    def create(self, payload: CreateSecurityGroupRequest) -> APIResponse[Dict]:
        """Create a security group."""
        response = self.client.call("createSecurityGroup", payload.model_dump(exclude_none=True))
        data = {}
        if 'createsecuritygroupresponse' in response:
            data = response['createsecuritygroupresponse']
        return APIResponse[Dict](**{"data": data})

    async def create_async(self, payload: CreateSecurityGroupRequest) -> APIResponse[Dict]:
        """Asynchronously create a security group."""
        response = await self.client.call_async("createSecurityGroup", payload.model_dump(exclude_none=True))
        data = {}
        if 'createsecuritygroupresponse' in response:
            data = response['createsecuritygroupresponse']
        return APIResponse[Dict](**{"data": data})

    def update(self, payload: UpdateSecurityGroupRequest) -> APIResponse[Dict]:
        """Update a security group."""
        response = self.client.call("updateSecurityGroup", payload.model_dump(exclude_none=True))
        data = {}
        if 'updatesecuritygroupresponse' in response:
            data = response['updatesecuritygroupresponse']
        return APIResponse[Dict](**{"data": data})

    async def update_async(self, payload: UpdateSecurityGroupRequest) -> APIResponse[Dict]:
        """Asynchronously update a security group."""
        response = await self.client.call_async("updateSecurityGroup", payload.model_dump(exclude_none=True))
        data = {}
        if 'updatesecuritygroupresponse' in response:
            data = response['updatesecuritygroupresponse']
        return APIResponse[Dict](**{"data": data})

    def delete(self, payload: DeleteSecurityGroupRequest) -> APIResponse[Dict]:
        """Delete a security group."""
        response = self.client.call("deleteSecurityGroup", payload.model_dump(exclude_none=True))
        data = {}
        if 'deletesecuritygroupresponse' in response:
            data = response['deletesecuritygroupresponse']
        return APIResponse[Dict](**{"data": data})

    async def delete_async(self, payload: DeleteSecurityGroupRequest) -> APIResponse[Dict]:
        """Asynchronously delete a security group."""
        response = await self.client.call_async("deleteSecurityGroup", payload.model_dump(exclude_none=True))
        data = {}
        if 'deletesecuritygroupresponse' in response:
            data = response['deletesecuritygroupresponse']
        return APIResponse[Dict](**{"data": data})

    def authorize_ingress(self, payload: AuthorizeSecurityGroupIngressRequest) -> APIResponse[Dict]:
        """Authorize ingress rule for a security group."""
        response = self.client.call("authorizeSecurityGroupIngress", payload.model_dump(exclude_none=True))
        data = {}
        if 'authorizesecuritygroupingressresponse' in response:
            data = response['authorizesecuritygroupingressresponse']
        return APIResponse[Dict](**{"data": data})

    async def authorize_ingress_async(self, payload: AuthorizeSecurityGroupIngressRequest) -> APIResponse[Dict]:
        """Asynchronously authorize ingress rule for a security group."""
        response = await self.client.call_async("authorizeSecurityGroupIngress", payload.model_dump(exclude_none=True))
        data = {}
        if 'authorizesecuritygroupingressresponse' in response:
            data = response['authorizesecuritygroupingressresponse']
        return APIResponse[Dict](**{"data": data})

    def authorize_egress(self, payload: AuthorizeSecurityGroupEgressRequest) -> APIResponse[Dict]:
        """Authorize egress rule for a security group."""
        response = self.client.call("authorizeSecurityGroupEgress", payload.model_dump(exclude_none=True))
        data = {}
        if 'authorizesecuritygroupegressresponse' in response:
            data = response['authorizesecuritygroupegressresponse']
        return APIResponse[Dict](**{"data": data})

    async def authorize_egress_async(self, payload: AuthorizeSecurityGroupEgressRequest) -> APIResponse[Dict]:
        """Asynchronously authorize egress rule for a security group."""
        response = await self.client.call_async("authorizeSecurityGroupEgress", payload.model_dump(exclude_none=True))
        data = {}
        if 'authorizesecuritygroupegressresponse' in response:
            data = response['authorizesecuritygroupegressresponse']
        return APIResponse[Dict](**{"data": data})

    def revoke_ingress(self, payload: RevokeSecurityGroupIngressRequest) -> APIResponse[Dict]:
        """Revoke ingress rule from a security group."""
        response = self.client.call("revokeSecurityGroupIngress", payload.model_dump(exclude_none=True))
        data = {}
        if 'revokesecuritygroupingressresponse' in response:
            data = response['revokesecuritygroupingressresponse']
        return APIResponse[Dict](**{"data": data})

    async def revoke_ingress_async(self, payload: RevokeSecurityGroupIngressRequest) -> APIResponse[Dict]:
        """Asynchronously revoke ingress rule from a security group."""
        response = await self.client.call_async("revokeSecurityGroupIngress", payload.model_dump(exclude_none=True))
        data = {}
        if 'revokesecuritygroupingressresponse' in response:
            data = response['revokesecuritygroupingressresponse']
        return APIResponse[Dict](**{"data": data})

    def revoke_egress(self, payload: RevokeSecurityGroupEgressRequest) -> APIResponse[Dict]:
        """Revoke egress rule from a security group."""
        response = self.client.call("revokeSecurityGroupEgress", payload.model_dump(exclude_none=True))
        data = {}
        if 'revokesecuritygroupegressresponse' in response:
            data = response['revokesecuritygroupegressresponse']
        return APIResponse[Dict](**{"data": data})

    async def revoke_egress_async(self, payload: RevokeSecurityGroupEgressRequest) -> APIResponse[Dict]:
        """Asynchronously revoke egress rule from a security group."""
        response = await self.client.call_async("revokeSecurityGroupEgress", payload.model_dump(exclude_none=True))
        data = {}
        if 'revokesecuritygroupegressresponse' in response:
            data = response['revokesecuritygroupegressresponse']
        return APIResponse[Dict](**{"data": data})
