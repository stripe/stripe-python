# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import NotRequired, TypedDict


class InboundTransferListParams(TypedDict):
    created: NotRequired[str]
    """
    Filter for objects created at the specified timestamp.
    Must be an RFC 3339 date & time value, for example: 2022-09-18T13:22:00Z.
    """
    created_gt: NotRequired[str]
    """
    Filter for objects created after the specified timestamp.
    Must be an RFC 3339 date & time value, for example: 2022-09-18T13:22:00Z.
    """
    created_gte: NotRequired[str]
    """
    Filter for objects created on or after the specified timestamp.
    Must be an RFC 3339 date & time value, for example: 2022-09-18T13:22:00Z.
    """
    created_lt: NotRequired[str]
    """
    Filter for objects created before the specified timestamp.
    Must be an RFC 3339 date & time value, for example: 2022-09-18T13:22:00Z.
    """
    created_lte: NotRequired[str]
    """
    Filter for objects created on or before the specified timestamp.
    Must be an RFC 3339 date & time value, for example: 2022-09-18T13:22:00Z.
    """
    limit: NotRequired[int]
    """
    The page limit.
    """
