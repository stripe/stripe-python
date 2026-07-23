# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import List, Union
from typing_extensions import Literal, NotRequired


class PaymentIntentSimulateCryptoDepositParams(RequestOptions):
    buyer_wallet: str
    """
    The buyer's wallet address from which the crypto deposit is originating.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    network: Union[
        Literal["base", "ethereum", "polygon", "solana", "tempo"], str
    ]
    """
    The blockchain network of the simulated crypto deposit.
    """
    token_currency: Literal["usdc", "usdg", "usdp"]
    """
    The token currency of the simulated crypto deposit.
    """
    transaction_hash: str
    """
    A testmode transaction hash that determines the outcome of the simulated deposit.
    """
