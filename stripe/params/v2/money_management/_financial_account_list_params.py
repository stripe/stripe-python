# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import Literal, NotRequired, TypedDict


class FinancialAccountListParams(TypedDict):
    limit: NotRequired[int]
    """
    The page limit.
    """
    status: NotRequired[Literal["closed", "open", "pending"]]
    """
    The status of the FinancialAccount to filter by. By default, closed FinancialAccounts are not returned.
    """
