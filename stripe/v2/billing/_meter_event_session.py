# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar
from typing_extensions import Literal


class MeterEventSession(StripeObject):
    OBJECT_NAME: ClassVar[Literal["billing.meter_event_session"]] = (
        "billing.meter_event_session"
    )
    authentication_token: str
    """
    The authentication token for this session.  Use this token when calling the
    high-throughput meter event API.
    """
    created: str
    """
    The creation time of this session.
    """
    expires_at: str
    """
    The time at which this session will expire.
    """
    id: str
    """
    The unique id of this auth session.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["billing.meter_event_session"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
