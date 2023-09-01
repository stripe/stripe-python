# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.stripe_object import StripeObject
from typing import List
from typing import Optional
from typing_extensions import Literal


class QuoteLine(StripeObject):
    """
    A quote line defines a set of changes, in the order provided, that will be applied upon quote acceptance.
    """

    OBJECT_NAME = "quote_line"
    actions: List[StripeObject]
    applies_to: Optional[StripeObject]
    billing_cycle_anchor: Optional[str]
    ends_at: Optional[StripeObject]
    id: str
    object: Literal["quote_line"]
    proration_behavior: Optional[str]
    set_pause_collection: Optional[StripeObject]
    set_schedule_end: Optional[str]
    starts_at: Optional[StripeObject]
    trial_settings: Optional[StripeObject]
