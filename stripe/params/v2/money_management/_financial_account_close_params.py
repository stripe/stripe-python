# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import NotRequired, TypedDict


class FinancialAccountCloseParams(TypedDict):
    forwarding_settings: NotRequired[
        "FinancialAccountCloseParamsForwardingSettings"
    ]
    """
    The addresses to forward any incoming transactions to.
    """


class FinancialAccountCloseParamsForwardingSettings(TypedDict):
    payment_method: NotRequired[str]
    """
    The address to send forwarded payments to.
    """
    payout_method: NotRequired[str]
    """
    The address to send forwarded payouts to.
    """
