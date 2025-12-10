# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.v2.tax._manual_rule_create_params import (
        ManualRuleCreateParams as ManualRuleCreateParams,
        ManualRuleCreateParamsLocation as ManualRuleCreateParamsLocation,
        ManualRuleCreateParamsProduct as ManualRuleCreateParamsProduct,
        ManualRuleCreateParamsScheduledTaxRate as ManualRuleCreateParamsScheduledTaxRate,
        ManualRuleCreateParamsScheduledTaxRateRate as ManualRuleCreateParamsScheduledTaxRateRate,
    )
    from stripe.params.v2.tax._manual_rule_deactivate_params import (
        ManualRuleDeactivateParams as ManualRuleDeactivateParams,
    )
    from stripe.params.v2.tax._manual_rule_list_params import (
        ManualRuleListParams as ManualRuleListParams,
    )
    from stripe.params.v2.tax._manual_rule_retrieve_params import (
        ManualRuleRetrieveParams as ManualRuleRetrieveParams,
    )
    from stripe.params.v2.tax._manual_rule_update_params import (
        ManualRuleUpdateParams as ManualRuleUpdateParams,
        ManualRuleUpdateParamsLocation as ManualRuleUpdateParamsLocation,
        ManualRuleUpdateParamsProduct as ManualRuleUpdateParamsProduct,
        ManualRuleUpdateParamsScheduledTaxRate as ManualRuleUpdateParamsScheduledTaxRate,
        ManualRuleUpdateParamsScheduledTaxRateRate as ManualRuleUpdateParamsScheduledTaxRateRate,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "ManualRuleCreateParams": (
        "stripe.params.v2.tax._manual_rule_create_params",
        False,
    ),
    "ManualRuleCreateParamsLocation": (
        "stripe.params.v2.tax._manual_rule_create_params",
        False,
    ),
    "ManualRuleCreateParamsProduct": (
        "stripe.params.v2.tax._manual_rule_create_params",
        False,
    ),
    "ManualRuleCreateParamsScheduledTaxRate": (
        "stripe.params.v2.tax._manual_rule_create_params",
        False,
    ),
    "ManualRuleCreateParamsScheduledTaxRateRate": (
        "stripe.params.v2.tax._manual_rule_create_params",
        False,
    ),
    "ManualRuleDeactivateParams": (
        "stripe.params.v2.tax._manual_rule_deactivate_params",
        False,
    ),
    "ManualRuleListParams": (
        "stripe.params.v2.tax._manual_rule_list_params",
        False,
    ),
    "ManualRuleRetrieveParams": (
        "stripe.params.v2.tax._manual_rule_retrieve_params",
        False,
    ),
    "ManualRuleUpdateParams": (
        "stripe.params.v2.tax._manual_rule_update_params",
        False,
    ),
    "ManualRuleUpdateParamsLocation": (
        "stripe.params.v2.tax._manual_rule_update_params",
        False,
    ),
    "ManualRuleUpdateParamsProduct": (
        "stripe.params.v2.tax._manual_rule_update_params",
        False,
    ),
    "ManualRuleUpdateParamsScheduledTaxRate": (
        "stripe.params.v2.tax._manual_rule_update_params",
        False,
    ),
    "ManualRuleUpdateParamsScheduledTaxRateRate": (
        "stripe.params.v2.tax._manual_rule_update_params",
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
