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
        return self._execute(
            "createSSHKeyPair",
            payload,
            envelope="createsshkeypairresponse",
            entity="keypair",
        )

    async def create_ssh_key_pair_async(
        self, payload: CreateSSHKeyPairRequest
    ) -> APIResponse[Dict]:
        """Asynchronously create a new keypair and returns the private key."""
        return await self._execute_async(
            "createSSHKeyPair",
            payload,
            envelope="createsshkeypairresponse",
            entity="keypair",
        )

    def delete_ssh_key_pair(self, payload: DeleteSSHKeyPairRequest) -> APIResponse[Dict]:
        """Delete an SSH key pair."""
        return self._execute(
            "deleteSSHKeyPair",
            payload,
            envelope="deletesshkeypairresponse",
        )

    async def delete_ssh_key_pair_async(
        self, payload: DeleteSSHKeyPairRequest
    ) -> APIResponse[Dict]:
        """Asynchronously delete an SSH key pair."""
        return await self._execute_async(
            "deleteSSHKeyPair",
            payload,
            envelope="deletesshkeypairresponse",
        )

    def list_ssh_key_pairs(self, payload: ListSSHKeyPairsRequest) -> APIResponse[List[Dict]]:
        """List SSH key pairs."""
        return self._execute(
            "listSSHKeyPairs",
            payload,
            envelope="listsshkeypairsresponse",
            entity="keypair",
        )

    async def list_ssh_key_pairs_async(
        self, payload: ListSSHKeyPairsRequest
    ) -> APIResponse[List[Dict]]:
        """Asynchronously list SSH key pairs."""
        return await self._execute_async(
            "listSSHKeyPairs",
            payload,
            envelope="listsshkeypairsresponse",
            entity="keypair",
        )

    def register_ssh_key_pair(self, payload: RegisterSSHKeyPairRequest) -> APIResponse[Dict]:
        """Register an existing SSH public key."""
        return self._execute(
            "registerSSHKeyPair",
            payload,
            envelope="registersshkeypairresponse",
        )

    async def register_ssh_key_pair_async(
        self, payload: RegisterSSHKeyPairRequest
    ) -> APIResponse[Dict]:
        """Asynchronously register an existing SSH public key."""
        return await self._execute_async(
            "registerSSHKeyPair",
            payload,
            envelope="registersshkeypairresponse",
        )
