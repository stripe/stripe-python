# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List
from typing_extensions import Literal, NotRequired, TypedDict


class PayoutMethodListParams(TypedDict):
    limit: NotRequired[int]
    """
    The page size.
    """
    usage_status: NotRequired["PayoutMethodListParamsUsageStatus"]
    """
    Usage status filter.
    """


class PayoutMethodListParamsUsageStatus(TypedDict):
    payments: NotRequired[
        List[Literal["eligible", "invalid", "requires_action"]]
    ]
    """
    List of payments status to filter by.
    """
    transfers: NotRequired[
        List[Literal["eligible", "invalid", "requires_action"]]
    ]
    """
    List of transfers status to filter by.
    """
