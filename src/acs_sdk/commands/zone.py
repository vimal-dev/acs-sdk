from acs_sdk import ApacheCloudStack
import click

@click.command("list:zones", help="List all zones available in CloudStack")
@click.pass_context
def list_zones(ctx):
    """List all zones available in CloudStack."""
    try:
        config = ctx.obj['config']
        acs = ApacheCloudStack(config)
        try:
            response = acs.client.call('listZones')
            
            if 'listzonesresponse' in response:
                response = response['listzonesresponse']
            if 'zone' in response and response['zone']:
                zones = response['zone']
                click.echo(click.style("\n📍 Available Zones:\n", fg="green", bold=True))
                
                for i, zone in enumerate(zones, 1):
                    click.echo(f"{i}. {zone.get('name')} (ID: {zone.get('id')})")
                    click.echo(f"   Type: {zone.get('type')}")
                    click.echo()
            else:
                click.echo(click.style("No zones found.", fg="yellow"))
        finally:
            acs.client.close()
    except Exception as e:
        click.echo(click.style(f"❌ Error: {str(e)}", fg="red"), err=True)
        #raise click.Exit(1)