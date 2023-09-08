# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.stripe_object import StripeObject
from typing import Any, Dict, List, Optional
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

    @classmethod
    def list(
        cls, api_key=None, stripe_version=None, stripe_account=None, **params
    ) -> ListObject["QuotePreviewSchedule"]:
        result = cls._static_request(
            "get",
            cls.class_url(),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )
        if not isinstance(result, ListObject):

            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result
