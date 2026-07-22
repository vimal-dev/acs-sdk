import asyncio
from unittest.mock import AsyncMock, Mock

from acs_sdk.schemas.request.ssl_cert import (
    DeleteSslCertRequest,
    ListSslCertsRequest,
    UploadSslCertRequest,
)
from acs_sdk.services.ssl_cert import SslCert


# ---------------------------------------------------------------------------
# upload
# ---------------------------------------------------------------------------

def test_ssl_cert_upload_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "uploadsslcertresponse": {"id": "cert-1", "name": "mycert"},
    }

    sc = SslCert(client=mock_client)
    payload = UploadSslCertRequest(certificate="cert-data", name="mycert", privateKey="key-data")
    response = sc.upload(payload)

    assert response.data == {"id": "cert-1", "name": "mycert"}
    mock_client.call.assert_called_once_with(
        "uploadSslCert", payload.model_dump(exclude_none=True)
    )


def test_ssl_cert_upload_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={"uploadsslcertresponse": {"id": "cert-1", "name": "mycert"}}
    )

    sc = SslCert(client=mock_client)
    payload = UploadSslCertRequest(certificate="cert-data", name="mycert", privateKey="key-data")
    response = asyncio.run(sc.upload_async(payload))

    assert response.data == {"id": "cert-1", "name": "mycert"}
    mock_client.call_async.assert_called_once_with(
        "uploadSslCert", payload.model_dump(exclude_none=True)
    )


# ---------------------------------------------------------------------------
# list
# ---------------------------------------------------------------------------

def test_ssl_cert_list_parses_list_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "listsslcertsresponse": {
            "sslcert": [{"id": "cert-1", "name": "mycert"}],
            "count": 1,
        }
    }

    sc = SslCert(client=mock_client)
    payload = ListSslCertsRequest()
    response = sc.list(payload)

    assert response.data == [{"id": "cert-1", "name": "mycert"}]
    assert response.count == 1
    mock_client.call.assert_called_once_with(
        "listSslCerts", payload.model_dump(exclude_none=True)
    )


def test_ssl_cert_list_async_parses_list_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={
            "listsslcertsresponse": {
                "sslcert": [{"id": "cert-2", "name": "othercert"}],
                "count": 1,
            }
        }
    )

    sc = SslCert(client=mock_client)
    payload = ListSslCertsRequest(certId="cert-2")
    response = asyncio.run(sc.list_async(payload))

    assert response.data == [{"id": "cert-2", "name": "othercert"}]
    assert response.count == 1
    mock_client.call_async.assert_called_once_with(
        "listSslCerts", payload.model_dump(exclude_none=True)
    )


# ---------------------------------------------------------------------------
# delete
# ---------------------------------------------------------------------------

def test_ssl_cert_delete_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "deletesslcertresponse": {"success": "true"},
    }

    sc = SslCert(client=mock_client)
    payload = DeleteSslCertRequest(id="cert-1")
    response = sc.delete(payload)

    assert response.data == {"success": "true"}
    mock_client.call.assert_called_once_with("deleteSslCert", {"id": "cert-1"})


def test_ssl_cert_delete_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={"deletesslcertresponse": {"success": "true"}}
    )

    sc = SslCert(client=mock_client)
    payload = DeleteSslCertRequest(id="cert-1")
    response = asyncio.run(sc.delete_async(payload))

    assert response.data == {"success": "true"}
    mock_client.call_async.assert_called_once_with("deleteSslCert", {"id": "cert-1"})
