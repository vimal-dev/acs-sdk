import asyncio
from unittest.mock import AsyncMock, Mock

from acs_sdk.schemas.request.console_session import (
    CreateConsoleEndpointRequest,
    ListConsoleSessionsRequest,
)
from acs_sdk.services.console_session import ConsoleSession


# ---------------------------------------------------------------------------
# create_endpoint
# ---------------------------------------------------------------------------


def test_console_session_create_endpoint_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "createconsoleendpointresponse": {
            "success": "true",
            "url": "https://host/console?token=abc",
        },
    }

    cs = ConsoleSession(client=mock_client)
    payload = CreateConsoleEndpointRequest(virtualMachineId="vm-1")
    response = cs.create_endpoint(payload)

    assert response.data == {"success": "true", "url": "https://host/console?token=abc"}
    mock_client.call.assert_called_once_with(
        "createConsoleEndpoint", payload.model_dump(exclude_none=True)
    )


def test_console_session_create_endpoint_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={
            "createconsoleendpointresponse": {
                "success": "true",
                "url": "https://host/console?token=abc",
            },
        }
    )

    cs = ConsoleSession(client=mock_client)
    payload = CreateConsoleEndpointRequest(virtualMachineId="vm-1", token="tok-1")
    response = asyncio.run(cs.create_endpoint_async(payload))

    assert response.data == {"success": "true", "url": "https://host/console?token=abc"}
    mock_client.call_async.assert_called_once_with(
        "createConsoleEndpoint", payload.model_dump(exclude_none=True)
    )


# ---------------------------------------------------------------------------
# list
# ---------------------------------------------------------------------------


def test_console_session_list_parses_list_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "listconsolesessionsresponse": {
            "consolesession": [{"id": "sess-1", "virtualmachineid": "vm-1"}],
            "count": 1,
        }
    }

    cs = ConsoleSession(client=mock_client)
    payload = ListConsoleSessionsRequest()
    response = cs.list(payload)

    assert response.data == [{"id": "sess-1", "virtualmachineid": "vm-1"}]
    assert response.count == 1
    mock_client.call.assert_called_once_with(
        "listConsoleSessions", payload.model_dump(exclude_none=True)
    )


def test_console_session_list_async_parses_list_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={
            "listconsolesessionsresponse": {
                "consolesession": [{"id": "sess-2", "virtualmachineid": "vm-2"}],
                "count": 1,
            }
        }
    )

    cs = ConsoleSession(client=mock_client)
    payload = ListConsoleSessionsRequest(virtualMachineId="vm-2")
    response = asyncio.run(cs.list_async(payload))

    assert response.data == [{"id": "sess-2", "virtualmachineid": "vm-2"}]
    assert response.count == 1
    mock_client.call_async.assert_called_once_with(
        "listConsoleSessions", payload.model_dump(exclude_none=True)
    )
