# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.stripe_object import StripeObject
from typing import Optional
from typing_extensions import Literal


class UsageRecordSummary(StripeObject):
    OBJECT_NAME = "usage_record_summary"
    id: str
    invoice: Optional[str]
    livemode: bool
    object: Literal["usage_record_summary"]
    period: StripeObject
    subscription_item: str
    total_usage: int
