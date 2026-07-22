# schemas/request/load_balancer.py
from typing import Any, Dict, List, Literal, Optional

from pydantic import BaseModel, Field, field_serializer

from acs_sdk.schemas.request.base import APIRequest, PaginationMixin

LBAlgorithm = Literal["source", "roundrobin", "leastconn"]
LBProtocol = Literal["tcp", "udp", "tcp-proxy", "ssl"]
LBStickinessMethod = Literal["LbCookie", "AppCookie", "SourceBased"]
LBScheme = Literal["Internal"]
GslbServiceType = Literal["tcp", "udp", "http"]
GslbLbMethod = Literal["roundrobin", "leastconn", "proximity"]
GslbStickySessionMethod = Literal["sourceip"]


def _flatten_indexed(data: Dict[str, Any], fields: List[str]) -> Dict[str, Any]:
    for field in fields:
        value = data.pop(field, None)
        if value:
            for idx, item in enumerate(value):
                for key, val in item.items():
                    data[f"{field}[{idx}].{key}"] = val
    return data


def _flatten_tags(data: Dict[str, Any], field: str = "tags") -> Dict[str, Any]:
    tags = data.pop(field, None)
    if tags:
        for idx, (key, value) in enumerate(tags.items()):
            data[f"{field}[{idx}].key"] = key
            data[f"{field}[{idx}].value"] = value
    return data


# ---------------------------------------------------------------------------
# Helper models
# ---------------------------------------------------------------------------


class VmIdIpEntry(BaseModel):
    """One entry in vmidipmap[]"""

    vmid: str = Field(..., description="ID of the virtual machine")
    vmip: str = Field(..., description="IP address to use for the virtual machine on the load balancer rule")


class StickinessParamEntry(BaseModel):
    """One entry in param[]"""

    name: str = Field(..., description="Name of the stickiness policy parameter")
    value: str = Field(..., description="Value of the stickiness policy parameter")


class GslbLbRuleWeightEntry(BaseModel):
    """One entry in gslblbruleweightsmap[]"""

    loadbalancerid: str = Field(..., description="ID of the load balancer rule")
    weight: int = Field(..., ge=1, le=100, description="Weight (1-100) of the load balancer rule in the GSLB rule")


# ---------------------------------------------------------------------------
# Load balancer rules
# ---------------------------------------------------------------------------


class CreateLoadBalancerRuleRequest(APIRequest):
    algorithm: LBAlgorithm = Field(..., description="Load balancer algorithm (source, roundrobin, leastconn)")
    name: str = Field(..., description="Name of the load balancer rule")
    privateport: int = Field(
        ...,
        alias="privatePort",
        description="The private port of the private IP address/virtual machine where the network traffic will be load balanced to",
    )
    publicport: int = Field(
        ..., alias="publicPort", description="The public port from where the network traffic will be load balanced from"
    )
    account: Optional[str] = Field(
        None, description="The account associated with the load balancer. Must be used with the domainId parameter."
    )
    cidrlist: Optional[List[str]] = Field(
        None,
        alias="cidrList",
        description="The source CIDR list to allow traffic from; all other CIDRs will be blocked. By default, all CIDRs are allowed.",
    )
    description: Optional[str] = Field(None, description="The description of the load balancer rule")
    domainid: Optional[str] = Field(None, alias="domainId", description="The domain ID associated with the load balancer")
    fordisplay: Optional[bool] = Field(
        None, alias="forDisplay", description="Whether to display the rule to the end user or not"
    )
    networkid: Optional[str] = Field(
        None,
        alias="networkId",
        description="The guest network this rule will be created for. Required when the public IP address is not associated with any guest network yet (VPC case)",
    )
    openfirewall: Optional[bool] = Field(
        None,
        alias="openFirewall",
        description="If true, firewall rule for source/end public port is automatically created; if false, it has to be created explicitly",
    )
    protocol: Optional[LBProtocol] = Field(None, description="The protocol for the LB such as tcp, udp, tcp-proxy or ssl")
    publicipid: Optional[str] = Field(
        None, alias="publicIpId", description="Public IP address ID from where the network traffic will be load balanced from"
    )
    zoneid: Optional[str] = Field(
        None,
        alias="zoneId",
        description="Zone where the load balancer is going to be created. Required when the LB service provider is ElasticLoadBalancerVm",
    )

    @field_serializer("cidrlist")
    def serialize_csv(self, value: Optional[List[str]]) -> Optional[str]:
        if value is None:
            return None
        return ",".join(value)


class ListLoadBalancerRulesRequest(APIRequest, PaginationMixin):
    account: Optional[str] = Field(
        None, description="List resources by account. Must be used with the domainId parameter."
    )
    domainid: Optional[str] = Field(
        None, alias="domainId", description="List only resources belonging to the domain specified"
    )
    fordisplay: Optional[bool] = Field(
        None, alias="forDisplay", description="List resources by display flag; only ROOT admin is eligible to pass this parameter"
    )
    id: Optional[str] = Field(None, description="The ID of the load balancer rule")
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
    name: Optional[str] = Field(None, description="The name of the load balancer rule")
    networkid: Optional[str] = Field(None, alias="networkId", description="List by network ID the rule belongs to")
    projectid: Optional[str] = Field(
        None, alias="projectId", description="List objects by project; if projectid=-1 lists All VMs"
    )
    publicipid: Optional[str] = Field(
        None, alias="publicIpId", description="The public IP address ID of the load balancer rule"
    )
    tags: Optional[Dict[str, str]] = Field(None, description="List resources by tags (key/value pairs)")
    virtualmachineid: Optional[str] = Field(
        None, alias="virtualMachineId", description="The ID of the virtual machine of the load balancer rule"
    )
    zoneid: Optional[str] = Field(None, alias="zoneId", description="The availability zone ID")

    def model_dump(self, *args, **kwargs) -> Dict[str, Any]:
        data = super().model_dump(*args, **kwargs)
        return _flatten_tags(data)


class UpdateLoadBalancerRuleRequest(APIRequest):
    id: str = Field(..., description="The ID of the load balancer rule to update")
    algorithm: Optional[LBAlgorithm] = Field(
        None, description="Load balancer algorithm (source, roundrobin, leastconn)"
    )
    cidrlist: Optional[List[str]] = Field(None, alias="cidrList", description="The CIDR list to forward traffic from")
    customid: Optional[str] = Field(
        None, alias="customId", description="An optional custom ID for the resource. Allowed to Root Admins only."
    )
    description: Optional[str] = Field(None, description="The description of the load balancer rule")
    fordisplay: Optional[bool] = Field(
        None, alias="forDisplay", description="Whether to display the rule to the end user or not"
    )
    name: Optional[str] = Field(None, description="The name of the load balancer rule")
    protocol: Optional[LBProtocol] = Field(None, description="The protocol for the LB")

    @field_serializer("cidrlist")
    def serialize_csv(self, value: Optional[List[str]]) -> Optional[str]:
        if value is None:
            return None
        return ",".join(value)


class DeleteLoadBalancerRuleRequest(APIRequest):
    id: str = Field(..., description="The ID of the load balancer rule")


class AssignToLoadBalancerRuleRequest(APIRequest):
    id: str = Field(..., description="The ID of the load balancer rule")
    virtualmachineids: Optional[List[str]] = Field(
        None,
        alias="virtualMachineIds",
        description="The list of IDs of the virtual machines that are being assigned to the load balancer rule",
    )
    vmidipmap: Optional[List[VmIdIpEntry]] = Field(
        None, alias="vmIdIpMap", description="VM ID and IP map for assigning specific IPs to the load balancer rule"
    )

    @field_serializer("virtualmachineids")
    def serialize_csv(self, value: Optional[List[str]]) -> Optional[str]:
        if value is None:
            return None
        return ",".join(value)

    def model_dump(self, *args, **kwargs) -> Dict[str, Any]:
        data = super().model_dump(*args, **kwargs)
        return _flatten_indexed(data, ["vmidipmap"])


class RemoveFromLoadBalancerRuleRequest(APIRequest):
    id: str = Field(..., description="The ID of the load balancer rule")
    virtualmachineids: Optional[List[str]] = Field(
        None,
        alias="virtualMachineIds",
        description="The list of IDs of the virtual machines that are being removed from the load balancer rule",
    )
    vmidipmap: Optional[List[VmIdIpEntry]] = Field(
        None, alias="vmIdIpMap", description="VM ID and IP map identifying specific IPs to remove from the load balancer rule"
    )

    @field_serializer("virtualmachineids")
    def serialize_csv(self, value: Optional[List[str]]) -> Optional[str]:
        if value is None:
            return None
        return ",".join(value)

    def model_dump(self, *args, **kwargs) -> Dict[str, Any]:
        data = super().model_dump(*args, **kwargs)
        return _flatten_indexed(data, ["vmidipmap"])


class ListLoadBalancerRuleInstancesRequest(APIRequest, PaginationMixin):
    id: str = Field(..., description="The ID of the load balancer rule")
    applied: Optional[bool] = Field(
        None, description="True if listing all virtual machines currently applied to the load balancer rule; default is true"
    )
    keyword: Optional[str] = Field(None, description="List by keyword")
    lbvmips: Optional[bool] = Field(
        None, alias="lbvmIps", description="True if load balancer rule VM IP information is to be included; default is false"
    )


# ---------------------------------------------------------------------------
# LB health check policy
# ---------------------------------------------------------------------------


class CreateLBHealthCheckPolicyRequest(APIRequest):
    lbruleid: str = Field(..., alias="lbRuleId", description="The ID of the load balancer rule")
    description: Optional[str] = Field(None, description="The description of the load balancer health check policy")
    fordisplay: Optional[bool] = Field(
        None, alias="forDisplay", description="Whether to display the rule to the end user or not"
    )
    healthythreshold: Optional[int] = Field(
        None,
        alias="healthyThreshold",
        description="Number of consecutive health check successes before declaring an instance healthy",
    )
    intervaltime: Optional[int] = Field(
        None, alias="intervalTime", description="Amount of time between health checks (1 sec - 20940 sec)"
    )
    pingpath: Optional[str] = Field(None, alias="pingPath", description="HTTP ping path")
    responsetimeout: Optional[int] = Field(
        None, alias="responseTimeout", description="Time to wait when receiving a response from the health check (2sec - 60 sec)"
    )
    unhealthythreshold: Optional[int] = Field(
        None,
        alias="unhealthyThreshold",
        description="Number of consecutive health check failures before declaring an instance unhealthy",
    )


class DeleteLBHealthCheckPolicyRequest(APIRequest):
    id: str = Field(..., description="The ID of the load balancer health check policy")


class UpdateLBHealthCheckPolicyRequest(APIRequest):
    id: str = Field(..., description="The ID of the load balancer health check policy")
    customid: Optional[str] = Field(
        None, alias="customId", description="An optional custom ID for the resource. Allowed to Root Admins only."
    )
    fordisplay: Optional[bool] = Field(
        None, alias="forDisplay", description="Whether to display the policy to the end user or not"
    )


class ListLBHealthCheckPoliciesRequest(APIRequest, PaginationMixin):
    fordisplay: Optional[bool] = Field(
        None, alias="forDisplay", description="List resources by display flag; only ROOT admin is eligible to pass this parameter"
    )
    id: Optional[str] = Field(None, description="The ID of the health check policy")
    keyword: Optional[str] = Field(None, description="List by keyword")
    lbruleid: Optional[str] = Field(None, alias="lbRuleId", description="The ID of the load balancer rule")


# ---------------------------------------------------------------------------
# LB stickiness policy
# ---------------------------------------------------------------------------


class CreateLBStickinessPolicyRequest(APIRequest):
    lbruleid: str = Field(..., alias="lbRuleId", description="The ID of the load balancer rule")
    methodname: LBStickinessMethod = Field(
        ...,
        alias="methodName",
        description="Name of the load balancer stickiness policy method: LbCookie, AppCookie, SourceBased",
    )
    name: str = Field(..., description="Name of the load balancer stickiness policy")
    description: Optional[str] = Field(None, description="The description of the load balancer stickiness policy")
    fordisplay: Optional[bool] = Field(
        None, alias="forDisplay", description="Whether to display the rule to the end user or not"
    )
    param: Optional[List[StickinessParamEntry]] = Field(
        None, description="Param list. Example: param[0].name=cookiename&param[0].value=LBCookie"
    )

    def model_dump(self, *args, **kwargs) -> Dict[str, Any]:
        data = super().model_dump(*args, **kwargs)
        return _flatten_indexed(data, ["param"])


class DeleteLBStickinessPolicyRequest(APIRequest):
    id: str = Field(..., description="The ID of the LB stickiness policy")


class UpdateLBStickinessPolicyRequest(APIRequest):
    id: str = Field(..., description="The ID of the LB stickiness policy")
    customid: Optional[str] = Field(
        None, alias="customId", description="An optional custom ID for the resource. Allowed to Root Admins only."
    )
    fordisplay: Optional[bool] = Field(
        None, alias="forDisplay", description="Whether to display the policy to the end user or not"
    )


class ListLBStickinessPoliciesRequest(APIRequest, PaginationMixin):
    fordisplay: Optional[bool] = Field(
        None, alias="forDisplay", description="List resources by display flag; only ROOT admin is eligible to pass this parameter"
    )
    id: Optional[str] = Field(None, description="The ID of the load balancer stickiness policy")
    keyword: Optional[str] = Field(None, description="List by keyword")
    lbruleid: Optional[str] = Field(None, alias="lbRuleId", description="The ID of the load balancer rule")


# ---------------------------------------------------------------------------
# Internal load balancer
# ---------------------------------------------------------------------------


class CreateLoadBalancerRequest(APIRequest):
    algorithm: LBAlgorithm = Field(..., description="Load balancer algorithm (source, roundrobin, leastconn)")
    instanceport: int = Field(
        ..., alias="instancePort", description="The TCP port of the virtual machine where the network traffic will be load balanced to"
    )
    name: str = Field(..., description="Name of the load balancer")
    networkid: str = Field(..., alias="networkId", description="The guest network the load balancer will be created for")
    scheme: LBScheme = Field(..., description="The load balancer scheme. Supported value in this release is Internal")
    sourceipaddressnetworkid: str = Field(
        ..., alias="sourceIpAddressNetworkId", description="The network ID of the source IP address"
    )
    sourceport: int = Field(..., alias="sourcePort", description="The source port the network traffic will be load balanced from")
    description: Optional[str] = Field(None, description="The description of the load balancer")
    fordisplay: Optional[bool] = Field(
        None, alias="forDisplay", description="Whether to display the rule to the end user or not"
    )
    sourceipaddress: Optional[str] = Field(
        None, alias="sourceIpAddress", description="The source IP address the network traffic will be load balanced from"
    )


class ListLoadBalancersRequest(APIRequest, PaginationMixin):
    account: Optional[str] = Field(
        None, description="List resources by account. Must be used with the domainId parameter."
    )
    domainid: Optional[str] = Field(
        None, alias="domainId", description="List only resources belonging to the domain specified"
    )
    fordisplay: Optional[bool] = Field(
        None, alias="forDisplay", description="List resources by display flag; only ROOT admin is eligible to pass this parameter"
    )
    id: Optional[str] = Field(None, description="The ID of the load balancer")
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
    name: Optional[str] = Field(None, description="The name of the load balancer")
    networkid: Optional[str] = Field(None, alias="networkId", description="The network ID of the load balancer")
    projectid: Optional[str] = Field(
        None, alias="projectId", description="List objects by project; if projectid=-1 lists All VMs"
    )
    scheme: Optional[LBScheme] = Field(None, description="The scheme of the load balancer. Supported value is Internal")
    sourceipaddress: Optional[str] = Field(
        None, alias="sourceIpAddress", description="The source IP address of the load balancer"
    )
    sourceipaddressnetworkid: Optional[str] = Field(
        None, alias="sourceIpAddressNetworkId", description="The network ID of the source IP address"
    )
    tags: Optional[Dict[str, str]] = Field(None, description="List resources by tags (key/value pairs)")

    def model_dump(self, *args, **kwargs) -> Dict[str, Any]:
        data = super().model_dump(*args, **kwargs)
        return _flatten_tags(data)


class UpdateLoadBalancerRequest(APIRequest):
    id: str = Field(..., description="The ID of the load balancer")
    customid: Optional[str] = Field(
        None, alias="customId", description="An optional custom ID for the resource. Allowed to Root Admins only."
    )
    fordisplay: Optional[bool] = Field(
        None, alias="forDisplay", description="Whether to display the rule to the end user or not"
    )


class DeleteLoadBalancerRequest(APIRequest):
    id: str = Field(..., description="The ID of the load balancer")


# ---------------------------------------------------------------------------
# Global load balancer rule
# ---------------------------------------------------------------------------


class CreateGlobalLoadBalancerRuleRequest(APIRequest):
    gslbdomainname: str = Field(..., alias="gslbDomainName", description="Domain name for the GSLB service")
    gslbservicetype: GslbServiceType = Field(..., alias="gslbServiceType", description="GSLB service type (tcp, udp, http)")
    name: str = Field(..., description="Name of the load balancer rule")
    regionid: str = Field(..., alias="regionId", description="Region where the global load balancer is going to be created")
    account: Optional[str] = Field(
        None, description="The account associated with the global load balancer. Must be used with the domainId parameter."
    )
    description: Optional[str] = Field(None, description="The description of the load balancer rule")
    domainid: Optional[str] = Field(None, alias="domainId", description="The domain ID associated with the load balancer")
    gslblbmethod: Optional[GslbLbMethod] = Field(
        None,
        alias="gslbLbMethod",
        description="Load balancer algorithm used to distribute traffic across zones participating in GSLB. Defaults to roundrobin.",
    )
    gslbstickysessionmethodname: Optional[GslbStickySessionMethod] = Field(
        None, alias="gslbStickySessionMethodName", description="Session sticky method. Defaults to sourceip."
    )


class ListGlobalLoadBalancerRulesRequest(APIRequest, PaginationMixin):
    account: Optional[str] = Field(
        None, description="List resources by account. Must be used with the domainId parameter."
    )
    domainid: Optional[str] = Field(
        None, alias="domainId", description="List only resources belonging to the domain specified"
    )
    id: Optional[str] = Field(None, description="The ID of the global load balancer rule")
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
    projectid: Optional[str] = Field(
        None, alias="projectId", description="List objects by project; if projectid=-1 lists All VMs"
    )
    regionid: Optional[str] = Field(None, alias="regionId", description="Region ID")
    tags: Optional[Dict[str, str]] = Field(None, description="List resources by tags (key/value pairs)")

    def model_dump(self, *args, **kwargs) -> Dict[str, Any]:
        data = super().model_dump(*args, **kwargs)
        return _flatten_tags(data)


class UpdateGlobalLoadBalancerRuleRequest(APIRequest):
    id: str = Field(..., description="The ID of the global load balancer rule")
    description: Optional[str] = Field(None, description="The description of the load balancer rule")
    gslblbmethod: Optional[GslbLbMethod] = Field(
        None,
        alias="gslbLbMethod",
        description="Load balancer algorithm used to distribute traffic across zones participating in GSLB. Defaults to roundrobin.",
    )
    gslbstickysessionmethodname: Optional[GslbStickySessionMethod] = Field(
        None, alias="gslbStickySessionMethodName", description="Session sticky method. Defaults to sourceip."
    )


class DeleteGlobalLoadBalancerRuleRequest(APIRequest):
    id: str = Field(..., description="The ID of the global load balancer rule")


class AssignToGlobalLoadBalancerRuleRequest(APIRequest):
    id: str = Field(..., description="The ID of the global load balancer rule")
    loadbalancerrulelist: List[str] = Field(
        ..., alias="loadBalancerRuleList", description="The list of load balancer rules that will be assigned to the global load balancer rule"
    )
    gslblbruleweightsmap: Optional[List[GslbLbRuleWeightEntry]] = Field(
        None,
        alias="gslbLbRuleWeightsMap",
        description="Map of LB rule IDs and corresponding weights (1-100) in the GSLB rule. Defaults to 1 if not specified.",
    )

    @field_serializer("loadbalancerrulelist")
    def serialize_csv(self, value: List[str]) -> str:
        return ",".join(value)

    def model_dump(self, *args, **kwargs) -> Dict[str, Any]:
        data = super().model_dump(*args, **kwargs)
        return _flatten_indexed(data, ["gslblbruleweightsmap"])


class RemoveFromGlobalLoadBalancerRuleRequest(APIRequest):
    id: str = Field(..., description="The ID of the load balancer rule")
    loadbalancerrulelist: List[str] = Field(
        ..., alias="loadBalancerRuleList", description="The list of load balancer rules that will be removed from the global load balancer rule"
    )

    @field_serializer("loadbalancerrulelist")
    def serialize_csv(self, value: List[str]) -> str:
        return ",".join(value)


# ---------------------------------------------------------------------------
# SSL certificate
# ---------------------------------------------------------------------------


class AssignCertToLoadBalancerRequest(APIRequest):
    certid: str = Field(..., alias="certId", description="The ID of the certificate")
    lbruleid: str = Field(..., alias="lbRuleId", description="The ID of the load balancer rule")
    forced: Optional[bool] = Field(
        None, description="Force assign the certificate. If there is a certificate assigned to the LB, it will be removed first."
    )


class RemoveCertFromLoadBalancerRequest(APIRequest):
    lbruleid: str = Field(..., alias="lbRuleId", description="The ID of the load balancer rule")


class GetLoadBalancerSslCertificateRequest(APIRequest):
    id: str = Field(..., description="The ID of the load balancer")


# ---------------------------------------------------------------------------
# NetScaler VPX
# ---------------------------------------------------------------------------


class DeployNetscalerVpxRequest(APIRequest):
    serviceofferingid: str = Field(
        ..., alias="serviceOfferingId", description="The ID of the service offering for the virtual machine"
    )
    templateid: str = Field(..., alias="templateId", description="The ID of the template for the virtual machine")
    zoneid: str = Field(..., alias="zoneId", description="Availability zone for the virtual machine")
    networkid: Optional[str] = Field(
        None, alias="networkId", description="The network this IP address should be associated to"
    )


class StopNetScalerVpxRequest(APIRequest):
    id: str = Field(..., description="The ID of the NetScaler VM")
    forced: Optional[bool] = Field(
        None,
        description="Force stop the VM (VM is marked as Stopped even when the command fails to reach the backend)",
    )


# ---------------------------------------------------------------------------
# Service packages
# ---------------------------------------------------------------------------


class ListRegisteredServicePackagesRequest(APIRequest, PaginationMixin):
    keyword: Optional[str] = Field(None, description="List by keyword")


class DeleteServicePackageOfferingRequest(APIRequest):
    id: str = Field(..., description="The service offering ID")
