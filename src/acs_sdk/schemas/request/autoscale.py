# schemas/request/autoscale.py
from typing import Any, Dict, List, Literal, Optional

from pydantic import BaseModel, Field, field_serializer

from acs_sdk.schemas.request.base import APIRequest, PaginationMixin

AutoScaleAction = Literal["scaleup", "scaledown"]
RelationalOperator = Literal["EQ", "GT", "LT", "GE", "LE"]


def _flatten_indexed(data: Dict[str, Any], fields: List[str]) -> Dict[str, Any]:
    for field in fields:
        value = data.pop(field, None)
        if value:
            for idx, item in enumerate(value):
                for key, val in item.items():
                    data[f"{field}[{idx}].{key}"] = val
    return data


# ---------------------------------------------------------------------------
# Helper models
# ---------------------------------------------------------------------------


class NameValueEntry(BaseModel):
    """One entry in a name/value indexed parameter list (e.g. counterparam[0].name=x&counterparam[0].value=y)."""

    name: str = Field(..., description="Name of the parameter")
    value: str = Field(..., description="Value of the parameter")


# ---------------------------------------------------------------------------
# AutoScale policies
# ---------------------------------------------------------------------------


class CreateAutoScalePolicyRequest(APIRequest):
    action: AutoScaleAction = Field(
        ..., description="The action to be executed if all the conditions evaluate to true for the specified duration"
    )
    conditionids: List[str] = Field(
        ..., alias="conditionIds", description="The list of IDs of the conditions that are being evaluated on every interval"
    )
    duration: int = Field(..., description="The duration in which the conditions have to be true before action is taken")
    name: Optional[str] = Field(None, description="The name of the autoscale policy")
    quiettime: Optional[int] = Field(
        None,
        alias="quietTime",
        description="The cool down period in which the policy should not be evaluated after the action has been taken",
    )

    @field_serializer("conditionids")
    def serialize_conditionids(self, value: List[str]) -> str:
        return ",".join(value)


class UpdateAutoScalePolicyRequest(APIRequest):
    id: str = Field(..., description="The ID of the autoscale policy")
    conditionids: Optional[List[str]] = Field(
        None, alias="conditionIds", description="The list of IDs of the conditions that are being evaluated on every interval"
    )
    duration: Optional[int] = Field(None, description="The duration in which the conditions have to be true before action is taken")
    name: Optional[str] = Field(None, description="The name of the autoscale policy")
    quiettime: Optional[int] = Field(
        None,
        alias="quietTime",
        description="The cool down period in which the policy should not be evaluated after the action has been taken",
    )

    @field_serializer("conditionids")
    def serialize_conditionids(self, value: Optional[List[str]]) -> Optional[str]:
        if value is None:
            return None
        return ",".join(value)


class DeleteAutoScalePolicyRequest(APIRequest):
    id: str = Field(..., description="The ID of the autoscale policy")


class ListAutoScalePoliciesRequest(APIRequest, PaginationMixin):
    account: Optional[str] = Field(None, description="List resources by account. Must be used with the domainId parameter.")
    action: Optional[AutoScaleAction] = Field(
        None, description="The action to be executed if all the conditions evaluate to true for the specified duration"
    )
    conditionid: Optional[str] = Field(None, alias="conditionId", description="The ID of the condition of the policy")
    domainid: Optional[str] = Field(None, alias="domainId", description="List only resources belonging to the domain specified")
    id: Optional[str] = Field(None, description="The ID of the autoscale policy")
    isrecursive: Optional[bool] = Field(
        None,
        alias="isRecursive",
        description="Defaults to false, but if true, lists all resources from the parent specified by the domainId till leaves.",
    )
    keyword: Optional[str] = Field(None, description="List by keyword")
    listall: Optional[bool] = Field(
        None,
        alias="listAll",
        description="If set to false, list only resources belonging to the command's caller; if set to true - list resources that the caller is authorized to see.",
    )
    name: Optional[str] = Field(None, description="The name of the autoscale policy")
    projectid: Optional[str] = Field(None, alias="projectId", description="List objects by project; if projectid=-1 lists All VMs")
    vmgroupid: Optional[str] = Field(None, alias="vmGroupId", description="The ID of the autoscale vm group")


# ---------------------------------------------------------------------------
# AutoScale VM profiles
# ---------------------------------------------------------------------------


class CreateAutoScaleVmProfileRequest(APIRequest):
    serviceofferingid: str = Field(
        ..., alias="serviceOfferingId", description="The service offering of the auto deployed virtual machine"
    )
    templateid: str = Field(..., alias="templateId", description="The template of the auto deployed virtual machine")
    zoneid: str = Field(..., alias="zoneId", description="Availability zone for the auto deployed virtual machine")
    account: Optional[str] = Field(None, description="Account that will own the autoscale VM profile")
    autoscaleuserid: Optional[str] = Field(
        None, alias="autoscaleUserId", description="The ID of the user used to launch and destroy the VMs"
    )
    counterparam: Optional[List[NameValueEntry]] = Field(
        None, alias="counterParam", description="Counterparam list. Example: counterparam[0].name=snmpcommunity&counterparam[0].value=public"
    )
    domainid: Optional[str] = Field(None, alias="domainId", description="Domain ID of the account owning a autoscale VM profile")
    expungevmgraceperiod: Optional[int] = Field(
        None,
        alias="expungeVmGracePeriod",
        description="The time allowed for existing connections to get closed before a vm is expunged",
    )
    fordisplay: Optional[bool] = Field(
        None, alias="forDisplay", description="An optional field, whether to the display the profile to the end user or not"
    )
    otherdeployparams: Optional[List[NameValueEntry]] = Field(
        None,
        alias="otherDeployParams",
        description="Parameters beyond zone/service offering/template, including rootdisksize, diskofferingid, size, securitygroupids, keypairs, affinitygroupids, networkids",
    )
    projectid: Optional[str] = Field(None, alias="projectId", description="An optional project for the autoscale VM profile")
    userdata: Optional[str] = Field(
        None, description="Base64 encoded userdata sent to the deployed virtual machine"
    )
    userdatadetails: Optional[List[NameValueEntry]] = Field(
        None, alias="userdataDetails", description="Used to specify the parameters values for the variables in userdata"
    )
    userdataid: Optional[str] = Field(None, alias="userdataId", description="The ID of the Userdata")

    def model_dump(self, *args, **kwargs) -> Dict[str, Any]:
        data = super().model_dump(*args, **kwargs)
        return _flatten_indexed(data, ["counterparam", "otherdeployparams", "userdatadetails"])


class UpdateAutoScaleVmProfileRequest(APIRequest):
    id: str = Field(..., description="The ID of the autoscale vm profile")
    autoscaleuserid: Optional[str] = Field(
        None, alias="autoscaleUserId", description="The ID of the user used to launch and destroy the VMs"
    )
    counterparam: Optional[List[NameValueEntry]] = Field(
        None, alias="counterParam", description="Counterparam list using name-value pairs (e.g. snmpcommunity, snmpport)"
    )
    customid: Optional[str] = Field(
        None, alias="customId", description="An optional custom ID for the resource. Allowed to Root Admins only."
    )
    expungevmgraceperiod: Optional[int] = Field(
        None, alias="expungeVmGracePeriod", description="The time allowed for existing connections to get closed before a vm is destroyed"
    )
    fordisplay: Optional[bool] = Field(
        None, alias="forDisplay", description="An optional field, whether to the display the profile to the end user or not"
    )
    otherdeployparams: Optional[List[NameValueEntry]] = Field(
        None,
        alias="otherDeployParams",
        description="Additional VM deployment parameters (rootdisksize, diskofferingid, size, securitygroupids, keypairs, affinitygroupids, networkids)",
    )
    serviceofferingid: Optional[str] = Field(
        None, alias="serviceOfferingId", description="The service offering of the auto deployed virtual machine"
    )
    templateid: Optional[str] = Field(None, alias="templateId", description="The template of the auto deployed virtual machine")
    userdata: Optional[str] = Field(None, description="Base64 encoded userdata sent to the deployed virtual machine")
    userdatadetails: Optional[List[NameValueEntry]] = Field(
        None, alias="userdataDetails", description="Parameter values for variables declared in userdata"
    )
    userdataid: Optional[str] = Field(None, alias="userdataId", description="The ID of the userdata")

    def model_dump(self, *args, **kwargs) -> Dict[str, Any]:
        data = super().model_dump(*args, **kwargs)
        return _flatten_indexed(data, ["counterparam", "otherdeployparams", "userdatadetails"])


class DeleteAutoScaleVmProfileRequest(APIRequest):
    id: str = Field(..., description="The ID of the autoscale profile")


class ListAutoScaleVmProfilesRequest(APIRequest, PaginationMixin):
    account: Optional[str] = Field(None, description="List resources by account. Must be used with the domainId parameter.")
    domainid: Optional[str] = Field(None, alias="domainId", description="List only resources belonging to the domain specified")
    fordisplay: Optional[bool] = Field(
        None, alias="forDisplay", description="List resources by display flag; only ROOT admin is eligible to pass this parameter"
    )
    id: Optional[str] = Field(None, description="The ID of the autoscale vm profile")
    isrecursive: Optional[bool] = Field(
        None,
        alias="isRecursive",
        description="Defaults to false, but if true, lists all resources from the parent specified by the domainId till leaves.",
    )
    keyword: Optional[str] = Field(None, description="List by keyword")
    listall: Optional[bool] = Field(
        None,
        alias="listAll",
        description="If set to false, list only resources belonging to the command's caller; if set to true - list resources that the caller is authorized to see.",
    )
    otherdeployparams: Optional[str] = Field(
        None, alias="otherDeployParams", description="The otherdeployparameters of the autoscale vm profile"
    )
    projectid: Optional[str] = Field(None, alias="projectId", description="List objects by project; if projectid=-1 lists All VMs")
    serviceofferingid: Optional[str] = Field(None, alias="serviceOfferingId", description="List profiles by service offering id")
    templateid: Optional[str] = Field(None, alias="templateId", description="The templateid of the autoscale vm profile")
    zoneid: Optional[str] = Field(None, alias="zoneId", description="Availability zone for the auto deployed virtual machine")


# ---------------------------------------------------------------------------
# AutoScale VM groups
# ---------------------------------------------------------------------------


class CreateAutoScaleVmGroupRequest(APIRequest):
    lbruleid: str = Field(..., alias="lbRuleId", description="The ID of the load balancer rule")
    maxmembers: int = Field(
        ...,
        alias="maxMembers",
        description="The maximum number of members in the vmgroup, the number of instances in the vm group will be equal to or less than this number.",
    )
    minmembers: int = Field(
        ...,
        alias="minMembers",
        description="The minimum number of members in the vmgroup, the number of instances in the vm group will be equal to or more than this number.",
    )
    scaledownpolicyids: List[str] = Field(
        ..., alias="scaleDownPolicyIds", description="List of scaledown autoscale policies"
    )
    scaleuppolicyids: List[str] = Field(..., alias="scaleUpPolicyIds", description="List of scaleup autoscale policies")
    vmprofileid: str = Field(
        ..., alias="vmProfileId", description="The autoscale profile that contains information about the vms in the vm group."
    )
    fordisplay: Optional[bool] = Field(
        None, alias="forDisplay", description="An optional field, whether to the display the group to the end user or not"
    )
    interval: Optional[int] = Field(None, description="The frequency in which the performance counters to be collected")
    name: Optional[str] = Field(None, description="The name of the autoscale vmgroup")

    @field_serializer("scaledownpolicyids", "scaleuppolicyids")
    def serialize_policyids(self, value: List[str]) -> str:
        return ",".join(value)


class UpdateAutoScaleVmGroupRequest(APIRequest):
    id: str = Field(..., description="The ID of the autoscale group")
    customid: Optional[str] = Field(
        None, alias="customId", description="An optional custom ID for the resource. Allowed to Root Admins only."
    )
    fordisplay: Optional[bool] = Field(
        None, alias="forDisplay", description="An optional field, whether to the display the group to the end user or not"
    )
    interval: Optional[int] = Field(None, description="The frequency in which the performance counters to be collected")
    maxmembers: Optional[int] = Field(
        None,
        alias="maxMembers",
        description="The maximum number of members in the vmgroup, the number of instances in the vm group will be equal to or less than this number",
    )
    minmembers: Optional[int] = Field(
        None,
        alias="minMembers",
        description="The minimum number of members in the vmgroup, the number of instances in the vm group will be equal to or more than this number",
    )
    name: Optional[str] = Field(None, description="The name of the autoscale vmgroup")
    scaledownpolicyids: Optional[List[str]] = Field(
        None, alias="scaleDownPolicyIds", description="List of scaledown autoscale policies"
    )
    scaleuppolicyids: Optional[List[str]] = Field(
        None, alias="scaleUpPolicyIds", description="List of scaleup autoscale policies"
    )

    @field_serializer("scaledownpolicyids", "scaleuppolicyids")
    def serialize_policyids(self, value: Optional[List[str]]) -> Optional[str]:
        if value is None:
            return None
        return ",".join(value)


class DeleteAutoScaleVmGroupRequest(APIRequest):
    id: str = Field(..., description="The ID of the autoscale group")
    cleanup: Optional[bool] = Field(None, description="True if all VMs have to be cleaned up, false otherwise")


class EnableAutoScaleVmGroupRequest(APIRequest):
    id: str = Field(..., description="The ID of the autoscale group")


class DisableAutoScaleVmGroupRequest(APIRequest):
    id: str = Field(..., description="The ID of the autoscale group")


class ListAutoScaleVmGroupsRequest(APIRequest, PaginationMixin):
    account: Optional[str] = Field(None, description="List resources by account. Must be used with the domainId parameter.")
    domainid: Optional[str] = Field(None, alias="domainId", description="List only resources belonging to the domain specified")
    fordisplay: Optional[bool] = Field(
        None, alias="forDisplay", description="List resources by display flag; only ROOT admin is eligible to pass this parameter"
    )
    id: Optional[str] = Field(None, description="The ID of the autoscale vm group")
    isrecursive: Optional[bool] = Field(
        None,
        alias="isRecursive",
        description="Defaults to false, but if true, lists all resources from the parent specified by the domainId till leaves.",
    )
    keyword: Optional[str] = Field(None, description="List by keyword")
    lbruleid: Optional[str] = Field(None, alias="lbRuleId", description="The ID of the loadbalancer")
    listall: Optional[bool] = Field(
        None,
        alias="listAll",
        description="If set to false, list only resources belonging to the command's caller; if set to true - list resources that the caller is authorized to see.",
    )
    name: Optional[str] = Field(None, description="The name of the autoscale vmgroup")
    policyid: Optional[str] = Field(None, alias="policyId", description="The ID of the policy")
    projectid: Optional[str] = Field(None, alias="projectId", description="List objects by project; if projectid=-1 lists All VMs")
    vmprofileid: Optional[str] = Field(None, alias="vmProfileId", description="The ID of the profile")
    zoneid: Optional[str] = Field(None, alias="zoneId", description="The availability zone ID")


# ---------------------------------------------------------------------------
# Conditions
# ---------------------------------------------------------------------------


class CreateConditionRequest(APIRequest):
    counterid: str = Field(..., alias="counterId", description="ID of the Counter.")
    relationaloperator: RelationalOperator = Field(
        ..., alias="relationalOperator", description="Relational Operator to be used with threshold. Valid values are EQ, GT, LT, GE, LE."
    )
    threshold: float = Field(..., description="Value for which the Counter will be evaluated with the Operator selected.")
    account: Optional[str] = Field(
        None, description="The account owning the condition. Must be used with the domainId parameter."
    )
    domainid: Optional[str] = Field(None, alias="domainId", description="The domain ID of the account.")
    projectid: Optional[str] = Field(None, alias="projectId", description="An optional project for condition")


class UpdateConditionRequest(APIRequest):
    id: str = Field(..., description="The ID of the condition.")
    relationaloperator: RelationalOperator = Field(
        ..., alias="relationalOperator", description="Relational Operator to be used with threshold. Valid values are EQ, GT, LT, GE, LE."
    )
    threshold: float = Field(..., description="Value for which the Counter will be evaluated with the Operator selected.")


class DeleteConditionRequest(APIRequest):
    id: str = Field(..., description="The ID of the condition.")


class ListConditionsRequest(APIRequest, PaginationMixin):
    account: Optional[str] = Field(None, description="List resources by account. Must be used with the domainId parameter.")
    counterid: Optional[str] = Field(None, alias="counterId", description="ID of the Counter.")
    domainid: Optional[str] = Field(None, alias="domainId", description="List only resources belonging to the domain specified")
    id: Optional[str] = Field(None, description="The ID of the condition")
    isrecursive: Optional[bool] = Field(
        None,
        alias="isRecursive",
        description="Defaults to false, but if true, lists all resources from the parent specified by the domainId till leaves.",
    )
    keyword: Optional[str] = Field(None, description="List by keyword")
    listall: Optional[bool] = Field(
        None,
        alias="listAll",
        description="If set to false, list only resources belonging to the command's caller; if set to true - list resources that the caller is authorized to see.",
    )
    policyid: Optional[str] = Field(None, alias="policyId", description="The ID of the policy")
    projectid: Optional[str] = Field(None, alias="projectId", description="List objects by project; if projectid=-1 lists All VMs")


# ---------------------------------------------------------------------------
# Counters
# ---------------------------------------------------------------------------


class CreateCounterRequest(APIRequest):
    name: str = Field(..., description="Name of the counter.")
    provider: str = Field(..., description="Network provider of the counter.")
    source: str = Field(..., description="Source of the counter.")
    value: str = Field(..., description="Value of the counter e.g. oid in case of snmp.")


class DeleteCounterRequest(APIRequest):
    id: str = Field(..., description="The ID of the counter")


class ListCountersRequest(APIRequest, PaginationMixin):
    id: Optional[str] = Field(None, description="ID of the Counter.")
    keyword: Optional[str] = Field(None, description="List by keyword")
    name: Optional[str] = Field(None, description="Name of the counter.")
    provider: Optional[str] = Field(None, description="Network provider of the counter.")
    source: Optional[str] = Field(None, description="Source of the counter.")
