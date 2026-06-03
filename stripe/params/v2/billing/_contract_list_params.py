# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import NotRequired, TypedDict


class ContractListParams(TypedDict):
    customer: NotRequired[str]
    """
    Filter by customer ID.
    """
    limit: NotRequired[int]
    """
    The limit for the number of results per page.
    """
