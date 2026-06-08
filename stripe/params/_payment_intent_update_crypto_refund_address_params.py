# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import List
from typing_extensions import Literal, NotRequired


class PaymentIntentUpdateCryptoRefundAddressParams(RequestOptions):
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    network: Literal["base", "ethereum", "polygon", "solana", "sui", "tempo"]
    """
    The blockchain network for the refund address.
    """
    refund_address: str
    """
    The wallet address that should receive refunds for deposits on the specified network.
    """
