# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List
from typing_extensions import Literal, NotRequired, TypedDict


class FinancingOfferRefillParams(TypedDict):
    advance_amount: int
    """
    Amount of financing offered, in minor units. For example, 1,000 USD is represented as 100000.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    fee_amount: int
    """
    Fixed fee amount, in minor units. For example, 100 USD is represented as 10000.
    """
    financing_type: Literal["cash_advance", "fixed_term_loan", "flex_loan"]
    """
    The type of financing offer
    """
    status: NotRequired[
        Literal[
            "accepted",
            "accepted_other_offer",
            "canceled",
            "completed",
            "delivered",
            "expired",
            "fully_repaid",
            "paid_out",
            "rejected",
            "replaced",
            "undelivered",
        ]
    ]
    """
    The status of the financing offer
    """
    withhold_rate: float
    """
    Per-transaction rate at which Stripe withholds funds to repay the financing.
    """
