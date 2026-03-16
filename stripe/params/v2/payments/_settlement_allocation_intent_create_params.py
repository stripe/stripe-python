# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.v2._amount import AmountParam
from typing import Dict
from typing_extensions import NotRequired, TypedDict


class SettlementAllocationIntentCreateParams(TypedDict):
    amount: AmountParam
    """
    The amount and currency of the SettlementAllocationIntent. Allowed Currencies are `gbp` | `eur`.
    """
    expected_settlement_date: str
    """
    Date when we expect to receive the funds. Must be in future .
    """
    financial_account: str
    """
    Financial Account Id where the funds are expected for this SettlementAllocationIntent.
    """
    metadata: NotRequired[Dict[str, str]]
    """
    Metadata associated with the SettlementAllocationIntent.
    """
    reference: str
    """
    Reference for the SettlementAllocationIntent. This should be same as the transaction reference used by payments processor to send funds to Stripe. Must have length between 5 and 255 characters and it must be unique among existing SettlementAllocationIntents that have a non-terminal status (`pending`, `submitted`, `matched`, `errored`).
    """
