# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Optional
from typing_extensions import Literal


class FeedbackOptions(StripeObject):
    """
    A resource for the feedback options model (for custom cancellation reasons)
    """

    OBJECT_NAME: ClassVar[Literal["billing.feedback_options"]] = (
        "billing.feedback_options"
    )

    class StatusTransitions(StripeObject):
        deactivated_at: Optional[int]
        """
        The time the feedback option was deactivated, if any. Measured in seconds since Unix epoch.
        """

    description: str
    """
    An arbitrary string attached to the object. Often useful for displaying to users.
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.
    """
    object: Literal["billing.feedback_options"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    status: Literal["active", "inactive"]
    """
    The feedback option's status.
    """
    status_transitions: StatusTransitions
    _inner_class_types = {"status_transitions": StatusTransitions}
