# core/response_mapper.py
from abc import ABC, abstractmethod
from typing import Dict


class ResponseMapper(ABC):
    """Abstract interface for parsing API responses."""

    @abstractmethod
    def extract(self, response: Dict, envelope: str) -> Dict:
        """Extract the inner response data from the API envelope.

        Args:
            response: The raw API response dict.
            envelope: The key to extract (e.g., 'listasyncjobsresponse').

        Returns:
            The extracted response data dict.
        """
        pass


class DefaultResponseMapper(ResponseMapper):
    """Default implementation of ResponseMapper."""

    def extract(self, response: Dict, envelope: str) -> Dict:
        if envelope in response:
            response = response[envelope]
        return response if isinstance(response, dict) else {}
