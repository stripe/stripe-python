# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import List
from typing_extensions import NotRequired, TypedDict


class SessionApproveParams(RequestOptions):
    attempt: str
    """
    The ID of the customer's attempt to pay to approve.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    payment_intent_data: NotRequired["SessionApproveParamsPaymentIntentData"]
    """
    A subset of parameters to be passed to PaymentIntent creation for Checkout Sessions in `payment` mode.
    """
    return_url: NotRequired[str]
    """
    The URL to redirect your customer back to after they authenticate or cancel their payment on the
    payment method's app or site. This parameter is allowed and required if and only if you did not
    set the return URL during Checkout Session creation or in `checkout.confirm()` in Stripe.js.
    """
    subscription_data: NotRequired["SessionApproveParamsSubscriptionData"]
    """
    A subset of parameters to be passed to subscription creation for Checkout Sessions in `subscription` mode.
    """


class SessionApproveParamsPaymentIntentData(TypedDict):
    application_fee_amount: NotRequired[int]
    """
    The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account. The amount of the application fee collected will be capped at the total amount captured. For more information, see the PaymentIntents [use case for connected accounts](https://docs.stripe.com/payments/connected-accounts).
    """


class SessionApproveParamsSubscriptionData(TypedDict):
    application_fee_percent: NotRequired[float]
    """
    A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account. To use an application fee percent, the request must be made on behalf of another account, using the `Stripe-Account` header or an OAuth key. For more information, see the application fees [documentation](https://stripe.com/docs/connect/subscriptions#collecting-fees-on-subscriptions).
    """
