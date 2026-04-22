from pydantic import Field, model_validator
from typing import Optional
from .base import APIRequest, PaginationMixin


class ListServiceOfferingRequest(APIRequest, PaginationMixin):

    # Basic filters
    id: Optional[str] = Field(None, description="ID of the service offering")
    name: Optional[str] = Field(None, description="Name of the service offering")
    keyword: Optional[str] = Field(None, description="List by keyword")

    # Domain and account filters
    domainid: Optional[str] = Field(
        None,
        alias="domainId",
        description="List only resources belonging to the domain specified"
    )

    account: Optional[str] = Field(
        None,
        description="List resources by account. Must be used with the domainId parameter"
    )

    projectid: Optional[str] = Field(
        None,
        alias="projectId",
        description="List objects by project; if projectid=-1 lists all offerings"
    )

    isrecursive: Optional[bool] = Field(
        None,
        alias="isRecursive",
        description="Defaults to false, but if true, lists all resources from the parent specified by the domainId till leaves"
    )

    listall: Optional[bool] = Field(
        None,
        alias="listAll",
        description="If set to false, list only resources belonging to the command's caller; if set to true - list resources that the caller is authorized to see"
    )

    # System offering filters
    issystem: Optional[bool] = Field(
        None,
        alias="isSystem",
        description="Is this a system vm offering"
    )

    systemvmtype: Optional[str] = Field(
        None,
        alias="systemVmType",
        description="The system VM type. Possible types are 'consoleproxy', 'secondarystoragevm' or 'domainrouter'"
    )

    # VM and hardware filters
    virtualmachineid: Optional[str] = Field(
        None,
        alias="virtualMachineId",
        description="The ID of the virtual machine. Pass this in if you want to see the available service offering that a virtual machine can be changed to"
    )

    cpunumber: Optional[int] = Field(
        None,
        alias="cpuNumber",
        description="The CPU number that listed offerings must support"
    )

    cpuspeed: Optional[int] = Field(
        None,
        alias="cpuSpeed",
        description="The CPU speed that listed offerings must support"
    )

    memory: Optional[int] = Field(
        None,
        description="The RAM memory that listed offering must support"
    )

    # GPU and storage filters
    gpuenabled: Optional[bool] = Field(
        None,
        alias="gpuEnabled",
        description="Flag to indicate if the service offering supports GPU. If set to true, only service offerings that support GPU will be returned"
    )

    vgpuprofileid: Optional[str] = Field(
        None,
        alias="vgpuProfileId",
        description="The ID of the vGPU profile that listed offerings must support"
    )

    encryptroot: Optional[bool] = Field(
        None,
        alias="encryptRoot",
        description="Listed offerings support root disk encryption"
    )

    storagetype: Optional[str] = Field(
        None,
        alias="storageType",
        description="The storage type of the service offering. Values are 'local' and 'shared'"
    )

    # Zone and template filters
    zoneid: Optional[str] = Field(
        None,
        alias="zoneId",
        description="ID of zone the service offering is associated with"
    )

    templateid: Optional[str] = Field(
        None,
        alias="templateId",
        description="The ID of the template that listed offerings must support"
    )

    # State filter
    state: Optional[str] = Field(
        None,
        description="Filter by state of the service offering. Defaults to 'Active'. If set to 'all' shows both Active & Inactive offerings"
    )

    @model_validator(mode="after")
    def validate_model_dependency(self):        
        if self.account and not self.domainid:
            raise ValueError("domainid is required when account is provided")
        return self