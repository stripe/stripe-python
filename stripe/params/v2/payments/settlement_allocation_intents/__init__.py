# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.v2.payments.settlement_allocation_intents._split_cancel_params import (
        SplitCancelParams as SplitCancelParams,
    )
    from stripe.params.v2.payments.settlement_allocation_intents._split_create_params import (
        SplitCreateParams as SplitCreateParams,
    )
    from stripe.params.v2.payments.settlement_allocation_intents._split_list_params import (
        SplitListParams as SplitListParams,
    )
    from stripe.params.v2.payments.settlement_allocation_intents._split_retrieve_params import (
        SplitRetrieveParams as SplitRetrieveParams,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "SplitCancelParams": (
        "stripe.params.v2.payments.settlement_allocation_intents._split_cancel_params",
        False,
    ),
    "SplitCreateParams": (
        "stripe.params.v2.payments.settlement_allocation_intents._split_create_params",
        False,
    ),
    "SplitListParams": (
        "stripe.params.v2.payments.settlement_allocation_intents._split_list_params",
        False,
    ),
    "SplitRetrieveParams": (
        "stripe.params.v2.payments.settlement_allocation_intents._split_retrieve_params",
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
