# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Union
from typing_extensions import Literal


class EarnedCreditSimulation(StripeObject):
    """
    EarnedCredit Simulations represent simulated EarnedCredit creation requests for testing purposes.
    """

    OBJECT_NAME: ClassVar[
        Literal["v2.money_management.earned_credit_simulation"]
    ] = "v2.money_management.earned_credit_simulation"
    livemode: bool
    """
    Has the value true if the object exists in live mode.
    """
    object: Literal["v2.money_management.earned_credit_simulation"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    status: Union[Literal["accepted"], str]
    """
    The status of the request, signifying whether simulated EarnedCredit creation was initiated.
    """
