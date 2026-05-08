"""Base service module for CloudStack resource operations.

This module provides the BaseService class that acts as a foundation for
service implementations that communicate with the CloudStack API.
"""
from httpx import HTTPStatusError
from typing import Dict, List, Optional

from pydantic import BaseModel

from acs_sdk.client.contract import ClientContract
from acs_sdk.core.response_mapper import DefaultResponseMapper, ResponseMapper
from acs_sdk.schemas.response.base import APIError, APIResponse


class BaseService:
    """Base class for CloudStack service implementations.

    This abstract base class is intended to be subclassed for specific
    CloudStack resource services (e.g., UserService, VMService, etc.).
    It provides a common interface for accessing the CloudStack client.

    Attributes:
        client (ClientContract): The CloudStack API client used to execute
            commands on the CloudStack endpoint.
        response_mapper (ResponseMapper): An optional response mapper for
            extracting data from API responses.

    Example:
        >>> class UserService(BaseService):
        ...     def list_users(self):
        ...         return self._execute("listUsers", {}, envelope="listusersresponse", entity="user")
    """

    def __init__(
        self,
        client: ClientContract,
        response_mapper: Optional[ResponseMapper] = None,
    ):
        """Initialize the service with a CloudStack client.

        Args:
            client (ClientContract): The CloudStack API client for making
                API calls.
        """
        self.client = client
        self.response_mapper = response_mapper or DefaultResponseMapper()

    def _extract_response(self, response: Dict, envelope: str) -> Dict:
        """Extracts the relevant data from the API response using the response mapper."""
        return self.response_mapper.extract(response, envelope)

    @staticmethod
    def _wrap(response_data: Dict, entity: Optional[str]) -> APIResponse:
        """
        Wraps the response data in an APIResponse object, handling both single items and lists.
        Args:
            response_data (Dict): The raw response data extracted from the API response.
            entity (Optional[str]): If the response contains a list of items or a single item, specify the key to extract the list or item from the response data.
        Returns:
            APIResponse: The API response wrapped in an APIResponse object.
        """
        if entity:
            data = response_data.get(entity) if isinstance(response_data, dict) else None
            if isinstance(data, list):
                count = response_data.get("count", 0)
                return APIResponse[List[Dict]](data=data, count=count)
            return APIResponse[Dict](data=data)
        return APIResponse[Dict](data=response_data)
    
    @staticmethod
    def _error(response_data: Dict) -> APIResponse:
        """
        Wraps the error response data in an APIResponse object, handling both single items and lists.
        Args:
            response_data (Dict): The raw response data extracted from the API response.
        Returns:
            APIResponse: The API response wrapped in an APIResponse object.
        """
        return APIResponse[None](
            status="ERROR",
            data=None,
            errors=[
                APIError(Number=response_data.get("cserrorcode", response_data.get("errorcode", "")), Text=response_data.get("errortext", ""))
            ]
        )

    def _execute(
        self,
        command: str,
        payload: BaseModel,
        envelope: str,
        entity: Optional[str] = None,
    ) -> APIResponse:
        """
        Executes a synchronous command against the CloudStack API.
        Args:
            command (str): The CloudStack API command to execute.
            payload (BaseModel): The request payload as a Pydantic model.
            envelope (str): The expected envelope key in the API response.
            entity (Optional[str]): If the response contains a list of items or a single item,
                specify the key to extract the list or item from the response data.
        Returns:
            APIResponse: The API response wrapped in an APIResponse object.
        """
        try:
            response = self.client.call(command, payload.model_dump(exclude_none=True))
            response_data = self._extract_response(response, envelope)
            return self._wrap(response_data, entity)
        except HTTPStatusError as e:
            response = e.response.json()
            response_data = self._extract_response(response, envelope)
            return self._error(response_data)

    async def _execute_async(
        self,
        command: str,
        payload: BaseModel,
        envelope: str,
        entity: Optional[str] = None,
    ) -> APIResponse:
        """Executes an asynchronous command against the CloudStack API.
        Args:
            command (str): The CloudStack API command to execute.
            payload (BaseModel): The request payload as a Pydantic model.
            envelope (str): The expected envelope key in the API response.
            entity (Optional[str]): If the response contains a list of items or a single item,
                specify the key to extract the list or item from the response data.
        Returns:
            APIResponse: The API response wrapped in an APIResponse object.
        """
        try:
            response = await self.client.call_async(command, payload.model_dump(exclude_none=True))
            response_data = self._extract_response(response, envelope)
            return self._wrap(response_data, entity)
        except HTTPStatusError as e:
            response = e.response.json()
            response_data = self._extract_response(response, envelope)
            return self._error(response_data)
