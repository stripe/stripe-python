# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import Dict, List
from typing_extensions import Literal, NotRequired


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
    metadata: NotRequired["Literal['']|Dict[str, str]"]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """
