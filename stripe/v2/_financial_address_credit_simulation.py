# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar
from typing_extensions import Literal


class FinancialAddressCreditSimulation(StripeObject):
    OBJECT_NAME: ClassVar[Literal["financial_address_credit_simulation"]] = (
        "financial_address_credit_simulation"
    )
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["financial_address_credit_simulation"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    status: str
    """
    The status of the request, signifying whether a simulated credit was initiated.
    """
