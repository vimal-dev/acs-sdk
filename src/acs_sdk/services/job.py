# services/job.py
from typing import Dict

from acs_sdk.schemas.request.job import ListAsyncJobsRequest, QueryAsyncJobRequest

from .base import BaseService
from ..schemas.response.base import APIResponse


class Job(BaseService):
    def list(self, payload: ListAsyncJobsRequest) -> APIResponse[Dict]:
        data = self.client.call("listAsyncJobs", payload.model_dump(exclude_none=True))
        return APIResponse[Dict](**data)

    async def list_async(self, payload: ListAsyncJobsRequest) -> APIResponse[Dict]:
        data = await self.client.async_call("listAsyncJobs", payload.model_dump(exclude_none=True))
        return APIResponse[Dict](**data)
    

    def query(self, payload: QueryAsyncJobRequest) -> APIResponse[Dict]:
        data = self.client.call("queryAsyncJobResult", payload.model_dump(exclude_none=True))
        return APIResponse[Dict](**data)

    async def query_async(self, payload: QueryAsyncJobRequest) -> APIResponse[Dict]:
        data = await self.client.async_call("queryAsyncJobResult", payload.model_dump(exclude_none=True))
        return APIResponse[Dict](**data)
