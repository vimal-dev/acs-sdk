import asyncio
from unittest.mock import AsyncMock, Mock

from acs_sdk.schemas.request.affinity_group import (
    CreateAffinityGroupRequest,
    DeleteAffinityGroupRequest,
    ListAffinityGroupsRequest,
    ListAffinityGroupTypesRequest,
    UpdateVMAffinityGroupRequest,
)
from acs_sdk.services.affinity_group import AffinityGroup


# ---------------------------------------------------------------------------
# create
# ---------------------------------------------------------------------------


def test_affinity_group_create_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "createaffinitygroupresponse": {"id": "ag-1", "name": "ag-1"},
    }

    ag = AffinityGroup(client=mock_client)
    payload = CreateAffinityGroupRequest(name="ag-1", type="host anti-affinity")
    response = ag.create(payload)

    assert response.data == {"id": "ag-1", "name": "ag-1"}
    mock_client.call.assert_called_once_with(
        "createAffinityGroup", payload.model_dump(exclude_none=True)
    )


def test_affinity_group_create_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={"createaffinitygroupresponse": {"id": "ag-1", "name": "ag-1"}}
    )

    ag = AffinityGroup(client=mock_client)
    payload = CreateAffinityGroupRequest(name="ag-1", type="host anti-affinity")
    response = asyncio.run(ag.create_async(payload))

    assert response.data == {"id": "ag-1", "name": "ag-1"}
    mock_client.call_async.assert_called_once_with(
        "createAffinityGroup", payload.model_dump(exclude_none=True)
    )


# ---------------------------------------------------------------------------
# delete
# ---------------------------------------------------------------------------


def test_affinity_group_delete_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "deleteaffinitygroupresponse": {"success": "true"},
    }

    ag = AffinityGroup(client=mock_client)
    payload = DeleteAffinityGroupRequest(id="ag-1")
    response = ag.delete(payload)

    assert response.data == {"success": "true"}
    mock_client.call.assert_called_once_with("deleteAffinityGroup", {"id": "ag-1"})


def test_affinity_group_delete_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={"deleteaffinitygroupresponse": {"success": "true"}}
    )

    ag = AffinityGroup(client=mock_client)
    payload = DeleteAffinityGroupRequest(id="ag-1")
    response = asyncio.run(ag.delete_async(payload))

    assert response.data == {"success": "true"}
    mock_client.call_async.assert_called_once_with("deleteAffinityGroup", {"id": "ag-1"})


# ---------------------------------------------------------------------------
# list_types
# ---------------------------------------------------------------------------


def test_affinity_group_list_types_parses_list_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "listaffinitygrouptypesresponse": {
            "affinitygrouptype": [{"type": "host anti-affinity"}],
            "count": 1,
        }
    }

    ag = AffinityGroup(client=mock_client)
    payload = ListAffinityGroupTypesRequest()
    response = ag.list_types(payload)

    assert response.data == [{"type": "host anti-affinity"}]
    assert response.count == 1
    mock_client.call.assert_called_once_with(
        "listAffinityGroupTypes", payload.model_dump(exclude_none=True)
    )


def test_affinity_group_list_types_async_parses_list_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={
            "listaffinitygrouptypesresponse": {
                "affinitygrouptype": [{"type": "host affinity"}],
                "count": 1,
            }
        }
    )

    ag = AffinityGroup(client=mock_client)
    payload = ListAffinityGroupTypesRequest()
    response = asyncio.run(ag.list_types_async(payload))

    assert response.data == [{"type": "host affinity"}]
    assert response.count == 1
    mock_client.call_async.assert_called_once_with(
        "listAffinityGroupTypes", payload.model_dump(exclude_none=True)
    )


# ---------------------------------------------------------------------------
# list
# ---------------------------------------------------------------------------


def test_affinity_group_list_parses_list_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "listaffinitygroupsresponse": {
            "affinitygroup": [{"id": "ag-1", "name": "ag-1"}],
            "count": 1,
        }
    }

    ag = AffinityGroup(client=mock_client)
    payload = ListAffinityGroupsRequest()
    response = ag.list(payload)

    assert response.data == [{"id": "ag-1", "name": "ag-1"}]
    assert response.count == 1
    mock_client.call.assert_called_once_with(
        "listAffinityGroups", payload.model_dump(exclude_none=True)
    )


def test_affinity_group_list_async_parses_list_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={
            "listaffinitygroupsresponse": {
                "affinitygroup": [{"id": "ag-2", "name": "ag-2"}],
                "count": 1,
            }
        }
    )

    ag = AffinityGroup(client=mock_client)
    payload = ListAffinityGroupsRequest(name="ag-2")
    response = asyncio.run(ag.list_async(payload))

    assert response.data == [{"id": "ag-2", "name": "ag-2"}]
    assert response.count == 1
    mock_client.call_async.assert_called_once_with(
        "listAffinityGroups", payload.model_dump(exclude_none=True)
    )


# ---------------------------------------------------------------------------
# update_vm_affinity_group
# ---------------------------------------------------------------------------


def test_affinity_group_update_vm_affinity_group_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "updatevmaffinitygroupresponse": {"id": "vm-1", "name": "vm-1"},
    }

    ag = AffinityGroup(client=mock_client)
    payload = UpdateVMAffinityGroupRequest(id="vm-1", affinityGroupIds="ag-1")
    response = ag.update_vm_affinity_group(payload)

    assert response.data == {"id": "vm-1", "name": "vm-1"}
    mock_client.call.assert_called_once_with(
        "updateVMAffinityGroup", payload.model_dump(exclude_none=True)
    )


def test_affinity_group_update_vm_affinity_group_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={"updatevmaffinitygroupresponse": {"id": "vm-1", "name": "vm-1"}}
    )

    ag = AffinityGroup(client=mock_client)
    payload = UpdateVMAffinityGroupRequest(id="vm-1", affinityGroupNames="ag-1")
    response = asyncio.run(ag.update_vm_affinity_group_async(payload))

    assert response.data == {"id": "vm-1", "name": "vm-1"}
    mock_client.call_async.assert_called_once_with(
        "updateVMAffinityGroup", payload.model_dump(exclude_none=True)
    )
