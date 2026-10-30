# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.v2.billing.contracts.terms._quantity_change_list_contract_term_quantity_changes_params import (
        QuantityChangeListContractTermQuantityChangesParams as QuantityChangeListContractTermQuantityChangesParams,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "QuantityChangeListContractTermQuantityChangesParams": (
        "stripe.params.v2.billing.contracts.terms._quantity_change_list_contract_term_quantity_changes_params",
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
