# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar
from typing_extensions import Literal


class CustomerEntitlement(StripeObject):
    """
    A entitlement for a customer describes access to a feature.
    """

    OBJECT_NAME: ClassVar[
        Literal["customer_entitlement"]
    ] = "customer_entitlement"
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
