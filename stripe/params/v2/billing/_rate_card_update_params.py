# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import Dict, Optional
from typing_extensions import NotRequired, TypedDict


class RateCardUpdateParams(TypedDict):
    active: NotRequired[bool]
    """
    Sets whether the RateCard is active. Inactive RateCards cannot be used in new activations or have new rates added.
    """
    display_name: NotRequired[str]
    """
    A customer-facing name for the RateCard.
    This name is used in Stripe-hosted products like the Customer Portal and Checkout. It does not show up on Invoices.
    Maximum length of 250 characters.
    """
    live_version: NotRequired[str]
    """
    Changes the version that new RateCard activations will use. Providing `live_version = "latest"` will set the
    RateCard's `live_version` to its latest version.
    """
    lookup_key: NotRequired[str]
    """
    An internal key you can use to search for a particular RateCard. Maximum length of 200 characters.
    """
    metadata: NotRequired[Dict[str, Optional[str]]]
    """
    Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
