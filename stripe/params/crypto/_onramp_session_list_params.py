# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import List
from typing_extensions import Literal, NotRequired, TypedDict


class OnrampSessionListParams(RequestOptions):
    created: NotRequired["OnrampSessionListParamsCreated|int"]
    """
    Only return onramp sessions that were created during the given date interval.
    """
    destination_currency: NotRequired[
        Literal["avax", "btc", "eth", "matic", "sol", "usdc", "wld", "xlm"]
    ]
    """
    The destination cryptocurrency to filter by.
    """
    destination_network: NotRequired[
        Literal[
            "avalanche",
            "base",
            "bitcoin",
            "ethereum",
            "optimism",
            "polygon",
            "solana",
            "stellar",
            "worldchain",
        ]
    ]
    """
    The destination blockchain network to filter by.
    """
    ending_before: NotRequired[str]
    """
    An object ID cursor for use in pagination.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    limit: NotRequired[int]
    """
    A limit ranging from 1 to 100 (defaults to 10).
    """
    starting_after: NotRequired[str]
    """
    An object ID cursor for use in pagination.
    """
    status: NotRequired[
        Literal[
            "fulfillment_complete",
            "fulfillment_processing",
            "initialized",
            "rejected",
            "requires_payment",
        ]
    ]
    """
    The status of the Onramp Session. One of = `{initialized, rejected, requires_payment, fulfillment_processing, fulfillment_complete}`
    """


class OnrampSessionListParamsCreated(TypedDict):
    gt: NotRequired[int]
    """
    Minimum value to filter by (exclusive)
    """
    gte: NotRequired[int]
    """
    Minimum value to filter by (inclusive)
    """
    lt: NotRequired[int]
    """
    Maximum value to filter by (exclusive)
    """
    lte: NotRequired[int]
    """
    Maximum value to filter by (inclusive)
    """
