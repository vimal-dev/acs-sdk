import click

from acs_sdk.schemas.request.vpc_offering import ListVPCOfferingRequest

from .dependencies import get_acs_client

if __name__ == "__main__":
    
    acs_client = get_acs_client()
    payload = ListVPCOfferingRequest(listall=True)
    response = acs_client.vpcoffering.list(payload)
    if response.is_ok:
        vpc_offerings = response.data
        click.echo(click.style("\n Available VPC Offerings:\n", fg="green", bold=True))
        
        for i, vpc_offering in enumerate(vpc_offerings, 1):
            click.echo(f"{i}. {vpc_offering.get('name')} (ID: {vpc_offering.get('id')})")
            click.echo(f"   Endpoint: {vpc_offering.get('endpoint')}")
            click.echo()
    else:
        acs_client.logger.error(f"Error initiating cleanup: {response.error}")