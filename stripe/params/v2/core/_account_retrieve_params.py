# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List
from typing_extensions import Literal, NotRequired, TypedDict


class AccountRetrieveParams(TypedDict):
    include: NotRequired[
        List[
            Literal[
                "configuration.customer",
                "configuration.merchant",
                "configuration.recipient",
                "configuration.storer",
                "defaults",
                "identity",
                "requirements",
            ]
        ]
    ]
    """
    Additional fields to include in the response.
    """
