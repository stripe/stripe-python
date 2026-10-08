# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Optional
from typing_extensions import Literal


class Rule(StripeObject):
    OBJECT_NAME: ClassVar[Literal["radar.rule"]] = "radar.rule"
    action: str
    """
    The action taken on the payment.
    """
    id: str
    """
    Unique identifier for the object.
    """
    object: Optional[Literal["radar.rule"]]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    predicate: Optional[str]
    """
    The predicate to evaluate the payment against.
    """
