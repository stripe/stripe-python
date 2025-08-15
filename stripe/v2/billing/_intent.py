# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Optional
from typing_extensions import Literal


class Intent(StripeObject):
    OBJECT_NAME: ClassVar[Literal["v2.billing.intent"]] = "v2.billing.intent"

    class AmountDetails(StripeObject):
        currency: str
        """
        Three-letter ISO currency code, in lowercase.
        """
        discount: str
        """
        Amount of discount applied.
        """
        shipping: str
        """
        Amount of shipping charges.
        """
        subtotal: str
        """
        Subtotal amount before tax and discounts.
        """
        tax: str
        """
        Amount of tax.
        """
        total: str
        """
        Total amount for the BillingIntent.
        """

    class StatusTransitions(StripeObject):
        canceled_at: Optional[str]
        """
        Time at which the BillingIntent was canceled.
        """
        committed_at: Optional[str]
        """
        Time at which the BillingIntent was committed.
        """
        drafted_at: Optional[str]
        """
        Time at which the BillingIntent was drafted.
        """
        reserved_at: Optional[str]
        """
        Time at which the BillingIntent was reserved.
        """

    amount_details: AmountDetails
    """
    Breakdown of the amount for this BillingIntent.
    """
    cadence: Optional[str]
    """
    ID of an existing Cadence to use.
    """
    created: str
    """
    Time at which the object was created.
    """
    currency: str
    """
    Three-letter ISO currency code, in lowercase.
    """
    effective_at: Literal[
        "current_billing_period_start", "on_commit", "on_reserve"
    ]
    """
    When the BillingIntent will take effect.
    """
    id: str
    """
    Unique identifier for the BillingIntent.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["v2.billing.intent"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    status: Literal["canceled", "committed", "draft", "reserved"]
    """
    Current status of the BillingIntent.
    """
    status_transitions: StatusTransitions
    """
    Timestamps for status transitions of the BillingIntent.
    """
    _inner_class_types = {
        "amount_details": AmountDetails,
        "status_transitions": StatusTransitions,
    }
