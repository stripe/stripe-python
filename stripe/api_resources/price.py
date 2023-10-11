# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
    SearchableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.api_resources.search_result_object import SearchResultObject
from stripe.stripe_object import StripeObject
from typing import Any, Dict, List, Optional, cast
from typing_extensions import Literal
from urllib.parse import quote_plus

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.product import Product


class Price(
    CreateableAPIResource["Price"],
    ListableAPIResource["Price"],
    SearchableAPIResource["Price"],
    UpdateableAPIResource["Price"],
):
    """
    Prices define the unit cost, currency, and (optional) billing cycle for both recurring and one-time purchases of products.
    [Products](https://stripe.com/docs/api#products) help you track inventory or provisioning, and prices help you track payment terms. Different physical goods or levels of service should be represented by products, and pricing options should be represented by prices. This approach lets you change prices without having to change your provisioning scheme.

    For example, you might have a single "gold" product that has prices for $10/month, $100/year, and €9 once.

    Related guides: [Set up a subscription](https://stripe.com/docs/billing/subscriptions/set-up-subscription), [create an invoice](https://stripe.com/docs/billing/invoices/create), and more about [products and prices](https://stripe.com/docs/products-prices/overview).
    """

    OBJECT_NAME = "price"

    class CurrencyOptions(StripeObject):
        class CustomUnitAmount(StripeObject):
            maximum: Optional[int]
            minimum: Optional[int]
            preset: Optional[int]

        class Tier(StripeObject):
            flat_amount: Optional[int]
            flat_amount_decimal: Optional[float]
            unit_amount: Optional[int]
            unit_amount_decimal: Optional[float]
            up_to: Optional[int]

        custom_unit_amount: Optional[CustomUnitAmount]
        tax_behavior: Optional[
            Literal["exclusive", "inclusive", "unspecified"]
        ]
        tiers: Optional[List[Tier]]
        unit_amount: Optional[int]
        unit_amount_decimal: Optional[float]
        _inner_class_types = {
            "custom_unit_amount": CustomUnitAmount,
            "tiers": Tier,
        }

    class CustomUnitAmount(StripeObject):
        maximum: Optional[int]
        minimum: Optional[int]
        preset: Optional[int]

    class MigrateTo(StripeObject):
        behavior: Literal["at_cycle_end"]
        effective_after: int
        price: str

    class Recurring(StripeObject):
        aggregate_usage: Optional[
            Literal["last_during_period", "last_ever", "max", "sum"]
        ]
        interval: Literal["day", "month", "week", "year"]
        interval_count: int
        trial_period_days: Optional[int]
        usage_type: Literal["licensed", "metered"]

    class Tier(StripeObject):
        flat_amount: Optional[int]
        flat_amount_decimal: Optional[float]
        unit_amount: Optional[int]
        unit_amount_decimal: Optional[float]
        up_to: Optional[int]

    class TransformQuantity(StripeObject):
        divide_by: int
        round: Literal["down", "up"]

    active: bool
    billing_scheme: Literal["per_unit", "tiered"]
    created: int
    currency: str
    currency_options: Optional[Dict[str, CurrencyOptions]]
    custom_unit_amount: Optional[CustomUnitAmount]
    id: str
    livemode: bool
    lookup_key: Optional[str]
    metadata: Dict[str, str]
    migrate_to: Optional[MigrateTo]
    nickname: Optional[str]
    object: Literal["price"]
    product: ExpandableField["Product"]
    recurring: Optional[Recurring]
    tax_behavior: Optional[Literal["exclusive", "inclusive", "unspecified"]]
    tiers: Optional[List[Tier]]
    tiers_mode: Optional[Literal["graduated", "volume"]]
    transform_quantity: Optional[TransformQuantity]
    type: Literal["one_time", "recurring"]
    unit_amount: Optional[int]
    unit_amount_decimal: Optional[float]
    deleted: Optional[Literal[True]]

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ) -> "Price":
        return cast(
            "Price",
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
    ) -> ListObject["Price"]:
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
    def modify(cls, id, **params: Any) -> "Price":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "Price",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, api_key: Optional[str] = None, **params: Any
    ) -> "Price":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance

    @classmethod
    def search(cls, *args, **kwargs) -> SearchResultObject["Price"]:
        return cls._search(search_url="/v1/prices/search", *args, **kwargs)

    @classmethod
    def search_auto_paging_iter(cls, *args, **kwargs):
        return cls.search(*args, **kwargs).auto_paging_iter()

    _inner_class_types = {
        "currency_options": CurrencyOptions,
        "custom_unit_amount": CustomUnitAmount,
        "migrate_to": MigrateTo,
        "recurring": Recurring,
        "tiers": Tier,
        "transform_quantity": TransformQuantity,
    }
