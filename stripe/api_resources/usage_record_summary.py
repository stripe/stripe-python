# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.stripe_object import StripeObject
from typing import ClassVar, Optional
from typing_extensions import Literal


class UsageRecordSummary(StripeObject):
    OBJECT_NAME: ClassVar[
        Literal["usage_record_summary"]
    ] = "usage_record_summary"
    id: str
    """
    Unique identifier for the object.
    """
    invoice: Optional[str]
    """
    The invoice in which this usage period has been billed for.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["usage_record_summary"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    period: StripeObject
    subscription_item: str
    """
    The ID of the subscription item this summary is describing.
    """
    total_usage: int
    """
    The total usage within this usage period.
    """
