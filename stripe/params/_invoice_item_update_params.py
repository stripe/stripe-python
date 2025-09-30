# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import Dict, List
from typing_extensions import Literal, NotRequired, TypedDict


class InvoiceItemUpdateParams(TypedDict):
    amount: NotRequired[int]
    """
    The integer amount in cents (or local equivalent) of the charge to be applied to the upcoming invoice. If you want to apply a credit to the customer's account, pass a negative amount.
    """
    description: NotRequired[str]
    """
    An arbitrary string which you can attach to the invoice item. The description is displayed in the invoice for easy tracking.
    """
    discountable: NotRequired[bool]
    """
    Controls whether discounts apply to this invoice item. Defaults to false for prorations or negative invoice items, and true for all other invoice items. Cannot be set to true for prorations.
    """
    discounts: NotRequired["Literal['']|List[InvoiceItemUpdateParamsDiscount]"]
    """
    The coupons, promotion codes & existing discounts which apply to the invoice item or invoice line item. Item discounts are applied before invoice discounts. Pass an empty string to remove previously-defined discounts.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    margins: NotRequired["Literal['']|List[str]"]
    """
    The ids of the margins to apply to the invoice item. When set, the `default_margins` on the invoice do not apply to this invoice item.
    """
    metadata: NotRequired["Literal['']|Dict[str, str]"]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """
    period: NotRequired["InvoiceItemUpdateParamsPeriod"]
    """
    The period associated with this invoice item. When set to different values, the period will be rendered on the invoice. If you have [Stripe Revenue Recognition](https://stripe.com/docs/revenue-recognition) enabled, the period will be used to recognize and defer revenue. See the [Revenue Recognition documentation](https://stripe.com/docs/revenue-recognition/methodology/subscriptions-and-invoicing) for details.
    """
    price_data: NotRequired["InvoiceItemUpdateParamsPriceData"]
    """
    Data used to generate a new [Price](https://stripe.com/docs/api/prices) object inline.
    """
    pricing: NotRequired["InvoiceItemUpdateParamsPricing"]
    """
    The pricing information for the invoice item.
    """
    quantity: NotRequired[int]
    """
    Non-negative integer. The quantity of units for the invoice item.
    """
    tax_behavior: NotRequired[Literal["exclusive", "inclusive", "unspecified"]]
    """
    Only required if a [default tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
    """
    tax_code: NotRequired["Literal['']|str"]
    """
    A [tax code](https://stripe.com/docs/tax/tax-categories) ID.
    """
    tax_rates: NotRequired["Literal['']|List[str]"]
    """
    The tax rates which apply to the invoice item. When set, the `default_tax_rates` on the invoice do not apply to this invoice item. Pass an empty string to remove previously-defined tax rates.
    """
    unit_amount_decimal: NotRequired[str]
    """
    The decimal unit amount in cents (or local equivalent) of the charge to be applied to the upcoming invoice. This `unit_amount_decimal` will be multiplied by the quantity to get the full amount. Passing in a negative `unit_amount_decimal` will reduce the `amount_due` on the invoice. Accepts at most 12 decimal places.
    """


class InvoiceItemUpdateParamsDiscount(TypedDict):
    coupon: NotRequired[str]
    """
    ID of the coupon to create a new discount for.
    """
    discount: NotRequired[str]
    """
    ID of an existing discount on the object (or one of its ancestors) to reuse.
    """
    discount_end: NotRequired["InvoiceItemUpdateParamsDiscountDiscountEnd"]
    """
    Details to determine how long the discount should be applied for.
    """
    promotion_code: NotRequired[str]
    """
    ID of the promotion code to create a new discount for.
    """


class InvoiceItemUpdateParamsDiscountDiscountEnd(TypedDict):
    duration: NotRequired["InvoiceItemUpdateParamsDiscountDiscountEndDuration"]
    """
    Time span for the redeemed discount.
    """
    timestamp: NotRequired[int]
    """
    A precise Unix timestamp for the discount to end. Must be in the future.
    """
    type: Literal["duration", "timestamp"]
    """
    The type of calculation made to determine when the discount ends.
    """


class InvoiceItemUpdateParamsDiscountDiscountEndDuration(TypedDict):
    interval: Literal["day", "month", "week", "year"]
    """
    Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
    """
    interval_count: int
    """
    The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
    """


class InvoiceItemUpdateParamsPeriod(TypedDict):
    end: int
    """
    The end of the period, which must be greater than or equal to the start. This value is inclusive.
    """
    start: int
    """
    The start of the period. This value is inclusive.
    """


class InvoiceItemUpdateParamsPriceData(TypedDict):
    currency: str
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    product: str
    """
    The ID of the [Product](https://docs.stripe.com/api/products) that this [Price](https://docs.stripe.com/api/prices) will belong to.
    """
    tax_behavior: NotRequired[Literal["exclusive", "inclusive", "unspecified"]]
    """
    Only required if a [default tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
    """
    unit_amount: NotRequired[int]
    """
    A positive integer in cents (or local equivalent) (or 0 for a free price) representing how much to charge.
    """
    unit_amount_decimal: NotRequired[str]
    """
    Same as `unit_amount`, but accepts a decimal value in cents (or local equivalent) with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.
    """


class InvoiceItemUpdateParamsPricing(TypedDict):
    price: NotRequired[str]
    """
    The ID of the price object.
    """
