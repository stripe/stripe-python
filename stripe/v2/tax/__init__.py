# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.v2.tax._automatic_rule import AutomaticRule as AutomaticRule
    from stripe.v2.tax._automatic_rule_service import (
        AutomaticRuleService as AutomaticRuleService,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "AutomaticRule": ("stripe.v2.tax._automatic_rule", False),
    "AutomaticRuleService": ("stripe.v2.tax._automatic_rule_service", False),
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
