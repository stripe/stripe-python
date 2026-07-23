# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_object import UntypedStripeObject
from typing import Dict, List
from typing_extensions import Literal, NotRequired


class DepositAddressCreateParams(RequestOptions):
    customer: NotRequired[str]
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    metadata: NotRequired["Dict[str, str]|UntypedStripeObject[str]"]
    network: Literal["base", "solana", "tempo"]
