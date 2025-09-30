# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import Dict, List
from typing_extensions import Literal, NotRequired


class PaymentRecordReportPaymentAttemptCanceledParams(RequestOptions):
    canceled_at: int
    """
    When the reported payment was canceled. Measured in seconds since the Unix epoch.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    metadata: NotRequired["Literal['']|Dict[str, str]"]
