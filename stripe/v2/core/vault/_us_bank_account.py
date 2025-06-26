# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Optional
from typing_extensions import Literal


class UsBankAccount(StripeObject):
    """
    Use the USBankAccounts API to create and manage US bank accounts objects that you can use to receive funds. Note that these are not interchangeable with v1 Tokens.
    """

    OBJECT_NAME: ClassVar[Literal["v2.core.vault.us_bank_account"]] = (
        "v2.core.vault.us_bank_account"
    )
    archived: bool
    """
    Whether this USBankAccount object was archived.
    """
    bank_account_type: Literal["checking", "savings"]
    """
    Closed Enum. The type of bank account (checking or savings).
    """
    bank_name: str
    """
    The name of the bank this bank account belongs to. This field is populated automatically by Stripe based on the routing number.
    """
    created: str
    """
    Creation time of the object.
    """
    fedwire_routing_number: Optional[str]
    """
    The fedwire routing number of the bank account.
    """
    id: str
    """
    The ID of the USBankAccount object.
    """
    last4: str
    """
    The last 4 digits of the account number.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["v2.core.vault.us_bank_account"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    routing_number: Optional[str]
    """
    The ACH routing number of the bank account.
    """
