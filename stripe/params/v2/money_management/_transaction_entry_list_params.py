# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import NotRequired, TypedDict


class TransactionEntryListParams(TypedDict):
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
    limit: NotRequired[int]
    """
    The page limit.
    """
    transaction: NotRequired[str]
    """
    Filter for TransactionEntries belonging to a Transaction.
    """
