# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from stripe.v2._amount import Amount
from typing import ClassVar, Optional
from typing_extensions import Literal


class Adjustment(StripeObject):
    """
    Adjustments represent Stripe-initiated credits or debits to a user balance. They might be used to amend balances due to technical or operational error.
    """

    OBJECT_NAME: ClassVar[Literal["v2.money_management.adjustment"]] = (
        "v2.money_management.adjustment"
    )

    class AdjustedFlow(StripeObject):
        adjustment: Optional[str]
        """
        If applicable, the ID of the Adjustment linked to this Adjustment.
        """
        inbound_transfer: Optional[str]
        """
        If applicable, the ID of the InboundTransfer linked to this Adjustment.
        """
        outbound_payment: Optional[str]
        """
        If applicable, the ID of the OutboundPayment linked to this Adjustment.
        """
        outbound_transfer: Optional[str]
        """
        If applicable, the ID of the OutboundTransfer linked to this Adjustment.
        """
        received_credit: Optional[str]
        """
        If applicable, the ID of the ReceivedCredit linked to this Adjustment.
        """
        received_debit: Optional[str]
        """
        If applicable, the ID of the ReceivedDebit linked to this Adjustment.
        """
        type: Literal[
            "adjustment",
            "balance_exchange",
            "inbound_payment",
            "inbound_transfer",
            "outbound_payment",
            "outbound_transfer",
            "received_credit",
            "received_debit",
        ]
        """
        Closed Enum. If applicable, the type of flow linked to this Adjustment. The field matching this value will contain the ID of the flow.
        """

    adjusted_flow: Optional[AdjustedFlow]
    """
    If applicable, contains information about the original flow linked to this Adjustment.
    """
    amount: Amount
    """
    The amount of the Adjustment.
    """
    created: str
    """
    Time at which the object was created. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
    """
    description: Optional[str]
    """
    Description of the Adjustment and what it was used for.
    """
    financial_account: str
    """
    The FinancialAccount that this adjustment is for.
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["v2.money_management.adjustment"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    receipt_url: Optional[str]
    """
    A link to the Stripe-hosted receipt that is provided when money movement is considered regulated under Stripe's money transmission licenses. The receipt link remains active for 60 days from the Adjustment creation date. After this period, the link will expire and the receipt url value will be null.
    """
    _inner_class_types = {"adjusted_flow": AdjustedFlow}
