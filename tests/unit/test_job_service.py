from unittest.mock import Mock

from acs_sdk.core.timer import DefaultTimer
from acs_sdk.schemas.request.job import ListAsyncJobsRequest, QueryAsyncJobRequest
from acs_sdk.services.job import Job


def test_job_list_parses_list_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "listasyncjobsresponse": {
            "asyncjob": [{"id": "job-1"}],
            "count": 1,
        }
    }

    job = Job(client=mock_client)
    payload = ListAsyncJobsRequest()
    response = job.list(payload)

    assert response.data == [{"id": "job-1"}]
    assert response.count == 1
    mock_client.call.assert_called_once_with("listAsyncJobs", payload.model_dump(exclude_none=True))


def test_job_query_parses_query_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "queryasyncjobresultresponse": {
            "jobstatus": 1,
            "jobresult": {"foo": "bar"},
        }
    }

    job = Job(client=mock_client)
    response = job.query(QueryAsyncJobRequest(jobid="job-1"))

    assert response.data["jobstatus"] == 1
    assert response.data["jobresult"] == {"foo": "bar"}
    mock_client.call.assert_called_once_with("queryAsyncJobResult", {"jobid": "job-1"})


def test_job_poll_returns_success_on_job_completion():
    mock_client = Mock()
    mock_client.call.return_value = {
        "queryasyncjobresultresponse": {
            "jobstatus": 1,
            "jobprocstatus": 100,
            "jobinstancetype": "vm",
            "jobinstanceid": "vm-1",
            "jobresult": {"name": "ok"},
        }
    }

    mock_timer = Mock(spec=DefaultTimer)
    mock_timer.monotonic.side_effect = [0.0, 0.0]  # start and check

    job = Job(client=mock_client, timer=mock_timer)
    response = job.poll("job-1", interval=0, timeout=10, max_attempts=3)

    assert response.data["status"] == 1
    assert response.data["status_label"] == "Success"
    assert response.data["entity"] == "vm"
    assert response.data["entity_id"] == "vm-1"
    assert response.data["result"] == {"name": "ok"}
    assert response.data["attempts"] == 0
