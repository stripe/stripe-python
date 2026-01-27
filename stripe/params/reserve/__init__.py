# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.reserve._hold_list_params import (
        HoldListParams as HoldListParams,
    )
    from stripe.params.reserve._hold_retrieve_params import (
        HoldRetrieveParams as HoldRetrieveParams,
    )
    from stripe.params.reserve._plan_retrieve_params import (
        PlanRetrieveParams as PlanRetrieveParams,
    )
    from stripe.params.reserve._release_list_params import (
        ReleaseListParams as ReleaseListParams,
    )
    from stripe.params.reserve._release_retrieve_params import (
        ReleaseRetrieveParams as ReleaseRetrieveParams,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "HoldListParams": ("stripe.params.reserve._hold_list_params", False),
    "HoldRetrieveParams": (
        "stripe.params.reserve._hold_retrieve_params",
        False,
    ),
    "PlanRetrieveParams": (
        "stripe.params.reserve._plan_retrieve_params",
        False,
    ),
    "ReleaseListParams": ("stripe.params.reserve._release_list_params", False),
    "ReleaseRetrieveParams": (
        "stripe.params.reserve._release_retrieve_params",
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
