# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.v2.core._account_link_service import AccountLinkService
    from stripe.v2.core._account_service import AccountService
    from stripe.v2.core._claimable_sandbox_service import (
        ClaimableSandboxService,
    )
    from stripe.v2.core._event_destination_service import (
        EventDestinationService,
    )
    from stripe.v2.core._event_service import EventService
    from stripe.v2.core._vault_service import VaultService

_subservices = {
    "accounts": ["stripe.v2.core._account_service", "AccountService"],
    "account_links": [
        "stripe.v2.core._account_link_service",
        "AccountLinkService",
    ],
    "claimable_sandboxes": [
        "stripe.v2.core._claimable_sandbox_service",
        "ClaimableSandboxService",
    ],
    "events": ["stripe.v2.core._event_service", "EventService"],
    "event_destinations": [
        "stripe.v2.core._event_destination_service",
        "EventDestinationService",
    ],
    "vault": ["stripe.v2.core._vault_service", "VaultService"],
}


class CoreService(StripeService):
    accounts: "AccountService"
    account_links: "AccountLinkService"
    claimable_sandboxes: "ClaimableSandboxService"
    events: "EventService"
    event_destinations: "EventDestinationService"
    vault: "VaultService"

    def __init__(self, requestor):
        super().__init__(requestor)

    def __getattr__(self, name):
        try:
            import_from, service = _subservices[name]
            service_class = getattr(
                import_module(import_from),
                service,
            )
            setattr(
                self,
                name,
                service_class(self._requestor),
            )
            return getattr(self, name)
        except KeyError:
            raise AttributeError()
