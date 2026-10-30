# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import NotRequired, TypedDict


class FundingIntentListParams(TypedDict):
    created: NotRequired["FundingIntentListParamsCreated"]
    """
    Filters the results by their creation time.
    """
    limit: NotRequired[int]
    """
    The maximum number of results to return.
    """


class FundingIntentListParamsCreated(TypedDict):
    gt: NotRequired[str]
    """
    Return FundingIntents created after this timestamp.
    """
    gte: NotRequired[str]
    """
    Return FundingIntents created at or after this timestamp.
    """
    lt: NotRequired[str]
    """
    Return FundingIntents created before this timestamp.
    """
    lte: NotRequired[str]
    """
    Return FundingIntents created at or before this timestamp.
    """
