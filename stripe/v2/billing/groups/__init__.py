# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.v2.billing.groups._invoice_service import (
        InvoiceService as InvoiceService,
    )
    from stripe.v2.billing.groups._spend_modifier_rule_service import (
        SpendModifierRuleService as SpendModifierRuleService,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "InvoiceService": ("stripe.v2.billing.groups._invoice_service", False),
    "SpendModifierRuleService": (
        "stripe.v2.billing.groups._spend_modifier_rule_service",
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
