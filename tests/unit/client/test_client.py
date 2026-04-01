import pytest
import httpx

from acs_sdk.client.client import ApacheCloudStackClient
from acs_sdk.schemas.config import ApacheCloudStackConfig


# 🔹 Helper: create mock config
@pytest.fixture
def config():
    return ApacheCloudStackConfig(
        api_endpoint="https://api.cloudstack.example.com/client/api",
        api_key="testkey",
        api_secret="testsecret",
        timeout=30,
    )


# 🔹 Helper: mock transport
def mock_transport(handler):
    return httpx.MockTransport(handler)


SUCCESS_JSON_RESPONSE = {"Status": "OK", "CommandResponse": {"TestResult": "Success"}}


# ---------------------------------------------------
# SUCCESS CASE
# ---------------------------------------------------


def test_call_success(config):
    def handler(request: httpx.Request):
        assert request.method == "GET"

        # ensure params were attached
        assert request.url.params["command"] == "test.command"
        # assert request.url.params["ApiUser"] == "testuser"

        return httpx.Response(200, json=SUCCESS_JSON_RESPONSE)

    client = httpx.Client(
        base_url=config.endpoint, timeout=config.timeout, transport=mock_transport(handler)
    )
    nc = ApacheCloudStackClient(config, client=client)

    response = nc.call("test.command", {"foo": "bar"})

    assert response["Status"] == "OK"
    assert response["CommandResponse"]["TestResult"] == "Success"


# ---------------------------------------------------
# HTTP ERROR
# ---------------------------------------------------


def test_http_error(config):
    def handler(request: httpx.Request):
        return httpx.Response(500, text="Server Error")

    client = httpx.Client(
        base_url=config.endpoint, timeout=config.timeout, transport=mock_transport(handler)
    )
    nc = ApacheCloudStackClient(config, client=client)

    with pytest.raises(httpx.HTTPStatusError):
        nc.call("test.command")


# ---------------------------------------------------
# PARAM MERGING
# ---------------------------------------------------


def test_params_merging(config):
    def handler(request: httpx.Request):
        params = request.url.params

        # custom param
        assert params["foo"] == "bar"

        # required params
        assert params["command"] == "test.command"

        return httpx.Response(200, json=SUCCESS_JSON_RESPONSE)

    client = httpx.Client(
        base_url=config.endpoint, timeout=config.timeout, transport=mock_transport(handler)
    )
    nc = ApacheCloudStackClient(config, client=client)

    nc.call("test.command", {"foo": "bar"})


# ---------------------------------------------------
# EMPTY PARAMS
# ---------------------------------------------------


def test_call_without_params(config):
    def handler(request: httpx.Request):
        params = request.url.params

        assert params["command"] == "test.command"
        return httpx.Response(200, json=SUCCESS_JSON_RESPONSE)

    client = httpx.Client(
        base_url=config.endpoint, timeout=config.timeout, transport=mock_transport(handler)
    )
    nc = ApacheCloudStackClient(config, client=client)

    response = nc.call("test.command")

    assert response["Status"] == "OK"


# ---------------------------------------------------
# CLOSE CLIENT
# ---------------------------------------------------


def test_close(config):
    client = httpx.Client()
    nc = ApacheCloudStackClient(config, client=client)

    nc.close()

    assert client.is_closed is True
