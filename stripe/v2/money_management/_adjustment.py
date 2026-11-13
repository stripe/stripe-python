# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from stripe.v2._amount import Amount
from typing import ClassVar, Optional, Union
from typing_extensions import Literal


class Adjustment(StripeObject):
    """
    An Adjustment records a credit or debit that Stripe makes to your Financial Account balance,
    for example to correct technical or operational errors.
    """

    OBJECT_NAME: ClassVar[Literal["v2.money_management.adjustment"]] = (
        "v2.money_management.adjustment"
    )

    class AdjustedFlow(StripeObject):
        adjustment: Optional[str]
        """
        If applicable, the ID of the original Adjustment linked to this Adjustment.
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
        type: Union[
            Literal[
                "adjustment",
                "inbound_transfer",
                "outbound_payment",
                "outbound_transfer",
                "received_credit",
                "received_debit",
            ],
            str,
        ]
        """
        Open Enum. If applicable, the type of flow linked to this Adjustment. The field matching this value will contain the ID of the flow.
        """

    adjusted_flow: Optional[AdjustedFlow]
    """
    Details about the original flow object linked to this Adjustment, if applicable.
    `adjusted_flow.type` identifies the kind of object. The corresponding field contains its ID:
    for an InboundTransfer, `adjusted_flow.inbound_transfer` contains the InboundTransfer's ID.
    Pass that ID to the `adjusted_flow` parameter on List Adjustments.
    """
    amount: Amount
    """
    The amount of the Adjustment.
    """
    created: str
    """
    Time at which the object was created. Represented as an RFC 3339 timestamp in UTC with millisecond precision,
    for example `2022-09-18T13:22:18.123Z`.
    """
    description: Optional[str]
    """
    A description of the Adjustment and its purpose.
    """
    financial_account: str
    """
    The ID of the FinancialAccount whose balance this Adjustment affects.
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
    _inner_class_types = {"adjusted_flow": AdjustedFlow}
