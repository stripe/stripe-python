# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List, Union
from typing_extensions import Literal, NotRequired, TypedDict


class QueryRunListParams(TypedDict):
    created: NotRequired["QueryRunListParamsCreated"]
    """
    If supplied, only return query runs created within this time range.
    """
    limit: NotRequired[int]
    """
    The maximum number of results per page. Defaults to 10. Maximum is 100.
    """
    statuses: NotRequired[
        List[Union[Literal["canceled", "failed", "running", "succeeded"], str]]
    ]
    """
    If supplied, only return query runs that have any of these statuses.
    """


class QueryRunListParamsCreated(TypedDict):
    gt: NotRequired[str]
    """
    Only return runs created after this time.
    """
    gte: NotRequired[str]
    """
    Only return runs created at or after this time.
    """
    lt: NotRequired[str]
    """
    Only return runs created before this time.
    """
    lte: NotRequired[str]
    """
    Only return runs created at or before this time.
    """
