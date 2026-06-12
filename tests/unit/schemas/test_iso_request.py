import pytest
from pydantic import ValidationError

from acs_sdk.schemas.request.iso import (
    AttachIsoRequest,
    CopyIsoRequest,
    DeleteIsoRequest,
    DetachIsoRequest,
    ExtractIsoRequest,
    GetUploadParamsForIsoRequest,
    ListIsoPermissionsRequest,
    ListIsosRequest,
    RegisterIsoRequest,
    UpdateIsoRequest,
    UpdateIsoPermissionsRequest,
)


# ---------------------------------------------------------------------------
# AttachIsoRequest
# ---------------------------------------------------------------------------

def test_attach_iso_required_fields_serialize_correctly():
    req = AttachIsoRequest(id="iso-1", virtualMachineId="vm-1")
    dumped = req.model_dump(exclude_none=True)
    assert dumped["id"] == "iso-1"
    assert dumped["virtualmachineid"] == "vm-1"


def test_attach_iso_alias_populates_field():
    req = AttachIsoRequest(id="iso-1", virtualMachineId="vm-1")
    assert req.virtualmachineid == "vm-1"


def test_attach_iso_forced_excluded_when_none():
    req = AttachIsoRequest(id="iso-1", virtualMachineId="vm-1")
    dumped = req.model_dump(exclude_none=True)
    assert "forced" not in dumped


def test_attach_iso_forced_included_when_set():
    req = AttachIsoRequest(id="iso-1", virtualMachineId="vm-1", forced=True)
    dumped = req.model_dump(exclude_none=True)
    assert dumped["forced"] is True


def test_attach_iso_missing_required_raises():
    with pytest.raises(ValidationError):
        AttachIsoRequest(id="iso-1")


# ---------------------------------------------------------------------------
# CopyIsoRequest
# ---------------------------------------------------------------------------

def test_copy_iso_required_id_only():
    req = CopyIsoRequest(id="iso-1")
    dumped = req.model_dump(exclude_none=True)
    assert dumped == {"id": "iso-1"}


def test_copy_iso_optional_fields_excluded_when_none():
    req = CopyIsoRequest(id="iso-1")
    dumped = req.model_dump(exclude_none=True)
    assert "destzoneid" not in dumped
    assert "destzoneids" not in dumped
    assert "sourcezoneid" not in dumped


def test_copy_iso_destzoneids_list_serializes():
    req = CopyIsoRequest(id="iso-1", destZoneIds=["z1", "z2"])
    dumped = req.model_dump(exclude_none=True)
    assert dumped["destzoneids"] == ["z1", "z2"]


def test_copy_iso_missing_id_raises():
    with pytest.raises(ValidationError):
        CopyIsoRequest()


# ---------------------------------------------------------------------------
# DeleteIsoRequest
# ---------------------------------------------------------------------------

def test_delete_iso_required_id_serializes():
    req = DeleteIsoRequest(id="iso-1")
    dumped = req.model_dump(exclude_none=True)
    assert dumped["id"] == "iso-1"


def test_delete_iso_optional_zoneid_excluded_when_none():
    req = DeleteIsoRequest(id="iso-1")
    dumped = req.model_dump(exclude_none=True)
    assert "zoneid" not in dumped


def test_delete_iso_zoneid_included_when_set():
    req = DeleteIsoRequest(id="iso-1", zoneId="zone-1")
    dumped = req.model_dump(exclude_none=True)
    assert dumped["zoneid"] == "zone-1"


def test_delete_iso_missing_id_raises():
    with pytest.raises(ValidationError):
        DeleteIsoRequest()


# ---------------------------------------------------------------------------
# DetachIsoRequest
# ---------------------------------------------------------------------------

def test_detach_iso_required_field_via_alias():
    req = DetachIsoRequest(virtualMachineId="vm-1")
    dumped = req.model_dump(exclude_none=True)
    assert dumped["virtualmachineid"] == "vm-1"


def test_detach_iso_forced_excluded_when_none():
    req = DetachIsoRequest(virtualMachineId="vm-1")
    dumped = req.model_dump(exclude_none=True)
    assert "forced" not in dumped


def test_detach_iso_forced_included_when_set():
    req = DetachIsoRequest(virtualMachineId="vm-1", forced=False)
    dumped = req.model_dump(exclude_none=True)
    assert dumped["forced"] is False


def test_detach_iso_missing_required_raises():
    with pytest.raises(ValidationError):
        DetachIsoRequest()


# ---------------------------------------------------------------------------
# ExtractIsoRequest
# ---------------------------------------------------------------------------

def test_extract_iso_required_fields_serialize():
    req = ExtractIsoRequest(id="iso-1", mode="HTTP_DOWNLOAD")
    dumped = req.model_dump(exclude_none=True)
    assert dumped["id"] == "iso-1"
    assert dumped["mode"] == "HTTP_DOWNLOAD"


def test_extract_iso_ftp_upload_mode_accepted():
    req = ExtractIsoRequest(id="iso-1", mode="FTP_UPLOAD")
    assert req.mode == "FTP_UPLOAD"


def test_extract_iso_invalid_mode_raises():
    with pytest.raises(ValidationError):
        ExtractIsoRequest(id="iso-1", mode="INVALID_MODE")


def test_extract_iso_optional_fields_excluded_when_none():
    req = ExtractIsoRequest(id="iso-1", mode="HTTP_DOWNLOAD")
    dumped = req.model_dump(exclude_none=True)
    assert "url" not in dumped
    assert "zoneid" not in dumped


def test_extract_iso_optional_fields_included_when_set():
    req = ExtractIsoRequest(id="iso-1", mode="HTTP_DOWNLOAD", url="http://example.com", zoneId="z1")
    dumped = req.model_dump(exclude_none=True)
    assert dumped["url"] == "http://example.com"
    assert dumped["zoneid"] == "z1"


# ---------------------------------------------------------------------------
# GetUploadParamsForIsoRequest
# ---------------------------------------------------------------------------

def test_get_upload_params_required_trio_serializes():
    req = GetUploadParamsForIsoRequest(format="QCOW2", name="my-iso", zoneId="zone-1")
    dumped = req.model_dump(exclude_none=True)
    assert dumped["format"] == "QCOW2"
    assert dumped["name"] == "my-iso"
    assert dumped["zoneid"] == "zone-1"


@pytest.mark.parametrize("fmt", ["QCOW2", "OVA", "VHD"])
def test_get_upload_params_iso_format_enum_accepted(fmt):
    req = GetUploadParamsForIsoRequest(format=fmt, name="iso", zoneId="z1")
    assert req.format == fmt


def test_get_upload_params_invalid_format_raises():
    with pytest.raises(ValidationError):
        GetUploadParamsForIsoRequest(format="RAW", name="iso", zoneId="z1")


def test_get_upload_params_optional_fields_excluded_when_none():
    req = GetUploadParamsForIsoRequest(format="QCOW2", name="iso", zoneId="z1")
    dumped = req.model_dump(exclude_none=True)
    assert "bootable" not in dumped
    assert "ostypeid" not in dumped
    assert "ispublic" not in dumped


def test_get_upload_params_optional_fields_included_when_set():
    req = GetUploadParamsForIsoRequest(
        format="OVA", name="iso", zoneId="z1",
        bootable=True, osTypeId="os-1", isPublic=True,
    )
    dumped = req.model_dump(exclude_none=True)
    assert dumped["bootable"] is True
    assert dumped["ostypeid"] == "os-1"
    assert dumped["ispublic"] is True


# ---------------------------------------------------------------------------
# ListIsoPermissionsRequest
# ---------------------------------------------------------------------------

def test_list_iso_permissions_required_id_serializes():
    req = ListIsoPermissionsRequest(id="iso-1")
    dumped = req.model_dump(exclude_none=True)
    assert dumped["id"] == "iso-1"


def test_list_iso_permissions_missing_id_raises():
    with pytest.raises(ValidationError):
        ListIsoPermissionsRequest()


# ---------------------------------------------------------------------------
# ListIsosRequest
# ---------------------------------------------------------------------------

def test_list_isos_all_optional_with_pagination_defaults():
    req = ListIsosRequest()
    dumped = req.model_dump(exclude_none=True)
    assert dumped["page"] == 1
    assert dumped["pagesize"] == 50


def test_list_isos_isofilter_valid_values_accepted():
    for f in ["featured", "self", "selfexecutable", "sharedexecutable", "executable", "community", "all"]:
        req = ListIsosRequest(isoFilter=f)
        assert req.isofilter == f


def test_list_isos_isofilter_invalid_raises():
    with pytest.raises(ValidationError):
        ListIsosRequest(isoFilter="unknown")


@pytest.mark.parametrize("arch", ["x86_64", "aarch64"])
def test_list_isos_arch_enum_accepted(arch):
    req = ListIsosRequest(arch=arch)
    assert req.arch == arch


def test_list_isos_invalid_arch_raises():
    with pytest.raises(ValidationError):
        ListIsosRequest(arch="arm64")


def test_list_isos_optional_fields_excluded_when_none():
    req = ListIsosRequest()
    dumped = req.model_dump(exclude_none=True)
    assert "isofilter" not in dumped
    assert "zoneid" not in dumped
    assert "id" not in dumped


def test_list_isos_optional_fields_included_when_set():
    req = ListIsosRequest(isoFilter="featured", zoneId="z1", bootable=True, keyword="ubuntu")
    dumped = req.model_dump(exclude_none=True)
    assert dumped["isofilter"] == "featured"
    assert dumped["zoneid"] == "z1"
    assert dumped["bootable"] is True
    assert dumped["keyword"] == "ubuntu"


# ---------------------------------------------------------------------------
# RegisterIsoRequest
# ---------------------------------------------------------------------------

def test_register_iso_required_fields_serialize():
    req = RegisterIsoRequest(name="ubuntu", url="http://example.com/ubuntu.iso", zoneId="zone-1")
    dumped = req.model_dump(exclude_none=True)
    assert dumped["name"] == "ubuntu"
    assert dumped["url"] == "http://example.com/ubuntu.iso"
    assert dumped["zoneid"] == "zone-1"


def test_register_iso_optional_fields_excluded_when_none():
    req = RegisterIsoRequest(name="iso", url="http://example.com/iso", zoneId="z1")
    dumped = req.model_dump(exclude_none=True)
    assert "bootable" not in dumped
    assert "ostypeid" not in dumped
    assert "ispublic" not in dumped
    assert "domainid" not in dumped


def test_register_iso_optional_fields_included_when_set():
    req = RegisterIsoRequest(
        name="iso", url="http://example.com/iso", zoneId="z1",
        bootable=True, osTypeId="os-1", isPublic=False,
        domainId="dom-1", passwordEnabled=True,
    )
    dumped = req.model_dump(exclude_none=True)
    assert dumped["bootable"] is True
    assert dumped["ostypeid"] == "os-1"
    assert dumped["ispublic"] is False
    assert dumped["domainid"] == "dom-1"
    assert dumped["passwordenabled"] is True


@pytest.mark.parametrize("arch", ["x86_64", "aarch64"])
def test_register_iso_arch_enum_accepted(arch):
    req = RegisterIsoRequest(name="iso", url="http://x.com/iso", zoneId="z1", arch=arch)
    assert req.arch == arch


def test_register_iso_missing_required_raises():
    with pytest.raises(ValidationError):
        RegisterIsoRequest(name="iso", url="http://x.com/iso")


# ---------------------------------------------------------------------------
# UpdateIsoRequest
# ---------------------------------------------------------------------------

def test_update_iso_required_id_serializes():
    req = UpdateIsoRequest(id="iso-1")
    dumped = req.model_dump(exclude_none=True)
    assert dumped["id"] == "iso-1"


def test_update_iso_all_optional_excluded_when_none():
    req = UpdateIsoRequest(id="iso-1")
    dumped = req.model_dump(exclude_none=True)
    assert list(dumped.keys()) == ["id"]


def test_update_iso_sortkey_is_int():
    req = UpdateIsoRequest(id="iso-1", sortKey=5)
    dumped = req.model_dump(exclude_none=True)
    assert isinstance(dumped["sortkey"], int)
    assert dumped["sortkey"] == 5


def test_update_iso_format_enum_validates():
    req = UpdateIsoRequest(id="iso-1", format="VHD")
    assert req.format == "VHD"


def test_update_iso_invalid_format_raises():
    with pytest.raises(ValidationError):
        UpdateIsoRequest(id="iso-1", format="INVALID")


def test_update_iso_optional_fields_included_when_set():
    req = UpdateIsoRequest(
        id="iso-1", name="new-name", displayText="New Display",
        bootable=True, passwordEnabled=False, sshKeyEnabled=True,
    )
    dumped = req.model_dump(exclude_none=True)
    assert dumped["name"] == "new-name"
    assert dumped["displaytext"] == "New Display"
    assert dumped["bootable"] is True
    assert dumped["passwordenabled"] is False
    assert dumped["sshkeyenabled"] is True


def test_update_iso_missing_id_raises():
    with pytest.raises(ValidationError):
        UpdateIsoRequest()


# ---------------------------------------------------------------------------
# UpdateIsoPermissionsRequest
# ---------------------------------------------------------------------------

def test_update_iso_permissions_required_id_serializes():
    req = UpdateIsoPermissionsRequest(id="iso-1")
    dumped = req.model_dump(exclude_none=True)
    assert dumped["id"] == "iso-1"


@pytest.mark.parametrize("op", ["add", "remove", "reset"])
def test_update_iso_permissions_op_enum_accepted(op):
    req = UpdateIsoPermissionsRequest(id="iso-1", op=op)
    assert req.op == op


def test_update_iso_permissions_invalid_op_raises():
    with pytest.raises(ValidationError):
        UpdateIsoPermissionsRequest(id="iso-1", op="delete")


def test_update_iso_permissions_optional_fields_excluded_when_none():
    req = UpdateIsoPermissionsRequest(id="iso-1")
    dumped = req.model_dump(exclude_none=True)
    assert "accounts" not in dumped
    assert "ispublic" not in dumped
    assert "op" not in dumped


def test_update_iso_permissions_optional_fields_included_when_set():
    req = UpdateIsoPermissionsRequest(
        id="iso-1", accounts="acc1,acc2", isPublic=True,
        isFeatured=False, op="add", projectIds="proj-1",
    )
    dumped = req.model_dump(exclude_none=True)
    assert dumped["accounts"] == "acc1,acc2"
    assert dumped["ispublic"] is True
    assert dumped["isfeatured"] is False
    assert dumped["op"] == "add"
    assert dumped["projectids"] == "proj-1"


def test_update_iso_permissions_missing_id_raises():
    with pytest.raises(ValidationError):
        UpdateIsoPermissionsRequest()
