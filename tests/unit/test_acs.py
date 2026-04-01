from acs_sdk.acs import ApacheCloudStack, ApacheCloudStackClient


def test_import():
    assert ApacheCloudStack is not None


# ---------------------------------------------------
# Test Initialization
# ---------------------------------------------------
def test_intialization(config):
    acs = ApacheCloudStack(config)
    assert acs.config == config
    assert isinstance(acs.client, ApacheCloudStackClient)
