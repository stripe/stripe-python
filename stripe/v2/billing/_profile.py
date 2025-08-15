# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Dict, Optional
from typing_extensions import Literal


class Profile(StripeObject):
    OBJECT_NAME: ClassVar[Literal["v2.billing.profile"]] = "v2.billing.profile"
    created: str
    """
    Timestamp of when the object was created.
    """
    customer: Optional[str]
    """
    The ID of the customer object.
    """
    default_payment_method: Optional[str]
    """
    The ID of the payment method object.
    """
    display_name: Optional[str]
    """
    A customer-facing name for the billing profile.
    Maximum length of 250 characters.
    """
    id: str
    """
    The ID of the billing profile object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    lookup_key: Optional[str]
    """
    An internal key you can use to search for a particular billing profile.
    Maximum length of 200 characters.
    """
    metadata: Optional[Dict[str, str]]
    """
    Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: Literal["v2.billing.profile"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    status: Literal["active", "inactive"]
    """
    The current status of the billing profile.
    """
