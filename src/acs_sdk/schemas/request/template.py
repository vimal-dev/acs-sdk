from typing import Literal, Optional

from pydantic import Field

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
