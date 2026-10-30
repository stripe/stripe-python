# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.v2.risk._form_retrieve_params import (
        FormRetrieveParams as FormRetrieveParams,
    )
    from stripe.params.v2.risk._form_update_params import (
        FormUpdateParams as FormUpdateParams,
        FormUpdateParamsAppeal as FormUpdateParamsAppeal,
        FormUpdateParamsAuthorizationDocuments as FormUpdateParamsAuthorizationDocuments,
        FormUpdateParamsProductRemoval as FormUpdateParamsProductRemoval,
        FormUpdateParamsSelfFundingContext as FormUpdateParamsSelfFundingContext,
        FormUpdateParamsSelfFundingContextSourceOfWealth as FormUpdateParamsSelfFundingContextSourceOfWealth,
        FormUpdateParamsTransactionContext as FormUpdateParamsTransactionContext,
        FormUpdateParamsTransactionContextSourceOfFunds as FormUpdateParamsTransactionContextSourceOfFunds,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "FormRetrieveParams": (
        "stripe.params.v2.risk._form_retrieve_params",
        False,
    ),
    "FormUpdateParams": ("stripe.params.v2.risk._form_update_params", False),
    "FormUpdateParamsAppeal": (
        "stripe.params.v2.risk._form_update_params",
        False,
    ),
    "FormUpdateParamsAuthorizationDocuments": (
        "stripe.params.v2.risk._form_update_params",
        False,
    ),
    "FormUpdateParamsProductRemoval": (
        "stripe.params.v2.risk._form_update_params",
        False,
    ),
    "FormUpdateParamsSelfFundingContext": (
        "stripe.params.v2.risk._form_update_params",
        False,
    ),
    "FormUpdateParamsSelfFundingContextSourceOfWealth": (
        "stripe.params.v2.risk._form_update_params",
        False,
    ),
    "FormUpdateParamsTransactionContext": (
        "stripe.params.v2.risk._form_update_params",
        False,
    ),
    "FormUpdateParamsTransactionContextSourceOfFunds": (
        "stripe.params.v2.risk._form_update_params",
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
