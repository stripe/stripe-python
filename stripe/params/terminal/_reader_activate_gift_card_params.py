# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import List
from typing_extensions import Literal, NotRequired, TypedDict


class ReaderActivateGiftCardParams(RequestOptions):
    balance: NotRequired["ReaderActivateGiftCardParamsBalance"]
    """
    The initial balance to set on the gift card.
    """
    brand: Literal["fiserv_valuelink", "givex", "svs"]
    """
    The brand of the gift card.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    on_behalf_of: NotRequired[str]
    """
    The Stripe account ID to process the gift card operation on behalf of.
    """


class ReaderActivateGiftCardParamsBalance(TypedDict):
    amount: int
    """
    The initial balance amount to be loaded when activating the gift card, in the smallest currency unit
    """
    currency: str
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
