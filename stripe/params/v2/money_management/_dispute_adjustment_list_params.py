# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import NotRequired, TypedDict


class DisputeAdjustmentListParams(TypedDict):
    financial_account: NotRequired[str]
    """
    Filter results by the ID of the FinancialAccount associated with the DisputeAdjustment.
    """
    limit: NotRequired[int]
    """
    Maximum number of results to return, between 1 and 100. Defaults to 10.
    """
    related_dispute: NotRequired[str]
    """
    Filter results by the ID of the Dispute associated with the DisputeAdjustment.
    """
