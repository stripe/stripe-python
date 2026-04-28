# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import Literal, NotRequired, TypedDict


class FinancialAddressCreateParams(TypedDict):
    crypto_properties: NotRequired[
        "FinancialAddressCreateParamsCryptoProperties"
    ]
    """
    Properties needed to create a FinancialAddress for an FA with USDC currency.
    """
    financial_account: str
    """
    The ID of the FinancialAccount the new FinancialAddress should be associated with.
    """
    sepa_bank_account: NotRequired[
        "FinancialAddressCreateParamsSepaBankAccount"
    ]
    """
    Optional SEPA Bank account options, used to configure the type of SEPA Bank account to create, such as the originating country.
    """
    settlement_currency: NotRequired[str]
    """
    Open Enum. The currency the FinancialAddress settles into the FinancialAccount. Currently, only the `usd`, `gbp` and `usdc` values are supported.
    """
    type: Literal[
        "ca_bank_account",
        "crypto_wallet",
        "gb_bank_account",
        "mx_bank_account",
        "sepa_bank_account",
        "us_bank_account",
    ]
    """
    The type of FinancialAddress details to provision.
    """


class FinancialAddressCreateParamsCryptoProperties(TypedDict):
    network: Literal[
        "arbitrum",
        "avalanche_c_chain",
        "base",
        "ethereum",
        "optimism",
        "polygon",
        "solana",
        "stellar",
        "tempo",
    ]
    """
    The blockchain network of the crypto wallet.
    """


class FinancialAddressCreateParamsSepaBankAccount(TypedDict):
    country: str
    """
    The originating country of the SEPA Bank account.
    """
