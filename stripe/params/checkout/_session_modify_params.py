# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import Dict, List
from typing_extensions import Literal, NotRequired, TypedDict


class SessionModifyParams(RequestOptions):
    automatic_tax: NotRequired["SessionModifyParamsAutomaticTax"]
    """
    Settings for automatic tax lookup for this session and resulting payments, invoices, and subscriptions.
    """
    collected_information: NotRequired[
        "SessionModifyParamsCollectedInformation"
    ]
    """
    Information about the customer collected within the Checkout Session. Can only be set when updating `embedded` or `custom` sessions.
    """
    discounts: NotRequired["Literal['']|List[SessionModifyParamsDiscount]"]
    """
    List of coupons and promotion codes attached to the Checkout Session.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    invoice_creation: NotRequired["SessionModifyParamsInvoiceCreation"]
    """
    Generate a post-purchase Invoice for one-time payments.
    """
    line_items: NotRequired[List["SessionModifyParamsLineItem"]]
    """
    A list of items the customer is purchasing.

    When updating line items, you must retransmit the entire array of line items.

    To retain an existing line item, specify its `id`.

    To update an existing line item, specify its `id` along with the new values of the fields to update.

    To add a new line item, specify one of `price` or `price_data` and `quantity`.

    To remove an existing line item, omit the line item's ID from the retransmitted array.

    To reorder a line item, specify it at the desired position in the retransmitted array.
    """
    metadata: NotRequired["Literal['']|Dict[str, str]"]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """
    shipping_options: NotRequired[
        "Literal['']|List[SessionModifyParamsShippingOption]"
    ]
    """
    The shipping rate options to apply to this Session. Up to a maximum of 5.
    """
    subscription_data: NotRequired["SessionModifyParamsSubscriptionData"]
    """
    A subset of parameters to be passed to subscription creation for Checkout Sessions in `subscription` mode.
    """


class SessionModifyParamsAutomaticTax(TypedDict):
    liability: NotRequired["SessionModifyParamsAutomaticTaxLiability"]
    """
    The account that's liable for tax. If set, the business address and tax registrations required to perform the tax calculation are loaded from this account. The tax transaction is returned in the report of the connected account.
    """


class SessionModifyParamsAutomaticTaxLiability(TypedDict):
    account: NotRequired[str]
    """
    The connected account being referenced when `type` is `account`.
    """
    type: Literal["account", "self"]
    """
    Type of the account referenced in the request.
    """


class SessionModifyParamsCollectedInformation(TypedDict):
    shipping_details: NotRequired[
        "SessionModifyParamsCollectedInformationShippingDetails"
    ]
    """
    The shipping details to apply to this Session.
    """


class SessionModifyParamsCollectedInformationShippingDetails(TypedDict):
    address: "SessionModifyParamsCollectedInformationShippingDetailsAddress"
    """
    The address of the customer
    """
    name: str
    """
    The name of customer
    """


class SessionModifyParamsCollectedInformationShippingDetailsAddress(TypedDict):
    city: NotRequired[str]
    """
    City, district, suburb, town, or village.
    """
    country: str
    """
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
    """
    line1: str
    """
    Address line 1, such as the street, PO Box, or company name.
    """
    line2: NotRequired[str]
    """
    Address line 2, such as the apartment, suite, unit, or building.
    """
    postal_code: NotRequired[str]
    """
    ZIP or postal code.
    """
    state: NotRequired[str]
    """
    State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).
    """


class SessionModifyParamsDiscount(TypedDict):
    coupon: NotRequired[str]
    """
    The ID of the [Coupon](https://docs.stripe.com/api/coupons) to apply to this Session. One of `coupon` or `coupon_data` is required when updating discounts.
    """
    coupon_data: NotRequired["SessionModifyParamsDiscountCouponData"]
    """
    Data used to generate a new [Coupon](https://docs.stripe.com/api/coupon) object inline. One of `coupon` or `coupon_data` is required when updating discounts.
    """


class SessionModifyParamsDiscountCouponData(TypedDict):
    amount_off: NotRequired[int]
    """
    A positive integer representing the amount to subtract from an invoice total (required if `percent_off` is not passed).
    """
    currency: NotRequired[str]
    """
    Three-letter [ISO code for the currency](https://stripe.com/docs/currencies) of the `amount_off` parameter (required if `amount_off` is passed).
    """
    duration: NotRequired[Literal["forever", "once", "repeating"]]
    """
    Specifies how long the discount will be in effect if used on a subscription. Defaults to `once`.
    """
    metadata: NotRequired["Literal['']|Dict[str, str]"]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """
    name: NotRequired[str]
    """
    Name of the coupon displayed to customers on, for instance invoices, or receipts. By default the `id` is shown if `name` is not set.
    """
    percent_off: NotRequired[float]
    """
    A positive float larger than 0, and smaller or equal to 100, that represents the discount the coupon will apply (required if `amount_off` is not passed).
    """


class SessionModifyParamsInvoiceCreation(TypedDict):
    invoice_data: NotRequired["SessionModifyParamsInvoiceCreationInvoiceData"]
    """
    Parameters passed when creating invoices for payment-mode Checkout Sessions.
    """


class SessionModifyParamsInvoiceCreationInvoiceData(TypedDict):
    issuer: NotRequired["SessionModifyParamsInvoiceCreationInvoiceDataIssuer"]
    """
    The connected account that issues the invoice. The invoice is presented with the branding and support information of the specified account.
    """


class SessionModifyParamsInvoiceCreationInvoiceDataIssuer(TypedDict):
    account: NotRequired[str]
    """
    The connected account being referenced when `type` is `account`.
    """
    type: Literal["account", "self"]
    """
    Type of the account referenced in the request.
    """


class SessionModifyParamsLineItem(TypedDict):
    adjustable_quantity: NotRequired[
        "SessionModifyParamsLineItemAdjustableQuantity"
    ]
    """
    When set, provides configuration for this item's quantity to be adjusted by the customer during Checkout.
    """
    id: NotRequired[str]
    """
    ID of an existing line item.
    """
    metadata: NotRequired["Literal['']|Dict[str, str]"]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """
    price: NotRequired[str]
    """
    The ID of the [Price](https://docs.stripe.com/api/prices). One of `price` or `price_data` is required when creating a new line item.
    """
    price_data: NotRequired["SessionModifyParamsLineItemPriceData"]
    """
    Data used to generate a new [Price](https://docs.stripe.com/api/prices) object inline. One of `price` or `price_data` is required when creating a new line item.
    """
    quantity: NotRequired[int]
    """
    The quantity of the line item being purchased. Quantity should not be defined when `recurring.usage_type=metered`.
    """
    tax_rates: NotRequired["Literal['']|List[str]"]
    """
    The [tax rates](https://docs.stripe.com/api/tax_rates) which apply to this line item.
    """


class SessionModifyParamsLineItemAdjustableQuantity(TypedDict):
    enabled: bool
    """
    Set to true if the quantity can be adjusted to any positive integer. Setting to false will remove any previously specified constraints on quantity.
    """
    maximum: NotRequired[int]
    """
    The maximum quantity the customer can purchase for the Checkout Session. By default this value is 99. You can specify a value up to 999999.
    """
    minimum: NotRequired[int]
    """
    The minimum quantity the customer must purchase for the Checkout Session. By default this value is 0.
    """


class SessionModifyParamsLineItemPriceData(TypedDict):
    currency: str
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    product: NotRequired[str]
    """
    The ID of the [Product](https://docs.stripe.com/api/products) that this [Price](https://docs.stripe.com/api/prices) will belong to. One of `product` or `product_data` is required.
    """
    product_data: NotRequired[
        "SessionModifyParamsLineItemPriceDataProductData"
    ]
    """
    Data used to generate a new [Product](https://docs.stripe.com/api/products) object inline. One of `product` or `product_data` is required.
    """
    recurring: NotRequired["SessionModifyParamsLineItemPriceDataRecurring"]
    """
    The recurring components of a price such as `interval` and `interval_count`.
    """
    tax_behavior: NotRequired[Literal["exclusive", "inclusive", "unspecified"]]
    """
    Only required if a [default tax behavior](https://docs.stripe.com/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
    """
    unit_amount: NotRequired[int]
    """
    A non-negative integer in cents (or local equivalent) representing how much to charge. One of `unit_amount` or `unit_amount_decimal` is required.
    """
    unit_amount_decimal: NotRequired[str]
    """
    Same as `unit_amount`, but accepts a decimal value in cents (or local equivalent) with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.
    """


class SessionModifyParamsLineItemPriceDataProductData(TypedDict):
    description: NotRequired[str]
    """
    The product's description, meant to be displayable to the customer. Use this field to optionally store a long form explanation of the product being sold for your own rendering purposes.
    """
    images: NotRequired[List[str]]
    """
    A list of up to 8 URLs of images for this product, meant to be displayable to the customer.
    """
    metadata: NotRequired[Dict[str, str]]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """
    name: str
    """
    The product's name, meant to be displayable to the customer.
    """
    tax_code: NotRequired[str]
    """
    A [tax code](https://docs.stripe.com/tax/tax-categories) ID.
    """
    unit_label: NotRequired[str]
    """
    A label that represents units of this product. When set, this will be included in customers' receipts, invoices, Checkout, and the customer portal.
    """
    tax_details: NotRequired[
        "SessionModifyParamsLineItemPriceDataProductDataTaxDetails"
    ]
    """
    Tax details for this product, including the [tax code](https://docs.stripe.com/tax/tax-codes) and an optional performance location.
    """


class SessionModifyParamsLineItemPriceDataProductDataTaxDetails(TypedDict):
    performance_location: NotRequired[str]
    """
    A tax location ID. Depending on the [tax code](https://docs.stripe.com/tax/tax-for-tickets/reference/tax-location-performance), this is required, optional, or not supported.
    """
    tax_code: str
    """
    A [tax code](https://docs.stripe.com/tax/tax-categories) ID.
    """


class SessionModifyParamsLineItemPriceDataRecurring(TypedDict):
    interval: Literal["day", "month", "week", "year"]
    """
    Specifies billing frequency. Either `day`, `week`, `month` or `year`.
    """
    interval_count: NotRequired[int]
    """
    The number of intervals between subscription billings. For example, `interval=month` and `interval_count=3` bills every 3 months. Maximum of three years interval allowed (3 years, 36 months, or 156 weeks).
    """


class SessionModifyParamsShippingOption(TypedDict):
    shipping_rate: NotRequired[str]
    """
    The ID of the Shipping Rate to use for this shipping option.
    """
    shipping_rate_data: NotRequired[
        "SessionModifyParamsShippingOptionShippingRateData"
    ]
    """
    Parameters to be passed to Shipping Rate creation for this shipping option.
    """


class SessionModifyParamsShippingOptionShippingRateData(TypedDict):
    delivery_estimate: NotRequired[
        "SessionModifyParamsShippingOptionShippingRateDataDeliveryEstimate"
    ]
    """
    The estimated range for how long shipping will take, meant to be displayable to the customer. This will appear on CheckoutSessions.
    """
    display_name: str
    """
    The name of the shipping rate, meant to be displayable to the customer. This will appear on CheckoutSessions.
    """
    fixed_amount: NotRequired[
        "SessionModifyParamsShippingOptionShippingRateDataFixedAmount"
    ]
    """
    Describes a fixed amount to charge for shipping. Must be present if type is `fixed_amount`.
    """
    metadata: NotRequired[Dict[str, str]]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """
    tax_behavior: NotRequired[Literal["exclusive", "inclusive", "unspecified"]]
    """
    Specifies whether the rate is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`.
    """
    tax_code: NotRequired[str]
    """
    A [tax code](https://docs.stripe.com/tax/tax-categories) ID. The Shipping tax code is `txcd_92010001`.
    """
    type: NotRequired[Literal["fixed_amount"]]
    """
    The type of calculation to use on the shipping rate.
    """


class SessionModifyParamsShippingOptionShippingRateDataDeliveryEstimate(
    TypedDict,
):
    maximum: NotRequired[
        "SessionModifyParamsShippingOptionShippingRateDataDeliveryEstimateMaximum"
    ]
    """
    The upper bound of the estimated range. If empty, represents no upper bound i.e., infinite.
    """
    minimum: NotRequired[
        "SessionModifyParamsShippingOptionShippingRateDataDeliveryEstimateMinimum"
    ]
    """
    The lower bound of the estimated range. If empty, represents no lower bound.
    """


class SessionModifyParamsShippingOptionShippingRateDataDeliveryEstimateMaximum(
    TypedDict,
):
    unit: Literal["business_day", "day", "hour", "month", "week"]
    """
    A unit of time.
    """
    value: int
    """
    Must be greater than 0.
    """


class SessionModifyParamsShippingOptionShippingRateDataDeliveryEstimateMinimum(
    TypedDict,
):
    unit: Literal["business_day", "day", "hour", "month", "week"]
    """
    A unit of time.
    """
    value: int
    """
    Must be greater than 0.
    """


class SessionModifyParamsShippingOptionShippingRateDataFixedAmount(TypedDict):
    amount: int
    """
    A non-negative integer in cents representing how much to charge.
    """
    currency: str
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    currency_options: NotRequired[
        Dict[
            str,
            "SessionModifyParamsShippingOptionShippingRateDataFixedAmountCurrencyOptions",
        ]
    ]
    """
    Shipping rates defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies).
    """


class SessionModifyParamsShippingOptionShippingRateDataFixedAmountCurrencyOptions(
    TypedDict,
):
    amount: int
    """
    A non-negative integer in cents representing how much to charge.
    """
    tax_behavior: NotRequired[Literal["exclusive", "inclusive", "unspecified"]]
    """
    Specifies whether the rate is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`.
    """


class SessionModifyParamsSubscriptionData(TypedDict):
    invoice_settings: NotRequired[
        "SessionModifyParamsSubscriptionDataInvoiceSettings"
    ]
    """
    All invoices will be billed using the specified settings.
    """
    trial_end: NotRequired[int]
    """
    Unix timestamp representing the end of the trial period the customer will get before being charged for the first time. Has to be at least 48 hours in the future.
    """
    trial_period_days: NotRequired["Literal['']|int"]
    """
    Integer representing the number of trial period days before the customer is charged for the first time. Has to be at least 1.
    """


class SessionModifyParamsSubscriptionDataInvoiceSettings(TypedDict):
    issuer: NotRequired[
        "SessionModifyParamsSubscriptionDataInvoiceSettingsIssuer"
    ]
    """
    The connected account that issues the invoice. The invoice is presented with the branding and support information of the specified account.
    """


class SessionModifyParamsSubscriptionDataInvoiceSettingsIssuer(TypedDict):
    account: NotRequired[str]
    """
    The connected account being referenced when `type` is `account`.
    """
    type: Literal["account", "self"]
    """
    Type of the account referenced in the request.
    """
