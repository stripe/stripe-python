# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe.delegated_checkout._requested_session_service import (
    RequestedSessionService,
)


class DelegatedCheckoutService(StripeService):
    def __init__(self, requestor):
        super().__init__(requestor)
        self.requested_sessions = RequestedSessionService(self._requestor)
