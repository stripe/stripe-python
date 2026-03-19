# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.v2._amount import AmountParam
from typing import Dict
from typing_extensions import Literal, NotRequired, TypedDict


class SplitCreateParams(TypedDict):
    account: str
    """
    The target account for settling the SettlementAllocationIntentSplit.
    """
    amount: AmountParam
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
