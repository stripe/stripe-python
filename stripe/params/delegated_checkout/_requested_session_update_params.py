# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import UntypedStripeObject
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
    metadata: NotRequired[
        "Literal['']|Dict[str, str]|UntypedStripeObject[str]"
    ]
    """
    The metadata for this requested session.
    """
    payment_method: NotRequired[str]
    """
    The payment method for this requested session.
    """
    payment_method_options: NotRequired[
        "RequestedSessionUpdateParamsPaymentMethodOptions"
    ]
    """
    The payment method options for this requested session.
    """
    shared_metadata: NotRequired[
        "Literal['']|Dict[str, str]|UntypedStripeObject[str]"
    ]
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
    selected_fulfillment_option_overrides: NotRequired[
        List[
            "RequestedSessionUpdateParamsFulfillmentDetailsSelectedFulfillmentOptionOverride"
        ]
    ]
    """
    The fulfillment option overrides for specific line items.
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


class RequestedSessionUpdateParamsFulfillmentDetailsSelectedFulfillmentOption(
    TypedDict,
):
    digital: NotRequired[
        "RequestedSessionUpdateParamsFulfillmentDetailsSelectedFulfillmentOptionDigital"
    ]
    """
    The digital fulfillment option.
    """
    shipping: NotRequired[
        "RequestedSessionUpdateParamsFulfillmentDetailsSelectedFulfillmentOptionShipping"
    ]
    """
    The shipping fulfillment option.
    """
    type: str
    """
    The type of fulfillment option.
    """


class RequestedSessionUpdateParamsFulfillmentDetailsSelectedFulfillmentOptionDigital(
    TypedDict,
):
    digital_option: str
    """
    The digital option identifier.
    """


class RequestedSessionUpdateParamsFulfillmentDetailsSelectedFulfillmentOptionShipping(
    TypedDict,
):
    shipping_option: str
    """
    The shipping option identifier.
    """


class RequestedSessionUpdateParamsFulfillmentDetailsSelectedFulfillmentOptionOverride(
    TypedDict,
):
    digital: NotRequired[
        "RequestedSessionUpdateParamsFulfillmentDetailsSelectedFulfillmentOptionOverrideDigital"
    ]
    """
    The digital fulfillment option.
    """
    line_item_keys: List[str]
    """
    The line item keys that this fulfillment option override applies to.
    """
    shipping: NotRequired[
        "RequestedSessionUpdateParamsFulfillmentDetailsSelectedFulfillmentOptionOverrideShipping"
    ]
    """
    The shipping fulfillment option.
    """
    type: str
    """
    The type of fulfillment option.
    """


class RequestedSessionUpdateParamsFulfillmentDetailsSelectedFulfillmentOptionOverrideDigital(
    TypedDict,
):
    digital_option: str
    """
    The digital option identifier.
    """


class RequestedSessionUpdateParamsFulfillmentDetailsSelectedFulfillmentOptionOverrideShipping(
    TypedDict,
):
    shipping_option: str
    """
    The shipping option identifier.
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


class RequestedSessionUpdateParamsPaymentMethodOptions(TypedDict):
    card: NotRequired["RequestedSessionUpdateParamsPaymentMethodOptionsCard"]
    """
    Card-specific payment method options.
    """
    excluded_payment_method_types: NotRequired[
        List[Literal["affirm", "card", "klarna"]]
    ]
    """
    The payment method types to exclude from the session.
    """


class RequestedSessionUpdateParamsPaymentMethodOptionsCard(TypedDict):
    brands_blocked: NotRequired[
        List[Literal["american_express", "mastercard", "visa"]]
    ]
    """
    The card brands to exclude from the session.
    """
