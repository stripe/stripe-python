# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._list_object import ListObject
    from stripe._request_options import RequestOptions
    from stripe.params.tax._location_create_params import LocationCreateParams
    from stripe.params.tax._location_list_params import LocationListParams
    from stripe.params.tax._location_retrieve_params import (
        LocationRetrieveParams,
    )
    from stripe.tax._location import Location


class LocationService(StripeService):
    def list(
        self,
        params: "LocationListParams",
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[Location]":
        """
        Retrieve a list of all tax locations. Tax locations can represent the venues for services, tickets, or other product types.

        The response includes detailed information for each tax location, such as its address, name, description, and current operational status.

        You can paginate through the list by using the limit parameter to control the number of results returned in each request.
        """
        return cast(
            "ListObject[Location]",
            self._request(
                "get",
                "/v1/tax/locations",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: "LocationListParams",
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[Location]":
        """
        Retrieve a list of all tax locations. Tax locations can represent the venues for services, tickets, or other product types.

        The response includes detailed information for each tax location, such as its address, name, description, and current operational status.

        You can paginate through the list by using the limit parameter to control the number of results returned in each request.
        """
        return cast(
            "ListObject[Location]",
            await self._request_async(
                "get",
                "/v1/tax/locations",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "LocationCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "Location":
        """
        Create a tax location to use in calculating taxes for a service, ticket, or other type of product. The resulting object contains the id, address, name, description, and current operational status of the tax location.
        """
        return cast(
            "Location",
            self._request(
                "post",
                "/v1/tax/locations",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "LocationCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "Location":
        """
        Create a tax location to use in calculating taxes for a service, ticket, or other type of product. The resulting object contains the id, address, name, description, and current operational status of the tax location.
        """
        return cast(
            "Location",
            await self._request_async(
                "post",
                "/v1/tax/locations",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        location: str,
        params: Optional["LocationRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Location":
        """
        Fetch the details of a specific tax location using its unique identifier. Use a tax location to calculate taxes based on the location of the end product, such as a performance, instead of the customer address. For more details, check the [integration guide](https://docs.stripe.com/tax/tax-for-tickets/integration-guide).
        """
        return cast(
            "Location",
            self._request(
                "get",
                "/v1/tax/locations/{location}".format(
                    location=sanitize_id(location),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        location: str,
        params: Optional["LocationRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Location":
        """
        Fetch the details of a specific tax location using its unique identifier. Use a tax location to calculate taxes based on the location of the end product, such as a performance, instead of the customer address. For more details, check the [integration guide](https://docs.stripe.com/tax/tax-for-tickets/integration-guide).
        """
        return cast(
            "Location",
            await self._request_async(
                "get",
                "/v1/tax/locations/{location}".format(
                    location=sanitize_id(location),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
