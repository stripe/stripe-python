# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.v2.tax._integration_configuration import (
        IntegrationConfiguration as IntegrationConfiguration,
    )
    from stripe.v2.tax._integration_configuration_service import (
        IntegrationConfigurationService as IntegrationConfigurationService,
    )
    from stripe.v2.tax._manual_rule import ManualRule as ManualRule
    from stripe.v2.tax._manual_rule_service import (
        ManualRuleService as ManualRuleService,
    )
    from stripe.v2.tax._operation_service import (
        OperationService as OperationService,
    )
    from stripe.v2.tax._operations_resolve_address_result import (
        OperationsResolveAddressResult as OperationsResolveAddressResult,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "IntegrationConfiguration": (
        "stripe.v2.tax._integration_configuration",
        False,
    ),
    "IntegrationConfigurationService": (
        "stripe.v2.tax._integration_configuration_service",
        False,
    ),
    "ManualRule": ("stripe.v2.tax._manual_rule", False),
    "ManualRuleService": ("stripe.v2.tax._manual_rule_service", False),
    "OperationService": ("stripe.v2.tax._operation_service", False),
    "OperationsResolveAddressResult": (
        "stripe.v2.tax._operations_resolve_address_result",
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
