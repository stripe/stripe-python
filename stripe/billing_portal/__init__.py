# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.billing_portal._configuration import (
        Configuration as Configuration,
    )
    from stripe.billing_portal._configuration_service import (
        ConfigurationService as ConfigurationService,
    )
    from stripe.billing_portal._session import Session as Session
    from stripe.billing_portal._session_service import (
        SessionService as SessionService,
    )

_submodules = {
    "Configuration": "stripe.billing_portal._configuration",
    "ConfigurationService": "stripe.billing_portal._configuration_service",
    "Session": "stripe.billing_portal._session",
    "SessionService": "stripe.billing_portal._session_service",
}
if not TYPE_CHECKING:

    def __getattr__(name):
        try:
            return getattr(
                import_module(_submodules[name]),
                name,
            )
        except KeyError:
            raise AttributeError(f"cannot import '{name}' from '{__name__}'")
