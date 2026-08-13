# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import NotRequired, TypedDict


class OperationResolveAddressParams(TypedDict):
    address: "OperationResolveAddressParamsAddress"
    """
    The address to resolve.
    """


class OperationResolveAddressParamsAddress(TypedDict):
    city: NotRequired[str]
    """
    The city.
    """
    country: str
    """
    The two-letter country code.
    """
    line1: NotRequired[str]
    """
    The first line of the street address.
    """
    postal_code: NotRequired[str]
    """
    The postal code.
    """
    state: NotRequired[str]
    """
    The state or province.
    """
