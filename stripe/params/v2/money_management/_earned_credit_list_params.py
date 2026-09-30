# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import NotRequired, TypedDict


class EarnedCreditListParams(TypedDict):
    financial_account: NotRequired[str]
    """
    The FinancialAccount to list EarnedCredits for.
    """
    limit: NotRequired[int]
    """
    The maximum number of EarnedCredits to return.
    """
