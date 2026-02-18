# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import List
from typing_extensions import Literal, NotRequired, TypedDict


class SubscriptionPauseParams(RequestOptions):
    bill_for: NotRequired["SubscriptionPauseParamsBillFor"]
    """
    Controls what to bill for when pausing the subscription.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    invoicing_behavior: NotRequired[Literal["invoice", "pending_invoice_item"]]
    """
    Determines how to handle debits and credits when pausing. The default is `pending_invoice_item`.
    """
    type: Literal["subscription"]
    """
    The type of pause to apply.
    """


class SubscriptionPauseParamsBillFor(TypedDict):
    outstanding_usage_through: NotRequired[
        "SubscriptionPauseParamsBillForOutstandingUsageThrough"
    ]
    """
    Controls when to bill for metered usage in the current period. Defaults to `{ type: "now" }`.
    """
    unused_time_from: NotRequired[
        "SubscriptionPauseParamsBillForUnusedTimeFrom"
    ]
    """
    Controls when to credit for unused time on licensed items. Defaults to `{ type: "now" }`.
    """


class SubscriptionPauseParamsBillForOutstandingUsageThrough(TypedDict):
    type: Literal["none", "now"]
    """
    When to bill metered usage in the current period.
    """


class SubscriptionPauseParamsBillForUnusedTimeFrom(TypedDict):
    type: Literal["item_current_period_start", "none", "now"]
    """
    When to credit for unused time.
    """
