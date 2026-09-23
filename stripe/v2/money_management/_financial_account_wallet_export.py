# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject, UntypedStripeObject
from typing import ClassVar, List, Optional, Union
from typing_extensions import Literal


class FinancialAccountWalletExport(StripeObject):
    """
    The singleton wallet export for a FinancialAccount.
    """

    OBJECT_NAME: ClassVar[
        Literal["v2.money_management.financial_account_wallet_export"]
    ] = "v2.money_management.financial_account_wallet_export"

    class Wallet(StripeObject):
        address: str
        """
        Public address of the exported wallet.
        """
        currency_networks: UntypedStripeObject[Union[Literal["tempo"], str]]
        """
        Network on which each stablecoin currency is stored. Keys are lowercase currency codes.
        """
        network_type: Union[Literal["ethereum"], str]
        """
        Network family for the wallet address.
        """

    credentials_available_until: Optional[str]
    """
    End of the fixed one-hour credentials retrieval window. Null until the first successful credential export; remains readable after expiry.
    """
    financial_account: str
    """
    FinancialAccount whose wallet is being exported.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["v2.money_management.financial_account_wallet_export"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    status: Literal["complete", "pending", "ready"]
    """
    Current wallet export status. The lifecycle is pending, ready, then complete.
    """
    wallets: Optional[List[Wallet]]
    """
    Public wallet metadata. Null while pending or ready, and retained after the credential window expires.
    """
    _inner_class_types = {"wallets": Wallet}
