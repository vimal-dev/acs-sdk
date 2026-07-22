import asyncio
from unittest.mock import AsyncMock, Mock

from acs_sdk.schemas.request.instance_group import (
    CreateInstanceGroupRequest,
    DeleteInstanceGroupRequest,
    ListInstanceGroupsRequest,
    UpdateInstanceGroupRequest,
)
from acs_sdk.services.instance_group import InstanceGroup


# ---------------------------------------------------------------------------
# list
# ---------------------------------------------------------------------------


def test_instance_group_list_parses_list_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "listinstancegroupsresponse": {
            "instancegroup": [{"id": "grp-1", "name": "web"}],
            "count": 1,
        }
    }

    ig = InstanceGroup(client=mock_client)
    payload = ListInstanceGroupsRequest()
    response = ig.list(payload)

    assert response.data == [{"id": "grp-1", "name": "web"}]
    assert response.count == 1
    mock_client.call.assert_called_once_with(
        "listInstanceGroups", payload.model_dump(exclude_none=True)
    )


def test_instance_group_list_async_parses_list_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={
            "listinstancegroupsresponse": {
                "instancegroup": [{"id": "grp-2", "name": "db"}],
                "count": 1,
            }
        }
    )

    ig = InstanceGroup(client=mock_client)
    payload = ListInstanceGroupsRequest(name="db")
    response = asyncio.run(ig.list_async(payload))

    assert response.data == [{"id": "grp-2", "name": "db"}]
    assert response.count == 1
    mock_client.call_async.assert_called_once_with(
        "listInstanceGroups", payload.model_dump(exclude_none=True)
    )


# ---------------------------------------------------------------------------
# create
# ---------------------------------------------------------------------------


def test_instance_group_create_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "createinstancegroupresponse": {"id": "grp-new", "name": "web"},
    }

    ig = InstanceGroup(client=mock_client)
    payload = CreateInstanceGroupRequest(name="web")
    response = ig.create(payload)

    assert response.data == {"id": "grp-new", "name": "web"}
    mock_client.call.assert_called_once_with(
        "createInstanceGroup", payload.model_dump(exclude_none=True)
    )


def test_instance_group_create_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={
            "createinstancegroupresponse": {"id": "grp-new", "name": "web"},
        }
    )

    ig = InstanceGroup(client=mock_client)
    payload = CreateInstanceGroupRequest(name="web")
    response = asyncio.run(ig.create_async(payload))

    assert response.data == {"id": "grp-new", "name": "web"}
    mock_client.call_async.assert_called_once_with(
        "createInstanceGroup", payload.model_dump(exclude_none=True)
    )


# ---------------------------------------------------------------------------
# update
# ---------------------------------------------------------------------------


def test_instance_group_update_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "updateinstancegroupresponse": {"id": "grp-1", "name": "web-updated"},
    }

    ig = InstanceGroup(client=mock_client)
    payload = UpdateInstanceGroupRequest(id="grp-1", name="web-updated")
    response = ig.update(payload)

    assert response.data == {"id": "grp-1", "name": "web-updated"}
    mock_client.call.assert_called_once_with(
        "updateInstanceGroup", payload.model_dump(exclude_none=True)
    )


def test_instance_group_update_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={
            "updateinstancegroupresponse": {"id": "grp-1", "name": "web-updated"},
        }
    )

    ig = InstanceGroup(client=mock_client)
    payload = UpdateInstanceGroupRequest(id="grp-1", name="web-updated")
    response = asyncio.run(ig.update_async(payload))

    assert response.data == {"id": "grp-1", "name": "web-updated"}
    mock_client.call_async.assert_called_once_with(
        "updateInstanceGroup", payload.model_dump(exclude_none=True)
    )


# ---------------------------------------------------------------------------
# delete
# ---------------------------------------------------------------------------


def test_instance_group_delete_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "deleteinstancegroupresponse": {"success": "true"},
    }

    ig = InstanceGroup(client=mock_client)
    payload = DeleteInstanceGroupRequest(id="grp-1")
    response = ig.delete(payload)

    assert response.data == {"success": "true"}
    mock_client.call.assert_called_once_with("deleteInstanceGroup", {"id": "grp-1"})


def test_instance_group_delete_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={"deleteinstancegroupresponse": {"success": "true"}}
    )

    ig = InstanceGroup(client=mock_client)
    payload = DeleteInstanceGroupRequest(id="grp-1")
    response = asyncio.run(ig.delete_async(payload))

    assert response.data == {"success": "true"}
    mock_client.call_async.assert_called_once_with("deleteInstanceGroup", {"id": "grp-1"})
