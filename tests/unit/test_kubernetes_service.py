import asyncio
from unittest.mock import AsyncMock, Mock

from acs_sdk.schemas.request.kubernetes import (
    AddKubernetesSupportedVersionRequest,
    AddNodesToKubernetesClusterRequest,
    AddVirtualMachinesToKubernetesClusterRequest,
    CreateKubernetesClusterRequest,
    DeleteKubernetesClusterRequest,
    DeleteKubernetesSupportedVersionRequest,
    GetKubernetesClusterConfigRequest,
    GetUploadParamsForKubernetesSupportedVersionRequest,
    ListKubernetesClustersRequest,
    ListKubernetesSupportedVersionsRequest,
    RemoveNodesFromKubernetesClusterRequest,
    RemoveVirtualMachinesFromKubernetesClusterRequest,
    ScaleKubernetesClusterRequest,
    StartKubernetesClusterRequest,
    StopKubernetesClusterRequest,
    UpdateKubernetesSupportedVersionRequest,
    UpgradeKubernetesClusterRequest,
)
from acs_sdk.services.kubernetes import Kubernetes


# ---------------------------------------------------------------------------
# create_cluster
# ---------------------------------------------------------------------------


def test_kubernetes_create_cluster_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "createkubernetesclusterresponse": {"id": "k8s-1", "name": "cluster-1"},
    }

    kube = Kubernetes(client=mock_client)
    payload = CreateKubernetesClusterRequest(name="cluster-1", zoneId="zone-1")
    response = kube.create_cluster(payload)

    assert response.data == {"id": "k8s-1", "name": "cluster-1"}
    mock_client.call.assert_called_once_with(
        "createKubernetesCluster", payload.model_dump(exclude_none=True)
    )


def test_kubernetes_create_cluster_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={"createkubernetesclusterresponse": {"id": "k8s-1", "name": "cluster-1"}}
    )

    kube = Kubernetes(client=mock_client)
    payload = CreateKubernetesClusterRequest(name="cluster-1", zoneId="zone-1")
    response = asyncio.run(kube.create_cluster_async(payload))

    assert response.data == {"id": "k8s-1", "name": "cluster-1"}
    mock_client.call_async.assert_called_once_with(
        "createKubernetesCluster", payload.model_dump(exclude_none=True)
    )


# ---------------------------------------------------------------------------
# delete_cluster
# ---------------------------------------------------------------------------


def test_kubernetes_delete_cluster_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "deletekubernetesclusterresponse": {"success": "true"},
    }

    kube = Kubernetes(client=mock_client)
    payload = DeleteKubernetesClusterRequest(id="k8s-1")
    response = kube.delete_cluster(payload)

    assert response.data == {"success": "true"}
    mock_client.call.assert_called_once_with("deleteKubernetesCluster", {"id": "k8s-1"})


def test_kubernetes_delete_cluster_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={"deletekubernetesclusterresponse": {"success": "true"}}
    )

    kube = Kubernetes(client=mock_client)
    payload = DeleteKubernetesClusterRequest(id="k8s-1")
    response = asyncio.run(kube.delete_cluster_async(payload))

    assert response.data == {"success": "true"}
    mock_client.call_async.assert_called_once_with("deleteKubernetesCluster", {"id": "k8s-1"})


# ---------------------------------------------------------------------------
# start_cluster
# ---------------------------------------------------------------------------


def test_kubernetes_start_cluster_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "startkubernetesclusterresponse": {"id": "k8s-1", "state": "Running"},
    }

    kube = Kubernetes(client=mock_client)
    payload = StartKubernetesClusterRequest(id="k8s-1")
    response = kube.start_cluster(payload)

    assert response.data == {"id": "k8s-1", "state": "Running"}
    mock_client.call.assert_called_once_with("startKubernetesCluster", {"id": "k8s-1"})


def test_kubernetes_start_cluster_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={"startkubernetesclusterresponse": {"id": "k8s-1", "state": "Running"}}
    )

    kube = Kubernetes(client=mock_client)
    payload = StartKubernetesClusterRequest(id="k8s-1")
    response = asyncio.run(kube.start_cluster_async(payload))

    assert response.data == {"id": "k8s-1", "state": "Running"}
    mock_client.call_async.assert_called_once_with("startKubernetesCluster", {"id": "k8s-1"})


# ---------------------------------------------------------------------------
# stop_cluster
# ---------------------------------------------------------------------------


def test_kubernetes_stop_cluster_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "stopkubernetesclusterresponse": {"success": "true"},
    }

    kube = Kubernetes(client=mock_client)
    payload = StopKubernetesClusterRequest(id="k8s-1")
    response = kube.stop_cluster(payload)

    assert response.data == {"success": "true"}
    mock_client.call.assert_called_once_with("stopKubernetesCluster", {"id": "k8s-1"})


def test_kubernetes_stop_cluster_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={"stopkubernetesclusterresponse": {"success": "true"}}
    )

    kube = Kubernetes(client=mock_client)
    payload = StopKubernetesClusterRequest(id="k8s-1")
    response = asyncio.run(kube.stop_cluster_async(payload))

    assert response.data == {"success": "true"}
    mock_client.call_async.assert_called_once_with("stopKubernetesCluster", {"id": "k8s-1"})


# ---------------------------------------------------------------------------
# scale_cluster
# ---------------------------------------------------------------------------


def test_kubernetes_scale_cluster_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "scalekubernetesclusterresponse": {"id": "k8s-1", "size": 3},
    }

    kube = Kubernetes(client=mock_client)
    payload = ScaleKubernetesClusterRequest(id="k8s-1", size=3)
    response = kube.scale_cluster(payload)

    assert response.data == {"id": "k8s-1", "size": 3}
    mock_client.call.assert_called_once_with(
        "scaleKubernetesCluster", payload.model_dump(exclude_none=True)
    )


def test_kubernetes_scale_cluster_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={"scalekubernetesclusterresponse": {"id": "k8s-1", "size": 3}}
    )

    kube = Kubernetes(client=mock_client)
    payload = ScaleKubernetesClusterRequest(id="k8s-1", size=3)
    response = asyncio.run(kube.scale_cluster_async(payload))

    assert response.data == {"id": "k8s-1", "size": 3}
    mock_client.call_async.assert_called_once_with(
        "scaleKubernetesCluster", payload.model_dump(exclude_none=True)
    )


# ---------------------------------------------------------------------------
# upgrade_cluster
# ---------------------------------------------------------------------------


def test_kubernetes_upgrade_cluster_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "upgradekubernetesclusterresponse": {"id": "k8s-1", "kubernetesversionid": "v-2"},
    }

    kube = Kubernetes(client=mock_client)
    payload = UpgradeKubernetesClusterRequest(id="k8s-1", kubernetesVersionId="v-2")
    response = kube.upgrade_cluster(payload)

    assert response.data == {"id": "k8s-1", "kubernetesversionid": "v-2"}
    mock_client.call.assert_called_once_with(
        "upgradeKubernetesCluster", {"id": "k8s-1", "kubernetesversionid": "v-2"}
    )


def test_kubernetes_upgrade_cluster_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={
            "upgradekubernetesclusterresponse": {"id": "k8s-1", "kubernetesversionid": "v-2"}
        }
    )

    kube = Kubernetes(client=mock_client)
    payload = UpgradeKubernetesClusterRequest(id="k8s-1", kubernetesVersionId="v-2")
    response = asyncio.run(kube.upgrade_cluster_async(payload))

    assert response.data == {"id": "k8s-1", "kubernetesversionid": "v-2"}
    mock_client.call_async.assert_called_once_with(
        "upgradeKubernetesCluster", {"id": "k8s-1", "kubernetesversionid": "v-2"}
    )


# ---------------------------------------------------------------------------
# list_clusters
# ---------------------------------------------------------------------------


def test_kubernetes_list_clusters_parses_list_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "listkubernetesclustersresponse": {
            "kubernetescluster": [{"id": "k8s-1", "name": "cluster-1"}],
            "count": 1,
        }
    }

    kube = Kubernetes(client=mock_client)
    payload = ListKubernetesClustersRequest()
    response = kube.list_clusters(payload)

    assert response.data == [{"id": "k8s-1", "name": "cluster-1"}]
    assert response.count == 1
    mock_client.call.assert_called_once_with(
        "listKubernetesClusters", payload.model_dump(exclude_none=True)
    )


def test_kubernetes_list_clusters_async_parses_list_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={
            "listkubernetesclustersresponse": {
                "kubernetescluster": [{"id": "k8s-2", "name": "cluster-2"}],
                "count": 1,
            }
        }
    )

    kube = Kubernetes(client=mock_client)
    payload = ListKubernetesClustersRequest(name="cluster-2")
    response = asyncio.run(kube.list_clusters_async(payload))

    assert response.data == [{"id": "k8s-2", "name": "cluster-2"}]
    assert response.count == 1
    mock_client.call_async.assert_called_once_with(
        "listKubernetesClusters", payload.model_dump(exclude_none=True)
    )


# ---------------------------------------------------------------------------
# get_cluster_config
# ---------------------------------------------------------------------------


def test_kubernetes_get_cluster_config_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "getkubernetesclusterconfigresponse": {"id": "k8s-1", "configdata": "apiVersion: v1"},
    }

    kube = Kubernetes(client=mock_client)
    payload = GetKubernetesClusterConfigRequest(id="k8s-1")
    response = kube.get_cluster_config(payload)

    assert response.data == {"id": "k8s-1", "configdata": "apiVersion: v1"}
    mock_client.call.assert_called_once_with("getKubernetesClusterConfig", {"id": "k8s-1"})


def test_kubernetes_get_cluster_config_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={
            "getkubernetesclusterconfigresponse": {"id": "k8s-1", "configdata": "apiVersion: v1"}
        }
    )

    kube = Kubernetes(client=mock_client)
    payload = GetKubernetesClusterConfigRequest(id="k8s-1")
    response = asyncio.run(kube.get_cluster_config_async(payload))

    assert response.data == {"id": "k8s-1", "configdata": "apiVersion: v1"}
    mock_client.call_async.assert_called_once_with("getKubernetesClusterConfig", {"id": "k8s-1"})


# ---------------------------------------------------------------------------
# add_nodes / remove_nodes
# ---------------------------------------------------------------------------


def test_kubernetes_add_nodes_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "addnodestokubernetesclusterresponse": {"id": "k8s-1"},
    }

    kube = Kubernetes(client=mock_client)
    payload = AddNodesToKubernetesClusterRequest(id="k8s-1", nodeIds=["node-1", "node-2"])
    response = kube.add_nodes(payload)

    assert response.data == {"id": "k8s-1"}
    mock_client.call.assert_called_once_with(
        "addNodesToKubernetesCluster", {"id": "k8s-1", "nodeids": "node-1,node-2"}
    )


def test_kubernetes_add_nodes_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={"addnodestokubernetesclusterresponse": {"id": "k8s-1"}}
    )

    kube = Kubernetes(client=mock_client)
    payload = AddNodesToKubernetesClusterRequest(id="k8s-1", nodeIds=["node-1"])
    response = asyncio.run(kube.add_nodes_async(payload))

    assert response.data == {"id": "k8s-1"}
    mock_client.call_async.assert_called_once_with(
        "addNodesToKubernetesCluster", {"id": "k8s-1", "nodeids": "node-1"}
    )


def test_kubernetes_remove_nodes_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "removenodesfromkubernetesclusterresponse": {"id": "k8s-1"},
    }

    kube = Kubernetes(client=mock_client)
    payload = RemoveNodesFromKubernetesClusterRequest(id="k8s-1", nodeIds=["node-1"])
    response = kube.remove_nodes(payload)

    assert response.data == {"id": "k8s-1"}
    mock_client.call.assert_called_once_with(
        "removeNodesFromKubernetesCluster", {"id": "k8s-1", "nodeids": "node-1"}
    )


def test_kubernetes_remove_nodes_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={"removenodesfromkubernetesclusterresponse": {"id": "k8s-1"}}
    )

    kube = Kubernetes(client=mock_client)
    payload = RemoveNodesFromKubernetesClusterRequest(id="k8s-1", nodeIds=["node-1"])
    response = asyncio.run(kube.remove_nodes_async(payload))

    assert response.data == {"id": "k8s-1"}
    mock_client.call_async.assert_called_once_with(
        "removeNodesFromKubernetesCluster", {"id": "k8s-1", "nodeids": "node-1"}
    )


# ---------------------------------------------------------------------------
# add_virtual_machines / remove_virtual_machines
# ---------------------------------------------------------------------------


def test_kubernetes_add_virtual_machines_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "addvirtualmachinestokubernetesclusterresponse": {"success": "true"},
    }

    kube = Kubernetes(client=mock_client)
    payload = AddVirtualMachinesToKubernetesClusterRequest(id="k8s-1", virtualMachineIds=["vm-1"])
    response = kube.add_virtual_machines(payload)

    assert response.data == {"success": "true"}
    mock_client.call.assert_called_once_with(
        "addVirtualMachinesToKubernetesCluster", {"id": "k8s-1", "virtualmachineids": "vm-1"}
    )


def test_kubernetes_add_virtual_machines_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={"addvirtualmachinestokubernetesclusterresponse": {"success": "true"}}
    )

    kube = Kubernetes(client=mock_client)
    payload = AddVirtualMachinesToKubernetesClusterRequest(id="k8s-1", virtualMachineIds=["vm-1"])
    response = asyncio.run(kube.add_virtual_machines_async(payload))

    assert response.data == {"success": "true"}
    mock_client.call_async.assert_called_once_with(
        "addVirtualMachinesToKubernetesCluster", {"id": "k8s-1", "virtualmachineids": "vm-1"}
    )


def test_kubernetes_remove_virtual_machines_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "removevirtualmachinesfromkubernetesclusterresponse": {"id": "k8s-1"},
    }

    kube = Kubernetes(client=mock_client)
    payload = RemoveVirtualMachinesFromKubernetesClusterRequest(
        id="k8s-1", virtualMachineIds=["vm-1"]
    )
    response = kube.remove_virtual_machines(payload)

    assert response.data == {"id": "k8s-1"}
    mock_client.call.assert_called_once_with(
        "removeVirtualMachinesFromKubernetesCluster",
        payload.model_dump(exclude_none=True),
    )


def test_kubernetes_remove_virtual_machines_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={"removevirtualmachinesfromkubernetesclusterresponse": {"id": "k8s-1"}}
    )

    kube = Kubernetes(client=mock_client)
    payload = RemoveVirtualMachinesFromKubernetesClusterRequest(
        id="k8s-1", virtualMachineIds=["vm-1"]
    )
    response = asyncio.run(kube.remove_virtual_machines_async(payload))

    assert response.data == {"id": "k8s-1"}
    mock_client.call_async.assert_called_once_with(
        "removeVirtualMachinesFromKubernetesCluster",
        payload.model_dump(exclude_none=True),
    )


# ---------------------------------------------------------------------------
# supported versions
# ---------------------------------------------------------------------------


def test_kubernetes_add_supported_version_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "addkubernetessupportedversionresponse": {"id": "v-1", "semanticversion": "1.30.0"},
    }

    kube = Kubernetes(client=mock_client)
    payload = AddKubernetesSupportedVersionRequest(
        minCpuNumber=2, minMemory=2048, semanticVersion="1.30.0"
    )
    response = kube.add_supported_version(payload)

    assert response.data == {"id": "v-1", "semanticversion": "1.30.0"}
    mock_client.call.assert_called_once_with(
        "addKubernetesSupportedVersion", payload.model_dump(exclude_none=True)
    )


def test_kubernetes_add_supported_version_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={"addkubernetessupportedversionresponse": {"id": "v-1"}}
    )

    kube = Kubernetes(client=mock_client)
    payload = AddKubernetesSupportedVersionRequest(
        minCpuNumber=2, minMemory=2048, semanticVersion="1.30.0"
    )
    response = asyncio.run(kube.add_supported_version_async(payload))

    assert response.data == {"id": "v-1"}
    mock_client.call_async.assert_called_once_with(
        "addKubernetesSupportedVersion", payload.model_dump(exclude_none=True)
    )


def test_kubernetes_update_supported_version_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "updatekubernetessupportedversionresponse": {"id": "v-1", "state": "Disabled"},
    }

    kube = Kubernetes(client=mock_client)
    payload = UpdateKubernetesSupportedVersionRequest(id="v-1", state="Disabled")
    response = kube.update_supported_version(payload)

    assert response.data == {"id": "v-1", "state": "Disabled"}
    mock_client.call.assert_called_once_with(
        "updateKubernetesSupportedVersion", {"id": "v-1", "state": "Disabled"}
    )


def test_kubernetes_update_supported_version_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={
            "updatekubernetessupportedversionresponse": {"id": "v-1", "state": "Disabled"}
        }
    )

    kube = Kubernetes(client=mock_client)
    payload = UpdateKubernetesSupportedVersionRequest(id="v-1", state="Disabled")
    response = asyncio.run(kube.update_supported_version_async(payload))

    assert response.data == {"id": "v-1", "state": "Disabled"}
    mock_client.call_async.assert_called_once_with(
        "updateKubernetesSupportedVersion", {"id": "v-1", "state": "Disabled"}
    )


def test_kubernetes_delete_supported_version_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "deletekubernetessupportedversionresponse": {"success": "true"},
    }

    kube = Kubernetes(client=mock_client)
    payload = DeleteKubernetesSupportedVersionRequest(id="v-1")
    response = kube.delete_supported_version(payload)

    assert response.data == {"success": "true"}
    mock_client.call.assert_called_once_with("deleteKubernetesSupportedVersion", {"id": "v-1"})


def test_kubernetes_delete_supported_version_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={"deletekubernetessupportedversionresponse": {"success": "true"}}
    )

    kube = Kubernetes(client=mock_client)
    payload = DeleteKubernetesSupportedVersionRequest(id="v-1")
    response = asyncio.run(kube.delete_supported_version_async(payload))

    assert response.data == {"success": "true"}
    mock_client.call_async.assert_called_once_with(
        "deleteKubernetesSupportedVersion", {"id": "v-1"}
    )


def test_kubernetes_list_supported_versions_parses_list_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "listkubernetessupportedversionsresponse": {
            "kubernetessupportedversion": [{"id": "v-1", "semanticversion": "1.30.0"}],
            "count": 1,
        }
    }

    kube = Kubernetes(client=mock_client)
    payload = ListKubernetesSupportedVersionsRequest()
    response = kube.list_supported_versions(payload)

    assert response.data == [{"id": "v-1", "semanticversion": "1.30.0"}]
    assert response.count == 1
    mock_client.call.assert_called_once_with(
        "listKubernetesSupportedVersions", payload.model_dump(exclude_none=True)
    )


def test_kubernetes_list_supported_versions_async_parses_list_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={
            "listkubernetessupportedversionsresponse": {
                "kubernetessupportedversion": [{"id": "v-2", "semanticversion": "1.31.0"}],
                "count": 1,
            }
        }
    )

    kube = Kubernetes(client=mock_client)
    payload = ListKubernetesSupportedVersionsRequest()
    response = asyncio.run(kube.list_supported_versions_async(payload))

    assert response.data == [{"id": "v-2", "semanticversion": "1.31.0"}]
    assert response.count == 1
    mock_client.call_async.assert_called_once_with(
        "listKubernetesSupportedVersions", payload.model_dump(exclude_none=True)
    )


def test_kubernetes_get_upload_params_for_supported_version_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "getuploadparamsforkubernetessupportedversionresponse": {
            "id": "v-1",
            "postURL": "https://upload.example.com",
        },
    }

    kube = Kubernetes(client=mock_client)
    payload = GetUploadParamsForKubernetesSupportedVersionRequest(
        format="QCOW2",
        minCpuNumber=2,
        minMemory=2048,
        name="k8s-1.30.0",
        semanticVersion="1.30.0",
        zoneId="zone-1",
    )
    response = kube.get_upload_params_for_supported_version(payload)

    assert response.data == {"id": "v-1", "postURL": "https://upload.example.com"}
    mock_client.call.assert_called_once_with(
        "getUploadParamsForKubernetesSupportedVersion", payload.model_dump(exclude_none=True)
    )


def test_kubernetes_get_upload_params_for_supported_version_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={"getuploadparamsforkubernetessupportedversionresponse": {"id": "v-1"}}
    )

    kube = Kubernetes(client=mock_client)
    payload = GetUploadParamsForKubernetesSupportedVersionRequest(
        format="QCOW2",
        minCpuNumber=2,
        minMemory=2048,
        name="k8s-1.30.0",
        semanticVersion="1.30.0",
        zoneId="zone-1",
    )
    response = asyncio.run(kube.get_upload_params_for_supported_version_async(payload))

    assert response.data == {"id": "v-1"}
    mock_client.call_async.assert_called_once_with(
        "getUploadParamsForKubernetesSupportedVersion", payload.model_dump(exclude_none=True)
    )
