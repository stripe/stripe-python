# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import Dict, List
from typing_extensions import Literal, NotRequired, TypedDict


class RequestedSessionConfirmParams(RequestOptions):
    affiliate_attribution: NotRequired[
        "RequestedSessionConfirmParamsAffiliateAttribution"
    ]
    """
    Affiliate attribution data associated with this requested session.
    """
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


class RequestedSessionConfirmParamsAffiliateAttribution(TypedDict):
    campaign_id: NotRequired[str]
    """
    Agent-scoped campaign identifier.
    """
    creative_id: NotRequired[str]
    """
    Agent-scoped creative identifier.
    """
    expires_at: int
    """
    Timestamp when the attribution token expires.
    """
    identification_token: str
    """
    Agent-issued secret to validate the legitimacy of the source of this data.
    """
    issued_at: int
    """
    Timestamp for when the attribution token was issued.
    """
    provider: str
    """
    Identifier for the attribution agent / affiliate network namespace.
    """
    publisher_id: NotRequired[str]
    """
    Agent-scoped affiliate/publisher identifier.
    """
    shared_metadata: NotRequired[Dict[str, str]]
    """
    Freeform key/value pairs for additional non-sensitive per-agent data.
    """
    source: NotRequired[
        "RequestedSessionConfirmParamsAffiliateAttributionSource"
    ]
    """
    Context about where the attribution originated.
    """
    sub_id: NotRequired[str]
    """
    Agent-scoped sub-tracking identifier.
    """
    touchpoint: Literal["first", "last"]
    """
    Whether this is the first or last touchpoint.
    """


class RequestedSessionConfirmParamsAffiliateAttributionSource(TypedDict):
    platform: NotRequired[str]
    """
    The platform where the attribution originated.
    """
    type: Literal["platform", "url"]
    """
    The type of the attribution source.
    """
    url: NotRequired[str]
    """
    The URL where the attribution originated.
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
