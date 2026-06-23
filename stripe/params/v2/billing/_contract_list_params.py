# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List
from typing_extensions import Literal, NotRequired, TypedDict


class ContractListParams(TypedDict):
    customer: NotRequired[str]
    """
    Filter by customer ID.
    """
    include: NotRequired[
        List[
            Literal[
                "billing_settings",
                "one_time_fees",
                "pricing_lines",
                "pricing_overrides",
            ]
        ]
    ]
    """
    Additional fields to include in the response.
    """
    limit: NotRequired[int]
    """
    The limit for the number of results per page.
    """
