# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Optional
from typing_extensions import Literal


class CustomerEntitlement(StripeObject):
    """
    A entitlement for a customer describes access to a feature.
    """

    OBJECT_NAME: ClassVar[
        Literal["customer_entitlement"]
    ] = "customer_entitlement"

    class Quantity(StripeObject):
        total_available: int
        """
        The total quantity available to the customer.
        """

    feature: str
    """
    The feature that the customer is entitled to.
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    lookup_key: str
    """
    A unique key you provide as your own system identifier. This may be up to 80 characters.
    """
    object: Literal["customer_entitlement"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    quantity: Optional[Quantity]
    """
    Contains information about entitlements relating to features with type=quantity. Required when the feature has type=quantity.
    """
    type: Literal["quantity", "switch"]
    """
    The type of feature.
    """
    _inner_class_types = {"quantity": Quantity}
