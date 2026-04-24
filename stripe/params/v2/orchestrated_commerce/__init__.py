# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.v2.orchestrated_commerce._agreement_confirm_params import (
        AgreementConfirmParams as AgreementConfirmParams,
    )
    from stripe.params.v2.orchestrated_commerce._agreement_create_params import (
        AgreementCreateParams as AgreementCreateParams,
    )
    from stripe.params.v2.orchestrated_commerce._agreement_list_params import (
        AgreementListParams as AgreementListParams,
    )
    from stripe.params.v2.orchestrated_commerce._agreement_retrieve_params import (
        AgreementRetrieveParams as AgreementRetrieveParams,
    )
    from stripe.params.v2.orchestrated_commerce._agreement_terminate_params import (
        AgreementTerminateParams as AgreementTerminateParams,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "AgreementConfirmParams": (
        "stripe.params.v2.orchestrated_commerce._agreement_confirm_params",
        False,
    ),
    "AgreementCreateParams": (
        "stripe.params.v2.orchestrated_commerce._agreement_create_params",
        False,
    ),
    "AgreementListParams": (
        "stripe.params.v2.orchestrated_commerce._agreement_list_params",
        False,
    ),
    "AgreementRetrieveParams": (
        "stripe.params.v2.orchestrated_commerce._agreement_retrieve_params",
        False,
    ),
    "AgreementTerminateParams": (
        "stripe.params.v2.orchestrated_commerce._agreement_terminate_params",
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
