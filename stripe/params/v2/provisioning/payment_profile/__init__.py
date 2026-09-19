# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.v2.provisioning.payment_profile._update_limit_update_params import (
        UpdateLimitUpdateParams as UpdateLimitUpdateParams,
        UpdateLimitUpdateParamsUsageLimits as UpdateLimitUpdateParamsUsageLimits,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "UpdateLimitUpdateParams": (
        "stripe.params.v2.provisioning.payment_profile._update_limit_update_params",
        False,
    ),
    "UpdateLimitUpdateParamsUsageLimits": (
        "stripe.params.v2.provisioning.payment_profile._update_limit_update_params",
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
