# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.radar._early_fraud_warning import (
        EarlyFraudWarning as EarlyFraudWarning,
    )
    from stripe.radar._early_fraud_warning_service import (
        EarlyFraudWarningService as EarlyFraudWarningService,
    )
    from stripe.radar._value_list import ValueList as ValueList
    from stripe.radar._value_list_item import ValueListItem as ValueListItem
    from stripe.radar._value_list_item_service import (
        ValueListItemService as ValueListItemService,
    )
    from stripe.radar._value_list_service import (
        ValueListService as ValueListService,
    )

_submodules = {
    "EarlyFraudWarning": "stripe.radar._early_fraud_warning",
    "EarlyFraudWarningService": "stripe.radar._early_fraud_warning_service",
    "ValueList": "stripe.radar._value_list",
    "ValueListItem": "stripe.radar._value_list_item",
    "ValueListItemService": "stripe.radar._value_list_item_service",
    "ValueListService": "stripe.radar._value_list_service",
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
