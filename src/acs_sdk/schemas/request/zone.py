from typing import Optional
from pydantic import Field
from acs_sdk.schemas.request.base import APIRequest


class ListZonesRequest(APIRequest):
    id: Optional[str] = Field(
        None, description="List zones by ID"
    )
    ids: Optional[str] = Field(
        None, description="List zones by a comma-separated list of IDs"
    )
    name: Optional[str] = Field(
        None, description="List zones by name"
    )
    keyword: Optional[str] = Field(
        None, description="List zones by keyword"
    )
    domainid: Optional[str] = Field(
        None,
        alias="domainId",
        description="the ID of the domain associated with the zone"
    )
    available: Optional[bool] = Field(
        False, description="true if you want to retrieve all available Zones. False if you only want to return the Zones from which you have at least one VM"
    )
    networktype: Optional[str] = Field(
        None, description="The network type of the zone that the virtual machine belongs to"
    )
    showcapacities: Optional[bool] = Field(
        None, description="true if you want to retrieve the capacity of the zones"
    )
    showicon: Optional[bool] = Field(
        None, description="true if you want to retrieve the icon of the zones"
    )
    storageaccessgroup: Optional[str] = Field(
        None,
        alias="storageAccessGroup",
        description="the name of the storage access group. If specified, list only zones that belong to this storage access group."
    )
    page: Optional[int] = Field(
        1, ge=1, description="Page number"
    )
    pagesize: Optional[int] = Field(
        50, ge=1, le=500, description="Number of results per page"
    )