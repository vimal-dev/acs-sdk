from pydantic import ValidationError
import pytest

from acs_sdk.acs import ApacheCloudStack, ApacheCloudStackClient


def test_import():
    assert ApacheCloudStack is not None


# ---------------------------------------------------
# Test Initialization
# ---------------------------------------------------
def test_intialization(config):
    acs = ApacheCloudStack(config)
    assert isinstance(acs.client, ApacheCloudStackClient)


def test_get_service_client_region(config):
    """Test that region service is correctly loaded and cached."""
    acs = ApacheCloudStack(config)
    acs_region = acs.region
    assert acs_region is not None
    assert isinstance(acs_region.client, ApacheCloudStackClient)


def test_get_service_client_job(config):
    """Test that job service is correctly loaded and cached."""
    acs = ApacheCloudStack(config)
    acs_job = acs.job
    assert acs_job is not None
    assert isinstance(acs_job.client, ApacheCloudStackClient)


def test_service_caching(config):
    """Test that services are cached and reused on subsequent accesses."""
    acs = ApacheCloudStack(config)
    region_first_access = acs.region
    region_second_access = acs.region
    # Same instance should be returned from cache
    assert region_first_access is region_second_access


def test_invalid_service_raises_attribute_error(config):
    """Test that accessing an invalid service raises AttributeError."""
    acs = ApacheCloudStack(config)
    with pytest.raises(AttributeError) as exc_info:
        acs.invalid_service
    assert "invalid_service not found" in str(exc_info.value)
