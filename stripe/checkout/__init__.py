# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.checkout._session import Session as Session
    from stripe.checkout._session_line_item_service import (
        SessionLineItemService as SessionLineItemService,
    )
    from stripe.checkout._session_service import (
        SessionService as SessionService,
    )

_submodules = {
    "Session": "stripe.checkout._session",
    "SessionLineItemService": "stripe.checkout._session_line_item_service",
    "SessionService": "stripe.checkout._session_service",
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
