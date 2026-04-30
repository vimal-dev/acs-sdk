import click

from .dependencies import get_acs_client

if __name__ == "__main__":
    acs_client = get_acs_client()
    response = acs_client.usage.list_usage_types()
    if response.is_ok:
        usage_records = response.data if response.data else []
        if not usage_records:
            click.echo(click.style("No usage types found.", fg="yellow"))
            exit(0)
        click.echo(click.style("\n📍 Available Usage Type Records:\n", fg="green", bold=True))

        for i, usage_record in enumerate(usage_records, 1):
            click.echo(f"{i}. {usage_record.get('name')} (ID: {usage_record.get('id')})")
            click.echo(f"    Description: {usage_record.get('description')}")
            click.echo()
    else:
        acs_client.logger.error(f"Error initiating cleanup: {response.error}")
