# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._expandable_field import ExpandableField
from stripe._stripe_object import StripeObject
from typing import ClassVar, Optional
from typing_extensions import Literal, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._customer import Customer
    from stripe.billing._meter import Meter


class Alert(StripeObject):
    """
    A billing alert is a resource that notifies you when a certain usage threshold on a meter is crossed. For example, you might create a billing alert to notify you when a certain user made 100 API requests.
    """

    OBJECT_NAME: ClassVar[Literal["billing.alert"]] = "billing.alert"

    class Filter(StripeObject):
        customer: Optional[ExpandableField["Customer"]]
        """
        Limit the scope of the alert to this customer ID
        """

    class UsageThresholdConfig(StripeObject):
        gte: int
        """
        The value at which this alert will trigger.
        """
        meter: ExpandableField["Meter"]
        """
        The [Billing Meter](https://stripe.com/api/billing/meter) ID whose usage is monitored.
        """
        recurrence: Literal["one_time"]
        """
        Defines how the alert will behave.
        """

    alert_type: Literal["usage_threshold"]
    """
    Defines the type of the alert.
    """
    filter: Optional[Filter]
    """
    Limits the scope of the alert to a specific [customer](https://stripe.com/docs/api/customers).
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["billing.alert"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    status: Optional[Literal["active", "archived", "inactive"]]
    """
    Status of the alert. This can be active, inactive or archived.
    """
    title: str
    """
    Title of the alert.
    """
    usage_threshold_config: Optional[UsageThresholdConfig]
    """
    Encapsulates configuration of the alert to monitor usage on a specific [Billing Meter](https://stripe.com/docs/api/billing/meter).
    """
    _inner_class_types = {
        "filter": Filter,
        "usage_threshold_config": UsageThresholdConfig,
    }
