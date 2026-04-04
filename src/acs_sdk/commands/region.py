
from pprint import pprint

from acs_sdk.client.client import ApacheCloudStackClient
import click

@click.command("list:regions", help="List all regions available in CloudStack")
@click.pass_context
def list_regions(ctx):
    """List all regions available in CloudStack."""
    try:
        config = ctx.obj['config']
        client = ApacheCloudStackClient(config)
        try:
            response = client.call('listRegions')
            pprint(response)
            if 'listregionsresponse' in response:
                response = response['listregionsresponse']
            if 'region' in response and response['region']:
                regions = response['region']
                click.echo(click.style("\n📍 Available Regions:\n", fg="green", bold=True))
                
                for i, region in enumerate(regions, 1):
                    click.echo(f"{i}. {region.get('name')} (ID: {region.get('id')})")
                    click.echo(f"   Endpoint: {region.get('endpoint')}")
                    click.echo()
            else:
                click.echo(click.style("No regions found.", fg="yellow"))
        finally:
            client.close()
    except Exception as e:
        click.echo(click.style(f"❌ Error: {str(e)}", fg="red"), err=True)
        #raise click.Exit(1)