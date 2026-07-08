# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List
from typing_extensions import Literal, NotRequired, TypedDict


class AccountListParams(TypedDict):
    applied_configurations: NotRequired[
        List[
            Literal[
                "card_creator",
                "customer",
                "merchant",
                "recipient",
                "money_manager",
            ]
        ]
    ]
    """
    Filter only accounts that have all of the configurations specified. If omitted, returns all accounts regardless of which configurations they have.
    """
    closed: NotRequired[bool]
    """
    Filter by whether the account is closed. If omitted, returns only Accounts that are not closed.
    """
    limit: NotRequired[int]
    """
    The upper limit on the number of accounts returned by the List Account request.
    """
    related_network_object: NotRequired[str]
    """
    Filter by the network object related to the account. If omitted, returns all Accounts regardless of the network object they have.
    """
