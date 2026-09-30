# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import NotRequired, TypedDict


class TransactionListParams(TypedDict):
    created: NotRequired["TransactionListParamsCreated"]
    """
    Set of filters to query Transactions within a range of `created` timestamps.
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


class TransactionListParamsCreated(TypedDict):
    gt: NotRequired[str]
    """
    Filter for Transactions created after the specified timestamp.
    """
    gte: NotRequired[str]
    """
    Filter for Transactions created at or after the specified timestamp.
    """
    lt: NotRequired[str]
    """
    Filter for Transactions created before the specified timestamp.
    """
    lte: NotRequired[str]
    """
    Filter for Transactions created at or before the specified timestamp.
    """
