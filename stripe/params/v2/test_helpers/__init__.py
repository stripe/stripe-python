# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.v2.test_helpers._financial_address_credit_params import (
        FinancialAddressCreditParams as FinancialAddressCreditParams,
        FinancialAddressCreditParamsAmount as FinancialAddressCreditParamsAmount,
    )
    from stripe.params.v2.test_helpers._financial_address_generate_microdeposits_params import (
        FinancialAddressGenerateMicrodepositsParams as FinancialAddressGenerateMicrodepositsParams,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "FinancialAddressCreditParams": (
        "stripe.params.v2.test_helpers._financial_address_credit_params",
        False,
    ),
    "FinancialAddressCreditParamsAmount": (
        "stripe.params.v2.test_helpers._financial_address_credit_params",
        False,
    ),
    "FinancialAddressGenerateMicrodepositsParams": (
        "stripe.params.v2.test_helpers._financial_address_generate_microdeposits_params",
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
