# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import Literal, NotRequired, TypedDict


class GbBankAccountCreateParams(TypedDict):
    account_number: str
    """
    The Account Number of the bank account.
    """
    bank_account_type: NotRequired[Literal["checking", "savings"]]
    """
    Closed Enum. The type of the bank account (checking or savings).
    """
    confirmation_of_payee: NotRequired[
        "GbBankAccountCreateParamsConfirmationOfPayee"
    ]
    """
    Whether or not to automatically perform Confirmation of Payee to verify the users information
    against what was provided by the bank. Doing so is required for all bank accounts not owned
    by you before making domestic UK OutboundPayments.
    """
    sort_code: str
    """
    The Sort Code of the bank account.
    """


class GbBankAccountCreateParamsConfirmationOfPayee(TypedDict):
    business_type: NotRequired[Literal["business", "personal"]]
    """
    The business type to be checked against. Legal entity information will be used if unspecified.
    Closed enum.
    """
    initiate: bool
    """
    User specifies whether Confirmation of Payee is automatically initiated when creating the bank account.
    """
    name: NotRequired[str]
    """
    The name to be checked against. Legal entity information will be used if unspecified.
    """
