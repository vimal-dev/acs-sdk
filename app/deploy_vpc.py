from pprint import pprint
import sys

import click
import httpx

from acs_sdk.schemas.request.vpc import CreateVPCRequest
from acs_sdk.schemas.request.vpc_offering import ListVPCOfferingRequest
from acs_sdk.schemas.request.network import CreateNetworkRequest
from acs_sdk.schemas.request.network_offering import ListNetworkOfferingRequest
from acs_sdk.schemas.request.zone import ListZonesRequest
from acs_sdk.utils.ipaddress import cidr_info
from acs_sdk.schemas.request.network_acl import ListNetworkACLListsRequest

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

def get_network_acl(acs_client, vpc_id, account, domain_id):
    """Get the default network ACL ID for the account."""
    # This is a placeholder implementation. You may need to implement logic to find the correct ACL ID.
    payload = ListNetworkACLListsRequest(account=account, domainid=domain_id, vpcId=vpc_id, name="default_allow")
    response = acs_client.networkacl.list_acl_lists(payload)
    if response.is_ok and response.data:
        return response.data[0]
    return None


@click.command()
@click.option("--account", required=True, help="Account name for the VPC")
@click.option("--domain-id", required=True, help="Domain ID for the account")
@click.option("--zone-id", help="Zone ID (if not provided, will use the first available zone)")
@click.option("--vpc-name", default="default-vpc", help="Name for the VPC")
@click.option("--vpc-cidr", default="172.16.0.0/16", help="CIDR for the VPC")
@click.option("--subnet1-cidr", default="172.16.2.0/24", help="CIDR for first subnet")
@click.option("--subnet2-cidr", default="172.16.3.0/24", help="CIDR for second subnet")
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
        name=f"default-vpc-auto",
        # display_text=f"Default VPC",
        cidr=vpc_cidr,
        vpcOfferingId=vpc_offering["id"],
        zoneId=zone_id,
        account=account,
        domainId=domain_id,

        # name=f"default-vpc-auto",
        # display_text=f"Default VPC",
        # cidr="172.16.0.0/16",
        # account=account,
        # domainid=str(domain_id),
        # zoneid="f14fffed-c623-4105-8d65-c84c86ac0b9c",
        # vpcofferingid="6d8a3a3a-ce8e-4342-b967-417a9bca03a9",
    )

    try:
        vpc_response = acs_client.vpc.create_vpc(vpc_payload)
    except httpx.HTTPStatusError as e:
        click.echo(f"Exception while creating VPC: {str(e.response.text)}", err=True)
        return
    except httpx.HTTPError as e:
        click.echo(f"Exception while creating VPC: {str(e)}", err=True)
        return

    if not vpc_response.is_ok:
        click.echo(f"Error creating VPC: {vpc_response.error}", err=True)
        return

    vpc = vpc_response.data
    vpc_id = vpc["id"]
    click.echo(f"✅ Created VPC: (ID: {vpc_id})")
    #click.echo(f"✅ Created VPC: {vpc['name']} (ID: {vpc_id})")

    # Get default network offering for VPC networks
    network_offering = get_default_vpc_network_offering(acs_client, zone_id)
    if not network_offering:
        click.echo("Error: No network offering available for VPC networks", err=True)
        return

    click.echo(f"Using network offering: {network_offering['name']} (ID: {network_offering['id']})")

    acl = get_network_acl(acs_client, vpc_id, account, domain_id)
    if not acl:
        click.echo("Error: No ACL list available for VPC networks", err=True)
        return
    
    acl_id = acl["id"]
    click.echo(f"Using ACL list: {acl['name']} (ID: {acl_id})")

    # Create first subnet
    subnet1_info = cidr_info(subnet1_cidr)
    subnet1_payload = CreateNetworkRequest(
        name=f"{vpc_name}-subnet1",
        #displayText=f"Subnet 1 for {vpc_name}",
        networkOfferingId=network_offering["id"],
        zoneId=zone_id,
        vpcId=vpc_id,
        aclId=acl_id,
        account=account,
        domainId=domain_id,
        gateway=subnet1_info["gateway"],
        netmask=subnet1_info["netmask"],
    )

    subnet1_response = acs_client.network.create(subnet1_payload)
    if subnet1_response.is_ok:
        subnet1 = subnet1_response.data
        click.echo(f"✅ Created subnet 1: {subnet1['name']} (ID: {subnet1['id']})")
    else:
        click.echo(f"Error creating subnet 1: {subnet1_response.error}", err=True)

    # Create second subnet
    subnet2_info = cidr_info(subnet2_cidr)
    subnet2_payload = CreateNetworkRequest(
        name=f"{vpc_name}-subnet2",
        #displayText=f"Subnet 2 for {vpc_name}",
        networkOfferingId=network_offering["id"],
        zoneId=zone_id,
        vpcId=vpc_id,
        aclId=acl_id,
        account=account,
        domainId=domain_id,
        gateway=subnet2_info["gateway"],
        netmask=subnet2_info["netmask"],
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