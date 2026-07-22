# services/kubernetes.py
from typing import Dict, List

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

from .base import BaseService
from ..schemas.response.base import APIResponse


class Kubernetes(BaseService):
    # -------------------------------------------------------------------------
    # Cluster lifecycle
    # -------------------------------------------------------------------------

    def create_cluster(self, payload: CreateKubernetesClusterRequest) -> APIResponse[Dict]:
        """Create a Kubernetes cluster."""
        return self._execute(
            "createKubernetesCluster",
            payload,
            envelope="createkubernetesclusterresponse",
        )

    async def create_cluster_async(
        self, payload: CreateKubernetesClusterRequest
    ) -> APIResponse[Dict]:
        """Asynchronously create a Kubernetes cluster."""
        return await self._execute_async(
            "createKubernetesCluster",
            payload,
            envelope="createkubernetesclusterresponse",
        )

    def delete_cluster(self, payload: DeleteKubernetesClusterRequest) -> APIResponse[Dict]:
        """Delete a Kubernetes cluster."""
        return self._execute(
            "deleteKubernetesCluster",
            payload,
            envelope="deletekubernetesclusterresponse",
        )

    async def delete_cluster_async(
        self, payload: DeleteKubernetesClusterRequest
    ) -> APIResponse[Dict]:
        """Asynchronously delete a Kubernetes cluster."""
        return await self._execute_async(
            "deleteKubernetesCluster",
            payload,
            envelope="deletekubernetesclusterresponse",
        )

    def start_cluster(self, payload: StartKubernetesClusterRequest) -> APIResponse[Dict]:
        """Start a stopped CloudManaged Kubernetes cluster."""
        return self._execute(
            "startKubernetesCluster",
            payload,
            envelope="startkubernetesclusterresponse",
        )

    async def start_cluster_async(
        self, payload: StartKubernetesClusterRequest
    ) -> APIResponse[Dict]:
        """Asynchronously start a stopped CloudManaged Kubernetes cluster."""
        return await self._execute_async(
            "startKubernetesCluster",
            payload,
            envelope="startkubernetesclusterresponse",
        )

    def stop_cluster(self, payload: StopKubernetesClusterRequest) -> APIResponse[Dict]:
        """Stop a running CloudManaged Kubernetes cluster."""
        return self._execute(
            "stopKubernetesCluster",
            payload,
            envelope="stopkubernetesclusterresponse",
        )

    async def stop_cluster_async(self, payload: StopKubernetesClusterRequest) -> APIResponse[Dict]:
        """Asynchronously stop a running CloudManaged Kubernetes cluster."""
        return await self._execute_async(
            "stopKubernetesCluster",
            payload,
            envelope="stopkubernetesclusterresponse",
        )

    def scale_cluster(self, payload: ScaleKubernetesClusterRequest) -> APIResponse[Dict]:
        """Scale a created, running or stopped CloudManaged Kubernetes cluster."""
        return self._execute(
            "scaleKubernetesCluster",
            payload,
            envelope="scalekubernetesclusterresponse",
        )

    async def scale_cluster_async(
        self, payload: ScaleKubernetesClusterRequest
    ) -> APIResponse[Dict]:
        """Asynchronously scale a created, running or stopped CloudManaged Kubernetes cluster."""
        return await self._execute_async(
            "scaleKubernetesCluster",
            payload,
            envelope="scalekubernetesclusterresponse",
        )

    def upgrade_cluster(self, payload: UpgradeKubernetesClusterRequest) -> APIResponse[Dict]:
        """Upgrade a running CloudManaged Kubernetes cluster."""
        return self._execute(
            "upgradeKubernetesCluster",
            payload,
            envelope="upgradekubernetesclusterresponse",
        )

    async def upgrade_cluster_async(
        self, payload: UpgradeKubernetesClusterRequest
    ) -> APIResponse[Dict]:
        """Asynchronously upgrade a running CloudManaged Kubernetes cluster."""
        return await self._execute_async(
            "upgradeKubernetesCluster",
            payload,
            envelope="upgradekubernetesclusterresponse",
        )

    # -------------------------------------------------------------------------
    # Cluster list / config
    # -------------------------------------------------------------------------

    def list_clusters(self, payload: ListKubernetesClustersRequest) -> APIResponse[List[Dict]]:
        """List Kubernetes clusters."""
        return self._execute(
            "listKubernetesClusters",
            payload,
            envelope="listkubernetesclustersresponse",
            entity="kubernetescluster",
        )

    async def list_clusters_async(
        self, payload: ListKubernetesClustersRequest
    ) -> APIResponse[List[Dict]]:
        """Asynchronously list Kubernetes clusters."""
        return await self._execute_async(
            "listKubernetesClusters",
            payload,
            envelope="listkubernetesclustersresponse",
            entity="kubernetescluster",
        )

    def get_cluster_config(self, payload: GetKubernetesClusterConfigRequest) -> APIResponse[Dict]:
        """Get the config for a Kubernetes cluster."""
        return self._execute(
            "getKubernetesClusterConfig",
            payload,
            envelope="getkubernetesclusterconfigresponse",
        )

    async def get_cluster_config_async(
        self, payload: GetKubernetesClusterConfigRequest
    ) -> APIResponse[Dict]:
        """Asynchronously get the config for a Kubernetes cluster."""
        return await self._execute_async(
            "getKubernetesClusterConfig",
            payload,
            envelope="getkubernetesclusterconfigresponse",
        )

    # -------------------------------------------------------------------------
    # Node management
    # -------------------------------------------------------------------------

    def add_nodes(self, payload: AddNodesToKubernetesClusterRequest) -> APIResponse[Dict]:
        """Add nodes as workers to an existing CKS cluster."""
        return self._execute(
            "addNodesToKubernetesCluster",
            payload,
            envelope="addnodestokubernetesclusterresponse",
        )

    async def add_nodes_async(
        self, payload: AddNodesToKubernetesClusterRequest
    ) -> APIResponse[Dict]:
        """Asynchronously add nodes as workers to an existing CKS cluster."""
        return await self._execute_async(
            "addNodesToKubernetesCluster",
            payload,
            envelope="addnodestokubernetesclusterresponse",
        )

    def remove_nodes(self, payload: RemoveNodesFromKubernetesClusterRequest) -> APIResponse[Dict]:
        """Remove external nodes from a CKS cluster."""
        return self._execute(
            "removeNodesFromKubernetesCluster",
            payload,
            envelope="removenodesfromkubernetesclusterresponse",
        )

    async def remove_nodes_async(
        self, payload: RemoveNodesFromKubernetesClusterRequest
    ) -> APIResponse[Dict]:
        """Asynchronously remove external nodes from a CKS cluster."""
        return await self._execute_async(
            "removeNodesFromKubernetesCluster",
            payload,
            envelope="removenodesfromkubernetesclusterresponse",
        )

    # -------------------------------------------------------------------------
    # VM management (ExternalManaged clusters)
    # -------------------------------------------------------------------------

    def add_virtual_machines(
        self, payload: AddVirtualMachinesToKubernetesClusterRequest
    ) -> APIResponse[Dict]:
        """Add VMs to an ExternalManaged Kubernetes cluster."""
        return self._execute(
            "addVirtualMachinesToKubernetesCluster",
            payload,
            envelope="addvirtualmachinestokubernetesclusterresponse",
        )

    async def add_virtual_machines_async(
        self, payload: AddVirtualMachinesToKubernetesClusterRequest
    ) -> APIResponse[Dict]:
        """Asynchronously add VMs to an ExternalManaged Kubernetes cluster."""
        return await self._execute_async(
            "addVirtualMachinesToKubernetesCluster",
            payload,
            envelope="addvirtualmachinestokubernetesclusterresponse",
        )

    def remove_virtual_machines(
        self, payload: RemoveVirtualMachinesFromKubernetesClusterRequest
    ) -> APIResponse[Dict]:
        """Remove VMs from an ExternalManaged Kubernetes cluster."""
        return self._execute(
            "removeVirtualMachinesFromKubernetesCluster",
            payload,
            envelope="removevirtualmachinesfromkubernetesclusterresponse",
        )

    async def remove_virtual_machines_async(
        self, payload: RemoveVirtualMachinesFromKubernetesClusterRequest
    ) -> APIResponse[Dict]:
        """Asynchronously remove VMs from an ExternalManaged Kubernetes cluster."""
        return await self._execute_async(
            "removeVirtualMachinesFromKubernetesCluster",
            payload,
            envelope="removevirtualmachinesfromkubernetesclusterresponse",
        )

    # -------------------------------------------------------------------------
    # Supported versions
    # -------------------------------------------------------------------------

    def add_supported_version(
        self, payload: AddKubernetesSupportedVersionRequest
    ) -> APIResponse[Dict]:
        """Add a supported Kubernetes version."""
        return self._execute(
            "addKubernetesSupportedVersion",
            payload,
            envelope="addkubernetessupportedversionresponse",
        )

    async def add_supported_version_async(
        self, payload: AddKubernetesSupportedVersionRequest
    ) -> APIResponse[Dict]:
        """Asynchronously add a supported Kubernetes version."""
        return await self._execute_async(
            "addKubernetesSupportedVersion",
            payload,
            envelope="addkubernetessupportedversionresponse",
        )

    def update_supported_version(
        self, payload: UpdateKubernetesSupportedVersionRequest
    ) -> APIResponse[Dict]:
        """Update a supported Kubernetes version."""
        return self._execute(
            "updateKubernetesSupportedVersion",
            payload,
            envelope="updatekubernetessupportedversionresponse",
        )

    async def update_supported_version_async(
        self, payload: UpdateKubernetesSupportedVersionRequest
    ) -> APIResponse[Dict]:
        """Asynchronously update a supported Kubernetes version."""
        return await self._execute_async(
            "updateKubernetesSupportedVersion",
            payload,
            envelope="updatekubernetessupportedversionresponse",
        )

    def delete_supported_version(
        self, payload: DeleteKubernetesSupportedVersionRequest
    ) -> APIResponse[Dict]:
        """Delete a supported Kubernetes version."""
        return self._execute(
            "deleteKubernetesSupportedVersion",
            payload,
            envelope="deletekubernetessupportedversionresponse",
        )

    async def delete_supported_version_async(
        self, payload: DeleteKubernetesSupportedVersionRequest
    ) -> APIResponse[Dict]:
        """Asynchronously delete a supported Kubernetes version."""
        return await self._execute_async(
            "deleteKubernetesSupportedVersion",
            payload,
            envelope="deletekubernetessupportedversionresponse",
        )

    def list_supported_versions(
        self, payload: ListKubernetesSupportedVersionsRequest
    ) -> APIResponse[List[Dict]]:
        """List supported Kubernetes versions."""
        return self._execute(
            "listKubernetesSupportedVersions",
            payload,
            envelope="listkubernetessupportedversionsresponse",
            entity="kubernetessupportedversion",
        )

    async def list_supported_versions_async(
        self, payload: ListKubernetesSupportedVersionsRequest
    ) -> APIResponse[List[Dict]]:
        """Asynchronously list supported Kubernetes versions."""
        return await self._execute_async(
            "listKubernetesSupportedVersions",
            payload,
            envelope="listkubernetessupportedversionsresponse",
            entity="kubernetessupportedversion",
        )

    def get_upload_params_for_supported_version(
        self, payload: GetUploadParamsForKubernetesSupportedVersionRequest
    ) -> APIResponse[Dict]:
        """Get the parameters required to upload a supported Kubernetes version ISO."""
        return self._execute(
            "getUploadParamsForKubernetesSupportedVersion",
            payload,
            envelope="getuploadparamsforkubernetessupportedversionresponse",
        )

    async def get_upload_params_for_supported_version_async(
        self, payload: GetUploadParamsForKubernetesSupportedVersionRequest
    ) -> APIResponse[Dict]:
        """Asynchronously get the parameters required to upload a supported Kubernetes version ISO."""
        return await self._execute_async(
            "getUploadParamsForKubernetesSupportedVersion",
            payload,
            envelope="getuploadparamsforkubernetessupportedversionresponse",
        )
