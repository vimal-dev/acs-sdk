from typing import Optional
from pydantic import Field
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