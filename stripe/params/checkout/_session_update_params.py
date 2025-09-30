# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import Dict, List
from typing_extensions import Literal, NotRequired, TypedDict


class SessionUpdateParams(TypedDict):
    collected_information: NotRequired[
        "SessionUpdateParamsCollectedInformation"
    ]
    """
    Information about the customer collected within the Checkout Session. Can only be set when updating `embedded` or `custom` sessions.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    metadata: NotRequired["Literal['']|Dict[str, str]"]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """
    shipping_options: NotRequired[
        "Literal['']|List[SessionUpdateParamsShippingOption]"
    ]
    """
    The shipping rate options to apply to this Session. Up to a maximum of 5.
    """


class SessionUpdateParamsCollectedInformation(TypedDict):
    shipping_details: NotRequired[
        "SessionUpdateParamsCollectedInformationShippingDetails"
    ]
    """
    The shipping details to apply to this Session.
    """


class SessionUpdateParamsCollectedInformationShippingDetails(TypedDict):
    address: "SessionUpdateParamsCollectedInformationShippingDetailsAddress"
    """
    The address of the customer
    """
    name: str
    """
    The name of customer
    """


class SessionUpdateParamsCollectedInformationShippingDetailsAddress(TypedDict):
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
    State, county, province, or region.
    """


class SessionUpdateParamsShippingOption(TypedDict):
    shipping_rate: NotRequired[str]
    """
    The ID of the Shipping Rate to use for this shipping option.
    """
    shipping_rate_data: NotRequired[
        "SessionUpdateParamsShippingOptionShippingRateData"
    ]
    """
    Parameters to be passed to Shipping Rate creation for this shipping option.
    """


class SessionUpdateParamsShippingOptionShippingRateData(TypedDict):
    delivery_estimate: NotRequired[
        "SessionUpdateParamsShippingOptionShippingRateDataDeliveryEstimate"
    ]
    """
    The estimated range for how long shipping will take, meant to be displayable to the customer. This will appear on CheckoutSessions.
    """
    display_name: str
    """
    The name of the shipping rate, meant to be displayable to the customer. This will appear on CheckoutSessions.
    """
    fixed_amount: NotRequired[
        "SessionUpdateParamsShippingOptionShippingRateDataFixedAmount"
    ]
    """
    Describes a fixed amount to charge for shipping. Must be present if type is `fixed_amount`.
    """
    metadata: NotRequired[Dict[str, str]]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """
    tax_behavior: NotRequired[Literal["exclusive", "inclusive", "unspecified"]]
    """
    Specifies whether the rate is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`.
    """
    tax_code: NotRequired[str]
    """
    A [tax code](https://stripe.com/docs/tax/tax-categories) ID. The Shipping tax code is `txcd_92010001`.
    """
    type: NotRequired[Literal["fixed_amount"]]
    """
    The type of calculation to use on the shipping rate.
    """


class SessionUpdateParamsShippingOptionShippingRateDataDeliveryEstimate(
    TypedDict,
):
    maximum: NotRequired[
        "SessionUpdateParamsShippingOptionShippingRateDataDeliveryEstimateMaximum"
    ]
    """
    The upper bound of the estimated range. If empty, represents no upper bound i.e., infinite.
    """
    minimum: NotRequired[
        "SessionUpdateParamsShippingOptionShippingRateDataDeliveryEstimateMinimum"
    ]
    """
    The lower bound of the estimated range. If empty, represents no lower bound.
    """


class SessionUpdateParamsShippingOptionShippingRateDataDeliveryEstimateMaximum(
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


class SessionUpdateParamsShippingOptionShippingRateDataDeliveryEstimateMinimum(
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


class SessionUpdateParamsShippingOptionShippingRateDataFixedAmount(TypedDict):
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
            "SessionUpdateParamsShippingOptionShippingRateDataFixedAmountCurrencyOptions",
        ]
    ]
    """
    Shipping rates defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies).
    """


class SessionUpdateParamsShippingOptionShippingRateDataFixedAmountCurrencyOptions(
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
