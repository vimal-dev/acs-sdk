import click

from acs_sdk.schemas.request.service_offering import ListServiceOfferingRequest

from .dependencies import get_acs_client

if __name__ == "__main__":
    acs_client = get_acs_client()
    payload = ListServiceOfferingRequest()
    response = acs_client.serviceoffering.list(payload)
    if response.is_ok:
        service_offerings = response.data
        click.echo(click.style("\n Available Service Offerings:\n", fg="green", bold=True))

        for i, service_offering in enumerate(service_offerings, 1):
            click.echo(f"{i}. {service_offering.get('name')} (ID: {service_offering.get('id')})")
            click.echo(f"   Endpoint: {service_offering.get('endpoint')}")
            click.echo()
    else:
        acs_client.logger.error(f"Error initiating cleanup: {response.error}")
