# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List
from typing_extensions import Literal, NotRequired, TypedDict


class AccountRetrieveParams(TypedDict):
    include: NotRequired[
        List[
            Literal[
                "configuration.card_creator",
                "configuration.customer",
                "configuration.merchant",
                "configuration.recipient",
                "configuration.storer",
                "defaults",
                "future_requirements",
                "identity",
                "requirements",
            ]
        ]
    ]
    """
    Additional fields to include in the response.
    """
