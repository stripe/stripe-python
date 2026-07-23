# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_object import UntypedStripeObject
from typing import Dict, List
from typing_extensions import Literal, NotRequired, TypedDict


class PaymentRecordReportPaymentAttemptGuaranteedParams(RequestOptions):
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    guaranteed_at: NotRequired[int]
    """
    When the reported payment was guaranteed. Measured in seconds since the Unix epoch.
    """
    metadata: NotRequired[
        "Literal['']|Dict[str, str]|UntypedStripeObject[str]"
    ]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """
    payment_evaluations: NotRequired[List[str]]
    """
    Payment evaluations associated with this reported payment.
    """
    payment_method_details: NotRequired[
        "PaymentRecordReportPaymentAttemptGuaranteedParamsPaymentMethodDetails"
    ]
    """
    Information about the Payment Method debited for this payment.
    """
    processor_details: NotRequired[
        "PaymentRecordReportPaymentAttemptGuaranteedParamsProcessorDetails"
    ]
    """
    Processor information for this payment.
    """


class PaymentRecordReportPaymentAttemptGuaranteedParamsPaymentMethodDetails(
    TypedDict,
):
    card: NotRequired[
        "PaymentRecordReportPaymentAttemptGuaranteedParamsPaymentMethodDetailsCard"
    ]
    """
    Information about the card payment method used to make this payment.
    """
    type: Literal["card"]
    """
    The type of the payment method details. An additional hash is included on the payment_method_details with a name matching this value. It contains additional information specific to the type.
    """


class PaymentRecordReportPaymentAttemptGuaranteedParamsPaymentMethodDetailsCard(
    TypedDict,
):
    checks: NotRequired[
        "PaymentRecordReportPaymentAttemptGuaranteedParamsPaymentMethodDetailsCardChecks"
    ]
    """
    Verification checks performed on the card.
    """


class PaymentRecordReportPaymentAttemptGuaranteedParamsPaymentMethodDetailsCardChecks(
    TypedDict,
):
    address_line1_check: NotRequired[
        "Literal['fail', 'pass', 'unavailable', 'unchecked']|str"
    ]
    """
    The result of the check on the cardholder's address line 1.
    """
    address_postal_code_check: NotRequired[
        "Literal['fail', 'pass', 'unavailable', 'unchecked']|str"
    ]
    """
    The result of the check on the cardholder's postal code.
    """
    cvc_check: NotRequired[
        "Literal['fail', 'pass', 'unavailable', 'unchecked']|str"
    ]
    """
    The result of the check on the card's CVC.
    """


class PaymentRecordReportPaymentAttemptGuaranteedParamsProcessorDetails(
    TypedDict,
):
    custom: NotRequired[
        "PaymentRecordReportPaymentAttemptGuaranteedParamsProcessorDetailsCustom"
    ]
    """
    Information about the custom processor used to make this payment.
    """
    type: Literal["custom"]
    """
    The type of the processor details. An additional hash is included on processor_details with a name matching this value. It contains additional information specific to the processor.
    """


class PaymentRecordReportPaymentAttemptGuaranteedParamsProcessorDetailsCustom(
    TypedDict,
):
    payment_reference: str
    """
    An opaque string for manual reconciliation of this payment, for example a check number or a payment processor ID.
    """
