# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Optional
from typing_extensions import Literal, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.billing._alert import Alert


class AlertTriggered(StripeObject):
    OBJECT_NAME: ClassVar[Literal["billing.alert_triggered"]] = (
        "billing.alert_triggered"
    )
    alert: "Alert"
    """
    A billing alert is a resource that notifies you when a certain usage threshold on a meter is crossed. For example, you might create a billing alert to notify you when a certain user made 100 API requests.
    """
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    currency: Optional[str]
    """
    Currency for the threshold value
    """
    custom_pricing_unit: Optional[str]
    """
    Custom pricing unit for the threshold value
    """
    customer: str
    """
    ID of customer for which the alert triggered
    """
    external_customer_id: Optional[str]
    """
    External customer ID for the customer for which the alert triggered
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["billing.alert_triggered"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    value: str
    """
    The value triggering the alert
    """
