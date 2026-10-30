# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.v2._amount import AmountParam
from typing_extensions import NotRequired, TypedDict

_CurrencyConversionCreateParamsBase = TypedDict(
    "CurrencyConversionCreateParams",
    {"from": "CurrencyConversionCreateParamsFrom"},
)


class CurrencyConversionCreateParams(_CurrencyConversionCreateParamsBase):
    financial_account: NotRequired[str]
    """
    The ID of the Financial Account in which the Currency Conversion should be created. If omitted, it will be created in the payments balance.
    """
    fx_quote: NotRequired[str]
    """
    The ID of the [FX Quote](https://docs.stripe.com/api/fx_quotes) to use.
    """
    to: "CurrencyConversionCreateParamsTo"
    """
    The destination currency to credit, optionally including an amount.
    """


class CurrencyConversionCreateParamsFrom(TypedDict):
    amount: NotRequired[AmountParam]
    """
    An amount specified for conversion.
    """
    currency: NotRequired[str]
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """


class CurrencyConversionCreateParamsTo(TypedDict):
    amount: NotRequired[AmountParam]
    """
    An amount specified for conversion.
    """
    currency: NotRequired[str]
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
