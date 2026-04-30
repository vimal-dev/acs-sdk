import click

from acs_sdk.schemas.request.disk_offering import ListDiskOfferingRequest

from .dependencies import get_acs_client

if __name__ == "__main__":
    try:
        acs_client = get_acs_client()
        payload = ListDiskOfferingRequest(listAll=True)
        response = acs_client.diskoffering.list(payload)
        if response.is_ok:
            disk_offerings = response.data
            click.echo(click.style("\n� Available Disk Offerings:\n", fg="green", bold=True))

            for i, disk_offering in enumerate(disk_offerings, 1):
                click.echo(f"{i}. {disk_offering.get('name')} (ID: {disk_offering.get('id')})")
                click.echo(f"   Endpoint: {disk_offering.get('endpoint')}")
                click.echo()
        else:
            acs_client.logger.error(f"Error initiating cleanup: {response.error}")
    except Exception as e:
        click.echo(click.style(f"Error: {str(e)}", fg="red", bold=True))
        exit(1)
