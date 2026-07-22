import pytest
from pydantic import ValidationError

from acs_sdk.schemas.request.kubernetes import (
    AddKubernetesSupportedVersionRequest,
    AddNodesToKubernetesClusterRequest,
    AddVirtualMachinesToKubernetesClusterRequest,
    CreateKubernetesClusterRequest,
    DeleteKubernetesClusterRequest,
    GetUploadParamsForKubernetesSupportedVersionRequest,
    ListKubernetesClustersRequest,
    RemoveNodesFromKubernetesClusterRequest,
    RemoveVirtualMachinesFromKubernetesClusterRequest,
    ScaleKubernetesClusterRequest,
    UpdateKubernetesSupportedVersionRequest,
    UpgradeKubernetesClusterRequest,
)


# ---------------------------------------------------------------------------
# CreateKubernetesClusterRequest
# ---------------------------------------------------------------------------

def test_create_kubernetes_cluster_required_fields_serialize():
    req = CreateKubernetesClusterRequest(name="cluster-1", zoneId="zone-1")
    dumped = req.model_dump(exclude_none=True)
    assert dumped == {"name": "cluster-1", "zoneid": "zone-1"}


def test_create_kubernetes_cluster_aliases_serialize_to_snake_case():
    req = CreateKubernetesClusterRequest(
        name="cluster-1",
        zoneId="zone-1",
        clusterType="ExternalManaged",
        controlNodes=3,
        serviceOfferingId="so-1",
        kubernetesVersionId="v-1",
    )
    dumped = req.model_dump(exclude_none=True)
    assert dumped["clustertype"] == "ExternalManaged"
    assert dumped["controlnodes"] == 3
    assert dumped["serviceofferingid"] == "so-1"
    assert dumped["kubernetesversionid"] == "v-1"


def test_create_kubernetes_cluster_flattens_kv_maps():
    req = CreateKubernetesClusterRequest(
        name="cluster-1",
        zoneId="zone-1",
        nodeOfferings={"control": "so-1", "worker": "so-2"},
        nodeTemplates={"worker": "tmpl-1"},
        cniConfigDetails={"accesskey": "abc"},
    )
    dumped = req.model_dump(exclude_none=True)
    assert dumped["nodeofferings[0].key"] == "control"
    assert dumped["nodeofferings[0].value"] == "so-1"
    assert dumped["nodeofferings[1].key"] == "worker"
    assert dumped["nodeofferings[1].value"] == "so-2"
    assert dumped["nodetemplates[0].key"] == "worker"
    assert dumped["nodetemplates[0].value"] == "tmpl-1"
    assert dumped["cniconfigdetails[0].key"] == "accesskey"
    assert dumped["cniconfigdetails[0].value"] == "abc"
    assert "nodeofferings" not in dumped
    assert "nodetemplates" not in dumped
    assert "cniconfigdetails" not in dumped


def test_create_kubernetes_cluster_missing_required_fields_raises():
    with pytest.raises(ValidationError):
        CreateKubernetesClusterRequest()


# ---------------------------------------------------------------------------
# DeleteKubernetesClusterRequest
# ---------------------------------------------------------------------------

def test_delete_kubernetes_cluster_serializes():
    req = DeleteKubernetesClusterRequest(id="k8s-1", cleanup=True)
    dumped = req.model_dump(exclude_none=True)
    assert dumped == {"id": "k8s-1", "cleanup": True}


def test_delete_kubernetes_cluster_missing_id_raises():
    with pytest.raises(ValidationError):
        DeleteKubernetesClusterRequest()


# ---------------------------------------------------------------------------
# ScaleKubernetesClusterRequest
# ---------------------------------------------------------------------------

def test_scale_kubernetes_cluster_serializes_nodeids_csv():
    req = ScaleKubernetesClusterRequest(id="k8s-1", nodeIds=["node-1", "node-2"])
    dumped = req.model_dump(exclude_none=True)
    assert dumped["nodeids"] == "node-1,node-2"


def test_scale_kubernetes_cluster_flattens_nodeofferings():
    req = ScaleKubernetesClusterRequest(id="k8s-1", nodeOfferings={"worker": "so-2"})
    dumped = req.model_dump(exclude_none=True)
    assert dumped["nodeofferings[0].key"] == "worker"
    assert dumped["nodeofferings[0].value"] == "so-2"
    assert "nodeofferings" not in dumped


def test_scale_kubernetes_cluster_missing_id_raises():
    with pytest.raises(ValidationError):
        ScaleKubernetesClusterRequest()


# ---------------------------------------------------------------------------
# UpgradeKubernetesClusterRequest
# ---------------------------------------------------------------------------

def test_upgrade_kubernetes_cluster_required_fields_serialize():
    req = UpgradeKubernetesClusterRequest(id="k8s-1", kubernetesVersionId="v-2")
    dumped = req.model_dump(exclude_none=True)
    assert dumped == {"id": "k8s-1", "kubernetesversionid": "v-2"}


def test_upgrade_kubernetes_cluster_missing_required_fields_raises():
    with pytest.raises(ValidationError):
        UpgradeKubernetesClusterRequest(id="k8s-1")


# ---------------------------------------------------------------------------
# ListKubernetesClustersRequest
# ---------------------------------------------------------------------------

def test_list_kubernetes_clusters_defaults_from_pagination_mixin():
    req = ListKubernetesClustersRequest()
    dumped = req.model_dump(exclude_none=True)
    assert dumped["page"] == 1
    assert dumped["pagesize"] == 50


def test_list_kubernetes_clusters_aliases_serialize_to_snake_case():
    req = ListKubernetesClustersRequest(
        domainId="dom-1",
        projectId="proj-1",
        isRecursive=True,
        listAll=True,
        clusterType="CloudManaged",
    )
    dumped = req.model_dump(exclude_none=True)
    assert dumped["domainid"] == "dom-1"
    assert dumped["projectid"] == "proj-1"
    assert dumped["isrecursive"] is True
    assert dumped["listall"] is True
    assert dumped["clustertype"] == "CloudManaged"


# ---------------------------------------------------------------------------
# AddNodesToKubernetesClusterRequest / RemoveNodesFromKubernetesClusterRequest
# ---------------------------------------------------------------------------

def test_add_nodes_serializes_nodeids_csv():
    req = AddNodesToKubernetesClusterRequest(id="k8s-1", nodeIds=["node-1", "node-2"])
    dumped = req.model_dump(exclude_none=True)
    assert dumped == {"id": "k8s-1", "nodeids": "node-1,node-2"}


def test_add_nodes_missing_required_fields_raises():
    with pytest.raises(ValidationError):
        AddNodesToKubernetesClusterRequest(id="k8s-1")


def test_remove_nodes_serializes_nodeids_csv():
    req = RemoveNodesFromKubernetesClusterRequest(id="k8s-1", nodeIds=["node-1"])
    dumped = req.model_dump(exclude_none=True)
    assert dumped == {"id": "k8s-1", "nodeids": "node-1"}


# ---------------------------------------------------------------------------
# AddVirtualMachinesToKubernetesClusterRequest / RemoveVirtualMachinesFromKubernetesClusterRequest
# ---------------------------------------------------------------------------

def test_add_virtual_machines_serializes_ids_csv():
    req = AddVirtualMachinesToKubernetesClusterRequest(
        id="k8s-1", virtualMachineIds=["vm-1", "vm-2"], isControlNode=True
    )
    dumped = req.model_dump(exclude_none=True)
    assert dumped == {
        "id": "k8s-1",
        "virtualmachineids": "vm-1,vm-2",
        "iscontrolnode": True,
    }


def test_remove_virtual_machines_serializes_ids_csv_with_pagination_defaults():
    req = RemoveVirtualMachinesFromKubernetesClusterRequest(id="k8s-1", virtualMachineIds=["vm-1"])
    dumped = req.model_dump(exclude_none=True)
    assert dumped["id"] == "k8s-1"
    assert dumped["virtualmachineids"] == "vm-1"
    assert dumped["page"] == 1
    assert dumped["pagesize"] == 50


# ---------------------------------------------------------------------------
# AddKubernetesSupportedVersionRequest
# ---------------------------------------------------------------------------

def test_add_supported_version_required_fields_serialize():
    req = AddKubernetesSupportedVersionRequest(
        minCpuNumber=2, minMemory=2048, semanticVersion="1.30.0"
    )
    dumped = req.model_dump(exclude_none=True)
    assert dumped == {"mincpunumber": 2, "minmemory": 2048, "semanticversion": "1.30.0"}


def test_add_supported_version_missing_required_fields_raises():
    with pytest.raises(ValidationError):
        AddKubernetesSupportedVersionRequest(minCpuNumber=2)


def test_add_supported_version_invalid_arch_raises():
    with pytest.raises(ValidationError):
        AddKubernetesSupportedVersionRequest(
            minCpuNumber=2, minMemory=2048, semanticVersion="1.30.0", arch="mips"
        )


# ---------------------------------------------------------------------------
# UpdateKubernetesSupportedVersionRequest
# ---------------------------------------------------------------------------

def test_update_supported_version_required_fields_serialize():
    req = UpdateKubernetesSupportedVersionRequest(id="v-1", state="Disabled")
    dumped = req.model_dump(exclude_none=True)
    assert dumped == {"id": "v-1", "state": "Disabled"}


def test_update_supported_version_missing_required_fields_raises():
    with pytest.raises(ValidationError):
        UpdateKubernetesSupportedVersionRequest(id="v-1")


# ---------------------------------------------------------------------------
# GetUploadParamsForKubernetesSupportedVersionRequest
# ---------------------------------------------------------------------------

def test_get_upload_params_required_fields_serialize():
    req = GetUploadParamsForKubernetesSupportedVersionRequest(
        format="QCOW2",
        minCpuNumber=2,
        minMemory=2048,
        name="k8s-1.30.0",
        semanticVersion="1.30.0",
        zoneId="zone-1",
    )
    dumped = req.model_dump(exclude_none=True)
    assert dumped == {
        "format": "QCOW2",
        "mincpunumber": 2,
        "minmemory": 2048,
        "name": "k8s-1.30.0",
        "semanticversion": "1.30.0",
        "zoneid": "zone-1",
    }


def test_get_upload_params_invalid_format_raises():
    with pytest.raises(ValidationError):
        GetUploadParamsForKubernetesSupportedVersionRequest(
            format="ISO",
            minCpuNumber=2,
            minMemory=2048,
            name="k8s-1.30.0",
            semanticVersion="1.30.0",
            zoneId="zone-1",
        )
