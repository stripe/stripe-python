# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import List, Union
from typing_extensions import Literal, NotRequired


class AccountSubscribeParams(RequestOptions):
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    features: List[
        Union[Literal["balance", "inferred_balances", "transactions"], str]
    ]
    """
    The list of account features to which you would like to subscribe.
    """
