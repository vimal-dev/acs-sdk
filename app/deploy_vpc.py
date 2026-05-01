import click

from acs_sdk.schemas.request.vpc import CreateVPCRequest
from acs_sdk.schemas.request.vpc_offering import ListVPCOfferingRequest
from acs_sdk.schemas.request.network import CreateNetworkRequest
from acs_sdk.schemas.request.network_offering import ListNetworkOfferingRequest
from acs_sdk.schemas.request.zone import ListZonesRequest

from .dependencies import get_acs_client


def get_default_vpc_offering(acs_client, zone_id):
    """Get the default VPC offering for the zone."""
    payload = ListVPCOfferingRequest(isdefault=True, zoneid=zone_id)
    response = acs_client.vpcoffering.list(payload)
    if response.is_ok and response.data:
        return response.data[0]
    # If no default, get the first available
    payload = ListVPCOfferingRequest(zoneid=zone_id)
    response = acs_client.vpcoffering.list(payload)
    if response.is_ok and response.data:
        return response.data[0]
    return None


def get_default_vpc_network_offering(acs_client, zone_id):
    """Get the default network offering for VPC networks."""
    payload = ListNetworkOfferingRequest(forvpc=True, isdefault=True, zoneid=zone_id)
    response = acs_client.networkoffering.list(payload)
    if response.is_ok and response.data:
        return response.data[0]
    # If no default, get the first available for VPC
    payload = ListNetworkOfferingRequest(forvpc=True, zoneid=zone_id)
    response = acs_client.networkoffering.list(payload)
    if response.is_ok and response.data:
        return response.data[0]
    return None


@click.command()
@click.option("--account", required=True, help="Account name for the VPC")
@click.option("--domain-id", required=True, help="Domain ID for the account")
@click.option("--zone-id", help="Zone ID (if not provided, will use the first available zone)")
@click.option("--vpc-name", default="default-vpc", help="Name for the VPC")
@click.option("--vpc-cidr", default="10.0.0.0/16", help="CIDR for the VPC")
@click.option("--subnet1-cidr", default="10.0.1.0/24", help="CIDR for first subnet")
@click.option("--subnet2-cidr", default="10.0.2.0/24", help="CIDR for second subnet")
def deploy_vpc(account, domain_id, zone_id, vpc_name, vpc_cidr, subnet1_cidr, subnet2_cidr):
    """Deploy a default VPC with 2 subnetworks under a specific account."""
    acs_client = get_acs_client()

    # Get zone if not provided
    if not zone_id:
        zones_response = acs_client.zone.list(ListZonesRequest())
        if zones_response.is_ok and zones_response.data:
            zone_id = zones_response.data[0]["id"]
            click.echo(f"Using zone: {zones_response.data[0]['name']} (ID: {zone_id})")
        else:
            click.echo("Error: No zones available", err=True)
            return

    # Get default VPC offering
    vpc_offering = get_default_vpc_offering(acs_client, zone_id)
    if not vpc_offering:
        click.echo("Error: No VPC offering available", err=True)
        return

    click.echo(f"Using VPC offering: {vpc_offering['name']} (ID: {vpc_offering['id']})")

    # Create VPC
    vpc_payload = CreateVPCRequest(
        name=vpc_name,
        vpcofferingid=vpc_offering["id"],
        zoneid=zone_id,
        cidr=vpc_cidr,
        account=account,
        domainid=domain_id,
        displaytext=f"Default VPC for {account}"
    )

    try:
        vpc_response = acs_client.vpc.create_vpc(vpc_payload)
    except Exception as e:
        click.echo(f"Exception while creating VPC: {str(e)}", err=True)
        return

    if not vpc_response.is_ok:
        click.echo(f"Error creating VPC: {vpc_response.error}", err=True)
        return

    vpc = vpc_response.data
    vpc_id = vpc["id"]
    click.echo(f"✅ Created VPC: {vpc['name']} (ID: {vpc_id})")

    # Get default network offering for VPC networks
    network_offering = get_default_vpc_network_offering(acs_client, zone_id)
    if not network_offering:
        click.echo("Error: No network offering available for VPC networks", err=True)
        return

    click.echo(f"Using network offering: {network_offering['name']} (ID: {network_offering['id']})")

    # Create first subnet
    subnet1_payload = CreateNetworkRequest(
        name=f"{vpc_name}-subnet1",
        displaytext=f"Subnet 1 for {vpc_name}",
        networkofferingid=network_offering["id"],
        zoneid=zone_id,
        vpcid=vpc_id,
        account=account,
        domainid=domain_id
    )

    subnet1_response = acs_client.network.create(subnet1_payload)
    if subnet1_response.is_ok:
        subnet1 = subnet1_response.data
        click.echo(f"✅ Created subnet 1: {subnet1['name']} (ID: {subnet1['id']})")
    else:
        click.echo(f"Error creating subnet 1: {subnet1_response.error}", err=True)

    # Create second subnet
    subnet2_payload = CreateNetworkRequest(
        name=f"{vpc_name}-subnet2",
        displaytext=f"Subnet 2 for {vpc_name}",
        networkofferingid=network_offering["id"],
        zoneid=zone_id,
        vpcid=vpc_id,
        account=account,
        domainid=domain_id
    )

    subnet2_response = acs_client.network.create(subnet2_payload)
    if subnet2_response.is_ok:
        subnet2 = subnet2_response.data
        click.echo(f"✅ Created subnet 2: {subnet2['name']} (ID: {subnet2['id']})")
    else:
        click.echo(f"Error creating subnet 2: {subnet2_response.error}", err=True)

    click.echo("\n🎉 VPC deployment completed!")


if __name__ == "__main__":
    deploy_vpc()