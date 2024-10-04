# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Dict, Optional
from typing_extensions import Literal


class Margin(StripeObject):
    """
    A (partner) margin represents a specific discount distributed in partner reseller programs to business partners who
    resell products and services and earn a discount (margin) for doing so.
    """

    OBJECT_NAME: ClassVar[Literal["margin"]] = "margin"
    active: bool
    """
    Whether the margin can be applied to invoices, invoice items, or invoice line items. Defaults to `true`.
    """
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: Optional[Dict[str, str]]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    name: Optional[str]
    """
    Name of the margin that's displayed on, for example, invoices.
    """
    object: Literal["margin"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    percent_off: float
    """
    Percent that will be taken off the subtotal before tax (after all other discounts and promotions) of any invoice to which the margin is applied.
    """
    updated: int
    """
    Time at which the object was last updated. Measured in seconds since the Unix epoch.
    """
