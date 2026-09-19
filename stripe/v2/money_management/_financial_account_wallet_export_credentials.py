# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject, UntypedStripeObject
from typing import ClassVar, List, Union
from typing_extensions import Literal


class FinancialAccountWalletExportCredentials(StripeObject):
    """
    Credentials exported from a FinancialAccount wallet export.
    """

    OBJECT_NAME: ClassVar[
        Literal[
            "v2.money_management.financial_account_wallet_export_credentials"
        ]
    ] = "v2.money_management.financial_account_wallet_export_credentials"

    class Wallet(StripeObject):
        class CredentialsEncrypted(StripeObject):
            ciphertext: str
            """
            Base64url-encoded encrypted wallet credentials. Stripe does not persist this response.
            """
            encapsulated_key: str
            """
            Base64url-encoded HPKE encapsulated key.
            """
            type: Union[Literal["hpke"], str]
            """
            Encryption scheme used for these credentials.
            """

        address: str
        """
        Public address of the exported wallet.
        """
        credentials_encrypted: CredentialsEncrypted
        """
        Credentials encrypted to the supplied recipient public key.
        """
        currency_networks: UntypedStripeObject[Union[Literal["tempo"], str]]
        """
        Tempo network configured for each stablecoin currency. Keys are lowercase currency codes.
        """
        network_type: Union[Literal["ethereum"], str]
        """
        Network family for the wallet address.
        """
        _inner_class_types = {"credentials_encrypted": CredentialsEncrypted}

    credentials_available_until: str
    """
    End of the fixed one-hour credentials retrieval window.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal[
        "v2.money_management.financial_account_wallet_export_credentials"
    ]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    wallets: List[Wallet]
    """
    Exported wallets and credentials encrypted to the supplied recipient public key.
    """
    _inner_class_types = {"wallets": Wallet}
