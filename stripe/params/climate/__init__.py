# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.climate._order_cancel_params import (
        OrderCancelParams as OrderCancelParams,
    )
    from stripe.params.climate._order_create_params import (
        OrderCreateParams as OrderCreateParams,
        OrderCreateParamsBeneficiary as OrderCreateParamsBeneficiary,
    )
    from stripe.params.climate._order_list_params import (
        OrderListParams as OrderListParams,
    )
    from stripe.params.climate._order_modify_params import (
        OrderModifyParams as OrderModifyParams,
        OrderModifyParamsBeneficiary as OrderModifyParamsBeneficiary,
    )
    from stripe.params.climate._order_retrieve_params import (
        OrderRetrieveParams as OrderRetrieveParams,
    )
    from stripe.params.climate._order_update_params import (
        OrderUpdateParams as OrderUpdateParams,
        OrderUpdateParamsBeneficiary as OrderUpdateParamsBeneficiary,
    )
    from stripe.params.climate._product_list_params import (
        ProductListParams as ProductListParams,
    )
    from stripe.params.climate._product_retrieve_params import (
        ProductRetrieveParams as ProductRetrieveParams,
    )
    from stripe.params.climate._supplier_list_params import (
        SupplierListParams as SupplierListParams,
    )
    from stripe.params.climate._supplier_retrieve_params import (
        SupplierRetrieveParams as SupplierRetrieveParams,
    )

_submodules = {
    "OrderCancelParams": "stripe.params.climate._order_cancel_params",
    "OrderCreateParams": "stripe.params.climate._order_create_params",
    "OrderCreateParamsBeneficiary": "stripe.params.climate._order_create_params",
    "OrderListParams": "stripe.params.climate._order_list_params",
    "OrderModifyParams": "stripe.params.climate._order_modify_params",
    "OrderModifyParamsBeneficiary": "stripe.params.climate._order_modify_params",
    "OrderRetrieveParams": "stripe.params.climate._order_retrieve_params",
    "OrderUpdateParams": "stripe.params.climate._order_update_params",
    "OrderUpdateParamsBeneficiary": "stripe.params.climate._order_update_params",
    "ProductListParams": "stripe.params.climate._product_list_params",
    "ProductRetrieveParams": "stripe.params.climate._product_retrieve_params",
    "SupplierListParams": "stripe.params.climate._supplier_list_params",
    "SupplierRetrieveParams": "stripe.params.climate._supplier_retrieve_params",
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
