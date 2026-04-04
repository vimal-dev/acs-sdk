"""Command-line interface module for Apache CloudStack SDK.

This module provides CLI functionality for interacting with Apache CloudStack
from the command line, offering a convenient alternative to programmatic usage.
"""

import click

from acs_sdk.commands.vm import list_vms
from acs_sdk.commands.zone import list_zones
from acs_sdk.schemas.config import ApacheCloudStackConfig
from acs_sdk.commands.region import list_regions


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


console.add_command(list_regions)
console.add_command(list_zones)
console.add_command(list_vms)


if __name__ == '__main__':
    console()