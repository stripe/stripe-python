# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import NotRequired, TypedDict

_CurrencyConversionCreateParamsBase = TypedDict(
    "CurrencyConversionCreateParams",
    {"from": "CurrencyConversionCreateParamsFrom"},
)


class CurrencyConversionCreateParams(_CurrencyConversionCreateParamsBase):
    financial_account: str
    """
    The FinancialAccount id to create the CurrencyConversion on.
    """
    to: "CurrencyConversionCreateParamsTo"
    """
    To amount object indicating the to currency or optional amount.
    """


class CurrencyConversionCreateParamsFrom(TypedDict):
    amount: NotRequired["CurrencyConversionCreateParamsFromAmount"]
    """
    Amount object.
    """
    currency: NotRequired[str]
    """
    A lowercase alpha3 currency code like "usd".
    """


class CurrencyConversionCreateParamsFromAmount(TypedDict):
    value: NotRequired[int]
    """
    A non-negative integer representing how much to charge in the [smallest currency unit](https://docs.stripe.com/currencies#minor-units).
    """
    currency: NotRequired[str]
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """


class CurrencyConversionCreateParamsTo(TypedDict):
    amount: NotRequired["CurrencyConversionCreateParamsToAmount"]
    """
    Amount object.
    """
    currency: NotRequired[str]
    """
    A lowercase alpha3 currency code like "usd".
    """


class CurrencyConversionCreateParamsToAmount(TypedDict):
    value: NotRequired[int]
    """
    A non-negative integer representing how much to charge in the [smallest currency unit](https://docs.stripe.com/currencies#minor-units).
    """
    currency: NotRequired[str]
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
