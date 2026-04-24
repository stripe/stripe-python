# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.v2.commerce import product_catalog as product_catalog
    from stripe.v2.commerce._product_catalog_import import (
        ProductCatalogImport as ProductCatalogImport,
    )
    from stripe.v2.commerce._product_catalog_service import (
        ProductCatalogService as ProductCatalogService,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "product_catalog": ("stripe.v2.commerce.product_catalog", True),
    "ProductCatalogImport": (
        "stripe.v2.commerce._product_catalog_import",
        False,
    ),
    "ProductCatalogService": (
        "stripe.v2.commerce._product_catalog_service",
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
