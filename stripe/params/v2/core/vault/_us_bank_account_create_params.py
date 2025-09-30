# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import Literal, NotRequired, TypedDict


class UsBankAccountCreateParams(TypedDict):
    account_number: str
    """
    The account number of the bank account.
    """
    bank_account_type: NotRequired[Literal["checking", "savings"]]
    """
    Closed Enum. The type of the bank account (checking or savings).
    """
    fedwire_routing_number: NotRequired[str]
    """
    The fedwire routing number of the bank account. Note that certain banks have the same ACH and wire routing number.
    """
    routing_number: NotRequired[str]
    """
    The ACH routing number of the bank account. Note that certain banks have the same ACH and wire routing number.
    """
