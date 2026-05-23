# services/job.py
import enum
from typing import Callable, Dict, List, Optional

from acs_sdk.schemas.request.job import ListAsyncJobsRequest, QueryAsyncJobRequest

from .base import BaseService
from ..core.response_mapper import ResponseMapper
from ..core.timer import DefaultTimer, Timer
from ..schemas.response.base import APIResponse


class JobStatus(enum.IntEnum):
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


class Job(BaseService):
    def __init__(
        self,
        client,
        response_mapper: Optional[ResponseMapper] = None,
        timer: Optional[Timer] = None,
    ):
        super().__init__(client, response_mapper)
        self.timer = timer or DefaultTimer()

    def list(self, payload: ListAsyncJobsRequest) -> APIResponse[List[Dict]]:
        return self._execute(
            "listAsyncJobs",
            payload,
            envelope="listasyncjobsresponse",
            entity="asyncjob",
        )

    async def list_async(self, payload: ListAsyncJobsRequest) -> APIResponse[List[Dict]]:
        return await self._execute_async(
            "listAsyncJobs",
            payload,
            envelope="listasyncjobsresponse",
            entity="asyncjob",
        )

    def query(self, payload: QueryAsyncJobRequest) -> APIResponse[Dict]:
        return self._execute(
            "queryAsyncJobResult",
            payload,
            envelope="queryasyncjobresultresponse",
        )

    async def query_async(self, payload: QueryAsyncJobRequest) -> APIResponse[Dict]:
        return await self._execute_async(
            "queryAsyncJobResult",
            payload,
            envelope="queryasyncjobresultresponse",
        )

    def _build_poll_response(
        self,
        data: Dict,
        elapsed_seconds: float,
        attempts: int,
        success: bool,
    ) -> APIResponse[Dict]:
        status_code = data.get("jobstatus")
        status = JobStatus(status_code) if status_code in JobStatus._value2member_map_ else None

        return APIResponse[Dict](
            **{
                "data": {
                    "status": status_code,
                    "status_label": status.label if status is not None else "Unknown",
                    "progress": data.get("jobprocstatus"),
                    "entity": data.get("jobinstancetype"),
                    "entity_id": data.get("jobinstanceid"),
                    "result": data.get("jobresult") if success else {},
                    "error": None
                    if success
                    else data.get("jobresult", {}).get("errortext") or "Job failed",
                    "elapsed_seconds": elapsed_seconds,
                    "attempts": attempts,
                }
            }
        )

    def poll(
        self,
        job_id: str,
        interval: int = 5,
        timeout: int = 300,
        max_attempts: int = 60,
        sleep_func: Optional[Callable[[int], None]] = None,
        time_func: Optional[Callable[[], float]] = None,
    ) -> APIResponse[Dict]:
        start_time = time_func() if time_func is not None else self.timer.monotonic()
        attempts = 0
        sleep = sleep_func or self.timer.sleep
        time_get = time_func or self.timer.monotonic

        while True:
            response = self.query(QueryAsyncJobRequest(jobid=job_id))
            data = response.data or {}
            elapsed = time_get() - start_time
            status_code = data.get("jobstatus")
            status = JobStatus(status_code) if status_code in JobStatus._value2member_map_ else None

            if status == JobStatus.SUCCESS:
                return self._build_poll_response(data, elapsed, attempts, success=True)

            if status == JobStatus.FAILURE:
                return self._build_poll_response(data, elapsed, attempts, success=False)

            if elapsed > timeout:
                raise TimeoutError(f"Job {job_id} did not complete within {timeout} seconds.")

            attempts += 1
            if attempts >= max_attempts:
                raise TimeoutError(f"Job {job_id} did not complete within {max_attempts} attempts.")

            sleep(interval)

    async def poll_async(
        self,
        job_id: str,
        interval: int = 5,
        timeout: int = 300,
        max_attempts: int = 60,
        sleep_func: Optional[Callable[[int], None]] = None,
        time_func: Optional[Callable[[], float]] = None,
    ) -> APIResponse[Dict]:
        start_time = time_func() if time_func is not None else self.timer.async_time()
        attempts = 0
        sleep = sleep_func or self.timer.async_sleep
        time_get = time_func or self.timer.async_time

        while True:
            response = await self.query_async(QueryAsyncJobRequest(jobid=job_id))
            data = response.data or {}
            current_time = time_get()
            elapsed = current_time - start_time
            status_code = data.get("jobstatus")
            status = JobStatus(status_code) if status_code in JobStatus._value2member_map_ else None

            if status == JobStatus.SUCCESS:
                return self._build_poll_response(data, elapsed, attempts, success=True)

            if status == JobStatus.FAILURE:
                return self._build_poll_response(data, elapsed, attempts, success=False)

            if elapsed > timeout:
                raise TimeoutError(f"Job {job_id} did not complete within {timeout} seconds.")

            attempts += 1
            if attempts >= max_attempts:
                raise TimeoutError(f"Job {job_id} did not complete within {max_attempts} attempts.")

            await sleep(interval)
