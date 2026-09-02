# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import NotRequired, TypedDict


class PaymentRetryEvaluationUpdateParams(TypedDict):
    payment_intent: NotRequired[str]
    """
    PaymentIntent to update to. Must match the evaluation's signal type.
    """
    payment_record: NotRequired[str]
    """
    PaymentRecord to update to. Must match the evaluation's signal type.
    """
