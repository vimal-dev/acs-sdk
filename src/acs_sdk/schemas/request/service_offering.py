from pydantic import Field, model_validator
from typing import Optional
from .base import APIRequest, PaginationMixin


class CreateServiceOfferingRequest(APIRequest):
    """Request parameters for ``createServiceOffering``.

    Reference: https://cloudstack.apache.org/api/apidocs-4.22/apis/createServiceOffering.html
    """

    # --- required -----------------------------------------------------------

    name: str = Field(..., description="The name of the service offering")

    # --- compute ------------------------------------------------------------

    displaytext: Optional[str] = Field(
        None,
        alias="displayText",
        description="The display text of the service offering, defaults to 'name'",
    )
    cpunumber: Optional[int] = Field(
        None, alias="cpuNumber", description="The CPU number of the service offering"
    )
    cpuspeed: Optional[int] = Field(None, alias="cpuSpeed", description="CPU speed in MHz")
    memory: Optional[int] = Field(None, description="Total memory of the service offering in MB")
    customized: Optional[bool] = Field(
        None, description="Whether service offering size is custom or not"
    )
    customizediops: Optional[bool] = Field(
        None, alias="customizedIops", description="Whether compute offering IOPS is custom or not"
    )
    mincpunumber: Optional[int] = Field(
        None,
        alias="minCpuNumber",
        description="The minimum number of CPUs for a custom compute offering",
    )
    maxcpunumber: Optional[int] = Field(
        None,
        alias="maxCpuNumber",
        description="The maximum number of CPUs for a custom compute offering",
    )
    minmemory: Optional[int] = Field(
        None,
        alias="minMemory",
        description="The minimum memory size (MB) for a custom service offering",
    )
    maxmemory: Optional[int] = Field(
        None,
        alias="maxMemory",
        description="The maximum memory size (MB) for a custom service offering",
    )
    dynamicscalingenabled: Optional[bool] = Field(
        None,
        alias="dynamicScalingEnabled",
        description="True if virtual machine needs to be dynamically scalable",
    )
    limitcpuuse: Optional[bool] = Field(
        None,
        alias="limitCpuUse",
        description="Restrict the CPU usage to committed service offering",
    )

    # --- storage / disk -----------------------------------------------------

    storagetype: Optional[str] = Field(
        None, alias="storageType", description="Storage type: 'local' or 'shared'"
    )
    provisioningtype: Optional[str] = Field(
        None, alias="provisioningType", description="Provisioning type: 'thin', 'sparse', or 'fat'"
    )
    rootdisksize: Optional[int] = Field(
        None, alias="rootDiskSize", description="Root disk size in GB"
    )
    diskofferingid: Optional[str] = Field(
        None,
        alias="diskOfferingId",
        description="ID of the disk offering to map to this service offering",
    )
    diskofferingstrictness: Optional[bool] = Field(
        None,
        alias="diskOfferingStrictness",
        description="If true, disk offering override is not permitted during VM deployment",
    )
    encryptroot: Optional[bool] = Field(
        None,
        alias="encryptRoot",
        description="VMs using this offering require root volume encryption",
    )
    isvolatile: Optional[bool] = Field(
        None,
        alias="isVolatile",
        description="VM root disk is destroyed and recreated on each reboot",
    )
    cachemode: Optional[str] = Field(
        None,
        alias="cacheMode",
        description="Cache mode: none, writeback, writethrough, or hypervisor default",
    )
    hypervisorsnapshotreserve: Optional[int] = Field(
        None,
        alias="hypervisorSnapshotReserve",
        description="Hypervisor snapshot reserve space as a percent of a volume",
    )
    storagepolicy: Optional[str] = Field(
        None,
        alias="storagePolicy",
        description="Name of the storage policy defined at vCenter (VMware only)",
    )

    # --- IOPS / throughput --------------------------------------------------

    miniops: Optional[int] = Field(
        None, alias="minIops", description="Min IOPS of the compute offering"
    )
    maxiops: Optional[int] = Field(
        None, alias="maxIops", description="Max IOPS of the compute offering"
    )
    bytesreadrate: Optional[int] = Field(
        None, alias="bytesReadRate", description="Bytes read rate of the disk offering"
    )
    bytesreadratemax: Optional[int] = Field(
        None, alias="bytesReadRateMax", description="Burst bytes read rate of the disk offering"
    )
    bytesreadratemaxlength: Optional[int] = Field(
        None, alias="bytesReadRateMaxLength", description="Length (in seconds) of the read burst"
    )
    byteswriterate: Optional[int] = Field(
        None, alias="bytesWriteRate", description="Bytes write rate of the disk offering"
    )
    byteswriteratemax: Optional[int] = Field(
        None, alias="bytesWriteRateMax", description="Burst bytes write rate of the disk offering"
    )
    byteswriteratemaxlength: Optional[int] = Field(
        None, alias="bytesWriteRateMaxLength", description="Length (in seconds) of the write burst"
    )
    iopsreadrate: Optional[int] = Field(
        None, alias="iopsReadRate", description="IO requests read rate of the disk offering"
    )
    iopsreadratemax: Optional[int] = Field(
        None,
        alias="iopsReadRateMax",
        description="Burst IO requests read rate of the disk offering",
    )
    iopsreadratemaxlength: Optional[int] = Field(
        None,
        alias="iopsReadRateMaxLength",
        description="Length (in seconds) of the read IOPS burst",
    )
    iopswriterate: Optional[int] = Field(
        None, alias="iopsWriteRate", description="IO requests write rate of the disk offering"
    )
    iopswriteratemax: Optional[int] = Field(
        None,
        alias="iopsWriteRateMax",
        description="Burst IO requests write rate of the disk offering",
    )
    iopswriteratemaxlength: Optional[int] = Field(
        None,
        alias="iopsWriteRateMaxLength",
        description="Length (in seconds) of the write IOPS burst",
    )

    # --- network ------------------------------------------------------------

    networkrate: Optional[int] = Field(
        None, alias="networkRate", description="Data transfer rate in Mbps (non-system offerings)"
    )

    # --- HA / system --------------------------------------------------------

    offerha: Optional[bool] = Field(
        None, alias="offerHa", description="Enable HA for this service offering"
    )
    issystem: Optional[bool] = Field(
        None, alias="isSystem", description="Is this a system VM offering"
    )
    systemvmtype: Optional[str] = Field(
        None,
        alias="systemVmType",
        description="System VM type: 'domainrouter', 'consoleproxy', 'secondarystoragevm'",
    )

    # --- GPU ----------------------------------------------------------------

    vgpuprofileid: Optional[str] = Field(
        None,
        alias="vgpuProfileId",
        description="ID of the vGPU profile to map to this service offering",
    )
    gpucount: Optional[int] = Field(
        None, alias="gpuCount", description="Count of GPUs for this service offering"
    )
    gpudisplay: Optional[bool] = Field(
        None,
        alias="gpuDisplay",
        description="Whether to enable GPU display for this service offering",
    )

    # --- lease --------------------------------------------------------------

    leaseduration: Optional[int] = Field(
        None, alias="leaseDuration", description="Number of days instance is leased for"
    )
    leaseexpiryaction: Optional[str] = Field(
        None, alias="leaseExpiryAction", description="Lease expiry action: STOP or DESTROY"
    )
    purgeresources: Optional[bool] = Field(
        None, alias="purgeResources", description="Cleanup instance and resources upon VM expunge"
    )

    # --- placement / tags ---------------------------------------------------

    hosttags: Optional[str] = Field(
        None, alias="hostTags", description="Host tag for this service offering"
    )
    tags: Optional[str] = Field(None, description="Storage tags for this service offering")
    deploymentplanner: Optional[str] = Field(
        None,
        alias="deploymentPlanner",
        description="Deployment planner heuristic used to deploy a VM",
    )
    serviceofferingdetails: Optional[str] = Field(
        None,
        alias="serviceOfferingDetails",
        description="Details for planner (key/value parameters)",
    )
    externaldetails: Optional[str] = Field(
        None, alias="externalDetails", description="External key/value pair details"
    )

    # --- scope --------------------------------------------------------------

    domainid: Optional[str] = Field(
        None,
        alias="domainId",
        description="ID of the containing domain(s); null for public offerings",
    )
    zoneid: Optional[str] = Field(
        None, alias="zoneId", description="ID of the containing zone(s); null for public offerings"
    )


class DeleteServiceOfferingRequest(APIRequest):
    """Request parameters for ``deleteServiceOffering``.

    Reference: https://cloudstack.apache.org/api/apidocs-4.22/apis/deleteServiceOffering.html
    """

    id: str = Field(..., description="The ID of the service offering to delete")


class UpdateServiceOfferingRequest(APIRequest):
    """Request parameters for ``updateServiceOffering``.

    Reference: https://cloudstack.apache.org/api/apidocs-4.22/apis/updateServiceOffering.html
    """

    # --- required -----------------------------------------------------------

    id: str = Field(..., description="The ID of the service offering to update")

    # --- optional -----------------------------------------------------------

    name: Optional[str] = Field(None, description="New name for the service offering")
    displaytext: Optional[str] = Field(
        None, alias="displayText", description="New display text for the service offering"
    )
    domainid: Optional[str] = Field(
        None,
        alias="domainId",
        description="Containing domain ID(s) as comma-separated string; 'public' for public offerings",
    )
    zoneid: Optional[str] = Field(
        None,
        alias="zoneId",
        description="Containing zone ID(s) as comma-separated string; 'all' for all zones",
    )
    hosttags: Optional[str] = Field(
        None, alias="hostTags", description="Host tag for this service offering"
    )
    storagetags: Optional[str] = Field(
        None,
        alias="storageTags",
        description="Comma-separated storage tags matching existing storage pool tags",
    )
    state: Optional[str] = Field(None, description="State of the service offering")
    sortkey: Optional[int] = Field(
        None, alias="sortKey", description="Sort key of the service offering"
    )
    purgeresources: Optional[bool] = Field(
        None,
        alias="purgeResources",
        description="Whether to cleanup VM and its associated resources upon expunge",
    )
    cleanupexternaldetails: Optional[bool] = Field(
        None,
        alias="cleanupExternalDetails",
        description="Whether external details should be cleaned up",
    )
    externaldetails: Optional[str] = Field(
        None, alias="externalDetails", description="External key/value pair details"
    )


class ListServiceOfferingRequest(APIRequest, PaginationMixin):
    # Basic filters
    id: Optional[str] = Field(None, description="ID of the service offering")
    name: Optional[str] = Field(None, description="Name of the service offering")
    keyword: Optional[str] = Field(None, description="List by keyword")

    # Domain and account filters
    domainid: Optional[str] = Field(
        None, alias="domainId", description="List only resources belonging to the domain specified"
    )

    account: Optional[str] = Field(
        None, description="List resources by account. Must be used with the domainId parameter"
    )

    projectid: Optional[str] = Field(
        None,
        alias="projectId",
        description="List objects by project; if projectid=-1 lists all offerings",
    )

    isrecursive: Optional[bool] = Field(
        None,
        alias="isRecursive",
        description="Defaults to false, but if true, lists all resources from the parent specified by the domainId till leaves",
    )

    listall: Optional[bool] = Field(
        None,
        alias="listAll",
        description="If set to false, list only resources belonging to the command's caller; if set to true - list resources that the caller is authorized to see",
    )

    # System offering filters
    issystem: Optional[bool] = Field(
        None, alias="isSystem", description="Is this a system vm offering"
    )

    systemvmtype: Optional[str] = Field(
        None,
        alias="systemVmType",
        description="The system VM type. Possible types are 'consoleproxy', 'secondarystoragevm' or 'domainrouter'",
    )

    # VM and hardware filters
    virtualmachineid: Optional[str] = Field(
        None,
        alias="virtualMachineId",
        description="The ID of the virtual machine. Pass this in if you want to see the available service offering that a virtual machine can be changed to",
    )

    cpunumber: Optional[int] = Field(
        None, alias="cpuNumber", description="The CPU number that listed offerings must support"
    )

    cpuspeed: Optional[int] = Field(
        None, alias="cpuSpeed", description="The CPU speed that listed offerings must support"
    )

    memory: Optional[int] = Field(
        None, description="The RAM memory that listed offering must support"
    )

    # GPU and storage filters
    gpuenabled: Optional[bool] = Field(
        None,
        alias="gpuEnabled",
        description="Flag to indicate if the service offering supports GPU. If set to true, only service offerings that support GPU will be returned",
    )

    vgpuprofileid: Optional[str] = Field(
        None,
        alias="vgpuProfileId",
        description="The ID of the vGPU profile that listed offerings must support",
    )

    encryptroot: Optional[bool] = Field(
        None, alias="encryptRoot", description="Listed offerings support root disk encryption"
    )

    storagetype: Optional[str] = Field(
        None,
        alias="storageType",
        description="The storage type of the service offering. Values are 'local' and 'shared'",
    )

    # Zone and template filters
    zoneid: Optional[str] = Field(
        None, alias="zoneId", description="ID of zone the service offering is associated with"
    )

    templateid: Optional[str] = Field(
        None,
        alias="templateId",
        description="The ID of the template that listed offerings must support",
    )

    # State filter
    state: Optional[str] = Field(
        None,
        description="Filter by state of the service offering. Defaults to 'Active'. If set to 'all' shows both Active & Inactive offerings",
    )

    @model_validator(mode="after")
    def validate_model_dependency(self):
        if self.account and not self.domainid:
            raise ValueError("domainid is required when account is provided")
        return self
