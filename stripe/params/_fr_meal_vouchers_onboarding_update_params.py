# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List
from typing_extensions import NotRequired, TypedDict


class FrMealVouchersOnboardingUpdateParams(TypedDict):
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    postal_code: str
    """
    Corrected Postal code of the restaurant.
    """
