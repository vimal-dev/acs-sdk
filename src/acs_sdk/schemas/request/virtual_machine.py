from typing import Dict, List, Optional
from pydantic import Field, model_validator

from acs_sdk.services import account
from .base import APIRequest


class ListVirtualMachinesRequest(APIRequest):
    # Filters
    id: Optional[str] = Field(None, description="List VM by ID")
    name: Optional[str] = Field(None, description="List VM by name")
    keyword: Optional[str] = Field(None, description="Search keyword")

    account: Optional[str] = Field(None, description="List VMs by account name")
    accountid: Optional[str] = Field(None, description="List VMs by account ID")

    domainid: Optional[str] = Field(None, description="Domain ID")
    isrecursive: Optional[bool] = Field(
        None,
        description="Include subdomains (used with domainid)"
    )

    projectid: Optional[str] = Field(None, description="Project ID")

    zoneid: Optional[str] = Field(None, description="Zone ID")
    hostid: Optional[str] = Field(None, description="Host ID")

    clusterid: Optional[str] = Field(None, description="Cluster ID")
    podid: Optional[str] = Field(None, description="Pod ID")

    networkid: Optional[str] = Field(None, description="Network ID")
    vpcid: Optional[str] = Field(None, description="VPC ID")

    serviceofferingid: Optional[str] = Field(
        None,
        description="Filter by service offering"
    )

    templateid: Optional[str] = Field(None, description="Template ID")
    isoid: Optional[str] = Field(None, description="ISO ID")

    state: Optional[str] = Field(
        None,
        description="VM state (Running, Stopped, Destroyed, etc.)"
    )

    haenable: Optional[bool] = Field(
        None,
        description="Filter HA-enabled VMs"
    )

    hypervisor: Optional[str] = Field(
        None,
        description="Filter by hypervisor type"
    )

    tags: Optional[str] = Field(
        None,
        description="List VMs by tags (key/value pairs)"
    )

    # Access / visibility
    listall: Optional[bool] = Field(
        None,
        description="List all VMs available to the caller"
    )

    details: Optional[str] = Field(
        None,
        description="Comma-separated list of details (e.g., 'all', 'nics', 'stats')"
    )

    # Pagination
    page: Optional[int] = Field(
        1, ge=1, description="Page number"
    )
    pagesize: Optional[int] = Field(
        50, ge=1, le=500, description="Number of results per page"
    )

    # Advanced filters
    forvirtualnetwork: Optional[bool] = Field(
        None,
        description="List VMs for virtual network"
    )

    storageid: Optional[str] = Field(
        None,
        description="Filter by storage ID"
    )

class AddNICToVirtualMachineRequest(APIRequest):
    virtualmachineid: str = Field(..., description="ID of the virtual machine")
    networkid: str = Field(..., description="ID of the network to add the NIC to")
    dhcpoptions: Optional[str] = Field(
        None,
        description="DHCP options which are passed to the nic Example: dhcpoptions[0].dhcp:114=url&dhcpoptions[0].dhcp:66=www.test.com"
    )
    ipaddress: Optional[str] = Field(
        None,
        description="IP address for the new NIC. If not specified, an IP address will be automatically allocated from the specified network."
    )
    macaddress: Optional[str] = Field(
        None,
        description="MAC address for the new NIC."
    )

class AssignVirtualMachineToBackupOfferingRequest(APIRequest):
    virtualmachineid: str = Field(..., description="ID of the virtual machine")
    backupofferingid: str = Field(..., description="ID of the backup offering to assign the VM to")


class CreateVMScheduleRequest(APIRequest):
    virtualmachineid: str = Field(..., description="ID of the virtual machine")
    schedule: str = Field(..., description="Schedule in cron format (e.g., '0 0 * * *' for daily at midnight)")
    timezone: Optional[str] = Field(
        None,
        description="Timezone for the schedule (e.g., 'UTC', 'America/New_York')"
    )
    action: str = Field(..., description="Action to perform (e.g., 'start', 'stop', 'reboot', 'force_stop', 'force_reboot')")
    description: Optional[str] = Field(
        None,
        description="Optional description for the schedule"
    )
    enabled: Optional[bool] = Field(
        None,
        description="Whether the schedule is enabled (default: True)"
    )
    startdate: Optional[str] = Field(
        None,
        description="Start date for the schedule in ISO 8601 format (e.g., '2024-01-01T00:00:00Z')"
    )
    enddate: Optional[str] = Field(
        None,
        description="End date for the schedule in ISO 8601 format (e.g., '2024-12-31T23:59:59Z')"
    )


class UpdateVMScheduleRequest(APIRequest):
    id: str = Field(..., description="ID of the virtual machine schedule to update")
    schedule: str = Field(..., description="Schedule in cron format (e.g., '0 0 * * *' for daily at midnight)")
    timezone: Optional[str] = Field(
        None,
        description="Timezone for the schedule (e.g., 'UTC', 'America/New_York')"
    )
    description: Optional[str] = Field(
        None,
        description="Optional description for the schedule"
    )
    enabled: Optional[bool] = Field(
        None,
        description="Whether the schedule is enabled (default: True)"
    )
    startdate: Optional[str] = Field(
        None,
        description="Start date for the schedule in ISO 8601 format (e.g., '2024-01-01T00:00:00Z')"
    )
    enddate: Optional[str] = Field(
        None,
        description="End date for the schedule in ISO 8601 format (e.g., '2024-12-31T23:59:59Z')"
    )

class DeleteVMScheduleRequest(APIRequest):
    virtualmachineid: str = Field(..., description="ID of the virtual machine")
    id: str = Field(..., description="ID of the virtual machine schedule to update")
    ids: Optional[List[str]] = Field(
        None,
        description="List of IDs of the virtual machine schedules to delete (if multiple schedules need to be deleted)"
    )


class DeployVirtualMachineRequest(APIRequest):

    # REQUIRED
    serviceofferingid: str = Field(..., description="ID of the service offering")
    zoneid: str = Field(..., description="Availability zone for the virtual machine")
    templateid: str = Field(..., description="ID of the template")

    # GENERAL OPTIONS
    customid: Optional[str] = Field(
        None,
        description="Custom ID for the virtual machine (optional, allows you to specify your own ID instead of having one auto-generated)"
    )
    name: Optional[str] = Field(
        None,
        description="Host name for the virtual machine (optional)"
    )
    displayname: Optional[str] = Field(
        None,
        description="Display name for the virtual machine (optional)"
    )
    displayvm: Optional[bool] = Field(
        None,
        description="Whether to display the VM to the end user (default: True)"
    )
    group: Optional[str] = Field(
        None,
        description="Group for the virtual machine (optional)"
    )
    projectid: Optional[str] = Field(
        None,     
        description="Project ID for the virtual machine (optional)"
    )


    # ACCOUNT / DOMAIN
    account: Optional[str] = Field(
        None, description="List resources by account (requires domainid)"
    )
    domainid: Optional[str] = Field(
        None, alias="domainId", description="Filter by domain ID"
    )

    # AFFINITY GROUPS (mutually exclusive)
    affinitygroupids: Optional[List[str]] = Field(
        None, alias="affinityGroupIds"
    )
    affinitygroupnames: Optional[List[str]] = Field(
        None, alias="affinityGroupNames"
    )

    # SECURITY GROUPS (mutually exclusive)
    securitygroupids: Optional[List[str]] = Field(
        None, alias="securityGroupIds"
    )
    securitygroupnames: Optional[List[str]] = Field(
        None, alias="securityGroupNames"
    )

    # DISK OPTIONS
    diskofferingid: Optional[str] = Field(
        None,
        description="ID of the disk offering (optional if template already has a disk offering)"
    )
    size: Optional[int] = Field(
        None,
        description="Data disk size in GB (optional, only used if diskofferingid is not specified and template does not have a disk offering)"
    )
    rootdisksize: Optional[int] = Field(
        None,
        description="Root disk size in GB (optional, only used if template does not have a disk offering or if you want to override the template's root disk size)"
    )
    overridediskofferingid: Optional[str] = Field(
        None,
        description="ID of the disk offering to override the template's disk offering (optional, only used if template has a disk offering and you want to use a different one)"
    )
    datadiskofferinglist: Optional[List[str]] = Field(
        None,
        description="List of disk offering IDs for data disks (optional, only used if you want to specify multiple data disks or if you want to override the template's disk offering for data disks)"
    )
    dadatadisksdetails: Optional[List[Dict[str, str]]] = Field(
        None,
        alias="datadisksdetails",
        description="List of key-value pairs for data disk details (optional, alternative to providing datadiskofferinglist or used to provide additional details for each data disk such as size if not specified in the disk offering)"
    )

    # NETWORK / HOST CONFIG    
    networkids: Optional[List[str]] = Field(
        None,
        description="List of network IDs to attach to the VM (optional if template already has network requirements)"
    )
    vpcid: Optional[str] = Field(
        None,
        description="ID of the VPC to deploy the VM into (optional, only used if template does not have network requirements or if you want to override the template's network requirements)"
    )
    extraconfig: Optional[str] = Field(
        None,
        description="Extra configuration parameters for the VM in key=value format (optional)"
    )

    # USER DATA
    userdata: Optional[str] = Field(
        None,
        description="Base64-encoded user data to be passed to the VM (optional)"
    )
    userdatadetails: Optional[Dict[str, str]] = Field(
        None,
        alias="userDataDetails",
        description="Key-value pairs of user data details (optional, alternative to providing userdata directly or via userdataid)"
    )
    userdataid: Optional[str] = Field(
        None,
        description="ID of the user data to be passed to the VM (optional, alternative to providing userdata directly)"
    )

    # Security / access
    keypair: Optional[str] = Field(
        None,
        description="Name of the SSH key pair to inject into the VM (optional)"
    )
    keyspairs: Optional[List[str]] = Field(
        None,
        description="List of SSH key pairs to inject into the VM (optional, alternative to providing a single keypair)"
    )

    # ✅ AFFINITY GROUPS (mutually exclusive)
    affinitygroupids: Optional[List[str]] = Field(
        None, alias="affinityGroupIds"
    )
    affinitygroupnames: Optional[List[str]] = Field(
        None, alias="affinityGroupNames"
    )


    # ADVANCED FLAGS
    bootintosetup: Optional[bool] = Field(
        None,
        description="Whether to boot the VM into setup mode (default: False)"
    )
    bootmode: Optional[str] = Field(
        None,
        description="Boot mode for the VM (e.g., 'legacy', 'uefi', 'uefi_secure')"
    )
    clusterid: Optional[str] = Field(
        None,   
        description="ID of the cluster to deploy the VM into (optional, overrides hostid if both are specified)"
    )
    hostid: Optional[str] = Field(
        None,
        description="ID of the host to deploy the VM on (optional, overrides clusterid if both are specified)"
    )
    podid: Optional[str] = Field(
        None,
        description="ID of the pod to deploy the VM into (optional, overrides zoneid if both are specified)"
    )
    dynamicscalingenabled: Optional[bool] = Field(
        None,
        description="Whether dynamic scaling is enabled for the VM (default: False)"
    )
    haenable: Optional[bool] = Field(
        None,
        description="Whether to enable high availability for the VM (default: False)"
    )
    iothreadsenabled: Optional[bool] = Field(
        None,
        description="Whether to enable IO threads for the VM (default: False)"
    )
    iodriverpolicy: Optional[str] = Field(
        None,
        description="IO driver policy for the VM (e.g., 'native', 'emulated', 'auto')"
    )
    hypervisor: Optional[str] = Field(
        None,
        description="Hypervisor type to deploy the VM on (e.g., 'kvm', 'xen', 'vmware')"
    )
    snapshotid: Optional[str] = Field(
        None,
        description="ID of the snapshot to create the VM from (optional, alternative to templateid)"
    )
    startvm: Optional[bool] = Field(
        None,
        description="Whether to start the VM after deployment (default: True)"
    )

    @model_validator(mode="after")
    def validate_model_dependency(self):
        if self.affinitygroupids and self.affinitygroupnames:
            raise ValueError("affinitygroupids and affinitygroupnames are mutually exclusive")

        if self.securitygroupids and self.securitygroupnames:
            raise ValueError("securitygroupids and securitygroupnames are mutually exclusive")

        if self.diskofferingid and self.size:
            raise ValueError("diskofferingid and size are mutually exclusive")
        
        if self.account and not self.domainid:
            raise ValueError("domainid is required when account is provided")
        return self
    
class DestroyVirtualMachineRequest(APIRequest):
    id: str = Field(..., description="ID of the virtual machine to destroy")
    expunge: Optional[bool] = Field(
        None,
        description="Whether to expunge the VM immediately (default: False, which means the VM will be marked as destroyed but not expunged until the next cleanup cycle)"
    )
    volumeids: Optional[List[str]] = Field(
        None,
        description="List of volume IDs to destroy along with the VM (optional, only used if expunge is True)"
    )