# -*- coding: utf-8 -*-

from typing import ClassVar, Optional

from typing_extensions import Literal, TypedDict

from stripe._stripe_object import StripeObject

# This describes the common format for the pull payload of a V2 ThinEvent
# more specific classes will add `data` and `fetch_related_objects()` as needed


# The beginning of the section generated from our OpenAPI spec
class Event(StripeObject):
    OBJECT_NAME: ClassVar[Literal["v2.core.event"]] = "v2.core.event"

    class Reason(StripeObject):
        class Request(StripeObject):
            id: str
            """
            ID of the API request that caused the event.
            """
            idempotency_key: str
            """
            The idempotency key transmitted during the request.
            """

        type: Literal["request"]
        """
        Open Enum. Event reason type.
        """
        request: Optional[Request]
        """
        Information on the API request that instigated the event.
        """
        _inner_class_types = {"request": Request}

    context: Optional[str]
    """
    Authentication context needed to fetch the event or related object.
    """
    created: str
    """
    Time at which the object was created.
    """
    id: str
    """
    Unique identifier for the event.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["v2.core.event"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    reason: Optional[Reason]
    """
    Reason for the event.
    """
    type: str
    """
    The type of the event.
    """
    _inner_class_types = {"reason": Reason}


# The end of the section generated from our OpenAPI spec


class Reason(TypedDict):
    id: str
    idempotency_key: str


class RelatedObject(TypedDict):
    id: str
    type: str
    url: str


class ThinEvent(TypedDict):
    """
    ThinEvent represents the json that's delivered from an Event Destination. It's a basic `dict` with no additional methods or properties. Use it to check basic information about a delivered event. If you want more details, use `stripe.v2.Event.retrieve(thin_event["id"])` to fetch the full event object.
    """

    id: str
    type: str
    created: str
    context: Optional[str]
    related_object: Optional[RelatedObject]
    reason: Optional[Reason]
