# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import Union
from typing_extensions import Literal, NotRequired, TypedDict


class OutboundSetupIntentCreateParams(TypedDict):
    from_resource: NotRequired["OutboundSetupIntentCreateParamsFromResource"]
    """
    An existing resource to use as the source for setting up outbound credentials.
    """
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


class OutboundSetupIntentCreateParamsFromResource(TypedDict):
    id: str
    """
    The identifier of the source resource.
    """
    type: Union[Literal["payment_method"], str]
    """
    The type of the source resource.
    """


class OutboundSetupIntentCreateParamsPayoutMethodData(TypedDict):
    apple_pay: NotRequired[
        "OutboundSetupIntentCreateParamsPayoutMethodDataApplePay"
    ]
    """
    The type specific details of the Apple Pay payout method.
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
    type: Union[
        Literal[
            "apple_pay",
            "bank_account",
            "card",
            "crypto_wallet",
            "network_business_profile_wallet",
        ],
        str,
    ]
    """
    Open Enum. The type of payout method to be created.
    """


class OutboundSetupIntentCreateParamsPayoutMethodDataApplePay(TypedDict):
    pk_token: NotRequired[str]
    """
    The paymentData property of the Apple-provided PKPaymentToken (or ApplePayPaymentToken, for Apple Pay on the Web) as a UTF-8 encoded serialization of a JSON dictionary.
    """
    pk_token_display_name: str
    """
    The paymentMethod.displayName property of the Apple-provided PKPaymentToken (or ApplePayPaymentToken, for Apple Pay on the Web), e.g. "Visa 1234".
    """


class OutboundSetupIntentCreateParamsPayoutMethodDataBankAccount(TypedDict):
    account_number: str
    """
    The account number or IBAN of the bank account.
    """
    bank_account_type: NotRequired[
        Literal["checking", "futsu", "savings", "toza"]
    ]
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
    currency: str
    """
    The currency of the bank account.
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
    currency: str
    """
    The currency of the card.
    """
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
    Which rail we should use to make an Outbound money movement to this wallet.
    """
