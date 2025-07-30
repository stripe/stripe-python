# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe.terminal._configuration_service import ConfigurationService
from stripe.terminal._connection_token_service import ConnectionTokenService
from stripe.terminal._location_service import LocationService
from stripe.terminal._onboarding_link_service import OnboardingLinkService
from stripe.terminal._reader_collected_data_service import (
    ReaderCollectedDataService,
)
from stripe.terminal._reader_service import ReaderService


class TerminalService(StripeService):
    def __init__(self, requestor):
        super().__init__(requestor)
        self.configurations = ConfigurationService(self._requestor)
        self.connection_tokens = ConnectionTokenService(self._requestor)
        self.locations = LocationService(self._requestor)
        self.onboarding_links = OnboardingLinkService(self._requestor)
        self.readers = ReaderService(self._requestor)
        self.reader_collected_data = ReaderCollectedDataService(
            self._requestor
        )
