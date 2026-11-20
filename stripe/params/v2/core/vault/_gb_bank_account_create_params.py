# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import Literal, NotRequired, TypedDict


class GbBankAccountCreateParams(TypedDict):
    account_number: NotRequired[str]
    """
    The Account Number of the bank account.
    """
    bank_account_type: NotRequired[Literal["checking", "savings"]]
    """
    Closed Enum. The type of the bank account (checking or savings).
    """
    currency: str
    """
    The currency of the bank account.
    """
    iban: NotRequired[str]
    """
    The IBAN of the bank account.
    """
    sort_code: NotRequired[str]
    """
    The Sort Code of the bank account.
    """
