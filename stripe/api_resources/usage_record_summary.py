# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.stripe_object import StripeObject
from typing import Optional
from typing_extensions import Literal


class UsageRecordSummary(StripeObject):
    OBJECT_NAME = "usage_record_summary"

    class Period(StripeObject):
        end: Optional[int]
        start: Optional[int]

    id: str
    invoice: Optional[str]
    livemode: bool
    object: Literal["usage_record_summary"]
    period: Period
    subscription_item: str
    total_usage: int

    _inner_class_types = {"period": Period}
