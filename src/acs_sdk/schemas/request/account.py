
from pydantic import BaseModel, Field
from typing import Optional

class CreateAccountRequest(BaseModel):
    username: str = Field(..., description="unique username for the account")
    email: str = Field(..., description="Email of the account")
    password: str = Field(..., description="Clear text password for the account")
    firstname: str = Field(..., description="First name of the account")
    lastname: str = Field(..., description="Last name of the account")
    domainid: Optional[str] = Field(
        None, alias="domainId", description="Creates the user under the specified domain. If no domain is specified, the root domain will be used."
    )
    accounttype: Optional[int] = Field(
        0, description="Type of the account. Valid account types are 1 (admin), 2 (domain-admin), and 0 (user)."
    )
    account = Optional[str] = Field(
        None, description="Name of the account to be created. The user will be added to this newly created account. If no account is specified, the username will be used as the account name."
    )
    networkdomain: Optional[str] = Field(
        None, description="networkdomainNetwork domain for the account's networks"
    )
    roleid: Optional[str] = Field(
        None, alias="roleId", description="Creates the account under the specified role."
    )
    timezone: Optional[str] = Field(
        None, description="Specifies a timezone for this command. For more information on the timezone."
    )
    userid: Optional[str] = Field(
        None, alias="userId", description="User UUID, required for adding account from external provisioning system"
    )
    accountid: Optional[str] = Field(
        None, alias="accountId", description="Account UUID, required for adding account from external provisioning system"
    )
    accountdetails: Optional[str] = Field(
        None, alias="accountDetails", description="details for account used to store specific parameters."
    )


class ListAccountsRequest(BaseModel):
    id: Optional[str] = Field(
        None, description="List accounts by ID"
    )
    accounttype: Optional[int] = Field(
        None, description="List accounts by account type. Valid account types are 1 (admin), 2 (domain-admin), and 0 (user)."
    )
    apikeyaccesskey: Optional[str] = Field(
        None, alias="apiKeyAccessKey", description="List accounts by API key access key"
    )
    domainid: Optional[str] = Field(
        None, alias="domainId", description="List accounts by domain ID"
    )
    iscleanuprequired: Optional[bool] = Field(
        None, alias="isCleanupRequired", description="List accounts by cleanup required flag"
    )
    isrecursive: Optional[bool] = Field(
        False, alias="isRecursive", description="Include subdomains recursively"
    )
    keyword: Optional[str] = Field(
        None, description="Search keyword"
    )
    listall: Optional[bool] = Field(
        False,
        alias="listAll",
        description="List all resources caller is authorized to see"
    )
    name: Optional[str] = Field(
        None, description="List accounts by name"
    )
    page: Optional[int] = Field(
        1, ge=1, description="Page number"
    )
    pagesize: Optional[int] = Field(
        50, ge=1, le=500, description="Number of results per page"
    )
    state: Optional[str] = Field(
        None, description="List accounts by state. Valid states are enabled, disabled, and locked."
    )
    tag=Optional[str] = Field(
        None, description="List accounts by tag (key/value pairs)"
    )

class EnableAccountRequest(BaseModel):
    id: str = Field(..., description="ID of the account to enable")
    account: Optional[str] = Field(
        None, description="Enables specified account. If account parameter is used, domainId must also be used."
    )
    domainid: Optional[str] = Field(
        None, alias="domainId", description="Enables specified account in this domain."
    )

class DisableAccountRequest(BaseModel):
    id: str = Field(..., description="ID of the account to disable")
    lock: Optional[bool] = Field(
        False, description="If true, only lock the account; else disable the account"
    )
    account: Optional[str] = Field(
        None, description="Disables specified account. If account parameter is used, domainId must also be used."
    )
    domainid: Optional[str] = Field(
        None, alias="domainId", description="Disables specified account in this domain."
    )

class MarkDefaultZoneForAccountRequest(BaseModel):
    account: str = Field(..., description="Account for which to mark default zone")
    domainid: str = Field(..., alias="domainId", description="Domain ID of the account")
    zoneid: str = Field(..., alias="zoneId", description="Zone ID to mark as default for the account")


class UpdateAccountRequest(BaseModel):
    
    id: Optional[str] = Field(
        None, alias="accountId", description="Account UUID"
    )
    domainid: Optional[str] = Field(
        None, alias="domainId", description="The UUID of the domain where the account exists."
    )
    accountdetails: Optional[str] = Field(
        None, alias="accountDetails", description="details for account used to store specific parameters."
    )
    account = Optional[str] = Field(
        None, description="Current name of the account."
    )
    networkdomain: Optional[str] = Field(
        None, alias="networkDomain", description="Network domain for the account's networks; empty string will update domainName with NULL value"
    )
    roleid: Optional[str] = Field(
        None, alias="roleId", description="The UUID of the dynamic role to set for the account."
    )
    newname: Optional[str] = Field(
        None, alias="newName", description="New name for the account."
    )
    apiaccesskey: Optional[str] = Field(
        None, alias="apiAccessKey", description="Determines if Api key access for this user is enabled, disabled or inherits the value from its parent, the domain level setting api.key.access"
    )