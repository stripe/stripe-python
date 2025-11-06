# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar
from typing_extensions import Literal


class TransitBalance(StripeObject):
    """
    Funds that are in transit and destined for another balance or another connected account.
    """

    OBJECT_NAME: ClassVar[Literal["transit_balance"]] = "transit_balance"

    class Balance(StripeObject):
        available: int
        pending: int

    balance: Balance
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    currency: str
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["transit_balance"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    _inner_class_types = {"balance": Balance}
