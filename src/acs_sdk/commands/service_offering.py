from pydantic import ValidationError

from acs_sdk import ApacheCloudStack
import click

from acs_sdk.schemas.request.service_offering import ListServiceOfferingsRequest

@click.command("list:service-offerings", help="List all service offerings available in CloudStack")
@click.pass_context
def list_service_offerings(ctx):
    """List all service offerings available in CloudStack."""
    try:
        config = ctx.obj['config']
        acs = ApacheCloudStack(config)
        try:
            payload = ListServiceOfferingsRequest()
            response = acs.serviceoffering.list(payload)
            if len(response.data) > 0:
                offerings = response.data
                click.echo(click.style("\n📍 Available Service Offerings:\n", fg="green", bold=True))
                
                for i, offering in enumerate(offerings, 1):
                    click.echo(f"{i}. {offering.get('name')} (ID: {offering.get('id')})")
                    click.echo(f"       CPU: {offering.get('cpunumber')} X {offering.get('cpuspeed')} MHz ({offering.get('arch')})")
                    click.echo(f"       MEM: {offering.get('memory')}")
                    click.echo()
            else:
                click.echo(click.style("No service offerings found.", fg="yellow"))
        except ValidationError as e:
            click.echo(click.style(f"❌ Validation Error: {str(e)}", fg="red"), err=True)
        finally:
            acs.client.close()
    except Exception as e:
        click.echo(click.style(f"❌ Error: {str(e)}", fg="red"), err=True)
        if isinstance(e, ValidationError):
            click.echo(click.style("Please check the input parameters and try again.", fg="yellow"))
        #raise click.Exit(1)