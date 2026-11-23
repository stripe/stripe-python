# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List, Union
from typing_extensions import Literal, NotRequired, TypedDict


class SpendingMandateListParams(TypedDict):
    financial_account: NotRequired[str]
    """
    The ID of the FinancialAccount to filter by.
    """
    limit: NotRequired[int]
    """
    The page limit.
    """
    network: NotRequired["Literal['ach', 'bacs', 'sepa']|str"]
    """
    Filter by bank transfer network. If omitted, returns mandates for all networks.
    """
    statuses: NotRequired[
        List[
            Union[
                Literal[
                    "active", "canceled", "expired", "pending_cancellation"
                ],
                str,
            ]
        ]
    ]
    """
    Filter by mandate status.
    """
    type: NotRequired["Literal['bank_transfer']|str"]
    """
    The type of SpendingMandate to filter by.
    """
