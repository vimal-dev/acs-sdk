# schemas/request/tag.py
from typing import Any, Dict, List, Optional

from pydantic import Field, field_serializer

from acs_sdk.schemas.request.base import APIRequest, PaginationMixin


def _flatten_tags(data: Dict[str, Any]) -> Dict[str, Any]:
    tags = data.pop("tags", None)
    if tags:
        for idx, (key, value) in enumerate(tags.items()):
            data[f"tags[{idx}].key"] = key
            data[f"tags[{idx}].value"] = value
    return data


class CreateTagsRequest(APIRequest):
    resourceids: List[str] = Field(
        ..., alias="resourceIds", description="List of resources to create the tags for"
    )
    resourcetype: str = Field(..., alias="resourceType", description="Type of the resource")
    tags: Dict[str, str] = Field(..., description="Map of tags (key/value pairs)")
    customer: Optional[str] = Field(
        None,
        description="Identifies client-specific tags; when populated, the tag cannot be used by CloudStack internally",
    )

    @field_serializer("resourceids")
    def serialize_csv(self, value: List[str]) -> str:
        return ",".join(value)

    def model_dump(self, *args, **kwargs) -> Dict[str, Any]:
        data = super().model_dump(*args, **kwargs)
        return _flatten_tags(data)


class DeleteTagsRequest(APIRequest):
    resourceids: List[str] = Field(
        ..., alias="resourceIds", description="Delete tags for resource id(s)"
    )
    resourcetype: str = Field(..., alias="resourceType", description="Delete tag by resource type")
    tags: Optional[Dict[str, str]] = Field(None, description="Delete tags matching key/value pairs")

    @field_serializer("resourceids")
    def serialize_csv(self, value: List[str]) -> str:
        return ",".join(value)

    def model_dump(self, *args, **kwargs) -> Dict[str, Any]:
        data = super().model_dump(*args, **kwargs)
        return _flatten_tags(data)


class ListStorageTagsRequest(APIRequest, PaginationMixin):
    keyword: Optional[str] = Field(None, description="List by keyword")


class ListTagsRequest(APIRequest, PaginationMixin):
    account: Optional[str] = Field(
        None, description="List resources by account. Must be used with the domainId parameter."
    )
    customer: Optional[str] = Field(None, description="List by customer name")
    domainid: Optional[str] = Field(
        None, alias="domainId", description="List only resources belonging to the domain specified"
    )
    isrecursive: Optional[bool] = Field(
        False,
        alias="isRecursive",
        description="Defaults to false, but if true, lists all resources from the parent specified by the domainId till leaves.",
    )
    key: Optional[str] = Field(None, description="List by key")
    keyword: Optional[str] = Field(None, description="List by keyword")
    listall: Optional[bool] = Field(
        False,
        alias="listAll",
        description="If set to false, list only resources belonging to the command's caller; if set to true - list resources that the caller is authorized to see.",
    )
    projectid: Optional[str] = Field(
        None,
        alias="projectId",
        description="List objects by project; if projectid=-1 lists All VMs",
    )
    resourceid: Optional[str] = Field(None, alias="resourceId", description="List by resource id")
    resourcetype: Optional[str] = Field(
        None, alias="resourceType", description="List by resource type"
    )
    value: Optional[str] = Field(None, description="List by value")
