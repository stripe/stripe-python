# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe.v2.core._event_destination_service import EventDestinationService
from stripe.v2.core._event_service import EventService


class CoreService(StripeService):
    def __init__(self, requestor):
        super().__init__(requestor)
        self.events = EventService(self._requestor)
        self.event_destinations = EventDestinationService(self._requestor)
