from typing import Optional
from pydantic import Field
from acs_sdk.schemas.request.base import APIRequest, PaginationMixin


class CreateNetworkACLRequest(APIRequest):
    """Request to create a network ACL rule."""
    
    # Required fields
    protocol: str = Field(
        ..., description="The protocol for the ACL rule. Valid values are TCP/UDP/ICMP/ALL or valid protocol number"
    )
    
    # Optional fields
    aclid: Optional[str] = Field(
        None, alias="aclId", description="The network of the VM the ACL will be created for"
    )
    
    action: Optional[str] = Field(
        None, description="ACL entry action, allow or deny"
    )
    
    cidrlist: Optional[str] = Field(
        None, alias="cidrList", description="The CIDR list to allow traffic from/to. Multiple entries must be separated by a single comma character (,)."
    )
    
    endport: Optional[int] = Field(
        None, alias="endPort", description="The ending port of ACL"
    )
    
    fordisplay: Optional[bool] = Field(
        None, alias="forDisplay", description="An optional field, whether to display the rule to the end user or not"
    )
    
    icmpcode: Optional[int] = Field(
        None, alias="icmpCode", description="Error code for this ICMP message"
    )
    
    icmptype: Optional[int] = Field(
        None, alias="icmpType", description="Type of the ICMP message being sent"
    )
    
    networkid: Optional[str] = Field(
        None, alias="networkId", description="The network of the VM the ACL will be created for"
    )
    
    number: Optional[int] = Field(
        None, description="The number of the ACL item, its ordering"
    )
    
    reason: Optional[str] = Field(
        None, description="A description indicating why the ACL rule is required"
    )
    
    startport: Optional[int] = Field(
        None, alias="startPort", description="The starting port of ACL"
    )
    
    traffictype: Optional[str] = Field(
        None, alias="trafficType", description="The traffic type for the ACL, can be ingress or egress, defaulted to ingress if not specified"
    )


class CreateNetworkACLListRequest(APIRequest):
    """Request to create a network ACL list."""
    
    # Required fields
    name: str = Field(
        ..., description="Name of the network ACL list"
    )
    
    # Optional fields
    description: Optional[str] = Field(
        None, description="Description of the network ACL list"
    )
    
    fordisplay: Optional[bool] = Field(
        None, alias="forDisplay", description="An optional field, whether to display the list to the end user or not"
    )
    
    vpcid: Optional[str] = Field(
        None, alias="vpcId", description="ID of the VPC associated with this network ACL list"
    )


class DeleteNetworkACLRequest(APIRequest):
    """Request to delete a network ACL rule."""
    
    # Required fields
    id: str = Field(
        ..., description="The ID of the network ACL"
    )


class DeleteNetworkACLListRequest(APIRequest):
    """Request to delete a network ACL list."""
    
    # Required fields
    id: str = Field(
        ..., description="The ID of the network ACL"
    )


class ListNetworkACLListsRequest(APIRequest, PaginationMixin):
    """Request to list network ACL lists."""
    
    # Optional fields
    account: Optional[str] = Field(
        None, description="List resources by account. Must be used with the domainId parameter"
    )
    
    domainid: Optional[str] = Field(
        None, alias="domainId", description="List only resources belonging to the domain specified"
    )
    
    fordisplay: Optional[bool] = Field(
        None, alias="forDisplay", description="List resources by display flag; only ROOT admin is eligible to pass this parameter"
    )
    
    id: Optional[str] = Field(
        None, description="Lists network ACL with the specified ID"
    )
    
    isrecursive: Optional[bool] = Field(
        None, alias="isRecursive", description="Defaults to false, but if true, lists all resources from the parent specified by the domainId till leaves"
    )
    
    keyword: Optional[str] = Field(
        None, description="List by keyword"
    )
    
    listall: Optional[bool] = Field(
        None, alias="listAll", description="If set to false, list only resources belonging to the command's caller; if set to true - list resources that the caller is authorized to see"
    )
    
    name: Optional[str] = Field(
        None, description="List network ACLs by specified name"
    )
    
    networkid: Optional[str] = Field(
        None, alias="networkId", description="List network ACLs by network ID"
    )
    
    projectid: Optional[str] = Field(
        None, alias="projectId", description="List objects by project; if projectid=-1 lists All VMs"
    )
    
    vpcid: Optional[str] = Field(
        None, alias="vpcId", description="List network ACLs by VPC ID"
    )


class ListNetworkACLsRequest(APIRequest, PaginationMixin):
    """Request to list network ACL items."""
    
    # Optional fields
    account: Optional[str] = Field(
        None, description="List resources by account. Must be used with the domainId parameter"
    )
    
    aclid: Optional[str] = Field(
        None, alias="aclId", description="List network ACL items by ACL ID"
    )
    
    action: Optional[str] = Field(
        None, description="List network ACL items by action"
    )
    
    domainid: Optional[str] = Field(
        None, alias="domainId", description="List only resources belonging to the domain specified"
    )
    
    fordisplay: Optional[bool] = Field(
        None, alias="forDisplay", description="List resources by display flag; only ROOT admin is eligible to pass this parameter"
    )
    
    id: Optional[str] = Field(
        None, description="Lists network ACL Item with the specified ID"
    )
    
    isrecursive: Optional[bool] = Field(
        None, alias="isRecursive", description="Defaults to false, but if true, lists all resources from the parent specified by the domainId till leaves"
    )
    
    keyword: Optional[str] = Field(
        None, description="List by keyword"
    )
    
    listall: Optional[bool] = Field(
        None, alias="listAll", description="If set to false, list only resources belonging to the command's caller; if set to true - list resources that the caller is authorized to see"
    )
    
    networkid: Optional[str] = Field(
        None, alias="networkId", description="List network ACL items by network ID"
    )
    
    projectid: Optional[str] = Field(
        None, alias="projectId", description="List objects by project; if projectid=-1 lists All VMs"
    )
    
    protocol: Optional[str] = Field(
        None, description="List network ACL items by protocol"
    )
    
    tags: Optional[str] = Field(
        None, description="List resources by tags (key/value pairs)"
    )
    
    traffictype: Optional[str] = Field(
        None, alias="trafficType", description="List network ACL items by traffic type - ingress or egress"
    )


class MoveNetworkAclItemRequest(APIRequest):
    """Request to move a network ACL item to a new position."""
    
    # Required fields
    id: str = Field(
        ..., description="The ID of the network ACL rule that is being moved to a new position"
    )
    
    # Optional fields
    aclconsistencyhash: Optional[str] = Field(
        None, alias="aclConsistencyHash", description="MD5 hash used to check the consistency of the ACL rule list before applying the ACL rule move"
    )
    
    customerid: Optional[str] = Field(
        None, alias="customerId", description="An optional field, in case you want to set a custom id to the resource. Allowed to Root Admins only"
    )
    
    nextaclruleid: Optional[str] = Field(
        None, alias="nextAclRuleId", description="The ID of the rule that is right after the new position where the rule being moved is going to be placed. This value can be 'NULL' if the rule is being moved to the last position"
    )
    
    previousaclruleid: Optional[str] = Field(
        None, alias="previousAclRuleId", description="The ID of the first rule that is right before the new position where the rule being moved is going to be placed. This value can be 'NULL' if the rule is being moved to the first position"
    )


class ReplaceNetworkACLListRequest(APIRequest):
    """Request to replace ACL associated with a network or private gateway."""
    
    # Required fields
    aclid: str = Field(
        ..., alias="aclId", description="The ID of the network ACL"
    )
    
    # Optional fields
    gatewayid: Optional[str] = Field(
        None, alias="gatewayId", description="The ID of the private gateway"
    )
    
    networkid: Optional[str] = Field(
        None, alias="networkId", description="The ID of the network"
    )


class UpdateNetworkACLItemRequest(APIRequest):
    """Request to update a network ACL item."""
    
    # Required fields
    id: str = Field(
        ..., description="The ID of the network ACL item"
    )
    
    # Optional fields
    action: Optional[str] = Field(
        None, description="ACL entry action, allow or deny"
    )
    
    cidrlist: Optional[str] = Field(
        None, alias="cidrList", description="The CIDR list to allow traffic from/to. Multiple entries must be separated by a single comma character (,)."
    )
    
    customerid: Optional[str] = Field(
        None, alias="customerId", description="An optional field, in case you want to set a custom id to the resource. Allowed to Root Admins only"
    )
    
    endport: Optional[int] = Field(
        None, alias="endPort", description="The ending port of ACL"
    )
    
    fordisplay: Optional[bool] = Field(
        None, alias="forDisplay", description="An optional field, whether to display the rule to the end user or not"
    )
    
    icmpcode: Optional[int] = Field(
        None, alias="icmpCode", description="Error code for this ICMP message"
    )
    
    icmptype: Optional[int] = Field(
        None, alias="icmpType", description="Type of the ICMP message being sent"
    )
    
    number: Optional[int] = Field(
        None, description="The network of the VM the ACL will be created for"
    )
    
    partialupgrade: Optional[bool] = Field(
        None, alias="partialUpgrade", description="Indicates if the ACL rule is to be updated partially (merging the parameters sent with current configuration) or completely. Default is true"
    )
    
    protocol: Optional[str] = Field(
        None, description="The protocol for the ACL rule. Valid values are TCP/UDP/ICMP/ALL or valid protocol number"
    )
    
    reason: Optional[str] = Field(
        None, description="A description indicating why the ACL rule is required"
    )
    
    startport: Optional[int] = Field(
        None, alias="startPort", description="The starting port of ACL"
    )
    
    traffictype: Optional[str] = Field(
        None, alias="trafficType", description="The traffic type for the ACL, can be Ingress or Egress, defaulted to Ingress if not specified"
    )


class UpdateNetworkACLListRequest(APIRequest):
    """Request to update a network ACL list."""
    
    # Required fields
    id: str = Field(
        ..., description="The ID of the network ACL"
    )
    
    # Optional fields
    customerid: Optional[str] = Field(
        None, alias="customerId", description="An optional field, in case you want to set a custom id to the resource. Allowed to Root Admins only"
    )
    
    description: Optional[str] = Field(
        None, description="Description of the network ACL list"
    )
    
    fordisplay: Optional[bool] = Field(
        None, alias="forDisplay", description="An optional field, whether to display the list to the end user or not"
    )
    
    name: Optional[str] = Field(
        None, description="Name of the network ACL list"
    )


