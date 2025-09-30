# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import NotRequired, TypedDict


class TransactionListParams(TypedDict):
    created: NotRequired[str]
    """
    Filter for Transactions created at an exact time.
    """
    created_gt: NotRequired[str]
    """
    Filter for Transactions created after the specified timestamp.
    """
    created_gte: NotRequired[str]
    """
    Filter for Transactions created at or after the specified timestamp.
    """
    created_lt: NotRequired[str]
    """
    Filter for Transactions created before the specified timestamp.
    """
    created_lte: NotRequired[str]
    """
    Filter for Transactions created at or before the specified timestamp.
    """
    financial_account: NotRequired[str]
    """
    Filter for Transactions belonging to a FinancialAccount.
    """
    flow: NotRequired[str]
    """
    Filter for Transactions corresponding to a Flow.
    """
    limit: NotRequired[int]
    """
    The page limit.
    """
