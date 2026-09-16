# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import Union
from typing_extensions import Literal, NotRequired, TypedDict


class FinancialAddressCreateParams(TypedDict):
    bank_account: NotRequired["FinancialAddressCreateParamsBankAccount"]
    """
    Properties for creating a bank account FinancialAddress.
    """
    crypto_wallet: NotRequired["FinancialAddressCreateParamsCryptoWallet"]
    financial_account: str
    """
    The ID of the FinancialAccount the new FinancialAddress should be associated with.
    """
    settlement_currency: NotRequired[str]
    type: Union[Literal["bank_account", "crypto_wallet"], str]
    """
    The type of FinancialAddress to create. Must agree with which branch of financial_address_type_properties is set.
    """


class FinancialAddressCreateParamsBankAccount(TypedDict):
    country: NotRequired[str]
    """
    The country for the bank account. Used to select the appropriate rails (e.g. for SEPA).
    """
    currency: Union[Literal["cad", "eur", "gbp", "mxn", "usd"], str]
    """
    The currency of the bank account to provision.
    """


class FinancialAddressCreateParamsCryptoWallet(TypedDict):
    network: Union[
        Literal[
            "arbitrum",
            "avalanche_c_chain",
            "base",
            "ethereum",
            "optimism",
            "polygon",
            "solana",
            "stellar",
            "tempo",
        ],
        str,
    ]
    """
    The blockchain network of the crypto wallet.
    """
