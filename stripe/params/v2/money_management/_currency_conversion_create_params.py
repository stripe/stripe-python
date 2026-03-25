# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.v2._amount import AmountParam
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
    amount: NotRequired[AmountParam]
    """
    Amount object.
    """
    currency: NotRequired[str]
    """
    A lowercase alpha3 currency code like "usd".
    """


class CurrencyConversionCreateParamsTo(TypedDict):
    amount: NotRequired[AmountParam]
    """
    Amount object.
    """
    currency: NotRequired[str]
    """
    A lowercase alpha3 currency code like "usd".
    """
