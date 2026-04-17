# services/nat.py
from typing import Dict, List

from acs_sdk.schemas.request.nat import (
    CreateIpForwardingRuleRequest,
    DeleteIpForwardingRuleRequest,
    DisableStaticNatRequest,
    EnableStaticNatRequest,
    ListIpForwardingRulesRequest,
)

from .base import BaseService
from ..schemas.response.base import APIResponse


class NAT(BaseService):
    def list_ip_forwarding_rules(self, payload: ListIpForwardingRulesRequest) -> APIResponse[List[Dict]]:
        """List all IP forwarding rules."""
        response = self.client.call("listIpForwardingRules", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listipforwardingrulesresponse' in response:
            response = response['listipforwardingrulesresponse']
        if 'ipforwardingrule' in response and response['ipforwardingrule']:
            data = response['ipforwardingrule']
            count = response['count']
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    async def list_ip_forwarding_rules_async(self, payload: ListIpForwardingRulesRequest) -> APIResponse[List[Dict]]:
        """Asynchronously list all IP forwarding rules."""
        response = await self.client.call_async("listIpForwardingRules", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listipforwardingrulesresponse' in response:
            response = response['listipforwardingrulesresponse']
        if 'ipforwardingrule' in response and response['ipforwardingrule']:
            data = response['ipforwardingrule']
            count = response['count']
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    def create_ip_forwarding_rule(self, payload: CreateIpForwardingRuleRequest) -> APIResponse[Dict]:
        """Create an IP forwarding rule."""
        response = self.client.call("createIpForwardingRule", payload.model_dump(exclude_none=True))
        data = {}
        if 'createipforwardingruleresponse' in response:
            data = response['createipforwardingruleresponse']
        return APIResponse[Dict](**{"data": data})

    async def create_ip_forwarding_rule_async(self, payload: CreateIpForwardingRuleRequest) -> APIResponse[Dict]:
        """Asynchronously create an IP forwarding rule."""
        response = await self.client.call_async("createIpForwardingRule", payload.model_dump(exclude_none=True))
        data = {}
        if 'createipforwardingruleresponse' in response:
            data = response['createipforwardingruleresponse']
        return APIResponse[Dict](**{"data": data})

    def delete_ip_forwarding_rule(self, payload: DeleteIpForwardingRuleRequest) -> APIResponse[Dict]:
        """Delete an IP forwarding rule."""
        response = self.client.call("deleteIpForwardingRule", payload.model_dump(exclude_none=True))
        data = {}
        if 'deleteipforwardingruleresponse' in response:
            data = response['deleteipforwardingruleresponse']
        return APIResponse[Dict](**{"data": data})

    async def delete_ip_forwarding_rule_async(self, payload: DeleteIpForwardingRuleRequest) -> APIResponse[Dict]:
        """Asynchronously delete an IP forwarding rule."""
        response = await self.client.call_async("deleteIpForwardingRule", payload.model_dump(exclude_none=True))
        data = {}
        if 'deleteipforwardingruleresponse' in response:
            data = response['deleteipforwardingruleresponse']
        return APIResponse[Dict](**{"data": data})

    def enable_static_nat(self, payload: EnableStaticNatRequest) -> APIResponse[Dict]:
        """Enable static NAT."""
        response = self.client.call("enableStaticNat", payload.model_dump(exclude_none=True))
        data = {}
        if 'enablestaticnatresponse' in response:
            data = response['enablestaticnatresponse']
        return APIResponse[Dict](**{"data": data})

    async def enable_static_nat_async(self, payload: EnableStaticNatRequest) -> APIResponse[Dict]:
        """Asynchronously enable static NAT."""
        response = await self.client.call_async("enableStaticNat", payload.model_dump(exclude_none=True))
        data = {}
        if 'enablestaticnatresponse' in response:
            data = response['enablestaticnatresponse']
        return APIResponse[Dict](**{"data": data})

    def disable_static_nat(self, payload: DisableStaticNatRequest) -> APIResponse[Dict]:
        """Disable static NAT."""
        response = self.client.call("disableStaticNat", payload.model_dump(exclude_none=True))
        data = {}
        if 'disablestaticnatresponse' in response:
            data = response['disablestaticnatresponse']
        return APIResponse[Dict](**{"data": data})

    async def disable_static_nat_async(self, payload: DisableStaticNatRequest) -> APIResponse[Dict]:
        """Asynchronously disable static NAT."""
        response = await self.client.call_async("disableStaticNat", payload.model_dump(exclude_none=True))
        data = {}
        if 'disablestaticnatresponse' in response:
            data = response['disablestaticnatresponse']
        return APIResponse[Dict](**{"data": data})