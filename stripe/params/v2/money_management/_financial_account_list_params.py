# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List
from typing_extensions import Literal, NotRequired, TypedDict


class FinancialAccountListParams(TypedDict):
    include: NotRequired[
        List[Literal["storage.deposit_insurance_eligibility"]]
    ]
    """
    Additional fields to include in the response.
    """
    limit: NotRequired[int]
    """
    The page limit.
    """
    statuses: NotRequired[List[Literal["closed", "open", "pending"]]]
    """
    Return FinancialAccounts whose `status` matches any of the provided values.
    If omitted, closed FinancialAccounts are not returned.
    """
