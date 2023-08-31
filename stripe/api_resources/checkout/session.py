# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.stripe_object import StripeObject
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing_extensions import Literal


class Session(
    CreateableAPIResource["Session"], ListableAPIResource["Session"]
):
    """
    A Checkout Session represents your customer's session as they pay for
    one-time purchases or subscriptions through [Checkout](https://stripe.com/docs/payments/checkout)
    or [Payment Links](https://stripe.com/docs/payments/payment-links). We recommend creating a
    new Session each time your customer attempts to pay.

    Once payment is successful, the Checkout Session will contain a reference
    to the [Customer](https://stripe.com/docs/api/customers), and either the successful
    [PaymentIntent](https://stripe.com/docs/api/payment_intents) or an active
    [Subscription](https://stripe.com/docs/api/subscriptions).

    You can create a Checkout Session on your server and redirect to its URL
    to begin Checkout.

    Related guide: [Checkout quickstart](https://stripe.com/docs/checkout/quickstart)
    """

    OBJECT_NAME = "checkout.session"
    after_expiration: Optional[StripeObject]
    allow_promotion_codes: Optional[bool]
    amount_subtotal: Optional[int]
    amount_total: Optional[int]
    automatic_tax: StripeObject
    billing_address_collection: Optional[str]
    cancel_url: Optional[str]
    client_reference_id: Optional[str]
    consent: Optional[StripeObject]
    consent_collection: Optional[StripeObject]
    created: str
    currency: Optional[str]
    currency_conversion: Optional[StripeObject]
    custom_fields: List[StripeObject]
    custom_text: StripeObject
    customer: Optional[Any]
    customer_creation: Optional[str]
    customer_details: Optional[StripeObject]
    customer_email: Optional[str]
    expires_at: str
    id: str
    invoice: Optional[Any]
    invoice_creation: Optional[StripeObject]
    line_items: Any
    livemode: bool
    locale: Optional[str]
    metadata: Optional[Dict[str, str]]
    mode: str
    object: Literal["checkout.session"]
    payment_intent: Optional[Any]
    payment_link: Optional[Any]
    payment_method_collection: Optional[str]
    payment_method_options: Optional[StripeObject]
    payment_method_types: List[str]
    payment_status: str
    phone_number_collection: StripeObject
    recovered_from: Optional[str]
    setup_intent: Optional[Any]
    shipping_address_collection: Optional[StripeObject]
    shipping_cost: Optional[StripeObject]
    shipping_details: Optional[StripeObject]
    shipping_options: List[StripeObject]
    status: Optional[str]
    submit_type: Optional[str]
    subscription: Optional[Any]
    success_url: Optional[str]
    tax_id_collection: StripeObject
    total_details: Optional[StripeObject]
    url: Optional[str]

    @classmethod
    def _cls_expire(
        cls,
        session,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "post",
            "/v1/checkout/sessions/{session}/expire".format(
                session=util.sanitize_id(session)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_expire")
    def expire(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/checkout/sessions/{session}/expire".format(
                session=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def _cls_list_line_items(
        cls,
        session,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "get",
            "/v1/checkout/sessions/{session}/line_items".format(
                session=util.sanitize_id(session)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_list_line_items")
    def list_line_items(self, idempotency_key=None, **params):
        return self._request(
            "get",
            "/v1/checkout/sessions/{session}/line_items".format(
                session=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )
