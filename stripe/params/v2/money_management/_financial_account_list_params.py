# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List, Union
from typing_extensions import Literal, NotRequired, TypedDict


class FinancialAccountListParams(TypedDict):
    include: NotRequired[List[Literal["payments.balance_by_funds_type"]]]
    """
    Additional fields to include in the response.
    """
    limit: NotRequired[int]
    """
    The page limit.
    """
    statuses: NotRequired[List[Literal["closed", "open", "pending"]]]
    """
    Filter for FinancialAccount `status`. By default, closed FinancialAccounts are not returned.
    """
    types: NotRequired[
        List[
            Union[
                Literal[
                    "accrued_fees",
                    "credit",
                    "multiprocessor_settlement",
                    "payments",
                    "storage",
                ],
                str,
            ]
        ]
    ]
    """
    Filter for FinancialAccount `type`. By default, FinancialAccounts of any `type` are returned.
    """
