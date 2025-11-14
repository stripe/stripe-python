# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.v2.billing.collection_settings._version_list_params import (
        VersionListParams as VersionListParams,
    )
    from stripe.params.v2.billing.collection_settings._version_retrieve_params import (
        VersionRetrieveParams as VersionRetrieveParams,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "VersionListParams": (
        "stripe.params.v2.billing.collection_settings._version_list_params",
        False,
    ),
    "VersionRetrieveParams": (
        "stripe.params.v2.billing.collection_settings._version_retrieve_params",
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
