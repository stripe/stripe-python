# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import Literal, NotRequired, TypedDict


class SplitListParams(TypedDict):
    limit: NotRequired[int]
    """
    The page size.
    """
    status: NotRequired[Literal["canceled", "pending", "settled"]]
    """
    Filter the SettlementAllocationIntentSplits by status.
    """
