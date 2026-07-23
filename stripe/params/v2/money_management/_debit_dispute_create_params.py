# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import Literal, NotRequired, TypedDict


class DebitDisputeCreateParams(TypedDict):
    bank_transfer: NotRequired["DebitDisputeCreateParamsBankTransfer"]
    """
    Parameters for bank transfer disputes.
    """
    received_debit: str
    """
    The ID of the ReceivedDebit to dispute.
    """


class DebitDisputeCreateParamsBankTransfer(TypedDict):
    reason: NotRequired[
        "Literal['incorrect_amount_or_date', 'unauthorized']|str"
    ]
    """
    The reason for the dispute.
    """
