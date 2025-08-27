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
        Three-letter ISO currency code, in lowercase. Must be a supported currency.
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
        Total amount for the Billing Intent.
        """

    class StatusTransitions(StripeObject):
        canceled_at: Optional[str]
        """
        Time at which the Billing Intent was canceled.
        """
        committed_at: Optional[str]
        """
        Time at which the Billing Intent was committed.
        """
        drafted_at: Optional[str]
        """
        Time at which the Billing Intent was drafted.
        """
        reserved_at: Optional[str]
        """
        Time at which the Billing Intent was reserved.
        """

    amount_details: AmountDetails
    """
    Breakdown of the amount for this Billing Intent.
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
    Three-letter ISO currency code, in lowercase. Must be a supported currency.
    """
    id: str
    """
    Unique identifier for the object.
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
    Current status of the Billing Intent.
    """
    status_transitions: StatusTransitions
    """
    Timestamps for status transitions of the Billing Intent.
    """
    _inner_class_types = {
        "amount_details": AmountDetails,
        "status_transitions": StatusTransitions,
    }
