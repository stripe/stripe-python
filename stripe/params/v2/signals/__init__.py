# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.v2.signals._account_signal_list_params import (
        AccountSignalListParams as AccountSignalListParams,
        AccountSignalListParamsAccountDetails as AccountSignalListParamsAccountDetails,
    )
    from stripe.params.v2.signals._account_signal_retrieve_params import (
        AccountSignalRetrieveParams as AccountSignalRetrieveParams,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "AccountSignalListParams": (
        "stripe.params.v2.signals._account_signal_list_params",
        False,
    ),
    "AccountSignalListParamsAccountDetails": (
        "stripe.params.v2.signals._account_signal_list_params",
        False,
    ),
    "AccountSignalRetrieveParams": (
        "stripe.params.v2.signals._account_signal_retrieve_params",
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
