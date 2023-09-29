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
    from stripe.api_resources.application import Application
    from stripe.api_resources.customer import Customer
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
    amount_remaining: Optional[int]
    amount_subtotal: int
    amount_total: int
    application: Optional[ExpandableField["Application"]]
    automatic_tax: Optional[StripeObject]
    billing_details: Optional[StripeObject]
    client_secret: Optional[str]
    created: int
    credits: Optional[List[StripeObject]]
    currency: str
    customer: Optional[ExpandableField["Customer"]]
    description: Optional[str]
    discounts: Optional[List[ExpandableField["Discount"]]]
    id: str
    ip_address: Optional[str]
    line_items: Optional[ListObject["LineItem"]]
    livemode: bool
    metadata: Optional[Dict[str, str]]
    object: Literal["order"]
    payment: StripeObject
    shipping_cost: Optional[StripeObject]
    shipping_details: Optional[StripeObject]
    status: Literal["canceled", "complete", "open", "processing", "submitted"]
    tax_details: Optional[StripeObject]
    total_details: StripeObject

    @classmethod
    def _cls_cancel(
        cls,
        id: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
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
    def cancel(self, idempotency_key: Optional[str] = None, **params: Any):
        return self._request(
            "post",
            "/v1/orders/{id}/cancel".format(
                id=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ) -> "Order":
        return cast(
            "Order",
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
    ) -> ListObject["Order"]:
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
        id: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
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
    def list_line_items(
        self, idempotency_key: Optional[str] = None, **params: Any
    ):
        return self._request(
            "get",
            "/v1/orders/{id}/line_items".format(
                id=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def modify(cls, id, **params: Any) -> "Order":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "Order",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def _cls_reopen(
        cls,
        id: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
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
    def reopen(self, idempotency_key: Optional[str] = None, **params: Any):
        return self._request(
            "post",
            "/v1/orders/{id}/reopen".format(
                id=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def retrieve(
        cls, id: str, api_key: Optional[str] = None, **params: Any
    ) -> "Order":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance

    @classmethod
    def _cls_submit(
        cls,
        id: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
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
    def submit(self, idempotency_key: Optional[str] = None, **params: Any):
        return self._request(
            "post",
            "/v1/orders/{id}/submit".format(
                id=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )
