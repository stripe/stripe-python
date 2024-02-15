# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Dict
from typing_extensions import Literal


class AccountInferredBalance(StripeObject):
    """
    A historical balance for the account on a particular day. It may be sourced from a balance snapshot provided by a financial institution, or inferred using transactions data.
    """

    OBJECT_NAME: ClassVar[
        Literal["financial_connections.account_inferred_balance"]
    ] = "financial_connections.account_inferred_balance"
    as_of: int
    """
    The time for which this balance was calculated, measured in seconds since the Unix epoch. If the balance was computed by Stripe and not provided directly by a financial institution, it will always be 23:59:59 UTC.
    """
    current: Dict[str, int]
    """
    The balances owed to (or by) the account holder.

    Each key is a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase.

    Each value is a integer amount. A positive amount indicates money owed to the account holder. A negative amount indicates money owed by the account holder.
    """
    id: str
    """
    Unique identifier for the object.
    """
    object: Literal["financial_connections.account_inferred_balance"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
