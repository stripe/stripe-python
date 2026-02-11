# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import Dict
from typing_extensions import NotRequired, TypedDict


class OneTimeItemCreateParams(TypedDict):
    display_name: str
    """
    Description that customers will see in the invoice line item.
    Maximum length of 250 characters.
    """
    lookup_key: NotRequired[str]
    """
    An internal key you can use to search for a particular one-time item.
    Must be unique among billable items.
    Maximum length of 200 characters.
    """
    metadata: NotRequired[Dict[str, str]]
    """
    Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    tax_details: NotRequired["OneTimeItemCreateParamsTaxDetails"]
    """
    Stripe Tax details.
    """
    unit_label: NotRequired[str]
    """
    The unit to use when displaying prices for this one-time item. For example, set this field
    to "credit" for the display to show "(price) per credit".
    Maximum length of 100 characters.
    """


class OneTimeItemCreateParamsTaxDetails(TypedDict):
    tax_code: str
    """
    Product tax code (PTC).
    """
