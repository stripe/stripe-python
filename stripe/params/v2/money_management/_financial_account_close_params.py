# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import NotRequired, TypedDict


class FinancialAccountCloseParams(TypedDict):
    forwarding_settings: NotRequired[
        "FinancialAccountCloseParamsForwardingSettings"
    ]
    """
    Settings that specify where to send positive balances and how to cover negative balances.
    You must provide these settings if the FinancialAccount has a non-zero balance.
    """


class FinancialAccountCloseParamsForwardingSettings(TypedDict):
    payment_method: NotRequired[str]
    """
    ID of the FinancialAccount that supplies funds to cover negative balances
    during or after this FinancialAccount's closure.
    """
    payout_method: NotRequired[str]
    """
    ID of the FinancialAccount that receives funds forwarded from this FinancialAccount when it closes.
    """
