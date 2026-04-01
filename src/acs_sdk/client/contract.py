# client/contracts.py

from abc import ABC, abstractmethod
from typing import Dict, Any, Optional


class ClientContract(ABC):
    @abstractmethod
    def call(self, command: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Execute Apache CloudStack API command and optionally map response
        to a Pydantic model.
        """

    @abstractmethod
    def close(self) -> None:
        """Close HTTP connection"""
