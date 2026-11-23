# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from stripe.v2._amount import Amount
from typing import ClassVar, Optional, Union
from typing_extensions import Literal


class DisputeAdjustment(StripeObject):
    """
    A DisputeAdjustment records a money movement associated with a Dispute.
    """

    OBJECT_NAME: ClassVar[
        Literal["v2.money_management.dispute_adjustment"]
    ] = "v2.money_management.dispute_adjustment"

    class RelatedDispute(StripeObject):
        dispute: Optional[str]
        """
        The ID of the Dispute associated with this DisputeAdjustment. Present when `type` is `dispute`.
        """
        type: Union[Literal["dispute"], str]
        """
        The type of Dispute associated with this DisputeAdjustment.
        """

    amount: Amount
    """
    The amount and currency of the DisputeAdjustment.
    """
    created: str
    """
    The time at which the DisputeAdjustment was created.
    """
    financial_account: str
    """
    The ID of the FinancialAccount associated with the DisputeAdjustment.
    """
    id: str
    """
    Unique identifier for the DisputeAdjustment.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["v2.money_management.dispute_adjustment"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    related_dispute: RelatedDispute
    """
    The Dispute associated with this DisputeAdjustment.
    """
    _inner_class_types = {"related_dispute": RelatedDispute}
