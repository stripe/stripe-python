# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import List
from typing_extensions import Literal, NotRequired


class GiftCardCreateParams(RequestOptions):
    brand: Literal["fiserv_valuelink", "givex", "svs"]
    """
    The brand of the gift card.
    """
    exp_month: NotRequired[int]
    """
    Two-digit number representing the gift card's expiration month.
    """
    exp_year: NotRequired[int]
    """
    Four-digit number representing the gift card's expiration year.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    number: NotRequired[str]
    """
    The gift card number.
    """
    pin: NotRequired[str]
    """
    The gift card PIN.
    """
