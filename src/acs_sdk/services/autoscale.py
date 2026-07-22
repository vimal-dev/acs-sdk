# services/autoscale.py
from typing import Dict, List

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

from .base import BaseService
from ..schemas.response.base import APIResponse


class AutoScale(BaseService):
    # -------------------------------------------------------------------
    # AutoScale policies
    # -------------------------------------------------------------------

    def create_policy(self, payload: CreateAutoScalePolicyRequest) -> APIResponse[Dict]:
        """Create an autoscale policy."""
        return self._execute("createAutoScalePolicy", payload, envelope="createautoscalepolicyresponse")

    async def create_policy_async(self, payload: CreateAutoScalePolicyRequest) -> APIResponse[Dict]:
        """Asynchronously create an autoscale policy."""
        return await self._execute_async("createAutoScalePolicy", payload, envelope="createautoscalepolicyresponse")

    def list_policies(self, payload: ListAutoScalePoliciesRequest) -> APIResponse[List[Dict]]:
        """List autoscale policies."""
        return self._execute(
            "listAutoScalePolicies", payload, envelope="listautoscalepoliciesresponse", entity="autoscalepolicy"
        )

    async def list_policies_async(self, payload: ListAutoScalePoliciesRequest) -> APIResponse[List[Dict]]:
        """Asynchronously list autoscale policies."""
        return await self._execute_async(
            "listAutoScalePolicies", payload, envelope="listautoscalepoliciesresponse", entity="autoscalepolicy"
        )

    def update_policy(self, payload: UpdateAutoScalePolicyRequest) -> APIResponse[Dict]:
        """Update an autoscale policy."""
        return self._execute("updateAutoScalePolicy", payload, envelope="updateautoscalepolicyresponse")

    async def update_policy_async(self, payload: UpdateAutoScalePolicyRequest) -> APIResponse[Dict]:
        """Asynchronously update an autoscale policy."""
        return await self._execute_async("updateAutoScalePolicy", payload, envelope="updateautoscalepolicyresponse")

    def delete_policy(self, payload: DeleteAutoScalePolicyRequest) -> APIResponse[Dict]:
        """Delete an autoscale policy."""
        return self._execute("deleteAutoScalePolicy", payload, envelope="deleteautoscalepolicyresponse")

    async def delete_policy_async(self, payload: DeleteAutoScalePolicyRequest) -> APIResponse[Dict]:
        """Asynchronously delete an autoscale policy."""
        return await self._execute_async("deleteAutoScalePolicy", payload, envelope="deleteautoscalepolicyresponse")

    # -------------------------------------------------------------------
    # AutoScale VM profiles
    # -------------------------------------------------------------------

    def create_vm_profile(self, payload: CreateAutoScaleVmProfileRequest) -> APIResponse[Dict]:
        """Create an autoscale VM profile."""
        return self._execute("createAutoScaleVmProfile", payload, envelope="createautoscalevmprofileresponse")

    async def create_vm_profile_async(self, payload: CreateAutoScaleVmProfileRequest) -> APIResponse[Dict]:
        """Asynchronously create an autoscale VM profile."""
        return await self._execute_async(
            "createAutoScaleVmProfile", payload, envelope="createautoscalevmprofileresponse"
        )

    def list_vm_profiles(self, payload: ListAutoScaleVmProfilesRequest) -> APIResponse[List[Dict]]:
        """List autoscale VM profiles."""
        return self._execute(
            "listAutoScaleVmProfiles", payload, envelope="listautoscalevmprofilesresponse", entity="autoscalevmprofile"
        )

    async def list_vm_profiles_async(self, payload: ListAutoScaleVmProfilesRequest) -> APIResponse[List[Dict]]:
        """Asynchronously list autoscale VM profiles."""
        return await self._execute_async(
            "listAutoScaleVmProfiles", payload, envelope="listautoscalevmprofilesresponse", entity="autoscalevmprofile"
        )

    def update_vm_profile(self, payload: UpdateAutoScaleVmProfileRequest) -> APIResponse[Dict]:
        """Update an autoscale VM profile."""
        return self._execute("updateAutoScaleVmProfile", payload, envelope="updateautoscalevmprofileresponse")

    async def update_vm_profile_async(self, payload: UpdateAutoScaleVmProfileRequest) -> APIResponse[Dict]:
        """Asynchronously update an autoscale VM profile."""
        return await self._execute_async(
            "updateAutoScaleVmProfile", payload, envelope="updateautoscalevmprofileresponse"
        )

    def delete_vm_profile(self, payload: DeleteAutoScaleVmProfileRequest) -> APIResponse[Dict]:
        """Delete an autoscale VM profile."""
        return self._execute("deleteAutoScaleVmProfile", payload, envelope="deleteautoscalevmprofileresponse")

    async def delete_vm_profile_async(self, payload: DeleteAutoScaleVmProfileRequest) -> APIResponse[Dict]:
        """Asynchronously delete an autoscale VM profile."""
        return await self._execute_async(
            "deleteAutoScaleVmProfile", payload, envelope="deleteautoscalevmprofileresponse"
        )

    # -------------------------------------------------------------------
    # AutoScale VM groups
    # -------------------------------------------------------------------

    def create_vm_group(self, payload: CreateAutoScaleVmGroupRequest) -> APIResponse[Dict]:
        """Create an autoscale VM group."""
        return self._execute("createAutoScaleVmGroup", payload, envelope="createautoscalevmgroupresponse")

    async def create_vm_group_async(self, payload: CreateAutoScaleVmGroupRequest) -> APIResponse[Dict]:
        """Asynchronously create an autoscale VM group."""
        return await self._execute_async("createAutoScaleVmGroup", payload, envelope="createautoscalevmgroupresponse")

    def list_vm_groups(self, payload: ListAutoScaleVmGroupsRequest) -> APIResponse[List[Dict]]:
        """List autoscale VM groups."""
        return self._execute(
            "listAutoScaleVmGroups", payload, envelope="listautoscalevmgroupsresponse", entity="autoscalevmgroup"
        )

    async def list_vm_groups_async(self, payload: ListAutoScaleVmGroupsRequest) -> APIResponse[List[Dict]]:
        """Asynchronously list autoscale VM groups."""
        return await self._execute_async(
            "listAutoScaleVmGroups", payload, envelope="listautoscalevmgroupsresponse", entity="autoscalevmgroup"
        )

    def update_vm_group(self, payload: UpdateAutoScaleVmGroupRequest) -> APIResponse[Dict]:
        """Update an autoscale VM group."""
        return self._execute("updateAutoScaleVmGroup", payload, envelope="updateautoscalevmgroupresponse")

    async def update_vm_group_async(self, payload: UpdateAutoScaleVmGroupRequest) -> APIResponse[Dict]:
        """Asynchronously update an autoscale VM group."""
        return await self._execute_async("updateAutoScaleVmGroup", payload, envelope="updateautoscalevmgroupresponse")

    def delete_vm_group(self, payload: DeleteAutoScaleVmGroupRequest) -> APIResponse[Dict]:
        """Delete an autoscale VM group."""
        return self._execute("deleteAutoScaleVmGroup", payload, envelope="deleteautoscalevmgroupresponse")

    async def delete_vm_group_async(self, payload: DeleteAutoScaleVmGroupRequest) -> APIResponse[Dict]:
        """Asynchronously delete an autoscale VM group."""
        return await self._execute_async("deleteAutoScaleVmGroup", payload, envelope="deleteautoscalevmgroupresponse")

    def enable_vm_group(self, payload: EnableAutoScaleVmGroupRequest) -> APIResponse[Dict]:
        """Enable an autoscale VM group."""
        return self._execute("enableAutoScaleVmGroup", payload, envelope="enableautoscalevmgroupresponse")

    async def enable_vm_group_async(self, payload: EnableAutoScaleVmGroupRequest) -> APIResponse[Dict]:
        """Asynchronously enable an autoscale VM group."""
        return await self._execute_async("enableAutoScaleVmGroup", payload, envelope="enableautoscalevmgroupresponse")

    def disable_vm_group(self, payload: DisableAutoScaleVmGroupRequest) -> APIResponse[Dict]:
        """Disable an autoscale VM group."""
        return self._execute("disableAutoScaleVmGroup", payload, envelope="disableautoscalevmgroupresponse")

    async def disable_vm_group_async(self, payload: DisableAutoScaleVmGroupRequest) -> APIResponse[Dict]:
        """Asynchronously disable an autoscale VM group."""
        return await self._execute_async(
            "disableAutoScaleVmGroup", payload, envelope="disableautoscalevmgroupresponse"
        )

    # -------------------------------------------------------------------
    # Conditions
    # -------------------------------------------------------------------

    def create_condition(self, payload: CreateConditionRequest) -> APIResponse[Dict]:
        """Create a condition."""
        return self._execute("createCondition", payload, envelope="createconditionresponse")

    async def create_condition_async(self, payload: CreateConditionRequest) -> APIResponse[Dict]:
        """Asynchronously create a condition."""
        return await self._execute_async("createCondition", payload, envelope="createconditionresponse")

    def list_conditions(self, payload: ListConditionsRequest) -> APIResponse[List[Dict]]:
        """List conditions."""
        return self._execute("listConditions", payload, envelope="listconditionsresponse", entity="condition")

    async def list_conditions_async(self, payload: ListConditionsRequest) -> APIResponse[List[Dict]]:
        """Asynchronously list conditions."""
        return await self._execute_async(
            "listConditions", payload, envelope="listconditionsresponse", entity="condition"
        )

    def update_condition(self, payload: UpdateConditionRequest) -> APIResponse[Dict]:
        """Update a condition."""
        return self._execute("updateCondition", payload, envelope="updateconditionresponse")

    async def update_condition_async(self, payload: UpdateConditionRequest) -> APIResponse[Dict]:
        """Asynchronously update a condition."""
        return await self._execute_async("updateCondition", payload, envelope="updateconditionresponse")

    def delete_condition(self, payload: DeleteConditionRequest) -> APIResponse[Dict]:
        """Delete a condition."""
        return self._execute("deleteCondition", payload, envelope="deleteconditionresponse")

    async def delete_condition_async(self, payload: DeleteConditionRequest) -> APIResponse[Dict]:
        """Asynchronously delete a condition."""
        return await self._execute_async("deleteCondition", payload, envelope="deleteconditionresponse")

    # -------------------------------------------------------------------
    # Counters
    # -------------------------------------------------------------------

    def create_counter(self, payload: CreateCounterRequest) -> APIResponse[Dict]:
        """Create a counter."""
        return self._execute("createCounter", payload, envelope="createcounterresponse")

    async def create_counter_async(self, payload: CreateCounterRequest) -> APIResponse[Dict]:
        """Asynchronously create a counter."""
        return await self._execute_async("createCounter", payload, envelope="createcounterresponse")

    def list_counters(self, payload: ListCountersRequest) -> APIResponse[List[Dict]]:
        """List counters."""
        return self._execute("listCounters", payload, envelope="listcountersresponse", entity="counter")

    async def list_counters_async(self, payload: ListCountersRequest) -> APIResponse[List[Dict]]:
        """Asynchronously list counters."""
        return await self._execute_async("listCounters", payload, envelope="listcountersresponse", entity="counter")

    def delete_counter(self, payload: DeleteCounterRequest) -> APIResponse[Dict]:
        """Delete a counter."""
        return self._execute("deleteCounter", payload, envelope="deletecounterresponse")

    async def delete_counter_async(self, payload: DeleteCounterRequest) -> APIResponse[Dict]:
        """Asynchronously delete a counter."""
        return await self._execute_async("deleteCounter", payload, envelope="deletecounterresponse")
