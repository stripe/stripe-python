# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import util
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import Dict, List, Optional, Union, cast
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)
from urllib.parse import quote_plus

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
    if TYPE_CHECKING:

        class CreateParams(RequestOptions):
            active: NotRequired["bool|None"]
            aggregate_usage: NotRequired[
                "Literal['last_during_period', 'last_ever', 'max', 'sum']|None"
            ]
            amount: NotRequired["int|None"]
            amount_decimal: NotRequired["float|None"]
            billing_scheme: NotRequired["Literal['per_unit', 'tiered']|None"]
            currency: str
            expand: NotRequired["List[str]|None"]
            id: NotRequired["str|None"]
            interval: Literal["day", "month", "week", "year"]
            interval_count: NotRequired["int|None"]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            nickname: NotRequired["str|None"]
            product: NotRequired["Plan.CreateParamsProduct|str|None"]
            tiers: NotRequired["List[Plan.CreateParamsTier]|None"]
            tiers_mode: NotRequired["Literal['graduated', 'volume']|None"]
            transform_usage: NotRequired[
                "Plan.CreateParamsTransformUsage|None"
            ]
            trial_period_days: NotRequired["int|None"]
            usage_type: NotRequired["Literal['licensed', 'metered']|None"]

        class CreateParamsTransformUsage(TypedDict):
            divide_by: int
            round: Literal["down", "up"]

        class CreateParamsTier(TypedDict):
            flat_amount: NotRequired["int|None"]
            flat_amount_decimal: NotRequired["float|None"]
            unit_amount: NotRequired["int|None"]
            unit_amount_decimal: NotRequired["float|None"]
            up_to: Union[Literal["inf"], int]

        class CreateParamsProduct(TypedDict):
            active: NotRequired["bool|None"]
            id: NotRequired["str|None"]
            metadata: NotRequired["Dict[str, str]|None"]
            name: str
            statement_descriptor: NotRequired["str|None"]
            tax_code: NotRequired["str|None"]
            unit_label: NotRequired["str|None"]

        class DeleteParams(RequestOptions):
            pass

        class ListParams(RequestOptions):
            active: NotRequired["bool|None"]
            created: NotRequired["Plan.ListParamsCreated|int|None"]
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            product: NotRequired["str|None"]
            starting_after: NotRequired["str|None"]

        class ListParamsCreated(TypedDict):
            gt: NotRequired["int|None"]
            gte: NotRequired["int|None"]
            lt: NotRequired["int|None"]
            lte: NotRequired["int|None"]

        class ModifyParams(RequestOptions):
            active: NotRequired["bool|None"]
            expand: NotRequired["List[str]|None"]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            nickname: NotRequired["str|None"]
            product: NotRequired["str|None"]
            trial_period_days: NotRequired["int|None"]

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

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
        **params: Unpack["Plan.CreateParams"]
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
    def _cls_delete(
        cls, sid: str, **params: Unpack["Plan.DeleteParams"]
    ) -> "Plan":
        url = "%s/%s" % (cls.class_url(), quote_plus(sid))
        return cast(
            "Plan",
            cls._static_request("delete", url, params=params),
        )

    @util.class_method_variant("_cls_delete")
    def delete(self, **params: Unpack["Plan.DeleteParams"]) -> "Plan":
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
        **params: Unpack["Plan.ListParams"]
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
    def modify(cls, id, **params: Unpack["Plan.ModifyParams"]) -> "Plan":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "Plan",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["Plan.RetrieveParams"]
    ) -> "Plan":
        instance = cls(id, **params)
        instance.refresh()
        return instance
