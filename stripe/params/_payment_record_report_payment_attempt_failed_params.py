# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import Dict, List
from typing_extensions import Literal, NotRequired


class PaymentRecordReportPaymentAttemptFailedParams(RequestOptions):
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    failed_at: int
    """
    When the reported payment failed. Measured in seconds since the Unix epoch.
    """
    metadata: NotRequired["Literal['']|Dict[str, str]"]
