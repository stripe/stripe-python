# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import Union
from typing_extensions import Literal, NotRequired, TypedDict


class OutboundSetupIntentUpdateParams(TypedDict):
    payout_method: NotRequired[str]
    """
    If provided, the existing payout method resource to link to this outbound setup intent.
    """
    payout_method_data: NotRequired[
        "OutboundSetupIntentUpdateParamsPayoutMethodData"
    ]
    """
    If no payout_method provided, used to create the underlying credential that is set up for outbound money movement.
    If a payout_method provided, used to update data on the credential linked to this setup intent.
    Only card expiry (exp_month, exp_year) can be updated in the case where payout_method is provided.
    """


class OutboundSetupIntentUpdateParamsPayoutMethodData(TypedDict):
    bank_account: NotRequired[
        "OutboundSetupIntentUpdateParamsPayoutMethodDataBankAccount"
    ]
    """
    The type specific details of the bank account payout method.
    """
    type: Union[Literal["bank_account", "card"], str]
    """
    Open Enum. The type of payout method to be created/updated.
    """


class OutboundSetupIntentUpdateParamsPayoutMethodDataBankAccount(TypedDict):
    account_number: str
    """
    The account number or IBAN of the bank account.
    """
    bank_account_type: NotRequired[
        Literal["checking", "futsu", "savings", "toza"]
    ]
    """
    Closed Enum. The type of the bank account (checking or savings).
    """
    branch_number: NotRequired[str]
    """
    The branch number of the bank account, if present.
    """
    country: str
    """
    The country code of the bank account.
    """
    currency: str
    """
    The currency of the bank account.
    """
    routing_number: NotRequired[str]
    """
    The routing number of the bank account, if present.
    """
    swift_code: NotRequired[str]
    """
    The swift code of the bank account, if present.
    """
