import asyncio
from unittest.mock import AsyncMock, Mock

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
    UpdateAutoScalePolicyRequest,
    UpdateAutoScaleVmGroupRequest,
    UpdateAutoScaleVmProfileRequest,
    UpdateConditionRequest,
)
from acs_sdk.services.autoscale import AutoScale


# ---------------------------------------------------------------------------
# AutoScale policies
# ---------------------------------------------------------------------------


def test_autoscale_create_policy_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {"createautoscalepolicyresponse": {"id": "policy-1"}}

    svc = AutoScale(client=mock_client)
    payload = CreateAutoScalePolicyRequest(action="scaleup", conditionIds=["cond-1"], duration=60)
    response = svc.create_policy(payload)

    assert response.data == {"id": "policy-1"}
    mock_client.call.assert_called_once_with(
        "createAutoScalePolicy", payload.model_dump(exclude_none=True)
    )


def test_autoscale_create_policy_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={"createautoscalepolicyresponse": {"id": "policy-1"}}
    )

    svc = AutoScale(client=mock_client)
    payload = CreateAutoScalePolicyRequest(action="scaleup", conditionIds=["cond-1"], duration=60)
    response = asyncio.run(svc.create_policy_async(payload))

    assert response.data == {"id": "policy-1"}
    mock_client.call_async.assert_called_once_with(
        "createAutoScalePolicy", payload.model_dump(exclude_none=True)
    )


def test_autoscale_list_policies_parses_list_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "listautoscalepoliciesresponse": {"autoscalepolicy": [{"id": "policy-1"}], "count": 1}
    }

    svc = AutoScale(client=mock_client)
    payload = ListAutoScalePoliciesRequest()
    response = svc.list_policies(payload)

    assert response.data == [{"id": "policy-1"}]
    assert response.count == 1
    mock_client.call.assert_called_once_with(
        "listAutoScalePolicies", payload.model_dump(exclude_none=True)
    )


def test_autoscale_list_policies_async_parses_list_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={
            "listautoscalepoliciesresponse": {"autoscalepolicy": [{"id": "policy-1"}], "count": 1}
        }
    )

    svc = AutoScale(client=mock_client)
    payload = ListAutoScalePoliciesRequest()
    response = asyncio.run(svc.list_policies_async(payload))

    assert response.data == [{"id": "policy-1"}]
    assert response.count == 1
    mock_client.call_async.assert_called_once_with(
        "listAutoScalePolicies", payload.model_dump(exclude_none=True)
    )


def test_autoscale_update_policy_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {"updateautoscalepolicyresponse": {"id": "policy-1"}}

    svc = AutoScale(client=mock_client)
    payload = UpdateAutoScalePolicyRequest(id="policy-1", name="renamed")
    response = svc.update_policy(payload)

    assert response.data == {"id": "policy-1"}
    mock_client.call.assert_called_once_with(
        "updateAutoScalePolicy", payload.model_dump(exclude_none=True)
    )


def test_autoscale_update_policy_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={"updateautoscalepolicyresponse": {"id": "policy-1"}}
    )

    svc = AutoScale(client=mock_client)
    payload = UpdateAutoScalePolicyRequest(id="policy-1", name="renamed")
    response = asyncio.run(svc.update_policy_async(payload))

    assert response.data == {"id": "policy-1"}
    mock_client.call_async.assert_called_once_with(
        "updateAutoScalePolicy", payload.model_dump(exclude_none=True)
    )


def test_autoscale_delete_policy_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {"deleteautoscalepolicyresponse": {"success": "true"}}

    svc = AutoScale(client=mock_client)
    payload = DeleteAutoScalePolicyRequest(id="policy-1")
    response = svc.delete_policy(payload)

    assert response.data == {"success": "true"}
    mock_client.call.assert_called_once_with("deleteAutoScalePolicy", {"id": "policy-1"})


def test_autoscale_delete_policy_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={"deleteautoscalepolicyresponse": {"success": "true"}}
    )

    svc = AutoScale(client=mock_client)
    payload = DeleteAutoScalePolicyRequest(id="policy-1")
    response = asyncio.run(svc.delete_policy_async(payload))

    assert response.data == {"success": "true"}
    mock_client.call_async.assert_called_once_with("deleteAutoScalePolicy", {"id": "policy-1"})


# ---------------------------------------------------------------------------
# AutoScale VM profiles
# ---------------------------------------------------------------------------


def test_autoscale_create_vm_profile_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {"createautoscalevmprofileresponse": {"id": "profile-1"}}

    svc = AutoScale(client=mock_client)
    payload = CreateAutoScaleVmProfileRequest(
        serviceOfferingId="so-1", templateId="tpl-1", zoneId="zone-1"
    )
    response = svc.create_vm_profile(payload)

    assert response.data == {"id": "profile-1"}
    mock_client.call.assert_called_once_with(
        "createAutoScaleVmProfile", payload.model_dump(exclude_none=True)
    )


def test_autoscale_create_vm_profile_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={"createautoscalevmprofileresponse": {"id": "profile-1"}}
    )

    svc = AutoScale(client=mock_client)
    payload = CreateAutoScaleVmProfileRequest(
        serviceOfferingId="so-1", templateId="tpl-1", zoneId="zone-1"
    )
    response = asyncio.run(svc.create_vm_profile_async(payload))

    assert response.data == {"id": "profile-1"}
    mock_client.call_async.assert_called_once_with(
        "createAutoScaleVmProfile", payload.model_dump(exclude_none=True)
    )


def test_autoscale_list_vm_profiles_parses_list_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "listautoscalevmprofilesresponse": {"autoscalevmprofile": [{"id": "profile-1"}], "count": 1}
    }

    svc = AutoScale(client=mock_client)
    payload = ListAutoScaleVmProfilesRequest()
    response = svc.list_vm_profiles(payload)

    assert response.data == [{"id": "profile-1"}]
    assert response.count == 1
    mock_client.call.assert_called_once_with(
        "listAutoScaleVmProfiles", payload.model_dump(exclude_none=True)
    )


def test_autoscale_list_vm_profiles_async_parses_list_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={
            "listautoscalevmprofilesresponse": {
                "autoscalevmprofile": [{"id": "profile-1"}],
                "count": 1,
            }
        }
    )

    svc = AutoScale(client=mock_client)
    payload = ListAutoScaleVmProfilesRequest()
    response = asyncio.run(svc.list_vm_profiles_async(payload))

    assert response.data == [{"id": "profile-1"}]
    assert response.count == 1
    mock_client.call_async.assert_called_once_with(
        "listAutoScaleVmProfiles", payload.model_dump(exclude_none=True)
    )


def test_autoscale_update_vm_profile_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {"updateautoscalevmprofileresponse": {"id": "profile-1"}}

    svc = AutoScale(client=mock_client)
    payload = UpdateAutoScaleVmProfileRequest(id="profile-1")
    response = svc.update_vm_profile(payload)

    assert response.data == {"id": "profile-1"}
    mock_client.call.assert_called_once_with(
        "updateAutoScaleVmProfile", payload.model_dump(exclude_none=True)
    )


def test_autoscale_update_vm_profile_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={"updateautoscalevmprofileresponse": {"id": "profile-1"}}
    )

    svc = AutoScale(client=mock_client)
    payload = UpdateAutoScaleVmProfileRequest(id="profile-1")
    response = asyncio.run(svc.update_vm_profile_async(payload))

    assert response.data == {"id": "profile-1"}
    mock_client.call_async.assert_called_once_with(
        "updateAutoScaleVmProfile", payload.model_dump(exclude_none=True)
    )


def test_autoscale_delete_vm_profile_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {"deleteautoscalevmprofileresponse": {"success": "true"}}

    svc = AutoScale(client=mock_client)
    payload = DeleteAutoScaleVmProfileRequest(id="profile-1")
    response = svc.delete_vm_profile(payload)

    assert response.data == {"success": "true"}
    mock_client.call.assert_called_once_with("deleteAutoScaleVmProfile", {"id": "profile-1"})


def test_autoscale_delete_vm_profile_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={"deleteautoscalevmprofileresponse": {"success": "true"}}
    )

    svc = AutoScale(client=mock_client)
    payload = DeleteAutoScaleVmProfileRequest(id="profile-1")
    response = asyncio.run(svc.delete_vm_profile_async(payload))

    assert response.data == {"success": "true"}
    mock_client.call_async.assert_called_once_with("deleteAutoScaleVmProfile", {"id": "profile-1"})


# ---------------------------------------------------------------------------
# AutoScale VM groups
# ---------------------------------------------------------------------------


def test_autoscale_create_vm_group_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {"createautoscalevmgroupresponse": {"id": "group-1"}}

    svc = AutoScale(client=mock_client)
    payload = CreateAutoScaleVmGroupRequest(
        lbRuleId="lb-1",
        maxMembers=5,
        minMembers=1,
        scaleDownPolicyIds=["down-1"],
        scaleUpPolicyIds=["up-1"],
        vmProfileId="profile-1",
    )
    response = svc.create_vm_group(payload)

    assert response.data == {"id": "group-1"}
    mock_client.call.assert_called_once_with(
        "createAutoScaleVmGroup", payload.model_dump(exclude_none=True)
    )


def test_autoscale_create_vm_group_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={"createautoscalevmgroupresponse": {"id": "group-1"}}
    )

    svc = AutoScale(client=mock_client)
    payload = CreateAutoScaleVmGroupRequest(
        lbRuleId="lb-1",
        maxMembers=5,
        minMembers=1,
        scaleDownPolicyIds=["down-1"],
        scaleUpPolicyIds=["up-1"],
        vmProfileId="profile-1",
    )
    response = asyncio.run(svc.create_vm_group_async(payload))

    assert response.data == {"id": "group-1"}
    mock_client.call_async.assert_called_once_with(
        "createAutoScaleVmGroup", payload.model_dump(exclude_none=True)
    )


def test_autoscale_list_vm_groups_parses_list_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "listautoscalevmgroupsresponse": {"autoscalevmgroup": [{"id": "group-1"}], "count": 1}
    }

    svc = AutoScale(client=mock_client)
    payload = ListAutoScaleVmGroupsRequest()
    response = svc.list_vm_groups(payload)

    assert response.data == [{"id": "group-1"}]
    assert response.count == 1
    mock_client.call.assert_called_once_with(
        "listAutoScaleVmGroups", payload.model_dump(exclude_none=True)
    )


def test_autoscale_list_vm_groups_async_parses_list_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={
            "listautoscalevmgroupsresponse": {"autoscalevmgroup": [{"id": "group-1"}], "count": 1}
        }
    )

    svc = AutoScale(client=mock_client)
    payload = ListAutoScaleVmGroupsRequest()
    response = asyncio.run(svc.list_vm_groups_async(payload))

    assert response.data == [{"id": "group-1"}]
    assert response.count == 1
    mock_client.call_async.assert_called_once_with(
        "listAutoScaleVmGroups", payload.model_dump(exclude_none=True)
    )


def test_autoscale_update_vm_group_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {"updateautoscalevmgroupresponse": {"id": "group-1"}}

    svc = AutoScale(client=mock_client)
    payload = UpdateAutoScaleVmGroupRequest(id="group-1", name="renamed")
    response = svc.update_vm_group(payload)

    assert response.data == {"id": "group-1"}
    mock_client.call.assert_called_once_with(
        "updateAutoScaleVmGroup", payload.model_dump(exclude_none=True)
    )


def test_autoscale_update_vm_group_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={"updateautoscalevmgroupresponse": {"id": "group-1"}}
    )

    svc = AutoScale(client=mock_client)
    payload = UpdateAutoScaleVmGroupRequest(id="group-1", name="renamed")
    response = asyncio.run(svc.update_vm_group_async(payload))

    assert response.data == {"id": "group-1"}
    mock_client.call_async.assert_called_once_with(
        "updateAutoScaleVmGroup", payload.model_dump(exclude_none=True)
    )


def test_autoscale_delete_vm_group_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {"deleteautoscalevmgroupresponse": {"success": "true"}}

    svc = AutoScale(client=mock_client)
    payload = DeleteAutoScaleVmGroupRequest(id="group-1")
    response = svc.delete_vm_group(payload)

    assert response.data == {"success": "true"}
    mock_client.call.assert_called_once_with("deleteAutoScaleVmGroup", {"id": "group-1"})


def test_autoscale_delete_vm_group_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={"deleteautoscalevmgroupresponse": {"success": "true"}}
    )

    svc = AutoScale(client=mock_client)
    payload = DeleteAutoScaleVmGroupRequest(id="group-1")
    response = asyncio.run(svc.delete_vm_group_async(payload))

    assert response.data == {"success": "true"}
    mock_client.call_async.assert_called_once_with("deleteAutoScaleVmGroup", {"id": "group-1"})


def test_autoscale_enable_vm_group_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "enableautoscalevmgroupresponse": {"id": "group-1", "state": "Enabled"}
    }

    svc = AutoScale(client=mock_client)
    payload = EnableAutoScaleVmGroupRequest(id="group-1")
    response = svc.enable_vm_group(payload)

    assert response.data == {"id": "group-1", "state": "Enabled"}
    mock_client.call.assert_called_once_with("enableAutoScaleVmGroup", {"id": "group-1"})


def test_autoscale_enable_vm_group_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={"enableautoscalevmgroupresponse": {"id": "group-1", "state": "Enabled"}}
    )

    svc = AutoScale(client=mock_client)
    payload = EnableAutoScaleVmGroupRequest(id="group-1")
    response = asyncio.run(svc.enable_vm_group_async(payload))

    assert response.data == {"id": "group-1", "state": "Enabled"}
    mock_client.call_async.assert_called_once_with("enableAutoScaleVmGroup", {"id": "group-1"})


def test_autoscale_disable_vm_group_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "disableautoscalevmgroupresponse": {"id": "group-1", "state": "Disabled"}
    }

    svc = AutoScale(client=mock_client)
    payload = DisableAutoScaleVmGroupRequest(id="group-1")
    response = svc.disable_vm_group(payload)

    assert response.data == {"id": "group-1", "state": "Disabled"}
    mock_client.call.assert_called_once_with("disableAutoScaleVmGroup", {"id": "group-1"})


def test_autoscale_disable_vm_group_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={"disableautoscalevmgroupresponse": {"id": "group-1", "state": "Disabled"}}
    )

    svc = AutoScale(client=mock_client)
    payload = DisableAutoScaleVmGroupRequest(id="group-1")
    response = asyncio.run(svc.disable_vm_group_async(payload))

    assert response.data == {"id": "group-1", "state": "Disabled"}
    mock_client.call_async.assert_called_once_with("disableAutoScaleVmGroup", {"id": "group-1"})


# ---------------------------------------------------------------------------
# Conditions
# ---------------------------------------------------------------------------


def test_autoscale_create_condition_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {"createconditionresponse": {"id": "cond-1"}}

    svc = AutoScale(client=mock_client)
    payload = CreateConditionRequest(counterId="counter-1", relationalOperator="GT", threshold=80)
    response = svc.create_condition(payload)

    assert response.data == {"id": "cond-1"}
    mock_client.call.assert_called_once_with(
        "createCondition", payload.model_dump(exclude_none=True)
    )


def test_autoscale_create_condition_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(return_value={"createconditionresponse": {"id": "cond-1"}})

    svc = AutoScale(client=mock_client)
    payload = CreateConditionRequest(counterId="counter-1", relationalOperator="GT", threshold=80)
    response = asyncio.run(svc.create_condition_async(payload))

    assert response.data == {"id": "cond-1"}
    mock_client.call_async.assert_called_once_with(
        "createCondition", payload.model_dump(exclude_none=True)
    )


def test_autoscale_list_conditions_parses_list_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "listconditionsresponse": {"condition": [{"id": "cond-1"}], "count": 1}
    }

    svc = AutoScale(client=mock_client)
    payload = ListConditionsRequest()
    response = svc.list_conditions(payload)

    assert response.data == [{"id": "cond-1"}]
    assert response.count == 1
    mock_client.call.assert_called_once_with(
        "listConditions", payload.model_dump(exclude_none=True)
    )


def test_autoscale_list_conditions_async_parses_list_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={"listconditionsresponse": {"condition": [{"id": "cond-1"}], "count": 1}}
    )

    svc = AutoScale(client=mock_client)
    payload = ListConditionsRequest()
    response = asyncio.run(svc.list_conditions_async(payload))

    assert response.data == [{"id": "cond-1"}]
    assert response.count == 1
    mock_client.call_async.assert_called_once_with(
        "listConditions", payload.model_dump(exclude_none=True)
    )


def test_autoscale_update_condition_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {"updateconditionresponse": {"id": "cond-1"}}

    svc = AutoScale(client=mock_client)
    payload = UpdateConditionRequest(id="cond-1", relationalOperator="LE", threshold=10)
    response = svc.update_condition(payload)

    assert response.data == {"id": "cond-1"}
    mock_client.call.assert_called_once_with(
        "updateCondition", payload.model_dump(exclude_none=True)
    )


def test_autoscale_update_condition_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(return_value={"updateconditionresponse": {"id": "cond-1"}})

    svc = AutoScale(client=mock_client)
    payload = UpdateConditionRequest(id="cond-1", relationalOperator="LE", threshold=10)
    response = asyncio.run(svc.update_condition_async(payload))

    assert response.data == {"id": "cond-1"}
    mock_client.call_async.assert_called_once_with(
        "updateCondition", payload.model_dump(exclude_none=True)
    )


def test_autoscale_delete_condition_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {"deleteconditionresponse": {"success": "true"}}

    svc = AutoScale(client=mock_client)
    payload = DeleteConditionRequest(id="cond-1")
    response = svc.delete_condition(payload)

    assert response.data == {"success": "true"}
    mock_client.call.assert_called_once_with("deleteCondition", {"id": "cond-1"})


def test_autoscale_delete_condition_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={"deleteconditionresponse": {"success": "true"}}
    )

    svc = AutoScale(client=mock_client)
    payload = DeleteConditionRequest(id="cond-1")
    response = asyncio.run(svc.delete_condition_async(payload))

    assert response.data == {"success": "true"}
    mock_client.call_async.assert_called_once_with("deleteCondition", {"id": "cond-1"})


# ---------------------------------------------------------------------------
# Counters
# ---------------------------------------------------------------------------


def test_autoscale_create_counter_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {"createcounterresponse": {"id": "counter-1"}}

    svc = AutoScale(client=mock_client)
    payload = CreateCounterRequest(
        name="cpu-usage", provider="VirtualRouter", source="cpu", value="1.3.6.1.4.1"
    )
    response = svc.create_counter(payload)

    assert response.data == {"id": "counter-1"}
    mock_client.call.assert_called_once_with("createCounter", payload.model_dump(exclude_none=True))


def test_autoscale_create_counter_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(return_value={"createcounterresponse": {"id": "counter-1"}})

    svc = AutoScale(client=mock_client)
    payload = CreateCounterRequest(
        name="cpu-usage", provider="VirtualRouter", source="cpu", value="1.3.6.1.4.1"
    )
    response = asyncio.run(svc.create_counter_async(payload))

    assert response.data == {"id": "counter-1"}
    mock_client.call_async.assert_called_once_with(
        "createCounter", payload.model_dump(exclude_none=True)
    )


def test_autoscale_list_counters_parses_list_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "listcountersresponse": {"counter": [{"id": "counter-1"}], "count": 1}
    }

    svc = AutoScale(client=mock_client)
    payload = ListCountersRequest()
    response = svc.list_counters(payload)

    assert response.data == [{"id": "counter-1"}]
    assert response.count == 1
    mock_client.call.assert_called_once_with("listCounters", payload.model_dump(exclude_none=True))


def test_autoscale_list_counters_async_parses_list_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={"listcountersresponse": {"counter": [{"id": "counter-1"}], "count": 1}}
    )

    svc = AutoScale(client=mock_client)
    payload = ListCountersRequest()
    response = asyncio.run(svc.list_counters_async(payload))

    assert response.data == [{"id": "counter-1"}]
    assert response.count == 1
    mock_client.call_async.assert_called_once_with(
        "listCounters", payload.model_dump(exclude_none=True)
    )


def test_autoscale_delete_counter_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {"deletecounterresponse": {"success": "true"}}

    svc = AutoScale(client=mock_client)
    payload = DeleteCounterRequest(id="counter-1")
    response = svc.delete_counter(payload)

    assert response.data == {"success": "true"}
    mock_client.call.assert_called_once_with("deleteCounter", {"id": "counter-1"})


def test_autoscale_delete_counter_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(return_value={"deletecounterresponse": {"success": "true"}})

    svc = AutoScale(client=mock_client)
    payload = DeleteCounterRequest(id="counter-1")
    response = asyncio.run(svc.delete_counter_async(payload))

    assert response.data == {"success": "true"}
    mock_client.call_async.assert_called_once_with("deleteCounter", {"id": "counter-1"})
