import pytest
from pydantic import ValidationError

from acs_sdk.schemas.request.ssl_cert import (
    DeleteSslCertRequest,
    ListSslCertsRequest,
    UploadSslCertRequest,
)


# ---------------------------------------------------------------------------
# UploadSslCertRequest
# ---------------------------------------------------------------------------


def test_upload_ssl_cert_required_fields_serialize():
    req = UploadSslCertRequest(certificate="cert-data", name="mycert", privateKey="key-data")
    dumped = req.model_dump(exclude_none=True)
    assert dumped == {
        "certificate": "cert-data",
        "name": "mycert",
        "privatekey": "key-data",
    }


def test_upload_ssl_cert_optional_fields_serialize():
    req = UploadSslCertRequest(
        certificate="cert-data",
        name="mycert",
        privateKey="key-data",
        account="acct1",
        certChain="chain-data",
        domainId="dom-1",
        enabledRevocationCheck=True,
        password="secret",
        projectId="proj-1",
    )
    dumped = req.model_dump(exclude_none=True)
    assert dumped["account"] == "acct1"
    assert dumped["certchain"] == "chain-data"
    assert dumped["domainid"] == "dom-1"
    assert dumped["enabledrevocationcheck"] is True
    assert dumped["password"] == "secret"
    assert dumped["projectid"] == "proj-1"


def test_upload_ssl_cert_missing_required_fields_raises():
    with pytest.raises(ValidationError):
        UploadSslCertRequest()


# ---------------------------------------------------------------------------
# DeleteSslCertRequest
# ---------------------------------------------------------------------------


def test_delete_ssl_cert_required_id_serializes():
    req = DeleteSslCertRequest(id="cert-1")
    dumped = req.model_dump(exclude_none=True)
    assert dumped == {"id": "cert-1"}


def test_delete_ssl_cert_missing_id_raises():
    with pytest.raises(ValidationError):
        DeleteSslCertRequest()


# ---------------------------------------------------------------------------
# ListSslCertsRequest
# ---------------------------------------------------------------------------


def test_list_ssl_certs_all_fields_optional():
    req = ListSslCertsRequest()
    dumped = req.model_dump(exclude_none=True)
    assert dumped == {}


def test_list_ssl_certs_aliases_serialize_to_snake_case():
    req = ListSslCertsRequest(
        accountId="acct-1",
        certId="cert-1",
        lbRuleId="lb-1",
        projectId="proj-1",
    )
    dumped = req.model_dump(exclude_none=True)
    assert dumped["accountid"] == "acct-1"
    assert dumped["certid"] == "cert-1"
    assert dumped["lbruleid"] == "lb-1"
    assert dumped["projectid"] == "proj-1"
