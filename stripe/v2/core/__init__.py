# -*- coding: utf-8 -*-

from typing_extensions import TYPE_CHECKING
from stripe.v2.core._event import (
    EventNotification as EventNotification,
    RelatedObject as RelatedObject,
    Reason as Reason,
    ReasonRequest as ReasonRequest,
)

# The beginning of the section generated from our OpenAPI spec
from importlib import import_module

if TYPE_CHECKING:
    from stripe.v2.core import accounts as accounts, vault as vault
    from stripe.v2.core._account import Account as Account
    from stripe.v2.core._account_link import AccountLink as AccountLink
    from stripe.v2.core._account_link_service import (
        AccountLinkService as AccountLinkService,
    )
    from stripe.v2.core._account_person import AccountPerson as AccountPerson
    from stripe.v2.core._account_person_token import (
        AccountPersonToken as AccountPersonToken,
    )
    from stripe.v2.core._account_service import (
        AccountService as AccountService,
    )
    from stripe.v2.core._account_token import AccountToken as AccountToken
    from stripe.v2.core._account_token_service import (
        AccountTokenService as AccountTokenService,
    )
    from stripe.v2.core._claimable_sandbox import (
        ClaimableSandbox as ClaimableSandbox,
    )
    from stripe.v2.core._claimable_sandbox_service import (
        ClaimableSandboxService as ClaimableSandboxService,
    )
    from stripe.v2.core._event import Event as Event
    from stripe.v2.core._event_destination import (
        EventDestination as EventDestination,
    )
    from stripe.v2.core._event_destination_service import (
        EventDestinationService as EventDestinationService,
    )
    from stripe.v2.core._event_service import EventService as EventService
    from stripe.v2.core._vault_service import VaultService as VaultService

# name -> (import_target, is_submodule)
_import_map = {
    "accounts": ("stripe.v2.core.accounts", True),
    "vault": ("stripe.v2.core.vault", True),
    "Account": ("stripe.v2.core._account", False),
    "AccountLink": ("stripe.v2.core._account_link", False),
    "AccountLinkService": ("stripe.v2.core._account_link_service", False),
    "AccountPerson": ("stripe.v2.core._account_person", False),
    "AccountPersonToken": ("stripe.v2.core._account_person_token", False),
    "AccountService": ("stripe.v2.core._account_service", False),
    "AccountToken": ("stripe.v2.core._account_token", False),
    "AccountTokenService": ("stripe.v2.core._account_token_service", False),
    "ClaimableSandbox": ("stripe.v2.core._claimable_sandbox", False),
    "ClaimableSandboxService": (
        "stripe.v2.core._claimable_sandbox_service",
        False,
    ),
    "Event": ("stripe.v2.core._event", False),
    "EventDestination": ("stripe.v2.core._event_destination", False),
    "EventDestinationService": (
        "stripe.v2.core._event_destination_service",
        False,
    ),
    "EventService": ("stripe.v2.core._event_service", False),
    "VaultService": ("stripe.v2.core._vault_service", False),
}
if not TYPE_CHECKING:

    def __getattr__(name):
        try:
            target, is_submodule = _import_map[name]
            module = import_module(target)
            if is_submodule:
                return module

            return getattr(
                module,
                name,
            )
        except KeyError:
            raise AttributeError()

# The end of the section generated from our OpenAPI spec
