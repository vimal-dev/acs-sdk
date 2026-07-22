# schemas/request/kubernetes.py
from typing import Any, Dict, List, Literal, Optional

from pydantic import Field, field_serializer

from acs_sdk.schemas.request.base import APIRequest, PaginationMixin

ClusterType = Literal["CloudManaged", "ExternalManaged"]
KubernetesVersionArch = Literal["x86_64", "aarch64"]
UploadFormat = Literal["QCOW2", "OVA", "VHD"]


def _flatten_kv_maps(data: Dict[str, Any], fields: List[str]) -> Dict[str, Any]:
    for field in fields:
        value = data.pop(field, None)
        if value:
            for idx, (key, val) in enumerate(value.items()):
                data[f"{field}[{idx}].key"] = key
                data[f"{field}[{idx}].value"] = val
    return data


# ---------------------------------------------------------------------------
# Cluster lifecycle
# ---------------------------------------------------------------------------


class CreateKubernetesClusterRequest(APIRequest):
    name: str = Field(..., description="Name for the Kubernetes cluster")
    zoneid: str = Field(
        ...,
        alias="zoneId",
        description="Availability zone in which the Kubernetes cluster is to be launched",
    )
    account: Optional[str] = Field(
        None, description="An optional account for the virtual machine. Must be used with domainId."
    )
    asnumber: Optional[str] = Field(
        None, alias="asNumber", description="The AS Number of the network"
    )
    clustertype: Optional[ClusterType] = Field(
        None,
        alias="clusterType",
        description="Type of the cluster: CloudManaged or ExternalManaged. Defaults to CloudManaged.",
    )
    cniconfigdetails: Optional[Dict[str, str]] = Field(
        None,
        alias="cniConfigDetails",
        description="Parameter values for the variables in the CNI userdata",
    )
    cniconfigurationid: Optional[str] = Field(
        None,
        alias="cniConfigurationId",
        description="The ID of the Userdata used for CNI configuration",
    )
    controlnodes: Optional[int] = Field(
        None,
        alias="controlNodes",
        description="Number of Kubernetes cluster control nodes. Defaults to 1.",
    )
    description: Optional[str] = Field(None, description="Description for the Kubernetes cluster")
    dockerregistrypassword: Optional[str] = Field(
        None,
        alias="dockerRegistryPassword",
        description="Password for the docker image private registry",
    )
    dockerregistryurl: Optional[str] = Field(
        None, alias="dockerRegistryUrl", description="URL for the docker image private registry"
    )
    dockerregistryusername: Optional[str] = Field(
        None,
        alias="dockerRegistryUsername",
        description="User name for the docker image private registry",
    )
    domainid: Optional[str] = Field(
        None,
        alias="domainId",
        description="An optional domainId for the virtual machine. If the account parameter is used, domainId must also be used.",
    )
    enablecsi: Optional[bool] = Field(
        None, alias="enableCsi", description="If true, sets up the CloudStack CSI driver"
    )
    etcdnodes: Optional[int] = Field(
        None,
        alias="etcdNodes",
        description="Number of Kubernetes cluster etcd nodes. Defaults to 0, meaning etcd runs on the control nodes.",
    )
    externalloadbalanceripaddress: Optional[str] = Field(
        None,
        alias="externalLoadBalancerIpAddress",
        description="External load balancer IP address while using a shared network with a Kubernetes HA cluster",
    )
    hypervisor: Optional[str] = Field(
        None,
        description="The hypervisor on which the CKS cluster is to be deployed. Required if the zone has clusters with different hypervisor types.",
    )
    keypair: Optional[str] = Field(
        None, description="Name of the SSH key pair used to log in to the virtual machines"
    )
    kubernetesversionid: Optional[str] = Field(
        None,
        alias="kubernetesVersionId",
        description="Kubernetes version with which the cluster is to be launched",
    )
    masternodes: Optional[int] = Field(
        None,
        alias="masterNodes",
        description="Number of Kubernetes cluster master nodes. Deprecated, use controlnodes instead.",
    )
    networkid: Optional[str] = Field(
        None,
        alias="networkId",
        description="Network in which the Kubernetes cluster is to be launched",
    )
    nodeofferings: Optional[Dict[str, str]] = Field(
        None,
        alias="nodeOfferings",
        description="Node type to service offering ID mapping. Overrides serviceofferingid if provided.",
    )
    noderootdisksize: Optional[int] = Field(
        None, alias="nodeRootDiskSize", description="Root disk size in GB for each node"
    )
    nodetemplates: Optional[Dict[str, str]] = Field(
        None,
        alias="nodeTemplates",
        description="Node type to template ID mapping. Overrides the default System VM template if provided.",
    )
    projectid: Optional[str] = Field(
        None, alias="projectId", description="Deploy the cluster for the project"
    )
    serviceofferingid: Optional[str] = Field(
        None,
        alias="serviceOfferingId",
        description="The ID of the service offering for the virtual machines in the cluster",
    )
    size: Optional[int] = Field(None, description="Number of Kubernetes cluster worker nodes")

    def model_dump(self, *args, **kwargs) -> Dict[str, Any]:
        data = super().model_dump(*args, **kwargs)
        return _flatten_kv_maps(data, ["cniconfigdetails", "nodeofferings", "nodetemplates"])


class DeleteKubernetesClusterRequest(APIRequest):
    id: str = Field(..., description="The ID of the Kubernetes cluster")
    cleanup: Optional[bool] = Field(
        None,
        description="Destroy attached instances of the ExternalManaged cluster. Default: false",
    )
    expunge: Optional[bool] = Field(
        None,
        description="Expunge attached instances of the ExternalManaged cluster. If true, the value of cleanup is ignored. Default: false",
    )


class StartKubernetesClusterRequest(APIRequest):
    id: str = Field(..., description="The ID of the Kubernetes cluster")


class StopKubernetesClusterRequest(APIRequest):
    id: str = Field(..., description="The ID of the Kubernetes cluster")


class ScaleKubernetesClusterRequest(APIRequest):
    id: str = Field(..., description="The ID of the Kubernetes cluster")
    autoscalingenabled: Optional[bool] = Field(
        None,
        alias="autoscalingEnabled",
        description="Whether autoscaling is enabled for the cluster",
    )
    maxsize: Optional[int] = Field(
        None, alias="maxSize", description="Maximum number of worker nodes in the cluster"
    )
    minsize: Optional[int] = Field(
        None, alias="minSize", description="Minimum number of worker nodes in the cluster"
    )
    nodeids: Optional[List[str]] = Field(
        None, alias="nodeIds", description="The IDs of the nodes to be removed"
    )
    nodeofferings: Optional[Dict[str, str]] = Field(
        None,
        alias="nodeOfferings",
        description="Node type to service offering ID mapping. Overrides serviceofferingid if provided.",
    )
    serviceofferingid: Optional[str] = Field(
        None,
        alias="serviceOfferingId",
        description="The ID of the service offering for the virtual machines in the cluster",
    )
    size: Optional[int] = Field(None, description="Number of Kubernetes cluster nodes")

    @field_serializer("nodeids")
    def serialize_csv(self, value: Optional[List[str]]) -> Optional[str]:
        if value is None:
            return None
        return ",".join(value)

    def model_dump(self, *args, **kwargs) -> Dict[str, Any]:
        data = super().model_dump(*args, **kwargs)
        return _flatten_kv_maps(data, ["nodeofferings"])


class UpgradeKubernetesClusterRequest(APIRequest):
    id: str = Field(..., description="The ID of the Kubernetes cluster")
    kubernetesversionid: str = Field(
        ..., alias="kubernetesVersionId", description="The ID of the Kubernetes version for upgrade"
    )


# ---------------------------------------------------------------------------
# Cluster list / config
# ---------------------------------------------------------------------------


class ListKubernetesClustersRequest(APIRequest, PaginationMixin):
    account: Optional[str] = Field(
        None, description="List resources by account. Must be used with the domainId parameter."
    )
    clustertype: Optional[ClusterType] = Field(
        None,
        alias="clusterType",
        description="Type of the cluster: CloudManaged or ExternalManaged",
    )
    domainid: Optional[str] = Field(
        None, alias="domainId", description="List only resources belonging to the domain specified"
    )
    id: Optional[str] = Field(None, description="The ID of the Kubernetes cluster")
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
    name: Optional[str] = Field(
        None, description="Name of the Kubernetes cluster (substring match)"
    )
    projectid: Optional[str] = Field(
        None,
        alias="projectId",
        description="List objects by project; if projectid=-1 lists All VMs",
    )
    state: Optional[str] = Field(None, description="State of the Kubernetes cluster")


class GetKubernetesClusterConfigRequest(APIRequest):
    id: Optional[str] = Field(None, description="The ID of the Kubernetes cluster")


# ---------------------------------------------------------------------------
# Node / VM management
# ---------------------------------------------------------------------------


class AddNodesToKubernetesClusterRequest(APIRequest):
    id: str = Field(..., description="The ID of the Kubernetes cluster")
    nodeids: List[str] = Field(
        ...,
        alias="nodeIds",
        description="IDs of the (external) nodes to be added as worker nodes to an existing managed Kubernetes cluster (CKS)",
    )
    manualupgrade: Optional[bool] = Field(
        None,
        alias="manualUpgrade",
        description="Indicates if the node is marked for manual upgrade and excluded from the Kubernetes cluster upgrade operation",
    )
    mountcksisoonvr: Optional[bool] = Field(
        None,
        alias="mountCksIsoOnVr",
        description="VMware only: uses the CKS cluster network VR to mount the CKS ISO",
    )

    @field_serializer("nodeids")
    def serialize_csv(self, value: List[str]) -> str:
        return ",".join(value)


class RemoveNodesFromKubernetesClusterRequest(APIRequest):
    id: str = Field(..., description="The ID of the Kubernetes cluster")
    nodeids: List[str] = Field(
        ...,
        alias="nodeIds",
        description="IDs of the (physical or virtual machine) nodes to be removed from the Kubernetes cluster (CKS)",
    )

    @field_serializer("nodeids")
    def serialize_csv(self, value: List[str]) -> str:
        return ",".join(value)


class AddVirtualMachinesToKubernetesClusterRequest(APIRequest):
    """Add VMs to an ExternalManaged Kubernetes cluster. Not applicable for CloudManaged clusters."""

    id: str = Field(..., description="The ID of the Kubernetes cluster")
    virtualmachineids: List[str] = Field(
        ..., alias="virtualMachineIds", description="The IDs of the VMs to add to the cluster"
    )
    iscontrolnode: Optional[bool] = Field(
        None, alias="isControlNode", description="Is control node or not? Defaults to false."
    )

    @field_serializer("virtualmachineids")
    def serialize_csv(self, value: List[str]) -> str:
        return ",".join(value)


class RemoveVirtualMachinesFromKubernetesClusterRequest(APIRequest, PaginationMixin):
    """Remove VMs from an ExternalManaged Kubernetes cluster. Not applicable for CloudManaged clusters."""

    id: str = Field(..., description="The ID of the Kubernetes cluster")
    virtualmachineids: List[str] = Field(
        ..., alias="virtualMachineIds", description="The IDs of the VMs to remove from the cluster"
    )
    keyword: Optional[str] = Field(None, description="List by keyword")

    @field_serializer("virtualmachineids")
    def serialize_csv(self, value: List[str]) -> str:
        return ",".join(value)


# ---------------------------------------------------------------------------
# Supported versions
# ---------------------------------------------------------------------------


class AddKubernetesSupportedVersionRequest(APIRequest):
    mincpunumber: int = Field(
        ...,
        alias="minCpuNumber",
        description="The minimum number of CPUs to be set with the Kubernetes version",
    )
    minmemory: int = Field(
        ...,
        alias="minMemory",
        description="The minimum RAM size in MB to be set with the Kubernetes version",
    )
    semanticversion: str = Field(
        ...,
        alias="semanticVersion",
        description="The semantic version of the Kubernetes version, specified in MAJOR.MINOR.PATCH format",
    )
    arch: Optional[KubernetesVersionArch] = Field(
        None, description="The CPU arch of the Kubernetes ISO. Valid options are: x86_64, aarch64"
    )
    checksum: Optional[str] = Field(None, description="The checksum value of the binaries ISO")
    directdownload: Optional[bool] = Field(
        None,
        alias="directDownload",
        description="If true, the Kubernetes supported version ISO bypasses Secondary Storage and downloads directly to Primary Storage on deployment. Default is false.",
    )
    name: Optional[str] = Field(None, description="The name of the Kubernetes supported version")
    url: Optional[str] = Field(
        None, description="The URL of the binaries ISO for the Kubernetes supported version"
    )
    zoneid: Optional[str] = Field(
        None,
        alias="zoneId",
        description="The ID of the zone in which the Kubernetes supported version will be available",
    )


class UpdateKubernetesSupportedVersionRequest(APIRequest):
    id: str = Field(..., description="The ID of the Kubernetes supported version")
    state: str = Field(
        ..., description="The enabled or disabled state of the Kubernetes supported version"
    )


class DeleteKubernetesSupportedVersionRequest(APIRequest):
    id: str = Field(..., description="The ID of the Kubernetes supported version")


class ListKubernetesSupportedVersionsRequest(APIRequest, PaginationMixin):
    arch: Optional[KubernetesVersionArch] = Field(
        None, description="The CPU arch of the binaries ISO. Valid options are: x86_64, aarch64"
    )
    id: Optional[str] = Field(None, description="The ID of the Kubernetes supported version")
    keyword: Optional[str] = Field(None, description="List by keyword")
    minimumkubernetesversionid: Optional[str] = Field(
        None,
        alias="minimumKubernetesVersionId",
        description="The ID of the minimum Kubernetes supported version",
    )
    minimumsemanticversion: Optional[str] = Field(
        None,
        alias="minimumSemanticVersion",
        description="The minimum semantic version for the Kubernetes supported version to be listed",
    )
    zoneid: Optional[str] = Field(
        None,
        alias="zoneId",
        description="The ID of the zone in which the Kubernetes supported version will be available",
    )


class GetUploadParamsForKubernetesSupportedVersionRequest(APIRequest):
    format: UploadFormat = Field(
        ..., description="The format for the volume/template/iso. Possible values: QCOW2, OVA, VHD."
    )
    mincpunumber: int = Field(
        ...,
        alias="minCpuNumber",
        description="The minimum number of CPUs to be set with the Kubernetes version",
    )
    minmemory: int = Field(
        ...,
        alias="minMemory",
        description="The minimum RAM size in MB to be set with the Kubernetes version",
    )
    name: str = Field(..., description="The name of the volume/template/iso")
    semanticversion: str = Field(
        ...,
        alias="semanticVersion",
        description="The semantic version of the Kubernetes version, specified in MAJOR.MINOR.PATCH format",
    )
    zoneid: str = Field(
        ...,
        alias="zoneId",
        description="The ID of the zone the volume/template/iso is to be hosted on",
    )
    account: Optional[str] = Field(
        None, description="An optional account name. Must be used with domainId."
    )
    checksum: Optional[str] = Field(None, description="The checksum value of the binaries ISO")
    domainid: Optional[str] = Field(
        None,
        alias="domainId",
        description="An optional domainId. If the account parameter is used, domainId must also be used.",
    )
    projectid: Optional[str] = Field(
        None, alias="projectId", description="Upload the volume/template/iso for the project"
    )
