# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import Dict, List
from typing_extensions import Literal, NotRequired, TypedDict


class LicenseFeeCreateParams(TypedDict):
    currency: str
    """
    Three-letter ISO currency code, in lowercase. Must be a supported currency.
    """
    display_name: str
    """
    A customer-facing name for the License Fee.
    This name is used in Stripe-hosted products like the Customer Portal and Checkout. It does not show up on Invoices.
    Maximum length of 250 characters.
    """
    licensed_item: str
    """
    The Licensed Item that this License Fee binds to.
    """
    lookup_key: NotRequired[str]
    """
    An internal key you can use to search for a particular license fee. Maximum length of 200 characters.
    """
    metadata: NotRequired[Dict[str, str]]
    """
    Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    service_interval: Literal["day", "month", "week", "year"]
    """
    The interval for assessing service. For example, a monthly license fee with a rate of $1 for the first 10 "workloads"
    and $2 thereafter means "$1 per workload up to 10 workloads during a month of service." This is similar to but
    distinct from billing interval; the service interval deals with the rate at which the customer accumulates fees,
    while the billing interval in Cadence deals with the rate the customer is billed.
    """
    service_interval_count: int
    """
    The length of the interval for assessing service. For example, set this to 3 and `service_interval` to `"month"` in
    order to specify quarterly service.
    """
    tax_behavior: Literal["exclusive", "inclusive"]
    """
    The Stripe Tax tax behavior - whether the license fee is inclusive or exclusive of tax.
    """
    tiering_mode: NotRequired[Literal["graduated", "volume"]]
    """
    Defines whether the tiered price should be graduated or volume-based. In volume-based tiering, the maximum
    quantity within a period determines the per-unit price. In graduated tiering, the pricing changes as the quantity
    grows into new tiers. Can only be set if `tiers` is set.
    """
    tiers: NotRequired[List["LicenseFeeCreateParamsTier"]]
    """
    Each element represents a pricing tier. Cannot be set if `unit_amount` is provided.
    """
    transform_quantity: NotRequired["LicenseFeeCreateParamsTransformQuantity"]
    """
    Apply a transformation to the reported usage or set quantity before computing the amount billed.
    """
    unit_amount: NotRequired[str]
    """
    The per-unit amount to be charged, represented as a decimal string in minor currency units with at most 12 decimal
    places. Cannot be set if `tiers` is provided.
    """


class LicenseFeeCreateParamsTier(TypedDict):
    flat_amount: NotRequired[str]
    """
    Price for the entire tier, represented as a decimal string in minor currency units with at most 12 decimal places.
    """
    unit_amount: NotRequired[str]
    """
    Per-unit price for units included in this tier, represented as a decimal string in minor currency units with at
    most 12 decimal places.
    """
    up_to_decimal: NotRequired[str]
    """
    Up to and including this quantity will be contained in the tier. Only one of `up_to_decimal` and `up_to_inf` may
    be set.
    """
    up_to_inf: NotRequired[Literal["inf"]]
    """
    No upper bound to this tier. Only one of `up_to_decimal` and `up_to_inf` may be set.
    """


class LicenseFeeCreateParamsTransformQuantity(TypedDict):
    divide_by: int
    """
    Divide usage by this number.
    """
    round: Literal["down", "up"]
    """
    After division, round the result up or down.
    """
