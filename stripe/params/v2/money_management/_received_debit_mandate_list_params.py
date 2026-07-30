# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List, Union
from typing_extensions import Literal, NotRequired, TypedDict


class ReceivedDebitMandateListParams(TypedDict):
    financial_account: NotRequired[str]
    """
    The ID of the FinancialAccount to filter by.
    """
    limit: NotRequired[int]
    """
    The page limit.
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
    type: NotRequired[Literal["bank_transfer"]]
    """
    The type of ReceivedDebitMandate to filter by.
    """
