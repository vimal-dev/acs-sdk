import pytest
from pydantic import ValidationError

from acs_sdk.schemas.request.affinity_group import (
    CreateAffinityGroupRequest,
    DeleteAffinityGroupRequest,
    ListAffinityGroupsRequest,
    ListAffinityGroupTypesRequest,
    UpdateVMAffinityGroupRequest,
)


# ---------------------------------------------------------------------------
# CreateAffinityGroupRequest
# ---------------------------------------------------------------------------


def test_create_affinity_group_required_fields_serialize():
    req = CreateAffinityGroupRequest(name="ag-1", type="host anti-affinity")
    dumped = req.model_dump(exclude_none=True)
    assert dumped == {"name": "ag-1", "type": "host anti-affinity"}


def test_create_affinity_group_optional_fields_serialize():
    req = CreateAffinityGroupRequest(
        name="ag-1",
        type="host anti-affinity",
        account="acct1",
        description="desc",
        domainId="dom-1",
        projectId="proj-1",
    )
    dumped = req.model_dump(exclude_none=True)
    assert dumped["account"] == "acct1"
    assert dumped["description"] == "desc"
    assert dumped["domainid"] == "dom-1"
    assert dumped["projectid"] == "proj-1"


def test_create_affinity_group_missing_required_fields_raises():
    with pytest.raises(ValidationError):
        CreateAffinityGroupRequest()


# ---------------------------------------------------------------------------
# DeleteAffinityGroupRequest
# ---------------------------------------------------------------------------


def test_delete_affinity_group_by_id_serializes():
    req = DeleteAffinityGroupRequest(id="ag-1")
    dumped = req.model_dump(exclude_none=True)
    assert dumped == {"id": "ag-1"}


def test_delete_affinity_group_by_name_serializes():
    req = DeleteAffinityGroupRequest(name="ag-1")
    dumped = req.model_dump(exclude_none=True)
    assert dumped == {"name": "ag-1"}


def test_delete_affinity_group_id_and_name_mutually_exclusive_raises():
    with pytest.raises(ValidationError):
        DeleteAffinityGroupRequest(id="ag-1", name="ag-1")


# ---------------------------------------------------------------------------
# ListAffinityGroupTypesRequest
# ---------------------------------------------------------------------------


def test_list_affinity_group_types_defaults_from_pagination_mixin():
    req = ListAffinityGroupTypesRequest()
    dumped = req.model_dump(exclude_none=True)
    assert dumped["page"] == 1
    assert dumped["pagesize"] == 50


def test_list_affinity_group_types_keyword_serializes():
    req = ListAffinityGroupTypesRequest(keyword="host")
    dumped = req.model_dump(exclude_none=True)
    assert dumped["keyword"] == "host"


# ---------------------------------------------------------------------------
# ListAffinityGroupsRequest
# ---------------------------------------------------------------------------


def test_list_affinity_groups_defaults_from_pagination_mixin():
    req = ListAffinityGroupsRequest()
    dumped = req.model_dump(exclude_none=True)
    assert dumped["page"] == 1
    assert dumped["pagesize"] == 50


def test_list_affinity_groups_aliases_serialize_to_snake_case():
    req = ListAffinityGroupsRequest(
        domainId="dom-1",
        projectId="proj-1",
        isRecursive=True,
        listAll=True,
        virtualMachineId="vm-1",
    )
    dumped = req.model_dump(exclude_none=True)
    assert dumped["domainid"] == "dom-1"
    assert dumped["projectid"] == "proj-1"
    assert dumped["isrecursive"] is True
    assert dumped["listall"] is True
    assert dumped["virtualmachineid"] == "vm-1"


def test_list_affinity_groups_optional_fields_excluded_when_none():
    req = ListAffinityGroupsRequest()
    dumped = req.model_dump(exclude_none=True)
    assert "id" not in dumped
    assert "name" not in dumped
    assert "type" not in dumped


# ---------------------------------------------------------------------------
# UpdateVMAffinityGroupRequest
# ---------------------------------------------------------------------------


def test_update_vm_affinity_group_required_id_serializes():
    req = UpdateVMAffinityGroupRequest(id="vm-1")
    dumped = req.model_dump(exclude_none=True)
    assert dumped == {"id": "vm-1"}


def test_update_vm_affinity_group_ids_serializes():
    req = UpdateVMAffinityGroupRequest(id="vm-1", affinityGroupIds="ag-1,ag-2")
    dumped = req.model_dump(exclude_none=True)
    assert dumped["affinitygroupids"] == "ag-1,ag-2"


def test_update_vm_affinity_group_names_serializes():
    req = UpdateVMAffinityGroupRequest(id="vm-1", affinityGroupNames="ag-1,ag-2")
    dumped = req.model_dump(exclude_none=True)
    assert dumped["affinitygroupnames"] == "ag-1,ag-2"


def test_update_vm_affinity_group_ids_and_names_mutually_exclusive_raises():
    with pytest.raises(ValidationError):
        UpdateVMAffinityGroupRequest(id="vm-1", affinityGroupIds="ag-1", affinityGroupNames="ag-2")


def test_update_vm_affinity_group_missing_id_raises():
    with pytest.raises(ValidationError):
        UpdateVMAffinityGroupRequest()
