# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.v2._amount import AmountParam
from typing_extensions import NotRequired, TypedDict


class SettlementAllocationIntentUpdateParams(TypedDict):
    amount: NotRequired[AmountParam]
    """
    The new amount for the SettlementAllocationIntent. Only amount.value can be updated and currency must remain same.
    """
    reference: NotRequired[str]
    """
    The new reference for the SettlementAllocationIntent.
    """
