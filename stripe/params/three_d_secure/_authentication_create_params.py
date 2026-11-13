# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_object import UntypedStripeObject
from typing import Dict, List, Union
from typing_extensions import Literal, NotRequired, TypedDict


class AuthenticationCreateParams(RequestOptions):
    acquirer_details: NotRequired["AuthenticationCreateParamsAcquirerDetails"]
    """
    Contains additional details about the acquirer for this 3DS Authentication.

    Refer to the [Pass acquirer details and directory server section of the standalone 3DS guide](https://docs.stripe.com/payments/3d-secure/standalone-3d-secure#pass-acquirer-details-and-directory-server) for more information.
    """
    amount: NotRequired[int]
    """
    A non-negative integer representing the amount in the [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal). You can't include this parameter if `message_category` is `non_payment_authentication`
    """
    channel: "AuthenticationCreateParamsChannel"
    """
    Contains additional details on the channel used for this 3DS Authentication.
    """
    currency: NotRequired[str]
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    directory_server: NotRequired[
        "Literal['american_express', 'cartes_bancaires', 'discover', 'mastercard', 'visa']|str"
    ]
    """
    The 3DS directory server with which this 3DS Authentication was processed.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    flow_preference: NotRequired["AuthenticationCreateParamsFlowPreference"]
    """
    Contains additional details on your flow preference for this 3DS Authentication.

    Refer to the [Specify a flow preference section of the standalone 3DS guide](https://docs.stripe.com/payments/3d-secure/standalone-3d-secure#specify-a-flow-preference) for more information.
    """
    future_usage: NotRequired["AuthenticationCreateParamsFutureUsage"]
    """
    Contains information about future usage of this 3DS Authentication
    """
    message_category: Union[
        Literal["non_payment_authentication", "payment_authentication"], str
    ]
    """
    Indicates whether this 3DS Authentication is being performed for a payment or non-payment use case.
    """
    metadata: NotRequired[
        "Literal['']|Dict[str, str]|UntypedStripeObject[str]"
    ]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """
    payment_method: NotRequired[str]
    """
    ID of the payment method (a PaymentMethod object) to attach to this 3DS Authentication.
    """
    payment_method_data: NotRequired[
        "AuthenticationCreateParamsPaymentMethodData"
    ]
    """
    Hash used to generate the PaymentMethod to be used for this Authentication. This is mutually exclusive with the `payment_method` parameter.
    """
    reason: NotRequired[
        "Literal['cardholder_authentication', 'issuer_requested', 'liability_shift', 'processing_costs', 'regulatory_compliance']|str"
    ]
    """
    The reason for invoking standalone 3DS. This is tailored specifically for cases when you want Stripe to help determine the standalone 3DS flow to fit your use case instead of needing to select a specific 3DS flow.

    This parameter is exclusive with `flow_preference`. You can either use `reason` for controlling 3DS according to your business requirements, or use `flow_preference` for having fine-grained control over your 3DS flow preference.
    """
    shipping_address: NotRequired["AuthenticationCreateParamsShippingAddress"]
    """
    The shipping address requested by the cardholder. You should try to include as complete address information as possible.
    """
    submit: NotRequired[
        "Literal['always', 'if_fingerprinting_not_supported', 'never']|str"
    ]
    """
    Set to `always` to skip the fingerprinting step and submit this Authentication immediately or `if_fingerprinting_not_supported` to submit this Authentication only if fingerprinting is not available. This parameter defaults to `never`.

    Refer to the [Submit at creation section of the standalone 3DS guide](https://docs.stripe.com/payments/3d-secure/standalone-3d-secure#submit-at-creation) for more information.
    """


class AuthenticationCreateParamsAcquirerDetails(TypedDict):
    acquirer_bin: str
    """
    The Acquirer BIN (specific to the directory_server).
    """
    acquirer_country: str
    """
    The two-letter country code of the acquirer ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
    """
    acquirer_merchant_id: str
    """
    The Merchant ID (or Card Acceptor ID) that your acquirer assigned you (specific to the directory_server).
    """
    mcc: NotRequired[str]
    """
    The [merchant category code](https://en.wikipedia.org/wiki/Merchant_category_code) as defined by each payment system or directory server.
    """
    merchant_name: NotRequired[str]
    """
    The merchant name assigned by the acquirer or payment system. Same name used in the authorization message as defined in [ISO 8583](https://en.wikipedia.org/wiki/ISO_8583).
    """
    requestor_id: NotRequired[str]
    """
    Requestor ID if you're enrolled in the card network's 3DS program. Otherwise, you can omit this field because Stripe assigns a Requestor ID with the card networks.
    """


class AuthenticationCreateParamsChannel(TypedDict):
    browser: NotRequired["AuthenticationCreateParamsChannelBrowser"]
    """
    Contains additional details about the browser details you collected.
    """
    three_r_i: NotRequired["AuthenticationCreateParamsChannelThreeRI"]
    """
    Contains additional details about the 3DS Requestor Initiated (3RI) channel.
    """
    type: Union[Literal["browser", "three_r_i"], str]
    """
    Type of channel you would prefer to use for this 3DS Authentication.
    """


class AuthenticationCreateParamsChannelBrowser(TypedDict):
    accept_header: str
    """
    The HTTP accept headers from the cardholder's browser. Collected server-side.
    """
    color_depth: NotRequired[int]
    """
    The color depth of the cardholder's screen.

    Returned from the `screen.colorDepth` property.
    """
    device_id: NotRequired[str]
    """
    Unique and immutable identifier linked to a device that is consistent across 3DS transactions for the specific user device. For example: hardware device ID or a platform-calculated device fingerprint.
    """
    ip_address: str
    """
    The IP address of the browser. Included in the HTTP request to your server before you create the 3DS Authentication.

    Collected server-side.
    """
    java_enabled: NotRequired[bool]
    """
    The cardholder browser's ability to execute Java. Returned from the navigator.javaEnabled property.
    """
    javascript_enabled: bool
    """
    The cardholder browser's ability to execute JavaScript.
    """
    language: str
    """
    An IETF BCP 47 language tag representing the browser language. Typically returned from the `navigator.language` property, but might also be returned from `navigator.languages` or `navigator.browserLanguage`.

     In some cases, this value might be an array. To cast it to a string or null value, you can use the `getBrowserLanguage()` [example function](https://docs.stripe.com/payments/3d-secure/standalone-3d-secure#pass-client-side-collected-channel-information).
    """
    screen_height: NotRequired[int]
    """
    The total height of the cardholder's screen in pixels.

    Returned from the `screen.height` property.
    """
    screen_width: NotRequired[int]
    """
    The total width of the cardholder's screen in pixels.

    Returned from the `screen.width` property.
    """
    timezone_offset: NotRequired[int]
    """
    The time difference between UTC time and the local time of the cardholder's browser, in minutes.

    Returned by `new Date().getTimezoneOffset()`
    """
    user_agent: str
    """
    The browser user agent. You can retrieve this value on the client side using the `navigator.userAgent` property, or in the HTTP request to your server before you create the 3DS Authentication.
    """


class AuthenticationCreateParamsChannelThreeRI(TypedDict):
    previous_authentication: str
    """
    ID of a prior `Authentication`. For example, the first recurring transaction that was authenticated by the cardholder.
    """
    type: Union[
        Literal[
            "delayed_shipment", "other_payment", "recurring", "split_shipment"
        ],
        str,
    ]
    """
    It provides additional information to the ACS to determine the best approach for handling a 3RI request.
    """


class AuthenticationCreateParamsFlowPreference(TypedDict):
    challenge: NotRequired["AuthenticationCreateParamsFlowPreferenceChallenge"]
    """
    Contains additional details about your challenge flow preference for this 3DS Authentication.
    """
    data_share: NotRequired[
        "AuthenticationCreateParamsFlowPreferenceDataShare"
    ]
    """
    Contains additional details about your data share only flow preference for this 3DS Authentication.
    """
    frictionless: NotRequired[
        "AuthenticationCreateParamsFlowPreferenceFrictionless"
    ]
    """
    Contains additional details about your frictionless flow preference for this 3DS Authentication.
    """
    type: Union[Literal["challenge", "data_share", "frictionless"], str]
    """
    Type of flow you requested for this 3DS Authentication.
    """


class AuthenticationCreateParamsFlowPreferenceChallenge(TypedDict):
    type: Union[Literal["mandated", "preferred"], str]
    """
    Type of challenge flow you requested for this 3DS Authentication.
    """


class AuthenticationCreateParamsFlowPreferenceDataShare(TypedDict):
    type: Union[Literal["ds_specific", "emv_standard"], str]
    """
    Type of data share only flow you requested for this 3DS Authentication.
    """


class AuthenticationCreateParamsFlowPreferenceFrictionless(TypedDict):
    type: Union[Literal["low_risk", "none"], str]
    """
    Type of frictionless flow you requested for this 3DS Authentication.
    """


class AuthenticationCreateParamsFutureUsage(TypedDict):
    installment: NotRequired[
        "AuthenticationCreateParamsFutureUsageInstallment"
    ]
    """
    Parameters related to an installment payment.
    """
    recurring: NotRequired["AuthenticationCreateParamsFutureUsageRecurring"]
    """
    Parameters related to a recurring payment.
    """
    type: Union[Literal["card_on_file", "installment", "recurring"], str]
    """
    The type of future usage declared for this 3DS Authentication
    """


class AuthenticationCreateParamsFutureUsageInstallment(TypedDict):
    amount: int
    """
    A non-negative integer representing the future authorizations' amount in the [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal).
    """
    expiry: "AuthenticationCreateParamsFutureUsageInstallmentExpiry"
    """
    Information about the expiry of the future usage of this authentication.
    """
    interval: NotRequired[Literal["day"]]
    """
    The unit of time for `interval_count`.
    """
    interval_count: NotRequired[int]
    """
    The minimum number of time intervals between authorizations. Must be greater than 0, and defaults to 1.
    """
    number: int
    """
    The maximum number of installments. Must be greater than 1.
    """


class AuthenticationCreateParamsFutureUsageInstallmentExpiry(TypedDict):
    date: NotRequired[str]
    """
    The date before which the last authorization related to this authentication will occur.
    """
    type: Union[Literal["date", "never"], str]
    """
    The type of expiry for the future use of this authentication.
    """


class AuthenticationCreateParamsFutureUsageRecurring(TypedDict):
    amount: int
    """
    A non-negative integer representing the future authorizations' amount in the [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal).
    """
    expiry: "AuthenticationCreateParamsFutureUsageRecurringExpiry"
    """
    Information about the expiry of the future usage of this authentication.
    """
    interval: NotRequired[Literal["day"]]
    """
    The unit of time for `interval_count`.
    """
    interval_count: NotRequired[int]
    """
    The minimum number of time intervals between authorizations. Must be greater than 0, and defaults to 1.
    """


class AuthenticationCreateParamsFutureUsageRecurringExpiry(TypedDict):
    date: NotRequired[str]
    """
    The date before which the last authorization related to this authentication will occur.
    """
    type: Union[Literal["date", "never"], str]
    """
    The type of expiry for the future use of this authentication.
    """


class AuthenticationCreateParamsPaymentMethodData(TypedDict):
    billing_details: NotRequired[
        "AuthenticationCreateParamsPaymentMethodDataBillingDetails"
    ]
    """
    Billing information associated with the PaymentMethod that may be used or required by particular types of payment methods.
    """
    card: "AuthenticationCreateParamsPaymentMethodDataCard"
    type: Literal["card"]
    """
    The type of the PaymentMethod. An additional hash is included on the PaymentMethod with a name matching this value. It contains additional information specific to the PaymentMethod type.
    """


class AuthenticationCreateParamsPaymentMethodDataBillingDetails(TypedDict):
    address: NotRequired[
        "AuthenticationCreateParamsPaymentMethodDataBillingDetailsAddress"
    ]
    """
    Billing address.
    """
    email: NotRequired[str]
    """
    Email address.
    """
    name: NotRequired[str]
    """
    Full name.
    """
    phone: NotRequired[str]
    """
    Billing phone number (including extension).
    """


class AuthenticationCreateParamsPaymentMethodDataBillingDetailsAddress(
    TypedDict,
):
    city: NotRequired[str]
    """
    City, district, suburb, town, or village.
    """
    country: NotRequired[str]
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
    postal_code: NotRequired[str]
    """
    ZIP or postal code.
    """
    state: NotRequired[str]
    """
    Country subdivision code defined in ISO 3166-2.
    """


class AuthenticationCreateParamsPaymentMethodDataCard(TypedDict):
    cvc: NotRequired[str]
    exp_month: NotRequired[int]
    exp_year: NotRequired[int]
    number: NotRequired[str]
    token: NotRequired[str]


class AuthenticationCreateParamsShippingAddress(TypedDict):
    city: NotRequired[str]
    """
    City, district, suburb, town, or village.
    """
    country: NotRequired[str]
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
    postal_code: NotRequired[str]
    """
    ZIP or postal code.
    """
    state: NotRequired[str]
    """
    Country subdivision code defined in ISO 3166-2.
    """
