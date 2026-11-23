import asyncio
from unittest.mock import AsyncMock, Mock

import pytest

from acs_sdk.schemas.request.template import (
    CopyTemplateRequest,
    CreateTemplateRequest,
    DeleteTemplateRequest,
    ExtractTemplateRequest,
    GetUploadParamsForTemplateRequest,
    ListTemplatePermissionsRequest,
    ListTemplatesRequest,
    PrepareTemplateRequest,
    RegisterTemplateRequest,
    UpdateTemplatePermissionsRequest,
    UpdateTemplateRequest,
)
from acs_sdk.services.template import Template


def _service(return_value):
    client = Mock()
    client.call.return_value = return_value
    return Template(client=client), client


def test_template_list_parses_list_response():
    svc, client = _service({"listtemplatesresponse": {"template": [{"id": "t-1"}], "count": 1}})
    payload = ListTemplatesRequest(templateFilter="self")
    response = svc.list(payload)

    assert response.data == [{"id": "t-1"}]
    assert response.count == 1
    client.call.assert_called_once_with("listTemplates", payload.model_dump(exclude_none=True))


def test_template_list_permissions_parses_response():
    svc, client = _service(
        {"listtemplatepermissionsresponse": {"templatepermission": {"id": "t-1", "ispublic": True}}}
    )
    response = svc.list_permissions(ListTemplatePermissionsRequest(id="t-1"))

    assert response.data == {"id": "t-1", "ispublic": True}
    client.call.assert_called_once_with("listTemplatePermissions", {"id": "t-1"})


def test_template_register_parses_list_response():
    svc, client = _service(
        {"registertemplateresponse": {"template": [{"id": "t-new"}], "count": 1}}
    )
    payload = RegisterTemplateRequest(
        displayText="Ubuntu",
        format="QCOW2",
        hypervisor="KVM",
        name="ubuntu",
        url="http://example.com/ubuntu.qcow2",
        zoneIds=["z-1", "z-2"],
        details={"keyboard": "us"},
    )
    response = svc.register(payload)

    assert response.data == [{"id": "t-new"}]
    assert response.count == 1
    params = client.call.call_args.args[1]
    assert client.call.call_args.args[0] == "registerTemplate"
    assert params["zoneids"] == "z-1,z-2"
    assert params["details[0].keyboard"] == "us"
    assert "details" not in params


def test_template_create_returns_job():
    svc, client = _service({"createtemplateresponse": {"id": "t-2", "jobid": "job-1"}})
    payload = CreateTemplateRequest(
        displayText="From vol", name="from-vol", osTypeId="os-1", volumeId="vol-1"
    )
    response = svc.create(payload)

    assert response.data == {"id": "t-2", "jobid": "job-1"}
    client.call.assert_called_once_with(
        "createTemplate",
        {"displaytext": "From vol", "name": "from-vol", "ostypeid": "os-1", "volumeid": "vol-1"},
    )


def test_template_update_parses_response():
    svc, client = _service({"updatetemplateresponse": {"template": {"id": "t-1", "name": "new"}}})
    response = svc.update(UpdateTemplateRequest(id="t-1", name="new"))

    assert response.data == {"id": "t-1", "name": "new"}
    client.call.assert_called_once_with("updateTemplate", {"id": "t-1", "name": "new"})


def test_template_delete_returns_job():
    svc, client = _service({"deletetemplateresponse": {"jobid": "job-2"}})
    response = svc.delete(DeleteTemplateRequest(id="t-1", zoneId="z-1"))

    assert response.data == {"jobid": "job-2"}
    client.call.assert_called_once_with("deleteTemplate", {"id": "t-1", "zoneid": "z-1"})


def test_template_update_permissions_serializes_lists():
    svc, client = _service({"updatetemplatepermissionsresponse": {"success": "true"}})
    payload = UpdateTemplatePermissionsRequest(id="t-1", op="add", accounts=["a", "b"])
    response = svc.update_permissions(payload)

    assert response.data == {"success": "true"}
    client.call.assert_called_once_with(
        "updateTemplatePermissions", {"id": "t-1", "op": "add", "accounts": "a,b"}
    )


def test_template_copy_returns_job():
    svc, client = _service({"copytemplateresponse": {"jobid": "job-3"}})
    response = svc.copy(CopyTemplateRequest(id="t-1", destZoneIds=["z-2"]))

    assert response.data is None  # job response carries no "template" key yet
    client.call.assert_called_once_with("copyTemplate", {"id": "t-1", "destzoneids": "z-2"})


def test_template_extract_parses_response():
    svc, client = _service(
        {"extracttemplateresponse": {"template": {"id": "t-1", "url": "http://dl"}}}
    )
    response = svc.extract(ExtractTemplateRequest(id="t-1", mode="HTTP_DOWNLOAD"))

    assert response.data == {"id": "t-1", "url": "http://dl"}
    client.call.assert_called_once_with("extractTemplate", {"id": "t-1", "mode": "HTTP_DOWNLOAD"})


def test_template_get_upload_params_parses_response():
    svc, client = _service(
        {
            "getuploadparamsfortemplateresponse": {
                "getuploadparams": {"id": "t-1", "postURL": "https://ssvm/upload"}
            }
        }
    )
    payload = GetUploadParamsForTemplateRequest(
        displayText="Up", format="QCOW2", hypervisor="KVM", name="up", zoneId="z-1"
    )
    response = svc.get_upload_params(payload)

    assert response.data == {"id": "t-1", "postURL": "https://ssvm/upload"}
    assert client.call.call_args.args[0] == "getUploadParamsForTemplate"


def test_template_prepare_parses_response():
    svc, client = _service({"preparetemplateresponse": {"template": [{"id": "t-1"}], "count": 1}})
    response = svc.prepare(PrepareTemplateRequest(templateId="t-1", zoneId="z-1"))

    assert response.data == [{"id": "t-1"}]
    client.call.assert_called_once_with("prepareTemplate", {"templateid": "t-1", "zoneid": "z-1"})


@pytest.mark.parametrize(
    "method, command, envelope, payload",
    [
        (
            "delete_async",
            "deleteTemplate",
            "deletetemplateresponse",
            DeleteTemplateRequest(id="t-1"),
        ),
        (
            "extract_async",
            "extractTemplate",
            "extracttemplateresponse",
            ExtractTemplateRequest(id="t-1", mode="HTTP_DOWNLOAD"),
        ),
        (
            "update_permissions_async",
            "updateTemplatePermissions",
            "updatetemplatepermissionsresponse",
            UpdateTemplatePermissionsRequest(id="t-1", isPublic=True),
        ),
    ],
)
def test_template_async_variants_call_client(method, command, envelope, payload):
    client = Mock()
    client.call_async = AsyncMock(return_value={envelope: {"jobid": "job-x"}})
    svc = Template(client=client)

    asyncio.run(getattr(svc, method)(payload))

    client.call_async.assert_called_once_with(command, payload.model_dump(exclude_none=True))
