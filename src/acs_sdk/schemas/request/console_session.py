# schemas/request/console_session.py
from datetime import datetime
from typing import Optional

from pydantic import Field, field_serializer

from acs_sdk.schemas.request.base import APIRequest, PaginationMixin


class CreateConsoleEndpointRequest(APIRequest):
    virtualmachineid: str = Field(..., alias="virtualMachineId", description="ID of the VM")
    token: Optional[str] = Field(
        None, description="Extra security token, valid when the extra validation is enabled"
    )


class ListConsoleSessionsRequest(APIRequest, PaginationMixin):
    accountid: Optional[str] = Field(
        None, alias="accountId", description="The ID of the account that created the console endpoint."
    )
    acquired: Optional[bool] = Field(
        False,
        description=(
            "Lists acquired console sessions, defaults to false. Acquired console sessions are the ones "
            "that have been accessed. The 'activeonly' parameter has precedence over the 'acquired' "
            "parameter, i.e., when the 'activeonly' parameter is 'true', the 'acquired' parameter value "
            "will be ignored."
        ),
    )
    activeonly: Optional[bool] = Field(
        True,
        alias="activeOnly",
        description=(
            "Lists only active console sessions, defaults to true. Active sessions are the ones that have "
            "been acquired and have not been removed."
        ),
    )
    clientaddress: Optional[str] = Field(
        None, alias="clientAddress", description="IP address of the client that accessed the console session."
    )
    consoleendpointcreatoraddress: Optional[str] = Field(
        None,
        alias="consoleEndpointCreatorAddress",
        description="IP address of the creator of the console endpoint.",
    )
    domainid: Optional[str] = Field(
        None, alias="domainId", description="The domain ID of the account that created the console endpoint."
    )
    enddate: Optional[datetime] = Field(
        None, alias="endDate", description="Lists console sessions generated up until this date."
    )
    hostid: Optional[str] = Field(
        None, alias="hostId", description="Lists console sessions from the specified host."
    )
    id: Optional[str] = Field(None, description="The ID of the console session.")
    isrecursive: Optional[bool] = Field(
        False,
        alias="isRecursive",
        description=(
            "Lists console sessions recursively per domain. If an account ID is informed, only the "
            "account's console sessions will be listed. Defaults to false."
        ),
    )
    keyword: Optional[str] = Field(None, description="List by keyword")
    startdate: Optional[datetime] = Field(
        None, alias="startDate", description="Lists console sessions generated from this date onwards."
    )
    userid: Optional[str] = Field(
        None, alias="userId", description="The ID of the user that created the console endpoint."
    )
    virtualmachineid: Optional[str] = Field(
        None, alias="virtualMachineId", description="The ID of the virtual machine."
    )

    @field_serializer("startdate", "enddate")
    def serialize_date(self, value: Optional[datetime], _info):
        if isinstance(value, datetime):
            return value.strftime("%Y-%m-%d %H:%M:%S")
        return value
