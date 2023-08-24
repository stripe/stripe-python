# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing_extensions import Literal


class PaymentLink(
    CreateableAPIResource["PaymentLink"],
    ListableAPIResource["PaymentLink"],
    UpdateableAPIResource["PaymentLink"],
):
    """
    A payment link is a shareable URL that will take your customers to a hosted payment page. A payment link can be shared and used multiple times.

    When a customer opens a payment link it will open a new [checkout session](https://stripe.com/docs/api/checkout/sessions) to render the payment page. You can use [checkout session events](https://stripe.com/docs/api/events/types#event_types-checkout.session.completed) to track payments through payment links.

    Related guide: [Payment Links API](https://stripe.com/docs/payment-links)
    """

    OBJECT_NAME = "payment_link"
    active: bool
    after_completion: Any
    allow_promotion_codes: bool
    application_fee_amount: Optional[int]
    application_fee_percent: Optional[float]
    automatic_tax: Any
    billing_address_collection: str
    consent_collection: Optional[Any]
    currency: str
    custom_fields: List[Any]
    custom_text: Any
    customer_creation: str
    id: str
    invoice_creation: Optional[Any]
    line_items: Any
    livemode: bool
    metadata: Dict[str, str]
    object: Literal["payment_link"]
    on_behalf_of: Optional[Any]
    payment_intent_data: Optional[Any]
    payment_method_collection: str
    payment_method_types: Optional[List[str]]
    phone_number_collection: Any
    shipping_address_collection: Optional[Any]
    shipping_options: List[Any]
    submit_type: str
    subscription_data: Optional[Any]
    tax_id_collection: Any
    transfer_data: Optional[Any]
    url: str

    @classmethod
    def _cls_list_line_items(
        cls,
        payment_link,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "get",
            "/v1/payment_links/{payment_link}/line_items".format(
                payment_link=util.sanitize_id(payment_link)
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
            "/v1/payment_links/{payment_link}/line_items".format(
                payment_link=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )
