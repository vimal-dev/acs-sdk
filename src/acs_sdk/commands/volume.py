from acs_sdk import ApacheCloudStack
import click

from acs_sdk.schemas.request.virtual_machine import ListVirtualMachinesRequest

@click.command("list:volumes", help="List all volumes available in CloudStack")
@click.pass_context
def list_volumes(ctx):
    """List all volumes available in CloudStack."""
    try:
        config = ctx.obj['config']
        acs = ApacheCloudStack(config)
        try:
            payload = ListVirtualMachinesRequest(listall=True, pagesize=100)
            response = acs.volume.list(payload)
            
            if len(response.data) > 0:
                volumes = response.data
                click.echo(click.style("\n📍 Available Volumes:\n", fg="green", bold=True))
                
                for i, volume in enumerate(volumes, 1):
                    click.echo(f"{i}. {volume.get('name')} (ID: {volume.get('id')})")
                    click.echo(f"   Type: {volume.get('type')}")
                    click.echo()
            else:
                click.echo(click.style("No volumes found.", fg="yellow"))
        finally:
            acs.client.close()
    except Exception as e:
        click.echo(click.style(f"❌ Error: {str(e)}", fg="red"), err=True)
        #raise click.Exit(1)