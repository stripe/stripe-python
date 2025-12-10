# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import Dict
from typing_extensions import NotRequired, TypedDict


class SettlementAllocationIntentCreateParams(TypedDict):
    amount: "SettlementAllocationIntentCreateParamsAmount"
    """
    The amount and currency of the SettlementAllocationIntent.
    """
    expected_settlement_date: str
    """
    Expected date when we expect to receive the funds.
    """
    financial_account: str
    """
    FinancialAccount where the funds are expected to land / FinancialAccount to map this SettlementAllocationIntent to.
    """
    metadata: NotRequired[Dict[str, str]]
    """
    Metadata associated with the SettlementAllocationIntent.
    """
    reference: str
    """
    Reference for the settlement intent . Max 255 characters . The reference used by PSP to send funds to Stripe .
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
