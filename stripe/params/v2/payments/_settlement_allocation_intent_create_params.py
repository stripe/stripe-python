# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import Dict
from typing_extensions import NotRequired, TypedDict


class SettlementAllocationIntentCreateParams(TypedDict):
    amount: "SettlementAllocationIntentCreateParamsAmount"
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


class SettlementAllocationIntentCreateParamsAmount(TypedDict):
    value: NotRequired[int]
    """
    A non-negative integer representing how much to charge in the [smallest currency unit](https://docs.stripe.com/currencies#minor-units).
    """
    currency: NotRequired[str]
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
