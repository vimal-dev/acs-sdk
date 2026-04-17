# services/ssh.py
from typing import Dict, List

from acs_sdk.schemas.request.ssh import (
    CreateSSHKeyPairRequest,
    DeleteSSHKeyPairRequest,
    ListSSHKeyPairsRequest,
    RegisterSSHKeyPairRequest,
)

from .base import BaseService
from ..schemas.response.base import APIResponse


class SSH(BaseService):
    def create_ssh_key_pair(self, payload: CreateSSHKeyPairRequest) -> APIResponse[Dict]:
        """Create a new keypair and returns the private key."""
        response = self.client.call("createSSHKeyPair", payload.model_dump(exclude_none=True))
        data = {}
        if 'createsshkeypairresponse' in response:
            data = response['createsshkeypairresponse']
        return APIResponse[Dict](**{"data": data})

    async def create_ssh_key_pair_async(self, payload: CreateSSHKeyPairRequest) -> APIResponse[Dict]:
        """Asynchronously create a new keypair and returns the private key."""
        response = await self.client.call_async("createSSHKeyPair", payload.model_dump(exclude_none=True))
        data = {}
        if 'createsshkeypairresponse' in response:
            data = response['createsshkeypairresponse']
        return APIResponse[Dict](**{"data": data})

    def delete_ssh_key_pair(self, payload: DeleteSSHKeyPairRequest) -> APIResponse[Dict]:
        """Delete an SSH key pair."""
        response = self.client.call("deleteSSHKeyPair", payload.model_dump(exclude_none=True))
        data = {}
        if 'deletesshkeypairresponse' in response:
            data = response['deletesshkeypairresponse']
        return APIResponse[Dict](**{"data": data})

    async def delete_ssh_key_pair_async(self, payload: DeleteSSHKeyPairRequest) -> APIResponse[Dict]:
        """Asynchronously delete an SSH key pair."""
        response = await self.client.call_async("deleteSSHKeyPair", payload.model_dump(exclude_none=True))
        data = {}
        if 'deletesshkeypairresponse' in response:
            data = response['deletesshkeypairresponse']
        return APIResponse[Dict](**{"data": data})

    def list_ssh_key_pairs(self, payload: ListSSHKeyPairsRequest) -> APIResponse[List[Dict]]:
        """List SSH key pairs."""
        response = self.client.call("listSSHKeyPairs", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listsshkeypairsresponse' in response:
            response = response['listsshkeypairsresponse']
        if 'sshkeypair' in response and response['sshkeypair']:
            data = response['sshkeypair']
            count = response.get('count', 0)
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    async def list_ssh_key_pairs_async(self, payload: ListSSHKeyPairsRequest) -> APIResponse[List[Dict]]:
        """Asynchronously list SSH key pairs."""
        response = await self.client.call_async("listSSHKeyPairs", payload.model_dump(exclude_none=True))
        count = 0
        data = []
        if 'listsshkeypairsresponse' in response:
            response = response['listsshkeypairsresponse']
        if 'sshkeypair' in response and response['sshkeypair']:
            data = response['sshkeypair']
            count = response.get('count', 0)
        return APIResponse[List[Dict]](**{"data": data, "count": count})

    def register_ssh_key_pair(self, payload: RegisterSSHKeyPairRequest) -> APIResponse[Dict]:
        """Register an existing SSH public key."""
        response = self.client.call("registerSSHKeyPair", payload.model_dump(exclude_none=True))
        data = {}
        if 'registersshkeypairresponse' in response:
            data = response['registersshkeypairresponse']
        return APIResponse[Dict](**{"data": data})

    async def register_ssh_key_pair_async(self, payload: RegisterSSHKeyPairRequest) -> APIResponse[Dict]:
        """Asynchronously register an existing SSH public key."""
        response = await self.client.call_async("registerSSHKeyPair", payload.model_dump(exclude_none=True))
        data = {}
        if 'registersshkeypairresponse' in response:
            data = response['registersshkeypairresponse']
        return APIResponse[Dict](**{"data": data})
