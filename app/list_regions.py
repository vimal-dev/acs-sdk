import click

from acs_sdk.schemas.request.region import ListRegionsRequest

from .dependencies import get_acs_client

if __name__ == "__main__":
    
    acs_client = get_acs_client()
    payload = ListRegionsRequest()
    response = acs_client.region.list(payload)
    if response.is_ok:
        regions = response.data
        click.echo(click.style("\n📍 Available Regions:\n", fg="green", bold=True))
        
        for i, region in enumerate(regions, 1):
            click.echo(f"{i}. {region.get('name')} (ID: {region.get('id')})")
            click.echo(f"   Endpoint: {region.get('endpoint')}")
            click.echo()
    else:
        acs_client.logger.error(f"Error initiating cleanup: {response.error}")