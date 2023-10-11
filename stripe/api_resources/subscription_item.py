# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
    nested_resource_class_methods,
)
from stripe.api_resources.list_object import ListObject
from stripe.stripe_object import StripeObject
from typing import Any, Dict, List, Optional, cast
from typing_extensions import Literal
from urllib.parse import quote_plus

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.plan import Plan
    from stripe.api_resources.price import Price
    from stripe.api_resources.tax_rate import TaxRate


@nested_resource_class_methods("usage_record")
@nested_resource_class_methods("usage_record_summary")
class SubscriptionItem(
    CreateableAPIResource["SubscriptionItem"],
    DeletableAPIResource["SubscriptionItem"],
    ListableAPIResource["SubscriptionItem"],
    UpdateableAPIResource["SubscriptionItem"],
):
    """
    Subscription items allow you to create customer subscriptions with more than
    one plan, making it easy to represent complex billing relationships.
    """

    OBJECT_NAME = "subscription_item"
    billing_thresholds: Optional[StripeObject]
    created: int
    id: str
    metadata: Dict[str, str]
    object: Literal["subscription_item"]
    plan: "Plan"
    price: "Price"
    quantity: Optional[int]
    subscription: str
    tax_rates: Optional[List["TaxRate"]]
    deleted: Optional[Literal[True]]

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ) -> "SubscriptionItem":
        return cast(
            "SubscriptionItem",
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
    def _cls_delete(cls, sid: str, **params: Any) -> "SubscriptionItem":
        url = "%s/%s" % (cls.class_url(), quote_plus(sid))
        return cast(
            "SubscriptionItem",
            cls._static_request("delete", url, params=params),
        )

    @util.class_method_variant("_cls_delete")
    def delete(self, **params: Any) -> "SubscriptionItem":
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
    ) -> ListObject["SubscriptionItem"]:
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
    def modify(cls, id, **params: Any) -> "SubscriptionItem":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "SubscriptionItem",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, api_key: Optional[str] = None, **params: Any
    ) -> "SubscriptionItem":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance

    @classmethod
    def create_usage_record(
        cls,
        subscription_item: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "post",
            "/v1/subscription_items/{subscription_item}/usage_records".format(
                subscription_item=util.sanitize_id(subscription_item)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def list_usage_record_summaries(
        cls,
        subscription_item: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "get",
            "/v1/subscription_items/{subscription_item}/usage_record_summaries".format(
                subscription_item=util.sanitize_id(subscription_item)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )
