# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.forwarding._request import Request as Request
    from stripe.forwarding._request_service import (
        RequestService as RequestService,
    )

_submodules = {
    "Request": "stripe.forwarding._request",
    "RequestService": "stripe.forwarding._request_service",
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
