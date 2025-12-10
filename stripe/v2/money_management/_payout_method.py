# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, List, Optional
from typing_extensions import Literal


class PayoutMethod(StripeObject):
    """
    Use the PayoutMethods API to list and interact with PayoutMethod objects.
    """

    OBJECT_NAME: ClassVar[Literal["v2.money_management.payout_method"]] = (
        "v2.money_management.payout_method"
    )

    class AlternativeReference(StripeObject):
        id: str
        """
        The ID of the alternative resource being referenced.
        """
        type: Literal["external_account", "payment_method"]
        """
        The type of the alternative reference (e.g., external_account for V1 external accounts).
        """

    class BankAccount(StripeObject):
        archived: bool
        """
        Whether this PayoutMethodBankAccount object was archived. PayoutMethodBankAccount objects can be archived through
        the /archive API, and they will not be automatically archived by Stripe. Archived PayoutMethodBankAccount objects
        cannot be used as payout methods and will not appear in the payout method list.
        """
        bank_account_type: Literal["checking", "savings"]
        """
        The type of bank account (checking or savings).
        """
        bank_name: str
        """
        The name of the bank this bank account is in. This field is populated automatically by Stripe.
        """
        country: str
        """
        The country code of the bank account.
        """
        enabled_delivery_options: List[str]
        """
        List of enabled flows for this bank account (wire or local).
        """
        financial_connections_account: Optional[str]
        """
        The ID of the Financial Connections Account used to create the bank account.
        """
        last4: str
        """
        The last 4 digits of the account number.
        """
        routing_number: Optional[str]
        """
        The routing number of the bank account, if present.
        """
        supported_currencies: List[str]
        """
        The list of currencies supported by this bank account.
        """

    class Card(StripeObject):
        archived: bool
        """
        Whether the PayoutMethodCard object was archived. PayoutMethodCard objects can be archived through
        the /archive API, and they will not be automatically archived by Stripe. Archived PayoutMethodCard objects
        cannot be used as payout methods and will not appear in the payout method list.
        """
        exp_month: str
        """
        The month the card expires.
        """
        exp_year: str
        """
        The year the card expires.
        """
        last4: str
        """
        The last 4 digits of the card number.
        """

    class CryptoWallet(StripeObject):
        address: str
        """
        Destination wallet address.
        """
        archived: bool
        """
        Whether the crypto wallet was archived. Crypto wallets can be archived through the /archive API,
        and they will not be automatically archived by Stripe. Archived crypto wallets cannot be used as
        payout method and will not appear in the payout method list.
        """
        memo: Optional[str]
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
        Which rail is being used to make an outbound money movement to this wallet.
        """

    class UsageStatus(StripeObject):
        payments: Literal["eligible", "invalid", "requires_action"]
        """
        Payments status - used when sending OutboundPayments (sending funds to recipients).
        """
        transfers: Literal["eligible", "invalid", "requires_action"]
        """
        Transfers status - used when making an OutboundTransfer (sending funds to yourself).
        """

    alternative_reference: Optional[AlternativeReference]
    """
    The alternative reference for this payout method, if it's a projected payout method.
    """
    available_payout_speeds: List[Literal["instant", "standard"]]
    """
    A set of available payout speeds for this payout method.
    """
    bank_account: Optional[BankAccount]
    """
    The PayoutMethodBankAccount object details.
    """
    card: Optional[Card]
    """
    The PayoutMethodCard object details.
    """
    created: str
    """
    Created timestamp.
    """
    crypto_wallet: Optional[CryptoWallet]
    """
    The PayoutMethodCryptoWallet object details.
    """
    id: str
    """
    ID of the PayoutMethod object.
    """
    latest_outbound_setup_intent: Optional[str]
    """
    ID of the underlying active OutboundSetupIntent object, if any.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["v2.money_management.payout_method"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    type: Literal["bank_account", "card", "crypto_wallet"]
    """
    Closed Enum. The type of payout method.
    """
    usage_status: UsageStatus
    """
    Indicates whether the payout method has met the necessary requirements for outbound money movement.
    """
    _inner_class_types = {
        "alternative_reference": AlternativeReference,
        "bank_account": BankAccount,
        "card": Card,
        "crypto_wallet": CryptoWallet,
        "usage_status": UsageStatus,
    }
