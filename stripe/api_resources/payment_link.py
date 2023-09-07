# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.stripe_object import StripeObject
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing_extensions import Literal

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.line_item import LineItem
    from stripe.api_resources.account import Account


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
    after_completion: StripeObject
    allow_promotion_codes: bool
    application: Optional[ExpandableField[Any]]
    application_fee_amount: Optional[int]
    application_fee_percent: Optional[float]
    automatic_tax: StripeObject
    billing_address_collection: str
    consent_collection: Optional[StripeObject]
    currency: str
    custom_fields: List[StripeObject]
    custom_text: StripeObject
    customer_creation: str
    id: str
    invoice_creation: Optional[StripeObject]
    line_items: ListObject["LineItem"]
    livemode: bool
    metadata: Dict[str, str]
    object: Literal["payment_link"]
    on_behalf_of: Optional[ExpandableField["Account"]]
    payment_intent_data: Optional[StripeObject]
    payment_method_collection: str
    payment_method_types: Optional[List[str]]
    phone_number_collection: StripeObject
    shipping_address_collection: Optional[StripeObject]
    shipping_options: List[StripeObject]
    submit_type: str
    subscription_data: Optional[StripeObject]
    tax_id_collection: StripeObject
    transfer_data: Optional[StripeObject]
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
