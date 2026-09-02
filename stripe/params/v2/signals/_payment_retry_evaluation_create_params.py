# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import NotRequired, TypedDict


class PaymentRetryEvaluationCreateParams(TypedDict):
    payment_intent: NotRequired[str]
    """
    ID of the PaymentIntent to evaluate. Mutually exclusive with payment_record.
    """
    payment_record: NotRequired[str]
    """
    ID of the PaymentRecord to evaluate. Mutually exclusive with payment_intent.
    """
