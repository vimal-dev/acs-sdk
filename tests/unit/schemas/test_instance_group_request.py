import pytest
from pydantic import ValidationError

from acs_sdk.schemas.request.instance_group import (
    CreateInstanceGroupRequest,
    DeleteInstanceGroupRequest,
    ListInstanceGroupsRequest,
    UpdateInstanceGroupRequest,
)


# ---------------------------------------------------------------------------
# CreateInstanceGroupRequest
# ---------------------------------------------------------------------------

def test_create_instance_group_required_name_serializes():
    req = CreateInstanceGroupRequest(name="web")
    dumped = req.model_dump(exclude_none=True)
    assert dumped == {"name": "web"}


def test_create_instance_group_optional_scoping_fields_serialize():
    req = CreateInstanceGroupRequest(name="web", account="acct1", domainId="dom-1", projectId="proj-1")
    dumped = req.model_dump(exclude_none=True)
    assert dumped["account"] == "acct1"
    assert dumped["domainid"] == "dom-1"
    assert dumped["projectid"] == "proj-1"


def test_create_instance_group_missing_name_raises():
    with pytest.raises(ValidationError):
        CreateInstanceGroupRequest()


# ---------------------------------------------------------------------------
# UpdateInstanceGroupRequest
# ---------------------------------------------------------------------------

def test_update_instance_group_required_id_serializes():
    req = UpdateInstanceGroupRequest(id="grp-1")
    dumped = req.model_dump(exclude_none=True)
    assert dumped == {"id": "grp-1"}


def test_update_instance_group_name_serializes():
    req = UpdateInstanceGroupRequest(id="grp-1", name="web-updated")
    dumped = req.model_dump(exclude_none=True)
    assert dumped["name"] == "web-updated"


def test_update_instance_group_missing_id_raises():
    with pytest.raises(ValidationError):
        UpdateInstanceGroupRequest()


# ---------------------------------------------------------------------------
# DeleteInstanceGroupRequest
# ---------------------------------------------------------------------------

def test_delete_instance_group_required_id_serializes():
    req = DeleteInstanceGroupRequest(id="grp-1")
    dumped = req.model_dump(exclude_none=True)
    assert dumped == {"id": "grp-1"}


def test_delete_instance_group_missing_id_raises():
    with pytest.raises(ValidationError):
        DeleteInstanceGroupRequest()


# ---------------------------------------------------------------------------
# ListInstanceGroupsRequest
# ---------------------------------------------------------------------------

def test_list_instance_groups_defaults_from_pagination_mixin():
    req = ListInstanceGroupsRequest()
    dumped = req.model_dump(exclude_none=True)
    assert dumped["page"] == 1
    assert dumped["pagesize"] == 50


def test_list_instance_groups_domainid_alias():
    req = ListInstanceGroupsRequest(domainId="dom-1")
    dumped = req.model_dump(exclude_none=True)
    assert dumped["domainid"] == "dom-1"


def test_list_instance_groups_projectid_alias():
    req = ListInstanceGroupsRequest(projectId="proj-1")
    dumped = req.model_dump(exclude_none=True)
    assert dumped["projectid"] == "proj-1"


def test_list_instance_groups_optional_fields_excluded_when_none():
    req = ListInstanceGroupsRequest()
    dumped = req.model_dump(exclude_none=True)
    assert "id" not in dumped
    assert "name" not in dumped
    assert "keyword" not in dumped
