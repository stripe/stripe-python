# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from stripe.sigma._scheduled_query_run import ScheduledQueryRun
from stripe.v2._event import Event
from typing import cast
from typing_extensions import Literal


class V1SigmaScheduledQueryRunCreatedEvent(Event):
    LOOKUP_TYPE = "v1.sigma.scheduled_query_run.created"
    type: Literal["v1.sigma.scheduled_query_run.created"]

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

    related_object: RelatedObject
    """
    Object containing the reference to API resource relevant to the event
    """

    def fetch_related_object(self) -> ScheduledQueryRun:
        """
        Retrieves the related object from the API. Makes an API request on every call.
        """
        return cast(
            ScheduledQueryRun,
            self._requestor.request(
                "get",
                self.related_object.url,
                base_address="api",
                options={"stripe_account": self.context},
            ),
        )
