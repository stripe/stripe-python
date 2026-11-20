# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import NotRequired, TypedDict


class TransactionListParams(TypedDict):
    created: NotRequired["TransactionListParamsCreated"]
    """
    Filter for Transactions created within a specified time range.
    """
    financial_account: NotRequired[str]
    """
    Filter for Transactions belonging to a specific FinancialAccount. This filter only supports filtering by the FinancialAccount's ID.
    """
    flow: NotRequired[str]
    """
    Filter for Transactions created by a specific flow object. This filter only supports filtering by
    the flow object's ID, such as `ibt_123` for an InboundTransfer. A value that doesn't match a flow ID
    returns an empty list.
    """
    limit: NotRequired[int]
    """
    The page limit.
    """


class TransactionListParamsCreated(TypedDict):
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
