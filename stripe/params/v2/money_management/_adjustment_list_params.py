# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import NotRequired, TypedDict


class AdjustmentListParams(TypedDict):
    adjusted_flow: NotRequired[str]
    """
    Filter for Adjustments linked to a specific flow object. This filter only supports filtering by
    the flow object's ID, such as `ibt_123` for an InboundTransfer.
    """
    created: NotRequired["AdjustmentListParamsCreated"]
    """
    Filter for Adjustments by their creation time using `gt`, `gte`, `lt`, or `lte`.
    """
    limit: NotRequired[int]
    """
    The page limit.
    """


class AdjustmentListParamsCreated(TypedDict):
    gt: NotRequired[str]
    """
    Filter for Adjustments created after the specified timestamp.
    The timestamp must be in RFC 3339 format, for example `2022-09-18T13:22:00Z`.
    """
    gte: NotRequired[str]
    """
    Filter for Adjustments created on or after the specified timestamp.
    The timestamp must be in RFC 3339 format, for example `2022-09-18T13:22:00Z`.
    """
    lt: NotRequired[str]
    """
    Filter for Adjustments created before the specified timestamp.
    The timestamp must be in RFC 3339 format, for example `2022-09-18T13:22:00Z`.
    """
    lte: NotRequired[str]
    """
    Filter for Adjustments created on or before the specified timestamp.
    The timestamp must be in RFC 3339 format, for example `2022-09-18T13:22:00Z`.
    """
