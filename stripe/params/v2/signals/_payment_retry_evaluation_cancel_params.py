# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import NotRequired, TypedDict


class PaymentRetryEvaluationCancelParams(TypedDict):
    cancellation_reason: NotRequired[str]
    """
    Optional reason for canceling the evaluation.
    """
