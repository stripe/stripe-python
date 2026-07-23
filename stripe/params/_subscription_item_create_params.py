# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from decimal import Decimal
from stripe._request_options import RequestOptions
from stripe._stripe_object import UntypedStripeObject
from typing import Dict, List, Union
from typing_extensions import Literal, NotRequired, TypedDict


class SubscriptionItemCreateParams(RequestOptions):
    billing_thresholds: NotRequired[
        "Literal['']|SubscriptionItemCreateParamsBillingThresholds"
    ]
    """
    Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period. Pass an empty string to remove previously-defined thresholds.
    """
    current_trial: NotRequired["SubscriptionItemCreateParamsCurrentTrial"]
    """
    The trial offer to apply to this subscription item.
    """
    discounts: NotRequired[
        "Literal['']|List[SubscriptionItemCreateParamsDiscount]"
    ]
    """
    The coupons to redeem into discounts for the subscription item.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    metadata: NotRequired["Dict[str, str]|UntypedStripeObject[str]"]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """
    payment_behavior: NotRequired[
        Literal[
            "allow_incomplete",
            "default_incomplete",
            "error_if_incomplete",
            "pending_if_incomplete",
        ]
    ]
    """
    Controls how Stripe handles payment when a subscription update requires payment and `collection_method=charge_automatically`.
    """
    plan: NotRequired[str]
    """
    The identifier of the plan to add to the subscription.
    """
    price: NotRequired[str]
    """
    The ID of the price object.
    """
    price_data: NotRequired["SubscriptionItemCreateParamsPriceData"]
    """
    Data used to generate a new [Price](https://docs.stripe.com/api/prices) object inline.
    """
    proration_behavior: NotRequired[
        "Literal['always_invoice', 'create_prorations', 'none']|str"
    ]
    """
    Determines how to handle [prorations](https://docs.stripe.com/billing/subscriptions/prorations) when the billing cycle changes (e.g., when switching plans, resetting `billing_cycle_anchor=now`, or starting a trial), or if an item's `quantity` changes. The default value is `create_prorations`.
    """
    proration_date: NotRequired[int]
    """
    If set, the proration will be calculated as though the subscription was updated at the given time. This can be used to apply the same proration that was previewed with the [upcoming invoice](https://docs.stripe.com/api/invoices/create_preview) endpoint.
    """
    quantity: NotRequired[int]
    """
    The quantity you'd like to apply to the subscription item you're creating.
    """
    subscription: str
    """
    The identifier of the subscription to modify.
    """
    tax_rates: NotRequired["Literal['']|List[str]"]
    """
    A list of [Tax Rate](https://docs.stripe.com/api/tax_rates) ids. These Tax Rates will override the [`default_tax_rates`](https://docs.stripe.com/api/subscriptions/create#create_subscription-default_tax_rates) on the Subscription. When updating, pass an empty string to remove previously-defined tax rates.
    """
    trial: NotRequired["SubscriptionItemCreateParamsTrial"]
    """
    Options that configure the trial on the subscription item.
    """


class SubscriptionItemCreateParamsBillingThresholds(TypedDict):
    usage_gte: int
    """
    Number of units that meets the billing threshold to advance the subscription to a new billing period (e.g., it takes 10 $5 units to meet a $50 [monetary threshold](https://docs.stripe.com/api/subscriptions/update#update_subscription-billing_thresholds-amount_gte))
    """


class SubscriptionItemCreateParamsCurrentTrial(TypedDict):
    trial_end: NotRequired[int]
    """
    Unix timestamp representing the end of the trial offer period. Required when the trial offer has `duration.type=timestamp`. Cannot be specified when `duration.type=relative`.
    """
    trial_offer: str
    """
    The ID of the trial offer to apply to the subscription item.
    """


class SubscriptionItemCreateParamsDiscount(TypedDict):
    coupon: NotRequired[str]
    """
    ID of the coupon to create a new discount for.
    """
    discount: NotRequired[str]
    """
    ID of an existing discount on the object (or one of its ancestors) to reuse.
    """
    discount_end: NotRequired[
        "SubscriptionItemCreateParamsDiscountDiscountEnd"
    ]
    """
    Details to determine how long the discount should be applied for.
    """
    promotion_code: NotRequired[str]
    """
    ID of the promotion code to create a new discount for.
    """
    settings: NotRequired["SubscriptionItemCreateParamsDiscountSettings"]
    """
    Settings for discount application including service period anchoring.
    """


class SubscriptionItemCreateParamsDiscountDiscountEnd(TypedDict):
    duration: NotRequired[
        "SubscriptionItemCreateParamsDiscountDiscountEndDuration"
    ]
    """
    Time span for the redeemed discount.
    """
    timestamp: NotRequired[int]
    """
    A precise Unix timestamp for the discount to end. Must be in the future.
    """
    type: Union[Literal["duration", "timestamp"], str]
    """
    The type of calculation made to determine when the discount ends.
    """


class SubscriptionItemCreateParamsDiscountDiscountEndDuration(TypedDict):
    interval: Union[Literal["day", "month", "week", "year"], str]
    """
    Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
    """
    interval_count: int
    """
    The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
    """


class SubscriptionItemCreateParamsDiscountSettings(TypedDict):
    service_period_anchor_config: NotRequired[
        "SubscriptionItemCreateParamsDiscountSettingsServicePeriodAnchorConfig"
    ]
    """
    Configures service period cycle anchoring.
    """
    start_date: NotRequired[
        "Literal['current_period_end', 'current_period_start', 'now']|str"
    ]
    """
    The start date of the discount's service period when applying a coupon or promotion code with a service period duration. Defaults to `now` if omitted.
    """


class SubscriptionItemCreateParamsDiscountSettingsServicePeriodAnchorConfig(
    TypedDict,
):
    custom: NotRequired[
        "SubscriptionItemCreateParamsDiscountSettingsServicePeriodAnchorConfigCustom"
    ]
    """
    Anchor the service period to a custom date. Type must be `custom` to specify.
    """
    type: NotRequired[
        "Literal['custom', 'subscription_service_cycle_anchor']|str"
    ]
    """
    The type of service period anchor config. Defaults to `subscription_service_cycle_anchor` if omitted.
    """


class SubscriptionItemCreateParamsDiscountSettingsServicePeriodAnchorConfigCustom(
    TypedDict,
):
    day_of_month: int
    """
    The day of the month the anchor should be. Ranges from 1 to 31.
    """
    hour: NotRequired[int]
    """
    The hour of the day the anchor should be. Ranges from 0 to 23.
    """
    minute: NotRequired[int]
    """
    The minute of the hour the anchor should be. Ranges from 0 to 59.
    """
    month: NotRequired[int]
    """
    The month to start full cycle periods. Ranges from 1 to 12.
    """
    second: NotRequired[int]
    """
    The second of the minute the anchor should be. Ranges from 0 to 59.
    """


class SubscriptionItemCreateParamsPriceData(TypedDict):
    currency: str
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    product: str
    """
    The ID of the [Product](https://docs.stripe.com/api/products) that this [Price](https://docs.stripe.com/api/prices) will belong to.
    """
    recurring: "SubscriptionItemCreateParamsPriceDataRecurring"
    """
    The recurring components of a price such as `interval` and `interval_count`.
    """
    tax_behavior: NotRequired[Literal["exclusive", "inclusive", "unspecified"]]
    """
    Only required if a [default tax behavior](https://docs.stripe.com/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
    """
    unit_amount: NotRequired[int]
    """
    A positive integer in cents (or local equivalent) (or 0 for a free price) representing how much to charge.
    """
    unit_amount_decimal: NotRequired[Decimal]
    """
    Same as `unit_amount`, but accepts a decimal value in cents (or local equivalent) with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.
    """


class SubscriptionItemCreateParamsPriceDataRecurring(TypedDict):
    interval: Literal["day", "month", "week", "year"]
    """
    Specifies billing frequency. Either `day`, `week`, `month` or `year`.
    """
    interval_count: NotRequired[int]
    """
    The number of intervals between subscription billings. For example, `interval=month` and `interval_count=3` bills every 3 months. Maximum of three years interval allowed (3 years, 36 months, or 156 weeks).
    """


class SubscriptionItemCreateParamsTrial(TypedDict):
    converts_to: NotRequired[List[str]]
    """
    List of price IDs which, if present on the subscription following a paid trial, constitute opting-in to the paid trial. Currently only supports at most 1 price ID.
    """
    type: Union[Literal["free", "paid"], str]
    """
    Determines the type of trial for this item.
    """
