# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.v2.commerce.product_catalog._import_create_params import (
        ImportCreateParams as ImportCreateParams,
    )
    from stripe.params.v2.commerce.product_catalog._import_list_params import (
        ImportListParams as ImportListParams,
    )
    from stripe.params.v2.commerce.product_catalog._import_retrieve_params import (
        ImportRetrieveParams as ImportRetrieveParams,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "ImportCreateParams": (
        "stripe.params.v2.commerce.product_catalog._import_create_params",
        False,
    ),
    "ImportListParams": (
        "stripe.params.v2.commerce.product_catalog._import_list_params",
        False,
    ),
    "ImportRetrieveParams": (
        "stripe.params.v2.commerce.product_catalog._import_retrieve_params",
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
