# -*- coding: utf-8 -*-

from stripe._stripe_object import StripeObject
from stripe._util import sanitize_id
from typing import Optional
from typing_extensions import Literal
from typing import ClassVar


# The beginning of the section generated from our OpenAPI spec
class ThinEvent(StripeObject):
    OBJECT_NAME: ClassVar[Literal["event"]] = "event"

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

    class RelatedObject(StripeObject):
        id: str
        """
        Unique identifier for the object relevant to the event.
        """
        type: str
        """
        Type of the object relevant to the event.
        """
        url: str
        """
        URL to retrieve the resource.
        """

    created: str
    """
    Time at which the object was created.
    """
    id: str
    """
    Unique identifier for the event.
    """
    object: Literal["event"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    reason: Reason
    """
    Reason for the event.
    """
    related_object: RelatedObject
    """
    Object containing the reference to API resource relevant to the event.
    """
    type: str
    """
    The type of the event.
    """
    _inner_class_types = {"reason": Reason, "related_object": RelatedObject}

    # The end of the section generated from our OpenAPI spec
    def fetch_object(self) -> StripeObject:
        url = self.related_object.get("url")
        if url is None:
            raise ValueError(
                "Unexpected: cannot call fetch_object on an event without a 'url' field"
            )
        return self._requestor.request(
            "get",
            url,
            base_address="api",
        )

    def fetch_data(self, event_data_cls) -> StripeObject:
        full_event = self._requestor.request(
            "get",
            "/v2/events/{id}".format(id=sanitize_id(self.get("id"))),
            base_address="api",
        )
        assert isinstance(full_event, dict)
        data = full_event["data"]
        if data is None:
            raise ValueError(
                "Unexpected: fetch_data returned an event without a 'data' field"
            )
        return event_data_cls._construct_from(
            values=data, requestor=self._requestor, api_mode="V2"
        )
