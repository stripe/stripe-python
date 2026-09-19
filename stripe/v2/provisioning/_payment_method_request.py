# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar
from typing_extensions import Literal


class PaymentMethodRequest(StripeObject):
    """
    The result of an in-progress request for a customer to authorize a new payment method.
    """

    OBJECT_NAME: ClassVar[
        Literal["v2.provisioning.payment_method_request"]
    ] = "v2.provisioning.payment_method_request"
    checkout_session_url: str
    """
    URL for the customer to complete payment method authorization.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["v2.provisioning.payment_method_request"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    status: Literal["checkout_initiated", "complete"]
    """
    Status of the payment method request.
    """
