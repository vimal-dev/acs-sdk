from acs_sdk.schemas.request.virtual_machine import DeployVirtualMachineRequest


def test_deploy_virtual_machine_request_flattens_iptonetworklist():
    request = DeployVirtualMachineRequest(
        serviceofferingid="so-1",
        zoneid="zone-1",
        iptonetworklist=[
            {"networkid": "net-1", "ip": "10.0.0.5"},
            {"networkid": "net-2", "ip": "10.0.0.6"},
        ],
    )

    dumped = request.model_dump()

    assert "iptonetworklist" not in dumped
    assert dumped["iptonetworklist[0].networkid"] == "net-1"
    assert dumped["iptonetworklist[0].ip"] == "10.0.0.5"
    assert dumped["iptonetworklist[1].networkid"] == "net-2"
    assert dumped["iptonetworklist[1].ip"] == "10.0.0.6"


def test_deploy_virtual_machine_request_flattens_datadisksdetails():
    request = DeployVirtualMachineRequest(
        serviceofferingid="so-1",
        zoneid="zone-1",
        datadisksdetails=[
            {"diskofferingid": "do-1", "size": "50"},
        ],
    )

    dumped = request.model_dump()

    assert "datadisksdetails" not in dumped
    assert dumped["datadisksdetails[0].diskofferingid"] == "do-1"
    assert dumped["datadisksdetails[0].size"] == "50"
