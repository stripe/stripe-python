# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import Literal, NotRequired, TypedDict


class SettlementAllocationIntentListParams(TypedDict):
    created_gt: NotRequired[str]
    """
    Filter for objects created after the specified timestamp.
    Must be an RFC 3339 date & time value, for example: 2025-10-17T13:22::00Z.
    """
    created_gte: NotRequired[str]
    """
    Filter for objects created on or after the specified timestamp.
    Must be an RFC 3339 date & time value, for example: 2025-10-17T13:22::00Z.
    """
    created_lt: NotRequired[str]
    """
    Filter for objects created before the specified timestamp.
    Must be an RFC 3339 date & time value, for example: 2025-10-17T13:22::00Z.
    """
    created_lte: NotRequired[str]
    """
    Filter for objects created on or before the specified timestamp.
    Must be an RFC 3339 date & time value, for example: 2025-10-17T13:22::00Z.
    """
    financial_account: NotRequired[str]
    """
    Filter the SettlementAllocationIntents by FinancialAccount.
    """
    limit: NotRequired[int]
    """
    The page size.
    """
    status: NotRequired[
        Literal[
            "canceled", "errored", "matched", "pending", "settled", "submitted"
        ]
    ]
    """
    Filter the SettlementAllocationIntents by status.
    """
