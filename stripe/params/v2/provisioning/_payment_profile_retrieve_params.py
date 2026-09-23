# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import NotRequired, TypedDict


class PaymentProfileRetrieveParams(TypedDict):
    livemode: NotRequired[bool]
    """
    Whether the billing operation should use Stripe live-mode objects. When omitted, this
    resolves from the authenticated request context.
    """
