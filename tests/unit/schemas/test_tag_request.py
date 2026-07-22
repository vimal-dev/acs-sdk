import pytest
from pydantic import ValidationError

from acs_sdk.schemas.request.tag import (
    CreateTagsRequest,
    DeleteTagsRequest,
    ListStorageTagsRequest,
    ListTagsRequest,
)


# ---------------------------------------------------------------------------
# CreateTagsRequest
# ---------------------------------------------------------------------------

def test_create_tags_required_fields_serialize():
    req = CreateTagsRequest(
        resourceIds=["vm-1", "vm-2"],
        resourceType="UserVm",
        tags={"env": "prod"},
    )
    dumped = req.model_dump(exclude_none=True)
    assert dumped == {
        "resourceids": "vm-1,vm-2",
        "resourcetype": "UserVm",
        "tags[0].key": "env",
        "tags[0].value": "prod",
    }


def test_create_tags_multiple_tags_flatten_indexed():
    req = CreateTagsRequest(
        resourceIds=["vm-1"],
        resourceType="UserVm",
        tags={"env": "prod", "owner": "team-a"},
    )
    dumped = req.model_dump(exclude_none=True)
    assert dumped["tags[0].key"] == "env"
    assert dumped["tags[0].value"] == "prod"
    assert dumped["tags[1].key"] == "owner"
    assert dumped["tags[1].value"] == "team-a"


def test_create_tags_customer_serializes():
    req = CreateTagsRequest(
        resourceIds=["vm-1"],
        resourceType="UserVm",
        tags={"env": "prod"},
        customer="acme",
    )
    dumped = req.model_dump(exclude_none=True)
    assert dumped["customer"] == "acme"


def test_create_tags_missing_required_fields_raises():
    with pytest.raises(ValidationError):
        CreateTagsRequest()


# ---------------------------------------------------------------------------
# DeleteTagsRequest
# ---------------------------------------------------------------------------

def test_delete_tags_required_fields_serialize():
    req = DeleteTagsRequest(resourceIds=["vm-1"], resourceType="UserVm")
    dumped = req.model_dump(exclude_none=True)
    assert dumped == {"resourceids": "vm-1", "resourcetype": "UserVm"}


def test_delete_tags_with_tags_filter_flattens():
    req = DeleteTagsRequest(
        resourceIds=["vm-1", "vm-2"],
        resourceType="UserVm",
        tags={"env": "prod"},
    )
    dumped = req.model_dump(exclude_none=True)
    assert dumped["resourceids"] == "vm-1,vm-2"
    assert dumped["tags[0].key"] == "env"
    assert dumped["tags[0].value"] == "prod"


def test_delete_tags_missing_required_fields_raises():
    with pytest.raises(ValidationError):
        DeleteTagsRequest()


# ---------------------------------------------------------------------------
# ListStorageTagsRequest
# ---------------------------------------------------------------------------

def test_list_storage_tags_defaults_from_pagination_mixin():
    req = ListStorageTagsRequest()
    dumped = req.model_dump(exclude_none=True)
    assert dumped["page"] == 1
    assert dumped["pagesize"] == 50


def test_list_storage_tags_keyword_serializes():
    req = ListStorageTagsRequest(keyword="nfs")
    dumped = req.model_dump(exclude_none=True)
    assert dumped["keyword"] == "nfs"


# ---------------------------------------------------------------------------
# ListTagsRequest
# ---------------------------------------------------------------------------

def test_list_tags_defaults_from_pagination_mixin():
    req = ListTagsRequest()
    dumped = req.model_dump(exclude_none=True)
    assert dumped["page"] == 1
    assert dumped["pagesize"] == 50


def test_list_tags_aliases_serialize_to_snake_case():
    req = ListTagsRequest(
        domainId="dom-1",
        projectId="proj-1",
        isRecursive=True,
        listAll=True,
        resourceId="vm-1",
        resourceType="UserVm",
    )
    dumped = req.model_dump(exclude_none=True)
    assert dumped["domainid"] == "dom-1"
    assert dumped["projectid"] == "proj-1"
    assert dumped["isrecursive"] is True
    assert dumped["listall"] is True
    assert dumped["resourceid"] == "vm-1"
    assert dumped["resourcetype"] == "UserVm"


def test_list_tags_optional_fields_excluded_when_none():
    req = ListTagsRequest()
    dumped = req.model_dump(exclude_none=True)
    assert "key" not in dumped
    assert "value" not in dumped
    assert "customer" not in dumped
