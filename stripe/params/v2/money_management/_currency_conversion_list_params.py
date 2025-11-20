# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import NotRequired, TypedDict


class CurrencyConversionListParams(TypedDict):
    financial_account: NotRequired[str]
    """
    The ID of the FinancialAccount to filter by.
    """
    limit: NotRequired[int]
    """
    The page limit.
    """
