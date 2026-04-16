import click

from acs_sdk.schemas.request.vpc import ListVPCRequest

from .dependencies import get_acs_client

if __name__ == "__main__":
    
    acs_client = get_acs_client()
    payload = ListVPCRequest(listall=True)
    response = acs_client.vpc.list_vpc(payload)
    if response.is_ok:
        regions = response.data
        click.echo(click.style("\n📍 Available VPCs:\n", fg="green", bold=True))
        
        for i, region in enumerate(regions, 1):
            click.echo(f"{i}. {region.get('name')} (ID: {region.get('id')})")
            click.echo(f"   Zone: {region.get('zonename')}")
            click.echo(f"   CIDR: {region.get('cidr')}")
            click.echo(f"   State: {region.get('state')}")
            click.echo()
    else:
        acs_client.logger.error(f"Error getting VPCs: {response.error}")