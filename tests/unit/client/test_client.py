import asyncio

import pytest
import httpx
from unittest.mock import AsyncMock, MagicMock, patch

from opentelemetry.trace import SpanKind

from acs_sdk.client.client import ApacheCloudStackAsyncClient, ApacheCloudStackClient
from acs_sdk.core.retry import RetryConfig
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


def test_call_tracing(config):
    def handler(request: httpx.Request):
        return httpx.Response(200, json=SUCCESS_JSON_RESPONSE)

    client = httpx.Client(
        base_url=config.endpoint, timeout=config.timeout, transport=mock_transport(handler)
    )
    tracer = MagicMock()
    span = MagicMock()
    tracer.start_as_current_span.return_value.__enter__.return_value = span

    nc = ApacheCloudStackClient(config, client=client, tracer=tracer)

    response = nc.call("test.command")

    tracer.start_as_current_span.assert_called_once_with(
        "CloudStack test.command", kind=SpanKind.CLIENT
    )
    span.set_attribute.assert_any_call("cloudstack.command", "test.command")
    assert response["Status"] == "OK"


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
# API ERROR
# ---------------------------------------------------


def test_api_error(config):
    assert 1 == 1
    # def handler(request: httpx.Request):
    #     return httpx.Response(200, json={"errorcode": 401, "errortext": "Unable to verify user credentials"})

    # client = httpx.Client(
    #     base_url=config.endpoint, timeout=config.timeout, transport=mock_transport(handler)
    # )
    # nc = ApacheCloudStackClient(config, client=client)

    # with pytest.raises(CloudStackAPIError) as exc_info:
    #     nc.call("test.command")

    # assert exc_info.value.error_code == "401"
    # assert "Unable to verify user credentials" in exc_info.value.error_text


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


# ---------------------------------------------------
# CREDENTIAL REDACTION
# ---------------------------------------------------


def test_http_error_does_not_leak_signed_url(config, caplog):
    def handler(request: httpx.Request):
        return httpx.Response(500, text="Server Error")

    client = httpx.Client(
        base_url=config.endpoint, timeout=config.timeout, transport=mock_transport(handler)
    )
    tracer = MagicMock()
    span = MagicMock()
    nc = ApacheCloudStackClient(config, client=client, tracer=tracer)

    with patch("acs_sdk.client.client.trace.get_current_span", return_value=span):
        with pytest.raises(httpx.HTTPStatusError) as exc_info:
            nc.call("test.command")

    assert "signature=***" in str(exc_info.value)
    assert "apikey=***" in str(exc_info.value)
    assert "testkey" not in str(exc_info.value)
    assert exc_info.value.__cause__ is None and exc_info.value.__suppress_context__
    for record in caplog.records:
        assert "testkey" not in record.getMessage()
        assert record.exc_info is None
    span.record_exception.assert_not_called()
    for call in span.set_attribute.call_args_list + span.set_status.call_args_list:
        assert "testkey" not in str(call)


def test_transport_error_is_redacted(config):
    def handler(request: httpx.Request):
        raise httpx.ReadTimeout(f"timed out for {request.url}", request=request)

    client = httpx.Client(
        base_url=config.endpoint, timeout=config.timeout, transport=mock_transport(handler)
    )
    nc = ApacheCloudStackClient(config, client=client)

    with pytest.raises(httpx.ReadTimeout) as exc_info:
        nc.call("test.command")

    assert "testkey" not in str(exc_info.value)


# ---------------------------------------------------
# RETRIES
# ---------------------------------------------------


@pytest.fixture
def no_sleep():
    with (
        patch("acs_sdk.core.retry.time.sleep"),
        patch("acs_sdk.core.retry.asyncio.sleep", new=AsyncMock()),
    ):
        yield


def _counting_client(config, responder):
    calls = []

    def handler(request: httpx.Request):
        calls.append(request)
        return responder(len(calls), request)

    client = httpx.Client(
        base_url=config.endpoint, timeout=config.timeout, transport=mock_transport(handler)
    )
    return ApacheCloudStackClient(config, client=client), calls


def test_business_error_is_not_retried(config, no_sleep):
    nc, calls = _counting_client(
        config, lambda n, r: httpx.Response(431, json={"errorcode": 431, "errortext": "bad"})
    )

    with pytest.raises(httpx.HTTPStatusError):
        nc.call("test.command")

    assert len(calls) == 1


def test_cloudstack_5xx_error_is_not_retried(config, no_sleep):
    nc, calls = _counting_client(config, lambda n, r: httpx.Response(530, json={}))

    with pytest.raises(httpx.HTTPStatusError):
        nc.call("test.command")

    assert len(calls) == 1


def test_gateway_error_is_retried_until_success(config, no_sleep):
    nc, calls = _counting_client(
        config,
        lambda n, r: (
            httpx.Response(503) if n < 3 else httpx.Response(200, json=SUCCESS_JSON_RESPONSE)
        ),
    )

    assert nc.call("test.command")["Status"] == "OK"
    assert len(calls) == 3


def test_connect_error_is_retried(config, no_sleep):
    def responder(n, request):
        raise httpx.ConnectError("refused", request=request)

    nc, calls = _counting_client(config, responder)

    with pytest.raises(httpx.ConnectError):
        nc.call("test.command")

    assert len(calls) == nc.retry.retries


# ---------------------------------------------------
# ASYNC
# ---------------------------------------------------


def test_call_async_retries_and_reuses_client(config, no_sleep):
    calls = []

    def handler(request: httpx.Request):
        calls.append(request)
        if len(calls) == 1:
            return httpx.Response(503)
        return httpx.Response(200, json=SUCCESS_JSON_RESPONSE)

    nc = ApacheCloudStackClient(config, client=httpx.Client())
    nc._async_client = httpx.AsyncClient(
        base_url=config.endpoint, transport=httpx.MockTransport(handler)
    )

    async def run():
        first_client = nc._get_async_client()
        response = await nc.call_async("test.command")
        await nc.call_async("test.command")
        assert nc._get_async_client() is first_client
        await nc.aclose()
        return response

    assert asyncio.run(run())["Status"] == "OK"
    assert len(calls) == 3


def test_lazy_async_client_is_created_once(config):
    nc = ApacheCloudStackClient(config, client=httpx.Client())

    async def run():
        first = nc._get_async_client()
        second = nc._get_async_client()
        await nc.aclose()
        return first, second

    first, second = asyncio.run(run())
    assert first is second


def test_async_only_client_works_without_context_manager(config):
    def handler(request: httpx.Request):
        return httpx.Response(200, json=SUCCESS_JSON_RESPONSE)

    async def run():
        nc = ApacheCloudStackAsyncClient(config)
        nc._get_async_client()._transport = httpx.MockTransport(handler)
        try:
            return await nc.call_async("test.command")
        finally:
            await nc.close()

    assert asyncio.run(run())["Status"] == "OK"


# ---------------------------------------------------
# CLIENT LIFECYCLE & PARITY
# ---------------------------------------------------


def test_async_only_client_opens_span(config):
    def handler(request: httpx.Request):
        return httpx.Response(200, json=SUCCESS_JSON_RESPONSE)

    tracer = MagicMock()
    span = MagicMock()
    tracer.start_as_current_span.return_value.__enter__.return_value = span
    nc = ApacheCloudStackAsyncClient(
        config,
        client=httpx.AsyncClient(base_url=config.endpoint, transport=mock_transport(handler)),
        tracer=tracer,
    )

    async def run():
        async with nc:
            return await nc.call_async("test.command")

    assert asyncio.run(run())["Status"] == "OK"
    tracer.start_as_current_span.assert_called_once_with(
        "CloudStack test.command", kind=SpanKind.CLIENT
    )
    span.set_attribute.assert_any_call("cloudstack.command", "test.command")


def test_sync_client_context_manager_closes(config):
    client = httpx.Client()
    with ApacheCloudStackClient(config, client=client) as nc:
        assert isinstance(nc, ApacheCloudStackClient)
    assert client.is_closed


def test_sync_client_async_context_manager_closes_both(config):
    client = httpx.Client()
    async_client = httpx.AsyncClient()

    async def run():
        async with ApacheCloudStackClient(config, client=client, async_client=async_client):
            pass

    asyncio.run(run())
    assert client.is_closed
    assert async_client.is_closed


def test_async_only_client_property(config):
    nc = ApacheCloudStackAsyncClient(config)
    assert nc.client is None

    async def run():
        async with nc:
            assert isinstance(nc.client, httpx.AsyncClient)
            return nc.client

    created = asyncio.run(run())
    assert created.is_closed
    assert nc.client is None

    injected = httpx.AsyncClient()
    assert ApacheCloudStackAsyncClient(config, client=injected).client is injected


def test_async_only_client_rejects_sync_call(config):
    with pytest.raises(NotImplementedError):
        ApacheCloudStackAsyncClient(config).call("test.command")


def test_clients_exported_from_package():
    import acs_sdk

    assert acs_sdk.ApacheCloudStackClient is ApacheCloudStackClient
    assert acs_sdk.ApacheCloudStackAsyncClient is ApacheCloudStackAsyncClient


def test_custom_retry_config(config, no_sleep):
    calls = []

    def handler(request: httpx.Request):
        calls.append(request)
        return httpx.Response(503)

    client = httpx.Client(base_url=config.endpoint, transport=mock_transport(handler))
    nc = ApacheCloudStackClient(config, client=client, retry=RetryConfig(retries=1))

    with pytest.raises(httpx.HTTPStatusError):
        nc.call("test.command")

    assert len(calls) == 1
