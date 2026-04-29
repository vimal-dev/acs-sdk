# services/firewall.py
from typing import Dict, List

from acs_sdk.schemas.request.firewall import (
    CreateEgressFirewallRuleRequest,
    CreateFirewallRuleRequest,
    CreateIpv6FirewallRuleRequest,
    CreatePortForwardingRuleRequest,
    CreateRoutingFirewallRuleRequest,
    DeleteEgressFirewallRuleRequest,
    DeleteFirewallRuleRequest,
    DeleteIpv6FirewallRuleRequest,
    DeletePortForwardingRuleRequest,
    DeleteRoutingFirewallRuleRequest,
    ListEgressFirewallRulesRequest,
    ListFirewallRulesRequest,
    ListIpv6FirewallRulesRequest,
    ListPortForwardingRulesRequest,
    ListRoutingFirewallRulesRequest,
    UpdateEgressFirewallRuleRequest,
    UpdateFirewallRuleRequest,
    UpdateIpv6FirewallRuleRequest,
    UpdatePortForwardingRuleRequest,
    UpdateRoutingFirewallRuleRequest,
)

from .base import BaseService
from ..schemas.response.base import APIResponse


class Firewall(BaseService):
    def create_firewall_rule(self, payload: CreateFirewallRuleRequest) -> APIResponse[Dict]:
        """Create a firewall rule."""
        return self._execute(
            "createFirewallRule",
            payload,
            envelope="createfirewallruleresponse",
        )

    async def create_firewall_rule_async(
        self, payload: CreateFirewallRuleRequest
    ) -> APIResponse[Dict]:
        """Asynchronously create a firewall rule."""
        return await self._execute_async(
            "createFirewallRule",
            payload,
            envelope="createfirewallruleresponse",
        )

    def create_egress_firewall_rule(
        self, payload: CreateEgressFirewallRuleRequest
    ) -> APIResponse[Dict]:
        """Create an egress firewall rule."""
        return self._execute(
            "createEgressFirewallRule",
            payload,
            envelope="createegressfirewallruleresponse",
        )

    async def create_egress_firewall_rule_async(
        self, payload: CreateEgressFirewallRuleRequest
    ) -> APIResponse[Dict]:
        """Asynchronously create an egress firewall rule."""
        return await self._execute_async(
            "createEgressFirewallRule",
            payload,
            envelope="createegressfirewallruleresponse",
        )

    def create_ipv6_firewall_rule(
        self, payload: CreateIpv6FirewallRuleRequest
    ) -> APIResponse[Dict]:
        """Create an IPv6 firewall rule."""
        return self._execute(
            "createIpv6FirewallRule",
            payload,
            envelope="createipv6firewallruleresponse",
        )

    async def create_ipv6_firewall_rule_async(
        self, payload: CreateIpv6FirewallRuleRequest
    ) -> APIResponse[Dict]:
        """Asynchronously create an IPv6 firewall rule."""
        return await self._execute_async(
            "createIpv6FirewallRule",
            payload,
            envelope="createipv6firewallruleresponse",
        )

    def create_port_forwarding_rule(
        self, payload: CreatePortForwardingRuleRequest
    ) -> APIResponse[Dict]:
        """Create a port forwarding rule."""
        return self._execute(
            "createPortForwardingRule",
            payload,
            envelope="createportforwardingruleresponse",
        )

    async def create_port_forwarding_rule_async(
        self, payload: CreatePortForwardingRuleRequest
    ) -> APIResponse[Dict]:
        """Asynchronously create a port forwarding rule."""
        return await self._execute_async(
            "createPortForwardingRule",
            payload,
            envelope="createportforwardingruleresponse",
        )

    def create_routing_firewall_rule(
        self, payload: CreateRoutingFirewallRuleRequest
    ) -> APIResponse[Dict]:
        """Create a routing firewall rule."""
        return self._execute(
            "createRoutingFirewallRule",
            payload,
            envelope="createroutingfirewallruleresponse",
        )

    async def create_routing_firewall_rule_async(
        self, payload: CreateRoutingFirewallRuleRequest
    ) -> APIResponse[Dict]:
        """Asynchronously create a routing firewall rule."""
        return await self._execute_async(
            "createRoutingFirewallRule",
            payload,
            envelope="createroutingfirewallruleresponse",
        )

    def list_firewall_rules(self, payload: ListFirewallRulesRequest) -> APIResponse[List[Dict]]:
        """List all firewall rules."""
        return self._execute(
            "listFirewallRules",
            payload,
            envelope="listfirewallrulesresponse",
            entity="firewallrule",
        )

    async def list_firewall_rules_async(
        self, payload: ListFirewallRulesRequest
    ) -> APIResponse[List[Dict]]:
        """Asynchronously list all firewall rules."""
        return await self._execute_async(
            "listFirewallRules",
            payload,
            envelope="listfirewallrulesresponse",
            entity="firewallrule",
        )

    def list_egress_firewall_rules(
        self, payload: ListEgressFirewallRulesRequest
    ) -> APIResponse[List[Dict]]:
        """List all egress firewall rules."""
        return self._execute(
            "listEgressFirewallRules",
            payload,
            envelope="listegressfirewallrulesresponse",
            entity="firewallrule",
        )

    async def list_egress_firewall_rules_async(
        self, payload: ListEgressFirewallRulesRequest
    ) -> APIResponse[List[Dict]]:
        """Asynchronously list all egress firewall rules."""
        return await self._execute_async(
            "listEgressFirewallRules",
            payload,
            envelope="listegressfirewallrulesresponse",
            entity="firewallrule",
        )

    def list_ipv6_firewall_rules(
        self, payload: ListIpv6FirewallRulesRequest
    ) -> APIResponse[List[Dict]]:
        """List all IPv6 firewall rules."""
        return self._execute(
            "listIpv6FirewallRules",
            payload,
            envelope="listipv6firewallrulesresponse",
            entity="firewallrule",
        )

    async def list_ipv6_firewall_rules_async(
        self, payload: ListIpv6FirewallRulesRequest
    ) -> APIResponse[List[Dict]]:
        """Asynchronously list all IPv6 firewall rules."""
        return await self._execute_async(
            "listIpv6FirewallRules",
            payload,
            envelope="listipv6firewallrulesresponse",
            entity="firewallrule",
        )

    def list_port_forwarding_rules(
        self, payload: ListPortForwardingRulesRequest
    ) -> APIResponse[List[Dict]]:
        """List all port forwarding rules."""
        return self._execute(
            "listPortForwardingRules",
            payload,
            envelope="listportforwardingrulesresponse",
            entity="portforwardingrule",
        )

    async def list_port_forwarding_rules_async(
        self, payload: ListPortForwardingRulesRequest
    ) -> APIResponse[List[Dict]]:
        """Asynchronously list all port forwarding rules."""
        return await self._execute_async(
            "listPortForwardingRules",
            payload,
            envelope="listportforwardingrulesresponse",
            entity="portforwardingrule",
        )

    def list_routing_firewall_rules(
        self, payload: ListRoutingFirewallRulesRequest
    ) -> APIResponse[List[Dict]]:
        """List all routing firewall rules."""
        return self._execute(
            "listRoutingFirewallRules",
            payload,
            envelope="listroutingfirewallrulesresponse",
            entity="firewallrule",
        )

    async def list_routing_firewall_rules_async(
        self, payload: ListRoutingFirewallRulesRequest
    ) -> APIResponse[List[Dict]]:
        """Asynchronously list all routing firewall rules."""
        return await self._execute_async(
            "listRoutingFirewallRules",
            payload,
            envelope="listroutingfirewallrulesresponse",
            entity="firewallrule",
        )

    def update_firewall_rule(self, payload: UpdateFirewallRuleRequest) -> APIResponse[Dict]:
        """Update a firewall rule."""
        return self._execute(
            "updateFirewallRule",
            payload,
            envelope="updatefirewallruleresponse",
        )

    async def update_firewall_rule_async(
        self, payload: UpdateFirewallRuleRequest
    ) -> APIResponse[Dict]:
        """Asynchronously update a firewall rule."""
        return await self._execute_async(
            "updateFirewallRule",
            payload,
            envelope="updatefirewallruleresponse",
        )

    def update_egress_firewall_rule(
        self, payload: UpdateEgressFirewallRuleRequest
    ) -> APIResponse[Dict]:
        """Update an egress firewall rule."""
        return self._execute(
            "updateEgressFirewallRule",
            payload,
            envelope="updateegressfirewallruleresponse",
        )

    async def update_egress_firewall_rule_async(
        self, payload: UpdateEgressFirewallRuleRequest
    ) -> APIResponse[Dict]:
        """Asynchronously update an egress firewall rule."""
        return await self._execute_async(
            "updateEgressFirewallRule",
            payload,
            envelope="updateegressfirewallruleresponse",
        )

    def update_ipv6_firewall_rule(
        self, payload: UpdateIpv6FirewallRuleRequest
    ) -> APIResponse[Dict]:
        """Update an IPv6 firewall rule."""
        return self._execute(
            "updateIpv6FirewallRule",
            payload,
            envelope="updateipv6firewallruleresponse",
        )

    async def update_ipv6_firewall_rule_async(
        self, payload: UpdateIpv6FirewallRuleRequest
    ) -> APIResponse[Dict]:
        """Asynchronously update an IPv6 firewall rule."""
        return await self._execute_async(
            "updateIpv6FirewallRule",
            payload,
            envelope="updateipv6firewallruleresponse",
        )

    def update_port_forwarding_rule(
        self, payload: UpdatePortForwardingRuleRequest
    ) -> APIResponse[Dict]:
        """Update a port forwarding rule."""
        return self._execute(
            "updatePortForwardingRule",
            payload,
            envelope="updateportforwardingruleresponse",
        )

    async def update_port_forwarding_rule_async(
        self, payload: UpdatePortForwardingRuleRequest
    ) -> APIResponse[Dict]:
        """Asynchronously update a port forwarding rule."""
        return await self._execute_async(
            "updatePortForwardingRule",
            payload,
            envelope="updateportforwardingruleresponse",
        )

    def update_routing_firewall_rule(
        self, payload: UpdateRoutingFirewallRuleRequest
    ) -> APIResponse[Dict]:
        """Update a routing firewall rule."""
        return self._execute(
            "updateRoutingFirewallRule",
            payload,
            envelope="updateroutingfirewallruleresponse",
        )

    async def update_routing_firewall_rule_async(
        self, payload: UpdateRoutingFirewallRuleRequest
    ) -> APIResponse[Dict]:
        """Asynchronously update a routing firewall rule."""
        return await self._execute_async(
            "updateRoutingFirewallRule",
            payload,
            envelope="updateroutingfirewallruleresponse",
        )

    def delete_firewall_rule(self, payload: DeleteFirewallRuleRequest) -> APIResponse[Dict]:
        """Delete a firewall rule."""
        return self._execute(
            "deleteFirewallRule",
            payload,
            envelope="deletefirewallruleresponse",
        )

    async def delete_firewall_rule_async(
        self, payload: DeleteFirewallRuleRequest
    ) -> APIResponse[Dict]:
        """Asynchronously delete a firewall rule."""
        return await self._execute_async(
            "deleteFirewallRule",
            payload,
            envelope="deletefirewallruleresponse",
        )

    def delete_egress_firewall_rule(
        self, payload: DeleteEgressFirewallRuleRequest
    ) -> APIResponse[Dict]:
        """Delete an egress firewall rule."""
        return self._execute(
            "deleteEgressFirewallRule",
            payload,
            envelope="deleteegressfirewallruleresponse",
        )

    async def delete_egress_firewall_rule_async(
        self, payload: DeleteEgressFirewallRuleRequest
    ) -> APIResponse[Dict]:
        """Asynchronously delete an egress firewall rule."""
        return await self._execute_async(
            "deleteEgressFirewallRule",
            payload,
            envelope="deleteegressfirewallruleresponse",
        )

    def delete_ipv6_firewall_rule(
        self, payload: DeleteIpv6FirewallRuleRequest
    ) -> APIResponse[Dict]:
        """Delete an IPv6 firewall rule."""
        return self._execute(
            "deleteIpv6FirewallRule",
            payload,
            envelope="deleteipv6firewallruleresponse",
        )

    async def delete_ipv6_firewall_rule_async(
        self, payload: DeleteIpv6FirewallRuleRequest
    ) -> APIResponse[Dict]:
        """Asynchronously delete an IPv6 firewall rule."""
        return await self._execute_async(
            "deleteIpv6FirewallRule",
            payload,
            envelope="deleteipv6firewallruleresponse",
        )

    def delete_port_forwarding_rule(
        self, payload: DeletePortForwardingRuleRequest
    ) -> APIResponse[Dict]:
        """Delete a port forwarding rule."""
        return self._execute(
            "deletePortForwardingRule",
            payload,
            envelope="deleteportforwardingruleresponse",
        )

    async def delete_port_forwarding_rule_async(
        self, payload: DeletePortForwardingRuleRequest
    ) -> APIResponse[Dict]:
        """Asynchronously delete a port forwarding rule."""
        return await self._execute_async(
            "deletePortForwardingRule",
            payload,
            envelope="deleteportforwardingruleresponse",
        )

    def delete_routing_firewall_rule(
        self, payload: DeleteRoutingFirewallRuleRequest
    ) -> APIResponse[Dict]:
        """Delete a routing firewall rule."""
        return self._execute(
            "deleteRoutingFirewallRule",
            payload,
            envelope="deleteroutingfirewallruleresponse",
        )

    async def delete_routing_firewall_rule_async(
        self, payload: DeleteRoutingFirewallRuleRequest
    ) -> APIResponse[Dict]:
        """Asynchronously delete a routing firewall rule."""
        return await self._execute_async(
            "deleteRoutingFirewallRule",
            payload,
            envelope="deleteroutingfirewallruleresponse",
        )
