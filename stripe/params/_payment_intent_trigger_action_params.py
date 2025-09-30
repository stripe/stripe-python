# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import List
from typing_extensions import Literal, NotRequired, TypedDict


class PaymentIntentTriggerActionParams(RequestOptions):
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    scan_qr_code: NotRequired["PaymentIntentTriggerActionParamsScanQrCode"]
    """
    True to simulate success, false to simulate failure.
    """
    type: Literal["expire", "fund"]
    """
    The type of action to be simulated.
    """


class PaymentIntentTriggerActionParamsScanQrCode(TypedDict):
    result: NotRequired[Literal["failure", "success"]]
    """
    Whether the QR Code scan's payment should succeed or fail.
    """
