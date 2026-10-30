# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import Union
from typing_extensions import Literal, NotRequired, TypedDict


class FinancialAddressCreateParams(TypedDict):
    account: NotRequired[str]
    """
    The ID of the Account that owns this FinancialAddress.
    """
    bank_account: NotRequired["FinancialAddressCreateParamsBankAccount"]
    """
    Properties for creating a bank account FinancialAddress.
    """
    crypto_wallet: NotRequired["FinancialAddressCreateParamsCryptoWallet"]
    """
    Properties for creating a crypto wallet FinancialAddress. Requires `settlement_currency`.
    """
    financial_account: str
    """
    The ID of the FinancialAccount the new FinancialAddress should be associated with.
    """
    settlement_currency: NotRequired[str]
    """
    Open Enum. The currency the FinancialAddress settles into the FinancialAccount. Optional for `bank_account`, where it defaults to `bank_account.currency`; required for all other types.
    """
    type: Union[Literal["bank_account", "crypto_wallet"], str]
    """
    The type of FinancialAddress to create. Must agree with which branch of financial_address_type_properties is set.
    """


class FinancialAddressCreateParamsBankAccount(TypedDict):
    country: NotRequired[str]
    """
    The country where Stripe provisions the bank account. Each currency supports the country listed in its description. If omitted, Stripe selects that country.
    """
    currency: Union[
        Literal["brl", "cad", "cop", "eur", "gbp", "mxn", "ngn", "pln", "usd"],
        str,
    ]
    """
    The currency of the bank account to provision. Some currencies require preview or rollout access, as configured for your account.
    """


class FinancialAddressCreateParamsCryptoWallet(TypedDict):
    network: Union[
        Literal[
            "arbitrum",
            "avalanche_c_chain",
            "base",
            "bitcoin",
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
