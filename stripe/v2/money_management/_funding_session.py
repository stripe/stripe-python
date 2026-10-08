# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, List, Optional, Union
from typing_extensions import Literal


class FundingSession(StripeObject):
    """
    A FundingSession is a hosted funding surface for a customer to fund a FinancialAccount.
    """

    OBJECT_NAME: ClassVar[Literal["v2.money_management.funding_session"]] = (
        "v2.money_management.funding_session"
    )

    class FinancialAddressOptions(StripeObject):
        class CryptoWallet(StripeObject):
            settlement_currency: str
            """
            Open Enum. The currency the crypto wallet FinancialAddress settles into the FinancialAccount. Required.
            """

        crypto_wallet: Optional[CryptoWallet]
        """
        Options for a crypto wallet FinancialAddress. Required if `crypto_wallet` is requested.
        """
        _inner_class_types = {"crypto_wallet": CryptoWallet}

    account: str
    """
    The ID of the Account that owns the FinancialAccount.
    """
    created: str
    """
    The creation timestamp of the FundingSession.
    """
    financial_account: str
    """
    The ID of the FinancialAccount this FundingSession funds.
    """
    financial_address_options: FinancialAddressOptions
    """
    Per-type options used when creating the FinancialAddress.
    """
    financial_address_types: List[
        Union[Literal["bank_account", "crypto_wallet"], str]
    ]
    """
    Open Enum. The types of FinancialAddress that can be funded in this session.
    """
    id: str
    """
    The ID of the FundingSession. ID prefix: `fndsess`.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["v2.money_management.funding_session"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    return_url: str
    """
    The URL the customer is redirected to after completing (or abandoning) the funding session.
    """
    url: str
    """
    The short-lived hosted funding URL the customer visits to fund the FinancialAccount.
    """
    _inner_class_types = {"financial_address_options": FinancialAddressOptions}
