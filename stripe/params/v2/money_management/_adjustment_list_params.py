# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import NotRequired, TypedDict


class AdjustmentListParams(TypedDict):
    adjusted_flow: NotRequired[str]
    """
    Filter for Adjustments linked to a Flow.
    """
    created: NotRequired["AdjustmentListParamsCreated"]
    """
    Set of filters to query Adjustments within a range of `created` timestamps.
    """
    limit: NotRequired[int]
    """
    The page limit.
    """


class AdjustmentListParamsCreated(TypedDict):
    gt: NotRequired[str]
    """
    Filter for objects created after the specified timestamp.
    Must be an RFC 3339 date & time value, for example: 2022-09-18T13:22:00Z.
    """
    gte: NotRequired[str]
    """
    Filter for objects created on or after the specified timestamp.
    Must be an RFC 3339 date & time value, for example: 2022-09-18T13:22:00Z.
    """
    lt: NotRequired[str]
    """
    Filter for objects created before the specified timestamp.
    Must be an RFC 3339 date & time value, for example: 2022-09-18T13:22:00Z.
    """
    lte: NotRequired[str]
    """
    Filter for objects created on or before the specified timestamp.
    Must be an RFC 3339 date & time value, for example: 2022-09-18T13:22:00Z.
    """
