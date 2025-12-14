# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import Dict, List
from typing_extensions import Literal, NotRequired, TypedDict


class GrantedTokenCreateParams(TypedDict):
    customer: NotRequired[str]
    """
    The Customer that the SharedPaymentGrantedToken belongs to. Should match the Customer that the PaymentMethod is attached to if any.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    payment_method: str
    """
    The PaymentMethod that is going to be shared by the SharedPaymentGrantedToken.
    """
    shared_metadata: NotRequired["Literal['']|Dict[str, str]"]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can attach to the SharedPaymentGrantedToken.
    """
    usage_limits: "GrantedTokenCreateParamsUsageLimits"
    """
    Limits on how this SharedPaymentGrantedToken can be used.
    """


class GrantedTokenCreateParamsUsageLimits(TypedDict):
    currency: str
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    expires_at: int
    """
    Time at which this SharedPaymentToken expires and can no longer be used to confirm a PaymentIntent.
    """
    max_amount: int
    """
    Max amount that can be captured using this SharedPaymentToken
    """
