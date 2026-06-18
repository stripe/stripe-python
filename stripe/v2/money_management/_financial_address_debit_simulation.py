# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar
from typing_extensions import Literal


class FinancialAddressDebitSimulation(StripeObject):
    """
    Debit Simulations represent a simulated debit transaction applied to financial addresses for testing purposes.
    """

    OBJECT_NAME: ClassVar[
        Literal["v2.money_management.financial_address_debit_simulation"]
    ] = "v2.money_management.financial_address_debit_simulation"
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["v2.money_management.financial_address_debit_simulation"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    status: str
    """
    The status of the request, signifying whether a simulated debit was initiated.
    """
