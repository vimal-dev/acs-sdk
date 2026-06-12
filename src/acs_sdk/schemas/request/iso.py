from typing import Literal, Optional

from pydantic import Field

from .base import APIRequest, PaginationMixin


IsoFilter = Literal[
    "featured",
    "self",
    "selfexecutable",
    "sharedexecutable",
    "executable",
    "community",
    "all",
]

IsoCPUArchitecture = Literal[
    "x86_64",
    "aarch64",
]

IsoFormat = Literal[
    "QCOW2",
    "OVA",
    "VHD",
]

ExtractMode = Literal[
    "HTTP_DOWNLOAD",
    "FTP_UPLOAD",
]

IsoPermissionOp = Literal[
    "add",
    "remove",
    "reset",
]


class AttachIsoRequest(APIRequest):
    id: str = Field(..., description="The ID of the ISO file.")
    virtualmachineid: str = Field(..., alias="virtualMachineId", description="The ID of the virtual machine.")
    forced: Optional[bool] = Field(None, description="If true, ejects existing ISO before attaching on VMware.")


class CopyIsoRequest(APIRequest):
    id: str = Field(..., description="The ID of the ISO to copy.")
    destzoneid: Optional[str] = Field(None, alias="destZoneId", description="ID of the zone to copy the ISO to.")
    destzoneids: Optional[list[str]] = Field(None, alias="destZoneIds", description="Comma-separated list of zone IDs for multi-zone copy. Mutually exclusive with destzoneid.")
    sourcezoneid: Optional[str] = Field(None, alias="sourceZoneId", description="ID of the zone where the ISO is currently hosted.")


class DeleteIsoRequest(APIRequest):
    id: str = Field(..., description="The ID of the ISO file.")
    zoneid: Optional[str] = Field(None, alias="zoneId", description="The ID of the zone. If not specified, the ISO will be deleted from all zones.")


class DetachIsoRequest(APIRequest):
    virtualmachineid: str = Field(..., alias="virtualMachineId", description="The ID of the virtual machine.")
    forced: Optional[bool] = Field(None, description="If true, ejects the ISO before detaching on VMware.")


class ExtractIsoRequest(APIRequest):
    id: str = Field(..., description="The ID of the ISO file.")
    mode: ExtractMode = Field(..., description="The mode of extraction - HTTP_DOWNLOAD or FTP_UPLOAD.")
    url: Optional[str] = Field(None, description="The URL to which the ISO would be extracted.")
    zoneid: Optional[str] = Field(None, alias="zoneId", description="The ID of the zone where the ISO is originally located.")


class GetUploadParamsForIsoRequest(APIRequest):
    format: IsoFormat = Field(..., description="The format for the ISO. Possible values: QCOW2, OVA, VHD.")
    name: str = Field(..., description="The name of the ISO.")
    zoneid: str = Field(..., alias="zoneId", description="The ID of the zone the ISO is to be hosted on.")
    account: Optional[str] = Field(None, description="An optional account name. Must be used with domainid.")
    bootable: Optional[bool] = Field(None, description="True if this ISO is bootable. Defaults to true.")
    checksum: Optional[str] = Field(None, description="The checksum value for the ISO, with algorithm prefix (e.g. md5:, sha256:).")
    displaytext: Optional[str] = Field(None, alias="displayText", description="The display text of the ISO.")
    domainid: Optional[str] = Field(None, alias="domainId", description="An optional domain ID. Must be used with account.")
    isextractable: Optional[bool] = Field(None, alias="isExtractable", description="True if the ISO or its derivatives are extractable. Defaults to false.")
    isfeatured: Optional[bool] = Field(None, alias="isFeatured", description="True if this ISO should be featured.")
    ispublic: Optional[bool] = Field(None, alias="isPublic", description="True if this ISO is publicly accessible.")
    ostypeid: Optional[str] = Field(None, alias="osTypeId", description="The ID of the OS type. Required if bootable is true.")
    projectid: Optional[str] = Field(None, alias="projectId", description="Upload ISO for the project.")


class ListIsoPermissionsRequest(APIRequest):
    id: str = Field(..., description="The ISO ID.")


class ListIsosRequest(APIRequest, PaginationMixin):
    account: Optional[str] = Field(None, description="List resources by account. Must be used with domainid.")
    arch: Optional[IsoCPUArchitecture] = Field(None, description="CPU architecture filter: x86_64 or aarch64.")
    bootable: Optional[bool] = Field(None, description="Filter by whether ISOs can be used to boot a system.")
    domainid: Optional[str] = Field(None, alias="domainId", description="List only resources belonging to the specified domain.")
    hypervisor: Optional[str] = Field(None, description="The hypervisor for which to restrict the search.")
    id: Optional[str] = Field(None, description="List ISOs by ID.")
    imagestoreid: Optional[str] = Field(None, alias="imageStoreId", description="ID of the image or image cache store.")
    isofilter: Optional[IsoFilter] = Field(None, alias="isoFilter", description="Filter by category: featured, self, selfexecutable, sharedexecutable, executable, community, or all.")
    ispublic: Optional[bool] = Field(None, alias="isPublic", description="True if the ISO is publicly accessible.")
    isready: Optional[bool] = Field(None, alias="isReady", description="List only ISOs that are ready to be deployed.")
    isrecursive: Optional[bool] = Field(None, alias="isRecursive", description="If true, lists all resources from the parent domain down to leaves.")
    keyword: Optional[str] = Field(None, description="List by keyword.")
    listall: Optional[bool] = Field(None, alias="listAll", description="If true, lists all resources the caller is authorized to see.")
    name: Optional[str] = Field(None, description="Filter by ISO name.")
    oscategoryid: Optional[str] = Field(None, alias="osCategoryId", description="The OS category ID to filter by.")
    projectid: Optional[str] = Field(None, alias="projectId", description="Project ID; use -1 for all projects.")
    showicon: Optional[bool] = Field(None, alias="showIcon", description="Flag to display resource icon for the ISOs.")
    showremoved: Optional[bool] = Field(None, alias="showRemoved", description="Include removed ISOs in the results.")
    showunique: Optional[bool] = Field(None, alias="showUnique", description="List only unique ISOs across zones.")
    storageid: Optional[str] = Field(None, alias="storageId", description="The ID of the storage pool to filter by.")
    tags: Optional[str] = Field(None, description="List resources by tags (key/value pairs).")
    zoneid: Optional[str] = Field(None, alias="zoneId", description="The ID of the zone to filter by.")


class RegisterIsoRequest(APIRequest):
    name: str = Field(..., description="The name of the ISO.")
    url: str = Field(..., description="The URL where the ISO is currently hosted.")
    zoneid: str = Field(..., alias="zoneId", description="The ID of the zone to register the ISO to.")
    account: Optional[str] = Field(None, description="An optional account name. Must be paired with domainid.")
    arch: Optional[IsoCPUArchitecture] = Field(None, description="CPU architecture: x86_64 or aarch64.")
    bootable: Optional[bool] = Field(None, description="True if this ISO is bootable. Defaults to true.")
    checksum: Optional[str] = Field(None, description="The checksum of the ISO, with algorithm prefix (e.g. md5:, sha256:).")
    directdownload: Optional[bool] = Field(None, alias="directDownload", description="If true, bypasses Secondary Storage and downloads directly to Primary Storage.")
    displaytext: Optional[str] = Field(None, alias="displayText", description="The display text of the ISO. Defaults to name if omitted.")
    domainid: Optional[str] = Field(None, alias="domainId", description="An optional domain ID. Required when account is used.")
    imagestoreuuid: Optional[str] = Field(None, alias="imageStoreUuid", description="The image store UUID to register the ISO to.")
    isdynamicallyscalable: Optional[bool] = Field(None, alias="isDynamicallyScalable", description="True if the ISO supports dynamic scaling via XS/VMware tools.")
    isextractable: Optional[bool] = Field(None, alias="isExtractable", description="True if the ISO or its derivatives are extractable. Defaults to false.")
    isfeatured: Optional[bool] = Field(None, alias="isFeatured", description="True if this ISO should be featured.")
    ispublic: Optional[bool] = Field(None, alias="isPublic", description="True if this ISO is publicly accessible.")
    ostypeid: Optional[str] = Field(None, alias="osTypeId", description="The ID of the OS type. Required for bootable ISOs.")
    passwordenabled: Optional[bool] = Field(None, alias="passwordEnabled", description="True if the ISO supports password reset. Defaults to false.")
    projectid: Optional[str] = Field(None, alias="projectId", description="Register ISO for the specified project.")


class UpdateIsoRequest(APIRequest):
    id: str = Field(..., description="The ID of the ISO.")
    arch: Optional[IsoCPUArchitecture] = Field(None, description="CPU architecture: x86_64 or aarch64.")
    bootable: Optional[bool] = Field(None, description="True if the ISO is bootable.")
    cleanupdetails: Optional[bool] = Field(None, alias="cleanupDetails", description="If true, removes existing details; otherwise preserves them.")
    details: Optional[str] = Field(None, description="Key/value detail pairs formatted as details[i].keyname=keyvalue.")
    displaytext: Optional[str] = Field(None, alias="displayText", description="The display text of the ISO.")
    forceupdateostype: Optional[bool] = Field(None, alias="forceUpdateOsType", description="Force OS type update for all instances deployed with this ISO.")
    format: Optional[IsoFormat] = Field(None, description="The format of the ISO.")
    isdynamicallyscalable: Optional[bool] = Field(None, alias="isDynamicallyScalable", description="True if the ISO supports dynamic scaling via XS/VMware tools.")
    isrouting: Optional[bool] = Field(None, alias="isRouting", description="True if this ISO is used to deploy a router.")
    name: Optional[str] = Field(None, description="The name of the ISO.")
    ostypeid: Optional[str] = Field(None, alias="osTypeId", description="The ID of the OS type.")
    passwordenabled: Optional[bool] = Field(None, alias="passwordEnabled", description="True if the ISO supports password reset.")
    sortkey: Optional[int] = Field(None, alias="sortKey", description="Sort key for the ISO (integer).")
    sshkeyenabled: Optional[bool] = Field(None, alias="sshKeyEnabled", description="True if the ISO supports SSH key upload.")


class UpdateIsoPermissionsRequest(APIRequest):
    id: str = Field(..., description="The ISO ID.")
    accounts: Optional[str] = Field(None, description="Comma-delimited list of accounts within the caller's domain. Requires op parameter.")
    isextractable: Optional[bool] = Field(None, alias="isExtractable", description="True if the ISO is extractable. Can only be set by root admin.")
    isfeatured: Optional[bool] = Field(None, alias="isFeatured", description="True for featured ISO, false otherwise.")
    ispublic: Optional[bool] = Field(None, alias="isPublic", description="True for public ISO, false for private.")
    op: Optional[IsoPermissionOp] = Field(None, description="Permission operator: add, remove, or reset.")
    projectids: Optional[str] = Field(None, alias="projectIds", description="Comma-delimited list of projects. Requires op parameter.")
