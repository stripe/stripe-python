# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List, Union
from typing_extensions import Literal, NotRequired, TypedDict


class ContractCancelParams(TypedDict):
    cancel_pricing_lines: NotRequired[
        List["ContractCancelParamsCancelPricingLine"]
    ]
    """
    Per-pricing-line proration behavior overrides. Falls back to `proration_behavior` if
    not specified for a given line.
    """
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
    Per-term proration overrides. Cannot be combined with cancel_pricing_lines.
    """


class ContractCancelParamsCancelPricingLine(TypedDict):
    id: NotRequired[str]
    """
    The id of the pricing line.
    """
    lookup_key: NotRequired[str]
    """
    The lookup key of the pricing line.
    """
    proration_behavior: NotRequired["Literal['none', 'prorated']|str"]
    """
    Proration behavior scoped to this pricing line. If not provided, falls back to the
    top-level `proration_behavior` on the cancel request. Defaults to `prorated`.
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
