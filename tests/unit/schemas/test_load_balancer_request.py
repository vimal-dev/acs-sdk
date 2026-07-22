import pytest
from pydantic import ValidationError

from acs_sdk.schemas.request.load_balancer import (
    AssignCertToLoadBalancerRequest,
    AssignToGlobalLoadBalancerRuleRequest,
    AssignToLoadBalancerRuleRequest,
    CreateGlobalLoadBalancerRuleRequest,
    CreateLBStickinessPolicyRequest,
    CreateLoadBalancerRequest,
    CreateLoadBalancerRuleRequest,
    DeleteLoadBalancerRuleRequest,
    ListGlobalLoadBalancerRulesRequest,
    ListLoadBalancerRulesRequest,
    ListLoadBalancersRequest,
    RemoveFromGlobalLoadBalancerRuleRequest,
    UpdateLoadBalancerRuleRequest,
)


# ---------------------------------------------------------------------------
# CreateLoadBalancerRuleRequest
# ---------------------------------------------------------------------------


def test_create_lb_rule_required_fields_serialize():
    req = CreateLoadBalancerRuleRequest(
        algorithm="roundrobin", name="rule-1", privatePort=80, publicPort=8080
    )
    dumped = req.model_dump(exclude_none=True)
    assert dumped == {
        "algorithm": "roundrobin",
        "name": "rule-1",
        "privateport": 80,
        "publicport": 8080,
    }


def test_create_lb_rule_aliases_serialize_to_snake_case():
    req = CreateLoadBalancerRuleRequest(
        algorithm="source",
        name="rule-1",
        privatePort=80,
        publicPort=80,
        domainId="dom-1",
        networkId="net-1",
        publicIpId="pubip-1",
        zoneId="zone-1",
        forDisplay=True,
        openFirewall=False,
    )
    dumped = req.model_dump(exclude_none=True)
    assert dumped["domainid"] == "dom-1"
    assert dumped["networkid"] == "net-1"
    assert dumped["publicipid"] == "pubip-1"
    assert dumped["zoneid"] == "zone-1"
    assert dumped["fordisplay"] is True
    assert dumped["openfirewall"] is False


def test_create_lb_rule_cidrlist_serializes_csv():
    req = CreateLoadBalancerRuleRequest(
        algorithm="leastconn",
        name="rule-1",
        privatePort=80,
        publicPort=80,
        cidrList=["10.0.0.0/24", "10.0.1.0/24"],
    )
    dumped = req.model_dump(exclude_none=True)
    assert dumped["cidrlist"] == "10.0.0.0/24,10.0.1.0/24"


def test_create_lb_rule_missing_required_fields_raises():
    with pytest.raises(ValidationError):
        CreateLoadBalancerRuleRequest()


def test_create_lb_rule_invalid_algorithm_raises():
    with pytest.raises(ValidationError):
        CreateLoadBalancerRuleRequest(
            algorithm="weighted", name="rule-1", privatePort=80, publicPort=80
        )


def test_create_lb_rule_invalid_protocol_raises():
    with pytest.raises(ValidationError):
        CreateLoadBalancerRuleRequest(
            algorithm="source",
            name="rule-1",
            privatePort=80,
            publicPort=80,
            protocol="http",
        )


# ---------------------------------------------------------------------------
# UpdateLoadBalancerRuleRequest / DeleteLoadBalancerRuleRequest
# ---------------------------------------------------------------------------


def test_update_lb_rule_serializes():
    req = UpdateLoadBalancerRuleRequest(id="rule-1", algorithm="leastconn", customId="custom-1")
    dumped = req.model_dump(exclude_none=True)
    assert dumped == {"id": "rule-1", "algorithm": "leastconn", "customid": "custom-1"}


def test_delete_lb_rule_missing_id_raises():
    with pytest.raises(ValidationError):
        DeleteLoadBalancerRuleRequest()


# ---------------------------------------------------------------------------
# ListLoadBalancerRulesRequest
# ---------------------------------------------------------------------------


def test_list_lb_rules_defaults_from_pagination_mixin():
    req = ListLoadBalancerRulesRequest()
    dumped = req.model_dump(exclude_none=True)
    assert dumped["page"] == 1
    assert dumped["pagesize"] == 50


def test_list_lb_rules_flattens_tags():
    req = ListLoadBalancerRulesRequest(tags={"env": "prod"})
    dumped = req.model_dump(exclude_none=True)
    assert dumped["tags[0].key"] == "env"
    assert dumped["tags[0].value"] == "prod"
    assert "tags" not in dumped


def test_list_lb_rules_aliases_serialize_to_snake_case():
    req = ListLoadBalancerRulesRequest(
        domainId="dom-1", isRecursive=True, listAll=True, virtualMachineId="vm-1"
    )
    dumped = req.model_dump(exclude_none=True)
    assert dumped["domainid"] == "dom-1"
    assert dumped["isrecursive"] is True
    assert dumped["listall"] is True
    assert dumped["virtualmachineid"] == "vm-1"


# ---------------------------------------------------------------------------
# AssignToLoadBalancerRuleRequest
# ---------------------------------------------------------------------------


def test_assign_to_lb_rule_serializes_virtualmachineids_csv():
    req = AssignToLoadBalancerRuleRequest(id="rule-1", virtualMachineIds=["vm-1", "vm-2"])
    dumped = req.model_dump(exclude_none=True)
    assert dumped == {"id": "rule-1", "virtualmachineids": "vm-1,vm-2"}


def test_assign_to_lb_rule_flattens_vmidipmap():
    req = AssignToLoadBalancerRuleRequest(
        id="rule-1",
        vmIdIpMap=[{"vmid": "vm-1", "vmip": "10.1.1.75"}],
    )
    dumped = req.model_dump(exclude_none=True)
    assert dumped["vmidipmap[0].vmid"] == "vm-1"
    assert dumped["vmidipmap[0].vmip"] == "10.1.1.75"
    assert "vmidipmap" not in dumped


def test_assign_to_lb_rule_missing_id_raises():
    with pytest.raises(ValidationError):
        AssignToLoadBalancerRuleRequest()


# ---------------------------------------------------------------------------
# CreateLBStickinessPolicyRequest
# ---------------------------------------------------------------------------


def test_create_stickiness_policy_required_fields_serialize():
    req = CreateLBStickinessPolicyRequest(lbRuleId="rule-1", methodName="LbCookie", name="policy-1")
    dumped = req.model_dump(exclude_none=True)
    assert dumped == {"lbruleid": "rule-1", "methodname": "LbCookie", "name": "policy-1"}


def test_create_stickiness_policy_flattens_param():
    req = CreateLBStickinessPolicyRequest(
        lbRuleId="rule-1",
        methodName="AppCookie",
        name="policy-1",
        param=[{"name": "cookiename", "value": "LBCookie"}],
    )
    dumped = req.model_dump(exclude_none=True)
    assert dumped["param[0].name"] == "cookiename"
    assert dumped["param[0].value"] == "LBCookie"
    assert "param" not in dumped


def test_create_stickiness_policy_invalid_methodname_raises():
    with pytest.raises(ValidationError):
        CreateLBStickinessPolicyRequest(lbRuleId="rule-1", methodName="Random", name="policy-1")


def test_create_stickiness_policy_missing_required_fields_raises():
    with pytest.raises(ValidationError):
        CreateLBStickinessPolicyRequest(lbRuleId="rule-1")


# ---------------------------------------------------------------------------
# CreateLoadBalancerRequest (internal LB)
# ---------------------------------------------------------------------------


def test_create_load_balancer_required_fields_serialize():
    req = CreateLoadBalancerRequest(
        algorithm="roundrobin",
        instancePort=80,
        name="ilb-1",
        networkId="net-1",
        scheme="Internal",
        sourceIpAddressNetworkId="net-1",
        sourcePort=80,
    )
    dumped = req.model_dump(exclude_none=True)
    assert dumped == {
        "algorithm": "roundrobin",
        "instanceport": 80,
        "name": "ilb-1",
        "networkid": "net-1",
        "scheme": "Internal",
        "sourceipaddressnetworkid": "net-1",
        "sourceport": 80,
    }


def test_create_load_balancer_invalid_scheme_raises():
    with pytest.raises(ValidationError):
        CreateLoadBalancerRequest(
            algorithm="roundrobin",
            instancePort=80,
            name="ilb-1",
            networkId="net-1",
            scheme="External",
            sourceIpAddressNetworkId="net-1",
            sourcePort=80,
        )


def test_create_load_balancer_missing_required_fields_raises():
    with pytest.raises(ValidationError):
        CreateLoadBalancerRequest(name="ilb-1")


# ---------------------------------------------------------------------------
# ListLoadBalancersRequest
# ---------------------------------------------------------------------------


def test_list_load_balancers_flattens_tags():
    req = ListLoadBalancersRequest(tags={"team": "net"})
    dumped = req.model_dump(exclude_none=True)
    assert dumped["tags[0].key"] == "team"
    assert dumped["tags[0].value"] == "net"
    assert "tags" not in dumped


def test_list_load_balancers_defaults_from_pagination_mixin():
    req = ListLoadBalancersRequest()
    dumped = req.model_dump(exclude_none=True)
    assert dumped["page"] == 1
    assert dumped["pagesize"] == 50


# ---------------------------------------------------------------------------
# CreateGlobalLoadBalancerRuleRequest
# ---------------------------------------------------------------------------


def test_create_global_lb_rule_required_fields_serialize():
    req = CreateGlobalLoadBalancerRuleRequest(
        gslbDomainName="gslb.example.com",
        gslbServiceType="tcp",
        name="gslb-1",
        regionId="1",
    )
    dumped = req.model_dump(exclude_none=True)
    assert dumped == {
        "gslbdomainname": "gslb.example.com",
        "gslbservicetype": "tcp",
        "name": "gslb-1",
        "regionid": "1",
    }


def test_create_global_lb_rule_invalid_service_type_raises():
    with pytest.raises(ValidationError):
        CreateGlobalLoadBalancerRuleRequest(
            gslbDomainName="gslb.example.com",
            gslbServiceType="icmp",
            name="gslb-1",
            regionId="1",
        )


def test_create_global_lb_rule_invalid_lbmethod_raises():
    with pytest.raises(ValidationError):
        CreateGlobalLoadBalancerRuleRequest(
            gslbDomainName="gslb.example.com",
            gslbServiceType="tcp",
            name="gslb-1",
            regionId="1",
            gslbLbMethod="weighted",
        )


# ---------------------------------------------------------------------------
# ListGlobalLoadBalancerRulesRequest
# ---------------------------------------------------------------------------


def test_list_global_lb_rules_flattens_tags():
    req = ListGlobalLoadBalancerRulesRequest(tags={"env": "prod"})
    dumped = req.model_dump(exclude_none=True)
    assert dumped["tags[0].key"] == "env"
    assert dumped["tags[0].value"] == "prod"


# ---------------------------------------------------------------------------
# AssignToGlobalLoadBalancerRuleRequest / RemoveFromGlobalLoadBalancerRuleRequest
# ---------------------------------------------------------------------------


def test_assign_to_global_lb_rule_serializes_loadbalancerrulelist_csv():
    req = AssignToGlobalLoadBalancerRuleRequest(
        id="gslb-1", loadBalancerRuleList=["rule-1", "rule-2"]
    )
    dumped = req.model_dump(exclude_none=True)
    assert dumped["loadbalancerrulelist"] == "rule-1,rule-2"


def test_assign_to_global_lb_rule_flattens_weights_map():
    req = AssignToGlobalLoadBalancerRuleRequest(
        id="gslb-1",
        loadBalancerRuleList=["rule-1"],
        gslbLbRuleWeightsMap=[{"loadbalancerid": "rule-1", "weight": 10}],
    )
    dumped = req.model_dump(exclude_none=True)
    assert dumped["gslblbruleweightsmap[0].loadbalancerid"] == "rule-1"
    assert dumped["gslblbruleweightsmap[0].weight"] == 10
    assert "gslblbruleweightsmap" not in dumped


def test_assign_to_global_lb_rule_missing_required_fields_raises():
    with pytest.raises(ValidationError):
        AssignToGlobalLoadBalancerRuleRequest(id="gslb-1")


def test_assign_to_global_lb_rule_weight_out_of_range_raises():
    with pytest.raises(ValidationError):
        AssignToGlobalLoadBalancerRuleRequest(
            id="gslb-1",
            loadBalancerRuleList=["rule-1"],
            gslbLbRuleWeightsMap=[{"loadbalancerid": "rule-1", "weight": 200}],
        )


def test_remove_from_global_lb_rule_serializes_loadbalancerrulelist_csv():
    req = RemoveFromGlobalLoadBalancerRuleRequest(id="gslb-1", loadBalancerRuleList=["rule-1"])
    dumped = req.model_dump(exclude_none=True)
    assert dumped == {"id": "gslb-1", "loadbalancerrulelist": "rule-1"}


# ---------------------------------------------------------------------------
# AssignCertToLoadBalancerRequest
# ---------------------------------------------------------------------------


def test_assign_cert_required_fields_serialize():
    req = AssignCertToLoadBalancerRequest(certId="cert-1", lbRuleId="rule-1")
    dumped = req.model_dump(exclude_none=True)
    assert dumped == {"certid": "cert-1", "lbruleid": "rule-1"}


def test_assign_cert_missing_required_fields_raises():
    with pytest.raises(ValidationError):
        AssignCertToLoadBalancerRequest(certId="cert-1")
