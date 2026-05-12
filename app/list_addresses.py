import click

from acs_sdk.schemas.request.address import ListPublicIpAddressesRequest

from .dependencies import get_acs_client

if __name__ == "__main__":
    acs_client = get_acs_client()
    payload = ListPublicIpAddressesRequest(state="Free")
    response = acs_client.address.list_public_ip_addresses(payload)
    if response.is_ok:
        addresses = response.data
        click.echo(click.style("\n📍 Available Addresses:\n", fg="green", bold=True))

        for i, address in enumerate(addresses, 1):
            click.echo(f"{i}. {address.get('ipaddress')} (ID: {address.get('id')})")
            click.echo(f"   State: {address.get('state')}")
            click.echo()
    else:
        acs_client.logger.error(f"Error initiating cleanup: {response.error}")
