# services/load_balancer.py
from typing import Dict, List

from acs_sdk.schemas.request.load_balancer import (
    AssignCertToLoadBalancerRequest,
    AssignToGlobalLoadBalancerRuleRequest,
    AssignToLoadBalancerRuleRequest,
    CreateGlobalLoadBalancerRuleRequest,
    CreateLBHealthCheckPolicyRequest,
    CreateLBStickinessPolicyRequest,
    CreateLoadBalancerRequest,
    CreateLoadBalancerRuleRequest,
    DeleteGlobalLoadBalancerRuleRequest,
    DeleteLBHealthCheckPolicyRequest,
    DeleteLBStickinessPolicyRequest,
    DeleteLoadBalancerRequest,
    DeleteLoadBalancerRuleRequest,
    DeleteServicePackageOfferingRequest,
    DeployNetscalerVpxRequest,
    GetLoadBalancerSslCertificateRequest,
    ListGlobalLoadBalancerRulesRequest,
    ListLBHealthCheckPoliciesRequest,
    ListLBStickinessPoliciesRequest,
    ListLoadBalancerRuleInstancesRequest,
    ListLoadBalancerRulesRequest,
    ListLoadBalancersRequest,
    ListRegisteredServicePackagesRequest,
    RemoveCertFromLoadBalancerRequest,
    RemoveFromGlobalLoadBalancerRuleRequest,
    RemoveFromLoadBalancerRuleRequest,
    StopNetScalerVpxRequest,
    UpdateGlobalLoadBalancerRuleRequest,
    UpdateLBHealthCheckPolicyRequest,
    UpdateLBStickinessPolicyRequest,
    UpdateLoadBalancerRequest,
    UpdateLoadBalancerRuleRequest,
)

from .base import BaseService
from ..schemas.response.base import APIResponse


class LoadBalancer(BaseService):

    # -------------------------------------------------------------------------
    # Load balancer rules
    # -------------------------------------------------------------------------

    def create_rule(self, payload: CreateLoadBalancerRuleRequest) -> APIResponse[Dict]:
        """Create a load balancer rule."""
        return self._execute(
            "createLoadBalancerRule",
            payload,
            envelope="createloadbalancerruleresponse",
        )

    async def create_rule_async(self, payload: CreateLoadBalancerRuleRequest) -> APIResponse[Dict]:
        """Asynchronously create a load balancer rule."""
        return await self._execute_async(
            "createLoadBalancerRule",
            payload,
            envelope="createloadbalancerruleresponse",
        )

    def list_rules(self, payload: ListLoadBalancerRulesRequest) -> APIResponse[List[Dict]]:
        """List load balancer rules."""
        return self._execute(
            "listLoadBalancerRules",
            payload,
            envelope="listloadbalancerrulesresponse",
            entity="loadbalancerrule",
        )

    async def list_rules_async(self, payload: ListLoadBalancerRulesRequest) -> APIResponse[List[Dict]]:
        """Asynchronously list load balancer rules."""
        return await self._execute_async(
            "listLoadBalancerRules",
            payload,
            envelope="listloadbalancerrulesresponse",
            entity="loadbalancerrule",
        )

    def update_rule(self, payload: UpdateLoadBalancerRuleRequest) -> APIResponse[Dict]:
        """Update a load balancer rule."""
        return self._execute(
            "updateLoadBalancerRule",
            payload,
            envelope="updateloadbalancerruleresponse",
        )

    async def update_rule_async(self, payload: UpdateLoadBalancerRuleRequest) -> APIResponse[Dict]:
        """Asynchronously update a load balancer rule."""
        return await self._execute_async(
            "updateLoadBalancerRule",
            payload,
            envelope="updateloadbalancerruleresponse",
        )

    def delete_rule(self, payload: DeleteLoadBalancerRuleRequest) -> APIResponse[Dict]:
        """Delete a load balancer rule."""
        return self._execute(
            "deleteLoadBalancerRule",
            payload,
            envelope="deleteloadbalancerruleresponse",
        )

    async def delete_rule_async(self, payload: DeleteLoadBalancerRuleRequest) -> APIResponse[Dict]:
        """Asynchronously delete a load balancer rule."""
        return await self._execute_async(
            "deleteLoadBalancerRule",
            payload,
            envelope="deleteloadbalancerruleresponse",
        )

    def assign_to_rule(self, payload: AssignToLoadBalancerRuleRequest) -> APIResponse[Dict]:
        """Assign virtual machine(s) to a load balancer rule."""
        return self._execute(
            "assignToLoadBalancerRule",
            payload,
            envelope="assigntoloadbalancerruleresponse",
        )

    async def assign_to_rule_async(self, payload: AssignToLoadBalancerRuleRequest) -> APIResponse[Dict]:
        """Asynchronously assign virtual machine(s) to a load balancer rule."""
        return await self._execute_async(
            "assignToLoadBalancerRule",
            payload,
            envelope="assigntoloadbalancerruleresponse",
        )

    def remove_from_rule(self, payload: RemoveFromLoadBalancerRuleRequest) -> APIResponse[Dict]:
        """Remove virtual machine(s) from a load balancer rule."""
        return self._execute(
            "removeFromLoadBalancerRule",
            payload,
            envelope="removefromloadbalancerruleresponse",
        )

    async def remove_from_rule_async(
        self, payload: RemoveFromLoadBalancerRuleRequest
    ) -> APIResponse[Dict]:
        """Asynchronously remove virtual machine(s) from a load balancer rule."""
        return await self._execute_async(
            "removeFromLoadBalancerRule",
            payload,
            envelope="removefromloadbalancerruleresponse",
        )

    def list_rule_instances(
        self, payload: ListLoadBalancerRuleInstancesRequest
    ) -> APIResponse[Dict]:
        """List virtual machine instances assigned to a load balancer rule."""
        return self._execute(
            "listLoadBalancerRuleInstances",
            payload,
            envelope="listloadbalancerruleinstancesresponse",
        )

    async def list_rule_instances_async(
        self, payload: ListLoadBalancerRuleInstancesRequest
    ) -> APIResponse[Dict]:
        """Asynchronously list virtual machine instances assigned to a load balancer rule."""
        return await self._execute_async(
            "listLoadBalancerRuleInstances",
            payload,
            envelope="listloadbalancerruleinstancesresponse",
        )

    # -------------------------------------------------------------------------
    # LB health check policy
    # -------------------------------------------------------------------------

    def create_health_check_policy(
        self, payload: CreateLBHealthCheckPolicyRequest
    ) -> APIResponse[Dict]:
        """Create a load balancer health check policy."""
        return self._execute(
            "createLBHealthCheckPolicy",
            payload,
            envelope="createlbhealthcheckpolicyresponse",
        )

    async def create_health_check_policy_async(
        self, payload: CreateLBHealthCheckPolicyRequest
    ) -> APIResponse[Dict]:
        """Asynchronously create a load balancer health check policy."""
        return await self._execute_async(
            "createLBHealthCheckPolicy",
            payload,
            envelope="createlbhealthcheckpolicyresponse",
        )

    def delete_health_check_policy(
        self, payload: DeleteLBHealthCheckPolicyRequest
    ) -> APIResponse[Dict]:
        """Delete a load balancer health check policy."""
        return self._execute(
            "deleteLBHealthCheckPolicy",
            payload,
            envelope="deletelbhealthcheckpolicyresponse",
        )

    async def delete_health_check_policy_async(
        self, payload: DeleteLBHealthCheckPolicyRequest
    ) -> APIResponse[Dict]:
        """Asynchronously delete a load balancer health check policy."""
        return await self._execute_async(
            "deleteLBHealthCheckPolicy",
            payload,
            envelope="deletelbhealthcheckpolicyresponse",
        )

    def update_health_check_policy(
        self, payload: UpdateLBHealthCheckPolicyRequest
    ) -> APIResponse[Dict]:
        """Update a load balancer health check policy."""
        return self._execute(
            "updateLBHealthCheckPolicy",
            payload,
            envelope="updatelbhealthcheckpolicyresponse",
        )

    async def update_health_check_policy_async(
        self, payload: UpdateLBHealthCheckPolicyRequest
    ) -> APIResponse[Dict]:
        """Asynchronously update a load balancer health check policy."""
        return await self._execute_async(
            "updateLBHealthCheckPolicy",
            payload,
            envelope="updatelbhealthcheckpolicyresponse",
        )

    def list_health_check_policies(
        self, payload: ListLBHealthCheckPoliciesRequest
    ) -> APIResponse[Dict]:
        """List load balancer health check policies."""
        return self._execute(
            "listLBHealthCheckPolicies",
            payload,
            envelope="listlbhealthcheckpoliciesresponse",
        )

    async def list_health_check_policies_async(
        self, payload: ListLBHealthCheckPoliciesRequest
    ) -> APIResponse[Dict]:
        """Asynchronously list load balancer health check policies."""
        return await self._execute_async(
            "listLBHealthCheckPolicies",
            payload,
            envelope="listlbhealthcheckpoliciesresponse",
        )

    # -------------------------------------------------------------------------
    # LB stickiness policy
    # -------------------------------------------------------------------------

    def create_stickiness_policy(
        self, payload: CreateLBStickinessPolicyRequest
    ) -> APIResponse[Dict]:
        """Create a load balancer stickiness policy."""
        return self._execute(
            "createLBStickinessPolicy",
            payload,
            envelope="createlbstickinesspolicyresponse",
        )

    async def create_stickiness_policy_async(
        self, payload: CreateLBStickinessPolicyRequest
    ) -> APIResponse[Dict]:
        """Asynchronously create a load balancer stickiness policy."""
        return await self._execute_async(
            "createLBStickinessPolicy",
            payload,
            envelope="createlbstickinesspolicyresponse",
        )

    def delete_stickiness_policy(
        self, payload: DeleteLBStickinessPolicyRequest
    ) -> APIResponse[Dict]:
        """Delete a load balancer stickiness policy."""
        return self._execute(
            "deleteLBStickinessPolicy",
            payload,
            envelope="deletelbstickinesspolicyresponse",
        )

    async def delete_stickiness_policy_async(
        self, payload: DeleteLBStickinessPolicyRequest
    ) -> APIResponse[Dict]:
        """Asynchronously delete a load balancer stickiness policy."""
        return await self._execute_async(
            "deleteLBStickinessPolicy",
            payload,
            envelope="deletelbstickinesspolicyresponse",
        )

    def update_stickiness_policy(
        self, payload: UpdateLBStickinessPolicyRequest
    ) -> APIResponse[Dict]:
        """Update a load balancer stickiness policy."""
        return self._execute(
            "updateLBStickinessPolicy",
            payload,
            envelope="updatelbstickinesspolicyresponse",
        )

    async def update_stickiness_policy_async(
        self, payload: UpdateLBStickinessPolicyRequest
    ) -> APIResponse[Dict]:
        """Asynchronously update a load balancer stickiness policy."""
        return await self._execute_async(
            "updateLBStickinessPolicy",
            payload,
            envelope="updatelbstickinesspolicyresponse",
        )

    def list_stickiness_policies(
        self, payload: ListLBStickinessPoliciesRequest
    ) -> APIResponse[Dict]:
        """List load balancer stickiness policies."""
        return self._execute(
            "listLBStickinessPolicies",
            payload,
            envelope="listlbstickinesspoliciesresponse",
        )

    async def list_stickiness_policies_async(
        self, payload: ListLBStickinessPoliciesRequest
    ) -> APIResponse[Dict]:
        """Asynchronously list load balancer stickiness policies."""
        return await self._execute_async(
            "listLBStickinessPolicies",
            payload,
            envelope="listlbstickinesspoliciesresponse",
        )

    # -------------------------------------------------------------------------
    # Internal load balancer
    # -------------------------------------------------------------------------

    def create(self, payload: CreateLoadBalancerRequest) -> APIResponse[Dict]:
        """Create an internal load balancer."""
        return self._execute(
            "createLoadBalancer",
            payload,
            envelope="createloadbalancerresponse",
        )

    async def create_async(self, payload: CreateLoadBalancerRequest) -> APIResponse[Dict]:
        """Asynchronously create an internal load balancer."""
        return await self._execute_async(
            "createLoadBalancer",
            payload,
            envelope="createloadbalancerresponse",
        )

    def list(self, payload: ListLoadBalancersRequest) -> APIResponse[List[Dict]]:
        """List internal load balancers."""
        return self._execute(
            "listLoadBalancers",
            payload,
            envelope="listloadbalancersresponse",
            entity="loadbalancer",
        )

    async def list_async(self, payload: ListLoadBalancersRequest) -> APIResponse[List[Dict]]:
        """Asynchronously list internal load balancers."""
        return await self._execute_async(
            "listLoadBalancers",
            payload,
            envelope="listloadbalancersresponse",
            entity="loadbalancer",
        )

    def update(self, payload: UpdateLoadBalancerRequest) -> APIResponse[Dict]:
        """Update an internal load balancer."""
        return self._execute(
            "updateLoadBalancer",
            payload,
            envelope="updateloadbalancerresponse",
        )

    async def update_async(self, payload: UpdateLoadBalancerRequest) -> APIResponse[Dict]:
        """Asynchronously update an internal load balancer."""
        return await self._execute_async(
            "updateLoadBalancer",
            payload,
            envelope="updateloadbalancerresponse",
        )

    def delete(self, payload: DeleteLoadBalancerRequest) -> APIResponse[Dict]:
        """Delete an internal load balancer."""
        return self._execute(
            "deleteLoadBalancer",
            payload,
            envelope="deleteloadbalancerresponse",
        )

    async def delete_async(self, payload: DeleteLoadBalancerRequest) -> APIResponse[Dict]:
        """Asynchronously delete an internal load balancer."""
        return await self._execute_async(
            "deleteLoadBalancer",
            payload,
            envelope="deleteloadbalancerresponse",
        )

    # -------------------------------------------------------------------------
    # Global (GSLB) load balancer rules
    # -------------------------------------------------------------------------

    def create_global_rule(
        self, payload: CreateGlobalLoadBalancerRuleRequest
    ) -> APIResponse[Dict]:
        """Create a global load balancer rule."""
        return self._execute(
            "createGlobalLoadBalancerRule",
            payload,
            envelope="creategloballoadbalancerruleresponse",
        )

    async def create_global_rule_async(
        self, payload: CreateGlobalLoadBalancerRuleRequest
    ) -> APIResponse[Dict]:
        """Asynchronously create a global load balancer rule."""
        return await self._execute_async(
            "createGlobalLoadBalancerRule",
            payload,
            envelope="creategloballoadbalancerruleresponse",
        )

    def list_global_rules(
        self, payload: ListGlobalLoadBalancerRulesRequest
    ) -> APIResponse[List[Dict]]:
        """List global load balancer rules."""
        return self._execute(
            "listGlobalLoadBalancerRules",
            payload,
            envelope="listgloballoadbalancerrulesresponse",
            entity="globalloadbalancerrule",
        )

    async def list_global_rules_async(
        self, payload: ListGlobalLoadBalancerRulesRequest
    ) -> APIResponse[List[Dict]]:
        """Asynchronously list global load balancer rules."""
        return await self._execute_async(
            "listGlobalLoadBalancerRules",
            payload,
            envelope="listgloballoadbalancerrulesresponse",
            entity="globalloadbalancerrule",
        )

    def update_global_rule(
        self, payload: UpdateGlobalLoadBalancerRuleRequest
    ) -> APIResponse[Dict]:
        """Update a global load balancer rule."""
        return self._execute(
            "updateGlobalLoadBalancerRule",
            payload,
            envelope="updategloballoadbalancerruleresponse",
        )

    async def update_global_rule_async(
        self, payload: UpdateGlobalLoadBalancerRuleRequest
    ) -> APIResponse[Dict]:
        """Asynchronously update a global load balancer rule."""
        return await self._execute_async(
            "updateGlobalLoadBalancerRule",
            payload,
            envelope="updategloballoadbalancerruleresponse",
        )

    def delete_global_rule(
        self, payload: DeleteGlobalLoadBalancerRuleRequest
    ) -> APIResponse[Dict]:
        """Delete a global load balancer rule."""
        return self._execute(
            "deleteGlobalLoadBalancerRule",
            payload,
            envelope="deletegloballoadbalancerruleresponse",
        )

    async def delete_global_rule_async(
        self, payload: DeleteGlobalLoadBalancerRuleRequest
    ) -> APIResponse[Dict]:
        """Asynchronously delete a global load balancer rule."""
        return await self._execute_async(
            "deleteGlobalLoadBalancerRule",
            payload,
            envelope="deletegloballoadbalancerruleresponse",
        )

    def assign_to_global_rule(
        self, payload: AssignToGlobalLoadBalancerRuleRequest
    ) -> APIResponse[Dict]:
        """Assign load balancer rule(s) to a global load balancer rule."""
        return self._execute(
            "assignToGlobalLoadBalancerRule",
            payload,
            envelope="assigntogloballoadbalancerruleresponse",
        )

    async def assign_to_global_rule_async(
        self, payload: AssignToGlobalLoadBalancerRuleRequest
    ) -> APIResponse[Dict]:
        """Asynchronously assign load balancer rule(s) to a global load balancer rule."""
        return await self._execute_async(
            "assignToGlobalLoadBalancerRule",
            payload,
            envelope="assigntogloballoadbalancerruleresponse",
        )

    def remove_from_global_rule(
        self, payload: RemoveFromGlobalLoadBalancerRuleRequest
    ) -> APIResponse[Dict]:
        """Remove a load balancer rule association from a global load balancer rule."""
        return self._execute(
            "removeFromGlobalLoadBalancerRule",
            payload,
            envelope="removefromgloballoadbalancerruleresponse",
        )

    async def remove_from_global_rule_async(
        self, payload: RemoveFromGlobalLoadBalancerRuleRequest
    ) -> APIResponse[Dict]:
        """Asynchronously remove a load balancer rule association from a global load balancer rule."""
        return await self._execute_async(
            "removeFromGlobalLoadBalancerRule",
            payload,
            envelope="removefromgloballoadbalancerruleresponse",
        )

    # -------------------------------------------------------------------------
    # SSL certificate
    # -------------------------------------------------------------------------

    def assign_cert(self, payload: AssignCertToLoadBalancerRequest) -> APIResponse[Dict]:
        """Assign a certificate to a load balancer rule."""
        return self._execute(
            "assignCertToLoadBalancer",
            payload,
            envelope="assigncerttoloadbalancerresponse",
        )

    async def assign_cert_async(
        self, payload: AssignCertToLoadBalancerRequest
    ) -> APIResponse[Dict]:
        """Asynchronously assign a certificate to a load balancer rule."""
        return await self._execute_async(
            "assignCertToLoadBalancer",
            payload,
            envelope="assigncerttoloadbalancerresponse",
        )

    def remove_cert(self, payload: RemoveCertFromLoadBalancerRequest) -> APIResponse[Dict]:
        """Remove a certificate from a load balancer rule."""
        return self._execute(
            "removeCertFromLoadBalancer",
            payload,
            envelope="removecertfromloadbalancerresponse",
        )

    async def remove_cert_async(
        self, payload: RemoveCertFromLoadBalancerRequest
    ) -> APIResponse[Dict]:
        """Asynchronously remove a certificate from a load balancer rule."""
        return await self._execute_async(
            "removeCertFromLoadBalancer",
            payload,
            envelope="removecertfromloadbalancerresponse",
        )

    def get_ssl_certificate(
        self, payload: GetLoadBalancerSslCertificateRequest
    ) -> APIResponse[Dict]:
        """Get the SSL certificate assigned to a load balancer."""
        return self._execute(
            "getLoadBalancerSslCertificate",
            payload,
            envelope="getloadbalancersslcertificateresponse",
        )

    async def get_ssl_certificate_async(
        self, payload: GetLoadBalancerSslCertificateRequest
    ) -> APIResponse[Dict]:
        """Asynchronously get the SSL certificate assigned to a load balancer."""
        return await self._execute_async(
            "getLoadBalancerSslCertificate",
            payload,
            envelope="getloadbalancersslcertificateresponse",
        )

    # -------------------------------------------------------------------------
    # NetScaler VPX
    # -------------------------------------------------------------------------

    def deploy_netscaler_vpx(self, payload: DeployNetscalerVpxRequest) -> APIResponse[Dict]:
        """Deploy a new NetScaler VPX."""
        return self._execute(
            "deployNetscalerVpx",
            payload,
            envelope="deploynetscalervpxresponse",
        )

    async def deploy_netscaler_vpx_async(
        self, payload: DeployNetscalerVpxRequest
    ) -> APIResponse[Dict]:
        """Asynchronously deploy a new NetScaler VPX."""
        return await self._execute_async(
            "deployNetscalerVpx",
            payload,
            envelope="deploynetscalervpxresponse",
        )

    def stop_netscaler_vpx(self, payload: StopNetScalerVpxRequest) -> APIResponse[Dict]:
        """Stop a NetScaler VPX VM."""
        return self._execute(
            "stopNetScalerVpx",
            payload,
            envelope="stopnetscalervpxresponse",
        )

    async def stop_netscaler_vpx_async(
        self, payload: StopNetScalerVpxRequest
    ) -> APIResponse[Dict]:
        """Asynchronously stop a NetScaler VPX VM."""
        return await self._execute_async(
            "stopNetScalerVpx",
            payload,
            envelope="stopnetscalervpxresponse",
        )

    # -------------------------------------------------------------------------
    # Service packages
    # -------------------------------------------------------------------------

    def list_registered_service_packages(
        self, payload: ListRegisteredServicePackagesRequest
    ) -> APIResponse[List[Dict]]:
        """List registered service packages."""
        return self._execute(
            "listRegisteredServicePackages",
            payload,
            envelope="listregisteredservicepackagesresponse",
            entity="servicepackage",
        )

    async def list_registered_service_packages_async(
        self, payload: ListRegisteredServicePackagesRequest
    ) -> APIResponse[List[Dict]]:
        """Asynchronously list registered service packages."""
        return await self._execute_async(
            "listRegisteredServicePackages",
            payload,
            envelope="listregisteredservicepackagesresponse",
            entity="servicepackage",
        )

    def delete_service_package_offering(
        self, payload: DeleteServicePackageOfferingRequest
    ) -> APIResponse[Dict]:
        """Delete a service package offering."""
        return self._execute(
            "deleteServicePackageOffering",
            payload,
            envelope="deleteservicepackageofferingresponse",
        )

    async def delete_service_package_offering_async(
        self, payload: DeleteServicePackageOfferingRequest
    ) -> APIResponse[Dict]:
        """Asynchronously delete a service package offering."""
        return await self._execute_async(
            "deleteServicePackageOffering",
            payload,
            envelope="deleteservicepackageofferingresponse",
        )
