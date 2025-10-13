# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.radar._early_fraud_warning_list_params import (
        EarlyFraudWarningListParams as EarlyFraudWarningListParams,
        EarlyFraudWarningListParamsCreated as EarlyFraudWarningListParamsCreated,
    )
    from stripe.params.radar._early_fraud_warning_retrieve_params import (
        EarlyFraudWarningRetrieveParams as EarlyFraudWarningRetrieveParams,
    )
    from stripe.params.radar._value_list_create_params import (
        ValueListCreateParams as ValueListCreateParams,
    )
    from stripe.params.radar._value_list_delete_params import (
        ValueListDeleteParams as ValueListDeleteParams,
    )
    from stripe.params.radar._value_list_item_create_params import (
        ValueListItemCreateParams as ValueListItemCreateParams,
    )
    from stripe.params.radar._value_list_item_delete_params import (
        ValueListItemDeleteParams as ValueListItemDeleteParams,
    )
    from stripe.params.radar._value_list_item_list_params import (
        ValueListItemListParams as ValueListItemListParams,
        ValueListItemListParamsCreated as ValueListItemListParamsCreated,
    )
    from stripe.params.radar._value_list_item_retrieve_params import (
        ValueListItemRetrieveParams as ValueListItemRetrieveParams,
    )
    from stripe.params.radar._value_list_list_params import (
        ValueListListParams as ValueListListParams,
        ValueListListParamsCreated as ValueListListParamsCreated,
    )
    from stripe.params.radar._value_list_modify_params import (
        ValueListModifyParams as ValueListModifyParams,
    )
    from stripe.params.radar._value_list_retrieve_params import (
        ValueListRetrieveParams as ValueListRetrieveParams,
    )
    from stripe.params.radar._value_list_update_params import (
        ValueListUpdateParams as ValueListUpdateParams,
    )

_submodules = {
    "EarlyFraudWarningListParams": "stripe.params.radar._early_fraud_warning_list_params",
    "EarlyFraudWarningListParamsCreated": "stripe.params.radar._early_fraud_warning_list_params",
    "EarlyFraudWarningRetrieveParams": "stripe.params.radar._early_fraud_warning_retrieve_params",
    "ValueListCreateParams": "stripe.params.radar._value_list_create_params",
    "ValueListDeleteParams": "stripe.params.radar._value_list_delete_params",
    "ValueListItemCreateParams": "stripe.params.radar._value_list_item_create_params",
    "ValueListItemDeleteParams": "stripe.params.radar._value_list_item_delete_params",
    "ValueListItemListParams": "stripe.params.radar._value_list_item_list_params",
    "ValueListItemListParamsCreated": "stripe.params.radar._value_list_item_list_params",
    "ValueListItemRetrieveParams": "stripe.params.radar._value_list_item_retrieve_params",
    "ValueListListParams": "stripe.params.radar._value_list_list_params",
    "ValueListListParamsCreated": "stripe.params.radar._value_list_list_params",
    "ValueListModifyParams": "stripe.params.radar._value_list_modify_params",
    "ValueListRetrieveParams": "stripe.params.radar._value_list_retrieve_params",
    "ValueListUpdateParams": "stripe.params.radar._value_list_update_params",
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
