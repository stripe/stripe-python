# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.v2._amount import AmountParam
from typing import Union
from typing_extensions import Literal, NotRequired, TypedDict


class SpendingMandateCreateParams(TypedDict):
    bank_transfer: NotRequired["SpendingMandateCreateParamsBankTransfer"]
    """
    Bank transfer authorization details. Required when `type` is `bank_transfer`.
    """
    financial_account: str
    """
    The Financial Account to authorize debits against.
    """
    type: Union[Literal["bank_transfer"], str]
    """
    The mandate type.
    """


class SpendingMandateCreateParamsBankTransfer(TypedDict):
    account_holder_name: str
    """
    Display name for the authorized originator.
    """
    ach: NotRequired["SpendingMandateCreateParamsBankTransferAch"]
    """
    ACH authorization details. Required when `network` is `ach`.
    """
    financial_address: str
    """
    An active US Financial Address belonging to the Financial Account.
    """
    network: Union[Literal["ach"], str]
    """
    The bank transfer network. Only ACH mandates can be created.
    """


class SpendingMandateCreateParamsBankTransferAch(TypedDict):
    originator_company_id: str
    """
    ACH Company ID identifying the authorized originator. Must contain exactly 10 alphanumeric characters.
    """
    transaction_limit: NotRequired[AmountParam]
    """
    Positive per-debit limit in USD.
    """
