from pydantic import Field, model_validator
from typing import Optional
from .base import APIRequest, PaginationMixin


class ListDiskOfferingRequest(APIRequest, PaginationMixin):

    # Basic filters
    id: Optional[str] = Field(None, description="ID of the disk offering")
    name: Optional[str] = Field(None, description="Name of the disk offering")
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

    # hardware filters
    virtualmachineid: Optional[str] = Field(
        None,
        alias="virtualMachineId",
        description="The ID of a virtual machine. Pass this in if you want to see the suitable disk offering that can be used to create and add a disk to the virtual machine"
    )

    encrypt: Optional[bool] = Field(
        None,
        description="Listed offerings support disk encryption"
    )

    storagetype: Optional[str] = Field(
        None,
        alias="storageType",
        description="The storage type of the service offering. Values are 'local' and 'shared'"
    )

    storageid: Optional[str] = Field(
        None,
        alias="storageId",
        description="The ID of the storage pool, tags of the storage pool are used to filter the offerings"
    )

    volumeid: Optional[str] = Field(
        None,
        alias="volumeId",
        description="The ID of the volume, tags of the volume are used to filter the offerings"
    )

    zoneid: Optional[str] = Field(
        None,
        alias="zoneId",
        description="ID of zone the service offering is associated with"
    )

    # State filter
    state: Optional[str] = Field(
        None,
        description="Filter by state of the disk offering. Defaults to 'Active'. If set to 'all' shows both Active & Inactive offerings."
    )

    @model_validator(mode="after")
    def validate_model_dependency(self):        
        if self.account and not self.domainid:
            raise ValueError("domainid is required when account is provided")
        return self