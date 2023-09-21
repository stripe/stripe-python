# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    SearchableAPIResource,
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
    from stripe.api_resources.price import Price
    from stripe.api_resources.tax_code import TaxCode


class Product(
    CreateableAPIResource["Product"],
    DeletableAPIResource["Product"],
    ListableAPIResource["Product"],
    SearchableAPIResource["Product"],
    UpdateableAPIResource["Product"],
):
    """
    Products describe the specific goods or services you offer to your customers.
    For example, you might offer a Standard and Premium version of your goods or service; each version would be a separate Product.
    They can be used in conjunction with [Prices](https://stripe.com/docs/api#prices) to configure pricing in Payment Links, Checkout, and Subscriptions.

    Related guides: [Set up a subscription](https://stripe.com/docs/billing/subscriptions/set-up-subscription),
    [share a Payment Link](https://stripe.com/docs/payment-links),
    [accept payments with Checkout](https://stripe.com/docs/payments/accept-a-payment#create-product-prices-upfront),
    and more about [Products and Prices](https://stripe.com/docs/products-prices/overview)
    """

    OBJECT_NAME = "product"
    active: bool
    created: int
    default_price: Optional[ExpandableField["Price"]]
    description: Optional[str]
    features: List[StripeObject]
    id: str
    images: List[str]
    livemode: bool
    metadata: Dict[str, str]
    name: str
    object: Literal["product"]
    package_dimensions: Optional[StripeObject]
    shippable: Optional[bool]
    statement_descriptor: Optional[str]
    tax_code: Optional[ExpandableField["TaxCode"]]
    type: Literal["good", "service"]
    unit_label: Optional[str]
    updated: int
    url: Optional[str]
    deleted: Optional[Literal[True]]

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ) -> "Product":
        return cast(
            "Product",
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
    def _cls_delete(cls, sid: str, **params: Any) -> "Product":
        url = "%s/%s" % (cls.class_url(), quote_plus(sid))
        return cast(
            "Product",
            cls._static_request("delete", url, params=params),
        )

    @util.class_method_variant("_cls_delete")
    def delete(self, **params: Any) -> "Product":
        return self._request_and_refresh(
            "delete",
            self.instance_url(),
            params=params,
        )

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ) -> ListObject["Product"]:
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
    def modify(cls, id, **params: Any) -> "Product":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "Product",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, api_key: Optional[str] = None, **params: Any
    ) -> "Product":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance

    @classmethod
    def search(cls, *args, **kwargs) -> Any:
        return cls._search(search_url="/v1/products/search", *args, **kwargs)

    @classmethod
    def search_auto_paging_iter(cls, *args, **kwargs) -> Any:
        return cls.search(*args, **kwargs).auto_paging_iter()
