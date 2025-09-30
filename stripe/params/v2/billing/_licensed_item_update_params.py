# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import Dict, Optional
from typing_extensions import NotRequired, TypedDict


class LicensedItemUpdateParams(TypedDict):
    display_name: NotRequired[str]
    """
    Description that customers will see in the invoice line item.
    Maximum length of 250 characters.
    """
    lookup_key: NotRequired[str]
    """
    An internal key you can use to search for a particular billable item.
    Maximum length of 200 characters.
    To remove the lookup_key from the object, set it to null in the request.
    """
    metadata: NotRequired[Dict[str, Optional[str]]]
    """
    Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    tax_details: NotRequired["LicensedItemUpdateParamsTaxDetails"]
    """
    Stripe Tax details.
    """
    unit_label: NotRequired[str]
    """
    The unit to use when displaying prices for this billable item in places like Checkout. For example, set this field
    to "seat" for Checkout to display "(price) per seat", or "environment" to display "(price) per environment".
    Maximum length of 100 characters.
    """


class LicensedItemUpdateParamsTaxDetails(TypedDict):
    tax_code: str
    """
    Product tax code (PTC).
    """
