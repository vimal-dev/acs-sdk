from typing import Any, Dict, List, Literal, Optional

from pydantic import Field, field_serializer

from .base import APIRequest, PaginationMixin


TemplateFilter = Literal[
    "featured",
    "self",
    "selfexecutable",
    "sharedexecutable",
    "executable",
    "community",
    "all",
]


TemplateCPUArchitecture = Literal[
    "x86_64",
    "aarch64",
]


TemplateFormat = Literal[
    "QCOW2",
    "RAW",
    "VHD",
    "VHDX",
    "OVA",
    "VMDK",
    "ISO",
    "TAR",
    "BAREMETAL",
]


ExtractMode = Literal[
    "HTTP_DOWNLOAD",
    "FTP_UPLOAD",
]


TemplatePermissionOp = Literal[
    "add",
    "remove",
    "reset",
]


TemplateHypervisor = Literal[
    "KVM",
    "VMware",
    "XenServer",
    "HyperV",
    "BareMetal",
    "LXC",
    "OVM",
    "Simulator",
]


def _flatten_details(data: Dict[str, Any]) -> Dict[str, Any]:
    """Flatten a details map into CloudStack's ``details[0].<key>=<value>`` form."""
    details = data.pop("details", None)
    if details:
        for key, value in details.items():
            data[f"details[0].{key}"] = value
    return data


class ListTemplatesRequest(APIRequest, PaginationMixin):
    templatefilter: TemplateFilter = Field(
        ..., alias="templateFilter", description="Template filter type."
    )

    account: Optional[str] = Field(
        None, description="List resources by account. Must be used with domainid."
    )
    arch: Optional[TemplateCPUArchitecture] = Field(
        None, description="CPU architecture (x86_64 or aarch64)."
    )
    details: Optional[str] = Field(
        None, description="Comma-separated list of template details (all, min)."
    )
    domainid: Optional[str] = Field(
        None, alias="domainId", description="List only resources belonging to the domain specified."
    )
    extensionid: Optional[str] = Field(
        None,
        alias="extensionId",
        description="Identifier for the extension associated with the template.",
    )
    forcks: Optional[bool] = Field(
        None, alias="forCKS", description="List templates usable for CKS cluster deployments."
    )
    hypervisor: Optional[TemplateHypervisor] = Field(
        None, description="Hypervisor type to filter by."
    )
    id: Optional[str] = Field(None, description="The template identifier.")
    ids: Optional[list[str]] = Field(
        None, description="Multiple template identifiers (mutually exclusive with id)."
    )
    imagestoreid: Optional[str] = Field(
        None, alias="imageStoreId", description="Image or image cache store identifier."
    )
    isready: Optional[bool] = Field(
        None, alias="isReady", description="Only return templates ready for deployment."
    )
    isrecursive: Optional[bool] = Field(
        None,
        alias="isRecursive",
        description="If true, lists all resources from parent domain till leaves.",
    )
    isvnf: Optional[bool] = Field(None, alias="isVNF", description="Whether to list VNF templates.")
    keyword: Optional[str] = Field(None, description="List by keyword.")
    listall: Optional[bool] = Field(
        None, alias="listAll", description="If true, lists all resources available to the caller."
    )
    name: Optional[str] = Field(None, description="The template name.")
    oscategoryid: Optional[str] = Field(
        None, alias="osCategoryId", description="Operating system category identifier."
    )
    parenttemplateid: Optional[str] = Field(
        None,
        alias="parentTemplateId",
        description="Parent template identifier for datadisk templates.",
    )
    projectid: Optional[str] = Field(
        None, alias="projectId", description="Project identifier; -1 lists all items."
    )
    showicon: Optional[bool] = Field(
        None, alias="showIcon", description="Display resource image for templates."
    )
    showremoved: Optional[bool] = Field(
        None, alias="showRemoved", description="Include removed templates in results."
    )
    showunique: Optional[bool] = Field(
        None, alias="showUnique", description="List only unique templates across zones."
    )
    storageid: Optional[str] = Field(
        None, alias="storageId", description="Storage pool identifier."
    )
    tags: Optional[str] = Field(None, description="List resources by tags (key/value pairs).")
    templatetype: Optional[str] = Field(
        None, alias="templateType", description="The template classification."
    )
    zoneid: Optional[str] = Field(
        None, alias="zoneId", description="Zone identifier for filtering."
    )


class ListTemplatePermissionsRequest(APIRequest):
    id: str = Field(..., description="The template ID.")


class CopyTemplateRequest(APIRequest):
    id: str = Field(..., description="The ID of the template to copy.")
    destzoneid: Optional[str] = Field(
        None, alias="destZoneId", description="ID of the zone the template is being copied to."
    )
    destzoneids: Optional[List[str]] = Field(
        None,
        alias="destZoneIds",
        description="List of zone IDs to copy the template to. Mutually exclusive with destzoneid.",
    )
    sourcezoneid: Optional[str] = Field(
        None,
        alias="sourceZoneId",
        description="ID of the zone the template is currently hosted on. "
        "If not specified, the template is copied from any zone it is available in.",
    )

    @field_serializer("destzoneids")
    def serialize_csv(self, value: Optional[List[str]]) -> Optional[str]:
        return ",".join(value) if value is not None else None


class CreateTemplateRequest(APIRequest):
    displaytext: str = Field(
        ..., alias="displayText", description="The display text of the template."
    )
    name: str = Field(..., description="The name of the template.")
    ostypeid: str = Field(
        ..., alias="osTypeId", description="The ID of the OS type that best represents the OS."
    )
    account: Optional[str] = Field(
        None, description="An optional account for the template. Must be used with domainid."
    )
    arch: Optional[TemplateCPUArchitecture] = Field(
        None, description="CPU architecture (x86_64 or aarch64)."
    )
    bits: Optional[int] = Field(None, description="32 or 64 bit.")
    details: Optional[Dict[str, str]] = Field(
        None, description="Template details as key/value pairs."
    )
    domainid: Optional[str] = Field(
        None, alias="domainId", description="An optional domain ID. Must be used with account."
    )
    isdynamicallyscalable: Optional[bool] = Field(
        None,
        alias="isDynamicallyScalable",
        description="True if the template supports dynamic scaling via XS/VMware tools.",
    )
    isfeatured: Optional[bool] = Field(
        None, alias="isFeatured", description="True if this template is a featured template."
    )
    ispublic: Optional[bool] = Field(
        None, alias="isPublic", description="True if this template is a public template."
    )
    passwordenabled: Optional[bool] = Field(
        None,
        alias="passwordEnabled",
        description="True if the template supports the password reset feature.",
    )
    projectid: Optional[str] = Field(
        None, alias="projectId", description="Create template for the project."
    )
    requireshvm: Optional[bool] = Field(
        None, alias="requiresHvm", description="True if the template requires HVM."
    )
    snapshotid: Optional[str] = Field(
        None,
        alias="snapshotId",
        description="The ID of the snapshot the template is being created from. "
        "Either this or volumeid must be passed in.",
    )
    sshkeyenabled: Optional[bool] = Field(
        None, alias="sshKeyEnabled", description="True if the template supports SSH key upload."
    )
    templatetag: Optional[str] = Field(
        None, alias="templateTag", description="The tag for this template."
    )
    url: Optional[str] = Field(
        None, description="Optional; overrides the URL the template is extracted to."
    )
    virtualmachineid: Optional[str] = Field(
        None,
        alias="virtualMachineId",
        description="Optional VM ID. If specified, the VM's metadata is used for the template.",
    )
    volumeid: Optional[str] = Field(
        None,
        alias="volumeId",
        description="The ID of the disk volume the template is being created from. "
        "Either this or snapshotid must be passed in.",
    )
    zoneid: Optional[str] = Field(
        None, alias="zoneId", description="The zone for the template (snapshot-based only)."
    )

    def model_dump(self, *args, **kwargs) -> Dict[str, Any]:
        data = super().model_dump(*args, **kwargs)
        return _flatten_details(data)


class DeleteTemplateRequest(APIRequest):
    id: str = Field(..., description="The ID of the template.")
    forced: Optional[bool] = Field(
        None, description="Force delete the template even if it is used by VMs."
    )
    zoneid: Optional[str] = Field(
        None,
        alias="zoneId",
        description="The ID of the zone. If not specified, the template is deleted from all zones.",
    )


class ExtractTemplateRequest(APIRequest):
    id: str = Field(..., description="The ID of the template.")
    mode: ExtractMode = Field(
        ..., description="The mode of extraction - HTTP_DOWNLOAD or FTP_UPLOAD."
    )
    url: Optional[str] = Field(
        None, description="The URL to which the template would be extracted."
    )
    zoneid: Optional[str] = Field(
        None,
        alias="zoneId",
        description="The ID of the zone where the template is originally located.",
    )


class GetUploadParamsForTemplateRequest(APIRequest):
    displaytext: str = Field(
        ..., alias="displayText", description="The display text of the template."
    )
    format: TemplateFormat = Field(..., description="The format for the template.")
    hypervisor: TemplateHypervisor = Field(
        ..., description="The target hypervisor for the template."
    )
    name: str = Field(..., description="The name of the template.")
    zoneid: str = Field(
        ..., alias="zoneId", description="The ID of the zone the template is to be hosted on."
    )
    account: Optional[str] = Field(
        None, description="An optional account name. Must be used with domainid."
    )
    arch: Optional[TemplateCPUArchitecture] = Field(
        None, description="CPU architecture (x86_64 or aarch64)."
    )
    bits: Optional[int] = Field(None, description="32 or 64 bits support. 64 by default.")
    checksum: Optional[str] = Field(
        None, description="The checksum value of the template, with algorithm prefix."
    )
    details: Optional[Dict[str, str]] = Field(
        None, description="Template details as key/value pairs."
    )
    domainid: Optional[str] = Field(
        None, alias="domainId", description="An optional domain ID. Must be used with account."
    )
    isdynamicallyscalable: Optional[bool] = Field(
        None,
        alias="isDynamicallyScalable",
        description="True if the template supports dynamic scaling via XS/VMware tools.",
    )
    isextractable: Optional[bool] = Field(
        None,
        alias="isExtractable",
        description="True if the template or its derivatives are extractable.",
    )
    isfeatured: Optional[bool] = Field(
        None, alias="isFeatured", description="True if this template is a featured template."
    )
    ispublic: Optional[bool] = Field(
        None, alias="isPublic", description="True if the template is available to all accounts."
    )
    isrouting: Optional[bool] = Field(
        None, alias="isRouting", description="True if the template type is routing."
    )
    ostypeid: Optional[str] = Field(
        None, alias="osTypeId", description="The ID of the OS type that best represents the OS."
    )
    passwordenabled: Optional[bool] = Field(
        None,
        alias="passwordEnabled",
        description="True if the template supports the password reset feature.",
    )
    projectid: Optional[str] = Field(
        None, alias="projectId", description="Upload template for the project."
    )
    requireshvm: Optional[bool] = Field(
        None, alias="requiresHvm", description="True if this template requires HVM."
    )
    sshkeyenabled: Optional[bool] = Field(
        None, alias="sshKeyEnabled", description="True if the template supports SSH key upload."
    )
    templatetag: Optional[str] = Field(
        None, alias="templateTag", description="The tag for this template."
    )

    def model_dump(self, *args, **kwargs) -> Dict[str, Any]:
        data = super().model_dump(*args, **kwargs)
        return _flatten_details(data)


class PrepareTemplateRequest(APIRequest):
    templateid: str = Field(
        ..., alias="templateId", description="Template ID of the template to be prepared."
    )
    zoneid: str = Field(
        ...,
        alias="zoneId",
        description="Zone ID of the template to be prepared in primary storage(s).",
    )
    storageid: Optional[str] = Field(
        None,
        alias="storageId",
        description="Storage pool ID of the primary storage pool to prepare the template in.",
    )


class RegisterTemplateRequest(APIRequest):
    displaytext: str = Field(
        ..., alias="displayText", description="The display text of the template."
    )
    format: TemplateFormat = Field(..., description="The format for the template.")
    hypervisor: TemplateHypervisor = Field(
        ..., description="The target hypervisor for the template."
    )
    name: str = Field(..., description="The name of the template.")
    url: str = Field(..., description="The URL of where the template is hosted.")
    account: Optional[str] = Field(
        None, description="An optional account name. Must be used with domainid."
    )
    arch: Optional[TemplateCPUArchitecture] = Field(
        None, description="CPU architecture (x86_64 or aarch64)."
    )
    bits: Optional[int] = Field(None, description="32 or 64 bits support. 64 by default.")
    checksum: Optional[str] = Field(
        None, description="The checksum value of the template, with algorithm prefix."
    )
    deployasis: Optional[bool] = Field(
        None,
        alias="deployAsIs",
        description="(VMware only) True if VM deployments should preserve OVF settings.",
    )
    details: Optional[Dict[str, str]] = Field(
        None, description="Template details as key/value pairs."
    )
    directdownload: Optional[bool] = Field(
        None,
        alias="directDownload",
        description="True if the template should bypass secondary storage "
        "and be downloaded directly to primary storage.",
    )
    domainid: Optional[str] = Field(
        None, alias="domainId", description="An optional domain ID. Must be used with account."
    )
    forcks: Optional[bool] = Field(
        None, alias="forCKS", description="True if the template is for CKS cluster deployments."
    )
    isdynamicallyscalable: Optional[bool] = Field(
        None,
        alias="isDynamicallyScalable",
        description="True if the template supports dynamic scaling via XS/VMware tools.",
    )
    isextractable: Optional[bool] = Field(
        None,
        alias="isExtractable",
        description="True if the template or its derivatives are extractable.",
    )
    isfeatured: Optional[bool] = Field(
        None, alias="isFeatured", description="True if this template is a featured template."
    )
    ispublic: Optional[bool] = Field(
        None, alias="isPublic", description="True if the template is available to all accounts."
    )
    isrouting: Optional[bool] = Field(
        None, alias="isRouting", description="True if the template type is routing."
    )
    ostypeid: Optional[str] = Field(
        None, alias="osTypeId", description="The ID of the OS type that best represents the OS."
    )
    passwordenabled: Optional[bool] = Field(
        None,
        alias="passwordEnabled",
        description="True if the template supports the password reset feature.",
    )
    projectid: Optional[str] = Field(
        None, alias="projectId", description="Register template for the project."
    )
    requireshvm: Optional[bool] = Field(
        None, alias="requiresHvm", description="True if this template requires HVM."
    )
    sshkeyenabled: Optional[bool] = Field(
        None, alias="sshKeyEnabled", description="True if the template supports SSH key upload."
    )
    templatetag: Optional[str] = Field(
        None, alias="templateTag", description="The tag for this template."
    )
    templatetype: Optional[str] = Field(
        None, alias="templateType", description="The type of the template (e.g. USER, ROUTING)."
    )
    zoneid: Optional[str] = Field(
        None,
        alias="zoneId",
        description="The ID of the zone the template is to be hosted on (-1 for all zones).",
    )
    zoneids: Optional[List[str]] = Field(
        None,
        alias="zoneIds",
        description="List of zone IDs the template is to be hosted on.",
    )

    @field_serializer("zoneids")
    def serialize_csv(self, value: Optional[List[str]]) -> Optional[str]:
        return ",".join(value) if value is not None else None

    def model_dump(self, *args, **kwargs) -> Dict[str, Any]:
        data = super().model_dump(*args, **kwargs)
        return _flatten_details(data)


class UpdateTemplateRequest(APIRequest):
    id: str = Field(..., description="The ID of the template.")
    arch: Optional[TemplateCPUArchitecture] = Field(
        None, description="CPU architecture (x86_64 or aarch64)."
    )
    bootable: Optional[bool] = Field(
        None, description="True if the image is bootable, false otherwise."
    )
    cleanupdetails: Optional[bool] = Field(
        None,
        alias="cleanupDetails",
        description="If true, removes existing template details; otherwise preserves them.",
    )
    details: Optional[Dict[str, str]] = Field(
        None, description="Template details as key/value pairs."
    )
    displaytext: Optional[str] = Field(
        None, alias="displayText", description="The display text of the template."
    )
    forcks: Optional[bool] = Field(
        None, alias="forCKS", description="True if the template is for CKS cluster deployments."
    )
    format: Optional[TemplateFormat] = Field(None, description="The format for the template.")
    isdynamicallyscalable: Optional[bool] = Field(
        None,
        alias="isDynamicallyScalable",
        description="True if the template supports dynamic scaling via XS/VMware tools.",
    )
    isrouting: Optional[bool] = Field(
        None, alias="isRouting", description="True if the template type is routing."
    )
    name: Optional[str] = Field(None, description="The name of the template.")
    ostypeid: Optional[str] = Field(
        None, alias="osTypeId", description="The ID of the OS type that best represents the OS."
    )
    passwordenabled: Optional[bool] = Field(
        None,
        alias="passwordEnabled",
        description="True if the template supports the password reset feature.",
    )
    requireshvm: Optional[bool] = Field(
        None, alias="requiresHvm", description="True if the template requires HVM."
    )
    sortkey: Optional[int] = Field(
        None, alias="sortKey", description="Sort key of the template (integer)."
    )
    sshkeyenabled: Optional[bool] = Field(
        None, alias="sshKeyEnabled", description="True if the template supports SSH key upload."
    )
    templatetag: Optional[str] = Field(
        None, alias="templateTag", description="The tag for this template."
    )
    templatetype: Optional[str] = Field(
        None, alias="templateType", description="The type of the template (e.g. USER, ROUTING)."
    )

    def model_dump(self, *args, **kwargs) -> Dict[str, Any]:
        data = super().model_dump(*args, **kwargs)
        return _flatten_details(data)


class UpdateTemplatePermissionsRequest(APIRequest):
    id: str = Field(..., description="The template ID.")
    accounts: Optional[List[str]] = Field(
        None,
        description="List of accounts within the caller's domain. Requires the op parameter.",
    )
    isextractable: Optional[bool] = Field(
        None,
        alias="isExtractable",
        description="True if the template is extractable. Can only be set by root admin.",
    )
    isfeatured: Optional[bool] = Field(
        None, alias="isFeatured", description="True for featured template, false otherwise."
    )
    ispublic: Optional[bool] = Field(
        None, alias="isPublic", description="True for public template, false for private."
    )
    op: Optional[TemplatePermissionOp] = Field(
        None, description="Permission operator: add, remove, or reset."
    )
    projectids: Optional[List[str]] = Field(
        None,
        alias="projectIds",
        description="List of project IDs. Requires the op parameter.",
    )

    @field_serializer("accounts", "projectids")
    def serialize_csv(self, value: Optional[List[str]]) -> Optional[str]:
        return ",".join(value) if value is not None else None
