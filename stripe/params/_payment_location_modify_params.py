# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import List
from typing_extensions import Literal, NotRequired, TypedDict


class PaymentLocationModifyParams(RequestOptions):
    address: NotRequired["PaymentLocationModifyParamsAddress"]
    """
    The full address of the location.
    """
    business_registration: NotRequired[
        "PaymentLocationModifyParamsBusinessRegistration"
    ]
    """
    Identification numbers associated with the location.
    """
    display_name: NotRequired[str]
    """
    A name for the location.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    onboarding_data_update_acknowledged: NotRequired[bool]
    """
    Pass true when updating location fields that trigger onboarding review for any of the location's active location capabilities. If this parameter isn't set to true, updates that would trigger onboarding review fail. Only applicable for locations with active location capabilities.
    """


class PaymentLocationModifyParamsAddress(TypedDict):
    city: NotRequired["Literal['']|str"]
    """
    City, district, suburb, town, or village.
    """
    country: NotRequired[str]
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
    State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).
    """


class PaymentLocationModifyParamsBusinessRegistration(TypedDict):
    siret: NotRequired["Literal['']|str"]
    """
    14-digit SIRET (Système d'identification du répertoire des établissements) number for the location.
    """
