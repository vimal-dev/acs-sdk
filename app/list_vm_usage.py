import click

from acs_sdk.schemas.request.usage import ListUsageRecordsRequest

from .dependencies import get_acs_client

if __name__ == "__main__":
    acs_client = get_acs_client()
    # response = acs_client.client.call("listUsageRecords", {
    #     "startdate": "2026-04-01T00:00:00",
    #     "enddate": "2026-04-30T23:59:59",
    # })
    # pprint(response)
    payload = ListUsageRecordsRequest(
        startdate="2025-04-01T00:00:00", enddate="2026-04-30T23:59:59"
    )
    response = acs_client.vm.lis(payload)
    if response.is_ok:
        usage_records = response.data if response.data else []
        if not usage_records:
            click.echo(
                click.style("No usage records found for the specified date range.", fg="yellow")
            )
            exit(0)
        click.echo(click.style("\n📍 Available Usage Records:\n", fg="green", bold=True))

        for i, usage_record in enumerate(usage_records, 1):
            click.echo(f"{i}. {usage_record.get('usagetype')} (ID: {usage_record.get('id')})")
            click.echo(f"   Usage Hours: {usage_record.get('usage')}")
            click.echo()
    else:
        acs_client.logger.error(f"Error initiating cleanup: {response.error}")
