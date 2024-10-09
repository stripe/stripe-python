# -*- coding: utf-8 -*-

import json
from typing import ClassVar, Optional

from typing_extensions import Literal

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
        Event reason type.
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


class Reason:
    id: str
    idempotency_key: str

    def __init__(self, d) -> None:
        self.id = d["id"]
        self.idempotency_key = d["idempotency_key"]

    def __repr__(self) -> str:
        return f"<Reason id={self.id} idempotency_key={self.idempotency_key}>"


class RelatedObject:
    id: str
    type: str
    url: str

    def __init__(self, d) -> None:
        self.id = d["id"]
        self.type_ = d["type"]
        self.url = d["url"]

    def __repr__(self) -> str:
        return f"<RelatedObject id={self.id} type={self.type_} url={self.url}>"


class ThinEvent:
    """
    ThinEvent represents the json that's delivered from an Event Destination. It's a basic `dict` with no additional methods or properties. Use it to check basic information about a delivered event. If you want more details, use `stripe.v2.Event.retrieve(thin_event.id)` to fetch the full event object.
    """

    id: str
    """
    Unique identifier for the event.
    """
    type: str
    """
    The type of the event.
    """
    created: str
    """
    Livemode indicates if the event is from a production(true) or test(false) account.
    """
    livemode: bool
    """
    Time at which the object was created.
    """
    context: Optional[str] = None
    """
    [Optional] Authentication context needed to fetch the event or related object.
    """
    related_object: Optional[RelatedObject] = None
    """
    [Optional] Object containing the reference to API resource relevant to the event.
    """
    reason: Optional[Reason] = None
    """
    [Optional] Reason for the event.
    """

    def __init__(self, payload: str) -> None:
        parsed = json.loads(payload)

        self.id = parsed["id"]
        self.type = parsed["type"]
        self.created = parsed["created"]
        self.livemode = parsed.get("livemode")
        self.context = parsed.get("context")
        if parsed.get("related_object"):
            self.related_object = RelatedObject(parsed["related_object"])
        if parsed.get("reason"):
            self.reason = Reason(parsed["reason"])

    def __repr__(self) -> str:
        return f"<ThinEvent id={self.id} type={self.type} created={self.created} context={self.context} related_object={self.related_object} reason={self.reason}>"
