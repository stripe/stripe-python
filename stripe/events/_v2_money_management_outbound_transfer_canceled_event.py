# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from stripe.v2._event import Event
from stripe.v2._outbound_transfer import OutboundTransfer
from typing import cast
from typing_extensions import Literal


class V2MoneyManagementOutboundTransferCanceledEvent(Event):
    LOOKUP_TYPE = "v2.money_management.outbound_transfer.canceled"
    type: Literal["v2.money_management.outbound_transfer.canceled"]

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

    def fetch_related_object(self) -> OutboundTransfer:
        """
        Retrieves the related object from the API. Makes an API request on every call.
        """
        return cast(
            OutboundTransfer,
            self._requestor.request(
                "get",
                self.related_object.url,
                base_address="api",
                options={"stripe_account": self.context},
            ),
        )
