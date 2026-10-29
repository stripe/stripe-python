# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, List, Optional
from typing_extensions import Literal


class GbBankAccount(StripeObject):
    """
    Use the GBBankAccounts API to create and manage GB bank account objects
    """

    OBJECT_NAME: ClassVar[Literal["v2.core.vault.gb_bank_account"]] = (
        "v2.core.vault.gb_bank_account"
    )
    archived: bool
    """
    Whether this bank account object was archived. Bank account objects can be archived through
    the /archive API, and they will not be automatically archived by Stripe. Archived bank account objects
    cannot be used as outbound destinations and will not appear in the outbound destination list.
    """
    bank_account_type: Literal["checking", "savings"]
    """
    Closed Enum. The type of the bank account (checking or savings).
    """
    bank_name: str
    """
    The name of the bank.
    """
    created: str
    """
    Creation time.
    """
    id: str
    """
    The ID of the GBBankAccount object.
    """
    last4: str
    """
    The last 4 digits of the account number or IBAN.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["v2.core.vault.gb_bank_account"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    restricted: bool
    """
    Whether the GB Bank Account is currently unusable for money movement, despite potentially being correctly set up. Please reach out to Stripe Support for more information.
    """
    sort_code: Optional[str]
    """
    The Sort Code of the bank account.
    """
    supported_currencies: List[str]
    """
    The list of currencies supported by this bank account.
    """
