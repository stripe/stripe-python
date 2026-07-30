# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.v2.risk._inquiry_list_params import (
        InquiryListParams as InquiryListParams,
    )
    from stripe.params.v2.risk._inquiry_retrieve_params import (
        InquiryRetrieveParams as InquiryRetrieveParams,
    )
    from stripe.params.v2.risk._inquiry_update_params import (
        InquiryUpdateParams as InquiryUpdateParams,
        InquiryUpdateParamsAppeal as InquiryUpdateParamsAppeal,
        InquiryUpdateParamsAuthorizationDocuments as InquiryUpdateParamsAuthorizationDocuments,
        InquiryUpdateParamsProductRemoval as InquiryUpdateParamsProductRemoval,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "InquiryListParams": ("stripe.params.v2.risk._inquiry_list_params", False),
    "InquiryRetrieveParams": (
        "stripe.params.v2.risk._inquiry_retrieve_params",
        False,
    ),
    "InquiryUpdateParams": (
        "stripe.params.v2.risk._inquiry_update_params",
        False,
    ),
    "InquiryUpdateParamsAppeal": (
        "stripe.params.v2.risk._inquiry_update_params",
        False,
    ),
    "InquiryUpdateParamsAuthorizationDocuments": (
        "stripe.params.v2.risk._inquiry_update_params",
        False,
    ),
    "InquiryUpdateParamsProductRemoval": (
        "stripe.params.v2.risk._inquiry_update_params",
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
