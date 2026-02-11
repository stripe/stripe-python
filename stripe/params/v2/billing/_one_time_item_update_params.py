# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import Dict, Optional
from typing_extensions import NotRequired, TypedDict


class OneTimeItemUpdateParams(TypedDict):
    display_name: NotRequired[str]
    """
    Description that customers will see in the invoice line item.
    Maximum length of 250 characters.
    """
    lookup_key: NotRequired[str]
    """
    An internal key you can use to search for a particular one-time item.
    Maximum length of 200 characters.
    To remove the lookup_key from the object, set it to null in the request.
    """
    metadata: NotRequired[Dict[str, Optional[str]]]
    """
    Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    tax_details: NotRequired["OneTimeItemUpdateParamsTaxDetails"]
    """
    Stripe Tax details.
    """
    unit_label: NotRequired[str]
    """
    The unit to use when displaying prices for this one-time item. For example, set this field
    to "credit" for the display to show "(price) per credit".
    Maximum length of 100 characters.
    """


class OneTimeItemUpdateParamsTaxDetails(TypedDict):
    tax_code: str
    """
    Product tax code (PTC).
    """
