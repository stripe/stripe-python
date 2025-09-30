# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import Dict
from typing_extensions import NotRequired, TypedDict


class CustomPricingUnitCreateParams(TypedDict):
    display_name: str
    """
    Description that customers will see in the invoice line item.
    Maximum length of 10 characters.
    """
    lookup_key: NotRequired[str]
    """
    An internal key you can use to search for a particular custom pricing unit item.
    Must be unique among items.
    Maximum length of 200 characters.
    """
    metadata: NotRequired[Dict[str, str]]
    """
    Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
