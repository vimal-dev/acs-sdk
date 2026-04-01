from acs_sdk.schemas.config import ApacheCloudStackConfig
from pydantic import ValidationError
import pytest


def test_valid_config(config):
    assert config.api_endpoint == "https://api.cloudstack.example.com/client/api"
    assert config.api_key == "testkey"
    assert config.api_secret == "testsecret"
    assert config.timeout == 30


def test_config_defaults():
    cfg = ApacheCloudStackConfig(
        api_endpoint="https://api.cloudstack.example.com/client/api",
        api_key="k",
        api_secret="k",
        timeout=30,
    )
    assert cfg.timeout == 30


def test_config_api_endpoint():
    cfg = ApacheCloudStackConfig(
        api_endpoint="https://api.cloudstack.example.com/client/api",
        api_key="k",
        api_secret="k",
        timeout=30,
    )
    assert cfg.endpoint == "https://api.cloudstack.example.com/client/api"


def test_invalid_timeout():
    from pydantic import ValidationError

    with pytest.raises(ValidationError):
        ApacheCloudStackConfig(
            api_endpoint="https://api.cloudstack.example.com/client/api",
            api_key="key",
            api_secret="secret",
            timeout="abc",
        )
    with pytest.raises(ValidationError):
        ApacheCloudStackConfig(
            api_endpoint="https://api.cloudstack.example.com/client/api",
            api_key="key",
            api_secret="secret",
            timeout="abc",
        )


def test_config_missing_fields():
    from pydantic import ValidationError

    with pytest.raises(ValidationError):
        ApacheCloudStackConfig()


def test_config_serialization(config):
    data = config.model_dump()
    assert "endpoint" in data
    assert data["endpoint"].startswith("https://")


@pytest.mark.parametrize(
    "field,value",
    [
        ("api_key", 123),
        ("api_secret", 123),
        ("timeout", "-10"),
    ],
)
def test_invalid_types(field, value):
    data = {
        "api_key": "key",
        "api_secret": "secret",
        "timeout": 30,
        field: value,
    }

    with pytest.raises(ValidationError):
        ApacheCloudStackConfig(**data)


@pytest.mark.parametrize(
    "field",
    ["api_endpoint", "api_key", "api_secret"],
)
def test_missing_required_fields(field):
    data = {
        "api_endpoint": "https://api.cloudstack.example.com/client/api",
        "api_key": "key",
        "api_secret": "secret",
        "timeout": 30,
    }

    data.pop(field)

    with pytest.raises(ValidationError):
        ApacheCloudStackConfig(**data)
