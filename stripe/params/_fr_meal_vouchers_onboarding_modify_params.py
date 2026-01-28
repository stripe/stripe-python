# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import List
from typing_extensions import NotRequired


class FrMealVouchersOnboardingModifyParams(RequestOptions):
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    postal_code: str
    """
    Corrected Postal code of the restaurant.
    """
