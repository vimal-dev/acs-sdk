import asyncio
from typing import Any, Dict, Optional

import httpx
import pytest
from pydantic import BaseModel

from acs_sdk.client.contract import ClientContract
from acs_sdk.core.response_mapper import ResponseMapper
from acs_sdk.exceptions import CloudStackAPIError
from acs_sdk.services.base import BaseService


class DummyPayload(BaseModel):
    field: Optional[str] = None


class DummyClient(ClientContract):
    def __init__(self, sync_response: Dict[str, Any], async_response: Dict[str, Any]):
        self.sync_response = sync_response
        self.async_response = async_response
        self.last_command: Optional[str] = None
        self.last_params: Optional[Dict[str, Any]] = None
        self.called_sync = False
        self.called_async = False

    def call(self, command: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        self.called_sync = True
        self.last_command = command
        self.last_params = params
        return self.sync_response

    async def call_async(
        self, command: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        self.called_async = True
        self.last_command = command
        self.last_params = params
        return self.async_response

    def close(self) -> None:
        return None


class CustomMapper(ResponseMapper):
    def __init__(self):
        self.called_with: Optional[tuple[Dict[str, Any], str]] = None

    def extract(self, response: Dict[str, Any], envelope: str) -> Dict[str, Any]:
        self.called_with = (response, envelope)
        return {"mapped": response.get(envelope, {})}


def test_extract_response_uses_custom_response_mapper():
    mapper = CustomMapper()
    client = DummyClient(sync_response={"test": "value"}, async_response={})
    service = BaseService(client, response_mapper=mapper)

    extracted = service._extract_response({"envelope": {"id": 42}}, "envelope")

    assert mapper.called_with == ({"envelope": {"id": 42}}, "envelope")
    assert extracted == {"mapped": {"id": 42}}


def test_wrap_with_list_entity_returns_list_api_response():
    response_data = {"items": [{"id": 1}, {"id": 2}], "count": 2}

    api_response = BaseService._wrap(response_data, entity="items")

    assert api_response.data == [{"id": 1}, {"id": 2}]
    assert api_response.count == 2
    assert api_response.is_ok is True


def test_wrap_with_single_entity_returns_dict_api_response():
    response_data = {"item": {"id": 1, "name": "alice"}}

    api_response = BaseService._wrap(response_data, entity="item")

    assert api_response.data == {"id": 1, "name": "alice"}
    assert api_response.count is None
    assert api_response.is_ok is True


def test_wrap_with_missing_entity_returns_none_data():
    response_data = {}

    api_response = BaseService._wrap(response_data, entity="missing")

    assert api_response.data is None
    assert api_response.count is None
    assert api_response.is_ok is True


def test_wrap_without_entity_returns_raw_response_data():
    response_data = {"status": "ok"}

    api_response = BaseService._wrap(response_data, entity=None)

    assert api_response.data == response_data
    assert api_response.count is None


def test_execute_calls_client_and_wraps_list_response():
    client = DummyClient(
        sync_response={"envelope": {"items": [{"id": 1}], "count": 1}},
        async_response={},
    )
    service = BaseService(client)
    payload = DummyPayload(field=None)

    api_response = service._execute("list.items", payload, envelope="envelope", entity="items")

    assert client.called_sync is True
    assert client.last_command == "list.items"
    assert client.last_params == {}
    assert api_response.data == [{"id": 1}]
    assert api_response.count == 1


def test_execute_with_single_entity_returns_dict_response():
    client = DummyClient(
        sync_response={"envelope": {"item": {"id": 2}}},
        async_response={},
    )
    service = BaseService(client)
    payload = DummyPayload(field="value")

    api_response = service._execute("get.item", payload, envelope="envelope", entity="item")

    assert client.called_sync is True
    assert client.last_command == "get.item"
    assert client.last_params == {"field": "value"}
    assert api_response.data == {"id": 2}
    assert api_response.count is None


def test_execute_async_calls_client_and_wraps_single_entity():
    client = DummyClient(
        sync_response={},
        async_response={"envelope": {"item": {"id": 3}}},
    )
    service = BaseService(client)
    payload = DummyPayload(field="async")

    api_response = asyncio.run(
        service._execute_async("get.async.item", payload, envelope="envelope", entity="item")
    )

    assert client.called_async is True
    assert client.last_command == "get.async.item"
    assert client.last_params == {"field": "async"}
    assert api_response.data == {"id": 3}
    assert api_response.count is None


class RaisingClient(DummyClient):
    def __init__(self, error):
        super().__init__(sync_response={}, async_response={})
        self.error = error

    def call(self, command, params=None):
        raise self.error

    async def call_async(self, command, params=None):
        raise self.error


def _status_error(response: httpx.Response) -> httpx.HTTPStatusError:
    response.request = httpx.Request("GET", "https://cs.example.com/client/api")
    return httpx.HTTPStatusError("error", request=response.request, response=response)


def test_execute_non_json_error_body_keeps_status_and_text():
    error = _status_error(httpx.Response(502, text="<html>Bad Gateway</html>"))
    service = BaseService(RaisingClient(error))

    with pytest.raises(CloudStackAPIError) as exc_info:
        service._execute("listZones", DummyPayload(), envelope="listzonesresponse")

    assert exc_info.value.error_code == 502
    assert "Bad Gateway" in exc_info.value.error_text


def test_execute_async_non_json_error_body_keeps_status_and_text():
    error = _status_error(httpx.Response(503, text="Service Unavailable"))
    service = BaseService(RaisingClient(error))

    with pytest.raises(CloudStackAPIError) as exc_info:
        asyncio.run(
            service._execute_async("listZones", DummyPayload(), envelope="listzonesresponse")
        )

    assert exc_info.value.error_code == 503
    assert exc_info.value.error_text == "Service Unavailable"


def test_execute_json_error_body_uses_cloudstack_error():
    body = {"listzonesresponse": {"errorcode": 431, "cserrorcode": 9999, "errortext": "bad id"}}
    service = BaseService(RaisingClient(_status_error(httpx.Response(431, json=body))))

    with pytest.raises(CloudStackAPIError) as exc_info:
        service._execute("listZones", DummyPayload(), envelope="listzonesresponse")

    assert exc_info.value.error_code == 9999
    assert exc_info.value.error_text == "bad id"


def test_execute_json_error_without_details_falls_back_to_status():
    service = BaseService(RaisingClient(_status_error(httpx.Response(500, json={}))))

    with pytest.raises(CloudStackAPIError) as exc_info:
        service._execute("listZones", DummyPayload(), envelope="listzonesresponse")

    assert exc_info.value.error_code == 500
    assert exc_info.value.error_text == "Internal Server Error"
