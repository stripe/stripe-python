# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject, UntypedStripeObject
from stripe.v2._amount import Amount
from typing import ClassVar, Optional, Union
from typing_extensions import Literal


class Dispute(StripeObject):
    """
    A Dispute tracks a claim challenging a money movement on behalf of a FinancialAccount holder.
    """

    OBJECT_NAME: ClassVar[Literal["v2.money_management.dispute"]] = (
        "v2.money_management.dispute"
    )

    class StatusTransitions(StripeObject):
        lost_at: Optional[str]
        """
        The time at which the Dispute became lost. Only present if status == lost.
        """
        won_at: Optional[str]
        """
        The time at which the Dispute became won. Only present if status == won.
        """

    class Target(StripeObject):
        received_debit: Optional[str]
        """
        If applicable, the ID of the ReceivedDebit being disputed.
        """
        type: Union[Literal["received_debit"], str]
        """
        The type of money movement being disputed.
        """

    amount: Amount
    """
    The amount and currency of the disputed money movement.
    """
    created: str
    """
    The time at which the dispute was created.
    """
    explanation: Optional[str]
    """
    Additional explanation for the dispute, if supplied.
    """
    financial_account: str
    """
    The FinancialAccount associated with the disputed money movement.
    """
    id: str
    """
    Unique identifier for the Dispute.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: Optional[UntypedStripeObject[str]]
    """
    Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: Literal["v2.money_management.dispute"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    reason: Union[
        Literal[
            "authorization_revoked",
            "duplicate",
            "incorrect_amount",
            "incorrect_date",
            "other",
            "unauthorized",
        ],
        str,
    ]
    """
    The FinancialAccount holder's reason for disputing the money movement.
    """
    status: Union[Literal["lost", "under_review", "won"], str]
    """
    The current status of the dispute.
    """
    status_transitions: Optional[StatusTransitions]
    """
    Timestamps describing when the dispute changed status.
    """
    target: Target
    """
    The money movement being disputed.
    """
    _inner_class_types = {
        "status_transitions": StatusTransitions,
        "target": Target,
    }
