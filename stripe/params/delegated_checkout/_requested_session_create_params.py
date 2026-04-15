# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_object import UntypedStripeObject
from typing import Dict, List
from typing_extensions import Literal, NotRequired, TypedDict


class RequestedSessionCreateParams(RequestOptions):
    affiliate_attribution: NotRequired[
        "RequestedSessionCreateParamsAffiliateAttribution"
    ]
    """
    Affiliate attribution data associated with this requested session.
    """
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
    metadata: NotRequired["Dict[str, str]|UntypedStripeObject[str]"]
    """
    The metadata for this requested session.
    """
    payment_method: NotRequired[str]
    """
    The payment method for this requested session.
    """
    payment_method_options: NotRequired[
        "RequestedSessionCreateParamsPaymentMethodOptions"
    ]
    """
    The payment method options for this requested session.
    """
    seller_details: "RequestedSessionCreateParamsSellerDetails"
    """
    The details of the seller.
    """
    setup_future_usage: NotRequired[Literal["on_session"]]
    """
    The setup future usage for this requested session.
    """
    shared_metadata: NotRequired["Dict[str, str]|UntypedStripeObject[str]"]
    """
    The shared metadata for this requested session.
    """


class RequestedSessionCreateParamsAffiliateAttribution(TypedDict):
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
    shared_metadata: NotRequired["Dict[str, str]|UntypedStripeObject[str]"]
    """
    Freeform key/value pairs for additional non-sensitive per-agent data.
    """
    source: NotRequired[
        "RequestedSessionCreateParamsAffiliateAttributionSource"
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


class RequestedSessionCreateParamsAffiliateAttributionSource(TypedDict):
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


class RequestedSessionCreateParamsLineItemDetail(TypedDict):
    quantity: int
    """
    The quantity of the line item.
    """
    sku_id: str
    """
    The SKU ID of the line item.
    """


class RequestedSessionCreateParamsPaymentMethodOptions(TypedDict):
    card: NotRequired["RequestedSessionCreateParamsPaymentMethodOptionsCard"]
    """
    Card-specific payment method options.
    """
    excluded_payment_method_types: NotRequired[
        List[Literal["affirm", "card", "klarna"]]
    ]
    """
    The payment method types to exclude from the session.
    """


class RequestedSessionCreateParamsPaymentMethodOptionsCard(TypedDict):
    brands_blocked: NotRequired[
        List[Literal["american_express", "mastercard", "visa"]]
    ]
    """
    The card brands to exclude from the session.
    """


class RequestedSessionCreateParamsSellerDetails(TypedDict):
    network_profile: str
    """
    The network profile for the seller.
    """
