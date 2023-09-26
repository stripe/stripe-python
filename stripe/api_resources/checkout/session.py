# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
)
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.stripe_object import StripeObject
from typing import Any, Dict, List, Optional, cast
from typing_extensions import Literal

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.customer import Customer
    from stripe.api_resources.invoice import Invoice
    from stripe.api_resources.line_item import LineItem
    from stripe.api_resources.payment_intent import PaymentIntent
    from stripe.api_resources.payment_link import PaymentLink
    from stripe.api_resources.setup_intent import SetupIntent
    from stripe.api_resources.subscription import Subscription


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
    billing_address_collection: Optional[Literal["auto", "required"]]
    cancel_url: Optional[str]
    client_reference_id: Optional[str]
    consent: Optional[StripeObject]
    consent_collection: Optional[StripeObject]
    created: int
    currency: Optional[str]
    currency_conversion: Optional[StripeObject]
    custom_fields: List[StripeObject]
    custom_text: StripeObject
    customer: Optional[ExpandableField["Customer"]]
    customer_creation: Optional[Literal["always", "if_required"]]
    customer_details: Optional[StripeObject]
    customer_email: Optional[str]
    expires_at: int
    id: str
    invoice: Optional[ExpandableField["Invoice"]]
    invoice_creation: Optional[StripeObject]
    line_items: Optional[ListObject["LineItem"]]
    livemode: bool
    locale: Optional[
        Literal[
            "auto",
            "bg",
            "cs",
            "da",
            "de",
            "el",
            "en",
            "en-GB",
            "es",
            "es-419",
            "et",
            "fi",
            "fil",
            "fr",
            "fr-CA",
            "hr",
            "hu",
            "id",
            "it",
            "ja",
            "ko",
            "lt",
            "lv",
            "ms",
            "mt",
            "nb",
            "nl",
            "pl",
            "pt",
            "pt-BR",
            "ro",
            "ru",
            "sk",
            "sl",
            "sv",
            "th",
            "tr",
            "vi",
            "zh",
            "zh-HK",
            "zh-TW",
        ]
    ]
    metadata: Optional[Dict[str, str]]
    mode: Literal["payment", "setup", "subscription"]
    object: Literal["checkout.session"]
    payment_intent: Optional[ExpandableField["PaymentIntent"]]
    payment_link: Optional[ExpandableField["PaymentLink"]]
    payment_method_collection: Optional[Literal["always", "if_required"]]
    payment_method_configuration_details: Optional[StripeObject]
    payment_method_options: Optional[StripeObject]
    payment_method_types: List[str]
    payment_status: Literal["no_payment_required", "paid", "unpaid"]
    phone_number_collection: Optional[StripeObject]
    recovered_from: Optional[str]
    setup_intent: Optional[ExpandableField["SetupIntent"]]
    shipping_address_collection: Optional[StripeObject]
    shipping_cost: Optional[StripeObject]
    shipping_details: Optional[StripeObject]
    shipping_options: List[StripeObject]
    status: Optional[Literal["complete", "expired", "open"]]
    submit_type: Optional[Literal["auto", "book", "donate", "pay"]]
    subscription: Optional[ExpandableField["Subscription"]]
    success_url: Optional[str]
    tax_id_collection: Optional[StripeObject]
    total_details: Optional[StripeObject]
    url: Optional[str]

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ) -> "Session":
        return cast(
            "Session",
            cls._static_request(
                "post",
                cls.class_url(),
                api_key,
                idempotency_key,
                stripe_version,
                stripe_account,
                params,
            ),
        )

    @classmethod
    def _cls_expire(
        cls,
        session: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
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
    def expire(self, idempotency_key: Optional[str] = None, **params: Any):
        return self._request(
            "post",
            "/v1/checkout/sessions/{session}/expire".format(
                session=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ) -> ListObject["Session"]:
        result = cls._static_request(
            "get",
            cls.class_url(),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )
        if not isinstance(result, ListObject):

            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

    @classmethod
    def _cls_list_line_items(
        cls,
        session: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
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
    def list_line_items(
        self, idempotency_key: Optional[str] = None, **params: Any
    ):
        return self._request(
            "get",
            "/v1/checkout/sessions/{session}/line_items".format(
                session=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def retrieve(
        cls, id: str, api_key: Optional[str] = None, **params: Any
    ) -> "Session":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance
