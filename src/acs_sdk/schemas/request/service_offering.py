from pydantic import Field
from typing import Optional
from .base import APIRequest


class ListServiceOfferingsRequest(APIRequest):

    # Filters
    id: Optional[str] = Field(None, description="ID of the service offering")
    name: Optional[str] = Field(None, description="Name of the service offering")
    keyword: Optional[str] = Field(None, description="Search by keyword")

    domainid: Optional[str] = Field(
        None,
        description="List offerings belonging to a domain"
    )

    isrecursive: Optional[bool] = Field(
        None,
        description="Include subdomains (used with domainid)"
    )

    listall: Optional[bool] = Field(
        None,
        description="List all accessible offerings"
    )

    issystem: Optional[bool] = Field(
        None,
        description="Filter system VM offerings"
    )

    systemvmtype: Optional[str] = Field(
        None,
        description="System VM type (consoleproxy, secondarystoragevm, domainrouter)"
    )

    virtualmachineid: Optional[str] = Field(
        None,
        description="Filter offerings available for VM upgrade"
    )

    # Pagination
    page: Optional[int] = Field(
        1, ge=1, description="Page number"
    )
    pagesize: Optional[int] = Field(
        50, ge=1, le=500, description="Number of results per page"
    )

    # Advanced filters (newer versions)
    cpunumber: Optional[int] = Field(
        None,
        description="Filter by CPU count"
    )

    cpuspeed: Optional[int] = Field(
        None,
        description="Filter by CPU speed (MHz)"
    )

    memory: Optional[int] = Field(
        None,
        description="Filter by RAM (MB)"
    )

    zoneid: Optional[str] = Field(
        None,
        description="Filter offerings available in a zone"
    )

    encryptroot: Optional[bool] = Field(
        None,
        description="Filter offerings supporting root disk encryption"
    )