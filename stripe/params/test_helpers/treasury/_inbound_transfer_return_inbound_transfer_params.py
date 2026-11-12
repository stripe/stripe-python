# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List
from typing_extensions import Literal, NotRequired, TypedDict


class InboundTransferReturnInboundTransferParams(TypedDict):
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    failure_details: NotRequired[
        "InboundTransferReturnInboundTransferParamsFailureDetails"
    ]
    """
    Details about a returned InboundTransfer.
    """


class InboundTransferReturnInboundTransferParamsFailureDetails(TypedDict):
    code: NotRequired[
        "Literal['account_closed', 'account_frozen', 'bank_account_restricted', 'bank_ownership_changed', 'debit_not_authorized', 'incorrect_account_holder_address', 'incorrect_account_holder_name', 'incorrect_account_holder_tax_id', 'insufficient_funds', 'invalid_account_number', 'invalid_currency', 'no_account', 'other']|str"
    ]
    """
    Reason for the failure.
    """
    network_details: NotRequired[
        "InboundTransferReturnInboundTransferParamsFailureDetailsNetworkDetails"
    ]
    """
    Network specific details for the failure.
    """


class InboundTransferReturnInboundTransferParamsFailureDetailsNetworkDetails(
    TypedDict,
):
    ach: NotRequired[
        "InboundTransferReturnInboundTransferParamsFailureDetailsNetworkDetailsAch"
    ]
    """
    ACH network failure details.
    """
    type: Literal["ach"]
    """
    The network used to transfer funds.
    """


class InboundTransferReturnInboundTransferParamsFailureDetailsNetworkDetailsAch(
    TypedDict,
):
    return_code: str
    """
    NACHA ACH return code.
    """
