# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import Dict, Optional
from typing_extensions import NotRequired, TypedDict


class ProfileUpdateParams(TypedDict):
    default_payment_method: NotRequired[str]
    """
    The ID of the payment method object.
    """
    display_name: NotRequired[str]
    """
    A customer-facing name for the billing profile.
    Maximum length of 250 characters.
    To remove the display_name from the object, set it to null in the request.
    """
    lookup_key: NotRequired[str]
    """
    An internal key you can use to search for a particular billing profile. It must be unique among billing profiles for a given customer.
    Maximum length of 200 characters.
    To remove the lookup_key from the object, set it to null in the request.
    """
    metadata: NotRequired[Dict[str, Optional[str]]]
    """
    Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
