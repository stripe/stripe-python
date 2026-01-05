# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import Dict, List
from typing_extensions import Literal, NotRequired, TypedDict


class RequestedSessionUpdateParams(TypedDict):
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    fulfillment_details: NotRequired[
        "RequestedSessionUpdateParamsFulfillmentDetails"
    ]
    """
    The details of the fulfillment.
    """
    line_item_details: NotRequired[
        List["RequestedSessionUpdateParamsLineItemDetail"]
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
        "Literal['']|RequestedSessionUpdateParamsPaymentMethodData"
    ]
    """
    The payment method data for this requested session.
    """
    shared_metadata: NotRequired["Literal['']|Dict[str, str]"]
    """
    The shared metadata for this requested session.
    """


class RequestedSessionUpdateParamsFulfillmentDetails(TypedDict):
    address: NotRequired[
        "RequestedSessionUpdateParamsFulfillmentDetailsAddress"
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
        "RequestedSessionUpdateParamsFulfillmentDetailsSelectedFulfillmentOption"
    ]
    """
    The fulfillment option to select.
    """


class RequestedSessionUpdateParamsFulfillmentDetailsAddress(TypedDict):
    city: str
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
    postal_code: str
    """
    ZIP or postal code.
    """
    state: str
    """
    State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).
    """


class RequestedSessionUpdateParamsFulfillmentDetailsSelectedFulfillmentOption(
    TypedDict,
):
    shipping: "RequestedSessionUpdateParamsFulfillmentDetailsSelectedFulfillmentOptionShipping"
    """
    The shipping fulfillment option.
    """
    type: str
    """
    The type of fulfillment option.
    """


class RequestedSessionUpdateParamsFulfillmentDetailsSelectedFulfillmentOptionShipping(
    TypedDict,
):
    shipping_option: str
    """
    The shipping option identifer.
    """


class RequestedSessionUpdateParamsLineItemDetail(TypedDict):
    key: str
    """
    The key of the line item.
    """
    quantity: int
    """
    The quantity of the line item.
    """


class RequestedSessionUpdateParamsPaymentMethodData(TypedDict):
    billing_details: NotRequired[
        "RequestedSessionUpdateParamsPaymentMethodDataBillingDetails"
    ]
    """
    The billing details for the payment method data.
    """
    card: NotRequired["RequestedSessionUpdateParamsPaymentMethodDataCard"]
    """
    The card for the payment method data.
    """
    type: NotRequired[Literal["card"]]
    """
    The type of the payment method data.
    """


class RequestedSessionUpdateParamsPaymentMethodDataBillingDetails(TypedDict):
    address: NotRequired[
        "RequestedSessionUpdateParamsPaymentMethodDataBillingDetailsAddress"
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


class RequestedSessionUpdateParamsPaymentMethodDataBillingDetailsAddress(
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
    line1: str
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


class RequestedSessionUpdateParamsPaymentMethodDataCard(TypedDict):
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
