import click

from acs_sdk.schemas.request.network_offering import ListNetworkOfferingRequest

from .dependencies import get_acs_client

if __name__ == "__main__":
    acs_client = get_acs_client()
    payload = ListNetworkOfferingRequest()
    response = acs_client.networkoffering.list(payload)
    if response.is_ok:
        network_offerings = response.data
        click.echo(click.style("\n Available Network Offerings:\n", fg="green", bold=True))

        for i, network_offering in enumerate(network_offerings, 1):
            click.echo(f"{i}. {network_offering.get('name')} (ID: {network_offering.get('id')})")
            click.echo(f"   Endpoint: {network_offering.get('endpoint')}")
            click.echo()
    else:
        acs_client.logger.error(f"Error initiating cleanup: {response.error}")
