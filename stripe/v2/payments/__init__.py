# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.v2.payments._off_session_payment import (
        OffSessionPayment as OffSessionPayment,
    )
    from stripe.v2.payments._off_session_payment_service import (
        OffSessionPaymentService as OffSessionPaymentService,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "OffSessionPayment": ("stripe.v2.payments._off_session_payment", False),
    "OffSessionPaymentService": (
        "stripe.v2.payments._off_session_payment_service",
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
