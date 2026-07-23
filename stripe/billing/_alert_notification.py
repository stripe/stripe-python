# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Optional, Union
from typing_extensions import Literal


class AlertNotification(StripeObject):
    OBJECT_NAME: ClassVar[Literal["billing.alert_notification"]] = (
        "billing.alert_notification"
    )
    action: Union[Literal["recovered", "triggered"], str]
    """
    Whether the alert was triggered or recovered.
    """
    aggregation_period_end: Optional[int]
    """
    End of the aggregation period for which this notification was sent. Only present for usage threshold alerts.
    """
    aggregation_period_start: Optional[int]
    """
    Start of the aggregation period for which this notification was sent. Only present for usage threshold alerts.
    """
    alert: str
    """
    ID of the billing alert that generated this notification.
    """
    alert_type: Union[
        Literal[
            "credit_balance_threshold", "spend_threshold", "usage_threshold"
        ],
        str,
    ]
    """
    The type of billing alert that generated this notification.
    """
    cadence: Optional[str]
    """
    The billing cadence associated with this notification. Only present for spend threshold alerts grouped by billing cadence.
    """
    currency: Optional[str]
    """
    Three-letter ISO currency code for the value, in lowercase. Only present for spend and credit balance threshold alerts.
    """
    custom_pricing_unit: Optional[str]
    """
    Custom pricing unit for the threshold value
    """
    customer: str
    """
    ID of the customer for which the alert notification was sent.
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.
    """
    meter: Optional[str]
    """
    ID of the billing meter associated with this notification. Only present for usage threshold alerts.
    """
    notification_event: str
    """
    ID of the event delivered for this notification. Retrievable via the Events API for a limited time; for long-term audit scenarios, capture the full event payload at webhook delivery time.
    """
    notified_at: int
    """
    Time at which the notification was sent. Measured in seconds since the Unix epoch.
    """
    object: Literal["billing.alert_notification"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    subscription: Optional[str]
    """
    ID of the subscription associated with this notification. Only present for spend threshold alerts grouped by subscription.
    """
    value: str
    """
    The value that triggered the alert. This may be a decimal string for custom pricing unit alerts. For usage threshold alerts, this is the meter event count. For credit balance and spend threshold alerts, this is the amount in the smallest currency unit.
    """
