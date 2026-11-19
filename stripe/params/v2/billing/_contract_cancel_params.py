# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List, Union
from typing_extensions import Literal, NotRequired, TypedDict


class ContractCancelParams(TypedDict):
    include: NotRequired[
        List[
            Union[
                Literal[
                    "billing_settings",
                    "one_time_fees",
                    "pricing_lines",
                    "pricing_overrides",
                    "terms",
                ],
                str,
            ]
        ]
    ]
    """
    Additional fields to include in the response.
    """
    proration_behavior: NotRequired["Literal['none', 'prorated']|str"]
    """
    Top-level proration behavior for the cancellation. Defaults to `prorated` if not set.
    """
    terms: NotRequired[List["ContractCancelParamsTerm"]]
    """
    Per-term proration overrides.
    """


class ContractCancelParamsTerm(TypedDict):
    proration_behavior: NotRequired["Literal['none', 'prorated']|str"]
    """
    Falls back to the contract cancellation's top-level proration behavior.
    """
    term: "ContractCancelParamsTermTerm"
    """
    Select a term by ID or its unique lookup key.
    """


class ContractCancelParamsTermTerm(TypedDict):
    id: NotRequired[str]
    """
    Select this term by its stable ID.
    """
    lookup_key: NotRequired[str]
    """
    Select this term by its unique lookup key.
    """
    type: Literal["id", "lookup_key"]
    """
    Whether the selector uses a term ID or lookup key.
    """
