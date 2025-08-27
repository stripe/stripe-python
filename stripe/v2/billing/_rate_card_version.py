# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar
from typing_extensions import Literal


class RateCardVersion(StripeObject):
    OBJECT_NAME: ClassVar[Literal["v2.billing.rate_card_version"]] = (
        "v2.billing.rate_card_version"
    )
    created: str
    """
    Timestamp of when the object was created.
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["v2.billing.rate_card_version"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    rate_card_id: str
    """
    The ID of the Rate Card that this version belongs to.
    """
