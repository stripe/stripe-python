# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import List
from typing_extensions import NotRequired, TypedDict


class PaymentLocationCreateParams(RequestOptions):
    address: "PaymentLocationCreateParamsAddress"
    """
    The full address of the location.
    """
    business_registration: NotRequired[
        "PaymentLocationCreateParamsBusinessRegistration"
    ]
    """
    Identification numbers associated with the location.
    """
    display_name: str
    """
    A name for the location.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """


class PaymentLocationCreateParamsAddress(TypedDict):
    city: NotRequired[str]
    """
    City, district, suburb, town, or village.
    """
    country: str
    """
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
    """
    line1: NotRequired[str]
    """
    Address line 1, such as the street, PO Box, or company name.
    """
    line2: NotRequired[str]
    """
    Address line 2, such as the apartment, suite, unit, or building.
    """
    postal_code: NotRequired[str]
    """
    ZIP or postal code.
    """
    state: NotRequired[str]
    """
    State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).
    """


class PaymentLocationCreateParamsBusinessRegistration(TypedDict):
    siret: NotRequired[str]
    """
    14-digit SIRET (Système d'identification du répertoire des établissements) number for the location.
    """
