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
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import Dict, List, Optional, Union, cast
from typing_extensions import Literal, NotRequired, TypedDict, Unpack
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

    class CreateParams(RequestOptions):
        billing_thresholds: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "SubscriptionItem.CreateBillingThresholdsParams",
                ]
            ]
        ]
        expand: NotRequired[Optional[List[str]]]
        metadata: NotRequired[Optional[Dict[str, str]]]
        payment_behavior: NotRequired[
            Optional[
                Literal[
                    "allow_incomplete",
                    "default_incomplete",
                    "error_if_incomplete",
                    "pending_if_incomplete",
                ]
            ]
        ]
        plan: NotRequired[Optional[str]]
        price: NotRequired[Optional[str]]
        price_data: NotRequired[
            Optional["SubscriptionItem.CreatePriceDataParams"]
        ]
        proration_behavior: NotRequired[
            Optional[Literal["always_invoice", "create_prorations", "none"]]
        ]
        proration_date: NotRequired[Optional[int]]
        quantity: NotRequired[Optional[int]]
        subscription: str
        tax_rates: NotRequired[Optional[Union[Literal[""], List[str]]]]

    class CreatePriceDataParams(TypedDict):
        currency: str
        product: str
        recurring: "SubscriptionItem.CreatePriceDataRecurringParams"
        tax_behavior: NotRequired[
            Optional[Literal["exclusive", "inclusive", "unspecified"]]
        ]
        unit_amount: NotRequired[Optional[int]]
        unit_amount_decimal: NotRequired[Optional[float]]

    class CreatePriceDataRecurringParams(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        interval_count: NotRequired[Optional[int]]

    class CreateBillingThresholdsParams(TypedDict):
        usage_gte: int

    class DeleteParams(RequestOptions):
        clear_usage: NotRequired[Optional[bool]]
        proration_behavior: NotRequired[
            Optional[Literal["always_invoice", "create_prorations", "none"]]
        ]
        proration_date: NotRequired[Optional[int]]

    class ListParams(RequestOptions):
        ending_before: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        limit: NotRequired[Optional[int]]
        starting_after: NotRequired[Optional[str]]
        subscription: str

    class ModifyParams(RequestOptions):
        billing_thresholds: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "SubscriptionItem.ModifyBillingThresholdsParams",
                ]
            ]
        ]
        expand: NotRequired[Optional[List[str]]]
        metadata: NotRequired[Optional[Union[Literal[""], Dict[str, str]]]]
        off_session: NotRequired[Optional[bool]]
        payment_behavior: NotRequired[
            Optional[
                Literal[
                    "allow_incomplete",
                    "default_incomplete",
                    "error_if_incomplete",
                    "pending_if_incomplete",
                ]
            ]
        ]
        plan: NotRequired[Optional[str]]
        price: NotRequired[Optional[str]]
        price_data: NotRequired[
            Optional["SubscriptionItem.ModifyPriceDataParams"]
        ]
        proration_behavior: NotRequired[
            Optional[Literal["always_invoice", "create_prorations", "none"]]
        ]
        proration_date: NotRequired[Optional[int]]
        quantity: NotRequired[Optional[int]]
        tax_rates: NotRequired[Optional[Union[Literal[""], List[str]]]]

    class ModifyPriceDataParams(TypedDict):
        currency: str
        product: str
        recurring: "SubscriptionItem.ModifyPriceDataRecurringParams"
        tax_behavior: NotRequired[
            Optional[Literal["exclusive", "inclusive", "unspecified"]]
        ]
        unit_amount: NotRequired[Optional[int]]
        unit_amount_decimal: NotRequired[Optional[float]]

    class ModifyPriceDataRecurringParams(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        interval_count: NotRequired[Optional[int]]

    class ModifyBillingThresholdsParams(TypedDict):
        usage_gte: int

    class RetrieveParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    class CreateUsageRecordParams(RequestOptions):
        action: NotRequired[Optional[Literal["increment", "set"]]]
        expand: NotRequired[Optional[List[str]]]
        quantity: int
        timestamp: NotRequired[Optional[Union[Literal["now"], int]]]

    class ListUsageRecordSummariesParams(RequestOptions):
        ending_before: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        limit: NotRequired[Optional[int]]
        starting_after: NotRequired[Optional[str]]

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
        **params: Unpack["SubscriptionItem.CreateParams"]
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
    def _cls_delete(
        cls, sid: str, **params: Unpack["SubscriptionItem.DeleteParams"]
    ) -> "SubscriptionItem":
        url = "%s/%s" % (cls.class_url(), quote_plus(sid))
        return cast(
            "SubscriptionItem",
            cls._static_request("delete", url, params=params),
        )

    @util.class_method_variant("_cls_delete")
    def delete(
        self, **params: Unpack["SubscriptionItem.DeleteParams"]
    ) -> "SubscriptionItem":
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
        **params: Unpack["SubscriptionItem.ListParams"]
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
    def modify(
        cls, id, **params: Unpack["SubscriptionItem.ModifyParams"]
    ) -> "SubscriptionItem":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "SubscriptionItem",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["SubscriptionItem.RetrieveParams"]
    ) -> "SubscriptionItem":
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    def create_usage_record(
        cls,
        subscription_item: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["SubscriptionItem.CreateUsageRecordParams"]
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
        **params: Unpack["SubscriptionItem.ListUsageRecordSummariesParams"]
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
