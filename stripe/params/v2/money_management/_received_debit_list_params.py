# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import NotRequired, TypedDict


class ReceivedDebitListParams(TypedDict):
    created: NotRequired["ReceivedDebitListParamsCreated"]
    """
    Filter ReceivedDebits by their creation time.
    """
    limit: NotRequired[int]
    """
    The page limit.
    """


class ReceivedDebitListParamsCreated(TypedDict):
    gt: NotRequired[str]
    """
    Return ReceivedDebits created after this timestamp.
    """
    gte: NotRequired[str]
    """
    Return ReceivedDebits created on or after this timestamp.
    """
    lt: NotRequired[str]
    """
    Return ReceivedDebits created before this timestamp.
    """
    lte: NotRequired[str]
    """
    Return ReceivedDebits created on or before this timestamp.
    """
