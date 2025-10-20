# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.v2.test_helpers._financial_address_service import (
        FinancialAddressService as FinancialAddressService,
    )
    from stripe.v2.test_helpers._money_management_service import (
        MoneyManagementService as MoneyManagementService,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "FinancialAddressService": (
        "stripe.v2.test_helpers._financial_address_service",
        False,
    ),
    "MoneyManagementService": (
        "stripe.v2.test_helpers._money_management_service",
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
