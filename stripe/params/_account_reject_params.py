# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import List, Union
from typing_extensions import Literal, NotRequired


class AccountRejectParams(RequestOptions):
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    payouts_action: NotRequired[Literal["none", "pause"]]
    """
    Whether to pause payouts on the account as part of the rejection. Defaults to `pause`. Use `none` to leave payouts enabled.
    """
    reason: Union[
        Literal[
            "credit",
            "fraud_no_intent_to_fulfill",
            "fraud_other",
            "fraud_payment_method_casher",
            "fraud_payment_method_tester",
            "other",
            "terms_of_service",
        ],
        str,
    ]
    """
    The reason for rejecting the account. Can be `fraud_payment_method_casher`, `fraud_payment_method_tester`, `fraud_no_intent_to_fulfill`, `fraud_other`, `credit`, `terms_of_service`, or `other`.
    """
