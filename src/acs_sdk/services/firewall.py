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
        response = self.client.call("createFirewallRule", payload.model_dump(exclude_none=True))
        data = {}
        if 'createfirewallruleresponse' in response:
            data = response['createfirewallruleresponse']
        return APIResponse[Dict](**{"data": data})

    async def create_firewall_rule_async(self, payload: CreateFirewallRuleRequest) -> APIResponse[Dict]:
        """Asynchronously create a firewall rule."""
        response = await self.client.call_async("createFirewallRule", payload.model_dump(exclude_none=True))
        data = {}
        if 'createfirewallruleresponse' in response:
            data = response['createfirewallruleresponse']
        return APIResponse[Dict](**{"data": data})

    def create_egress_firewall_rule(self, payload: CreateEgressFirewallRuleRequest) -> APIResponse[Dict]:
        """Create an egress firewall rule."""
        response = self.client.call("createEgressFirewallRule", payload.model_dump(exclude_none=True))
        data = {}
        if 'createegressfirewallruleresponse' in response:
            data = response['createegressfirewallruleresponse']
        return APIResponse[Dict](**{"data": data})

    async def create_egress_firewall_rule_async(self, payload: CreateEgressFirewallRuleRequest) -> APIResponse[Dict]:
        """Asynchronously create an egress firewall rule."""
        response = await self.client.call_async("createEgressFirewallRule", payload.model_dump(exclude_none=True))
        data = {}
        if 'createegressfirewallruleresponse' in response:
            data = response['createegressfirewallruleresponse']
        return APIResponse[Dict](**{"data": data})

    def create_ipv6_firewall_rule(self, payload: CreateIpv6FirewallRuleRequest) -> APIResponse[Dict]:
        """Create an IPv6 firewall rule."""
        response = self.client.call("createIpv6FirewallRule", payload.model_dump(exclude_none=True))
        data = {}
        if 'createipv6firewallruleresponse' in response:
            data = response['createipv6firewallruleresponse']
        return APIResponse[Dict](**{"data": data})

    async def create_ipv6_firewall_rule_async(self, payload: CreateIpv6FirewallRuleRequest) -> APIResponse[Dict]:
        """Asynchronously create an IPv6 firewall rule."""
        response = await self.client.call_async("createIpv6FirewallRule", payload.model_dump(exclude_none=True))
        data = {}
        if 'createipv6firewallruleresponse' in response:
            data = response['createipv6firewallruleresponse']
        return APIResponse[Dict](**{"data": data})

    def create_port_forwarding_rule(self, payload: CreatePortForwardingRuleRequest) -> APIResponse[Dict]:
        """Create a port forwarding rule."""
        response = self.client.call("createPortForwardingRule", payload.model_dump(exclude_none=True))
        data = {}
        if 'createportforwardingruleresponse' in response:
            data = response['createportforwardingruleresponse']
        return APIResponse[Dict](**{"data": data})

    async def create_port_forwarding_rule_async(self, payload: CreatePortForwardingRuleRequest) -> APIResponse[Dict]:
        """Asynchronously create a port forwarding rule."""
        response = await self.client.call_async("createPortForwardingRule", payload.model_dump(exclude_none=True))
        data = {}
        if 'createportforwardingruleresponse' in response:
            data = response['createportforwardingruleresponse']
        return APIResponse[Dict](**{"data": data})

    def create_routing_firewall_rule(self, payload: CreateRoutingFirewallRuleRequest) -> APIResponse[Dict]:
        """Create a routing firewall rule."""
        response = self.client.call("createRoutingFirewallRule", payload.model_dump(exclude_none=True))
        data = {}
        if 'createroutingfirewallruleresponse' in response:
            data = response['createroutingfirewallruleresponse']
        return APIResponse[Dict](**{"data": data})

    async def create_routing_firewall_rule_async(self, payload: CreateRoutingFirewallRuleRequest) -> APIResponse[Dict]:
        """Asynchronously create a routing firewall rule."""
        response = await self.client.call_async("createRoutingFirewallRule", payload.model_dump(exclude_none=True))
        data = {}
        if 'createroutingfirewallruleresponse' in response:
            data = response['createroutingfirewallruleresponse']
        return APIResponse[Dict](**{"data": data})

    def list_firewall_rules(self, payload: ListFirewallRulesRequest) -> APIResponse[List[Dict]]:
        """List all firewall rules."""
        response = self.client.call("listFirewallRules", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listfirewallrulesresponse' in response:
            response = response['listfirewallrulesresponse']
        if 'firewallrule' in response and response['firewallrule']:
            data = response['firewallrule']
            count = response['count']
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    async def list_firewall_rules_async(self, payload: ListFirewallRulesRequest) -> APIResponse[List[Dict]]:
        """Asynchronously list all firewall rules."""
        response = await self.client.call_async("listFirewallRules", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listfirewallrulesresponse' in response:
            response = response['listfirewallrulesresponse']
        if 'firewallrule' in response and response['firewallrule']:
            data = response['firewallrule']
            count = response['count']
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    def list_egress_firewall_rules(self, payload: ListEgressFirewallRulesRequest) -> APIResponse[List[Dict]]:
        """List all egress firewall rules."""
        response = self.client.call("listEgressFirewallRules", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listegressfirewallrulesresponse' in response:
            response = response['listegressfirewallrulesresponse']
        if 'firewallrule' in response and response['firewallrule']:
            data = response['firewallrule']
            count = response['count']
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    async def list_egress_firewall_rules_async(self, payload: ListEgressFirewallRulesRequest) -> APIResponse[List[Dict]]:
        """Asynchronously list all egress firewall rules."""
        response = await self.client.call_async("listEgressFirewallRules", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listegressfirewallrulesresponse' in response:
            response = response['listegressfirewallrulesresponse']
        if 'firewallrule' in response and response['firewallrule']:
            data = response['firewallrule']
            count = response['count']
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    def list_ipv6_firewall_rules(self, payload: ListIpv6FirewallRulesRequest) -> APIResponse[List[Dict]]:
        """List all IPv6 firewall rules."""
        response = self.client.call("listIpv6FirewallRules", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listipv6firewallrulesresponse' in response:
            response = response['listipv6firewallrulesresponse']
        if 'firewallrule' in response and response['firewallrule']:
            data = response['firewallrule']
            count = response['count']
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    async def list_ipv6_firewall_rules_async(self, payload: ListIpv6FirewallRulesRequest) -> APIResponse[List[Dict]]:
        """Asynchronously list all IPv6 firewall rules."""
        response = await self.client.call_async("listIpv6FirewallRules", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listipv6firewallrulesresponse' in response:
            response = response['listipv6firewallrulesresponse']
        if 'firewallrule' in response and response['firewallrule']:
            data = response['firewallrule']
            count = response['count']
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    def list_port_forwarding_rules(self, payload: ListPortForwardingRulesRequest) -> APIResponse[List[Dict]]:
        """List all port forwarding rules."""
        response = self.client.call("listPortForwardingRules", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listportforwardingrulesresponse' in response:
            response = response['listportforwardingrulesresponse']
        if 'portforwardingrule' in response and response['portforwardingrule']:
            data = response['portforwardingrule']
            count = response['count']
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    async def list_port_forwarding_rules_async(self, payload: ListPortForwardingRulesRequest) -> APIResponse[List[Dict]]:
        """Asynchronously list all port forwarding rules."""
        response = await self.client.call_async("listPortForwardingRules", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listportforwardingrulesresponse' in response:
            response = response['listportforwardingrulesresponse']
        if 'portforwardingrule' in response and response['portforwardingrule']:
            data = response['portforwardingrule']
            count = response['count']
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    def list_routing_firewall_rules(self, payload: ListRoutingFirewallRulesRequest) -> APIResponse[List[Dict]]:
        """List all routing firewall rules."""
        response = self.client.call("listRoutingFirewallRules", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listroutingfirewallrulesresponse' in response:
            response = response['listroutingfirewallrulesresponse']
        if 'firewallrule' in response and response['firewallrule']:
            data = response['firewallrule']
            count = response['count']
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    async def list_routing_firewall_rules_async(self, payload: ListRoutingFirewallRulesRequest) -> APIResponse[List[Dict]]:
        """Asynchronously list all routing firewall rules."""
        response = await self.client.call_async("listRoutingFirewallRules", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listroutingfirewallrulesresponse' in response:
            response = response['listroutingfirewallrulesresponse']
        if 'firewallrule' in response and response['firewallrule']:
            data = response['firewallrule']
            count = response['count']
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    def update_firewall_rule(self, payload: UpdateFirewallRuleRequest) -> APIResponse[Dict]:
        """Update a firewall rule."""
        response = self.client.call("updateFirewallRule", payload.model_dump(exclude_none=True))
        data = {}
        if 'updatefirewallruleresponse' in response:
            data = response['updatefirewallruleresponse']
        return APIResponse[Dict](**{"data": data})

    async def update_firewall_rule_async(self, payload: UpdateFirewallRuleRequest) -> APIResponse[Dict]:
        """Asynchronously update a firewall rule."""
        response = await self.client.call_async("updateFirewallRule", payload.model_dump(exclude_none=True))
        data = {}
        if 'updatefirewallruleresponse' in response:
            data = response['updatefirewallruleresponse']
        return APIResponse[Dict](**{"data": data})

    def update_egress_firewall_rule(self, payload: UpdateEgressFirewallRuleRequest) -> APIResponse[Dict]:
        """Update an egress firewall rule."""
        response = self.client.call("updateEgressFirewallRule", payload.model_dump(exclude_none=True))
        data = {}
        if 'updateegressfirewallruleresponse' in response:
            data = response['updateegressfirewallruleresponse']
        return APIResponse[Dict](**{"data": data})

    async def update_egress_firewall_rule_async(self, payload: UpdateEgressFirewallRuleRequest) -> APIResponse[Dict]:
        """Asynchronously update an egress firewall rule."""
        response = await self.client.call_async("updateEgressFirewallRule", payload.model_dump(exclude_none=True))
        data = {}
        if 'updateegressfirewallruleresponse' in response:
            data = response['updateegressfirewallruleresponse']
        return APIResponse[Dict](**{"data": data})

    def update_ipv6_firewall_rule(self, payload: UpdateIpv6FirewallRuleRequest) -> APIResponse[Dict]:
        """Update an IPv6 firewall rule."""
        response = self.client.call("updateIpv6FirewallRule", payload.model_dump(exclude_none=True))
        data = {}
        if 'updateipv6firewallruleresponse' in response:
            data = response['updateipv6firewallruleresponse']
        return APIResponse[Dict](**{"data": data})

    async def update_ipv6_firewall_rule_async(self, payload: UpdateIpv6FirewallRuleRequest) -> APIResponse[Dict]:
        """Asynchronously update an IPv6 firewall rule."""
        response = await self.client.call_async("updateIpv6FirewallRule", payload.model_dump(exclude_none=True))
        data = {}
        if 'updateipv6firewallruleresponse' in response:
            data = response['updateipv6firewallruleresponse']
        return APIResponse[Dict](**{"data": data})

    def update_port_forwarding_rule(self, payload: UpdatePortForwardingRuleRequest) -> APIResponse[Dict]:
        """Update a port forwarding rule."""
        response = self.client.call("updatePortForwardingRule", payload.model_dump(exclude_none=True))
        data = {}
        if 'updateportforwardingruleresponse' in response:
            data = response['updateportforwardingruleresponse']
        return APIResponse[Dict](**{"data": data})

    async def update_port_forwarding_rule_async(self, payload: UpdatePortForwardingRuleRequest) -> APIResponse[Dict]:
        """Asynchronously update a port forwarding rule."""
        response = await self.client.call_async("updatePortForwardingRule", payload.model_dump(exclude_none=True))
        data = {}
        if 'updateportforwardingruleresponse' in response:
            data = response['updateportforwardingruleresponse']
        return APIResponse[Dict](**{"data": data})

    def update_routing_firewall_rule(self, payload: UpdateRoutingFirewallRuleRequest) -> APIResponse[Dict]:
        """Update a routing firewall rule."""
        response = self.client.call("updateRoutingFirewallRule", payload.model_dump(exclude_none=True))
        data = {}
        if 'updateroutingfirewallruleresponse' in response:
            data = response['updateroutingfirewallruleresponse']
        return APIResponse[Dict](**{"data": data})

    async def update_routing_firewall_rule_async(self, payload: UpdateRoutingFirewallRuleRequest) -> APIResponse[Dict]:
        """Asynchronously update a routing firewall rule."""
        response = await self.client.call_async("updateRoutingFirewallRule", payload.model_dump(exclude_none=True))
        data = {}
        if 'updateroutingfirewallruleresponse' in response:
            data = response['updateroutingfirewallruleresponse']
        return APIResponse[Dict](**{"data": data})

    def delete_firewall_rule(self, payload: DeleteFirewallRuleRequest) -> APIResponse[Dict]:
        """Delete a firewall rule."""
        response = self.client.call("deleteFirewallRule", payload.model_dump(exclude_none=True))
        data = {}
        if 'deletefirewallruleresponse' in response:
            data = response['deletefirewallruleresponse']
        return APIResponse[Dict](**{"data": data})

    async def delete_firewall_rule_async(self, payload: DeleteFirewallRuleRequest) -> APIResponse[Dict]:
        """Asynchronously delete a firewall rule."""
        response = await self.client.call_async("deleteFirewallRule", payload.model_dump(exclude_none=True))
        data = {}
        if 'deletefirewallruleresponse' in response:
            data = response['deletefirewallruleresponse']
        return APIResponse[Dict](**{"data": data})

    def delete_egress_firewall_rule(self, payload: DeleteEgressFirewallRuleRequest) -> APIResponse[Dict]:
        """Delete an egress firewall rule."""
        response = self.client.call("deleteEgressFirewallRule", payload.model_dump(exclude_none=True))
        data = {}
        if 'deleteegressfirewallruleresponse' in response:
            data = response['deleteegressfirewallruleresponse']
        return APIResponse[Dict](**{"data": data})

    async def delete_egress_firewall_rule_async(self, payload: DeleteEgressFirewallRuleRequest) -> APIResponse[Dict]:
        """Asynchronously delete an egress firewall rule."""
        response = await self.client.call_async("deleteEgressFirewallRule", payload.model_dump(exclude_none=True))
        data = {}
        if 'deleteegressfirewallruleresponse' in response:
            data = response['deleteegressfirewallruleresponse']
        return APIResponse[Dict](**{"data": data})

    def delete_ipv6_firewall_rule(self, payload: DeleteIpv6FirewallRuleRequest) -> APIResponse[Dict]:
        """Delete an IPv6 firewall rule."""
        response = self.client.call("deleteIpv6FirewallRule", payload.model_dump(exclude_none=True))
        data = {}
        if 'deleteipv6firewallruleresponse' in response:
            data = response['deleteipv6firewallruleresponse']
        return APIResponse[Dict](**{"data": data})

    async def delete_ipv6_firewall_rule_async(self, payload: DeleteIpv6FirewallRuleRequest) -> APIResponse[Dict]:
        """Asynchronously delete an IPv6 firewall rule."""
        response = await self.client.call_async("deleteIpv6FirewallRule", payload.model_dump(exclude_none=True))
        data = {}
        if 'deleteipv6firewallruleresponse' in response:
            data = response['deleteipv6firewallruleresponse']
        return APIResponse[Dict](**{"data": data})

    def delete_port_forwarding_rule(self, payload: DeletePortForwardingRuleRequest) -> APIResponse[Dict]:
        """Delete a port forwarding rule."""
        response = self.client.call("deletePortForwardingRule", payload.model_dump(exclude_none=True))
        data = {}
        if 'deleteportforwardingruleresponse' in response:
            data = response['deleteportforwardingruleresponse']
        return APIResponse[Dict](**{"data": data})

    async def delete_port_forwarding_rule_async(self, payload: DeletePortForwardingRuleRequest) -> APIResponse[Dict]:
        """Asynchronously delete a port forwarding rule."""
        response = await self.client.call_async("deletePortForwardingRule", payload.model_dump(exclude_none=True))
        data = {}
        if 'deleteportforwardingruleresponse' in response:
            data = response['deleteportforwardingruleresponse']
        return APIResponse[Dict](**{"data": data})

    def delete_routing_firewall_rule(self, payload: DeleteRoutingFirewallRuleRequest) -> APIResponse[Dict]:
        """Delete a routing firewall rule."""
        response = self.client.call("deleteRoutingFirewallRule", payload.model_dump(exclude_none=True))
        data = {}
        if 'deleteroutingfirewallruleresponse' in response:
            data = response['deleteroutingfirewallruleresponse']
        return APIResponse[Dict](**{"data": data})

    async def delete_routing_firewall_rule_async(self, payload: DeleteRoutingFirewallRuleRequest) -> APIResponse[Dict]:
        """Asynchronously delete a routing firewall rule."""
        response = await self.client.call_async("deleteRoutingFirewallRule", payload.model_dump(exclude_none=True))
        data = {}
        if 'deleteroutingfirewallruleresponse' in response:
            data = response['deleteroutingfirewallruleresponse']
        return APIResponse[Dict](**{"data": data})