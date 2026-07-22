from datetime import datetime

import pytest
from pydantic import ValidationError

from acs_sdk.schemas.request.console_session import (
    CreateConsoleEndpointRequest,
    ListConsoleSessionsRequest,
)


# ---------------------------------------------------------------------------
# CreateConsoleEndpointRequest
# ---------------------------------------------------------------------------

def test_create_console_endpoint_required_vm_id_serializes():
    req = CreateConsoleEndpointRequest(virtualMachineId="vm-1")
    dumped = req.model_dump(exclude_none=True)
    assert dumped == {"virtualmachineid": "vm-1"}


def test_create_console_endpoint_token_serializes():
    req = CreateConsoleEndpointRequest(virtualMachineId="vm-1", token="tok-1")
    dumped = req.model_dump(exclude_none=True)
    assert dumped["token"] == "tok-1"


def test_create_console_endpoint_missing_vm_id_raises():
    with pytest.raises(ValidationError):
        CreateConsoleEndpointRequest()


# ---------------------------------------------------------------------------
# ListConsoleSessionsRequest
# ---------------------------------------------------------------------------

def test_list_console_sessions_defaults_from_pagination_mixin():
    req = ListConsoleSessionsRequest()
    dumped = req.model_dump(exclude_none=True)
    assert dumped["page"] == 1
    assert dumped["pagesize"] == 50


def test_list_console_sessions_boolean_defaults():
    req = ListConsoleSessionsRequest()
    dumped = req.model_dump(exclude_none=True)
    assert dumped["acquired"] is False
    assert dumped["activeonly"] is True
    assert dumped["isrecursive"] is False


def test_list_console_sessions_aliases_serialize_to_snake_case():
    req = ListConsoleSessionsRequest(
        accountId="acct-1",
        domainId="dom-1",
        hostId="host-1",
        userId="user-1",
        virtualMachineId="vm-1",
        clientAddress="10.0.0.1",
        consoleEndpointCreatorAddress="10.0.0.2",
        isRecursive=True,
        activeOnly=False,
    )
    dumped = req.model_dump(exclude_none=True)
    assert dumped["accountid"] == "acct-1"
    assert dumped["domainid"] == "dom-1"
    assert dumped["hostid"] == "host-1"
    assert dumped["userid"] == "user-1"
    assert dumped["virtualmachineid"] == "vm-1"
    assert dumped["clientaddress"] == "10.0.0.1"
    assert dumped["consoleendpointcreatoraddress"] == "10.0.0.2"
    assert dumped["isrecursive"] is True
    assert dumped["activeonly"] is False


def test_list_console_sessions_dates_serialize_to_string():
    req = ListConsoleSessionsRequest(
        startDate=datetime(2026, 1, 1, 0, 0, 0),
        endDate=datetime(2026, 1, 31, 23, 59, 59),
    )
    dumped = req.model_dump(exclude_none=True)
    assert dumped["startdate"] == "2026-01-01 00:00:00"
    assert dumped["enddate"] == "2026-01-31 23:59:59"


def test_list_console_sessions_optional_fields_excluded_when_none():
    req = ListConsoleSessionsRequest()
    dumped = req.model_dump(exclude_none=True)
    assert "id" not in dumped
    assert "keyword" not in dumped
    assert "startdate" not in dumped
    assert "enddate" not in dumped
