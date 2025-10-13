# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.terminal._configuration import Configuration as Configuration
    from stripe.terminal._configuration_service import (
        ConfigurationService as ConfigurationService,
    )
    from stripe.terminal._connection_token import (
        ConnectionToken as ConnectionToken,
    )
    from stripe.terminal._connection_token_service import (
        ConnectionTokenService as ConnectionTokenService,
    )
    from stripe.terminal._location import Location as Location
    from stripe.terminal._location_service import (
        LocationService as LocationService,
    )
    from stripe.terminal._reader import Reader as Reader
    from stripe.terminal._reader_service import ReaderService as ReaderService

_submodules = {
    "Configuration": "stripe.terminal._configuration",
    "ConfigurationService": "stripe.terminal._configuration_service",
    "ConnectionToken": "stripe.terminal._connection_token",
    "ConnectionTokenService": "stripe.terminal._connection_token_service",
    "Location": "stripe.terminal._location",
    "LocationService": "stripe.terminal._location_service",
    "Reader": "stripe.terminal._reader",
    "ReaderService": "stripe.terminal._reader_service",
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
