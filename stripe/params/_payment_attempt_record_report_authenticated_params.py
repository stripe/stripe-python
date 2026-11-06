# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_object import UntypedStripeObject
from typing import Dict, List, Union
from typing_extensions import Literal, NotRequired, TypedDict


class PaymentAttemptRecordReportAuthenticatedParams(RequestOptions):
    authenticated_at: NotRequired[int]
    """
    When the reported payment was authenticated. Measured in seconds since the Unix epoch.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    metadata: NotRequired[
        "Literal['']|Dict[str, str]|UntypedStripeObject[str]"
    ]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """
    payment_method_details: NotRequired[
        "PaymentAttemptRecordReportAuthenticatedParamsPaymentMethodDetails"
    ]
    """
    Information about the Payment Method debited for this payment.
    """


class PaymentAttemptRecordReportAuthenticatedParamsPaymentMethodDetails(
    TypedDict,
):
    card: NotRequired[
        "PaymentAttemptRecordReportAuthenticatedParamsPaymentMethodDetailsCard"
    ]
    """
    Information about the card payment method used to make this payment.
    """
    type: Literal["card"]
    """
    The type of the payment method details. An additional hash is included on the payment_method_details with a name matching this value. It contains additional information specific to the type.
    """


class PaymentAttemptRecordReportAuthenticatedParamsPaymentMethodDetailsCard(
    TypedDict,
):
    three_d_secure: NotRequired[
        "PaymentAttemptRecordReportAuthenticatedParamsPaymentMethodDetailsCardThreeDSecure"
    ]
    """
    Populated if this transaction used 3D Secure authentication.
    """


class PaymentAttemptRecordReportAuthenticatedParamsPaymentMethodDetailsCardThreeDSecure(
    TypedDict,
):
    authentication_flow: NotRequired[
        "Literal['challenge', 'frictionless']|str"
    ]
    """
    For authenticated transactions: Indicates how the issuing bank authenticated the customer.
    """
    electronic_commerce_indicator: NotRequired[
        "Literal['01', '02', '05', '06', '07']|str"
    ]
    """
    The Electronic Commerce Indicator (ECI). A protocol-level field indicating what degree of authentication was performed.
    """
    exemption_indicator: NotRequired["Literal['low_risk', 'none']|str"]
    """
    The exemption requested via 3DS and accepted by the issuer at authentication time.
    """
    result: Union[
        Literal["attempt_acknowledged", "authenticated", "exempted"], str
    ]
    """
    Indicates the outcome of 3D Secure authentication.
    """
    version: Union[Literal["1.0.2", "2.1.0", "2.2.0", "2.3.0", "2.3.1"], str]
    """
    The version of 3D Secure that was used.
    """
