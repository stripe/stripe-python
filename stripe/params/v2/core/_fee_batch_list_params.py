# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import NotRequired, TypedDict


class FeeBatchListParams(TypedDict):
    collection_record: NotRequired[str]
    """
    Filter to return only FeeBatches associated with this collection record ID.
    """
    created: NotRequired[str]
    """
    Filter for FeeBatches created at the exact specified timestamp.
    """
    created_gt: NotRequired[str]
    """
    Filter for FeeBatches created after the specified timestamp (exclusive).
    """
    created_gte: NotRequired[str]
    """
    Filter for FeeBatches created at or after the specified timestamp (inclusive).
    """
    created_lt: NotRequired[str]
    """
    Filter for FeeBatches created before the specified timestamp (exclusive).
    """
    created_lte: NotRequired[str]
    """
    Filter for FeeBatches created at or before the specified timestamp (inclusive).
    """
    limit: NotRequired[int]
    """
    Maximum number of results to return per page. Defaults to 20.
    """
