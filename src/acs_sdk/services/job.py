# services/job.py
from typing import Dict, List

from acs_sdk.schemas.request.job import ListAsyncJobsRequest, QueryAsyncJobRequest

from .base import BaseService
from ..schemas.response.base import APIResponse


class Job(BaseService):
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
