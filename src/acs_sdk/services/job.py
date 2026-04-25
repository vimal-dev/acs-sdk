# services/job.py
from typing import Dict, List

from acs_sdk.schemas.request.job import ListAsyncJobsRequest, QueryAsyncJobRequest

from .base import BaseService
from ..schemas.response.base import APIResponse


class Job(BaseService):

    _STATUS_LABLELS = {
        0: "In Progress",
        1: "Success",
        2: "Failure"
    }

    def list(self, payload: ListAsyncJobsRequest) -> APIResponse[List[Dict]]:
        response = self.client.call("listAsyncJobs", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listasyncjobsresponse' in response:
            response = response['listasyncjobsresponse']
        if 'asyncjob' in response and response['asyncjob']:
            data = response['asyncjob']
            count = response['count']
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    async def list_async(self, payload: ListAsyncJobsRequest) -> APIResponse[List[Dict]]:
        response = await self.client.async_call("listAsyncJobs", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listasyncjobsresponse' in response:
            response = response['listasyncjobsresponse']
        if 'asyncjob' in response and response['asyncjob']:
            data = response['asyncjob']
            count = response['count']
        return APIResponse[List[Dict]](**{"data": data, "count": count})
    

    def query(self, payload: QueryAsyncJobRequest) -> APIResponse[Dict]:
        response = self.client.call("queryAsyncJobResult", payload.model_dump(exclude_none=True))
        data = {}
        if 'queryasyncjobresultresponse' in response:
            data = response['queryasyncjobresultresponse']
        return APIResponse[Dict](**{"data": data})

    async def query_async(self, payload: QueryAsyncJobRequest) -> APIResponse[Dict]:
        response = await self.client.async_call("queryAsyncJobResult", payload.model_dump(exclude_none=True))
        data = {}
        if 'queryasyncjobresultresponse' in response:
            data = response['queryasyncjobresultresponse']
        return APIResponse[Dict](**{"data": data})
    

    def poll(self, job_id: str, interval: int = 5, timeout: int = 300, max_attempts: int = 60) -> APIResponse[Dict]:
        import time
        start_time = time.monotonic()
        attempts = 0
        while True:
            response = self.query(QueryAsyncJobRequest(jobid=job_id))
            elapsed = time.monotonic() - start_time
            job_status = response.data.get('jobstatus')
            job_progress = response.data.get('jobprocstatus')

            if job_status == 1:
                """Job completed successfully, return the result."""
                return APIResponse[Dict](**{"data": {
                    "status": job_status,
                    "status_label": self._STATUS_LABLELS.get(job_status, "Unknown"),
                    "progress": job_progress,
                    "entity": response.data.get('jobinstancetype'),
                    "entity_id": response.data.get('jobinstanceid'),
                    "result": response.data.get('jobresult'),
                    "elapsed_seconds": elapsed,
                    "attempts": attempts
                }})
            
            if job_status == 2:
                """Job failed, return the failure status."""
                return APIResponse[Dict](**{"data": {
                    "status": job_status,
                    "status_label": self._STATUS_LABLELS.get(job_status, "Unknown"),
                    "progress": job_progress,
                    "entity": response.data.get('jobinstancetype'),
                    "entity_id": response.data.get('jobinstanceid'),
                    "result": {},
                    "elapsed_seconds": elapsed,
                    "attempts": attempts
                }})
            
            if elapsed > timeout:
                raise TimeoutError(f"Job {job_id} did not complete within {timeout} seconds.")
            attempts += 1
            if attempts >= max_attempts:
                raise TimeoutError(f"Job {job_id} did not complete within {max_attempts} attempts.")
            time.sleep(interval)


    async def poll_async(self, job_id: str, interval: int = 5, timeout: int = 300, max_attempts: int = 60) -> APIResponse[Dict]:
        import asyncio
        start_time = asyncio.get_event_loop().time()
        attempts = 0
        while True:
            response = await self.query_async(QueryAsyncJobRequest(jobid=job_id))
            elapsed = asyncio.get_event_loop().time() - start_time
            job_status = response.data.get('jobstatus')
            job_progress = response.data.get('jobprocstatus')

            if job_status == 1:
                """Job completed successfully, return the result."""
                return APIResponse[Dict](**{"data": {
                    "status": job_status,
                    "status_label": self._STATUS_LABLELS.get(job_status, "Unknown"),
                    "progress": job_progress,
                    "entity": response.data.get('jobinstancetype'),
                    "entity_id": response.data.get('jobinstanceid'),
                    "result": response.data.get('jobresult'),
                    "elapsed_seconds": elapsed,
                    "attempts": attempts
                }})
            
            if job_status == 2:
                """Job failed, return the failure status."""
                return APIResponse[Dict](**{"data": {
                    "status": job_status,
                    "status_label": self._STATUS_LABLELS.get(job_status, "Unknown"),
                    "progress": job_progress,
                    "entity": response.data.get('jobinstancetype'),
                    "entity_id": response.data.get('jobinstanceid'),
                    "result": {},
                    "elapsed_seconds": elapsed,
                    "attempts": attempts
                }})
            
            if elapsed > timeout:
                raise TimeoutError(f"Job {job_id} did not complete within {timeout} seconds.")
            attempts += 1
            if attempts >= max_attempts:
                raise TimeoutError(f"Job {job_id} did not complete within {max_attempts} attempts.")
            await asyncio.sleep(interval)
