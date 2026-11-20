# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List, Union
from typing_extensions import Literal, NotRequired, TypedDict


class DisputeListParams(TypedDict):
    financial_account: NotRequired[str]
    """
    Filter results by the ID of the FinancialAccount associated with the dispute.
    """
    limit: NotRequired[int]
    """
    Maximum number of results to return, between 1 and 100. Defaults to 10.
    """
    statuses: NotRequired[
        List[Union[Literal["lost", "under_review", "won"], str]]
    ]
    """
    Filter results to Disputes with any of the provided statuses.
    """
    target: NotRequired[str]
    """
    Filter results by the ID of the disputed money movement.
    """
