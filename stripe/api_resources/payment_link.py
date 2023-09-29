# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.stripe_object import StripeObject
from typing import Any, Dict, List, Optional, cast
from typing_extensions import Literal
from urllib.parse import quote_plus

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.account import Account
    from stripe.api_resources.application import Application
    from stripe.api_resources.line_item import LineItem


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
    application: Optional[ExpandableField["Application"]]
    application_fee_amount: Optional[int]
    application_fee_percent: Optional[float]
    automatic_tax: StripeObject
    billing_address_collection: Literal["auto", "required"]
    consent_collection: Optional[StripeObject]
    currency: str
    custom_fields: List[StripeObject]
    custom_text: StripeObject
    customer_creation: Literal["always", "if_required"]
    id: str
    invoice_creation: Optional[StripeObject]
    line_items: Optional[ListObject["LineItem"]]
    livemode: bool
    metadata: Dict[str, str]
    object: Literal["payment_link"]
    on_behalf_of: Optional[ExpandableField["Account"]]
    payment_intent_data: Optional[StripeObject]
    payment_method_collection: Literal["always", "if_required"]
    payment_method_types: Optional[
        List[
            Literal[
                "affirm",
                "afterpay_clearpay",
                "alipay",
                "au_becs_debit",
                "bacs_debit",
                "bancontact",
                "blik",
                "boleto",
                "card",
                "cashapp",
                "eps",
                "fpx",
                "giropay",
                "grabpay",
                "ideal",
                "klarna",
                "konbini",
                "link",
                "oxxo",
                "p24",
                "paynow",
                "paypal",
                "pix",
                "promptpay",
                "sepa_debit",
                "sofort",
                "us_bank_account",
                "wechat_pay",
            ]
        ]
    ]
    phone_number_collection: StripeObject
    shipping_address_collection: Optional[StripeObject]
    shipping_options: List[StripeObject]
    submit_type: Literal["auto", "book", "donate", "pay"]
    subscription_data: Optional[StripeObject]
    tax_id_collection: StripeObject
    transfer_data: Optional[StripeObject]
    url: str

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ) -> "PaymentLink":
        return cast(
            "PaymentLink",
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
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ) -> ListObject["PaymentLink"]:
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
        payment_link: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
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
    def list_line_items(
        self, idempotency_key: Optional[str] = None, **params: Any
    ):
        return self._request(
            "get",
            "/v1/payment_links/{payment_link}/line_items".format(
                payment_link=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def modify(cls, id, **params: Any) -> "PaymentLink":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "PaymentLink",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, api_key: Optional[str] = None, **params: Any
    ) -> "PaymentLink":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance
