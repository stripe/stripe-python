# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.stripe_object import StripeObject
from typing import Any, Dict, Optional, cast
from typing_extensions import Literal
from urllib.parse import quote_plus

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.tax_code import TaxCode


class ShippingRate(
    CreateableAPIResource["ShippingRate"],
    ListableAPIResource["ShippingRate"],
    UpdateableAPIResource["ShippingRate"],
):
    """
    Shipping rates describe the price of shipping presented to your customers and
    applied to a purchase. For more information, see [Charge for shipping](https://stripe.com/docs/payments/during-payment/charge-shipping).
    """

    OBJECT_NAME = "shipping_rate"
    active: bool
    created: int
    delivery_estimate: Optional[StripeObject]
    display_name: Optional[str]
    fixed_amount: Optional[StripeObject]
    id: str
    livemode: bool
    metadata: Dict[str, str]
    object: Literal["shipping_rate"]
    tax_behavior: Optional[Literal["exclusive", "inclusive", "unspecified"]]
    tax_code: Optional[ExpandableField["TaxCode"]]
    type: Literal["fixed_amount"]

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ) -> "ShippingRate":
        return cast(
            "ShippingRate",
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
    ) -> ListObject["ShippingRate"]:
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
    def modify(cls, id, **params: Any) -> "ShippingRate":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "ShippingRate",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, api_key: Optional[str] = None, **params: Any
    ) -> "ShippingRate":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance
