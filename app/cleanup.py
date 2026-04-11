from acs_sdk.schemas.request.job import QueryAsyncJobRequest

from .dependencies import get_acs_client

if __name__ == "__main__":
    acs_client = get_acs_client()
    response = acs_client.vm.clean_vm_reservations()
    if response.is_ok:
        acs_client.logger.info("Cleanup initiated successfully.")
        job_id = response.data.get("jobid")
        acs_client.logger.info(f"Job ID: {job_id}")
        pending = True
        while pending:
            payload = QueryAsyncJobRequest(jobid=job_id)
            job_response = acs_client.job.query(payload)
            if job_response.is_ok:
                job_result = job_response.data
                acs_client.logger.info(f"Job Status: {job_result.get('jobstatus')}")
                if job_result.get("jobstatus") == 1:  # Success
                    acs_client.logger.info("VM reservations cleaned successfully.")
                    pending = False
                elif job_result.get("jobstatus") == 2:  # Failed
                    acs_client.logger.error("Failed to clean VM reservations.")
                    pending = False
            else:
                acs_client.logger.error(f"Error querying job status: {job_response.error}")
                pending = False
    else:
        acs_client.logger.error(f"Error initiating cleanup: {response.error}")