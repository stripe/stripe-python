# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_object import UntypedStripeObject
from typing import Dict, List
from typing_extensions import Literal, NotRequired, TypedDict


class PaymentRecordReportDisputeParams(RequestOptions):
    amount: "PaymentRecordReportDisputeParamsAmount"
    """
    The amount that has been lost to the customer due to disputes on this payment.
    """
    closed: NotRequired["PaymentRecordReportDisputeParamsClosed"]
    """
    Information about the dispute closing.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    funded: NotRequired["PaymentRecordReportDisputeParamsFunded"]
    """
    Information about the dispute funding event.
    """
    initiated_at: NotRequired[int]
    """
    When the reported payment was initiated. Measured in seconds since the Unix epoch.
    """
    metadata: NotRequired[
        "Literal['']|Dict[str, str]|UntypedStripeObject[str]"
    ]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """
    processor_details: "PaymentRecordReportDisputeParamsProcessorDetails"
    """
    Processor information for this payment.
    """
    reason: NotRequired[
        "Literal['bank_cannot_process', 'check_returned', 'credit_not_processed', 'customer_initiated', 'debit_not_authorized', 'duplicate', 'fraudulent', 'general', 'incorrect_account_details', 'insufficient_funds', 'noncompliant', 'product_not_received', 'product_unacceptable', 'subscription_canceled', 'unrecognized']|str"
    ]
    """
    The reason the payment was disputed.
    """


class PaymentRecordReportDisputeParamsAmount(TypedDict):
    currency: str
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    value: int
    """
    A positive integer representing the amount in the currency's [minor unit](https://docs.stripe.com/currencies#zero-decimal). For example, `100` can represent 1 USD or 100 JPY.
    """


class PaymentRecordReportDisputeParamsClosed(TypedDict):
    closed_at: int
    """
    When the dispute was closed. Measured in seconds since the Unix epoch.
    """


class PaymentRecordReportDisputeParamsFunded(TypedDict):
    amount: "PaymentRecordReportDisputeParamsFundedAmount"
    """
    The amount that has been lost to the customer due to disputes on this payment.
    """
    funded_at: int
    """
    When the dispute funding event occurred. Measured in seconds since the Unix epoch.
    """
    type: Literal["withdrawn"]
    """
    The type of dispute funding event.
    """


class PaymentRecordReportDisputeParamsFundedAmount(TypedDict):
    currency: str
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    value: int
    """
    A positive integer representing the amount in the currency's [minor unit](https://docs.stripe.com/currencies#zero-decimal). For example, `100` can represent 1 USD or 100 JPY.
    """


class PaymentRecordReportDisputeParamsProcessorDetails(TypedDict):
    custom: NotRequired[
        "PaymentRecordReportDisputeParamsProcessorDetailsCustom"
    ]
    """
    Information about the custom processor used to make this payment.
    """
    type: Literal["custom"]
    """
    The type of the processor details. An additional hash is included on processor_details with a name matching this value. It contains additional information specific to the processor.
    """


class PaymentRecordReportDisputeParamsProcessorDetailsCustom(TypedDict):
    dispute_reference: str
    """
    A reference to the external dispute. This field must be unique across all disputes.
    """
