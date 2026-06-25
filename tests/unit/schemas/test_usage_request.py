import pytest
from datetime import datetime, timezone, timedelta
from pydantic import ValidationError

from acs_sdk.schemas.request.usage import (
    GenerateUsageRecordsRequest,
    ListUsageRecordsRequest,
    RemoveRawUsageRecordsRequest,
)


# ---------------------------------------------------------------------------
# ListUsageRecordsRequest
# ---------------------------------------------------------------------------

def test_list_usage_required_fields_serialize():
    req = ListUsageRecordsRequest(
        startdate=datetime(2024, 1, 1, tzinfo=timezone.utc),
        enddate=datetime(2024, 1, 31, tzinfo=timezone.utc),
    )
    dumped = req.model_dump(exclude_none=True)
    assert dumped["startdate"] == "2024-01-01T00:00:00+0000"
    assert dumped["enddate"] == "2024-01-31T00:00:00+0000"


def test_list_usage_pagination_defaults():
    req = ListUsageRecordsRequest(
        startdate=datetime(2024, 1, 1),
        enddate=datetime(2024, 1, 31),
    )
    dumped = req.model_dump(exclude_none=True)
    assert dumped["page"] == 1
    assert dumped["pagesize"] == 50


def test_list_usage_optional_filters_excluded_when_none():
    req = ListUsageRecordsRequest(
        startdate=datetime(2024, 1, 1),
        enddate=datetime(2024, 1, 31),
    )
    dumped = req.model_dump(exclude_none=True)
    assert "account" not in dumped
    assert "accountid" not in dumped
    assert "domainid" not in dumped
    assert "projectid" not in dumped
    assert "usageid" not in dumped
    assert "type" not in dumped
    assert "keyword" not in dumped
    assert "includetags" not in dumped
    assert "isrecursive" not in dumped
    assert "oldformat" not in dumped


def test_list_usage_optional_filters_included_when_set():
    req = ListUsageRecordsRequest(
        startdate=datetime(2024, 1, 1),
        enddate=datetime(2024, 1, 31),
        account="testuser",
        accountId="acc-1",
        domainId="dom-1",
        projectId="proj-1",
        usageId="usage-1",
        type=1,
        keyword="test",
        includeTags=True,
        isRecursive=True,
        oldFormat=False,
    )
    dumped = req.model_dump(exclude_none=True)
    assert dumped["account"] == "testuser"
    assert dumped["accountid"] == "acc-1"
    assert dumped["domainid"] == "dom-1"
    assert dumped["projectid"] == "proj-1"
    assert dumped["usageid"] == "usage-1"
    assert dumped["type"] == 1
    assert dumped["keyword"] == "test"
    assert dumped["includetags"] is True
    assert dumped["isrecursive"] is True
    assert dumped["oldformat"] is False


def test_list_usage_enddate_before_startdate_raises():
    with pytest.raises(ValidationError, match="enddate must be >= startdate"):
        ListUsageRecordsRequest(
            startdate=datetime(2024, 2, 1),
            enddate=datetime(2024, 1, 1),
        )


def test_list_usage_missing_required_raises():
    with pytest.raises(ValidationError):
        ListUsageRecordsRequest()


def test_list_usage_missing_enddate_raises():
    with pytest.raises(ValidationError):
        ListUsageRecordsRequest(startdate=datetime(2024, 1, 1))


def test_list_usage_date_serialization_format():
    tz = timezone(timedelta(hours=5, minutes=30))
    req = ListUsageRecordsRequest(
        startdate=datetime(2024, 6, 15, 10, 30, 0, tzinfo=tz),
        enddate=datetime(2024, 6, 30, 23, 59, 59, tzinfo=tz),
    )
    dumped = req.model_dump(exclude_none=True)
    assert dumped["startdate"] == "2024-06-15T10:30:00+0530"
    assert dumped["enddate"] == "2024-06-30T23:59:59+0530"


# ---------------------------------------------------------------------------
# GenerateUsageRecordsRequest
# ---------------------------------------------------------------------------

def test_generate_usage_all_optional():
    req = GenerateUsageRecordsRequest()
    dumped = req.model_dump(exclude_none=True)
    assert dumped == {}


def test_generate_usage_with_dates_serializes():
    req = GenerateUsageRecordsRequest(
        startdate=datetime(2024, 6, 1),
        enddate=datetime(2024, 6, 30),
    )
    dumped = req.model_dump(exclude_none=True)
    assert dumped["startdate"] == "2024-06-01"
    assert dumped["enddate"] == "2024-06-30"


def test_generate_usage_with_domainid():
    req = GenerateUsageRecordsRequest(domainId="dom-1")
    dumped = req.model_dump(exclude_none=True)
    assert dumped["domainid"] == "dom-1"


def test_generate_usage_optional_fields_excluded_when_none():
    req = GenerateUsageRecordsRequest()
    dumped = req.model_dump(exclude_none=True)
    assert "startdate" not in dumped
    assert "enddate" not in dumped
    assert "domainid" not in dumped


def test_generate_usage_enddate_before_startdate_raises():
    with pytest.raises(ValidationError, match="enddate must be >= startdate"):
        GenerateUsageRecordsRequest(
            startdate=datetime(2024, 6, 30),
            enddate=datetime(2024, 6, 1),
        )


def test_generate_usage_date_format_is_yyyy_mm_dd():
    req = GenerateUsageRecordsRequest(
        startdate=datetime(2024, 1, 15, 10, 30, 0),
        enddate=datetime(2024, 1, 31, 23, 59, 59),
    )
    dumped = req.model_dump(exclude_none=True)
    assert dumped["startdate"] == "2024-01-15"
    assert dumped["enddate"] == "2024-01-31"


# ---------------------------------------------------------------------------
# RemoveRawUsageRecordsRequest
# ---------------------------------------------------------------------------

def test_remove_raw_usage_required_interval():
    req = RemoveRawUsageRecordsRequest(interval=10)
    dumped = req.model_dump(exclude_none=True)
    assert dumped["interval"] == 10


def test_remove_raw_usage_missing_interval_raises():
    with pytest.raises(ValidationError):
        RemoveRawUsageRecordsRequest()
