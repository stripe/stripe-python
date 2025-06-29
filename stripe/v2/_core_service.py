# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe.v2.core._account_link_service import AccountLinkService
from stripe.v2.core._account_service import AccountService
from stripe.v2.core._event_destination_service import EventDestinationService
from stripe.v2.core._event_service import EventService
from stripe.v2.core._vault_service import VaultService


class CoreService(StripeService):
    def __init__(self, requestor):
        super().__init__(requestor)
        self.account_links = AccountLinkService(self._requestor)
        self.accounts = AccountService(self._requestor)
        self.event_destinations = EventDestinationService(self._requestor)
        self.events = EventService(self._requestor)
        self.vault = VaultService(self._requestor)
