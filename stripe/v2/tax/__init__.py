# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.v2.tax._manual_rule import ManualRule as ManualRule
    from stripe.v2.tax._manual_rule_service import (
        ManualRuleService as ManualRuleService,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "ManualRule": ("stripe.v2.tax._manual_rule", False),
    "ManualRuleService": ("stripe.v2.tax._manual_rule_service", False),
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
