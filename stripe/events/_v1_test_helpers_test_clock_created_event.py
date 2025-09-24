# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from stripe.test_helpers._test_clock import TestClock
from stripe.v2._event import Event
from typing import cast
from typing_extensions import Literal


class V1TestHelpersTestClockCreatedEvent(Event):
    LOOKUP_TYPE = "v1.test_helpers.test_clock.created"
    type: Literal["v1.test_helpers.test_clock.created"]

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

    def fetch_related_object(self) -> TestClock:
        """
        Retrieves the related object from the API. Makes an API request on every call.
        """
        return cast(
            TestClock,
            self._requestor.request(
                "get",
                self.related_object.url,
                base_address="api",
                options={"stripe_account": self.context},
            ),
        )
