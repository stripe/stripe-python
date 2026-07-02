# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import List
from typing_extensions import Literal, NotRequired


class OnrampTransactionLimitsRetrieveParams(RequestOptions):
    customer_ip_address: NotRequired[str]
    """
    The IP address of the customer requesting transaction limits. We support IPv4 and IPv6 addresses.
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
    The destination blockchain network to use for limit calculations.
    """
    destination_tag: NotRequired[str]
    """
    The destination tag for the wallet address, if applicable for the network.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    wallet_address: NotRequired[str]
    """
    The wallet address to use for destination-specific limit calculations.
    """
