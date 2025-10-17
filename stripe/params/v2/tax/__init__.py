# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.v2.tax._automatic_rule_create_params import (
        AutomaticRuleCreateParams as AutomaticRuleCreateParams,
    )
    from stripe.params.v2.tax._automatic_rule_deactivate_params import (
        AutomaticRuleDeactivateParams as AutomaticRuleDeactivateParams,
    )
    from stripe.params.v2.tax._automatic_rule_find_params import (
        AutomaticRuleFindParams as AutomaticRuleFindParams,
    )
    from stripe.params.v2.tax._automatic_rule_retrieve_params import (
        AutomaticRuleRetrieveParams as AutomaticRuleRetrieveParams,
    )
    from stripe.params.v2.tax._automatic_rule_update_params import (
        AutomaticRuleUpdateParams as AutomaticRuleUpdateParams,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "AutomaticRuleCreateParams": (
        "stripe.params.v2.tax._automatic_rule_create_params",
        False,
    ),
    "AutomaticRuleDeactivateParams": (
        "stripe.params.v2.tax._automatic_rule_deactivate_params",
        False,
    ),
    "AutomaticRuleFindParams": (
        "stripe.params.v2.tax._automatic_rule_find_params",
        False,
    ),
    "AutomaticRuleRetrieveParams": (
        "stripe.params.v2.tax._automatic_rule_retrieve_params",
        False,
    ),
    "AutomaticRuleUpdateParams": (
        "stripe.params.v2.tax._automatic_rule_update_params",
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
