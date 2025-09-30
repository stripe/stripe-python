# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import NotRequired, TypedDict


class IntentCommitParams(TypedDict):
    payment_intent: NotRequired[str]
    """
    ID of the PaymentIntent associated with this commit.
    """
