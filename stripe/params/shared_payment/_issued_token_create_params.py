# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_object import UntypedStripeObject
from typing import Dict, List
from typing_extensions import Literal, NotRequired, TypedDict


class IssuedTokenCreateParams(RequestOptions):
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    payment_method: str
    """
    The PaymentMethod that is going to be shared by the SharedPaymentIssuedToken.
    """
    return_url: NotRequired[str]
    """
    If the customer does not exit their browser while authenticating, they will be redirected to this specified URL after completion.
    """
    seller_details: "IssuedTokenCreateParamsSellerDetails"
    """
    Seller details of the SharedPaymentIssuedToken, including network_id and external_id.
    """
    setup_future_usage: NotRequired[Literal["on_session"]]
    """
    Indicates that you intend to save the PaymentMethod of this SharedPaymentToken to a customer later.
    """
    shared_metadata: NotRequired["Dict[str, str]|UntypedStripeObject[str]"]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can attach to the SharedPaymentIssuedToken. The values here are visible by default with the party that you share this SharedPaymentIssuedToken with.
    """
    usage_limits: "IssuedTokenCreateParamsUsageLimits"
    """
    Limits on how this SharedPaymentToken can be used.
    """


class IssuedTokenCreateParamsSellerDetails(TypedDict):
    external_id: NotRequired[str]
    """
    A unique id within a network that identifies a logical seller, usually this would be the unique merchant id.
    """
    network_business_profile: NotRequired[str]
    """
    A string that identifies the network that this SharedToken is being created for.
    """


class IssuedTokenCreateParamsUsageLimits(TypedDict):
    currency: str
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    expires_at: NotRequired[int]
    """
    Time at which this SharedPaymentToken expires and can no longer be used to confirm a PaymentIntent.
    """
    max_amount: int
    """
    Max amount that can be captured using this SharedPaymentToken
    """
    recurring_interval: NotRequired[Literal["month", "week", "year"]]
    """
    The recurring interval at which the shared payment token's amount usage restrictions reset.
    """
