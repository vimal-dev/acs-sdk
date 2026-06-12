import click

from acs_sdk.schemas.request.iso import ListIsosRequest

from .dependencies import get_acs_client

if __name__ == "__main__":
    try:
        acs_client = get_acs_client()
        payload = ListIsosRequest(listAll=True)
        response = acs_client.iso.list(payload)
        if response.is_ok:
            isos = response.data
            click.echo(click.style("\n� Available ISOs:\n", fg="green", bold=True))

            for i, iso in enumerate(isos, 1):
                click.echo(f"{i}. {iso.get('name')} (ID: {iso.get('id')})")
                click.echo(f"   Arch: {iso.get('arch')}")
                click.echo(f"   Hypervisor: {iso.get('hypervisor')}")
                click.echo()
        else:
            acs_client.logger.error(f"Error initiating cleanup: {response.error}")
    except Exception as e:
        click.echo(click.style(f"Error: {str(e)}", fg="red", bold=True))
        exit(1)
