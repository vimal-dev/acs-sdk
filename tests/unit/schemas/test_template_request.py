import pytest
from pydantic import ValidationError

from acs_sdk.schemas.request.template import (
    CopyTemplateRequest,
    CreateTemplateRequest,
    ExtractTemplateRequest,
    GetUploadParamsForTemplateRequest,
    PrepareTemplateRequest,
    RegisterTemplateRequest,
    UpdateTemplatePermissionsRequest,
    UpdateTemplateRequest,
)


def _register(**kwargs):
    base = dict(displayText="d", format="QCOW2", hypervisor="KVM", name="n", url="http://x")
    base.update(kwargs)
    return RegisterTemplateRequest(**base)


def test_register_aliases_serialize_to_lowercase():
    dumped = _register(zoneId="z-1", osTypeId="os-1", isPublic=True).model_dump(exclude_none=True)
    assert dumped == {
        "displaytext": "d",
        "format": "QCOW2",
        "hypervisor": "KVM",
        "name": "n",
        "url": "http://x",
        "zoneid": "z-1",
        "ostypeid": "os-1",
        "ispublic": True,
    }


def test_register_zoneids_csv_and_details_flattened():
    dumped = _register(zoneIds=["a", "b"], details={"rootDiskController": "scsi"}).model_dump(
        exclude_none=True
    )
    assert dumped["zoneids"] == "a,b"
    assert dumped["details[0].rootDiskController"] == "scsi"
    assert "details" not in dumped


def test_register_invalid_format_raises():
    with pytest.raises(ValidationError):
        _register(format="EXE")


def test_register_missing_required_raises():
    with pytest.raises(ValidationError):
        RegisterTemplateRequest(name="n", url="http://x")


def test_create_requires_displaytext_name_ostype():
    with pytest.raises(ValidationError):
        CreateTemplateRequest(name="n")
    req = CreateTemplateRequest(displayText="d", name="n", osTypeId="os", snapshotId="s")
    assert req.model_dump(exclude_none=True)["snapshotid"] == "s"


def test_copy_destzoneids_csv():
    dumped = CopyTemplateRequest(id="t", destZoneIds=["z1", "z2"]).model_dump(exclude_none=True)
    assert dumped == {"id": "t", "destzoneids": "z1,z2"}


def test_extract_invalid_mode_raises():
    with pytest.raises(ValidationError):
        ExtractTemplateRequest(id="t", mode="SCP")


def test_get_upload_params_required_fields():
    with pytest.raises(ValidationError):
        GetUploadParamsForTemplateRequest(name="n", zoneId="z")
    req = GetUploadParamsForTemplateRequest(
        displayText="d", format="OVA", hypervisor="VMware", name="n", zoneId="z"
    )
    assert req.model_dump(exclude_none=True)["zoneid"] == "z"


def test_prepare_aliases():
    dumped = PrepareTemplateRequest(templateId="t", zoneId="z", storageId="p").model_dump(
        exclude_none=True
    )
    assert dumped == {"templateid": "t", "zoneid": "z", "storageid": "p"}


def test_update_details_flattened():
    dumped = UpdateTemplateRequest(id="t", details={"a": "1"}, cleanupDetails=False).model_dump(
        exclude_none=True
    )
    assert dumped == {"id": "t", "details[0].a": "1", "cleanupdetails": False}


def test_update_permissions_lists_and_op():
    dumped = UpdateTemplatePermissionsRequest(
        id="t", op="remove", projectIds=["p1", "p2"]
    ).model_dump(exclude_none=True)
    assert dumped == {"id": "t", "op": "remove", "projectids": "p1,p2"}
    with pytest.raises(ValidationError):
        UpdateTemplatePermissionsRequest(id="t", op="grant")
