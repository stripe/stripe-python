# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import UntypedStripeObject
from typing import Dict, Union
from typing_extensions import Literal, NotRequired, TypedDict


class DisputeCreateParams(TypedDict):
    explanation: NotRequired[str]
    """
    Additional information explaining the dispute. Must contain non-whitespace text and be no longer than 5000 characters.
    """
    metadata: NotRequired["Dict[str, str]|UntypedStripeObject[str]"]
    """
    Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    reason: Union[
        Literal[
            "authorization_revoked",
            "duplicate",
            "incorrect_amount",
            "incorrect_date",
            "other",
            "unauthorized",
        ],
        str,
    ]
    """
    The FinancialAccount holder's reason for disputing the money movement.
    """
    target: "DisputeCreateParamsTarget"
    """
    The money movement being disputed.
    """


class DisputeCreateParamsTarget(TypedDict):
    received_debit: NotRequired[str]
    """
    If applicable, the ID of the ReceivedDebit being disputed.
    """
    type: Union[Literal["received_debit"], str]
    """
    The type of money movement being disputed.
    """
