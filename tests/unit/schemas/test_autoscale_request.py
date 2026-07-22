import pytest
from pydantic import ValidationError

from acs_sdk.schemas.request.autoscale import (
    CreateAutoScalePolicyRequest,
    CreateAutoScaleVmGroupRequest,
    CreateAutoScaleVmProfileRequest,
    CreateConditionRequest,
    CreateCounterRequest,
    DeleteAutoScalePolicyRequest,
    DeleteAutoScaleVmGroupRequest,
    DeleteAutoScaleVmProfileRequest,
    DeleteConditionRequest,
    DeleteCounterRequest,
    DisableAutoScaleVmGroupRequest,
    EnableAutoScaleVmGroupRequest,
    ListAutoScalePoliciesRequest,
    ListAutoScaleVmGroupsRequest,
    ListAutoScaleVmProfilesRequest,
    ListConditionsRequest,
    ListCountersRequest,
    NameValueEntry,
    UpdateAutoScalePolicyRequest,
    UpdateAutoScaleVmGroupRequest,
    UpdateAutoScaleVmProfileRequest,
    UpdateConditionRequest,
)


# ---------------------------------------------------------------------------
# AutoScale policies
# ---------------------------------------------------------------------------

def test_create_autoscale_policy_required_fields_serialize():
    req = CreateAutoScalePolicyRequest(action="scaleup", conditionIds=["cond-1", "cond-2"], duration=60)
    dumped = req.model_dump(exclude_none=True)
    assert dumped == {"action": "scaleup", "conditionids": "cond-1,cond-2", "duration": 60}


def test_create_autoscale_policy_optional_fields_serialize():
    req = CreateAutoScalePolicyRequest(
        action="scaledown", conditionIds=["cond-1"], duration=60, name="my-policy", quietTime=120
    )
    dumped = req.model_dump(exclude_none=True)
    assert dumped["name"] == "my-policy"
    assert dumped["quiettime"] == 120


def test_create_autoscale_policy_missing_required_fields_raises():
    with pytest.raises(ValidationError):
        CreateAutoScalePolicyRequest()


def test_update_autoscale_policy_required_id_serializes():
    req = UpdateAutoScalePolicyRequest(id="policy-1")
    dumped = req.model_dump(exclude_none=True)
    assert dumped == {"id": "policy-1"}


def test_update_autoscale_policy_conditionids_serialize_to_csv():
    req = UpdateAutoScalePolicyRequest(id="policy-1", conditionIds=["cond-1", "cond-2"])
    dumped = req.model_dump(exclude_none=True)
    assert dumped["conditionids"] == "cond-1,cond-2"


def test_delete_autoscale_policy_missing_id_raises():
    with pytest.raises(ValidationError):
        DeleteAutoScalePolicyRequest()


def test_list_autoscale_policies_all_fields_optional():
    req = ListAutoScalePoliciesRequest()
    dumped = req.model_dump(exclude_none=True)
    assert dumped == {"page": 1, "pagesize": 50}


def test_list_autoscale_policies_aliases_serialize_to_snake_case():
    req = ListAutoScalePoliciesRequest(conditionId="cond-1", domainId="dom-1", vmGroupId="grp-1", projectId="proj-1")
    dumped = req.model_dump(exclude_none=True)
    assert dumped["conditionid"] == "cond-1"
    assert dumped["domainid"] == "dom-1"
    assert dumped["vmgroupid"] == "grp-1"
    assert dumped["projectid"] == "proj-1"


# ---------------------------------------------------------------------------
# AutoScale VM profiles
# ---------------------------------------------------------------------------

def test_create_autoscale_vm_profile_required_fields_serialize():
    req = CreateAutoScaleVmProfileRequest(serviceOfferingId="so-1", templateId="tpl-1", zoneId="zone-1")
    dumped = req.model_dump(exclude_none=True)
    assert dumped == {"serviceofferingid": "so-1", "templateid": "tpl-1", "zoneid": "zone-1"}


def test_create_autoscale_vm_profile_missing_required_fields_raises():
    with pytest.raises(ValidationError):
        CreateAutoScaleVmProfileRequest()


def test_create_autoscale_vm_profile_counterparam_flattens_indexed():
    req = CreateAutoScaleVmProfileRequest(
        serviceOfferingId="so-1",
        templateId="tpl-1",
        zoneId="zone-1",
        counterParam=[NameValueEntry(name="snmpcommunity", value="public")],
    )
    dumped = req.model_dump(exclude_none=True)
    assert dumped["counterparam[0].name"] == "snmpcommunity"
    assert dumped["counterparam[0].value"] == "public"
    assert "counterparam" not in dumped


def test_create_autoscale_vm_profile_otherdeployparams_and_userdatadetails_flatten():
    req = CreateAutoScaleVmProfileRequest(
        serviceOfferingId="so-1",
        templateId="tpl-1",
        zoneId="zone-1",
        otherDeployParams=[NameValueEntry(name="rootdisksize", value="10")],
        userdataDetails=[NameValueEntry(name="key1", value="val1")],
    )
    dumped = req.model_dump(exclude_none=True)
    assert dumped["otherdeployparams[0].name"] == "rootdisksize"
    assert dumped["otherdeployparams[0].value"] == "10"
    assert dumped["userdatadetails[0].name"] == "key1"
    assert dumped["userdatadetails[0].value"] == "val1"


def test_update_autoscale_vm_profile_required_id_serializes():
    req = UpdateAutoScaleVmProfileRequest(id="profile-1")
    dumped = req.model_dump(exclude_none=True)
    assert dumped == {"id": "profile-1"}


def test_delete_autoscale_vm_profile_missing_id_raises():
    with pytest.raises(ValidationError):
        DeleteAutoScaleVmProfileRequest()


def test_list_autoscale_vm_profiles_all_fields_optional():
    req = ListAutoScaleVmProfilesRequest()
    dumped = req.model_dump(exclude_none=True)
    assert dumped == {"page": 1, "pagesize": 50}


# ---------------------------------------------------------------------------
# AutoScale VM groups
# ---------------------------------------------------------------------------

def test_create_autoscale_vm_group_required_fields_serialize():
    req = CreateAutoScaleVmGroupRequest(
        lbRuleId="lb-1",
        maxMembers=5,
        minMembers=1,
        scaleDownPolicyIds=["down-1"],
        scaleUpPolicyIds=["up-1", "up-2"],
        vmProfileId="profile-1",
    )
    dumped = req.model_dump(exclude_none=True)
    assert dumped == {
        "lbruleid": "lb-1",
        "maxmembers": 5,
        "minmembers": 1,
        "scaledownpolicyids": "down-1",
        "scaleuppolicyids": "up-1,up-2",
        "vmprofileid": "profile-1",
    }


def test_create_autoscale_vm_group_missing_required_fields_raises():
    with pytest.raises(ValidationError):
        CreateAutoScaleVmGroupRequest()


def test_update_autoscale_vm_group_required_id_serializes():
    req = UpdateAutoScaleVmGroupRequest(id="group-1")
    dumped = req.model_dump(exclude_none=True)
    assert dumped == {"id": "group-1"}


def test_update_autoscale_vm_group_policyids_serialize_to_csv():
    req = UpdateAutoScaleVmGroupRequest(id="group-1", scaleDownPolicyIds=["d1", "d2"], scaleUpPolicyIds=["u1"])
    dumped = req.model_dump(exclude_none=True)
    assert dumped["scaledownpolicyids"] == "d1,d2"
    assert dumped["scaleuppolicyids"] == "u1"


def test_delete_autoscale_vm_group_optional_cleanup():
    req = DeleteAutoScaleVmGroupRequest(id="group-1", cleanup=True)
    dumped = req.model_dump(exclude_none=True)
    assert dumped == {"id": "group-1", "cleanup": True}


def test_delete_autoscale_vm_group_missing_id_raises():
    with pytest.raises(ValidationError):
        DeleteAutoScaleVmGroupRequest()


def test_enable_autoscale_vm_group_required_id():
    req = EnableAutoScaleVmGroupRequest(id="group-1")
    assert req.model_dump(exclude_none=True) == {"id": "group-1"}


def test_disable_autoscale_vm_group_required_id():
    req = DisableAutoScaleVmGroupRequest(id="group-1")
    assert req.model_dump(exclude_none=True) == {"id": "group-1"}


def test_list_autoscale_vm_groups_all_fields_optional():
    req = ListAutoScaleVmGroupsRequest()
    dumped = req.model_dump(exclude_none=True)
    assert dumped == {"page": 1, "pagesize": 50}


def test_list_autoscale_vm_groups_aliases_serialize_to_snake_case():
    req = ListAutoScaleVmGroupsRequest(lbRuleId="lb-1", policyId="policy-1", vmProfileId="profile-1", zoneId="zone-1")
    dumped = req.model_dump(exclude_none=True)
    assert dumped["lbruleid"] == "lb-1"
    assert dumped["policyid"] == "policy-1"
    assert dumped["vmprofileid"] == "profile-1"
    assert dumped["zoneid"] == "zone-1"


# ---------------------------------------------------------------------------
# Conditions
# ---------------------------------------------------------------------------

def test_create_condition_required_fields_serialize():
    req = CreateConditionRequest(counterId="counter-1", relationalOperator="GT", threshold=80)
    dumped = req.model_dump(exclude_none=True)
    assert dumped == {"counterid": "counter-1", "relationaloperator": "GT", "threshold": 80.0}


def test_create_condition_missing_required_fields_raises():
    with pytest.raises(ValidationError):
        CreateConditionRequest()


def test_update_condition_required_fields_serialize():
    req = UpdateConditionRequest(id="cond-1", relationalOperator="LE", threshold=10)
    dumped = req.model_dump(exclude_none=True)
    assert dumped == {"id": "cond-1", "relationaloperator": "LE", "threshold": 10.0}


def test_delete_condition_missing_id_raises():
    with pytest.raises(ValidationError):
        DeleteConditionRequest()


def test_list_conditions_all_fields_optional():
    req = ListConditionsRequest()
    dumped = req.model_dump(exclude_none=True)
    assert dumped == {"page": 1, "pagesize": 50}


def test_list_conditions_aliases_serialize_to_snake_case():
    req = ListConditionsRequest(counterId="counter-1", policyId="policy-1")
    dumped = req.model_dump(exclude_none=True)
    assert dumped["counterid"] == "counter-1"
    assert dumped["policyid"] == "policy-1"


# ---------------------------------------------------------------------------
# Counters
# ---------------------------------------------------------------------------

def test_create_counter_required_fields_serialize():
    req = CreateCounterRequest(name="cpu-usage", provider="VirtualRouter", source="cpu", value="1.3.6.1.4.1")
    dumped = req.model_dump(exclude_none=True)
    assert dumped == {
        "name": "cpu-usage",
        "provider": "VirtualRouter",
        "source": "cpu",
        "value": "1.3.6.1.4.1",
    }


def test_create_counter_missing_required_fields_raises():
    with pytest.raises(ValidationError):
        CreateCounterRequest()


def test_delete_counter_missing_id_raises():
    with pytest.raises(ValidationError):
        DeleteCounterRequest()


def test_list_counters_all_fields_optional():
    req = ListCountersRequest()
    dumped = req.model_dump(exclude_none=True)
    assert dumped == {"page": 1, "pagesize": 50}
