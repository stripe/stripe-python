# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import Dict, List
from typing_extensions import Literal, NotRequired, TypedDict


class RequestedSessionCreateParams(RequestOptions):
    currency: str
    """
    The currency for this requested session.
    """
    customer: NotRequired[str]
    """
    The customer for this requested session.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    fulfillment_details: NotRequired[
        "RequestedSessionCreateParamsFulfillmentDetails"
    ]
    """
    The details of the fulfillment.
    """
    line_item_details: List["RequestedSessionCreateParamsLineItemDetail"]
    """
    The details of the line items.
    """
    metadata: NotRequired[Dict[str, str]]
    """
    The metadata for this requested session.
    """
    payment_method: NotRequired[str]
    """
    The payment method for this requested session.
    """
    payment_method_data: NotRequired[
        "RequestedSessionCreateParamsPaymentMethodData"
    ]
    """
    The payment method data for this requested session.
    """
    seller_details: "RequestedSessionCreateParamsSellerDetails"
    """
    The details of the seller.
    """
    setup_future_usage: NotRequired[Literal["on_session"]]
    """
    The setup future usage for this requested session.
    """
    shared_metadata: NotRequired[Dict[str, str]]
    """
    The shared metadata for this requested session.
    """


class RequestedSessionCreateParamsFulfillmentDetails(TypedDict):
    address: NotRequired[
        "RequestedSessionCreateParamsFulfillmentDetailsAddress"
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


class RequestedSessionCreateParamsFulfillmentDetailsAddress(TypedDict):
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


class RequestedSessionCreateParamsLineItemDetail(TypedDict):
    quantity: int
    """
    The quantity of the line item.
    """
    sku_id: str
    """
    The SKU ID of the line item.
    """


class RequestedSessionCreateParamsPaymentMethodData(TypedDict):
    billing_details: NotRequired[
        "RequestedSessionCreateParamsPaymentMethodDataBillingDetails"
    ]
    """
    The billing details for the payment method data.
    """
    card: NotRequired["RequestedSessionCreateParamsPaymentMethodDataCard"]
    """
    The card for the payment method data.
    """
    type: NotRequired[Literal["card"]]
    """
    The type of the payment method data.
    """


class RequestedSessionCreateParamsPaymentMethodDataBillingDetails(TypedDict):
    address: NotRequired[
        "RequestedSessionCreateParamsPaymentMethodDataBillingDetailsAddress"
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


class RequestedSessionCreateParamsPaymentMethodDataBillingDetailsAddress(
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


class RequestedSessionCreateParamsPaymentMethodDataCard(TypedDict):
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


class RequestedSessionCreateParamsSellerDetails(TypedDict):
    network_profile: str
    """
    The network profile for the seller.
    """
