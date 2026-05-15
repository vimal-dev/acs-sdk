import click

from acs_sdk.schemas.request.template import ListTemplatesRequest

from .dependencies import get_acs_client

if __name__ == "__main__":
    acs_client = get_acs_client()
    payload = ListTemplatesRequest(listAll=True, templateFilter="all")
    response = acs_client.template.list(payload)
    if response.is_ok:
        templates = response.data
        click.echo(click.style("\n📍 Available Templates:\n", fg="green", bold=True))

        for i, template in enumerate(templates, 1):
            click.echo(f"{i}. {template.get('name')} (ID: {template.get('id')})")
            click.echo(f"   {template.get('displaytext')}")
            click.echo(f"   CPU Architecture: {template.get('arch')}")
            click.echo(f"   Hypervisor: {template.get('hypervisor')}")
            click.echo(f"   Format: {template.get('format')}")
            click.echo(f"   Template Status: {template.get('status')}")
            click.echo(f"   Template Type: {template.get('templatetype')}")
            click.echo(f"   Template Size: {template.get('size')}")
            click.echo(
                f"   Template OS: {template.get('ostypename')} (ID: {template.get('ostypeid')}) "
            )
            click.echo(f"   Cross Zones: {template.get('crossZones')}")
            click.echo(f"   Zone: {template.get('zonename')} (ID: {template.get('zoneid')}) ")
            click.echo("   Template Flags: ")
            click.echo(f"       Is Public: {template.get('ispublic')}")
            click.echo(f"       Is Ready: {template.get('isready')}")
            click.echo(f"       Is Featured: {template.get('isfeatured')}")
            click.echo(f"       Is Extractable: {template.get('isextractable')}")
            click.echo(f"       SSHKey Enabled: {template.get('sshkeyenabled')}")
            click.echo(f"       For CKS: {template.get('forcks')}")
            click.echo()
    else:
        acs_client.logger.error(f"Error initiating cleanup: {response.error}")
