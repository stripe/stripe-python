# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._createable_api_resource import CreateableAPIResource
from stripe._list_object import ListObject
from stripe._listable_api_resource import ListableAPIResource
from stripe._stripe_object import StripeObject
from typing import ClassVar, Optional, cast
from typing_extensions import Literal, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.tax._location_create_params import LocationCreateParams
    from stripe.params.tax._location_list_params import LocationListParams
    from stripe.params.tax._location_retrieve_params import (
        LocationRetrieveParams,
    )


class Location(
    CreateableAPIResource["Location"],
    ListableAPIResource["Location"],
):
    """
    Tax locations represent venues for services, tickets, or other product types.
    """

    OBJECT_NAME: ClassVar[Literal["tax.location"]] = "tax.location"

    class Address(StripeObject):
        city: Optional[str]
        """
        City, district, suburb, town, or village.
        """
        country: Optional[str]
        """
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
        """
        line1: Optional[str]
        """
        Address line 1, such as the street, PO Box, or company name.
        """
        line2: Optional[str]
        """
        Address line 2, such as the apartment, suite, unit, or building.
        """
        postal_code: Optional[str]
        """
        ZIP or postal code.
        """
        state: Optional[str]
        """
        State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).
        """

    address: Address
    description: Optional[str]
    """
    A descriptive text providing additional context about the tax location. This can include information about the venue, types of events held, services available, or any relevant details for better identification (e.g., "A spacious auditorium suitable for large concerts and events.").
    """
    id: str
    """
    Unique identifier for the object.
    """
    object: Literal["tax.location"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    type: Literal["performance"]
    """
    The type of tax location to be defined. Currently the only option is `performance`.
    """

    @classmethod
    def create(cls, **params: Unpack["LocationCreateParams"]) -> "Location":
        """
        Create a tax location to use in calculating taxes for a service, ticket, or other type of product. The resulting object contains the id, address, name, description, and current operational status of the tax location.
        """
        return cast(
            "Location",
            cls._static_request(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    async def create_async(
        cls, **params: Unpack["LocationCreateParams"]
    ) -> "Location":
        """
        Create a tax location to use in calculating taxes for a service, ticket, or other type of product. The resulting object contains the id, address, name, description, and current operational status of the tax location.
        """
        return cast(
            "Location",
            await cls._static_request_async(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    def list(
        cls, **params: Unpack["LocationListParams"]
    ) -> ListObject["Location"]:
        """
        Retrieve a list of all tax locations. Tax locations can represent the venues for services, tickets, or other product types.

        The response includes detailed information for each tax location, such as its address, name, description, and current operational status.

        You can paginate through the list by using the limit parameter to control the number of results returned in each request.
        """
        result = cls._static_request(
            "get",
            cls.class_url(),
            params=params,
        )
        if not isinstance(result, ListObject):
            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

    @classmethod
    async def list_async(
        cls, **params: Unpack["LocationListParams"]
    ) -> ListObject["Location"]:
        """
        Retrieve a list of all tax locations. Tax locations can represent the venues for services, tickets, or other product types.

        The response includes detailed information for each tax location, such as its address, name, description, and current operational status.

        You can paginate through the list by using the limit parameter to control the number of results returned in each request.
        """
        result = await cls._static_request_async(
            "get",
            cls.class_url(),
            params=params,
        )
        if not isinstance(result, ListObject):
            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["LocationRetrieveParams"]
    ) -> "Location":
        """
        Fetch the details of a specific tax location using its unique identifier. Use a tax location to calculate taxes based on the location of the end product, such as a performance, instead of the customer address. For more details, check the [integration guide](https://docs.stripe.com/tax/tax-for-tickets/integration-guide).
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls, id: str, **params: Unpack["LocationRetrieveParams"]
    ) -> "Location":
        """
        Fetch the details of a specific tax location using its unique identifier. Use a tax location to calculate taxes based on the location of the end product, such as a performance, instead of the customer address. For more details, check the [integration guide](https://docs.stripe.com/tax/tax-for-tickets/integration-guide).
        """
        instance = cls(id, **params)
        await instance.refresh_async()
        return instance

    _inner_class_types = {"address": Address}
