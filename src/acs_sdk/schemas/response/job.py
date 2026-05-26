import uuid
from enum import IntEnum
from typing import Any
from pydantic import BaseModel, ConfigDict, Field


class JobStatus(IntEnum):
    IN_PROGRESS = 0
    SUCCESS = 1
    FAILURE = 2

    @property
    def label(self) -> str:
        return {
            JobStatus.IN_PROGRESS: "In Progress",
            JobStatus.SUCCESS: "Success",
            JobStatus.FAILURE: "Failure",
        }.get(self, "Unknown")


class AsyncCommandResponse(BaseModel):
    """
    Schema for async command response from Apache CloudStack API.
    Returned immediately when an async operation is triggered 
    (e.g. associateIpAddress, deleteVolume, deployVirtualMachine).
    """
    jobId: uuid.UUID = Field(
        ...,
        alias="jobid",
        description="CloudStack async job ID to poll for completion status.",
    )
    id: uuid.UUID | None = Field(
        None,
        description="CloudStack resource ID, returned for create-type commands.",
    )

    model_config = ConfigDict(populate_by_name=True, use_enum_values=True)


class AsyncJobResultResponse(BaseModel):
    """
    Schema for queryAsyncJobResult response from Apache CloudStack API.
    Polled by Celery tasks (e.g. poll_address_associate_status) until
    job_status is SUCCESS or FAILED.
    """
    job_id: uuid.UUID = Field(..., alias="jobid")
    job_status: JobStatus = Field(..., alias="jobstatus")
    job_result_code: int = Field(..., alias="jobresultcode")
    job_result_type: str | None = Field(None, alias="jobresulttype")

    # Contains the actual created/updated resource on SUCCESS,
    # or error details on FAILED.
    job_result: dict[str, Any] | None = Field(None, alias="jobresult")

    model_config = {"populate_by_name": True}

    @property
    def is_pending(self) -> bool:
        return self.job_status == JobStatus.PENDING

    @property
    def is_success(self) -> bool:
        return self.job_status == JobStatus.SUCCESS

    @property
    def is_failed(self) -> bool:
        return self.job_status == JobStatus.FAILED

    @property
    def error_message(self) -> str | None:
        """Extract error text from job_result on failure."""
        if self.is_failed and self.job_result:
            error = self.job_result.get("errortext")
            return error
        return None

    @property
    def resource(self) -> dict[str, Any] | None:
        """Extract the resource payload from job_result on success."""
        if self.is_success and self.job_result:
            # CloudStack wraps the result under the resource type key
            # e.g. {"ipaddress": {...}} or {"virtualmachine": {...}}
            values = list(self.job_result.values())
            return values[0] if values else None
        return None