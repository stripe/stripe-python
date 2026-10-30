# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List, Union
from typing_extensions import Literal, NotRequired, TypedDict


class AccountRejectParams(TypedDict):
    include: NotRequired[
        List[
            Literal[
                "configuration.card_creator",
                "configuration.customer",
                "configuration.developer",
                "configuration.merchant",
                "configuration.recipient",
                "configuration.money_manager",
                "defaults",
                "future_requirements",
                "identity",
                "requirements",
            ]
        ]
    ]
    """
    Additional fields to include in the response.
    """
    preserve_operations: NotRequired[List[Union[Literal["payouts"], str]]]
    """
    Operations that remain unaffected by the rejection. Repeated requests replace the previous set; omitting this field clears any preserved operations.
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
    The reason for rejecting the Account. Repeated requests replace the previously recorded reason.
    """
