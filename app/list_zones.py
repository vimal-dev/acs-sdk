from pprint import pprint

import click

from acs_sdk.schemas.request.zone import ListZonesRequest

from .dependencies import get_acs_client

if __name__ == "__main__":
    
    acs_client = get_acs_client()
    payload = ListZonesRequest()
    response = acs_client.zone.list(payload)
    if response.is_ok:
        zones = response.data
        click.echo(click.style("\n📍 Available Zones:\n", fg="green", bold=True))
        
        for i, zone in enumerate(zones, 1):
            click.echo(f"{i}. {zone.get('name')} (ID: {zone.get('id')})")
            click.echo(f"   Network Type: {zone.get('networktype')}")
            click.echo()
    else:
        acs_client.logger.error(f"Error initiating cleanup: {response.error}")