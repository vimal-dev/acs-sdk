import asyncio
from unittest.mock import AsyncMock, Mock

from acs_sdk.schemas.request.load_balancer import (
    AssignCertToLoadBalancerRequest,
    AssignToGlobalLoadBalancerRuleRequest,
    AssignToLoadBalancerRuleRequest,
    CreateGlobalLoadBalancerRuleRequest,
    CreateLBHealthCheckPolicyRequest,
    CreateLBStickinessPolicyRequest,
    CreateLoadBalancerRequest,
    CreateLoadBalancerRuleRequest,
    DeleteGlobalLoadBalancerRuleRequest,
    DeleteLBHealthCheckPolicyRequest,
    DeleteLBStickinessPolicyRequest,
    DeleteLoadBalancerRequest,
    DeleteLoadBalancerRuleRequest,
    DeleteServicePackageOfferingRequest,
    DeployNetscalerVpxRequest,
    GetLoadBalancerSslCertificateRequest,
    ListGlobalLoadBalancerRulesRequest,
    ListLBHealthCheckPoliciesRequest,
    ListLBStickinessPoliciesRequest,
    ListLoadBalancerRuleInstancesRequest,
    ListLoadBalancerRulesRequest,
    ListLoadBalancersRequest,
    ListRegisteredServicePackagesRequest,
    RemoveCertFromLoadBalancerRequest,
    RemoveFromGlobalLoadBalancerRuleRequest,
    RemoveFromLoadBalancerRuleRequest,
    StopNetScalerVpxRequest,
    UpdateGlobalLoadBalancerRuleRequest,
    UpdateLBHealthCheckPolicyRequest,
    UpdateLBStickinessPolicyRequest,
    UpdateLoadBalancerRequest,
    UpdateLoadBalancerRuleRequest,
)
from acs_sdk.services.load_balancer import LoadBalancer


# ---------------------------------------------------------------------------
# create_rule
# ---------------------------------------------------------------------------

def test_lb_create_rule_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "createloadbalancerruleresponse": {"id": "lb-rule-1", "name": "rule-1"},
    }

    lb = LoadBalancer(client=mock_client)
    payload = CreateLoadBalancerRuleRequest(
        algorithm="roundrobin", name="rule-1", privatePort=80, publicPort=80
    )
    response = lb.create_rule(payload)

    assert response.data == {"id": "lb-rule-1", "name": "rule-1"}
    mock_client.call.assert_called_once_with(
        "createLoadBalancerRule", payload.model_dump(exclude_none=True)
    )


def test_lb_create_rule_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={"createloadbalancerruleresponse": {"id": "lb-rule-1"}}
    )

    lb = LoadBalancer(client=mock_client)
    payload = CreateLoadBalancerRuleRequest(
        algorithm="roundrobin", name="rule-1", privatePort=80, publicPort=80
    )
    response = asyncio.run(lb.create_rule_async(payload))

    assert response.data == {"id": "lb-rule-1"}
    mock_client.call_async.assert_called_once_with(
        "createLoadBalancerRule", payload.model_dump(exclude_none=True)
    )


# ---------------------------------------------------------------------------
# list_rules
# ---------------------------------------------------------------------------

def test_lb_list_rules_parses_list_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "listloadbalancerrulesresponse": {
            "loadbalancerrule": [{"id": "lb-rule-1", "name": "rule-1"}],
            "count": 1,
        }
    }

    lb = LoadBalancer(client=mock_client)
    payload = ListLoadBalancerRulesRequest()
    response = lb.list_rules(payload)

    assert response.data == [{"id": "lb-rule-1", "name": "rule-1"}]
    assert response.count == 1
    mock_client.call.assert_called_once_with(
        "listLoadBalancerRules", payload.model_dump(exclude_none=True)
    )


def test_lb_list_rules_async_parses_list_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={
            "listloadbalancerrulesresponse": {
                "loadbalancerrule": [{"id": "lb-rule-2"}],
                "count": 1,
            }
        }
    )

    lb = LoadBalancer(client=mock_client)
    payload = ListLoadBalancerRulesRequest(name="rule-2")
    response = asyncio.run(lb.list_rules_async(payload))

    assert response.data == [{"id": "lb-rule-2"}]
    assert response.count == 1
    mock_client.call_async.assert_called_once_with(
        "listLoadBalancerRules", payload.model_dump(exclude_none=True)
    )


# ---------------------------------------------------------------------------
# update_rule / delete_rule
# ---------------------------------------------------------------------------

def test_lb_update_rule_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "updateloadbalancerruleresponse": {"id": "lb-rule-1", "name": "rule-1-updated"},
    }

    lb = LoadBalancer(client=mock_client)
    payload = UpdateLoadBalancerRuleRequest(id="lb-rule-1", name="rule-1-updated")
    response = lb.update_rule(payload)

    assert response.data == {"id": "lb-rule-1", "name": "rule-1-updated"}
    mock_client.call.assert_called_once_with(
        "updateLoadBalancerRule", {"id": "lb-rule-1", "name": "rule-1-updated"}
    )


def test_lb_update_rule_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={"updateloadbalancerruleresponse": {"id": "lb-rule-1"}}
    )

    lb = LoadBalancer(client=mock_client)
    payload = UpdateLoadBalancerRuleRequest(id="lb-rule-1")
    response = asyncio.run(lb.update_rule_async(payload))

    assert response.data == {"id": "lb-rule-1"}
    mock_client.call_async.assert_called_once_with("updateLoadBalancerRule", {"id": "lb-rule-1"})


def test_lb_delete_rule_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "deleteloadbalancerruleresponse": {"success": "true"},
    }

    lb = LoadBalancer(client=mock_client)
    payload = DeleteLoadBalancerRuleRequest(id="lb-rule-1")
    response = lb.delete_rule(payload)

    assert response.data == {"success": "true"}
    mock_client.call.assert_called_once_with("deleteLoadBalancerRule", {"id": "lb-rule-1"})


def test_lb_delete_rule_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={"deleteloadbalancerruleresponse": {"success": "true"}}
    )

    lb = LoadBalancer(client=mock_client)
    payload = DeleteLoadBalancerRuleRequest(id="lb-rule-1")
    response = asyncio.run(lb.delete_rule_async(payload))

    assert response.data == {"success": "true"}
    mock_client.call_async.assert_called_once_with("deleteLoadBalancerRule", {"id": "lb-rule-1"})


# ---------------------------------------------------------------------------
# assign_to_rule / remove_from_rule
# ---------------------------------------------------------------------------

def test_lb_assign_to_rule_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "assigntoloadbalancerruleresponse": {"success": "true"},
    }

    lb = LoadBalancer(client=mock_client)
    payload = AssignToLoadBalancerRuleRequest(id="lb-rule-1", virtualMachineIds=["vm-1"])
    response = lb.assign_to_rule(payload)

    assert response.data == {"success": "true"}
    mock_client.call.assert_called_once_with(
        "assignToLoadBalancerRule", {"id": "lb-rule-1", "virtualmachineids": "vm-1"}
    )


def test_lb_assign_to_rule_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={"assigntoloadbalancerruleresponse": {"success": "true"}}
    )

    lb = LoadBalancer(client=mock_client)
    payload = AssignToLoadBalancerRuleRequest(id="lb-rule-1", virtualMachineIds=["vm-1"])
    response = asyncio.run(lb.assign_to_rule_async(payload))

    assert response.data == {"success": "true"}
    mock_client.call_async.assert_called_once_with(
        "assignToLoadBalancerRule", {"id": "lb-rule-1", "virtualmachineids": "vm-1"}
    )


def test_lb_remove_from_rule_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "removefromloadbalancerruleresponse": {"success": "true"},
    }

    lb = LoadBalancer(client=mock_client)
    payload = RemoveFromLoadBalancerRuleRequest(id="lb-rule-1", virtualMachineIds=["vm-1"])
    response = lb.remove_from_rule(payload)

    assert response.data == {"success": "true"}
    mock_client.call.assert_called_once_with(
        "removeFromLoadBalancerRule", {"id": "lb-rule-1", "virtualmachineids": "vm-1"}
    )


def test_lb_remove_from_rule_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={"removefromloadbalancerruleresponse": {"success": "true"}}
    )

    lb = LoadBalancer(client=mock_client)
    payload = RemoveFromLoadBalancerRuleRequest(id="lb-rule-1", virtualMachineIds=["vm-1"])
    response = asyncio.run(lb.remove_from_rule_async(payload))

    assert response.data == {"success": "true"}
    mock_client.call_async.assert_called_once_with(
        "removeFromLoadBalancerRule", {"id": "lb-rule-1", "virtualmachineids": "vm-1"}
    )


# ---------------------------------------------------------------------------
# list_rule_instances
# ---------------------------------------------------------------------------

def test_lb_list_rule_instances_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "listloadbalancerruleinstancesresponse": {
            "loadbalancerruleinstance": [{"id": "vm-1"}],
        }
    }

    lb = LoadBalancer(client=mock_client)
    payload = ListLoadBalancerRuleInstancesRequest(id="lb-rule-1")
    response = lb.list_rule_instances(payload)

    assert response.data == {"loadbalancerruleinstance": [{"id": "vm-1"}]}
    mock_client.call.assert_called_once_with(
        "listLoadBalancerRuleInstances", payload.model_dump(exclude_none=True)
    )


def test_lb_list_rule_instances_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={
            "listloadbalancerruleinstancesresponse": {
                "loadbalancerruleinstance": [{"id": "vm-2"}],
            }
        }
    )

    lb = LoadBalancer(client=mock_client)
    payload = ListLoadBalancerRuleInstancesRequest(id="lb-rule-1")
    response = asyncio.run(lb.list_rule_instances_async(payload))

    assert response.data == {"loadbalancerruleinstance": [{"id": "vm-2"}]}
    mock_client.call_async.assert_called_once_with(
        "listLoadBalancerRuleInstances", payload.model_dump(exclude_none=True)
    )


# ---------------------------------------------------------------------------
# health check policy
# ---------------------------------------------------------------------------

def test_lb_create_health_check_policy_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "createlbhealthcheckpolicyresponse": {"healthcheckpolicy": [{"id": "hcp-1"}]},
    }

    lb = LoadBalancer(client=mock_client)
    payload = CreateLBHealthCheckPolicyRequest(lbRuleId="lb-rule-1")
    response = lb.create_health_check_policy(payload)

    assert response.data == {"healthcheckpolicy": [{"id": "hcp-1"}]}
    mock_client.call.assert_called_once_with(
        "createLBHealthCheckPolicy", {"lbruleid": "lb-rule-1"}
    )


def test_lb_create_health_check_policy_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={"createlbhealthcheckpolicyresponse": {"healthcheckpolicy": [{"id": "hcp-1"}]}}
    )

    lb = LoadBalancer(client=mock_client)
    payload = CreateLBHealthCheckPolicyRequest(lbRuleId="lb-rule-1")
    response = asyncio.run(lb.create_health_check_policy_async(payload))

    assert response.data == {"healthcheckpolicy": [{"id": "hcp-1"}]}
    mock_client.call_async.assert_called_once_with(
        "createLBHealthCheckPolicy", {"lbruleid": "lb-rule-1"}
    )


def test_lb_delete_health_check_policy_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "deletelbhealthcheckpolicyresponse": {"success": "true"},
    }

    lb = LoadBalancer(client=mock_client)
    payload = DeleteLBHealthCheckPolicyRequest(id="hcp-1")
    response = lb.delete_health_check_policy(payload)

    assert response.data == {"success": "true"}
    mock_client.call.assert_called_once_with("deleteLBHealthCheckPolicy", {"id": "hcp-1"})


def test_lb_delete_health_check_policy_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={"deletelbhealthcheckpolicyresponse": {"success": "true"}}
    )

    lb = LoadBalancer(client=mock_client)
    payload = DeleteLBHealthCheckPolicyRequest(id="hcp-1")
    response = asyncio.run(lb.delete_health_check_policy_async(payload))

    assert response.data == {"success": "true"}
    mock_client.call_async.assert_called_once_with("deleteLBHealthCheckPolicy", {"id": "hcp-1"})


def test_lb_update_health_check_policy_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "updatelbhealthcheckpolicyresponse": {"healthcheckpolicy": [{"id": "hcp-1"}]},
    }

    lb = LoadBalancer(client=mock_client)
    payload = UpdateLBHealthCheckPolicyRequest(id="hcp-1", forDisplay=True)
    response = lb.update_health_check_policy(payload)

    assert response.data == {"healthcheckpolicy": [{"id": "hcp-1"}]}
    mock_client.call.assert_called_once_with(
        "updateLBHealthCheckPolicy", {"id": "hcp-1", "fordisplay": True}
    )


def test_lb_update_health_check_policy_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={"updatelbhealthcheckpolicyresponse": {"healthcheckpolicy": [{"id": "hcp-1"}]}}
    )

    lb = LoadBalancer(client=mock_client)
    payload = UpdateLBHealthCheckPolicyRequest(id="hcp-1")
    response = asyncio.run(lb.update_health_check_policy_async(payload))

    assert response.data == {"healthcheckpolicy": [{"id": "hcp-1"}]}
    mock_client.call_async.assert_called_once_with("updateLBHealthCheckPolicy", {"id": "hcp-1"})


def test_lb_list_health_check_policies_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "listlbhealthcheckpoliciesresponse": {"healthcheckpolicy": [{"id": "hcp-1"}]},
    }

    lb = LoadBalancer(client=mock_client)
    payload = ListLBHealthCheckPoliciesRequest(lbRuleId="lb-rule-1")
    response = lb.list_health_check_policies(payload)

    assert response.data == {"healthcheckpolicy": [{"id": "hcp-1"}]}
    mock_client.call.assert_called_once_with(
        "listLBHealthCheckPolicies", payload.model_dump(exclude_none=True)
    )


def test_lb_list_health_check_policies_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={"listlbhealthcheckpoliciesresponse": {"healthcheckpolicy": [{"id": "hcp-2"}]}}
    )

    lb = LoadBalancer(client=mock_client)
    payload = ListLBHealthCheckPoliciesRequest()
    response = asyncio.run(lb.list_health_check_policies_async(payload))

    assert response.data == {"healthcheckpolicy": [{"id": "hcp-2"}]}
    mock_client.call_async.assert_called_once_with(
        "listLBHealthCheckPolicies", payload.model_dump(exclude_none=True)
    )


# ---------------------------------------------------------------------------
# stickiness policy
# ---------------------------------------------------------------------------

def test_lb_create_stickiness_policy_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "createlbstickinesspolicyresponse": {"stickinesspolicy": [{"id": "sp-1"}]},
    }

    lb = LoadBalancer(client=mock_client)
    payload = CreateLBStickinessPolicyRequest(
        lbRuleId="lb-rule-1", methodName="LbCookie", name="policy-1"
    )
    response = lb.create_stickiness_policy(payload)

    assert response.data == {"stickinesspolicy": [{"id": "sp-1"}]}
    mock_client.call.assert_called_once_with(
        "createLBStickinessPolicy", payload.model_dump(exclude_none=True)
    )


def test_lb_create_stickiness_policy_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={"createlbstickinesspolicyresponse": {"stickinesspolicy": [{"id": "sp-1"}]}}
    )

    lb = LoadBalancer(client=mock_client)
    payload = CreateLBStickinessPolicyRequest(
        lbRuleId="lb-rule-1", methodName="SourceBased", name="policy-1"
    )
    response = asyncio.run(lb.create_stickiness_policy_async(payload))

    assert response.data == {"stickinesspolicy": [{"id": "sp-1"}]}
    mock_client.call_async.assert_called_once_with(
        "createLBStickinessPolicy", payload.model_dump(exclude_none=True)
    )


def test_lb_delete_stickiness_policy_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "deletelbstickinesspolicyresponse": {"success": "true"},
    }

    lb = LoadBalancer(client=mock_client)
    payload = DeleteLBStickinessPolicyRequest(id="sp-1")
    response = lb.delete_stickiness_policy(payload)

    assert response.data == {"success": "true"}
    mock_client.call.assert_called_once_with("deleteLBStickinessPolicy", {"id": "sp-1"})


def test_lb_delete_stickiness_policy_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={"deletelbstickinesspolicyresponse": {"success": "true"}}
    )

    lb = LoadBalancer(client=mock_client)
    payload = DeleteLBStickinessPolicyRequest(id="sp-1")
    response = asyncio.run(lb.delete_stickiness_policy_async(payload))

    assert response.data == {"success": "true"}
    mock_client.call_async.assert_called_once_with("deleteLBStickinessPolicy", {"id": "sp-1"})


def test_lb_update_stickiness_policy_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "updatelbstickinesspolicyresponse": {"stickinesspolicy": [{"id": "sp-1"}]},
    }

    lb = LoadBalancer(client=mock_client)
    payload = UpdateLBStickinessPolicyRequest(id="sp-1")
    response = lb.update_stickiness_policy(payload)

    assert response.data == {"stickinesspolicy": [{"id": "sp-1"}]}
    mock_client.call.assert_called_once_with("updateLBStickinessPolicy", {"id": "sp-1"})


def test_lb_update_stickiness_policy_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={"updatelbstickinesspolicyresponse": {"stickinesspolicy": [{"id": "sp-1"}]}}
    )

    lb = LoadBalancer(client=mock_client)
    payload = UpdateLBStickinessPolicyRequest(id="sp-1")
    response = asyncio.run(lb.update_stickiness_policy_async(payload))

    assert response.data == {"stickinesspolicy": [{"id": "sp-1"}]}
    mock_client.call_async.assert_called_once_with("updateLBStickinessPolicy", {"id": "sp-1"})


def test_lb_list_stickiness_policies_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "listlbstickinesspoliciesresponse": {"stickinesspolicy": [{"id": "sp-1"}]},
    }

    lb = LoadBalancer(client=mock_client)
    payload = ListLBStickinessPoliciesRequest(lbRuleId="lb-rule-1")
    response = lb.list_stickiness_policies(payload)

    assert response.data == {"stickinesspolicy": [{"id": "sp-1"}]}
    mock_client.call.assert_called_once_with(
        "listLBStickinessPolicies", payload.model_dump(exclude_none=True)
    )


def test_lb_list_stickiness_policies_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={"listlbstickinesspoliciesresponse": {"stickinesspolicy": [{"id": "sp-2"}]}}
    )

    lb = LoadBalancer(client=mock_client)
    payload = ListLBStickinessPoliciesRequest()
    response = asyncio.run(lb.list_stickiness_policies_async(payload))

    assert response.data == {"stickinesspolicy": [{"id": "sp-2"}]}
    mock_client.call_async.assert_called_once_with(
        "listLBStickinessPolicies", payload.model_dump(exclude_none=True)
    )


# ---------------------------------------------------------------------------
# internal load balancer
# ---------------------------------------------------------------------------

def test_lb_create_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "createloadbalancerresponse": {"id": "ilb-1", "name": "ilb"},
    }

    lb = LoadBalancer(client=mock_client)
    payload = CreateLoadBalancerRequest(
        algorithm="roundrobin",
        instancePort=80,
        name="ilb",
        networkId="net-1",
        scheme="Internal",
        sourceIpAddressNetworkId="net-1",
        sourcePort=80,
    )
    response = lb.create(payload)

    assert response.data == {"id": "ilb-1", "name": "ilb"}
    mock_client.call.assert_called_once_with(
        "createLoadBalancer", payload.model_dump(exclude_none=True)
    )


def test_lb_create_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={"createloadbalancerresponse": {"id": "ilb-1"}}
    )

    lb = LoadBalancer(client=mock_client)
    payload = CreateLoadBalancerRequest(
        algorithm="leastconn",
        instancePort=80,
        name="ilb",
        networkId="net-1",
        scheme="Internal",
        sourceIpAddressNetworkId="net-1",
        sourcePort=80,
    )
    response = asyncio.run(lb.create_async(payload))

    assert response.data == {"id": "ilb-1"}
    mock_client.call_async.assert_called_once_with(
        "createLoadBalancer", payload.model_dump(exclude_none=True)
    )


def test_lb_list_parses_list_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "listloadbalancersresponse": {
            "loadbalancer": [{"id": "ilb-1"}],
            "count": 1,
        }
    }

    lb = LoadBalancer(client=mock_client)
    payload = ListLoadBalancersRequest()
    response = lb.list(payload)

    assert response.data == [{"id": "ilb-1"}]
    assert response.count == 1
    mock_client.call.assert_called_once_with(
        "listLoadBalancers", payload.model_dump(exclude_none=True)
    )


def test_lb_list_async_parses_list_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={
            "listloadbalancersresponse": {"loadbalancer": [{"id": "ilb-2"}], "count": 1}
        }
    )

    lb = LoadBalancer(client=mock_client)
    payload = ListLoadBalancersRequest()
    response = asyncio.run(lb.list_async(payload))

    assert response.data == [{"id": "ilb-2"}]
    assert response.count == 1
    mock_client.call_async.assert_called_once_with(
        "listLoadBalancers", payload.model_dump(exclude_none=True)
    )


def test_lb_update_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "updateloadbalancerresponse": {"id": "ilb-1"},
    }

    lb = LoadBalancer(client=mock_client)
    payload = UpdateLoadBalancerRequest(id="ilb-1", forDisplay=False)
    response = lb.update(payload)

    assert response.data == {"id": "ilb-1"}
    mock_client.call.assert_called_once_with(
        "updateLoadBalancer", {"id": "ilb-1", "fordisplay": False}
    )


def test_lb_update_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={"updateloadbalancerresponse": {"id": "ilb-1"}}
    )

    lb = LoadBalancer(client=mock_client)
    payload = UpdateLoadBalancerRequest(id="ilb-1")
    response = asyncio.run(lb.update_async(payload))

    assert response.data == {"id": "ilb-1"}
    mock_client.call_async.assert_called_once_with("updateLoadBalancer", {"id": "ilb-1"})


def test_lb_delete_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "deleteloadbalancerresponse": {"success": "true"},
    }

    lb = LoadBalancer(client=mock_client)
    payload = DeleteLoadBalancerRequest(id="ilb-1")
    response = lb.delete(payload)

    assert response.data == {"success": "true"}
    mock_client.call.assert_called_once_with("deleteLoadBalancer", {"id": "ilb-1"})


def test_lb_delete_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={"deleteloadbalancerresponse": {"success": "true"}}
    )

    lb = LoadBalancer(client=mock_client)
    payload = DeleteLoadBalancerRequest(id="ilb-1")
    response = asyncio.run(lb.delete_async(payload))

    assert response.data == {"success": "true"}
    mock_client.call_async.assert_called_once_with("deleteLoadBalancer", {"id": "ilb-1"})


# ---------------------------------------------------------------------------
# global (GSLB) load balancer rules
# ---------------------------------------------------------------------------

def test_lb_create_global_rule_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "creategloballoadbalancerruleresponse": {"id": "gslb-1"},
    }

    lb = LoadBalancer(client=mock_client)
    payload = CreateGlobalLoadBalancerRuleRequest(
        gslbDomainName="gslb.example.com",
        gslbServiceType="tcp",
        name="gslb-rule",
        regionId="1",
    )
    response = lb.create_global_rule(payload)

    assert response.data == {"id": "gslb-1"}
    mock_client.call.assert_called_once_with(
        "createGlobalLoadBalancerRule", payload.model_dump(exclude_none=True)
    )


def test_lb_create_global_rule_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={"creategloballoadbalancerruleresponse": {"id": "gslb-1"}}
    )

    lb = LoadBalancer(client=mock_client)
    payload = CreateGlobalLoadBalancerRuleRequest(
        gslbDomainName="gslb.example.com",
        gslbServiceType="http",
        name="gslb-rule",
        regionId="1",
    )
    response = asyncio.run(lb.create_global_rule_async(payload))

    assert response.data == {"id": "gslb-1"}
    mock_client.call_async.assert_called_once_with(
        "createGlobalLoadBalancerRule", payload.model_dump(exclude_none=True)
    )


def test_lb_list_global_rules_parses_list_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "listgloballoadbalancerrulesresponse": {
            "globalloadbalancerrule": [{"id": "gslb-1"}],
            "count": 1,
        }
    }

    lb = LoadBalancer(client=mock_client)
    payload = ListGlobalLoadBalancerRulesRequest()
    response = lb.list_global_rules(payload)

    assert response.data == [{"id": "gslb-1"}]
    assert response.count == 1
    mock_client.call.assert_called_once_with(
        "listGlobalLoadBalancerRules", payload.model_dump(exclude_none=True)
    )


def test_lb_list_global_rules_async_parses_list_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={
            "listgloballoadbalancerrulesresponse": {
                "globalloadbalancerrule": [{"id": "gslb-2"}],
                "count": 1,
            }
        }
    )

    lb = LoadBalancer(client=mock_client)
    payload = ListGlobalLoadBalancerRulesRequest()
    response = asyncio.run(lb.list_global_rules_async(payload))

    assert response.data == [{"id": "gslb-2"}]
    assert response.count == 1
    mock_client.call_async.assert_called_once_with(
        "listGlobalLoadBalancerRules", payload.model_dump(exclude_none=True)
    )


def test_lb_update_global_rule_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "updategloballoadbalancerruleresponse": {"id": "gslb-1"},
    }

    lb = LoadBalancer(client=mock_client)
    payload = UpdateGlobalLoadBalancerRuleRequest(id="gslb-1", description="updated")
    response = lb.update_global_rule(payload)

    assert response.data == {"id": "gslb-1"}
    mock_client.call.assert_called_once_with(
        "updateGlobalLoadBalancerRule", {"id": "gslb-1", "description": "updated"}
    )


def test_lb_update_global_rule_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={"updategloballoadbalancerruleresponse": {"id": "gslb-1"}}
    )

    lb = LoadBalancer(client=mock_client)
    payload = UpdateGlobalLoadBalancerRuleRequest(id="gslb-1")
    response = asyncio.run(lb.update_global_rule_async(payload))

    assert response.data == {"id": "gslb-1"}
    mock_client.call_async.assert_called_once_with(
        "updateGlobalLoadBalancerRule", {"id": "gslb-1"}
    )


def test_lb_delete_global_rule_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "deletegloballoadbalancerruleresponse": {"success": "true"},
    }

    lb = LoadBalancer(client=mock_client)
    payload = DeleteGlobalLoadBalancerRuleRequest(id="gslb-1")
    response = lb.delete_global_rule(payload)

    assert response.data == {"success": "true"}
    mock_client.call.assert_called_once_with("deleteGlobalLoadBalancerRule", {"id": "gslb-1"})


def test_lb_delete_global_rule_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={"deletegloballoadbalancerruleresponse": {"success": "true"}}
    )

    lb = LoadBalancer(client=mock_client)
    payload = DeleteGlobalLoadBalancerRuleRequest(id="gslb-1")
    response = asyncio.run(lb.delete_global_rule_async(payload))

    assert response.data == {"success": "true"}
    mock_client.call_async.assert_called_once_with(
        "deleteGlobalLoadBalancerRule", {"id": "gslb-1"}
    )


def test_lb_assign_to_global_rule_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "assigntogloballoadbalancerruleresponse": {"success": "true"},
    }

    lb = LoadBalancer(client=mock_client)
    payload = AssignToGlobalLoadBalancerRuleRequest(
        id="gslb-1", loadBalancerRuleList=["lb-rule-1", "lb-rule-2"]
    )
    response = lb.assign_to_global_rule(payload)

    assert response.data == {"success": "true"}
    mock_client.call.assert_called_once_with(
        "assignToGlobalLoadBalancerRule",
        {"id": "gslb-1", "loadbalancerrulelist": "lb-rule-1,lb-rule-2"},
    )


def test_lb_assign_to_global_rule_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={"assigntogloballoadbalancerruleresponse": {"success": "true"}}
    )

    lb = LoadBalancer(client=mock_client)
    payload = AssignToGlobalLoadBalancerRuleRequest(id="gslb-1", loadBalancerRuleList=["lb-rule-1"])
    response = asyncio.run(lb.assign_to_global_rule_async(payload))

    assert response.data == {"success": "true"}
    mock_client.call_async.assert_called_once_with(
        "assignToGlobalLoadBalancerRule", {"id": "gslb-1", "loadbalancerrulelist": "lb-rule-1"}
    )


def test_lb_remove_from_global_rule_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "removefromgloballoadbalancerruleresponse": {"success": "true"},
    }

    lb = LoadBalancer(client=mock_client)
    payload = RemoveFromGlobalLoadBalancerRuleRequest(id="gslb-1", loadBalancerRuleList=["lb-rule-1"])
    response = lb.remove_from_global_rule(payload)

    assert response.data == {"success": "true"}
    mock_client.call.assert_called_once_with(
        "removeFromGlobalLoadBalancerRule", {"id": "gslb-1", "loadbalancerrulelist": "lb-rule-1"}
    )


def test_lb_remove_from_global_rule_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={"removefromgloballoadbalancerruleresponse": {"success": "true"}}
    )

    lb = LoadBalancer(client=mock_client)
    payload = RemoveFromGlobalLoadBalancerRuleRequest(id="gslb-1", loadBalancerRuleList=["lb-rule-1"])
    response = asyncio.run(lb.remove_from_global_rule_async(payload))

    assert response.data == {"success": "true"}
    mock_client.call_async.assert_called_once_with(
        "removeFromGlobalLoadBalancerRule", {"id": "gslb-1", "loadbalancerrulelist": "lb-rule-1"}
    )


# ---------------------------------------------------------------------------
# SSL certificate
# ---------------------------------------------------------------------------

def test_lb_assign_cert_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "assigncerttoloadbalancerresponse": {"success": "true"},
    }

    lb = LoadBalancer(client=mock_client)
    payload = AssignCertToLoadBalancerRequest(certId="cert-1", lbRuleId="lb-rule-1")
    response = lb.assign_cert(payload)

    assert response.data == {"success": "true"}
    mock_client.call.assert_called_once_with(
        "assignCertToLoadBalancer", {"certid": "cert-1", "lbruleid": "lb-rule-1"}
    )


def test_lb_assign_cert_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={"assigncerttoloadbalancerresponse": {"success": "true"}}
    )

    lb = LoadBalancer(client=mock_client)
    payload = AssignCertToLoadBalancerRequest(certId="cert-1", lbRuleId="lb-rule-1", forced=True)
    response = asyncio.run(lb.assign_cert_async(payload))

    assert response.data == {"success": "true"}
    mock_client.call_async.assert_called_once_with(
        "assignCertToLoadBalancer",
        {"certid": "cert-1", "lbruleid": "lb-rule-1", "forced": True},
    )


def test_lb_remove_cert_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "removecertfromloadbalancerresponse": {"success": "true"},
    }

    lb = LoadBalancer(client=mock_client)
    payload = RemoveCertFromLoadBalancerRequest(lbRuleId="lb-rule-1")
    response = lb.remove_cert(payload)

    assert response.data == {"success": "true"}
    mock_client.call.assert_called_once_with("removeCertFromLoadBalancer", {"lbruleid": "lb-rule-1"})


def test_lb_remove_cert_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={"removecertfromloadbalancerresponse": {"success": "true"}}
    )

    lb = LoadBalancer(client=mock_client)
    payload = RemoveCertFromLoadBalancerRequest(lbRuleId="lb-rule-1")
    response = asyncio.run(lb.remove_cert_async(payload))

    assert response.data == {"success": "true"}
    mock_client.call_async.assert_called_once_with(
        "removeCertFromLoadBalancer", {"lbruleid": "lb-rule-1"}
    )


def test_lb_get_ssl_certificate_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "getloadbalancersslcertificateresponse": {"crt": "cert-data", "key": "key-data"},
    }

    lb = LoadBalancer(client=mock_client)
    payload = GetLoadBalancerSslCertificateRequest(id="ilb-1")
    response = lb.get_ssl_certificate(payload)

    assert response.data == {"crt": "cert-data", "key": "key-data"}
    mock_client.call.assert_called_once_with("getLoadBalancerSslCertificate", {"id": "ilb-1"})


def test_lb_get_ssl_certificate_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={"getloadbalancersslcertificateresponse": {"crt": "cert-data"}}
    )

    lb = LoadBalancer(client=mock_client)
    payload = GetLoadBalancerSslCertificateRequest(id="ilb-1")
    response = asyncio.run(lb.get_ssl_certificate_async(payload))

    assert response.data == {"crt": "cert-data"}
    mock_client.call_async.assert_called_once_with(
        "getLoadBalancerSslCertificate", {"id": "ilb-1"}
    )


# ---------------------------------------------------------------------------
# NetScaler VPX
# ---------------------------------------------------------------------------

def test_lb_deploy_netscaler_vpx_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "deploynetscalervpxresponse": {"lbdeviceid": "ns-1"},
    }

    lb = LoadBalancer(client=mock_client)
    payload = DeployNetscalerVpxRequest(
        serviceOfferingId="so-1", templateId="tmpl-1", zoneId="zone-1"
    )
    response = lb.deploy_netscaler_vpx(payload)

    assert response.data == {"lbdeviceid": "ns-1"}
    mock_client.call.assert_called_once_with(
        "deployNetscalerVpx", payload.model_dump(exclude_none=True)
    )


def test_lb_deploy_netscaler_vpx_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={"deploynetscalervpxresponse": {"lbdeviceid": "ns-1"}}
    )

    lb = LoadBalancer(client=mock_client)
    payload = DeployNetscalerVpxRequest(
        serviceOfferingId="so-1", templateId="tmpl-1", zoneId="zone-1"
    )
    response = asyncio.run(lb.deploy_netscaler_vpx_async(payload))

    assert response.data == {"lbdeviceid": "ns-1"}
    mock_client.call_async.assert_called_once_with(
        "deployNetscalerVpx", payload.model_dump(exclude_none=True)
    )


def test_lb_stop_netscaler_vpx_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "stopnetscalervpxresponse": {"id": "ns-vm-1", "state": "Stopped"},
    }

    lb = LoadBalancer(client=mock_client)
    payload = StopNetScalerVpxRequest(id="ns-vm-1")
    response = lb.stop_netscaler_vpx(payload)

    assert response.data == {"id": "ns-vm-1", "state": "Stopped"}
    mock_client.call.assert_called_once_with("stopNetScalerVpx", {"id": "ns-vm-1"})


def test_lb_stop_netscaler_vpx_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={"stopnetscalervpxresponse": {"id": "ns-vm-1", "state": "Stopped"}}
    )

    lb = LoadBalancer(client=mock_client)
    payload = StopNetScalerVpxRequest(id="ns-vm-1", forced=True)
    response = asyncio.run(lb.stop_netscaler_vpx_async(payload))

    assert response.data == {"id": "ns-vm-1", "state": "Stopped"}
    mock_client.call_async.assert_called_once_with(
        "stopNetScalerVpx", {"id": "ns-vm-1", "forced": True}
    )


# ---------------------------------------------------------------------------
# service packages
# ---------------------------------------------------------------------------

def test_lb_list_registered_service_packages_parses_list_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "listregisteredservicepackagesresponse": {
            "servicepackage": [{"id": "sp-1", "name": "package-1"}],
            "count": 1,
        }
    }

    lb = LoadBalancer(client=mock_client)
    payload = ListRegisteredServicePackagesRequest()
    response = lb.list_registered_service_packages(payload)

    assert response.data == [{"id": "sp-1", "name": "package-1"}]
    assert response.count == 1
    mock_client.call.assert_called_once_with(
        "listRegisteredServicePackages", payload.model_dump(exclude_none=True)
    )


def test_lb_list_registered_service_packages_async_parses_list_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={
            "listregisteredservicepackagesresponse": {
                "servicepackage": [{"id": "sp-2"}],
                "count": 1,
            }
        }
    )

    lb = LoadBalancer(client=mock_client)
    payload = ListRegisteredServicePackagesRequest()
    response = asyncio.run(lb.list_registered_service_packages_async(payload))

    assert response.data == [{"id": "sp-2"}]
    assert response.count == 1
    mock_client.call_async.assert_called_once_with(
        "listRegisteredServicePackages", payload.model_dump(exclude_none=True)
    )


def test_lb_delete_service_package_offering_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "deleteservicepackageofferingresponse": {"success": "true"},
    }

    lb = LoadBalancer(client=mock_client)
    payload = DeleteServicePackageOfferingRequest(id="sp-1")
    response = lb.delete_service_package_offering(payload)

    assert response.data == {"success": "true"}
    mock_client.call.assert_called_once_with("deleteServicePackageOffering", {"id": "sp-1"})


def test_lb_delete_service_package_offering_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={"deleteservicepackageofferingresponse": {"success": "true"}}
    )

    lb = LoadBalancer(client=mock_client)
    payload = DeleteServicePackageOfferingRequest(id="sp-1")
    response = asyncio.run(lb.delete_service_package_offering_async(payload))

    assert response.data == {"success": "true"}
    mock_client.call_async.assert_called_once_with(
        "deleteServicePackageOffering", {"id": "sp-1"}
    )
