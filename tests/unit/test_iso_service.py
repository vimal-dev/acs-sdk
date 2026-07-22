import asyncio
from unittest.mock import AsyncMock, Mock

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
from acs_sdk.services.iso import ISO


# ---------------------------------------------------------------------------
# list
# ---------------------------------------------------------------------------


def test_iso_list_parses_list_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "listisosresponse": {
            "iso": [{"id": "iso-1", "name": "ubuntu"}],
            "count": 1,
        }
    }

    iso = ISO(client=mock_client)
    payload = ListIsosRequest()
    response = iso.list(payload)

    assert response.data == [{"id": "iso-1", "name": "ubuntu"}]
    assert response.count == 1
    mock_client.call.assert_called_once_with("listIsos", payload.model_dump(exclude_none=True))


# ---------------------------------------------------------------------------
# list_permissions
# ---------------------------------------------------------------------------


def test_iso_list_permissions_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "listisopermissionsresponse": {
            "isopermission": {"id": "iso-1", "ispublic": True},
        }
    }

    iso = ISO(client=mock_client)
    payload = ListIsoPermissionsRequest(id="iso-1")
    response = iso.list_permissions(payload)

    assert response.data == {"id": "iso-1", "ispublic": True}
    mock_client.call.assert_called_once_with("listIsoPermissions", {"id": "iso-1"})


# ---------------------------------------------------------------------------
# register
# ---------------------------------------------------------------------------


def test_iso_register_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "registerisoresponse": {
            "iso": {"id": "iso-new", "name": "ubuntu", "zoneid": "zone-1"},
        }
    }

    iso = ISO(client=mock_client)
    payload = RegisterIsoRequest(
        name="ubuntu", url="http://example.com/ubuntu.iso", zoneId="zone-1"
    )
    response = iso.register(payload)

    assert response.data == {"id": "iso-new", "name": "ubuntu", "zoneid": "zone-1"}
    mock_client.call.assert_called_once_with("registerIso", payload.model_dump(exclude_none=True))


# ---------------------------------------------------------------------------
# update
# ---------------------------------------------------------------------------


def test_iso_update_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "updateisoresponse": {
            "iso": {"id": "iso-1", "name": "updated-iso"},
        }
    }

    iso = ISO(client=mock_client)
    payload = UpdateIsoRequest(id="iso-1", name="updated-iso")
    response = iso.update(payload)

    assert response.data == {"id": "iso-1", "name": "updated-iso"}
    mock_client.call.assert_called_once_with("updateIso", payload.model_dump(exclude_none=True))


# ---------------------------------------------------------------------------
# delete
# ---------------------------------------------------------------------------


def test_iso_delete_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {"deleteisoresponse": {}}

    iso = ISO(client=mock_client)
    payload = DeleteIsoRequest(id="iso-1")
    response = iso.delete(payload)

    assert response.data == {}
    mock_client.call.assert_called_once_with("deleteIso", {"id": "iso-1"})


def test_iso_delete_with_zone_passes_correct_params():
    mock_client = Mock()
    mock_client.call.return_value = {"deleteisoresponse": {}}

    iso = ISO(client=mock_client)
    payload = DeleteIsoRequest(id="iso-1", zoneId="zone-1")
    iso.delete(payload)

    mock_client.call.assert_called_once_with("deleteIso", {"id": "iso-1", "zoneid": "zone-1"})


# ---------------------------------------------------------------------------
# update_permissions
# ---------------------------------------------------------------------------


def test_iso_update_permissions_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {"updateisopermissionsresponse": {}}

    iso = ISO(client=mock_client)
    payload = UpdateIsoPermissionsRequest(id="iso-1", isPublic=True, op="add")
    response = iso.update_permissions(payload)

    assert response.data == {}
    mock_client.call.assert_called_once_with(
        "updateIsoPermissions", payload.model_dump(exclude_none=True)
    )


# ---------------------------------------------------------------------------
# attach
# ---------------------------------------------------------------------------


def test_iso_attach_parses_vm_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "attachisoresponse": {
            "virtualmachine": {"id": "vm-1", "state": "Running"},
        }
    }

    iso = ISO(client=mock_client)
    payload = AttachIsoRequest(id="iso-1", virtualMachineId="vm-1")
    response = iso.attach(payload)

    assert response.data == {"id": "vm-1", "state": "Running"}
    mock_client.call.assert_called_once_with("attachIso", payload.model_dump(exclude_none=True))


# ---------------------------------------------------------------------------
# detach
# ---------------------------------------------------------------------------


def test_iso_detach_parses_vm_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "detachisoresponse": {
            "virtualmachine": {"id": "vm-1", "state": "Running"},
        }
    }

    iso = ISO(client=mock_client)
    payload = DetachIsoRequest(virtualMachineId="vm-1")
    response = iso.detach(payload)

    assert response.data == {"id": "vm-1", "state": "Running"}
    mock_client.call.assert_called_once_with("detachIso", {"virtualmachineid": "vm-1"})


# ---------------------------------------------------------------------------
# copy
# ---------------------------------------------------------------------------


def test_iso_copy_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "copyisoresponse": {
            "template": {"id": "iso-1", "zoneid": "zone-2"},
        }
    }

    iso = ISO(client=mock_client)
    payload = CopyIsoRequest(id="iso-1", destZoneId="zone-2")
    response = iso.copy(payload)

    assert response.data == {"id": "iso-1", "zoneid": "zone-2"}
    mock_client.call.assert_called_once_with("copyIso", payload.model_dump(exclude_none=True))


# ---------------------------------------------------------------------------
# extract
# ---------------------------------------------------------------------------


def test_iso_extract_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "extractisoresponse": {
            "template": {"id": "iso-1", "url": "http://download.example.com/iso-1"},
        }
    }

    iso = ISO(client=mock_client)
    payload = ExtractIsoRequest(id="iso-1", mode="HTTP_DOWNLOAD", zoneId="zone-1")
    response = iso.extract(payload)

    assert response.data == {"id": "iso-1", "url": "http://download.example.com/iso-1"}
    mock_client.call.assert_called_once_with("extractIso", payload.model_dump(exclude_none=True))


# ---------------------------------------------------------------------------
# get_upload_params
# ---------------------------------------------------------------------------


def test_iso_get_upload_params_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "getuploadparamsforisoresponse": {
            "getuploadparams": {
                "id": "upload-token-1",
                "postURL": "http://upload.example.com",
                "signature": "abc123",
                "expires": "2026-12-31",
                "metadata": "meta",
            },
        }
    }

    iso = ISO(client=mock_client)
    payload = GetUploadParamsForIsoRequest(format="QCOW2", name="my-iso", zoneId="zone-1")
    response = iso.get_upload_params(payload)

    assert response.data["id"] == "upload-token-1"
    assert response.data["postURL"] == "http://upload.example.com"
    mock_client.call.assert_called_once_with(
        "getUploadParamsForIso", payload.model_dump(exclude_none=True)
    )


# ---------------------------------------------------------------------------
# list_async (async variant)
# ---------------------------------------------------------------------------


def test_iso_list_async_parses_list_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={
            "listisosresponse": {
                "iso": [{"id": "iso-2", "name": "centos"}],
                "count": 1,
            }
        }
    )

    iso = ISO(client=mock_client)
    payload = ListIsosRequest(isoFilter="featured")
    response = asyncio.run(iso.list_async(payload))

    assert response.data == [{"id": "iso-2", "name": "centos"}]
    assert response.count == 1
    mock_client.call_async.assert_called_once_with(
        "listIsos", payload.model_dump(exclude_none=True)
    )
