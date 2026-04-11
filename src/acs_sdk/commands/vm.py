import pprint

from acs_sdk import ApacheCloudStack
import click

from acs_sdk.schemas.request.virtual_machine import ListVirtualMachinesRequest

@click.command("list:vm", help="List all virtual machines available in CloudStack")
@click.pass_context
def list_vms(ctx):
    """List all virtual machines available in CloudStack."""
    try:
        config = ctx.obj['config']
        acs = ApacheCloudStack(config)
        try:
            payload = ListVirtualMachinesRequest(listall=True, pagesize=100)
            response = acs.vm.list(payload)
            
            if len(response.data) > 0:
                vms = response.data
                click.echo(click.style("\n📍 Available Virtual Machines:\n", fg="green", bold=True))
                
                for i, vm in enumerate(vms, 1):
                    click.echo(f"{i}. {vm.get('name')} (ID: {vm.get('id')})")
                    click.echo(f"   Instance Type: {vm.get('serviceofferingname')}")
                    click.echo(f"       CPU: {vm.get('cpunumber')} X {vm.get('cpuspeed')} MHz ({vm.get('arch')})")
                    click.echo(f"       MEM: {vm.get('memory')}")
                    click.echo(f"   State: {vm.get('state')}")
                    click.echo(f"   IP: {vm.get('ipaddress')}")
                    click.echo(f"   OS: {vm.get('osdisplayname')}")
                    click.echo(f"   Zone: {vm.get('zonename')}")
                    click.echo(f"   Created: {vm.get('created')}")

                    click.echo()
            else:
                click.echo(click.style("No virtual machines found.", fg="yellow"))
        finally:
            acs.client.close()
    except Exception as e:
        click.echo(click.style(f"❌ Error: {str(e)}", fg="red"), err=True)
        #raise click.Exit(1)