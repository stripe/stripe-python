# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import Dict
from typing_extensions import Literal, NotRequired, TypedDict


class SplitCreateParams(TypedDict):
    account: str
    """
    The target account for settling the SettlementAllocationIntentSplit.
    """
    amount: "SplitCreateParamsAmount"
    """
    The amount and currency of the SettlementAllocationIntentSplit.
    """
    metadata: NotRequired[Dict[str, str]]
    """
    Metadata associated with the SettlementAllocationIntentSplit.
    """
    type: Literal["credit", "debit"]
    """
    The type of the fund transfer.
    """


class SplitCreateParamsAmount(TypedDict):
    value: NotRequired[int]
    """
    A non-negative integer representing how much to charge in the [smallest currency unit](https://docs.stripe.com/currencies#minor-units).
    """
    currency: NotRequired[str]
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
