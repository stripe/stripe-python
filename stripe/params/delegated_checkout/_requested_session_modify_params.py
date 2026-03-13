# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import Dict, List
from typing_extensions import Literal, NotRequired, TypedDict


class RequestedSessionModifyParams(RequestOptions):
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    fulfillment_details: NotRequired[
        "RequestedSessionModifyParamsFulfillmentDetails"
    ]
    """
    The details of the fulfillment.
    """
    line_item_details: NotRequired[
        List["RequestedSessionModifyParamsLineItemDetail"]
    ]
    """
    The details of the line items.
    """
    metadata: NotRequired["Literal['']|Dict[str, str]"]
    """
    The metadata for this requested session.
    """
    payment_method: NotRequired[str]
    """
    The payment method for this requested session.
    """
    payment_method_data: NotRequired[
        "Literal['']|RequestedSessionModifyParamsPaymentMethodData"
    ]
    """
    The payment method data for this requested session.
    """
    shared_metadata: NotRequired["Literal['']|Dict[str, str]"]
    """
    The shared metadata for this requested session.
    """


class RequestedSessionModifyParamsFulfillmentDetails(TypedDict):
    address: NotRequired[
        "RequestedSessionModifyParamsFulfillmentDetailsAddress"
    ]
    """
    The customer's address.
    """
    email: NotRequired[str]
    """
    The customer's email address.
    """
    name: NotRequired[str]
    """
    The customer's name.
    """
    phone: NotRequired[str]
    """
    The customer's phone number.
    """
    selected_fulfillment_option: NotRequired[
        "RequestedSessionModifyParamsFulfillmentDetailsSelectedFulfillmentOption"
    ]
    """
    The fulfillment option to select.
    """
    selected_fulfillment_option_overrides: NotRequired[
        List[
            "RequestedSessionModifyParamsFulfillmentDetailsSelectedFulfillmentOptionOverride"
        ]
    ]
    """
    The fulfillment option overrides for specific line items.
    """


class RequestedSessionModifyParamsFulfillmentDetailsAddress(TypedDict):
    city: str
    """
    City, district, suburb, town, or village.
    """
    country: str
    """
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
    """
    line1: NotRequired[str]
    """
    Address line 1, such as the street, PO Box, or company name.
    """
    line2: NotRequired[str]
    """
    Address line 2, such as the apartment, suite, unit, or building.
    """
    postal_code: str
    """
    ZIP or postal code.
    """
    state: str
    """
    State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).
    """


class RequestedSessionModifyParamsFulfillmentDetailsSelectedFulfillmentOption(
    TypedDict,
):
    shipping: NotRequired[
        "RequestedSessionModifyParamsFulfillmentDetailsSelectedFulfillmentOptionShipping"
    ]
    """
    The shipping fulfillment option.
    """
    type: str
    """
    The type of fulfillment option.
    """
    digital: NotRequired[
        "RequestedSessionModifyParamsFulfillmentDetailsSelectedFulfillmentOptionDigital"
    ]
    """
    The digital fulfillment option.
    """


class RequestedSessionModifyParamsFulfillmentDetailsSelectedFulfillmentOptionShipping(
    TypedDict,
):
    shipping_option: str
    """
    The shipping option identifier.
    """


class RequestedSessionModifyParamsFulfillmentDetailsSelectedFulfillmentOptionDigital(
    TypedDict,
):
    digital_option: str
    """
    The digital option identifier.
    """


class RequestedSessionModifyParamsFulfillmentDetailsSelectedFulfillmentOptionOverride(
    TypedDict,
):
    digital: NotRequired[
        "RequestedSessionModifyParamsFulfillmentDetailsSelectedFulfillmentOptionOverrideDigital"
    ]
    """
    The digital fulfillment option.
    """
    line_item_keys: List[str]
    """
    The line item keys that this fulfillment option override applies to.
    """
    shipping: NotRequired[
        "RequestedSessionModifyParamsFulfillmentDetailsSelectedFulfillmentOptionOverrideShipping"
    ]
    """
    The shipping fulfillment option.
    """
    type: str
    """
    The type of fulfillment option.
    """


class RequestedSessionModifyParamsFulfillmentDetailsSelectedFulfillmentOptionOverrideDigital(
    TypedDict,
):
    digital_option: str
    """
    The digital option identifier.
    """


class RequestedSessionModifyParamsFulfillmentDetailsSelectedFulfillmentOptionOverrideShipping(
    TypedDict,
):
    shipping_option: str
    """
    The shipping option identifier.
    """


class RequestedSessionModifyParamsLineItemDetail(TypedDict):
    key: str
    """
    The key of the line item.
    """
    quantity: int
    """
    The quantity of the line item.
    """


class RequestedSessionModifyParamsPaymentMethodData(TypedDict):
    billing_details: NotRequired[
        "RequestedSessionModifyParamsPaymentMethodDataBillingDetails"
    ]
    """
    The billing details for the payment method data.
    """
    card: NotRequired["RequestedSessionModifyParamsPaymentMethodDataCard"]
    """
    The card for the payment method data.
    """
    type: NotRequired[Literal["card"]]
    """
    The type of the payment method data.
    """


class RequestedSessionModifyParamsPaymentMethodDataBillingDetails(TypedDict):
    address: NotRequired[
        "RequestedSessionModifyParamsPaymentMethodDataBillingDetailsAddress"
    ]
    """
    The address for the billing details.
    """
    email: NotRequired[str]
    """
    The email for the billing details.
    """
    name: NotRequired[str]
    """
    The name for the billing details.
    """
    phone: NotRequired[str]
    """
    The phone for the billing details.
    """


class RequestedSessionModifyParamsPaymentMethodDataBillingDetailsAddress(
    TypedDict,
):
    city: str
    """
    City, district, suburb, town, or village.
    """
    country: str
    """
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
    """
    line1: NotRequired[str]
    """
    Address line 1, such as the street, PO Box, or company name.
    """
    line2: NotRequired[str]
    """
    Address line 2, such as the apartment, suite, unit, or building.
    """
    postal_code: str
    """
    ZIP or postal code.
    """
    state: str
    """
    State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).
    """


class RequestedSessionModifyParamsPaymentMethodDataCard(TypedDict):
    cvc: NotRequired[str]
    """
    The CVC of the card.
    """
    exp_month: int
    """
    The expiration month of the card.
    """
    exp_year: int
    """
    The expiration year of the card.
    """
    number: str
    """
    The number of the card.
    """
