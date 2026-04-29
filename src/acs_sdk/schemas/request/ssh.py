from typing import Optional

from pydantic import Field

from acs_sdk.schemas.request.base import APIRequest


class CreateSSHKeyPairRequest(APIRequest):
    name: str = Field(..., description="Name of the SSH key pair")
    account: Optional[str] = Field(
        None,
        description="Account the SSH key pair belongs to. Must be used with the domainId parameter.",
    )
    domainid: Optional[str] = Field(
        None, alias="domainId", description="Domain ID where the SSH key pair belongs"
    )
    projectid: Optional[str] = Field(
        None, alias="projectId", description="Project ID where the SSH key pair belongs"
    )


class DeleteSSHKeyPairRequest(APIRequest):
    name: str = Field(..., description="Name of the SSH key pair to delete")
    account: Optional[str] = Field(
        None,
        description="Account the SSH key pair belongs to. Must be used with the domainId parameter.",
    )
    domainid: Optional[str] = Field(
        None, alias="domainId", description="Domain ID where the SSH key pair belongs"
    )
    projectid: Optional[str] = Field(
        None, alias="projectId", description="Project ID where the SSH key pair belongs"
    )


class ListSSHKeyPairsRequest(APIRequest):
    name: Optional[str] = Field(None, description="List SSH key pairs by name")
    account: Optional[str] = Field(
        None, description="List resources by account. Must be used with the domainId parameter."
    )
    domainid: Optional[str] = Field(
        None, alias="domainId", description="List only resources belonging to the domain specified"
    )
    isrecursive: Optional[bool] = Field(
        False, alias="isRecursive", description="Include subdomains recursively"
    )
    keyword: Optional[str] = Field(None, description="Search keyword")
    listall: Optional[bool] = Field(
        False, alias="listAll", description="List all resources caller is authorized to see"
    )
    projectid: Optional[str] = Field(None, alias="projectId", description="List objects by project")
    fingerprint: Optional[str] = Field(
        None, description="List resources by A public key fingerprint"
    )
    page: Optional[int] = Field(1, ge=1, description="Page number")
    pagesize: Optional[int] = Field(50, ge=1, le=500, description="Number of results per page")


class RegisterSSHKeyPairRequest(APIRequest):
    name: str = Field(..., description="Name of the SSH key pair")
    publickey: str = Field(..., alias="publicKey", description="Public key material to register")
    account: Optional[str] = Field(
        None,
        description="Account the SSH key pair belongs to. Must be used with the domainId parameter.",
    )
    domainid: Optional[str] = Field(
        None, alias="domainId", description="Domain ID where the SSH key pair belongs"
    )
    projectid: Optional[str] = Field(
        None, alias="projectId", description="Project ID where the SSH key pair belongs"
    )
