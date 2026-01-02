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
    outstanding_usage: NotRequired[bool]
    """
    Controls whether to debit for accrued metered usage in the current billing period. The default is `false`.
    """
    unused_time: NotRequired[bool]
    """
    Controls whether to credit for licensed items in the current billing period. The default is `false`.
    """
