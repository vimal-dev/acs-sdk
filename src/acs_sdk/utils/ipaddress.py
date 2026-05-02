import ipaddress

def subnet_grid(vpc_cidr, new_prefix=24):
    """Generate subnets from a VPC CIDR block with the specified prefix.
        Arguments:
        - vpc_cidr: The CIDR block of the VPC (e.g., "172.31.0.0/16")
        - new_prefix: The prefix length for the generated subnets (default: 24)
    """
    vpc = ipaddress.ip_network(vpc_cidr)
    return vpc.subnets(new_prefix=new_prefix)

def cidr_info(cidr: str):
    """Get detailed information about a CIDR block.
        Arguments:
        - cidr: The CIDR block to analyze (e.g., "192.168.0.0/24")

        Returns a dictionary with keys:
        - cidr: The CIDR block
        - netmask: The subnet mask
        - network: The network address
        - broadcast: The broadcast address
        - total_ips: Total number of IPs in the block
        - usable_ips: Number of usable IPs (excluding network and broadcast)
        - gateway: The first usable IP (often used as gateway)
        - first_ip: The first usable IP address
        - last_ip: The last usable IP address
    """
    net = ipaddress.ip_network(cidr, strict=False)

    total_ips = net.num_addresses
    usable_ips = total_ips - 2 if net.prefixlen < 31 else total_ips

    hosts = list(net.hosts())

    return {
        "cidr": str(net),
        "netmask": str(net.netmask),
        "network": str(net.network_address),
        "broadcast": str(net.broadcast_address),
        "total_ips": total_ips,
        "usable_ips": usable_ips,
        "gateway": str(hosts[0]) if hosts else None,
        "first_ip": str(hosts[0]) if hosts else None,
        "last_ip": str(hosts[-1]) if hosts else None,
    }
