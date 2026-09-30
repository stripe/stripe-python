# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import NotRequired, TypedDict


class TransactionEntryListParams(TypedDict):
    created: NotRequired["TransactionEntryListParamsCreated"]
    """
    Set of filters to query TransactionEntries within a range of `created` timestamps.
    """
    limit: NotRequired[int]
    """
    The page limit.
    """
    transaction: NotRequired[str]
    """
    Filter for TransactionEntries belonging to a Transaction.
    """


class TransactionEntryListParamsCreated(TypedDict):
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
