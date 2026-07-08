# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import List
from typing_extensions import Literal, NotRequired


class ReaderReloadGiftCardParams(RequestOptions):
    amount: int
    """
    The amount to add to the gift card balance, in the smallest currency unit.
    """
    brand: Literal["fiserv_valuelink", "givex", "svs"]
    """
    The brand of the gift card.
    """
    currency: str
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    on_behalf_of: NotRequired[str]
    """
    The Stripe account ID to process the gift card operation on behalf of.
    """
