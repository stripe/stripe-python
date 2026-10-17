# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.risk._form_modify_params import (
        FormModifyParams as FormModifyParams,
        FormModifyParamsAppeal as FormModifyParamsAppeal,
        FormModifyParamsAuthorizationDocuments as FormModifyParamsAuthorizationDocuments,
        FormModifyParamsPaymentProcessing as FormModifyParamsPaymentProcessing,
        FormModifyParamsPaymentProcessingMultiProcessor as FormModifyParamsPaymentProcessingMultiProcessor,
        FormModifyParamsPaymentProcessingMultiProcessorFile as FormModifyParamsPaymentProcessingMultiProcessorFile,
        FormModifyParamsProductRemoval as FormModifyParamsProductRemoval,
        FormModifyParamsReviewedFields as FormModifyParamsReviewedFields,
        FormModifyParamsReviewedFieldsAttestation as FormModifyParamsReviewedFieldsAttestation,
        FormModifyParamsSelfFundingContext as FormModifyParamsSelfFundingContext,
        FormModifyParamsSelfFundingContextSourceOfWealth as FormModifyParamsSelfFundingContextSourceOfWealth,
        FormModifyParamsTransactionContext as FormModifyParamsTransactionContext,
        FormModifyParamsTransactionContextSourceOfFunds as FormModifyParamsTransactionContextSourceOfFunds,
    )
    from stripe.params.risk._form_retrieve_params import (
        FormRetrieveParams as FormRetrieveParams,
    )
    from stripe.params.risk._form_update_params import (
        FormUpdateParams as FormUpdateParams,
        FormUpdateParamsAppeal as FormUpdateParamsAppeal,
        FormUpdateParamsAuthorizationDocuments as FormUpdateParamsAuthorizationDocuments,
        FormUpdateParamsPaymentProcessing as FormUpdateParamsPaymentProcessing,
        FormUpdateParamsPaymentProcessingMultiProcessor as FormUpdateParamsPaymentProcessingMultiProcessor,
        FormUpdateParamsPaymentProcessingMultiProcessorFile as FormUpdateParamsPaymentProcessingMultiProcessorFile,
        FormUpdateParamsProductRemoval as FormUpdateParamsProductRemoval,
        FormUpdateParamsReviewedFields as FormUpdateParamsReviewedFields,
        FormUpdateParamsReviewedFieldsAttestation as FormUpdateParamsReviewedFieldsAttestation,
        FormUpdateParamsSelfFundingContext as FormUpdateParamsSelfFundingContext,
        FormUpdateParamsSelfFundingContextSourceOfWealth as FormUpdateParamsSelfFundingContextSourceOfWealth,
        FormUpdateParamsTransactionContext as FormUpdateParamsTransactionContext,
        FormUpdateParamsTransactionContextSourceOfFunds as FormUpdateParamsTransactionContextSourceOfFunds,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "FormModifyParams": ("stripe.params.risk._form_modify_params", False),
    "FormModifyParamsAppeal": (
        "stripe.params.risk._form_modify_params",
        False,
    ),
    "FormModifyParamsAuthorizationDocuments": (
        "stripe.params.risk._form_modify_params",
        False,
    ),
    "FormModifyParamsPaymentProcessing": (
        "stripe.params.risk._form_modify_params",
        False,
    ),
    "FormModifyParamsPaymentProcessingMultiProcessor": (
        "stripe.params.risk._form_modify_params",
        False,
    ),
    "FormModifyParamsPaymentProcessingMultiProcessorFile": (
        "stripe.params.risk._form_modify_params",
        False,
    ),
    "FormModifyParamsProductRemoval": (
        "stripe.params.risk._form_modify_params",
        False,
    ),
    "FormModifyParamsReviewedFields": (
        "stripe.params.risk._form_modify_params",
        False,
    ),
    "FormModifyParamsReviewedFieldsAttestation": (
        "stripe.params.risk._form_modify_params",
        False,
    ),
    "FormModifyParamsSelfFundingContext": (
        "stripe.params.risk._form_modify_params",
        False,
    ),
    "FormModifyParamsSelfFundingContextSourceOfWealth": (
        "stripe.params.risk._form_modify_params",
        False,
    ),
    "FormModifyParamsTransactionContext": (
        "stripe.params.risk._form_modify_params",
        False,
    ),
    "FormModifyParamsTransactionContextSourceOfFunds": (
        "stripe.params.risk._form_modify_params",
        False,
    ),
    "FormRetrieveParams": ("stripe.params.risk._form_retrieve_params", False),
    "FormUpdateParams": ("stripe.params.risk._form_update_params", False),
    "FormUpdateParamsAppeal": (
        "stripe.params.risk._form_update_params",
        False,
    ),
    "FormUpdateParamsAuthorizationDocuments": (
        "stripe.params.risk._form_update_params",
        False,
    ),
    "FormUpdateParamsPaymentProcessing": (
        "stripe.params.risk._form_update_params",
        False,
    ),
    "FormUpdateParamsPaymentProcessingMultiProcessor": (
        "stripe.params.risk._form_update_params",
        False,
    ),
    "FormUpdateParamsPaymentProcessingMultiProcessorFile": (
        "stripe.params.risk._form_update_params",
        False,
    ),
    "FormUpdateParamsProductRemoval": (
        "stripe.params.risk._form_update_params",
        False,
    ),
    "FormUpdateParamsReviewedFields": (
        "stripe.params.risk._form_update_params",
        False,
    ),
    "FormUpdateParamsReviewedFieldsAttestation": (
        "stripe.params.risk._form_update_params",
        False,
    ),
    "FormUpdateParamsSelfFundingContext": (
        "stripe.params.risk._form_update_params",
        False,
    ),
    "FormUpdateParamsSelfFundingContextSourceOfWealth": (
        "stripe.params.risk._form_update_params",
        False,
    ),
    "FormUpdateParamsTransactionContext": (
        "stripe.params.risk._form_update_params",
        False,
    ),
    "FormUpdateParamsTransactionContextSourceOfFunds": (
        "stripe.params.risk._form_update_params",
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
