# services/security_group.py
from typing import Dict, List

from acs_sdk.schemas.request.security_group import ListSecurityGroupRequest

from .base import BaseService
from ..schemas.response.base import APIResponse


class SecurityGroup(BaseService):
    def list(self, payload: ListSecurityGroupRequest) -> APIResponse[List[Dict]]:
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
        response = await self.client.async_call("listSecurityGroups", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listsecuritygroupsresponse' in response:
            response = response['listsecuritygroupsresponse']
        if 'securitygroup' in response and response['securitygroup']:
            data = response['securitygroup']
            count = response['count']
        return APIResponse[List[Dict]](**{"data": data, "count": count})
