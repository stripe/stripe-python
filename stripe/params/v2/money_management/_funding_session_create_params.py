# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List, Union
from typing_extensions import Literal, NotRequired, TypedDict


class FundingSessionCreateParams(TypedDict):
    account: str
    """
    The ID of the Account that owns the FinancialAccount. Required.
    """
    financial_account: str
    """
    The ID of the FinancialAccount to fund. Required.
    """
    financial_address_options: (
        "FundingSessionCreateParamsFinancialAddressOptions"
    )
    """
    Per-type options used when creating the FinancialAddress. Required.
    """
    financial_address_types: List[
        Union[Literal["bank_account", "crypto_wallet"], str]
    ]
    """
    Open Enum. The types of FinancialAddress that can be funded in this session. At least one is required.
    """
    return_url: str
    """
    The URL the customer is redirected to after completing or abandoning the funding session. Required.
    """


class FundingSessionCreateParamsFinancialAddressOptions(TypedDict):
    crypto_wallet: NotRequired[
        "FundingSessionCreateParamsFinancialAddressOptionsCryptoWallet"
    ]
    """
    Options for a crypto wallet FinancialAddress. Required if `crypto_wallet` is requested.
    """


class FundingSessionCreateParamsFinancialAddressOptionsCryptoWallet(TypedDict):
    settlement_currency: str
    """
    Open Enum. The currency the crypto wallet FinancialAddress settles into the FinancialAccount. Required.
    """
