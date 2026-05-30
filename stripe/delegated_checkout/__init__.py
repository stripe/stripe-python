# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.delegated_checkout._order import Order as Order
    from stripe.delegated_checkout._order_event import OrderEvent as OrderEvent
    from stripe.delegated_checkout._requested_session import (
        RequestedSession as RequestedSession,
    )
    from stripe.delegated_checkout._requested_session_order_service import (
        RequestedSessionOrderService as RequestedSessionOrderService,
    )
    from stripe.delegated_checkout._requested_session_service import (
        RequestedSessionService as RequestedSessionService,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "Order": ("stripe.delegated_checkout._order", False),
    "OrderEvent": ("stripe.delegated_checkout._order_event", False),
    "RequestedSession": (
        "stripe.delegated_checkout._requested_session",
        False,
    ),
    "RequestedSessionOrderService": (
        "stripe.delegated_checkout._requested_session_order_service",
        False,
    ),
    "RequestedSessionService": (
        "stripe.delegated_checkout._requested_session_service",
        False,
    ),
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
