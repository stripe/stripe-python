# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List
from typing_extensions import Literal, NotRequired, TypedDict


class OutboundPaymentListParams(TypedDict):
    created: NotRequired["OutboundPaymentListParamsCreated"]
    """
    Filter OutboundPayments by their creation time.
    """
    limit: NotRequired[int]
    """
    The maximum number of results to return.
    """
    recipient: NotRequired[str]
    """
    Only return OutboundPayments sent to this recipient.
    """
    status: NotRequired[
        List[Literal["canceled", "failed", "posted", "processing", "returned"]]
    ]
    """
    Closed Enum. Only return OutboundPayments with this status.
    """


class OutboundPaymentListParamsCreated(TypedDict):
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
