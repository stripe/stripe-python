# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import List
from typing_extensions import Literal, NotRequired


class SetupIntentCancelParams(RequestOptions):
    cancellation_reason: NotRequired[
        Literal["abandoned", "duplicate", "requested_by_customer"]
    ]
    """
    Reason for canceling this SetupIntent. Possible values are: `abandoned`, `requested_by_customer`, or `duplicate`
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
