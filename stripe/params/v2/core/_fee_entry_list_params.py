# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import NotRequired, TypedDict


class FeeEntryListParams(TypedDict):
    collection_record: NotRequired[str]
    """
    Filter by money movement id (e.g. txn_xxx, bt_xxx).
    """
    created: NotRequired[str]
    """
    Filter for FeeEntries created at the exact specified timestamp.
    """
    created_gt: NotRequired[str]
    """
    Filter for FeeEntries created after the specified timestamp (exclusive).
    """
    created_gte: NotRequired[str]
    """
    Filter for FeeEntries created at or after the specified timestamp (inclusive).
    """
    created_lt: NotRequired[str]
    """
    Filter for FeeEntries created before the specified timestamp (exclusive).
    """
    created_lte: NotRequired[str]
    """
    Filter for FeeEntries created at or before the specified timestamp (inclusive).
    """
    fee_batch: NotRequired[str]
    """
    Filter by fee batch id (fb_xxx).
    """
    incurred_by: NotRequired[str]
    """
    Filter by usage object id (e.g. ch_xxx, py_xxx).
    """
    limit: NotRequired[int]
    """
    Maximum number of results to return per page. Defaults to 20.
    """
