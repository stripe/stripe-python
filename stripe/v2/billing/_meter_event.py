# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Dict
from typing_extensions import Literal


class MeterEvent(StripeObject):
    """
    Fix me empty_doc_string.
    """

    OBJECT_NAME: ClassVar[Literal["billing.meter_event"]] = (
        "billing.meter_event"
    )
    created: str
    """
    The creation time of this meter event.
    """
    event_name: str
    """
    The name of the meter event. Corresponds with the `event_name` field on a meter.
    """
    identifier: str
    """
    A unique identifier for the event. If not provided, one will be generated. We recommend using a globally unique identifier for this. We'll enforce uniqueness within a rolling 24 hour period.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["billing.meter_event"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    payload: Dict[str, str]
    """
    The payload of the event. This must contain the fields corresponding to a meter's
    `customer_mapping.event_payload_key` (default is `stripe_customer_id`) and
    `value_settings.event_payload_key` (default is `value`). Read more about the payload.
    """
    timestamp: str
    """
    The time of the event. Must be within the past 35 calendar days or up to
    5 minutes in the future. Defaults to current timestamp if not specified.
    """
