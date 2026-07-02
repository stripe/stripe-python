# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Optional
from typing_extensions import Literal


class CustomerPaymentToken(StripeObject):
    """
    A read-only representation of a user's PaymentMethod for use in Crypto On Ramp transactions.
    """

    OBJECT_NAME: ClassVar[Literal["crypto.payment_token"]] = (
        "crypto.payment_token"
    )

    class Card(StripeObject):
        class Wallet(StripeObject):
            type: Literal["apple_pay", "google_pay"]
            """
            The type of the card wallet, one of `apple_pay` or `google_pay`.
            """

        brand: Optional[str]
        """
        Card brand. Can be `amex`, `cartes_bancaires`, `diners`, `discover`, `eftpos_au`, `jcb`, `link`, `mastercard`, `unionpay`, `visa` or `unknown`.
        """
        exp_month: Optional[int]
        """
        Two-digit number representing the card's expiration month.
        """
        exp_year: Optional[int]
        """
        Four-digit number representing the card's expiration year.
        """
        funding: str
        """
        Card funding type. Can be `credit`, `debit`, `prepaid`, or `unknown`.
        """
        last4: Optional[str]
        """
        The last four digits of the card.
        """
        wallet: Optional[Wallet]
        """
        If this Card is part of a card wallet, this contains the details of the card wallet.
        """
        _inner_class_types = {"wallet": Wallet}

    class UsBankAccount(StripeObject):
        account_type: Optional[Literal["checking", "savings"]]
        """
        Account type: `checkings` or `savings`.
        """
        bank_name: Optional[str]
        """
        The name of the bank.
        """
        last4: Optional[str]
        """
        Last four digits of the bank account number.
        """

    card: Optional[Card]
    """
    A `card` PaymentToken, this hash contains details of the card PaymentToken.
    """
    id: str
    """
    Unique identifier for the object.
    """
    object: Literal["crypto.payment_token"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    type: Literal["card", "us_bank_account"]
    """
    Type of the Payment Token.
    """
    us_bank_account: Optional[UsBankAccount]
    """
    A `us_bank_account` PaymentToken, this hash contains details of the US bank account PaymentToken.
    """
    _inner_class_types = {"card": Card, "us_bank_account": UsBankAccount}
