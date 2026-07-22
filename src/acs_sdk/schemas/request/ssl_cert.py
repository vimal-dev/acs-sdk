# schemas/request/ssl_cert.py
from typing import Optional

from pydantic import Field

from acs_sdk.schemas.request.base import APIRequest


class UploadSslCertRequest(APIRequest):
    certificate: str = Field(..., description="SSL certificate")
    name: str = Field(..., description="Name for the uploaded certificate")
    privatekey: str = Field(..., alias="privateKey", description="Private key")
    account: Optional[str] = Field(None, description="Account that will own the SSL certificate")
    certchain: Optional[str] = Field(
        None, alias="certChain", description="Certificate chain of trust"
    )
    domainid: Optional[str] = Field(
        None, alias="domainId", description="Domain ID of the account owning the SSL certificate"
    )
    enabledrevocationcheck: Optional[bool] = Field(
        None,
        alias="enabledRevocationCheck",
        description="Enables revocation checking for certificates",
    )
    password: Optional[str] = Field(None, description="Password for the private key")
    projectid: Optional[str] = Field(
        None, alias="projectId", description="An optional project for the SSL certificate"
    )


class DeleteSslCertRequest(APIRequest):
    id: str = Field(..., description="Id of SSL certificate")


class ListSslCertsRequest(APIRequest):
    accountid: Optional[str] = Field(None, alias="accountId", description="Account ID")
    certid: Optional[str] = Field(None, alias="certId", description="ID of SSL certificate")
    lbruleid: Optional[str] = Field(None, alias="lbRuleId", description="Load balancer rule ID")
    projectid: Optional[str] = Field(
        None, alias="projectId", description="Project that owns the SSL certificate"
    )
