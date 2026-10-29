import asyncio
import inspect
from unittest.mock import AsyncMock, patch

import httpx
import pytest

from acs_sdk.core.retry import RetryConfig, is_retryable, with_retry

REQUEST = httpx.Request("GET", "https://cs.example.com/client/api")


def status_error(code: int) -> httpx.HTTPStatusError:
    return httpx.HTTPStatusError(
        "error", request=REQUEST, response=httpx.Response(code, request=REQUEST)
    )


@pytest.mark.parametrize(
    "exc, expected",
    [
        (httpx.ConnectError("refused", request=REQUEST), True),
        (httpx.ConnectTimeout("timeout", request=REQUEST), True),
        (httpx.PoolTimeout("pool", request=REQUEST), True),
        (httpx.ReadTimeout("read", request=REQUEST), False),
        (status_error(429), True),
        (status_error(502), True),
        (status_error(503), True),
        (status_error(504), False),
        (status_error(401), False),
        (status_error(431), False),
        (status_error(530), False),
        (ValueError("boom"), False),
    ],
)
def test_is_retryable(exc, expected):
    assert is_retryable(exc) is expected


class Flaky:
    def __init__(self, errors, retry=None):
        self.errors = list(errors)
        self.calls = 0
        self.retry = retry or RetryConfig(retries=3, backoff=0.5)

    @with_retry
    def sync(self):
        self.calls += 1
        if self.errors:
            raise self.errors.pop(0)
        return "ok"

    @with_retry
    async def async_(self):
        self.calls += 1
        if self.errors:
            raise self.errors.pop(0)
        return "ok"


def test_sync_retries_transient_then_succeeds():
    flaky = Flaky([status_error(503), status_error(503)])
    with patch("acs_sdk.core.retry.time.sleep") as sleep:
        assert flaky.sync() == "ok"
    assert flaky.calls == 3
    assert [c.args[0] for c in sleep.call_args_list] == [0.5, 1.0]


def test_sync_does_not_retry_business_error():
    flaky = Flaky([status_error(431)])
    with patch("acs_sdk.core.retry.time.sleep") as sleep:
        with pytest.raises(httpx.HTTPStatusError):
            flaky.sync()
    assert flaky.calls == 1
    sleep.assert_not_called()


def test_sync_gives_up_after_max_attempts():
    flaky = Flaky([status_error(503)] * 5)
    with patch("acs_sdk.core.retry.time.sleep"):
        with pytest.raises(httpx.HTTPStatusError):
            flaky.sync()
    assert flaky.calls == 3


def test_async_retries_transient_then_succeeds():
    flaky = Flaky([httpx.ConnectError("refused", request=REQUEST)])
    sleep = AsyncMock()
    with patch("acs_sdk.core.retry.asyncio.sleep", new=sleep):
        assert asyncio.run(flaky.async_()) == "ok"
    assert flaky.calls == 2
    sleep.assert_awaited_once_with(0.5)


def test_async_does_not_retry_business_error():
    flaky = Flaky([status_error(401)])
    with patch("acs_sdk.core.retry.asyncio.sleep", new=AsyncMock()) as sleep:
        with pytest.raises(httpx.HTTPStatusError):
            asyncio.run(flaky.async_())
    assert flaky.calls == 1
    sleep.assert_not_awaited()


def test_custom_retry_statuses():
    flaky = Flaky([status_error(504)], retry=RetryConfig(retry_on=(504,)))
    with patch("acs_sdk.core.retry.time.sleep"):
        assert flaky.sync() == "ok"
    assert flaky.calls == 2


def test_wraps_preserves_metadata():
    assert Flaky.sync.__name__ == "sync"
    assert inspect.iscoroutinefunction(Flaky.async_)
