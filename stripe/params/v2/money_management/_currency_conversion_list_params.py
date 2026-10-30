# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import NotRequired, TypedDict


class CurrencyConversionListParams(TypedDict):
    financial_account: NotRequired[str]
    """
    The ID of the Financial Account for which conversions should be listed.
    """
    limit: NotRequired[int]
    """
    The maximum number of Currency Conversions to return.
    """
