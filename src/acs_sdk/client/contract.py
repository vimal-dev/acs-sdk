# client/contracts.py

from abc import ABC, abstractmethod
from typing import Dict, Any, Optional


class ClientContract(ABC):
    @abstractmethod
    def call(self, command: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Execute an Apache CloudStack API command and return the parsed JSON (sync)."""

    @abstractmethod
    async def call_async(
        self, command: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Execute an Apache CloudStack API command and return the parsed JSON (async)."""

    @abstractmethod
    def close(self) -> None:
        """Close HTTP connection"""
