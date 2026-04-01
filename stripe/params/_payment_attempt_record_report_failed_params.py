# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_object import UntypedStripeObject
from typing import Dict, List
from typing_extensions import Literal, NotRequired, TypedDict


class PaymentAttemptRecordReportFailedParams(RequestOptions):
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    failed_at: NotRequired[int]
    """
    When the reported payment failed. Measured in seconds since the Unix epoch.
    """
    failure_code: NotRequired[
        Literal[
            "payment_method_customer_decline",
            "payment_method_provider_unknown_outcome",
        ]
    ]
    """
    The failure code for this payment attempt. Must be one of `payment_method_customer_decline` or `payment_method_provider_unknown_outcome`.
    """
    metadata: NotRequired[
        "Literal['']|Dict[str, str]|UntypedStripeObject[str]"
    ]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """
    processor_details: NotRequired[
        "PaymentAttemptRecordReportFailedParamsProcessorDetails"
    ]
    """
    Processor information for this payment.
    """


class PaymentAttemptRecordReportFailedParamsProcessorDetails(TypedDict):
    custom: NotRequired[
        "PaymentAttemptRecordReportFailedParamsProcessorDetailsCustom"
    ]
    """
    Information about the custom processor used to make this payment.
    """
    type: Literal["custom"]
    """
    The type of the processor details. An additional hash is included on processor_details with a name matching this value. It contains additional information specific to the processor.
    """


class PaymentAttemptRecordReportFailedParamsProcessorDetailsCustom(TypedDict):
    payment_reference: str
    """
    An opaque string for manual reconciliation of this payment, for example a check number or a payment processor ID.
    """
