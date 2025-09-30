# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import Literal, NotRequired, TypedDict


class OutboundSetupIntentCreateParams(TypedDict):
    payout_method: NotRequired[str]
    """
    If provided, the existing payout method resource to link to this setup intent.
    Any payout_method_data provided is used to update information on this linked payout method resource.
    """
    payout_method_data: NotRequired[
        "OutboundSetupIntentCreateParamsPayoutMethodData"
    ]
    """
    If no payout_method provided, used to create the underlying credential that is set up for outbound money movement.
    If a payout_method provided, used to update data on the credential linked to this setup intent.
    """
    usage_intent: NotRequired[Literal["payment", "transfer"]]
    """
    Specify which type of outbound money movement this credential should be set up for (payment | transfer).
    If not provided, defaults to payment.
    """


class OutboundSetupIntentCreateParamsPayoutMethodData(TypedDict):
    type: Literal["bank_account", "card", "crypto_wallet"]
    """
    Closed Enum. The type of payout method to be created.
    """
    bank_account: NotRequired[
        "OutboundSetupIntentCreateParamsPayoutMethodDataBankAccount"
    ]
    """
    The type specific details of the bank account payout method.
    """
    card: NotRequired["OutboundSetupIntentCreateParamsPayoutMethodDataCard"]
    """
    The type specific details of the card payout method.
    """
    crypto_wallet: NotRequired[
        "OutboundSetupIntentCreateParamsPayoutMethodDataCryptoWallet"
    ]
    """
    The type specific details of the crypto wallet payout method.
    """


class OutboundSetupIntentCreateParamsPayoutMethodDataBankAccount(TypedDict):
    account_number: str
    """
    The account number or IBAN of the bank account.
    """
    bank_account_type: NotRequired[Literal["checking", "savings"]]
    """
    Closed Enum. The type of the bank account (checking or savings).
    """
    branch_number: NotRequired[str]
    """
    The branch number of the bank account, if present.
    """
    country: str
    """
    The country code of the bank account.
    """
    routing_number: NotRequired[str]
    """
    The routing number of the bank account, if present.
    """
    swift_code: NotRequired[str]
    """
    The swift code of the bank account, if present.
    """


class OutboundSetupIntentCreateParamsPayoutMethodDataCard(TypedDict):
    exp_month: str
    """
    The expiration month of the card.
    """
    exp_year: str
    """
    The expiration year of the card.
    """
    number: str
    """
    The card number.
    """


class OutboundSetupIntentCreateParamsPayoutMethodDataCryptoWallet(TypedDict):
    address: str
    """
    Crypto wallet address.
    """
    memo: NotRequired[str]
    """
    Optional field, required if network supports memos (only "stellar" currently).
    """
    network: Literal[
        "arbitrum",
        "avalanche_c_chain",
        "base",
        "ethereum",
        "optimism",
        "polygon",
        "solana",
        "stellar",
    ]
    """
    Which rail we should use to make an Outbound money movement to this wallet.
    """
