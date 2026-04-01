"""Command-line interface module for Apache CloudStack SDK.

This module provides CLI functionality for interacting with Apache CloudStack
from the command line, offering a convenient alternative to programmatic usage.
"""

import click

from acs_sdk.client.client import ApacheCloudStackClient
from acs_sdk.schemas.config import ApacheCloudStackConfig


@click.group()
@click.version_option(version="0.1.0")
@click.option('--endpoint', envvar='CLOUDSTACK_ENDPOINT', required=True, help='CloudStack API endpoint')
@click.option('--api-key', envvar='CLOUDSTACK_API_KEY', required=True, help='API key')
@click.option('--api-secret', envvar='CLOUDSTACK_API_SECRET', required=True, help='API secret')
@click.pass_context
def console(ctx, endpoint, api_key, api_secret):
    """Main entry point for the CloudStack CLI.

    This function serves as the command-line interface entry point for the
    Apache CloudStack SDK. It's typically invoked when the acs command
    is run from the terminal.

    Example:
        $ acs list-users
        $ acs create-vm --template ubuntu --zone us-west-1
    """
    # Store config in context for child commands
    ctx.ensure_object(dict)
    ctx.obj['config'] = ApacheCloudStackConfig(
        api_endpoint=endpoint,
        api_key=api_key,
        api_secret=api_secret,
        timeout=10
    )


@console.command()
@click.pass_context
def list_regions(ctx):
    """List all regions available in CloudStack."""
    try:
        config = ctx.obj['config']
        client = ApacheCloudStackClient(config)
        try:
            response = client.call('listRegions')
            
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


if __name__ == '__main__':
    console()