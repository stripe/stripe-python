# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.climate._order import Order as Order
    from stripe.climate._order_service import OrderService as OrderService
    from stripe.climate._product import Product as Product
    from stripe.climate._product_service import (
        ProductService as ProductService,
    )
    from stripe.climate._supplier import Supplier as Supplier
    from stripe.climate._supplier_service import (
        SupplierService as SupplierService,
    )

_submodules = {
    "Order": "stripe.climate._order",
    "OrderService": "stripe.climate._order_service",
    "Product": "stripe.climate._product",
    "ProductService": "stripe.climate._product_service",
    "Supplier": "stripe.climate._supplier",
    "SupplierService": "stripe.climate._supplier_service",
}
if not TYPE_CHECKING:

    def __getattr__(name):
        try:
            return getattr(
                import_module(_submodules[name]),
                name,
            )
        except KeyError:
            raise AttributeError(f"cannot import '{name}' from '{__name__}'")
