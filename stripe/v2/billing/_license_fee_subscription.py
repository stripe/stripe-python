# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Dict, Optional
from typing_extensions import Literal


class LicenseFeeSubscription(StripeObject):
    """
    A License Fee Subscription represents a customer's subscription to a License Fee at a specified quantity. It tracks
    the number of units (such as seats or licenses) the customer has subscribed to and bills them according to the service
    interval defined in the License Fee and the Billing Cadence.
    """

    OBJECT_NAME: ClassVar[Literal["v2.billing.license_fee_subscription"]] = (
        "v2.billing.license_fee_subscription"
    )
    billing_cadence: str
    """
    The ID of the Billing Cadence.
    """
    created: str
    """
    Timestamp of when the object was created.
    """
    id: str
    """
    Unique identifier for the object.
    """
    license_fee: str
    """
    The ID of the License Fee.
    """
    license_fee_version: str
    """
    The ID of the License Fee Version.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: Optional[Dict[str, str]]
    """
    Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: Literal["v2.billing.license_fee_subscription"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    quantity: int
    """
    Quantity of the License Fee subscribed to.
    """
    test_clock: Optional[str]
    """
    The ID of the Test Clock, if any.
    """
