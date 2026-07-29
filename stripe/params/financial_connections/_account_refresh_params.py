# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List, Union
from typing_extensions import Literal, NotRequired, TypedDict


class AccountRefreshParams(TypedDict):
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    features: List[
        Union[
            Literal[
                "balance", "inferred_balances", "ownership", "transactions"
            ],
            str,
        ]
    ]
    """
    The list of account features that you would like to refresh.
    """
