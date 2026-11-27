# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List, Union
from typing_extensions import Literal, NotRequired, TypedDict


class ReportRunListParams(TypedDict):
    created: NotRequired["ReportRunListParamsCreated"]
    """
    If supplied, only return report runs created within this time range.
    """
    limit: NotRequired[int]
    """
    The maximum number of results per page. Defaults to 10. Maximum is 100.
    """
    report: NotRequired[str]
    """
    If supplied, only return report runs of the `Report` with this ID.
    """
    statuses: NotRequired[
        List[Union[Literal["canceled", "failed", "running", "succeeded"], str]]
    ]
    """
    If supplied, only return report runs that have any of these statuses.
    """


class ReportRunListParamsCreated(TypedDict):
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
