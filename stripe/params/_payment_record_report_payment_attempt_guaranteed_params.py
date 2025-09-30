# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import Dict, List
from typing_extensions import Literal, NotRequired


class PaymentRecordReportPaymentAttemptGuaranteedParams(RequestOptions):
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    guaranteed_at: int
    """
    When the reported payment was guaranteed. Measured in seconds since the Unix epoch.
    """
    metadata: NotRequired["Literal['']|Dict[str, str]"]
