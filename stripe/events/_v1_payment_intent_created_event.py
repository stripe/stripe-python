# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._payment_intent import PaymentIntent
from stripe._stripe_object import StripeObject
from stripe.v2._event import Event
from typing import cast
from typing_extensions import Literal


class V1PaymentIntentCreatedEvent(Event):
    LOOKUP_TYPE = "v1.payment_intent.created"
    type: Literal["v1.payment_intent.created"]

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

    def fetch_related_object(self) -> PaymentIntent:
        """
        Retrieves the related object from the API. Makes an API request on every call.
        """
        return cast(
            PaymentIntent,
            self._requestor.request(
                "get",
                self.related_object.url,
                base_address="api",
                options={"stripe_account": self.context},
            ),
        )
