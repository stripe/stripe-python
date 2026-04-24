# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.v2.network._business_profile_me_params import (
        BusinessProfileMeParams as BusinessProfileMeParams,
    )
    from stripe.params.v2.network._business_profile_retrieve_params import (
        BusinessProfileRetrieveParams as BusinessProfileRetrieveParams,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "BusinessProfileMeParams": (
        "stripe.params.v2.network._business_profile_me_params",
        False,
    ),
    "BusinessProfileRetrieveParams": (
        "stripe.params.v2.network._business_profile_retrieve_params",
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
