# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import Literal, NotRequired, TypedDict


class StatementListParams(TypedDict):
    limit: NotRequired[int]
    """
    The maximum number of results to return.
    """
    order_by: NotRequired[Literal["created", "period_end_date"]]
    """
    The field by which to sort results. Defaults to "created".
    """
