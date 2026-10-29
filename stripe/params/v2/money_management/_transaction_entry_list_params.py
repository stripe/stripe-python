# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import NotRequired, TypedDict


class TransactionEntryListParams(TypedDict):
    created: NotRequired["TransactionEntryListParamsCreated"]
    """
    Filter for TransactionEntries created within a specified time range.
    """
    limit: NotRequired[int]
    """
    The page limit.
    """
    transaction: NotRequired[str]
    """
    Filter for TransactionEntries belonging to a specific Transaction. This filter only supports
    filtering by a Transaction ID, which appears in each TransactionEntry's `transaction` field.
    """


class TransactionEntryListParamsCreated(TypedDict):
    gt: NotRequired[str]
    """
    Filter for objects created after the specified timestamp.
    """
    gte: NotRequired[str]
    """
    Filter for objects created at or after the specified timestamp.
    """
    lt: NotRequired[str]
    """
    Filter for objects created before the specified timestamp.
    """
    lte: NotRequired[str]
    """
    Filter for objects created at or before the specified timestamp.
    """
