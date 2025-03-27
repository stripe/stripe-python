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

    class UsageStatus(StripeObject):
        payments: Literal["eligible", "invalid", "requires_action"]
        """
        Payments status.
        """
        transfers: Literal["eligible", "invalid", "requires_action"]
        """
        Transfers status.
        """

    class BankAccount(StripeObject):
        archived: bool
        """
        Whether this PayoutMethodBankAccount object was archived. PayoutMethodBankAccount objects can be archived through
        the /archive API, and they will not be automatically archived by Stripe. Archived PayoutMethodBankAccount objects
        cannot be used as payout methods and will not appear in the payout method list.
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

    available_payout_speeds: List[Literal["instant", "standard"]]
    """
    A set of available payout speeds for this payout method.
    """
    created: str
    """
    Created timestamp.
    """
    id: str
    """
    ID of the PayoutMethod object.
    """
    latest_outbound_setup_intent: Optional[str]
    """
    ID of the underlying active OutboundSetupIntent object, if any.
    """
    object: Literal["v2.money_management.payout_method"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    type: Literal["bank_account", "card"]
    """
    Closed Enum. The type of payout method.
    """
    usage_status: UsageStatus
    """
    Indicates whether the payout method has met the necessary requirements for outbound money movement.
    """
    bank_account: Optional[BankAccount]
    """
    The PayoutMethodBankAccount object details.
    """
    card: Optional[Card]
    """
    The PayoutMethodCard object details.
    """
    _inner_class_types = {
        "usage_status": UsageStatus,
        "bank_account": BankAccount,
        "card": Card,
    }
