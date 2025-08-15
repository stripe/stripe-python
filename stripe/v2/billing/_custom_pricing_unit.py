# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Dict, Optional
from typing_extensions import Literal


class CustomPricingUnit(StripeObject):
    """
    The Custom Pricing Unit object.
    """

    OBJECT_NAME: ClassVar[Literal["v2.billing.custom_pricing_unit"]] = (
        "v2.billing.custom_pricing_unit"
    )
    active: bool
    """
    Whether the CustomPricingUnit is active.
    """
    created: str
    """
    Timestamp of when the object was created.
    """
    display_name: str
    """
    Description that customers will see in the invoice line item.
    Maximum length of 250 characters.
    """
    id: str
    """
    The ID of the custom pricing unit.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    lookup_key: Optional[str]
    """
    An internal key you can use to search for a particular CustomPricingUnit item.
    Maximum length of 200 characters.
    """
    metadata: Optional[Dict[str, str]]
    """
    Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: Literal["v2.billing.custom_pricing_unit"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
