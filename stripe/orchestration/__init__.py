# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.orchestration._payment_attempt import (
        PaymentAttempt as PaymentAttempt,
    )
    from stripe.orchestration._payment_attempt_service import (
        PaymentAttemptService as PaymentAttemptService,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "PaymentAttempt": ("stripe.orchestration._payment_attempt", False),
    "PaymentAttemptService": (
        "stripe.orchestration._payment_attempt_service",
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
