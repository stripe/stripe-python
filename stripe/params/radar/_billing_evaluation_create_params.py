# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_object import UntypedStripeObject
from typing import Dict, List
from typing_extensions import Literal, NotRequired, TypedDict


class BillingEvaluationCreateParams(RequestOptions):
    client_device_metadata_details: NotRequired[
        "BillingEvaluationCreateParamsClientDeviceMetadataDetails"
    ]
    """
    Details about the client device to associate with the billing evaluation.
    """
    customer_details: "BillingEvaluationCreateParamsCustomerDetails"
    """
    Details about the customer whose upcoming payment is being evaluated.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    metadata: NotRequired["Dict[str, str]|UntypedStripeObject[str]"]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """
    payment_details: "BillingEvaluationCreateParamsPaymentDetails"
    """
    Details about the upcoming payment being evaluated.
    """


class BillingEvaluationCreateParamsClientDeviceMetadataDetails(TypedDict):
    radar_session: str
    """
    ID for the Radar Session to associate with the billing evaluation. A [Radar Session](https://docs.stripe.com/radar/radar-session) is a snapshot of the browser metadata and device details that help Radar make more accurate predictions about the customer behind the upcoming payment.
    """


class BillingEvaluationCreateParamsCustomerDetails(TypedDict):
    customer: NotRequired[str]
    """
    The ID of the customer whose upcoming payment is being evaluated.
    """
    customer_account: NotRequired[str]
    """
    The ID of the Account representing the customer whose upcoming payment is being evaluated.
    """
    data: NotRequired["BillingEvaluationCreateParamsCustomerDetailsData"]
    """
    Attributes of the customer being evaluated. Supply these when the customer isn't represented by a Customer or an Account. If `customer` or `customer_account` is also supplied, the attributes on that object are used and these are ignored.
    """


class BillingEvaluationCreateParamsCustomerDetailsData(TypedDict):
    email: NotRequired[str]
    """
    The email address of the customer being evaluated.
    """
    name: NotRequired[str]
    """
    The full name or business name of the customer being evaluated.
    """
    phone: NotRequired[str]
    """
    The phone number of the customer being evaluated.
    """


class BillingEvaluationCreateParamsPaymentDetails(TypedDict):
    amount: int
    """
    The amount that the upcoming payment collects. A positive integer representing how much is charged in the [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal) (for example, 100 cents to charge 1.00 USD or 100 to charge 100 Yen, a zero-decimal currency).
    """
    currency: str
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    description: NotRequired[str]
    """
    An arbitrary description of the upcoming payment.
    """
    money_movement_details: NotRequired[
        "BillingEvaluationCreateParamsPaymentDetailsMoneyMovementDetails"
    ]
    """
    Details about how the money for the upcoming payment moves.
    """
    payment_method_details: (
        "BillingEvaluationCreateParamsPaymentDetailsPaymentMethodDetails"
    )
    """
    Details about the payment method that the upcoming payment is charged to.
    """
    shipping_details: NotRequired[
        "BillingEvaluationCreateParamsPaymentDetailsShippingDetails"
    ]
    """
    Shipping details for the goods or services covered by the upcoming payment.
    """
    statement_descriptor: NotRequired[str]
    """
    The statement descriptor that appears on the customer's statement for the upcoming payment.
    """


class BillingEvaluationCreateParamsPaymentDetailsMoneyMovementDetails(
    TypedDict,
):
    card: NotRequired[
        "BillingEvaluationCreateParamsPaymentDetailsMoneyMovementDetailsCard"
    ]
    """
    Describes card money movement details.
    """
    money_movement_type: Literal["card"]
    """
    Describes the type of money movement. Currently only `card` is supported.
    """


class BillingEvaluationCreateParamsPaymentDetailsMoneyMovementDetailsCard(
    TypedDict,
):
    customer_presence: NotRequired["Literal['off_session', 'on_session']|str"]
    """
    Describes the presence of the customer during the payment.
    """
    payment_type: NotRequired[
        "Literal['one_off', 'recurring', 'setup_one_off', 'setup_recurring']|str"
    ]
    """
    Describes the type of payment.
    """


class BillingEvaluationCreateParamsPaymentDetailsPaymentMethodDetails(
    TypedDict,
):
    billing_details: NotRequired[
        "BillingEvaluationCreateParamsPaymentDetailsPaymentMethodDetailsBillingDetails"
    ]
    """
    Billing information associated with the payment method used for the upcoming payment.
    """
    payment_method: str
    """
    ID of the payment method that the upcoming payment is charged to.
    """


class BillingEvaluationCreateParamsPaymentDetailsPaymentMethodDetailsBillingDetails(
    TypedDict,
):
    address: NotRequired[
        "BillingEvaluationCreateParamsPaymentDetailsPaymentMethodDetailsBillingDetailsAddress"
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


class BillingEvaluationCreateParamsPaymentDetailsPaymentMethodDetailsBillingDetailsAddress(
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
    State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).
    """


class BillingEvaluationCreateParamsPaymentDetailsShippingDetails(TypedDict):
    address: NotRequired[
        "BillingEvaluationCreateParamsPaymentDetailsShippingDetailsAddress"
    ]
    """
    Shipping address.
    """
    name: NotRequired[str]
    """
    Shipping name.
    """
    phone: NotRequired[str]
    """
    Shipping phone number.
    """


class BillingEvaluationCreateParamsPaymentDetailsShippingDetailsAddress(
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
    State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).
    """
