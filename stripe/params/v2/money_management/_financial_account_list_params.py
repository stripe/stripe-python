# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List
from typing_extensions import Literal, NotRequired, TypedDict


class FinancialAccountListParams(TypedDict):
    limit: NotRequired[int]
    """
    The page limit.
    """
    statuses: NotRequired[List[Literal["closed", "open", "pending"]]]
    """
    Filter for FinancialAccount `status`. By default, closed FinancialAccounts are not returned.
    """
