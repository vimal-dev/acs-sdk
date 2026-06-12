from __future__ import annotations

import re
from enum import StrEnum
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, field_serializer, field_validator, model_validator

from .base import APIRequest, PaginationMixin


# ---------------------------------------------------------------------------
# Enums
# ---------------------------------------------------------------------------

class BootMode(StrEnum):
    LEGACY = "Legacy"
    SECURE = "Secure"


class BootType(StrEnum):
    BIOS = "BIOS"
    UEFI = "UEFI"


class KeyboardType(StrEnum):
    DE     = "de"
    DE_CH  = "de-ch"
    ES     = "es"
    FI     = "fi"
    FR     = "fr"
    FR_BE  = "fr-be"
    FR_CH  = "fr-ch"
    IS     = "is"
    IT     = "it"
    JP     = "jp"
    NL_BE  = "nl-be"
    NO     = "no"
    PT     = "pt"
    UK     = "uk"
    US     = "us"


class LeaseExpiryAction(StrEnum):
    STOP    = "STOP"
    DESTROY = "DESTROY"


class IODriverPolicy(StrEnum):
    NATIVE   = "native"
    THREADS  = "threads"
    IO_URING = "io_uring"


# ---------------------------------------------------------------------------
# Helper models
# ---------------------------------------------------------------------------

class UserDataDetail(BaseModel):
    key: str = Field(..., description="Variable name declared in userdata")
    value: str = Field(..., description="Value for the userdata variable")


class MigrateToEntry(BaseModel):
    """Volume-to-storage-pool mapping entry for migrateVirtualMachineWithVolume."""

    volume: str = Field(..., description="UUID of the volume to migrate")
    pool: str = Field(..., description="UUID of the destination storage pool")


class IpToNetworkEntry(BaseModel):
    """One entry in iptonetworklist[]"""
    networkid: str  = Field(..., description="UUID of the network")
    ip:        str | None = None
    ipv6:      str | None = None
    mac:       str | None = None
 
 
class DhcpOptionNetworkEntry(BaseModel):
    """One entry in dhcpoptionsnetworklist[]"""
    networkid: str = Field(..., description="UUID of the network")
    options:   dict[str, str] = Field(default_factory=dict,
                                      description="dhcp:<code>=<value> pairs")
 
 
class DataDiskDetail(BaseModel):
    """One entry in datadisksdetails[]"""
    diskofferingid: str = Field(..., description="UUID of the Disk Offering")
    size:           int | None = Field(None, gt=0, description="GB")
    miniops:        int | None = None
    maxiops:        int | None = None
 
 
class NicNetworkEntry(BaseModel):
    """VMware only — nicnetworklist[]"""
    ip:      str
    network: str


# ---------------------------------------------------------------------------
# Request classes
# ---------------------------------------------------------------------------

class AddNICToVirtualMachineRequest(APIRequest):
    """Reference: https://cloudstack.apache.org/api/apidocs-4.22/apis/addNicToVirtualMachine.html"""

    virtualmachineid: str = Field(..., alias="virtualMachineId", description="ID of the virtual machine")
    networkid: str = Field(..., alias="networkId", description="ID of the network to add the NIC to")
    dhcpoptions: Optional[str] = Field(
        None,
        description=(
            "DHCP options passed to the nic. "
            "Example: dhcpoptions[0].dhcp:114=url&dhcpoptions[0].dhcp:66=www.test.com"
        ),
    )
    ipaddress: Optional[str] = Field(
        None,
        description="IP address for the new NIC. Auto-allocated from the network if not specified.",
    )
    macaddress: Optional[str] = Field(None, description="MAC address for the new NIC.")


class AssignVirtualMachineRequest(APIRequest):
    """Reference: https://cloudstack.apache.org/api/apidocs-4.22/apis/assignVirtualMachine.html"""

    virtualmachineid: str = Field(..., alias="virtualMachineId", description="ID of the VM to be moved")

    account: Optional[str] = Field(None, description="Account name of the new VM owner")
    domainid: Optional[str] = Field(None, alias="domainId", description="Domain ID of the new VM owner")
    networkids: Optional[list[str]] = Field(
        None,
        alias="networkIds",
        description=(
            "Network IDs the moved VM will participate in. "
            "Defaults to the new account's default network if omitted."
        ),
    )
    projectid: Optional[str] = Field(
        None,
        alias="projectId",
        description="Project for the new VM owner (alternative to account/domainid)",
    )
    securitygroupids: Optional[list[str]] = Field(
        None,
        alias="securityGroupIds",
        description=(
            "Security group IDs to apply. "
            "Defaults to the new account's default security group if omitted."
        ),
    )

    @field_serializer("networkids", "securitygroupids")
    def serialize_csv(self, value: list[str] | None) -> str | None:
        if value is None:
            return None
        return ",".join(value)

    @model_validator(mode="after")
    def validate_owner(self) -> AssignVirtualMachineRequest:
        errors = []
        if self.account and not self.domainid:
            errors.append("domainid is required when account is provided")
        if self.projectid and (self.account or self.domainid):
            errors.append("projectid is mutually exclusive with account/domainid")
        if errors:
            raise ValueError(errors)
        return self


class AssignVirtualMachineToBackupOfferingRequest(APIRequest):
    """Reference: https://cloudstack.apache.org/api/apidocs-4.22/apis/assignVirtualMachineToBackupOffering.html"""

    virtualmachineid: str = Field(..., alias="virtualMachineId", description="ID of the virtual machine")
    backupofferingid: str = Field(..., alias="backupOfferingId", description="ID of the backup offering")


class CleanVMReservationsRequest(APIRequest):
    """Reference: https://cloudstack.apache.org/api/apidocs-4.22/apis/cleanVMReservations.html"""

    pass


class CreateVMScheduleRequest(APIRequest):
    """Reference: https://cloudstack.apache.org/api/apidocs-4.22/apis/createVMSchedule.html"""

    virtualmachineid: str = Field(..., alias="virtualMachineId", description="ID of the VM for which schedule is to be defined")
    schedule: str = Field(
        ...,
        description="Schedule for action on VM in cron format. e.g. '0 15 10 * *' for 'at 15:00 on 10th day of every month'",
    )
    timezone: str = Field(  # Required per docs
        ...,
        description="Timezone for this schedule (see CloudStack Time Zone Format)",
    )
    action: str = Field(
        ...,
        description="Action to take on the VM: start, stop, reboot, force_stop, force_reboot",
    )
    description: Optional[str] = Field(None, description="Description of the schedule")
    enabled: Optional[bool] = Field(None, description="Enable VM schedule. Defaults to true")
    startdate: Optional[str] = Field(
        None,
        alias="startDate",
        description='Start date from which the schedule becomes active. Use format "yyyy-MM-dd hh:mm:ss"',
    )
    enddate: Optional[str] = Field(
        None,
        alias="endDate",
        description='End date after which the schedule becomes inactive. Use format "yyyy-MM-dd hh:mm:ss"',
    )


class DeleteVMScheduleRequest(APIRequest):
    """Reference: https://cloudstack.apache.org/api/apidocs-4.22/apis/deleteVMSchedule.html"""

    virtualmachineid: str = Field(..., alias="virtualMachineId", description="ID of the virtual machine")
    id: Optional[str] = Field(None, description="ID of the VM schedule to delete. Mutually exclusive with ids.")
    ids: Optional[List[str]] = Field(
        None,
        description="IDs of VM schedules to delete. Mutually exclusive with id.",
    )

    @model_validator(mode="after")
    def check_id_mutex(self) -> "DeleteVMScheduleRequest":
        if self.id is None and self.ids is None:
            raise ValueError("At least one of 'id' or 'ids' must be provided.")
        if self.id is not None and self.ids is not None:
            raise ValueError("'id' and 'ids' are mutually exclusive.")
        return self

    @field_serializer("ids")
    def serialize_csv(self, value: list[str] | None) -> str | None:
        if value is None:
            return None
        return ",".join(value)


class DeployVirtualMachineRequest(APIRequest):
    """Reference: https://cloudstack.apache.org/api/apidocs-4.22/apis/deployVirtualMachine.html
    CloudStack deployVirtualMachine (4.22).
 
    Exactly ONE of the following source groups must be supplied:
      • template_based  → templateid  (non-ISO template)
      • iso_based       → templateid  (ISO) + diskofferingid
      • volume_based    → volumeid
      • snapshot_based  → snapshotid
    """

    # --- required -----------------------------------------------------------
    serviceofferingid: str = Field(..., alias="serviceOfferingId", description="ID of the service offering")
    zoneid: str = Field(..., alias="zoneId", description="Availability zone for the virtual machine")

    # --- deployment source (at least one required — validated below) --------
    templateid: Optional[str] = Field(None, alias="templateId", description="Template or ISO UUID. Mutually exclusive with snapshotid/volumeid.")
    volumeid: Optional[str] = Field(None, alias="volumeId", description="Existing volume UUID (volume-based deploy). Mutually exclusive with templateid/snapshotid.")
    snapshotid: Optional[str] = Field(
        None,
        alias="snapshotId",
        description="Snapshot UUID (snapshot-based deploy). Mutually exclusive with templateid/volumeid.",
    )
    name: Optional[str] = Field(None, description="Host name for the virtual machine")
    displayname: Optional[str] = Field(None, alias="displayName", description="User generated display name")
    customid: Optional[str] = Field(None, alias="customId", description="Custom ID (root admin only)")

    # --- account / domain / project -----------------------------------------
    account: Optional[str] = Field(None, description="Account for the VM (requires domainid)")
    domainid: Optional[str] = Field(None, alias="domainId", description="Domain ID (required when account is set)")
    projectid: Optional[str] = Field(None, alias="projectId", description="Deploy VM under this project")

    # --- network ------------------------------------------------------------
    networkids: Optional[list[str]] = Field(
        None,
        alias="networkIds",
        description="Network IDs to attach (CSV serialized, mutually exclusive with iptonetworklist)",
    )
    iptonetworklist: Optional[List[IpToNetworkEntry]] = Field(
        None,
        alias="ipToNetworkList",
        description=(
            "IP-to-network mappings for static IP assignment. "
            "Each item is a dict with keys 'networkid' and 'ip' (mutually exclusive with networkids)."
        ),
    )
    ipaddress: Optional[str] = Field(None, alias="ipAddress", description="Static IPv4 for the default network")
    ip6address: Optional[str] = Field(None, alias="ip6Address", description="Static IPv6 for the default network")
    macaddress: Optional[str] = Field(None, alias="macAddress", description="MAC address for the default network")

    # --- affinity groups ----------------------------------------------------
    affinitygroupids: Optional[list[str]] = Field(
        None,
        alias="affinityGroupIds",
        description="Affinity group IDs (mutually exclusive with affinitygroupnames)",
    )
    affinitygroupnames: Optional[list[str]] = Field(
        None,
        alias="affinityGroupNames",
        description="Affinity group names (mutually exclusive with affinitygroupids)",
    )

    # --- security groups ----------------------------------------------------
    securitygroupids: Optional[list[str]] = Field(
        None,
        alias="securityGroupIds",
        description="Security group IDs (mutually exclusive with securitygroupnames)",
    )
    securitygroupnames: Optional[list[str]] = Field(
        None,
        alias="securityGroupNames",
        description="Security group names (mutually exclusive with securitygroupids)",
    )

    # --- disk ---------------------------------------------------------------
    diskofferingid: Optional[str] = Field(None, alias="diskOfferingId", description="Disk offering ID")
    overridediskofferingid: Optional[str] = Field(
        None,
        alias="overrideDiskOfferingId",
        description="Override root disk offering (takes precedence for ISO deploys)",
    )
    rootdisksize: Optional[int] = Field(None, alias="rootDiskSize", description="Root disk size in GB (template-based deploys only)")
    size: Optional[int] = Field(None, description="Data disk size in GB (mutually exclusive with diskofferingid)")
    datadiskofferinglist: Optional[list[str]] = Field(
        None,
        alias="dataDiskOfferingList",
        description="Data disk offering IDs (mutually exclusive with diskofferingid)",
    )
    datadisksdetails: Optional[list[DataDiskDetail]] = Field(
        None,
        alias="dataDiskDetails",
        description="Data disk details e.g. diskofferingid, size, miniops, maxiops per disk",
    )

    # --- user data ----------------------------------------------------------
    userdata: Optional[str] = Field(None, description="Base64-encoded user data (max 4KB via GET, 1MB via POST)")
    userdataid: Optional[str] = Field(None, alias="userDataId", description="ID of pre-registered userdata")
    userdatadetails: Optional[UserDataDetail] = Field(
        None,
        alias="userDataDetails",
        description="Variable values for userdata template variables",
    )

    # --- ssh key pairs ------------------------------------------------------
    keypair: Optional[str] = Field(None, alias="keyPair", description="SSH key pair name")
    keypairs: Optional[list[str]] = Field(None, alias="keyPairs", description="Multiple SSH key pair names (CSV serialized)")

    # --- boot options -------------------------------------------------------
    startvm: Optional[bool] = Field(None, alias="startVm", description="Start VM after deploy (default: True)")
    boottype: Optional[BootType] = Field(None, alias="bootType", description="Boot type (BIOS or UEFI)")
    bootmode: Optional[BootMode] = Field(None, alias="bootMode", description="Boot mode: Legacy or Secure (UEFI only)")
    bootintosetup: Optional[bool] = Field(None, alias="bootIntoSetup", description="Boot into hardware setup (VMware only)")

    # --- placement ----------------------------------------------------------
    hostid: Optional[str] = Field(None, alias="hostId", description="Target host ID (root admin only)")
    clusterid: Optional[str] = Field(None, alias="clusterId", description="Target cluster ID (root admin only)")
    podid: Optional[str] = Field(None, alias="podId", description="Target pod ID (root admin only)")
    deploymentplanner: Optional[str] = Field(None, alias="deploymentPlanner", description="Deployment planner (root admin only)")
    hypervisor: Optional[str] = Field(None, description="Hypervisor type (required if not set on template/ISO)")

    # --- advanced / misc ----------------------------------------------------
    group: Optional[str] = Field(None, description="VM group name")
    displayvm: Optional[bool] = Field(None, alias="displayVm", description="Display VM to end user (default: True)")
    copyimagetags: Optional[bool] = Field(None, alias="copyImageTags", description="Copy image tags to VM (default: False)")
    dynamicscalingenabled: Optional[bool] = Field(None, alias="dynamicScalingEnabled", description="Enable dynamic CPU/memory scaling")
    iothreadsenabled: Optional[bool] = Field(None, alias="ioThreadsEnabled", description="Enable IO threads for disk devices")
    iodriverpolicy: Optional[IODriverPolicy] = Field(None, alias="ioDriverPolicy", description="IO driver policy")
    nicmultiqueuenumber: Optional[int] = Field(None, alias="nicMultiQueueNumber", description="Number of queues for multiqueue NICs")
    nicpackedvirtqueuesenabled: Optional[bool] = Field(None, alias="nicPackedVirtQueuesEnabled", description="Enable packed virtqueues")
    keyboard: Optional[KeyboardType] = Field(None, description="Keyboard layout type")
    extraconfig: Optional[str] = Field(None, alias="extraConfig", description="URL-encoded extra config (passed on successful deploy)")
    leaseduration: Optional[int] = Field(None, alias="leaseDuration", description="Lease duration in days")
    leaseexpiryaction: Optional[LeaseExpiryAction] = Field(None, alias="leaseExpiryAction", description="Action on lease expiry")
    password: Optional[str] = Field(None, description="VM password (random if not set)")

    # --- vmware specific ----------------------------------------------------
    nicnetworklist: Optional[list[NicNetworkEntry]] = Field(
        None,
        alias="nicNetworkList",
        description="VMware vApp: NIC-to-network mapping for 'as-is' import",
    )
    dhcpoptionsnetworklist: Optional[list[DhcpOptionNetworkEntry]] = Field(
        None,
        alias="dhcpOptionsNetworkList",
        description="Per-network DHCP option overrides",
    )
    properties: Optional[dict[str, str]] = Field(None, description="vApp properties (VMware)")

    # --- extra details -------------------------------------------------------
    details: Optional[dict[str, str]] = Field(
        None,
        description="Custom key/value parameters. The 'extraconfig' key is not allowed here.",
    )
    externaldetails: Optional[dict[str, str]] = Field(
        None,
        alias="externalDetails",
        description="External system details (hypervisor-specific)",
    )

    # --- serializers --------------------------------------------------------
    @field_serializer(
        "networkids",
        "keypairs",
        "affinitygroupids",
        "affinitygroupnames",
        "securitygroupids",
        "securitygroupnames",
        "datadiskofferinglist",
    )
    def serialize_csv(self, value: list[str] | None) -> str | None:
        if value is None:
            return None
        return ",".join(value)

    def model_dump(self, *args, **kwargs) -> Dict[str, Any]:
        data = super().model_dump(*args, **kwargs)
        return self._flatten_cloudstack_list_dicts(data)

    @field_serializer("userdatadetails")
    def serialize_userdata_details(
        self, value: list[UserDataDetail] | None
    ) -> dict[str, str] | None:
        if not value:
            return None
        return {
            k: v
            for i, entry in enumerate(value)
            for k, v in {
                f"userdatadetails[{i}].key": entry.key,
                f"userdatadetails[{i}].value": entry.value,
            }.items()
        }

    def _flatten_cloudstack_list_dicts(self, data: Dict[str, Any]) -> Dict[str, Any]:
        indexed_keys = {"iptonetworklist", "datadisksdetails", "nicnetworklist", "dhcpoptionsnetworklist"}
        flattened: Dict[str, Any] = {}
        for key, value in data.items():
            if key in indexed_keys and isinstance(value, list):
                for idx, item in enumerate(value):
                    if isinstance(item, dict):
                        for subk, subv in item.items():
                            flattened[f"{key}[{idx}].{subk}"] = subv
                    else:
                        flattened[f"{key}[{idx}]"] = item
            else:
                flattened[key] = value
        return flattened

    # --- validators ---------------------------------------------------------
    @model_validator(mode="after")
    def validate_deployment_source(self) -> DeployVirtualMachineRequest:
        sources = [s for s in (self.templateid, self.volumeid, self.snapshotid) if s is not None]
        if len(sources) == 0:
            raise ValueError("At least one deployment source is required: templateid, volumeid, or snapshotid.")
        if len(sources) > 1:
            raise ValueError("Only one deployment source allowed: templateid, volumeid, or snapshotid.")
        return self

    @model_validator(mode="after")
    def validate_mutual_exclusions(self) -> DeployVirtualMachineRequest:
        errors = []
        if self.networkids and self.iptonetworklist:
            errors.append("networkids and iptonetworklist are mutually exclusive")
        if self.affinitygroupids and self.affinitygroupnames:
            errors.append("affinitygroupids and affinitygroupnames are mutually exclusive")
        if self.securitygroupids and self.securitygroupnames:
            errors.append("securitygroupids and securitygroupnames are mutually exclusive")
        if self.diskofferingid and self.size:
            errors.append("diskofferingid and size are mutually exclusive")
        if self.diskofferingid and self.datadisksdetails:
            errors.append("diskofferingid and datadisksdetails are mutually exclusive")
        if self.account and not self.domainid:
            errors.append("domainid is required when account is provided")
        if self.bootmode and self.boottype != BootType.UEFI:
            errors.append("bootmode is only valid when boottype=UEFI")
        if errors:
            raise ValueError(errors)
        return self

    @field_validator("macaddress")
    @classmethod
    def validate_mac(cls, v: str | None) -> str | None:
        if v and not re.match(r"^([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$", v):
            raise ValueError(f"Invalid MAC address format: {v!r}")
        return v


# ---------------------------------------------------------------------------
# Deploy factory subclasses — convenient typed entry points
# ---------------------------------------------------------------------------

class DeployFromTemplate(DeployVirtualMachineRequest):
    """Deploy VM from a regular (non-ISO) template. templateid is required."""
    templateid: str = Field(..., alias="templateId", description="Non-ISO template UUID")  # type: ignore[assignment]


class DeployFromISO(DeployVirtualMachineRequest):
    """Deploy VM from an ISO image. templateid (ISO UUID) and diskofferingid are required."""
    templateid: str = Field(..., alias="templateId", description="ISO UUID")  # type: ignore[assignment]
    diskofferingid: str = Field(..., alias="diskOfferingId", description="Root disk offering for ISO deploy")  # type: ignore[assignment]


class DeployFromVolume(DeployVirtualMachineRequest):
    """Deploy VM by attaching an existing volume as root. volumeid is required."""
    volumeid: str = Field(..., alias="volumeId", description="Existing volume UUID")  # type: ignore[assignment]


class DeployFromSnapshot(DeployVirtualMachineRequest):
    """Deploy VM from a disk snapshot. snapshotid is required."""
    snapshotid: str = Field(..., alias="snapshotId", description="Snapshot UUID")  # type: ignore[assignment]


class DestroyVirtualMachineRequest(APIRequest):
    """Reference: https://cloudstack.apache.org/api/apidocs-4.22/apis/destroyVirtualMachine.html"""

    id: str = Field(..., description="ID of the virtual machine to destroy")
    expunge: Optional[bool] = Field(
        None,
        description="If true, the VM is expunged immediately. False by default.",
    )
    volumeids: Optional[List[str]] = Field(
        None,
        alias="volumeIds",
        description="Comma-separated list of volume UUIDs to destroy along with the VM",
    )

    @field_serializer("volumeids")
    def serialize_csv(self, value: list[str] | None) -> str | None:
        if value is None:
            return None
        return ",".join(value)


class ExpungeVirtualMachineRequest(APIRequest):
    """Reference: https://cloudstack.apache.org/api/apidocs-4.22/apis/expungeVirtualMachine.html"""

    id: str = Field(..., description="ID of the virtual machine to expunge")


class GetVMPasswordRequest(APIRequest):
    """Reference: https://cloudstack.apache.org/api/apidocs-4.22/apis/getVMPassword.html"""

    id: str = Field(..., description="ID of the virtual machine")


class GetVMUserdataRequest(APIRequest):
    """Reference: https://cloudstack.apache.org/api/apidocs-4.22/apis/getVirtualMachineUserData.html"""

    virtualmachineid: str = Field(..., alias="virtualMachineId", description="ID of the virtual machine")


class ImportUnmanagedInstanceRequest(APIRequest):
    """Reference: https://cloudstack.apache.org/api/apidocs-4.22/apis/importUnmanagedInstance.html"""

    # --- required -----------------------------------------------------------
    clusterid: str = Field(..., alias="clusterId", description="The cluster ID")
    name: str = Field(..., description="The name of the instance as it is known to the hypervisor")
    serviceofferingid: str = Field(..., alias="serviceOfferingId", description="The service offering for the virtual machine")

    # --- optional -----------------------------------------------------------
    account: Optional[str] = Field(None, description="An optional account for the virtual machine. Must be used with domainid.")
    datadiskofferinglist: Optional[list[str]] = Field(
        None,
        alias="dataDiskOfferingList",
        description="Datadisk template to disk-offering mapping using keys disk and diskOffering",
    )
    details: Optional[dict[str, str]] = Field(None, description="Custom parameters")
    displayname: Optional[str] = Field(None, alias="displayName", description="The display name of the instance")
    domainid: Optional[str] = Field(None, alias="domainId", description="Import instance to the domain specified")
    forced: Optional[bool] = Field(
        None,
        description="VM is imported despite some NIC MAC addresses already present; a new MAC is generated if needed",
    )
    hostname: Optional[str] = Field(None, alias="hostName", description="The host name of the instance")
    migrateallowed: Optional[bool] = Field(
        None,
        alias="migrateAllowed",
        description="VM and its volumes are allowed to migrate to a different host/pool when offerings are incompatible",
    )
    nicipaddresslist: Optional[list[dict[str, str]]] = Field(
        None,
        alias="nicIpAddressList",
        description="VM NIC to IP address mapping using keys nic, ip4Address",
    )
    nicnetworklist: Optional[list[NicNetworkEntry]] = Field(
        None,
        alias="nicNetworkList",
        description="VM NIC to network ID mapping using keys nic and network",
    )
    projectid: Optional[str] = Field(None, alias="projectId", description="Import instance for the project")
    templateid: Optional[str] = Field(None, alias="templateId", description="The ID of the template for the virtual machine")

    def model_dump(self, *args, **kwargs) -> Dict[str, Any]:
        data = super().model_dump(*args, **kwargs)
        return self._flatten_cloudstack_list_dicts(data)

    def _flatten_cloudstack_list_dicts(self, data: Dict[str, Any]) -> Dict[str, Any]:
        flattened: Dict[str, Any] = {}
        for key, value in data.items():
            if key in {"nicipaddresslist", "nicnetworklist"} and isinstance(value, list):
                for idx, item in enumerate(value):
                    if isinstance(item, dict):
                        for subk, subv in item.items():
                            flattened[f"{key}[{idx}].{subk}"] = subv
                    else:
                        flattened[f"{key}[{idx}]"] = item
            else:
                flattened[key] = value
        return flattened


class ImportVmRequest(APIRequest):
    """Reference: https://cloudstack.apache.org/api/apidocs-4.22/apis/importVm.html"""

    # --- required -----------------------------------------------------------
    clusterid: str = Field(..., alias="clusterId", description="The cluster ID")
    hypervisor: str = Field(..., description="Hypervisor type of the host")
    importsource: str = Field(..., alias="importSource", description="Source location for import")
    name: str = Field(..., description="The name of the instance as it is known to the hypervisor")
    serviceofferingid: str = Field(..., alias="serviceOfferingId", description="The service offering for the virtual machine")
    zoneid: str = Field(..., alias="zoneId", description="The zone ID")

    # --- optional -----------------------------------------------------------
    account: Optional[str] = Field(None, description="An optional account for the virtual machine. Must be used with domainId.")
    clustername: Optional[str] = Field(None, alias="clusterName", description="VMware cluster name (only for VMware to KVM imports)")
    convertinstancehostid: Optional[str] = Field(None, alias="convertInstanceHostId", description="Host to perform virt-v2v conversion from VMware to KVM")
    convertinstancepoolid: Optional[str] = Field(None, alias="convertInstancePoolId", description="Temporary storage pool for virt-v2v migration from VMware to KVM")
    datacentername: Optional[str] = Field(None, alias="dataCenterName", description="VMware datacenter name (only for VMware to KVM imports)")
    datadiskofferinglist: Optional[list[str]] = Field(None, alias="dataDiskOfferingList", description="Datadisk template to disk-offering mapping")
    details: Optional[dict[str, str]] = Field(None, description="Custom parameters specification")
    diskpath: Optional[str] = Field(None, alias="diskPath", description="Path of the disk image")
    displayname: Optional[str] = Field(None, alias="displayName", description="Display name of the instance")
    domainid: Optional[str] = Field(None, alias="domainId", description="Domain ID for instance import")
    existingvcenterid: Optional[str] = Field(None, alias="existingVcenterId", description="UUID of linked existing vCenter (VMware to KVM imports)")
    extraparams: Optional[str] = Field(None, alias="extraParams", description="Extra parameters for virt-v2v command (VMware to KVM imports)")
    forceconverttopool: Optional[bool] = Field(None, alias="forceConvertToPool", description="Force virt-v2v conversions to write directly to storage pool")
    forced: Optional[bool] = Field(None, description="Import VM despite duplicate MAC addresses; generates new MAC if needed")
    forcemstoimportvmfiles: Optional[bool] = Field(None, alias="forceMsToImportVmFiles", description="Force MS to export OVF from VMware to temporary storage")
    host: Optional[str] = Field(None, description="Host name or IP address")
    hostid: Optional[str] = Field(None, alias="hostId", description="Host where local disk is located")
    hostip: Optional[str] = Field(None, alias="hostIp", description="VMware ESXi host IP/Name (VMware to KVM imports)")
    hostname: Optional[str] = Field(None, alias="hostName", description="Host name of the instance")
    importinstancehostid: Optional[str] = Field(None, alias="importInstanceHostId", description="Host to import converted instance from VMware to KVM")
    migrateallowed: Optional[bool] = Field(None, alias="migrateAllowed", description="Allow VM and volumes to migrate to different host/pool for incompatible offerings")
    networkid: Optional[str] = Field(None, alias="networkId", description="The network ID")
    nicipaddresslist: Optional[list[dict[str, str]]] = Field(None, alias="nicIpAddressList", description="VM NIC to IP address mapping using keys nic, ip4Address")
    nicnetworklist: Optional[list[NicNetworkEntry]] = Field(None, alias="nicNetworkList", description="VM NIC to network ID mapping using keys nic and network")
    password: Optional[str] = Field(None, description="Password for the host")
    projectid: Optional[str] = Field(None, alias="projectId", description="Project ID for instance import")
    storageid: Optional[str] = Field(None, alias="storageId", description="Shared storage pool where disk is located")
    templateid: Optional[str] = Field(None, alias="templateId", description="Template ID for the virtual machine")
    temppath: Optional[str] = Field(None, alias="tempPath", description="Temp path on external host for disk image copy")
    username: Optional[str] = Field(None, alias="userName", description="Username for the host")
    vcenter: Optional[str] = Field(None, description="vCenter name/IP; use IP or FQDN for host running vCenter server")

    def model_dump(self, *args, **kwargs) -> Dict[str, Any]:
        data = super().model_dump(*args, **kwargs)
        return self._flatten_cloudstack_list_dicts(data)

    def _flatten_cloudstack_list_dicts(self, data: Dict[str, Any]) -> Dict[str, Any]:
        flattened: Dict[str, Any] = {}
        for key, value in data.items():
            if key in {"nicipaddresslist", "nicnetworklist", "datadiskofferinglist"} and isinstance(value, list):
                for idx, item in enumerate(value):
                    if isinstance(item, dict):
                        for subk, subv in item.items():
                            flattened[f"{key}[{idx}].{subk}"] = subv
                    else:
                        flattened[f"{key}[{idx}]"] = item
            else:
                flattened[key] = value
        return flattened


class ListUnmanagedInstancesRequest(APIRequest, PaginationMixin):
    """Reference: https://cloudstack.apache.org/api/apidocs-4.22/apis/listUnmanagedInstances.html"""

    clusterid: str = Field(..., alias="clusterId", description="The cluster ID")
    keyword: Optional[str] = Field(None, description="List by keyword")
    name: Optional[str] = Field(None, description="The hypervisor name of the instance")


class ListVirtualMachinesRequest(APIRequest, PaginationMixin):
    """Reference: https://cloudstack.apache.org/api/apidocs-4.22/apis/listVirtualMachines.html"""

    account: Optional[str] = Field(None, description="List resources by account. Must be used with domainid.")
    accumulate: Optional[bool] = Field(None, description="Accumulates VM metrics data instead of returning only the most recent data collected.")
    affinitygroupid: Optional[str] = Field(None, alias="affinityGroupId", description="List VMs by affinity group")
    arch: Optional[str] = Field(None, description="CPU architecture of the VM")
    autoscalevmgroupid: Optional[str] = Field(None, alias="autoScaleVmGroupId", description="The ID of AutoScaling VM Group")
    backupofferingid: Optional[str] = Field(None, alias="backupOfferingId", description="List by the backup offering")
    clusterid: Optional[str] = Field(None, alias="clusterId", description="The cluster ID")
    details: Optional[str] = Field(
        None,
        description="Comma-separated list of VM details requested (e.g. all, group, nics, stats, secgrp, tmpl, servoff, diskoff, backoff, iso, volume, min, affgrp)",
    )
    displayvm: Optional[bool] = Field(None, alias="displayVm", description="List resources by display flag; only ROOT admin may use this")
    domainid: Optional[str] = Field(None, alias="domainId", description="List only resources belonging to this domain")
    extensionid: Optional[str] = Field(None, alias="extensionId", description="The ID of the Orchestrator extension for the VM")
    forvirtualnetwork: Optional[bool] = Field(None, alias="forVirtualNetwork", description="List by network type; true for virtual network VMs")
    gpuenabled: Optional[bool] = Field(None, alias="gpuEnabled", description="Filter VMs by GPU support")
    groupid: Optional[str] = Field(None, alias="groupId", description="The group ID")
    haenable: Optional[bool] = Field(None, alias="haEnable", description="Filter by HA offering; true for HA-enabled VMs")
    hostid: Optional[str] = Field(None, alias="hostId", description="The host ID")
    hypervisor: Optional[str] = Field(None, description="Filter by hypervisor type")
    id: Optional[str] = Field(None, description="The ID of the virtual machine. Mutually exclusive with ids.")
    ids: Optional[list[str]] = Field(None, description="The IDs of the virtual machines. Mutually exclusive with id.")
    isoid: Optional[str] = Field(None, alias="isoId", description="List VMs by ISO")
    isrecursive: Optional[bool] = Field(None, alias="isRecursive", description="If true, lists all resources from the parent domain down to leaves")
    isvnf: Optional[bool] = Field(None, alias="isVnf", description="Flag to list VMs created from VNF templates")
    keypair: Optional[str] = Field(None, alias="keyPair", description="List VMs by SSH keypair name")
    keyword: Optional[str] = Field(None, description="Search keyword")
    leased: Optional[bool] = Field(None, description="Return only leased instances")
    listall: Optional[bool] = Field(None, alias="listAll", description="If true, list all resources the caller is authorized to see")
    name: Optional[str] = Field(None, description="Name of the virtual machine (substring match)")
    networkid: Optional[str] = Field(None, alias="networkId", description="List by network ID")
    podid: Optional[str] = Field(None, alias="podId", description="The pod ID")
    projectid: Optional[str] = Field(None, alias="projectId", description="List objects by project; -1 lists all VMs")
    retrieveonlyresourcecount: Optional[bool] = Field(None, alias="retrieveOnlyResourceCount", description="Response contains only the resource count")
    securitygroupid: Optional[str] = Field(None, alias="securityGroupId", description="The security group ID")
    serviceofferingid: Optional[str] = Field(None, alias="serviceOfferingId", description="Filter by service offering")
    showicon: Optional[bool] = Field(None, alias="showIcon", description="Display the resource icon for VMs")
    state: Optional[str] = Field(None, description="VM state: Running, Stopped, Present, Destroyed, Expunged")
    storageid: Optional[str] = Field(None, alias="storageId", description="Filter by storage ID where VM volumes belong")
    tags: Optional[str] = Field(None, description="List resources by tags (key/value pairs)")
    templateid: Optional[str] = Field(None, alias="templateId", description="List VMs by template")
    userdata: Optional[bool] = Field(None, description="Whether to return the VMs' user data")
    userdataid: Optional[str] = Field(None, alias="userDataId", description="Filter by userdata ID")
    userid: Optional[str] = Field(None, alias="userId", description="The user ID that created the VM")
    vpcid: Optional[str] = Field(None, alias="vpcId", description="List VMs by VPC")
    zoneid: Optional[str] = Field(None, alias="zoneId", description="The availability zone ID")

    @model_validator(mode="after")
    def check_id_mutex(self) -> "ListVirtualMachinesRequest":
        if self.id is not None and self.ids is not None:
            raise ValueError("'id' and 'ids' are mutually exclusive.")
        return self

    @field_serializer("ids")
    def serialize_csv(self, value: list[str] | None) -> str | None:
        if value is None:
            return None
        return ",".join(value)


class ListVirtualMachinesMetricsRequest(ListVirtualMachinesRequest):
    """Request parameters for ``listVirtualMachinesMetrics``.

    Identical parameters to listVirtualMachines.
    Reference: https://cloudstack.apache.org/api/apidocs-4.22/apis/listVirtualMachinesMetrics.html
    """

    pass


class ListVirtualMachinesUsageHistoryRequest(APIRequest, PaginationMixin):
    """Reference: https://cloudstack.apache.org/api/apidocs-4.22/apis/listVirtualMachinesUsageHistory.html"""

    enddate: Optional[str] = Field(None, alias="endDate", description="End date to filter stats. Use format 'yyyy-MM-dd hh:mm:ss'")
    id: Optional[str] = Field(None, description="The ID of the virtual machine. Mutually exclusive with ids.")
    ids: Optional[list[str]] = Field(None, description="The IDs of the virtual machines. Mutually exclusive with id.")
    keyword: Optional[str] = Field(None, description="List by keyword")
    name: Optional[str] = Field(None, description="Name of the VM (substring match)")
    startdate: Optional[str] = Field(None, alias="startDate", description="Start date to filter stats. Use format 'yyyy-MM-dd hh:mm:ss'")

    @model_validator(mode="after")
    def check_id_mutex(self) -> "ListVirtualMachinesUsageHistoryRequest":
        if self.id is not None and self.ids is not None:
            raise ValueError("'id' and 'ids' are mutually exclusive.")
        return self

    @field_serializer("ids")
    def serialize_csv(self, value: list[str] | None) -> str | None:
        if value is None:
            return None
        return ",".join(value)


class ListVMScheduleRequest(APIRequest, PaginationMixin):
    """Reference: https://cloudstack.apache.org/api/apidocs-4.22/apis/listVMSchedule.html"""

    virtualmachineid: str = Field(..., alias="virtualMachineId", description="ID of the VM for which schedule is defined")
    action: Optional[str] = Field(None, description="Action taken by schedule")
    enabled: Optional[bool] = Field(None, description="Filter by enabled state")
    id: Optional[str] = Field(None, description="ID of VM schedule")
    keyword: Optional[str] = Field(None, description="List by keyword")


class ListVmsForImportRequest(APIRequest, PaginationMixin):
    """Reference: https://cloudstack.apache.org/api/apidocs-4.22/apis/listVmsForImport.html"""

    host: str = Field(..., description="The host name or IP address")
    hypervisor: str = Field(..., description="Hypervisor type of the host")
    zoneid: str = Field(..., alias="zoneId", description="The zone ID")
    keyword: Optional[str] = Field(None, description="List by keyword")
    password: Optional[str] = Field(None, description="The password for the host")
    username: Optional[str] = Field(None, alias="userName", description="The username for the host")


class MigrateVirtualMachineRequest(APIRequest):
    """Reference: https://cloudstack.apache.org/api/apidocs-4.22/apis/migrateVirtualMachine.html"""

    virtualmachineid: str = Field(..., alias="virtualMachineId", description="The ID of the virtual machine")
    autoselect: Optional[bool] = Field(
        None,
        alias="autoSelect",
        description="Automatically select a destination host that does not require storage migration. False by default.",
    )
    hostid: Optional[str] = Field(None, alias="hostId", description="Destination Host ID to migrate VM to")
    storageid: Optional[str] = Field(
        None,
        alias="storageId",
        description="Destination storage pool ID to migrate VM volumes to. Required for migrating the root disk volume.",
    )


class MigrateVirtualMachineWithVolumeRequest(APIRequest):
    """Reference: https://cloudstack.apache.org/api/apidocs-4.22/apis/migrateVirtualMachineWithVolume.html"""

    virtualmachineid: str = Field(..., alias="virtualMachineId", description="The ID of the virtual machine")
    autoselect: Optional[bool] = Field(
        None,
        alias="autoSelect",
        description="Automatically select a destination host for a running instance. False by default.",
    )
    hostid: Optional[str] = Field(None, alias="hostId", description="Destination Host ID to migrate VM to")
    migrateto: Optional[list[MigrateToEntry]] = Field(
        None,
        alias="migrateTo",
        description="Volume-to-storage-pool mappings. Each entry specifies a volume UUID and destination pool UUID.",
    )

    def model_dump(self, *args, **kwargs) -> Dict[str, Any]:
        data = super().model_dump(*args, **kwargs)
        return self._flatten_migrateto(data)

    def _flatten_migrateto(self, data: Dict[str, Any]) -> Dict[str, Any]:
        flattened: Dict[str, Any] = {}
        for key, value in data.items():
            if key == "migrateto" and isinstance(value, list):
                for idx, item in enumerate(value):
                    if isinstance(item, dict):
                        for subk, subv in item.items():
                            flattened[f"migrateto[{idx}].{subk}"] = subv
            else:
                flattened[key] = value
        return flattened


class RebootVirtualMachineRequest(APIRequest):
    """Reference: https://cloudstack.apache.org/api/apidocs-4.22/apis/rebootVirtualMachine.html"""

    id: str = Field(..., description="ID of the virtual machine")
    bootintosetup: Optional[bool] = Field(None, alias="bootIntoSetup", description="Boot into hardware setup menu or not")
    forced: Optional[bool] = Field(None, description="Force reboot the VM (VM is Stopped and then Started)")


class RecoverVirtualMachineRequest(APIRequest):
    """Reference: https://cloudstack.apache.org/api/apidocs-4.22/apis/recoverVirtualMachine.html"""

    id: str = Field(..., description="ID of the virtual machine")


class RemoveNICFromVirtualMachineRequest(APIRequest):
    """Reference: https://cloudstack.apache.org/api/apidocs-4.22/apis/removeNicFromVirtualMachine.html"""

    virtualmachineid: str = Field(..., alias="virtualMachineId", description="ID of the virtual machine")
    nicid: str = Field(..., alias="nicId", description="ID of the NIC")


class RemoveVirtualMachineFromBackupOfferingRequest(APIRequest):
    """Reference: https://cloudstack.apache.org/api/apidocs-4.22/apis/removeVirtualMachineFromBackupOffering.html"""

    virtualmachineid: str = Field(..., alias="virtualMachineId", description="ID of the virtual machine")
    forced: Optional[bool] = Field(
        None,
        description="Whether to force remove VM from the backup offering (may also delete VM backups).",
    )


class ResetPasswordForVirtualMachineRequest(APIRequest):
    """Reference: https://cloudstack.apache.org/api/apidocs-4.22/apis/resetPasswordForVirtualMachine.html"""

    id: str = Field(..., description="ID of the virtual machine")
    password: Optional[str] = Field(
        None,
        description="The new password for the VM. If null, a random password will be generated.",
    )


class ResetSSHKeyForVirtualMachineRequest(APIRequest):
    """Reference: https://cloudstack.apache.org/api/apidocs-4.22/apis/resetSSHKeyForVirtualMachine.html"""

    id: str = Field(..., description="ID of the virtual machine")

    account: Optional[str] = Field(None, description="An optional account for the ssh key. Must be used with domainid.")
    domainid: Optional[str] = Field(None, alias="domainId", description="An optional domain ID. Required when account is provided.")
    keypair: Optional[str] = Field(None, alias="keyPair", description="Name of the SSH key pair")
    keypairs: Optional[list[str]] = Field(None, alias="keyPairs", description="Names of the SSH key pairs (CSV serialized)")
    projectid: Optional[str] = Field(None, alias="projectId", description="An optional project for the SSH key")

    @field_serializer("keypairs")
    def serialize_csv(self, value: list[str] | None) -> str | None:
        if value is None:
            return None
        return ",".join(value)

    @model_validator(mode="after")
    def validate_mutual_exclusions(self):
        if self.account and not self.domainid:
            raise ValueError("domainid is required when account is provided")
        return self


class ResetUserDataForVirtualMachineRequest(APIRequest):
    """Reference: https://cloudstack.apache.org/api/apidocs-4.22/apis/resetUserDataForVirtualMachine.html"""

    id: str = Field(..., description="The ID of the virtual machine")
    account: Optional[str] = Field(None, description="An optional account for the virtual machine. Must be used with domainid.")
    domainid: Optional[str] = Field(None, alias="domainId", description="An optional domain ID for the virtual machine.")
    projectid: Optional[str] = Field(None, alias="projectId", description="An optional project ID for the virtual machine.")
    userdata: Optional[str] = Field(None, description="Base64-encoded userdata content. Max 4KB via GET, 1MB via POST.")
    userdataid: Optional[str] = Field(None, alias="userDataId", description="ID of stored userdata")
    userdatadetails: Optional[list[UserDataDetail]] = Field(None, alias="userDataDetails", description="Variables and values used in userdata template")

    @model_validator(mode="after")
    def validate_mutual_exclusions(self):
        if self.account and not self.domainid:
            raise ValueError("domainid is required when account is provided")
        return self


class RestoreVirtualMachineRequest(APIRequest):
    """Reference: https://cloudstack.apache.org/api/apidocs-4.22/apis/restoreVirtualMachine.html"""

    virtualmachineid: str = Field(..., alias="virtualMachineId", description="ID of the VM to restore")

    templateid: Optional[str] = Field(
        None,
        alias="templateId",
        description="Template or ISO ID to restore from. Omit to restore from the VM's original template/ISO.",
    )
    diskofferingid: Optional[str] = Field(None, alias="diskOfferingId", description="Override the root volume's disk offering")
    rootdisksize: Optional[int] = Field(
        None,
        alias="rootDiskSize",
        description="Override root volume size in GB. Superseded by details['rootdisksize'] if both are provided.",
    )
    details: Optional[dict[str, str]] = Field(
        None,
        description="Custom key-value parameters e.g. {'rootdisksize': '100'}. Takes precedence over rootdisksize.",
    )
    expunge: Optional[bool] = Field(None, description="Expunge the old root volume after restore (default: False)")

    @model_validator(mode="after")
    def validate_disk_size(self) -> RestoreVirtualMachineRequest:
        if (
            self.rootdisksize is not None
            and self.details is not None
            and "rootdisksize" in self.details
        ):
            raise ValueError(
                "rootdisksize and details['rootdisksize'] are both set — "
                "details['rootdisksize'] will take precedence. Remove one to avoid ambiguity."
            )
        return self


class RevertToVMSnapshotRequest(APIRequest):
    """Reference: https://cloudstack.apache.org/api/apidocs-4.22/apis/revertToVMSnapshot.html"""

    vmsnapshotid: str = Field(..., alias="vmSnapshotId", description="The ID of the VM snapshot")


class ScaleVirtualMachineRequest(APIRequest):
    """Reference: https://cloudstack.apache.org/api/apidocs-4.22/apis/scaleVirtualMachine.html"""

    id: str = Field(..., description="The ID of the virtual machine")
    serviceofferingid: str = Field(..., alias="serviceOfferingId", description="The ID of the new service offering")

    automigrate: Optional[bool] = Field(
        None,
        alias="autoMigrate",
        description="Automatically migrate root volume when required to apply the new compute offering",
    )
    details: Optional[dict[str, str]] = Field(None, description="Custom parameters for cpuspeed, memory and cpunumber")
    maxiops: Optional[int] = Field(None, ge=0, alias="maxIops", description="New maximum IOPS for the custom disk offering")
    miniops: Optional[int] = Field(None, ge=0, alias="minIops", description="New minimum IOPS for the custom disk offering")
    shrinkok: Optional[bool] = Field(None, alias="shrinkOk", description="Verify OK to shrink the VM/root disk")


class StartVirtualMachineRequest(APIRequest):  # FIX: was BaseModel
    """Reference: https://cloudstack.apache.org/api/apidocs-4.22/apis/startVirtualMachine.html"""

    id: str = Field(..., description="The ID of the virtual machine")
    bootintosetup: Optional[bool] = Field(None, alias="bootIntoSetup", description="Boot into hardware setup menu or not")
    clusterid: Optional[str] = Field(None, alias="clusterId", description="Destination Cluster ID to deploy the VM to (ROOT admin only)")
    considerlasthost: Optional[bool] = Field(
        None,
        alias="considerLastHost",
        description="If true, CloudStack firstly tries to start the VM on the last host where it ran. Default: true.",
    )
    deploymentplanner: Optional[str] = Field(None, alias="deploymentPlanner", description="Deployment planner to use for VM allocation (ROOT admin only)")
    hostid: Optional[str] = Field(None, alias="hostId", description="Destination Host ID to deploy the VM to (ROOT admin only)")
    podid: Optional[str] = Field(None, alias="podId", description="Destination Pod ID to deploy the VM to (ROOT admin only)")


class StopVirtualMachineRequest(APIRequest):
    """Reference: https://cloudstack.apache.org/api/apidocs-4.22/apis/stopVirtualMachine.html"""

    id: str = Field(..., description="ID of the virtual machine")
    forced: Optional[bool] = Field(None, description="Force stop the VM (VM is marked as Stopped even if command fails to reach the backend)")


class UnmanageVirtualMachineRequest(APIRequest):
    """Reference: https://cloudstack.apache.org/api/apidocs-4.22/apis/unmanageVirtualMachine.html"""

    id: str = Field(..., description="The ID of the virtual machine to unmanage")
    forced: Optional[bool] = Field(None, description="Force unmanage with config drive. Applicable only for KVM Hypervisor.")
    hostid: Optional[str] = Field(
        None,
        alias="hostId",
        description="ID of the host used for unmanaging the Instance. Applicable only for KVM hypervisor and stopped Instances.",
    )


class UpdateDefaultNICForVirtualMachineRequest(APIRequest):
    """Reference: https://cloudstack.apache.org/api/apidocs-4.22/apis/updateDefaultNicForVirtualMachine.html"""

    nicid: str = Field(..., alias="nicId", description="NIC ID for the virtual machine")
    virtualmachineid: str = Field(..., alias="virtualMachineId", description="Virtual Machine ID")


class UpdateVirtualMachineRequest(APIRequest):
    """Reference: https://cloudstack.apache.org/api/apidocs-4.22/apis/updateVirtualMachine.html"""

    id: str = Field(..., description="ID of the virtual machine to update")

    # --- display / identity -------------------------------------------------
    name: Optional[str] = Field(None, description="New host name for the VM (requires stop/start to take effect)")
    displayname: Optional[str] = Field(None, alias="displayName", description="User-facing display name")
    displayvm: Optional[bool] = Field(None, alias="displayVm", description="Whether to display the VM to end users")
    group: Optional[str] = Field(None, description="Group name for the VM")
    instancename: Optional[str] = Field(None, alias="instanceName", description="Internal instance name (root admin only)")
    customid: Optional[str] = Field(None, alias="customId", description="Custom resource ID (root admin only)")
    ostypeid: Optional[str] = Field(None, alias="osTypeId", description="OS type ID that best represents this VM")

    # --- security groups ----------------------------------------------------
    securitygroupids: Optional[list[str]] = Field(
        None,
        alias="securityGroupIds",
        description="Security group IDs to apply (mutually exclusive with securitygroupnames)",
    )
    securitygroupnames: Optional[list[str]] = Field(
        None,
        alias="securityGroupNames",
        description="Security group names to apply (mutually exclusive with securitygroupids, Basic Network zones only)",
    )

    # --- user data ----------------------------------------------------------
    userdata: Optional[str] = Field(None, description="Base64-encoded user data. Max 4KB via GET, max 1MB via POST.")
    userdataid: Optional[str] = Field(None, alias="userDataId", description="ID of pre-registered userdata")
    userdatadetails: Optional[dict[str, str]] = Field(None, alias="userDataDetails", description="Variable values for userdata template variables")

    # --- details ------------------------------------------------------------
    details: Optional[dict[str, str]] = Field(
        None,
        description="Custom key-value parameters. 'extraconfig' key is not permitted here.",
    )
    cleanupdetails: Optional[bool] = Field(
        None,
        alias="cleanupDetails",
        description="If True, removes all existing details for this VM and ignores the details field.",
    )
    extraconfig: Optional[str] = Field(None, alias="extraConfig", description="URL-encoded extra config string passed to the VM on start")

    # --- DHCP options -------------------------------------------------------
    dhcpoptionsnetworklist: Optional[list[DhcpOptionNetworkEntry]] = Field(
        None,
        alias="dhcpOptionsNetworkList",
        description="DHCP options per network, passed to the VM on startup",
    )

    # --- HA / scaling -------------------------------------------------------
    haenable: Optional[bool] = Field(None, alias="haEnable", description="Enable or disable high availability for this VM")
    isdynamicallyscalable: Optional[bool] = Field(
        None,
        alias="isDynamicallyScalable",
        description="True if VM has XS/VMware tools for dynamic CPU/memory scaling.",
    )
    deleteprotection: Optional[bool] = Field(
        None,
        alias="deleteProtection",
        description="Protect the VM from deletion. Ignored if managed by autoscaling groups or CKS.",
    )

    # --- lease --------------------------------------------------------------
    leaseduration: Optional[int] = Field(
        None,
        alias="leaseDuration",
        description="Lease duration in days from now. Pass -1 to remove an existing lease.",
    )
    leaseexpiryaction: Optional[str] = Field(
        None,
        alias="leaseExpiryAction",
        description="Action on lease expiry: STOP or DESTROY",
    )

    # --- validators ---------------------------------------------------------
    @field_validator("leaseexpiryaction")
    @classmethod
    def validate_leaseexpiryaction(cls, v: str | None) -> str | None:
        if v is not None and v.upper() not in ("STOP", "DESTROY"):
            raise ValueError("leaseexpiryaction must be STOP or DESTROY")
        return v.upper() if v else v

    @field_validator("details")
    @classmethod
    def validate_details(cls, v: dict[str, str] | None) -> dict[str, str] | None:
        if v and "extraconfig" in v:
            raise ValueError(
                "'extraconfig' is not allowed inside details — use the extraconfig field directly"
            )
        return v

    @model_validator(mode="after")
    def validate_mutual_exclusions(self) -> UpdateVirtualMachineRequest:
        errors = []
        if self.securitygroupids and self.securitygroupnames:
            errors.append("securitygroupids and securitygroupnames are mutually exclusive")
        if self.cleanupdetails and self.details:
            errors.append("details is ignored when cleanupdetails=True — remove details or set cleanupdetails=False")
        if self.leaseduration is not None and self.leaseduration < -1:
            errors.append("leaseduration must be -1 (remove lease) or a positive number of days")
        if errors:
            raise ValueError(errors)
        return self

    # --- serializers --------------------------------------------------------
    @field_serializer("securitygroupids", "securitygroupnames")
    def serialize_csv(self, value: list[str] | None) -> str | None:
        if not value:
            return None
        return ",".join(value)

    @field_serializer("dhcpoptionsnetworklist")
    def serialize_dhcpoptionsnetworklist(
        self, value: list[DhcpOptionNetworkEntry] | None
    ) -> dict[str, str] | None:
        if not value:
            return None
        result = {}
        for i, entry in enumerate(value):
            result[f"dhcpoptionsnetworklist[{i}].networkid"] = entry.networkid
            for dhcp_key, dhcp_val in entry.options.items():
                result[f"dhcpoptionsnetworklist[{i}].{dhcp_key}"] = dhcp_val
        return result


class UpdateVMScheduleRequest(APIRequest):
    """Reference: https://cloudstack.apache.org/api/apidocs-4.22/apis/updateVMSchedule.html"""

    id: str = Field(..., description="ID of the virtual machine schedule to update")
    description: Optional[str] = Field(None, description="Name/description of the schedule")
    enabled: Optional[bool] = Field(None, description="Enable VM schedule")
    enddate: Optional[str] = Field(None, alias="endDate", description='End date after which schedule becomes inactive. Use format "yyyy-MM-dd hh:mm:ss"')
    schedule: Optional[str] = Field(None, description="Schedule in cron format. e.g. '0 15 10 * *'")  # FIX: was required
    startdate: Optional[str] = Field(None, alias="startDate", description='Start date from which schedule becomes active. Use format "yyyy-MM-dd hh:mm:ss"')
    timezone: Optional[str] = Field(None, description="Timezone for this schedule")
