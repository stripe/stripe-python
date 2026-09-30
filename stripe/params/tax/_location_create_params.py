# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import List
from typing_extensions import Literal, NotRequired, TypedDict


class LocationCreateParams(RequestOptions):
    address: "LocationCreateParamsAddress"
    """
    The physical address of the tax location.
    """
    description: NotRequired[str]
    """
    Details to identify the tax location by its venue, types of events held, or available services, such as "A spacious auditorium suitable for large concerts and events.".
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    type: Literal["performance"]
    """
    The type of tax location. The only supported value is "performance".
    """


class LocationCreateParamsAddress(TypedDict):
    city: NotRequired["Literal['']|str"]
    """
    City, district, suburb, town, or village.
    """
    country: str
    """
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
    """
    line1: NotRequired["Literal['']|str"]
    """
    Address line 1, such as the street, PO Box, or company name.
    """
    line2: NotRequired["Literal['']|str"]
    """
    Address line 2, such as the apartment, suite, unit, or building.
    """
    postal_code: NotRequired["Literal['']|str"]
    """
    ZIP or postal code.
    """
    state: NotRequired["Literal['']|str"]
    """
    State/province as an [ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2) subdivision code, without country prefix, such as "NY" or "TX".
    """
