# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    DeletableAPIResource,
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
    from stripe.api_resources.product import Product


class Plan(
    CreateableAPIResource["Plan"],
    DeletableAPIResource["Plan"],
    ListableAPIResource["Plan"],
    UpdateableAPIResource["Plan"],
):
    """
    You can now model subscriptions more flexibly using the [Prices API](https://stripe.com/docs/api#prices). It replaces the Plans API and is backwards compatible to simplify your migration.

    Plans define the base price, currency, and billing cycle for recurring purchases of products.
    [Products](https://stripe.com/docs/api#products) help you track inventory or provisioning, and plans help you track pricing. Different physical goods or levels of service should be represented by products, and pricing options should be represented by plans. This approach lets you change prices without having to change your provisioning scheme.

    For example, you might have a single "gold" product that has plans for $10/month, $100/year, €9/month, and €90/year.

    Related guides: [Set up a subscription](https://stripe.com/docs/billing/subscriptions/set-up-subscription) and more about [products and prices](https://stripe.com/docs/products-prices/overview).
    """

    OBJECT_NAME = "plan"
    active: bool
    aggregate_usage: Optional[
        Literal["last_during_period", "last_ever", "max", "sum"]
    ]
    amount: Optional[int]
    amount_decimal: Optional[float]
    billing_scheme: Literal["per_unit", "tiered"]
    created: int
    currency: str
    id: str
    interval: Literal["day", "month", "week", "year"]
    interval_count: int
    livemode: bool
    metadata: Optional[Dict[str, str]]
    nickname: Optional[str]
    object: Literal["plan"]
    product: Optional[ExpandableField["Product"]]
    tiers: Optional[List[StripeObject]]
    tiers_mode: Optional[Literal["graduated", "volume"]]
    transform_usage: Optional[StripeObject]
    trial_period_days: Optional[int]
    usage_type: Literal["licensed", "metered"]
    deleted: Optional[Literal[True]]

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ) -> "Plan":
        return cast(
            "Plan",
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
    def _cls_delete(cls, sid: str, **params: Any) -> "Plan":
        url = "%s/%s" % (cls.class_url(), quote_plus(sid))
        return cast(
            "Plan",
            cls._static_request("delete", url, params=params),
        )

    @util.class_method_variant("_cls_delete")
    def delete(self, **params: Any) -> "Plan":
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
    ) -> ListObject["Plan"]:
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
    def modify(cls, id, **params: Any) -> "Plan":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "Plan",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, api_key: Optional[str] = None, **params: Any
    ) -> "Plan":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance
