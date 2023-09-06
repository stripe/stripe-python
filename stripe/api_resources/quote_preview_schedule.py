# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.expandable_field import ExpandableField
from stripe.stripe_object import StripeObject
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing_extensions import Literal

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.subscription import Subscription
    from stripe.api_resources.test_helpers.test_clock import TestClock


class QuotePreviewSchedule(ListableAPIResource["QuotePreviewSchedule"]):
    OBJECT_NAME = "quote_preview_schedule"
    application: Optional[ExpandableField[Any]]
    applies_to: StripeObject
    billing_behavior: str
    canceled_at: Optional[str]
    completed_at: Optional[str]
    created: str
    current_phase: Optional[StripeObject]
    customer: ExpandableField[Any]
    default_settings: StripeObject
    end_behavior: str
    id: str
    livemode: bool
    metadata: Optional[Dict[str, str]]
    object: Literal["quote_preview_schedule"]
    phases: List[StripeObject]
    prebilling: Optional[StripeObject]
    released_at: Optional[str]
    released_subscription: Optional[str]
    status: str
    subscription: Optional[ExpandableField["Subscription"]]
    test_clock: Optional[ExpandableField["TestClock"]]
