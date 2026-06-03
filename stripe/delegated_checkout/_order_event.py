# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, List, Optional
from typing_extensions import Literal


class OrderEvent(StripeObject):
    """
    An order event represents a change to a delegated checkout order.
    """

    OBJECT_NAME: ClassVar[Literal["delegated_checkout.order_event"]] = (
        "delegated_checkout.order_event"
    )

    class Adjustment(StripeObject):
        class LineItem(StripeObject):
            key: str
            """
            The line item key.
            """
            quantity: int
            """
            The quantity associated with the order event.
            """

        amount: Optional[int]
        """
        The amount associated with the adjustment.
        """
        currency: Optional[str]
        """
        The currency associated with the adjustment amount.
        """
        description: str
        """
        The description of the adjustment.
        """
        line_items: Optional[List[LineItem]]
        """
        The line items associated with the adjustment.
        """
        status: Literal["completed", "failed", "pending"]
        """
        The status of the adjustment.
        """
        type: Literal[
            "cancellation",
            "credit",
            "dispute",
            "original_payment_refund",
            "return",
            "store_credit_refund",
        ]
        """
        The type of adjustment.
        """
        _inner_class_types = {"line_items": LineItem}

    class Fulfillment(StripeObject):
        class LineItem(StripeObject):
            key: str
            """
            The line item key.
            """
            quantity: int
            """
            The quantity associated with the order event.
            """

        carrier: Optional[str]
        """
        The carrier for the fulfillment.
        """
        delivered_at: Optional[int]
        """
        Time at which the fulfillment was delivered. Measured in seconds since the Unix epoch.
        """
        line_items: List[LineItem]
        """
        The line items associated with the fulfillment.
        """
        shipped_at: Optional[int]
        """
        Time at which the fulfillment shipped. Measured in seconds since the Unix epoch.
        """
        status: Literal[
            "confirmed",
            "delivered",
            "fulfilled",
            "pending",
            "returned",
            "shipped",
        ]
        """
        The status of the fulfillment.
        """
        tracking_number: Optional[str]
        """
        The tracking number for the fulfillment.
        """
        tracking_url: Optional[str]
        """
        The tracking URL for the fulfillment.
        """
        _inner_class_types = {"line_items": LineItem}

    adjustment: Optional[Adjustment]
    """
    The adjustment details for this order event.
    """
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    fulfillment: Optional[Fulfillment]
    """
    The fulfillment details for this order event.
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.
    """
    object: Literal["delegated_checkout.order_event"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    occurred_at: int
    """
    Time at which this event occurred. Measured in seconds since the Unix epoch.
    """
    order: str
    """
    The delegated checkout order associated with this order event.
    """
    requested_session: str
    """
    The requested session associated with this order event.
    """
    type: Literal["adjustment", "fulfillment"]
    """
    The type of order event.
    """
    _inner_class_types = {"adjustment": Adjustment, "fulfillment": Fulfillment}
