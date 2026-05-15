# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import List
from typing_extensions import NotRequired


class PaymentLocationCapabilityModifyParams(RequestOptions):
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    location: str
    """
    The location for which the capability enables functionality.
    """
    requested: bool
    """
    To request a new capability for the location, set this to `true`. You can remove it from the location by passing `false`.
    """
