# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import Literal, NotRequired, TypedDict


class DebitDisputeListParams(TypedDict):
    financial_account: NotRequired[str]
    """
    Filter by a Financial Account.
    """
    limit: NotRequired[int]
    """
    The page limit.
    """
    status: NotRequired[Literal["failed", "submitted", "succeeded"]]
    """
    Filter by status.
    """
