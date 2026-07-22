import asyncio
from unittest.mock import AsyncMock, Mock

from acs_sdk.schemas.request.tag import (
    CreateTagsRequest,
    DeleteTagsRequest,
    ListStorageTagsRequest,
    ListTagsRequest,
)
from acs_sdk.services.tag import Tag


# ---------------------------------------------------------------------------
# create
# ---------------------------------------------------------------------------


def test_tag_create_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "createtagsresponse": {"success": "true"},
    }

    tag = Tag(client=mock_client)
    payload = CreateTagsRequest(resourceIds=["vm-1"], resourceType="UserVm", tags={"env": "prod"})
    response = tag.create(payload)

    assert response.data == {"success": "true"}
    mock_client.call.assert_called_once_with("createTags", payload.model_dump(exclude_none=True))


def test_tag_create_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(return_value={"createtagsresponse": {"success": "true"}})

    tag = Tag(client=mock_client)
    payload = CreateTagsRequest(resourceIds=["vm-1"], resourceType="UserVm", tags={"env": "prod"})
    response = asyncio.run(tag.create_async(payload))

    assert response.data == {"success": "true"}
    mock_client.call_async.assert_called_once_with(
        "createTags", payload.model_dump(exclude_none=True)
    )


# ---------------------------------------------------------------------------
# delete
# ---------------------------------------------------------------------------


def test_tag_delete_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "deletetagsresponse": {"success": "true"},
    }

    tag = Tag(client=mock_client)
    payload = DeleteTagsRequest(resourceIds=["vm-1"], resourceType="UserVm")
    response = tag.delete(payload)

    assert response.data == {"success": "true"}
    mock_client.call.assert_called_once_with(
        "deleteTags", {"resourceids": "vm-1", "resourcetype": "UserVm"}
    )


def test_tag_delete_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(return_value={"deletetagsresponse": {"success": "true"}})

    tag = Tag(client=mock_client)
    payload = DeleteTagsRequest(resourceIds=["vm-1"], resourceType="UserVm")
    response = asyncio.run(tag.delete_async(payload))

    assert response.data == {"success": "true"}
    mock_client.call_async.assert_called_once_with(
        "deleteTags", {"resourceids": "vm-1", "resourcetype": "UserVm"}
    )


# ---------------------------------------------------------------------------
# list_storage_tags
# ---------------------------------------------------------------------------


def test_tag_list_storage_tags_parses_list_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "liststoragetagsresponse": {
            "storagetag": [{"id": "tag-1", "name": "ssd", "poolid": "pool-1"}],
            "count": 1,
        }
    }

    tag = Tag(client=mock_client)
    payload = ListStorageTagsRequest()
    response = tag.list_storage_tags(payload)

    assert response.data == [{"id": "tag-1", "name": "ssd", "poolid": "pool-1"}]
    assert response.count == 1
    mock_client.call.assert_called_once_with(
        "listStorageTags", payload.model_dump(exclude_none=True)
    )


def test_tag_list_storage_tags_async_parses_list_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={
            "liststoragetagsresponse": {
                "storagetag": [{"id": "tag-2", "name": "nfs", "poolid": "pool-2"}],
                "count": 1,
            }
        }
    )

    tag = Tag(client=mock_client)
    payload = ListStorageTagsRequest()
    response = asyncio.run(tag.list_storage_tags_async(payload))

    assert response.data == [{"id": "tag-2", "name": "nfs", "poolid": "pool-2"}]
    assert response.count == 1
    mock_client.call_async.assert_called_once_with(
        "listStorageTags", payload.model_dump(exclude_none=True)
    )


# ---------------------------------------------------------------------------
# list
# ---------------------------------------------------------------------------


def test_tag_list_parses_list_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "listtagsresponse": {
            "tag": [{"key": "env", "value": "prod", "resourceid": "vm-1"}],
            "count": 1,
        }
    }

    tag = Tag(client=mock_client)
    payload = ListTagsRequest()
    response = tag.list(payload)

    assert response.data == [{"key": "env", "value": "prod", "resourceid": "vm-1"}]
    assert response.count == 1
    mock_client.call.assert_called_once_with("listTags", payload.model_dump(exclude_none=True))


def test_tag_list_async_parses_list_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={
            "listtagsresponse": {
                "tag": [{"key": "owner", "value": "team-a", "resourceid": "vm-2"}],
                "count": 1,
            }
        }
    )

    tag = Tag(client=mock_client)
    payload = ListTagsRequest(resourceId="vm-2")
    response = asyncio.run(tag.list_async(payload))

    assert response.data == [{"key": "owner", "value": "team-a", "resourceid": "vm-2"}]
    assert response.count == 1
    mock_client.call_async.assert_called_once_with(
        "listTags", payload.model_dump(exclude_none=True)
    )
