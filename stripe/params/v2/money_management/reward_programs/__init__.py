# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.v2.money_management.reward_programs._rule_activate_params import (
        RuleActivateParams as RuleActivateParams,
    )
    from stripe.params.v2.money_management.reward_programs._rule_create_params import (
        RuleCreateParams as RuleCreateParams,
        RuleCreateParamsCondition as RuleCreateParamsCondition,
        RuleCreateParamsConditionCardSpend as RuleCreateParamsConditionCardSpend,
        RuleCreateParamsConditionCardSpendMerchantCategoryCodes as RuleCreateParamsConditionCardSpendMerchantCategoryCodes,
        RuleCreateParamsReward as RuleCreateParamsReward,
        RuleCreateParamsRewardCashback as RuleCreateParamsRewardCashback,
    )
    from stripe.params.v2.money_management.reward_programs._rule_deactivate_params import (
        RuleDeactivateParams as RuleDeactivateParams,
    )
    from stripe.params.v2.money_management.reward_programs._rule_list_params import (
        RuleListParams as RuleListParams,
    )
    from stripe.params.v2.money_management.reward_programs._rule_retrieve_params import (
        RuleRetrieveParams as RuleRetrieveParams,
    )
    from stripe.params.v2.money_management.reward_programs._rule_update_params import (
        RuleUpdateParams as RuleUpdateParams,
        RuleUpdateParamsCondition as RuleUpdateParamsCondition,
        RuleUpdateParamsConditionCardSpend as RuleUpdateParamsConditionCardSpend,
        RuleUpdateParamsConditionCardSpendMerchantCategoryCodes as RuleUpdateParamsConditionCardSpendMerchantCategoryCodes,
        RuleUpdateParamsReward as RuleUpdateParamsReward,
        RuleUpdateParamsRewardCashback as RuleUpdateParamsRewardCashback,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "RuleActivateParams": (
        "stripe.params.v2.money_management.reward_programs._rule_activate_params",
        False,
    ),
    "RuleCreateParams": (
        "stripe.params.v2.money_management.reward_programs._rule_create_params",
        False,
    ),
    "RuleCreateParamsCondition": (
        "stripe.params.v2.money_management.reward_programs._rule_create_params",
        False,
    ),
    "RuleCreateParamsConditionCardSpend": (
        "stripe.params.v2.money_management.reward_programs._rule_create_params",
        False,
    ),
    "RuleCreateParamsConditionCardSpendMerchantCategoryCodes": (
        "stripe.params.v2.money_management.reward_programs._rule_create_params",
        False,
    ),
    "RuleCreateParamsReward": (
        "stripe.params.v2.money_management.reward_programs._rule_create_params",
        False,
    ),
    "RuleCreateParamsRewardCashback": (
        "stripe.params.v2.money_management.reward_programs._rule_create_params",
        False,
    ),
    "RuleDeactivateParams": (
        "stripe.params.v2.money_management.reward_programs._rule_deactivate_params",
        False,
    ),
    "RuleListParams": (
        "stripe.params.v2.money_management.reward_programs._rule_list_params",
        False,
    ),
    "RuleRetrieveParams": (
        "stripe.params.v2.money_management.reward_programs._rule_retrieve_params",
        False,
    ),
    "RuleUpdateParams": (
        "stripe.params.v2.money_management.reward_programs._rule_update_params",
        False,
    ),
    "RuleUpdateParamsCondition": (
        "stripe.params.v2.money_management.reward_programs._rule_update_params",
        False,
    ),
    "RuleUpdateParamsConditionCardSpend": (
        "stripe.params.v2.money_management.reward_programs._rule_update_params",
        False,
    ),
    "RuleUpdateParamsConditionCardSpendMerchantCategoryCodes": (
        "stripe.params.v2.money_management.reward_programs._rule_update_params",
        False,
    ),
    "RuleUpdateParamsReward": (
        "stripe.params.v2.money_management.reward_programs._rule_update_params",
        False,
    ),
    "RuleUpdateParamsRewardCashback": (
        "stripe.params.v2.money_management.reward_programs._rule_update_params",
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
