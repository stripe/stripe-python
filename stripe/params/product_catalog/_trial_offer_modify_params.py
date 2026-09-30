# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import List
from typing_extensions import NotRequired


class TrialOfferModifyParams(RequestOptions):
    active: NotRequired[bool]
    """
    Whether the trial offer can be used for new purchases.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
