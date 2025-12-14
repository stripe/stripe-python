# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import NotRequired, TypedDict


class SettlementAllocationIntentUpdateParams(TypedDict):
    amount: NotRequired["SettlementAllocationIntentUpdateParamsAmount"]
    """
    The new amount for the SettlementAllocationIntent. Only amount.value can be updated and currency must remain same.
    """
    reference: NotRequired[str]
    """
    The new reference for the SettlementAllocationIntent.
    """


class SettlementAllocationIntentUpdateParamsAmount(TypedDict):
    value: NotRequired[int]
    """
    A non-negative integer representing how much to charge in the [smallest currency unit](https://docs.stripe.com/currencies#minor-units).
    """
    currency: NotRequired[str]
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
