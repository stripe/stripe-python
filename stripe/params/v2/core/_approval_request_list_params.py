# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import NotRequired, TypedDict


class ApprovalRequestListParams(TypedDict):
    action: NotRequired[str]
    """
    Filter by action type (e.g. "refund.create", "payment_intent.create", "payout.create").
    """
    created: NotRequired["ApprovalRequestListParamsCreated"]
    """
    Filter by creation time.
    """
    limit: NotRequired[int]
    """
    Maximum number of results to return.
    """
    status: NotRequired[str]
    """
    Filter by approval request status (e.g. "requires_review", "approved", "succeeded", "failed", "rejected", "canceled", "expired").
    """


class ApprovalRequestListParamsCreated(TypedDict):
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
