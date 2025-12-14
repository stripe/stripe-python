# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Optional
from typing_extensions import Literal


class SettlementAllocationIntentSplit(StripeObject):
    """
    SettlementAllocationIntentSplit resource.
    """

    OBJECT_NAME: ClassVar[
        Literal["v2.payments.settlement_allocation_intent_split"]
    ] = "v2.payments.settlement_allocation_intent_split"

    class Amount(StripeObject):
        currency: Optional[str]
        """
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
        """
        value: Optional[int]
        """
        A non-negative integer representing how much to charge in the [smallest currency unit](https://docs.stripe.com/currencies#minor-units).
        """

    class Flow(StripeObject):
        outbound_payment: Optional[str]
        """
        If applicable, the ID of the OutboundPayment that created this transaction.
        """
        outbound_transfer: Optional[str]
        """
        If applicable, the ID of the OutboundTransfer that created this transaction.
        """
        received_credit: Optional[str]
        """
        If applicable, the ID of the ReceivedCredit that created this transaction.
        """
        type: Literal[
            "outbound_payment", "outbound_transfer", "received_credit"
        ]
        """
        Type of the flow linked to the transaction which settled the SettlementAllocationIntentSplit. The field matching this value will contain the ID of the flow.
        """

    account: str
    """
    The account id against which the SettlementAllocationIntentSplit should be settled.
    """
    amount: Amount
    """
    The amount and currency of the SettlementAllocationIntentSplit.
    """
    created: str
    """
    Timestamp at which SettlementAllocationIntentSplit was created.
    """
    flow: Flow
    """
    Details about the Flow object that settled the split.
    """
    id: str
    """
    Unique identifier for the SettlementAllocationIntentSplit.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["v2.payments.settlement_allocation_intent_split"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    settlement_allocation_intent: str
    """
    The ID of the SettlementAllocationIntent that this split belongs too.
    """
    status: Literal["canceled", "pending", "settled"]
    """
    The status of the SettlementAllocationIntentSplit.
    """
    type: Literal["credit", "debit"]
    """
    The type of the SettlementAllocationIntentSplit.
    """
    _inner_class_types = {"amount": Amount, "flow": Flow}
