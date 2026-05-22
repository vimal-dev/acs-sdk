from __future__ import annotations

from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, field_serializer, field_validator, model_validator

from .base import APIRequest, PaginationMixin


class UserDataDetail(BaseModel):
    key: str = Field(
        ...,
        description="Variable name declared in userdata",
    )

    value: str = Field(
        ...,
        description="Value for the userdata variable",
    )


class AssignVirtualMachineRequest(APIRequest):
    # -------------------------------------------------------------------------
    # REQUIRED
    # -------------------------------------------------------------------------
    virtualmachineid: str = Field(..., description="ID of the VM to be moved")

    # -------------------------------------------------------------------------
    # NEW OWNER
    # account and domainid go together; projectid is an alternative to account
    # -------------------------------------------------------------------------
    account: Optional[str] = Field(None, description="Account name of the new VM owner")
    domainid: Optional[str] = Field(None, description="Domain ID of the new VM owner")
    projectid: Optional[str] = Field(
        None,
        description="Project for the new VM owner (alternative to account/domainid)",
    )

    # -------------------------------------------------------------------------
    # NETWORK / SECURITY
    # If not provided, VM joins the default network/security group of the zone
    # -------------------------------------------------------------------------
    networkids: Optional[list[str]] = Field(
        None,
        description=(
            "Network IDs the moved VM will participate in. "
            "Defaults to the new account's default network if omitted."
        ),
    )
    securitygroupids: Optional[list[str]] = Field(
        None,
        description=(
            "Security group IDs to apply. "
            "Defaults to the new account's default security group if omitted."
        ),
    )

    # -------------------------------------------------------------------------
    # SERIALIZERS
    # -------------------------------------------------------------------------
    @field_serializer("networkids", "securitygroupids")
    def serialize_csv(self, value: list[str] | None) -> str | None:
        if value is None:
            return None
        return ",".join(value)

    # -------------------------------------------------------------------------
    # VALIDATORS
    # -------------------------------------------------------------------------
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


class ListVirtualMachinesRequest(APIRequest, PaginationMixin):
    # Filters
    id: Optional[str] = Field(None, description="List VM by ID")
    name: Optional[str] = Field(None, description="List VM by name")
    keyword: Optional[str] = Field(None, description="Search keyword")

    account: Optional[str] = Field(None, description="List VMs by account name")
    accountid: Optional[str] = Field(None, description="List VMs by account ID")

    domainid: Optional[str] = Field(None, description="Domain ID")
    isrecursive: Optional[bool] = Field(None, description="Include subdomains (used with domainid)")

    projectid: Optional[str] = Field(None, description="Project ID")

    zoneid: Optional[str] = Field(None, description="Zone ID")
    hostid: Optional[str] = Field(None, description="Host ID")

    clusterid: Optional[str] = Field(None, description="Cluster ID")
    podid: Optional[str] = Field(None, description="Pod ID")

    networkid: Optional[str] = Field(None, description="Network ID")
    vpcid: Optional[str] = Field(None, description="VPC ID")

    serviceofferingid: Optional[str] = Field(None, description="Filter by service offering")

    templateid: Optional[str] = Field(None, description="Template ID")
    isoid: Optional[str] = Field(None, description="ISO ID")

    state: Optional[str] = Field(None, description="VM state (Running, Stopped, Destroyed, etc.)")

    haenable: Optional[bool] = Field(None, description="Filter HA-enabled VMs")

    hypervisor: Optional[str] = Field(None, description="Filter by hypervisor type")

    tags: Optional[str] = Field(None, description="List VMs by tags (key/value pairs)")

    # Access / visibility
    listall: Optional[bool] = Field(None, description="List all VMs available to the caller")

    details: Optional[str] = Field(
        None,
        description="Comma-separated list of details (e.g., 'all', 'nics', 'stats')",
    )

    # Advanced filters
    forvirtualnetwork: Optional[bool] = Field(None, description="List VMs for virtual network")

    storageid: Optional[str] = Field(None, description="Filter by storage ID")


class ListVMScheduleRequest(APIRequest, PaginationMixin):
    virtualmachineid: str = Field(
        ...,
        alias="virtualMachineId",
        description="ID of the VM for which schedule is defined",
    )

    action: Optional[str] = Field(
        default=None,
        description="Action taken by schedule",
    )

    enabled: Optional[bool] = Field(
        default=None,
        description="Filter by enabled state",
    )

    id: Optional[str] = Field(
        default=None,
        description="ID of VM schedule",
    )

    keyword: Optional[str] = Field(
        default=None,
        description="List by keyword",
    )


class AddNICToVirtualMachineRequest(APIRequest):
    virtualmachineid: str = Field(..., description="ID of the virtual machine")
    networkid: str = Field(..., description="ID of the network to add the NIC to")
    dhcpoptions: Optional[str] = Field(
        None,
        description="DHCP options which are passed to the nic Example: dhcpoptions[0].dhcp:114=url&dhcpoptions[0].dhcp:66=www.test.com",
    )
    ipaddress: Optional[str] = Field(
        None,
        description="IP address for the new NIC. If not specified, an IP address will be automatically allocated from the specified network.",
    )
    macaddress: Optional[str] = Field(None, description="MAC address for the new NIC.")


class RemoveNICFromVirtualMachineRequest(APIRequest):
    virtualmachineid: str = Field(
        ..., alias="virtualMachineId", description="ID of the virtual machine"
    )
    nicid: str = Field(..., alias="nicId", description="ID of the NIC")


class AssignVirtualMachineToBackupOfferingRequest(APIRequest):
    virtualmachineid: str = Field(..., description="ID of the virtual machine")
    backupofferingid: str = Field(..., description="ID of the backup offering to assign the VM to")


class CreateVMScheduleRequest(APIRequest):
    virtualmachineid: str = Field(..., description="ID of the virtual machine")
    schedule: str = Field(
        ...,
        description="Schedule in cron format (e.g., '0 0 * * *' for daily at midnight)",
    )
    timezone: Optional[str] = Field(
        None, description="Timezone for the schedule (e.g., 'UTC', 'America/New_York')"
    )
    action: str = Field(
        ...,
        description="Action to perform (e.g., 'start', 'stop', 'reboot', 'force_stop', 'force_reboot')",
    )
    description: Optional[str] = Field(None, description="Optional description for the schedule")
    enabled: Optional[bool] = Field(
        None, description="Whether the schedule is enabled (default: True)"
    )
    startdate: Optional[str] = Field(
        None,
        description="Start date for the schedule in ISO 8601 format (e.g., '2024-01-01T00:00:00Z')",
    )
    enddate: Optional[str] = Field(
        None,
        description="End date for the schedule in ISO 8601 format (e.g., '2024-12-31T23:59:59Z')",
    )


class UpdateVMScheduleRequest(APIRequest):
    id: str = Field(..., description="ID of the virtual machine schedule to update")
    schedule: str = Field(
        ...,
        description="Schedule in cron format (e.g., '0 0 * * *' for daily at midnight)",
    )
    timezone: Optional[str] = Field(
        None, description="Timezone for the schedule (e.g., 'UTC', 'America/New_York')"
    )
    description: Optional[str] = Field(None, description="Optional description for the schedule")
    enabled: Optional[bool] = Field(
        None, description="Whether the schedule is enabled (default: True)"
    )
    startdate: Optional[str] = Field(
        None,
        description="Start date for the schedule in ISO 8601 format (e.g., '2024-01-01T00:00:00Z')",
    )
    enddate: Optional[str] = Field(
        None,
        description="End date for the schedule in ISO 8601 format (e.g., '2024-12-31T23:59:59Z')",
    )


class DeleteVMScheduleRequest(APIRequest):
    virtualmachineid: str = Field(..., description="ID of the virtual machine")
    id: str = Field(..., description="ID of the virtual machine schedule to update")
    ids: Optional[List[str]] = Field(
        None,
        description="List of IDs of the virtual machine schedules to delete (if multiple schedules need to be deleted)",
    )

    # -------------------------------------------------------------------------
    # SERIALIZERS — CSV fields
    # -------------------------------------------------------------------------
    @field_serializer("ids")
    def serialize_csv(self, value: list[str] | None) -> str | None:
        if value is None:
            return None
        return ",".join(value)


class DeployVirtualMachineRequest(APIRequest):
    # -------------------------------------------------------------------------
    # REQUIRED
    # -------------------------------------------------------------------------
    serviceofferingid: str = Field(..., description="ID of the service offering")
    zoneid: str = Field(..., description="Availability zone for the virtual machine")

    # -------------------------------------------------------------------------
    # IDENTITY
    # templateid is optional per docs — can deploy from snapshotid instead
    # -------------------------------------------------------------------------
    templateid: Optional[str] = Field(None, description="ID of the template")
    isoid: Optional[str] = Field(None, description="ID of the ISO (alternative to template)")
    snapshotid: Optional[str] = Field(
        None,
        description="ID of the snapshot to create the VM from (mutually exclusive with templateid)",
    )
    name: Optional[str] = Field(None, description="Host name for the virtual machine")
    displayname: Optional[str] = Field(None, description="User generated display name")
    customid: Optional[str] = Field(None, description="Custom ID (root admin only)")

    # -------------------------------------------------------------------------
    # ACCOUNT / DOMAIN / PROJECT
    # -------------------------------------------------------------------------
    account: Optional[str] = Field(None, description="Account for the VM (requires domainid)")
    domainid: Optional[str] = Field(None, description="Domain ID (required when account is set)")
    projectid: Optional[str] = Field(None, description="Deploy VM under this project")

    # -------------------------------------------------------------------------
    # NETWORK
    # networkids and iptonetworklist are mutually exclusive
    # -------------------------------------------------------------------------
    networkids: Optional[list[str]] = Field(
        None,
        description="Network IDs to attach (CSV serialized, mutually exclusive with iptonetworklist)",
    )
    iptonetworklist: Optional[List[Dict[str, str]]] = Field(
        None,
        description=(
            "List of IP-to-network mappings when assigning a static IP to a specific network. "
            "Each item is a dict with keys like 'networkid' and 'ip' (mutually exclusive with networkids)."
        ),
    )
    ipaddress: Optional[str] = Field(None, description="Static IPv4 for the default network")
    ip6address: Optional[str] = Field(None, description="Static IPv6 for the default network")
    macaddress: Optional[str] = Field(None, description="MAC address for the default network")

    # -------------------------------------------------------------------------
    # AFFINITY GROUPS (mutually exclusive)
    # -------------------------------------------------------------------------
    affinitygroupids: Optional[list[str]] = Field(
        None,
        description="Affinity group IDs (mutually exclusive with affinitygroupnames)",
    )
    affinitygroupnames: Optional[list[str]] = Field(
        None,
        description="Affinity group names (mutually exclusive with affinitygroupids)",
    )

    # -------------------------------------------------------------------------
    # SECURITY GROUPS (mutually exclusive, Basic Network zones only)
    # -------------------------------------------------------------------------
    securitygroupids: Optional[list[str]] = Field(
        None,
        description="Security group IDs (mutually exclusive with securitygroupnames)",
    )
    securitygroupnames: Optional[list[str]] = Field(
        None,
        description="Security group names (mutually exclusive with securitygroupids)",
    )

    # -------------------------------------------------------------------------
    # DISK
    # diskofferingid and datadisksdetails are mutually exclusive
    # size is mutually exclusive with diskofferingid
    # -------------------------------------------------------------------------
    diskofferingid: Optional[str] = Field(None, description="Disk offering ID")
    overridediskofferingid: Optional[str] = Field(
        None,
        description="Override root disk offering (takes precedence for ISO deploys)",
    )
    rootdisksize: Optional[int] = Field(
        None, description="Root disk size in GB (template-based deploys only)"
    )
    size: Optional[int] = Field(
        None,
        description="Data disk size in GB (mutually exclusive with diskofferingid)",
    )
    datadiskofferinglist: Optional[list[str]] = Field(
        None,
        description="Data disk offering IDs (mutually exclusive with diskofferingid)",
    )
    datadisksdetails: Optional[list[dict[str, str]]] = Field(
        None,
        description="Data disk details e.g. diskofferingid, size, miniops, maxiops per disk",
    )

    # -------------------------------------------------------------------------
    # USER DATA
    # -------------------------------------------------------------------------
    userdata: Optional[str] = Field(
        None, description="Base64-encoded user data (max 4KB via GET, 1MB via POST)"
    )
    userdataid: Optional[str] = Field(None, description="ID of pre-registered userdata")
    userdatadetails: Optional[UserDataDetail] = Field(
        None, description="Variable values for userdata template variables"
    )

    # -------------------------------------------------------------------------
    # SSH KEY PAIRS
    # -------------------------------------------------------------------------
    keypair: Optional[str] = Field(None, description="SSH key pair name")
    keypairs: Optional[list[str]] = Field(
        None, description="Multiple SSH key pair names (CSV serialized)"
    )

    # -------------------------------------------------------------------------
    # BOOT OPTIONS
    # bootintosetup is VMware only and ignored when startvm=False
    # -------------------------------------------------------------------------
    startvm: Optional[bool] = Field(None, description="Start VM after deploy (default: True)")
    boottype: Optional[str] = Field(None, description="Boot type: BIOS or UEFI")
    bootmode: Optional[str] = Field(None, description="Boot mode: Legacy or Secure (UEFI only)")
    bootintosetup: Optional[bool] = Field(
        None, description="Boot into hardware setup (VMware only)"
    )

    # -------------------------------------------------------------------------
    # PLACEMENT (root admin only)
    # -------------------------------------------------------------------------
    hostid: Optional[str] = Field(None, description="Target host ID (root admin only)")
    clusterid: Optional[str] = Field(None, description="Target cluster ID (root admin only)")
    podid: Optional[str] = Field(None, description="Target pod ID (root admin only)")
    deploymentplanner: Optional[str] = Field(
        None, description="Deployment planner (root admin only)"
    )
    hypervisor: Optional[str] = Field(
        None, description="Hypervisor type (required if not set on template/ISO)"
    )

    # -------------------------------------------------------------------------
    # ADVANCED / MISC
    # -------------------------------------------------------------------------
    group: Optional[str] = Field(None, description="VM group name")
    displayvm: Optional[bool] = Field(None, description="Display VM to end user (default: True)")
    copyimagetags: Optional[bool] = Field(
        None, description="Copy image tags to VM (default: False)"
    )
    dynamicscalingenabled: Optional[bool] = Field(
        None, description="Enable dynamic CPU/memory scaling"
    )
    iothreadsenabled: Optional[bool] = Field(None, description="Enable IO threads for disk devices")
    iodriverpolicy: Optional[str] = Field(
        None, description="IO driver policy: native, emulated, auto"
    )
    nicmultiqueuenumber: Optional[int] = Field(
        None, description="Number of queues for multiqueue NICs"
    )
    nicpackedvirtqueuesenabled: Optional[bool] = Field(None, description="Enable packed virtqueues")
    keyboard: Optional[str] = Field(
        None,
        description="Keyboard type: de, de-ch, es, fi, fr, fr-be, fr-ch, is, it, jp, nl-be, no, pt, uk, us",
    )
    extraconfig: Optional[str] = Field(
        None, description="URL-encoded extra config (passed on successful deploy)"
    )
    leaseduration: Optional[int] = Field(None, description="Lease duration in days")
    leaseexpiryaction: Optional[str] = Field(
        None, description="Lease expiry action: STOP or DESTROY"
    )
    password: Optional[str] = Field(None, description="VM password (random if not set)")

    # -------------------------------------------------------------------------
    # SERIALIZERS — CSV fields
    # -------------------------------------------------------------------------
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

    # -------------------------------------------------------------------------
    # REQUEST SERIALIZATION
    # -------------------------------------------------------------------------
    def model_dump(self, *args, **kwargs) -> Dict[str, Any]:
        """Dump the request to a CloudStack-compatible parameter dictionary."""
        data = super().model_dump(*args, **kwargs)
        return self._flatten_cloudstack_list_dicts(data)

    # -----------------------------------------------------------------------------
    # SERIALIZERS
    # query-string format: userdatadetails[0].key=...&userdatadetails[0].value=...
    # -----------------------------------------------------------------------------
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
        flattened: Dict[str, Any] = {}
        for key, value in data.items():
            if key in {"iptonetworklist", "datadisksdetails"} and isinstance(value, list):
                for idx, item in enumerate(value):
                    if isinstance(item, dict):
                        for subk, subv in item.items():
                            flattened[f"{key}[{idx}].{subk}"] = subv
                    else:
                        flattened[f"{key}[{idx}]"] = item
            else:
                flattened[key] = value
        return flattened

    # -------------------------------------------------------------------------
    # VALIDATORS
    # -------------------------------------------------------------------------
    @model_validator(mode="after")
    def validate_mutual_exclusions(self):
        errors = []

        if self.templateid and self.snapshotid:
            errors.append("templateid and snapshotid are mutually exclusive")

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

        if self.bootmode and not self.boottype:
            errors.append("boottype is required when bootmode is set")

        if errors:
            raise ValueError(errors)

        return self


class DestroyVirtualMachineRequest(APIRequest):
    id: str = Field(..., description="ID of the virtual machine to destroy")
    expunge: Optional[bool] = Field(
        None,
        description="Whether to expunge the VM immediately (default: False, which means the VM will be marked as destroyed but not expunged until the next cleanup cycle)",
    )
    volumeids: Optional[List[str]] = Field(
        None,
        description="List of volume IDs to destroy along with the VM (optional, only used if expunge is True)",
    )

    # -------------------------------------------------------------------------
    # SERIALIZERS — CSV fields
    # -------------------------------------------------------------------------
    @field_serializer("volumeids")
    def serialize_csv(self, value: list[str] | None) -> str | None:
        if value is None:
            return None
        return ",".join(value)


class CleanVMReservationsRequest(APIRequest):
    pass


class ExpungeVirtualMachineRequest(APIRequest):
    id: str = Field(..., description="ID of the virtual machine to expunge")


class GetVMPasswordRequest(APIRequest):
    id: str = Field(..., description="ID of the virtual machine")


class GetVMUserdataRequest(APIRequest):
    id: str = Field(..., description="ID of the virtual machine")


class RebootVirtualMachineRequest(APIRequest):
    id: str = Field(..., description="ID of the virtual machine")
    bootintosetup: Optional[bool] = Field(
        default=None,
        alias="bootInfoSetup",
        description="Boot into hardware setup menu or not",
    )
    forced: Optional[bool] = Field(
        None, description="Force reboot the VM (VM is Stopped and then Started)"
    )


class RecoverVirtualMachineRequest(APIRequest):
    id: str = Field(..., description="ID of the virtual machine")


class RemoveVirtualMachineFromBackupOfferingRequest(APIRequest):
    virtualmachineid: str = Field(..., description="ID of the virtual machine")
    forced: Optional[bool] = Field(
        None,
        description="Whether to force remove VM from the backup offering that may also delete VM backups.",
    )


class ResetPasswordForVirtualMachineRequest(APIRequest):
    id: str = Field(..., description="ID of the virtual machine")
    password: Optional[str] = Field(
        None,
        description="The new password of the virtual machine. If null, a random password will be generated for the VM.",
    )


class ResetSSHKeyForVirtualMachineRequest(APIRequest):
    id: str = Field(..., description="ID of the virtual machine")

    # -------------------------------------------------------------------------
    # ACCOUNT / DOMAIN / PROJECT
    # -------------------------------------------------------------------------
    account: Optional[str] = Field(None, description="Account for the VM (requires domainid)")
    domainid: Optional[str] = Field(None, description="Domain ID (required when account is set)")
    projectid: Optional[str] = Field(None, description="Deploy VM under this project")

    # -------------------------------------------------------------------------
    # SSH KEY PAIRS
    # -------------------------------------------------------------------------
    keypair: Optional[str] = Field(None, description="SSH key pair name")
    keypairs: Optional[list[str]] = Field(
        None, description="Multiple SSH key pair names (CSV serialized)"
    )

    # -------------------------------------------------------------------------
    # SERIALIZERS — CSV fields
    # -------------------------------------------------------------------------
    @field_serializer("keypairs")
    def serialize_csv(self, value: list[str] | None) -> str | None:
        if value is None:
            return None
        return ",".join(value)

    # -------------------------------------------------------------------------
    # VALIDATORS
    # -------------------------------------------------------------------------
    @model_validator(mode="after")
    def validate_mutual_exclusions(self):

        if self.account and not self.domainid:
            raise ValueError("domainid is required when account is provided")

        return self


class ResetUserDataForVirtualMachineRequest(APIRequest):
    id: str = Field(
        ...,
        description="The ID of the virtual machine",
    )

    account: Optional[str] = Field(
        default=None,
        description="Optional account for the virtual machine. Must be used with domainid",
    )

    domainid: Optional[str] = Field(
        default=None,
        description="Optional domain ID for the virtual machine",
    )

    projectid: Optional[str] = Field(
        default=None,
        description="Optional project ID for the virtual machine",
    )

    userdata: Optional[str] = Field(
        default=None,
        description="Base64 encoded userdata content",
    )

    userdataid: Optional[str] = Field(
        default=None,
        description="ID of stored userdata",
    )

    userdatadetails: Optional[list[UserDataDetail]] = Field(
        default=None,
        description="Variables and values used in userdata template",
    )

    # -------------------------------------------------------------------------
    # VALIDATORS
    # -------------------------------------------------------------------------
    @model_validator(mode="after")
    def validate_mutual_exclusions(self):

        if self.account and not self.domainid:
            raise ValueError("domainid is required when account is provided")

        return self


class RestoreVirtualMachineRequest(APIRequest):
    # -------------------------------------------------------------------------
    # REQUIRED
    # -------------------------------------------------------------------------
    virtualmachineid: str = Field(..., description="ID of the VM to restore")

    # -------------------------------------------------------------------------
    # RESTORE TARGET
    # Omit templateid to restore from the VM's original template/ISO
    # -------------------------------------------------------------------------
    templateid: Optional[str] = Field(
        None,
        description=(
            "Template or ISO ID to restore from. "
            "Omit to restore from the VM's original template/ISO."
        ),
    )

    # -------------------------------------------------------------------------
    # ROOT DISK OVERRIDES
    # details[0].rootdisksize takes precedence over rootdisksize if both provided
    # -------------------------------------------------------------------------
    diskofferingid: Optional[str] = Field(
        None, description="Override the root volume's disk offering"
    )
    rootdisksize: Optional[int] = Field(
        None,
        description=(
            "Override root volume size in GB. "
            "Superseded by details[0].rootdisksize if both are provided."
        ),
    )
    details: Optional[dict[str, str]] = Field(
        None,
        description=(
            "Custom key-value parameters e.g. {'rootdisksize': '100'}. "
            "Takes precedence over rootdisksize when both are set."
        ),
    )

    # -------------------------------------------------------------------------
    # CLEANUP
    # -------------------------------------------------------------------------
    expunge: Optional[bool] = Field(
        None, description="Expunge the old root volume after restore (default: False)"
    )

    # -------------------------------------------------------------------------
    # VALIDATORS
    # -------------------------------------------------------------------------
    @model_validator(mode="after")
    def validate_disk_size(self) -> RestoreVirtualMachineRequest:
        if (
            self.rootdisksize is not None
            and self.details is not None
            and "rootdisksize" in self.details
        ):
            raise ValueError(
                "rootdisksize and details['rootdisksize'] are both set — "
                "details['rootdisksize'] will take precedence. "
                "Remove one to avoid ambiguity."
            )
        return self


class RevertTOVMSanpshotRequest(APIRequest):
    vmsnapshotid: str = Field(..., alias="vmSnapshotId", description="The ID of the vm snapshot")


class ScaleVirtualMachineRequest(APIRequest):
    id: str = Field(
        ...,
        description="The ID of the virtual machine",
    )

    serviceofferingid: str = Field(
        ...,
        alias="serviceOfferingId",
        description="The ID of the new service offering",
    )

    automigrate: Optional[bool] = Field(
        None,
        alias="autoMigrate",
        description=(
            "Automatically migrate root volume when required to apply the new compute offering"
        ),
    )

    details: Optional[dict[str, str]] = Field(
        None,
        description=("Custom parameters for cpuspeed, memory and cpunumber"),
    )

    maxiops: Optional[int] = Field(
        None,
        ge=0,
        description="New maximum IOPS for the custom disk offering",
    )

    miniops: Optional[int] = Field(
        None,
        ge=0,
        description="New minimum IOPS for the custom disk offering",
    )

    shrinkok: Optional[bool] = Field(
        None,
        alias="shrinkOk",
        description="Verify OK to shrink the VM/root disk",
    )


class StartVirtualMachineRequest(BaseModel):
    id: str = Field(
        ...,
        description="The ID of the virtual machine",
    )

    bootintosetup: Optional[bool] = Field(
        None,
        alias="bootIntoSetup",
        description="Boot into hardware setup menu or not",
    )

    clusterid: Optional[str] = Field(
        None,
        alias="clusteId",
        description=("Destination Cluster ID to deploy the VM to (ROOT admin only)"),
    )

    deploymentplanner: Optional[str] = Field(
        None,
        alias="deploymentPlanner",
        description=("Deployment planner to use for VM allocation (ROOT admin only)"),
    )

    hostid: Optional[str] = Field(
        None,
        alias="hostId",
        description=("Destination Host ID to deploy the VM to (ROOT admin only)"),
    )

    podid: Optional[str] = Field(
        None,
        alias="podId",
        description=("Destination Pod ID to deploy the VM to (ROOT admin only)"),
    )


class StopVirtualMachineRequest(APIRequest):
    id: str = Field(..., description="ID of the virtual machine")
    forced: Optional[bool] = Field(
        None, description="Force stop the VM (VM is Stopped marked stopped)"
    )


class UpdateDefaultNICForVirtualMachineRequest(APIRequest):
    nicid: str = Field(..., alias="nicId", description="NIC ID for the virtual machine")
    virtualmachineid: str = Field(..., alias="virtualMachineId", description="Virtual Machine ID")


class DhcpOptionNetworkEntry(APIRequest):
    """Single entry for dhcpoptionsnetworklist."""

    networkid: str = Field(..., description="Network ID to apply DHCP options to")
    # DHCP options are dynamic keys like dhcp:66, dhcp:114 etc.
    # carried as extra kwargs — stored as a plain dict alongside networkid
    options: dict[str, str] = Field(
        default_factory=dict,
        description="DHCP option key-value pairs e.g. {'dhcp:66': 'www.test.com', 'dhcp:114': 'http://url'}",
    )


class UpdateVirtualMachineRequest(APIRequest):
    # -------------------------------------------------------------------------
    # REQUIRED
    # -------------------------------------------------------------------------
    id: str = Field(..., description="ID of the virtual machine to update")

    # -------------------------------------------------------------------------
    # DISPLAY / IDENTITY
    # name change requires VM stop/start to take effect
    # -------------------------------------------------------------------------
    name: Optional[str] = Field(
        None, description="New host name for the VM (requires stop/start to take effect)"
    )
    displayname: Optional[str] = Field(None, description="User-facing display name")
    displayvm: Optional[bool] = Field(None, description="Whether to display the VM to end users")
    group: Optional[str] = Field(None, description="Group name for the VM")
    instancename: Optional[str] = Field(
        None, description="Internal instance name (root admin only)"
    )
    customid: Optional[str] = Field(None, description="Custom resource ID (root admin only)")
    ostypeid: Optional[str] = Field(None, description="OS type ID that best represents this VM")

    # -------------------------------------------------------------------------
    # SECURITY GROUPS (mutually exclusive)
    # Basic Network zones only
    # -------------------------------------------------------------------------
    securitygroupids: Optional[list[str]] = Field(
        None, description="Security group IDs to apply (mutually exclusive with securitygroupnames)"
    )
    securitygroupnames: Optional[list[str]] = Field(
        None,
        description="Security group names to apply (mutually exclusive with securitygroupids, Basic Network zones only)",
    )

    # -------------------------------------------------------------------------
    # USER DATA
    # -------------------------------------------------------------------------
    userdata: Optional[str] = Field(
        None, description=("Base64-encoded user data. Max 4KB via GET, max 1MB via POST.")
    )
    userdataid: Optional[str] = Field(None, description="ID of pre-registered userdata")
    userdatadetails: Optional[dict[str, str]] = Field(
        None, description="Variable values for userdata template variables"
    )

    # -------------------------------------------------------------------------
    # DETAILS
    # 'extraconfig' key is explicitly not allowed inside details
    # cleanupdetails=True removes all existing details (details field ignored when True)
    # -------------------------------------------------------------------------
    details: Optional[dict[str, str]] = Field(
        None,
        description=(
            "Custom key-value parameters. "
            "'extraconfig' key is not permitted here — use the extraconfig field instead."
        ),
    )
    cleanupdetails: Optional[bool] = Field(
        None,
        description=(
            "If True, removes all existing details for this VM and ignores the details field. "
            "If False or omitted, details are merged/updated."
        ),
    )
    extraconfig: Optional[str] = Field(
        None, description="URL-encoded extra config string passed to the VM on start"
    )

    # -------------------------------------------------------------------------
    # DHCP OPTIONS
    # Format: dhcpoptionsnetworklist[0].networkid=...
    #         dhcpoptionsnetworklist[0].dhcp:66=www.test.com
    # -------------------------------------------------------------------------
    dhcpoptionsnetworklist: Optional[list[DhcpOptionNetworkEntry]] = Field(
        None, description="DHCP options per network, passed to the VM on startup"
    )

    # -------------------------------------------------------------------------
    # HA / SCALING
    # -------------------------------------------------------------------------
    haenable: Optional[bool] = Field(
        None, description="Enable or disable high availability for this VM"
    )
    isdynamicallyscalable: Optional[bool] = Field(
        None,
        description=(
            "True if VM has XS/VMware tools for dynamic CPU/memory scaling. "
            "Requires dynamic scaling enabled on template, offering, and global settings."
        ),
    )
    deleteprotection: Optional[bool] = Field(
        None,
        description=(
            "Protect the VM from deletion. "
            "Ignored if the VM is managed by autoscaling groups or CKS."
        ),
    )

    # -------------------------------------------------------------------------
    # LEASE
    # leaseduration=-1 removes an existing lease
    # -------------------------------------------------------------------------
    leaseduration: Optional[int] = Field(
        None, description="Lease duration in days from now. Pass -1 to remove an existing lease."
    )
    leaseexpiryaction: Optional[str] = Field(
        None, description="Action on lease expiry: STOP or DESTROY"
    )

    # -------------------------------------------------------------------------
    # VALIDATORS
    # -------------------------------------------------------------------------
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
            errors.append(
                "details is ignored when cleanupdetails=True — "
                "remove details or set cleanupdetails=False"
            )

        if self.leaseduration is not None and self.leaseduration < -1:
            errors.append("leaseduration must be -1 (remove lease) or a positive number of days")

        if errors:
            raise ValueError(errors)

        return self

    # -------------------------------------------------------------------------
    # SERIALIZERS
    # -------------------------------------------------------------------------
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
