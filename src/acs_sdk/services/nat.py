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
    def list_ip_forwarding_rules(
        self, payload: ListIpForwardingRulesRequest
    ) -> APIResponse[List[Dict]]:
        """List all IP forwarding rules."""
        return self._execute(
            "listIpForwardingRules",
            payload,
            envelope="listipforwardingrulesresponse",
            entity="ipforwardingrule",
        )

    async def list_ip_forwarding_rules_async(
        self, payload: ListIpForwardingRulesRequest
    ) -> APIResponse[List[Dict]]:
        """Asynchronously list all IP forwarding rules."""
        return await self._execute_async(
            "listIpForwardingRules",
            payload,
            envelope="listipforwardingrulesresponse",
            entity="ipforwardingrule",
        )

    def create_ip_forwarding_rule(
        self, payload: CreateIpForwardingRuleRequest
    ) -> APIResponse[Dict]:
        """Create an IP forwarding rule."""
        return self._execute(
            "createIpForwardingRule",
            payload,
            envelope="createipforwardingruleresponse",
        )

    async def create_ip_forwarding_rule_async(
        self, payload: CreateIpForwardingRuleRequest
    ) -> APIResponse[Dict]:
        """Asynchronously create an IP forwarding rule."""
        return await self._execute_async(
            "createIpForwardingRule",
            payload,
            envelope="createipforwardingruleresponse",
        )

    def delete_ip_forwarding_rule(
        self, payload: DeleteIpForwardingRuleRequest
    ) -> APIResponse[Dict]:
        """Delete an IP forwarding rule."""
        return self._execute(
            "deleteIpForwardingRule",
            payload,
            envelope="deleteipforwardingruleresponse",
        )

    async def delete_ip_forwarding_rule_async(
        self, payload: DeleteIpForwardingRuleRequest
    ) -> APIResponse[Dict]:
        """Asynchronously delete an IP forwarding rule."""
        return await self._execute_async(
            "deleteIpForwardingRule",
            payload,
            envelope="deleteipforwardingruleresponse",
        )

    def enable_static_nat(self, payload: EnableStaticNatRequest) -> APIResponse[Dict]:
        """Enable static NAT."""
        return self._execute(
            "enableStaticNat",
            payload,
            envelope="enablestaticnatresponse",
        )

    async def enable_static_nat_async(self, payload: EnableStaticNatRequest) -> APIResponse[Dict]:
        """Asynchronously enable static NAT."""
        return await self._execute_async(
            "enableStaticNat",
            payload,
            envelope="enablestaticnatresponse",
        )

    def disable_static_nat(self, payload: DisableStaticNatRequest) -> APIResponse[Dict]:
        """Disable static NAT."""
        return self._execute(
            "disableStaticNat",
            payload,
            envelope="disablestaticnatresponse",
        )

    async def disable_static_nat_async(self, payload: DisableStaticNatRequest) -> APIResponse[Dict]:
        """Asynchronously disable static NAT."""
        return await self._execute_async(
            "disableStaticNat",
            payload,
            envelope="disablestaticnatresponse",
        )
