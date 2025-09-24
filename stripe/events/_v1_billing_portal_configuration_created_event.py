# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from stripe.billing_portal._configuration import Configuration
from stripe.v2._event import Event
from typing import cast
from typing_extensions import Literal


class V1BillingPortalConfigurationCreatedEvent(Event):
    LOOKUP_TYPE = "v1.billing_portal.configuration.created"
    type: Literal["v1.billing_portal.configuration.created"]

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

    def fetch_related_object(self) -> Configuration:
        """
        Retrieves the related object from the API. Makes an API request on every call.
        """
        return cast(
            Configuration,
            self._requestor.request(
                "get",
                self.related_object.url,
                base_address="api",
                options={"stripe_account": self.context},
            ),
        )
