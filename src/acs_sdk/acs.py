"""Main module for Apache CloudStack SDK.

This module provides the top-level ApacheCloudStack class that serves as
the primary interface for interacting with Apache CloudStack environments.
"""

import logging
from typing import Dict, Type
from opentelemetry import trace

from acs_sdk.schemas.config import ApacheCloudStackConfig
from acs_sdk.client.client import ApacheCloudStackClient
from acs_sdk.services.account import Account
from acs_sdk.services.address import Address
from acs_sdk.services.base import BaseService
from acs_sdk.services.backup_and_recovery import BackupAndRecovery
from acs_sdk.services.disk_offering import DiskOffering
from acs_sdk.services.firewall import Firewall
from acs_sdk.services.iso import ISO
from acs_sdk.services.job import Job
from acs_sdk.services.nat import NAT
from acs_sdk.services.network import Network
from acs_sdk.services.network_acl import NetworkACL
from acs_sdk.services.network_offering import NetworkOffering
from acs_sdk.services.region import Region
from acs_sdk.services.security_group import SecurityGroup
from acs_sdk.services.service_offering import ServiceOffering
from acs_sdk.services.snapshot import Snapshot
from acs_sdk.services.ssh import SSH
from acs_sdk.services.template import Template
from acs_sdk.services.usage import Usage
from acs_sdk.services.virtual_machine import VirtualMachine
from acs_sdk.services.volume import Volume
from acs_sdk.services.vpc import VPC
from acs_sdk.services.vpc_offering import VPCOffering
from acs_sdk.services.zone import Zone


class ApacheCloudStack:
    """High-level interface for Apache CloudStack API interactions.

    This class wraps the CloudStack client and provides a convenient entry point
    for working with CloudStack resources. It handles initialization of the
    client with provided configuration.

    Attributes:
        config (ApacheCloudStackConfig): CloudStack configuration with endpoint
            and API credentials.
        client (ApacheCloudStackClient): The underlying HTTP client for API
            communication.

    Example:
        >>> config = ApacheCloudStackConfig(
        ...     api_key='your-key',
        ...     api_secret='your-secret',
        ...     endpoint='https://cloudstack.example.com'
        ... )
        >>> acs = ApacheCloudStack(config)
        >>> response = acs.client.call('listUsers')
    """

    account: "Account"
    address: "Address"
    iso: "ISO"
    backupandrecovery: "BackupAndRecovery"
    diskoffering: "DiskOffering"
    firewall: "Firewall"
    job: "Job"
    template: "Template"
    nat: "NAT"
    network: "Network"
    networkacl: "NetworkACL"
    networkoffering: "NetworkOffering"
    region: "Region"
    securitygroup: "SecurityGroup"
    serviceoffering: "ServiceOffering"
    snapshot: "Snapshot"
    ssh: "SSH"
    usage: "Usage"
    vm: "VirtualMachine"
    volume: "Volume"
    vpc: "VPC"
    vpcoffering: "VPCOffering"
    zone: "Zone"

    _service_map: Dict[str, Type["BaseService"]] = {
        "account": Account,
        "iso": ISO,
        "address": Address,
        "backupandrecovery": BackupAndRecovery,
        "diskoffering": DiskOffering,
        "firewall": Firewall,
        "job": Job,
        "nat": NAT,
        "network": Network,
        "networkacl": NetworkACL,
        "networkoffering": NetworkOffering,
        "region": Region,
        "securitygroup": SecurityGroup,
        "serviceoffering": ServiceOffering,
        "snapshot": Snapshot,
        "ssh": SSH,
        "template": Template,
        "vm": VirtualMachine,
        "volume": Volume,
        "vpc": VPC,
        "vpcoffering": VPCOffering,
        "usage": Usage,
        "zone": Zone,
    }

    def __init__(
        self,
        config: ApacheCloudStackConfig,
        tracer: trace.Tracer = None,
        logger: logging.Logger = None,
    ):
        """Initialize the ApacheCloudStack SDK.

        Args:
            config (ApacheCloudStackConfig): Configuration object containing
                CloudStack endpoint URL and API credentials.
            tracer (trace.Tracer, optional): Tracer for API call tracing.
            logger (logging.Logger, optional): Logger for API call logging.

        """
        self.tracer = tracer or trace.get_tracer(__name__)
        self.logger = logger or logging.getLogger("cloudstack")
        self.client = ApacheCloudStackClient(config, tracer=self.tracer, logger=self.logger)
        self._cache = {}

    def __getattr__(self, name):
        """Dynamically load service classes on demand."""
        if name in self._service_map:
            if name not in self._cache:
                self._cache[name] = self._service_map[name](self.client)
            return self._cache[name]

        raise AttributeError(f"{name} not found")
