# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import List
from typing_extensions import NotRequired


class RequestedSessionConfirmParams(RequestOptions):
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    payment_method: NotRequired[str]
    """
    The PaymentMethod to use with the requested session.
    """
