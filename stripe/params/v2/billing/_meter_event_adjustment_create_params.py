# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import Literal, TypedDict


class MeterEventAdjustmentCreateParams(TypedDict):
    cancel: "MeterEventAdjustmentCreateParamsCancel"
    """
    Specifies which event to cancel.
    """
    event_name: str
    """
    The name of the meter event. Corresponds with the `event_name` field on a meter.
    """
    type: Literal["cancel"]
    """
    Specifies the type of cancellation. Currently supports canceling a single event.
    """


class MeterEventAdjustmentCreateParamsCancel(TypedDict):
    identifier: str
    """
    The identifier that was originally assigned to the meter event. You can only cancel events within 24 hours of Stripe receiving them.
    """
