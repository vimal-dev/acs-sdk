import pytest

from acs_sdk.schemas.config import ApacheCloudStackConfig


@pytest.fixture
def config():
    return ApacheCloudStackConfig(
        api_endpoint="https://api.cloudstack.example.com/client/api",
        api_key="testkey",
        api_secret="testsecret",
    )
