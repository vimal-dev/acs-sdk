from typing import Optional
from pydantic import Field
from acs_sdk.schemas.request.base import APIRequest, PaginationMixin


class ListVPCOfferingRequest(APIRequest, PaginationMixin):
    """Request schema for listing VPC offerings."""

    id: Optional[str] = Field(None, description="The ID of the VPC offering.")
    name: Optional[str] = Field(None, description="The name of the VPC offering.")
    displaytext: Optional[str] = Field(
        None, alias="displayText", description="The display text of the VPC offering."
    )
    domainid: Optional[str] = Field(
        None, alias="domainId", description="The domain ID of the VPC offering."
    )
    state: Optional[str] = Field(None, description="The state of the VPC offering.")
    isdefault: Optional[bool] = Field(
        None, alias="isDefault", description="Whether the VPC offering is default."
    )
    issystem: Optional[bool] = Field(
        None, alias="isSystem", description="Whether the VPC offering is system."
    )
    keyword: Optional[str] = Field(None, description="List by keyword.")
    supportedservices: Optional[str] = Field(
        None, alias="supportedServices", description="The supported services of the VPC offering."
    )
    zoneid: Optional[str] = Field(
        None, alias="zoneId", description="The zone ID of the VPC offering."
    )
