# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import List
from typing_extensions import NotRequired


class GiftCardCheckBalanceParams(RequestOptions):
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    on_behalf_of: NotRequired[str]
    """
    The Stripe account ID to process the gift card operation on behalf of.
    """
