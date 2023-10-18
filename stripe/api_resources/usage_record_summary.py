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
    invoice: Optional[str]
    livemode: bool
    object: Literal["usage_record_summary"]
    period: StripeObject
    subscription_item: str
    total_usage: int
