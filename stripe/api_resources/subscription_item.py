# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
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
from typing import Dict, List, Optional, cast
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)
from urllib.parse import quote_plus

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
    if TYPE_CHECKING:

        class CreateParams(RequestOptions):
            billing_thresholds: NotRequired[
                "Literal['']|SubscriptionItem.CreateParamsBillingThresholds|None"
            ]
            expand: NotRequired["List[str]|None"]
            metadata: NotRequired["Dict[str, str]|None"]
            payment_behavior: NotRequired[
                "Literal['allow_incomplete', 'default_incomplete', 'error_if_incomplete', 'pending_if_incomplete']|None"
            ]
            plan: NotRequired["str|None"]
            price: NotRequired["str|None"]
            price_data: NotRequired[
                "SubscriptionItem.CreateParamsPriceData|None"
            ]
            proration_behavior: NotRequired[
                "Literal['always_invoice', 'create_prorations', 'none']|None"
            ]
            proration_date: NotRequired["int|None"]
            quantity: NotRequired["int|None"]
            subscription: str
            tax_rates: NotRequired["Literal['']|List[str]|None"]

        class CreateParamsPriceData(TypedDict):
            currency: str
            product: str
            recurring: "SubscriptionItem.CreateParamsPriceDataRecurring"
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            unit_amount: NotRequired["int|None"]
            unit_amount_decimal: NotRequired["float|None"]

        class CreateParamsPriceDataRecurring(TypedDict):
            interval: Literal["day", "month", "week", "year"]
            interval_count: NotRequired["int|None"]

        class CreateParamsBillingThresholds(TypedDict):
            usage_gte: int

        class DeleteParams(RequestOptions):
            clear_usage: NotRequired["bool|None"]
            proration_behavior: NotRequired[
                "Literal['always_invoice', 'create_prorations', 'none']|None"
            ]
            proration_date: NotRequired["int|None"]

        class ListParams(RequestOptions):
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            starting_after: NotRequired["str|None"]
            subscription: str

        class ModifyParams(RequestOptions):
            billing_thresholds: NotRequired[
                "Literal['']|SubscriptionItem.ModifyParamsBillingThresholds|None"
            ]
            expand: NotRequired["List[str]|None"]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            off_session: NotRequired["bool|None"]
            payment_behavior: NotRequired[
                "Literal['allow_incomplete', 'default_incomplete', 'error_if_incomplete', 'pending_if_incomplete']|None"
            ]
            plan: NotRequired["str|None"]
            price: NotRequired["str|None"]
            price_data: NotRequired[
                "SubscriptionItem.ModifyParamsPriceData|None"
            ]
            proration_behavior: NotRequired[
                "Literal['always_invoice', 'create_prorations', 'none']|None"
            ]
            proration_date: NotRequired["int|None"]
            quantity: NotRequired["int|None"]
            tax_rates: NotRequired["Literal['']|List[str]|None"]

        class ModifyParamsPriceData(TypedDict):
            currency: str
            product: str
            recurring: "SubscriptionItem.ModifyParamsPriceDataRecurring"
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            unit_amount: NotRequired["int|None"]
            unit_amount_decimal: NotRequired["float|None"]

        class ModifyParamsPriceDataRecurring(TypedDict):
            interval: Literal["day", "month", "week", "year"]
            interval_count: NotRequired["int|None"]

        class ModifyParamsBillingThresholds(TypedDict):
            usage_gte: int

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

        class CreateUsageRecordParams(RequestOptions):
            action: NotRequired["Literal['increment', 'set']|None"]
            expand: NotRequired["List[str]|None"]
            quantity: int
            timestamp: NotRequired["Literal['now']|int|None"]

        class ListUsageRecordSummariesParams(RequestOptions):
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            starting_after: NotRequired["str|None"]

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
