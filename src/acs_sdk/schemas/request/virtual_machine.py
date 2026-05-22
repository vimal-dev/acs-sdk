from typing import Dict, List, Optional
from pydantic import Field, field_serializer, model_validator

from .base import APIRequest


class ListVirtualMachinesRequest(APIRequest):
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
        None, description="Comma-separated list of details (e.g., 'all', 'nics', 'stats')"
    )

    # Pagination
    page: Optional[int] = Field(1, ge=1, description="Page number")
    pagesize: Optional[int] = Field(50, ge=1, le=500, description="Number of results per page")

    # Advanced filters
    forvirtualnetwork: Optional[bool] = Field(None, description="List VMs for virtual network")

    storageid: Optional[str] = Field(None, description="Filter by storage ID")


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


class AssignVirtualMachineToBackupOfferingRequest(APIRequest):
    virtualmachineid: str = Field(..., description="ID of the virtual machine")
    backupofferingid: str = Field(..., description="ID of the backup offering to assign the VM to")


class CreateVMScheduleRequest(APIRequest):
    virtualmachineid: str = Field(..., description="ID of the virtual machine")
    schedule: str = Field(
        ..., description="Schedule in cron format (e.g., '0 0 * * *' for daily at midnight)"
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
        ..., description="Schedule in cron format (e.g., '0 0 * * *' for daily at midnight)"
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
    snapshotid: Optional[str] = Field(
        None, description="ID of the snapshot to create the VM from (mutually exclusive with templateid)"
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
        None, description="Network IDs to attach (CSV serialized, mutually exclusive with iptonetworklist)"
    )
    ipaddress: Optional[str] = Field(None, description="Static IPv4 for the default network")
    ip6address: Optional[str] = Field(None, description="Static IPv6 for the default network")
    macaddress: Optional[str] = Field(None, description="MAC address for the default network")

    # -------------------------------------------------------------------------
    # AFFINITY GROUPS (mutually exclusive)
    # -------------------------------------------------------------------------
    affinitygroupids: Optional[list[str]] = Field(
        None, description="Affinity group IDs (mutually exclusive with affinitygroupnames)"
    )
    affinitygroupnames: Optional[list[str]] = Field(
        None, description="Affinity group names (mutually exclusive with affinitygroupids)"
    )

    # -------------------------------------------------------------------------
    # SECURITY GROUPS (mutually exclusive, Basic Network zones only)
    # -------------------------------------------------------------------------
    securitygroupids: Optional[list[str]] = Field(
        None, description="Security group IDs (mutually exclusive with securitygroupnames)"
    )
    securitygroupnames: Optional[list[str]] = Field(
        None, description="Security group names (mutually exclusive with securitygroupids)"
    )

    # -------------------------------------------------------------------------
    # DISK
    # diskofferingid and datadisksdetails are mutually exclusive
    # size is mutually exclusive with diskofferingid
    # -------------------------------------------------------------------------
    diskofferingid: Optional[str] = Field(None, description="Disk offering ID")
    overridediskofferingid: Optional[str] = Field(
        None, description="Override root disk offering (takes precedence for ISO deploys)"
    )
    rootdisksize: Optional[int] = Field(
        None, description="Root disk size in GB (template-based deploys only)"
    )
    size: Optional[int] = Field(
        None, description="Data disk size in GB (mutually exclusive with diskofferingid)"
    )
    datadiskofferinglist: Optional[list[str]] = Field(
        None, description="Data disk offering IDs (mutually exclusive with diskofferingid)"
    )
    datadisksdetails: Optional[list[dict[str, str]]] = Field(
        None, description="Data disk details e.g. diskofferingid, size, miniops, maxiops per disk"
    )

    # -------------------------------------------------------------------------
    # USER DATA
    # -------------------------------------------------------------------------
    userdata: Optional[str] = Field(None, description="Base64-encoded user data (max 4KB via GET, 1MB via POST)")
    userdataid: Optional[str] = Field(None, description="ID of pre-registered userdata")
    userdatadetails: Optional[dict[str, str]] = Field(
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
    bootintosetup: Optional[bool] = Field(None, description="Boot into hardware setup (VMware only)")

    # -------------------------------------------------------------------------
    # PLACEMENT (root admin only)
    # -------------------------------------------------------------------------
    hostid: Optional[str] = Field(None, description="Target host ID (root admin only)")
    clusterid: Optional[str] = Field(None, description="Target cluster ID (root admin only)")
    podid: Optional[str] = Field(None, description="Target pod ID (root admin only)")
    deploymentplanner: Optional[str] = Field(None, description="Deployment planner (root admin only)")
    hypervisor: Optional[str] = Field(None, description="Hypervisor type (required if not set on template/ISO)")

    # -------------------------------------------------------------------------
    # ADVANCED / MISC
    # -------------------------------------------------------------------------
    group: Optional[str] = Field(None, description="VM group name")
    displayvm: Optional[bool] = Field(None, description="Display VM to end user (default: True)")
    copyimagetags: Optional[bool] = Field(None, description="Copy image tags to VM (default: False)")
    dynamicscalingenabled: Optional[bool] = Field(None, description="Enable dynamic CPU/memory scaling")
    iothreadsenabled: Optional[bool] = Field(None, description="Enable IO threads for disk devices")
    iodriverpolicy: Optional[str] = Field(None, description="IO driver policy: native, emulated, auto")
    nicmultiqueuenumber: Optional[int] = Field(None, description="Number of queues for multiqueue NICs")
    nicpackedvirtqueuesenabled: Optional[bool] = Field(None, description="Enable packed virtqueues")
    keyboard: Optional[str] = Field(
        None, description="Keyboard type: de, de-ch, es, fi, fr, fr-be, fr-ch, is, it, jp, nl-be, no, pt, uk, us"
    )
    extraconfig: Optional[str] = Field(None, description="URL-encoded extra config (passed on successful deploy)")
    leaseduration: Optional[int] = Field(None, description="Lease duration in days")
    leaseexpiryaction: Optional[str] = Field(None, description="Lease expiry action: STOP or DESTROY")
    password: Optional[str] = Field(None, description="VM password (random if not set)")

    # -------------------------------------------------------------------------
    # SERIALIZERS — CSV fields
    # -------------------------------------------------------------------------
    @field_serializer("networkids", "keypairs", "affinitygroupids", "affinitygroupnames",
                      "securitygroupids", "securitygroupnames", "datadiskofferinglist")
    def serialize_csv(self, value: list[str] | None) -> str | None:
        if value is None:
            return None
        return ",".join(value)

    # -------------------------------------------------------------------------
    # VALIDATORS
    # -------------------------------------------------------------------------
    @model_validator(mode="after")
    def validate_mutual_exclusions(self):
        errors = []

        if self.templateid and self.snapshotid:
            errors.append("templateid and snapshotid are mutually exclusive")

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
