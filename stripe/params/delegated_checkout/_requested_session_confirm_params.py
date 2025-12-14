# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import List
from typing_extensions import Literal, NotRequired, TypedDict


class RequestedSessionConfirmParams(RequestOptions):
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    payment_method: NotRequired[str]
    """
    The PaymentMethod to use with the requested session.
    """
    payment_method_data: NotRequired[
        "RequestedSessionConfirmParamsPaymentMethodData"
    ]
    """
    The payment method data for this requested session.
    """
    risk_details: NotRequired["RequestedSessionConfirmParamsRiskDetails"]
    """
    Risk details/signals associated with the requested session
    """


class RequestedSessionConfirmParamsPaymentMethodData(TypedDict):
    billing_details: NotRequired[
        "RequestedSessionConfirmParamsPaymentMethodDataBillingDetails"
    ]
    """
    The billing details for the payment method data.
    """
    card: NotRequired["RequestedSessionConfirmParamsPaymentMethodDataCard"]
    """
    The card for the payment method data.
    """
    type: NotRequired[Literal["card"]]
    """
    The type of the payment method data.
    """


class RequestedSessionConfirmParamsPaymentMethodDataBillingDetails(TypedDict):
    address: NotRequired[
        "RequestedSessionConfirmParamsPaymentMethodDataBillingDetailsAddress"
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


class RequestedSessionConfirmParamsPaymentMethodDataBillingDetailsAddress(
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


class RequestedSessionConfirmParamsPaymentMethodDataCard(TypedDict):
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


class RequestedSessionConfirmParamsRiskDetails(TypedDict):
    client_device_metadata_details: NotRequired[
        "RequestedSessionConfirmParamsRiskDetailsClientDeviceMetadataDetails"
    ]
    """
    The client device metadata details for this requested session.
    """


class RequestedSessionConfirmParamsRiskDetailsClientDeviceMetadataDetails(
    TypedDict,
):
    radar_session: NotRequired[str]
    """
    The radar session.
    """
    referrer: NotRequired[str]
    """
    The referrer of the client device.
    """
    remote_ip: NotRequired[str]
    """
    The remote IP address of the client device.
    """
    time_on_page_ms: NotRequired[int]
    """
    The time on page in milliseconds.
    """
    user_agent: NotRequired[str]
    """
    The user agent of the client device.
    """
