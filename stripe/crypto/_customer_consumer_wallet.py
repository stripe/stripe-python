# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Union
from typing_extensions import Literal


class CustomerConsumerWallet(StripeObject):
    """
    A consumer wallet represents a cryptocurrency wallet address associated with a Crypto Customer.
    """

    OBJECT_NAME: ClassVar[Literal["crypto.consumer_wallet"]] = (
        "crypto.consumer_wallet"
    )
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.
    """
    network: Union[
        Literal[
            "aptos",
            "avalanche",
            "base",
            "bitcoin",
            "ethereum",
            "optimism",
            "polygon",
            "solana",
            "stellar",
            "sui",
            "worldchain",
        ],
        str,
    ]
    """
    The blockchain network for this wallet
    """
    object: Literal["crypto.consumer_wallet"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    verified_ownership: bool
    """
    Whether ownership of this wallet has been verified
    """
    wallet_address: str
    """
    The wallet address
    """
