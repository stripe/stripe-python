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
    from stripe.api_resources.application import Application
    from stripe.api_resources.discount import Discount
    from stripe.api_resources.line_item import LineItem


class Order(
    CreateableAPIResource["Order"],
    ListableAPIResource["Order"],
    UpdateableAPIResource["Order"],
):
    """
    An Order describes a purchase being made by a customer, including the
    products & quantities being purchased, the order status, the payment information,
    and the billing/shipping details.

    Related guide: [Orders overview](https://stripe.com/docs/orders)
    """

    OBJECT_NAME = "order"
    amount_remaining: int
    amount_subtotal: int
    amount_total: int
    application: Optional[ExpandableField["Application"]]
    automatic_tax: StripeObject
    billing_details: Optional[StripeObject]
    client_secret: Optional[str]
    created: str
    credits: List[StripeObject]
    currency: str
    customer: Optional[ExpandableField[Any]]
    description: Optional[str]
    discounts: Optional[List[ExpandableField["Discount"]]]
    id: str
    ip_address: Optional[str]
    line_items: ListObject["LineItem"]
    livemode: bool
    metadata: Optional[Dict[str, str]]
    object: Literal["order"]
    payment: StripeObject
    shipping_cost: Optional[StripeObject]
    shipping_details: Optional[StripeObject]
    status: str
    tax_details: StripeObject
    total_details: StripeObject

    @classmethod
    def _cls_cancel(
        cls,
        id,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "post",
            "/v1/orders/{id}/cancel".format(id=util.sanitize_id(id)),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_cancel")
    def cancel(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/orders/{id}/cancel".format(
                id=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def _cls_list_line_items(
        cls,
        id,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "get",
            "/v1/orders/{id}/line_items".format(id=util.sanitize_id(id)),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_list_line_items")
    def list_line_items(self, idempotency_key=None, **params):
        return self._request(
            "get",
            "/v1/orders/{id}/line_items".format(
                id=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def _cls_reopen(
        cls,
        id,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "post",
            "/v1/orders/{id}/reopen".format(id=util.sanitize_id(id)),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_reopen")
    def reopen(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/orders/{id}/reopen".format(
                id=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def _cls_submit(
        cls,
        id,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "post",
            "/v1/orders/{id}/submit".format(id=util.sanitize_id(id)),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_submit")
    def submit(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/orders/{id}/submit".format(
                id=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )
