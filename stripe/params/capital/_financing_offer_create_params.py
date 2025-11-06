# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import List
from typing_extensions import Literal, NotRequired


class FinancingOfferCreateParams(RequestOptions):
    advance_amount: int
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    fee_amount: int
    financing_type: Literal["cash_advance", "fixed_term_loan", "flex_loan"]
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
    withhold_rate: float
