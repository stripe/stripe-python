# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import List, Union
from typing_extensions import Literal, NotRequired


class ReaderCashoutGiftCardParams(RequestOptions):
    brand: Union[Literal["svs"], str]
    """
    The brand of the gift card.
    """
    enable_customer_cancellation: NotRequired[bool]
    """
    Enables cancel button on gift card operation screens.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    on_behalf_of: NotRequired[str]
    """
    The Stripe account ID to process the gift card operation on behalf of.
    """
