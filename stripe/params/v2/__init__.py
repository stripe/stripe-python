# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.v2 import (
        billing as billing,
        core as core,
        iam as iam,
        money_management as money_management,
        payments as payments,
        reporting as reporting,
        tax as tax,
        test_helpers as test_helpers,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "billing": ("stripe.params.v2.billing", True),
    "core": ("stripe.params.v2.core", True),
    "iam": ("stripe.params.v2.iam", True),
    "money_management": ("stripe.params.v2.money_management", True),
    "payments": ("stripe.params.v2.payments", True),
    "reporting": ("stripe.params.v2.reporting", True),
    "tax": ("stripe.params.v2.tax", True),
    "test_helpers": ("stripe.params.v2.test_helpers", True),
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
