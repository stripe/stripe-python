# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import Dict
from typing_extensions import NotRequired, TypedDict


class LicensedItemCreateParams(TypedDict):
    display_name: str
    """
    Description that customers will see in the invoice line item.
    Maximum length of 250 characters.
    """
    lookup_key: NotRequired[str]
    """
    An internal key you can use to search for a particular billable item.
    Must be unique among billable items.
    Maximum length of 200 characters.
    """
    metadata: NotRequired[Dict[str, str]]
    """
    Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    tax_details: NotRequired["LicensedItemCreateParamsTaxDetails"]
    """
    Stripe Tax details.
    """
    unit_label: NotRequired[str]
    """
    The unit to use when displaying prices for this billable item in places like Checkout. For example, set this field
    to "seat" for Checkout to display "(price) per seat", or "environment" to display "(price) per environment".
    Maximum length of 100 characters.
    """


class LicensedItemCreateParamsTaxDetails(TypedDict):
    tax_code: str
    """
    Product tax code (PTC).
    """
