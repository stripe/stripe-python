# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.v2.billing.groups._invoice_create_params import (
        InvoiceCreateParams as InvoiceCreateParams,
    )
    from stripe.params.v2.billing.groups._spend_modifier_rule_list_params import (
        SpendModifierRuleListParams as SpendModifierRuleListParams,
    )
    from stripe.params.v2.billing.groups._spend_modifier_rule_retrieve_params import (
        SpendModifierRuleRetrieveParams as SpendModifierRuleRetrieveParams,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "InvoiceCreateParams": (
        "stripe.params.v2.billing.groups._invoice_create_params",
        False,
    ),
    "SpendModifierRuleListParams": (
        "stripe.params.v2.billing.groups._spend_modifier_rule_list_params",
        False,
    ),
    "SpendModifierRuleRetrieveParams": (
        "stripe.params.v2.billing.groups._spend_modifier_rule_retrieve_params",
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
