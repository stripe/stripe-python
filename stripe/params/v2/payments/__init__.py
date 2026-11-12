# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.v2.payments._off_session_payment_cancel_params import (
        OffSessionPaymentCancelParams as OffSessionPaymentCancelParams,
    )
    from stripe.params.v2.payments._off_session_payment_create_params import (
        OffSessionPaymentCreateParams as OffSessionPaymentCreateParams,
        OffSessionPaymentCreateParamsAutomaticTax as OffSessionPaymentCreateParamsAutomaticTax,
        OffSessionPaymentCreateParamsItem as OffSessionPaymentCreateParamsItem,
        OffSessionPaymentCreateParamsItemOneTimePrice as OffSessionPaymentCreateParamsItemOneTimePrice,
        OffSessionPaymentCreateParamsItemOneTimePriceItem as OffSessionPaymentCreateParamsItemOneTimePriceItem,
        OffSessionPaymentCreateParamsItemOneTimePriceItemPriceData as OffSessionPaymentCreateParamsItemOneTimePriceItemPriceData,
        OffSessionPaymentCreateParamsItemOneTimePriceItemPriceDataProductData as OffSessionPaymentCreateParamsItemOneTimePriceItemPriceDataProductData,
        OffSessionPaymentCreateParamsItemOneTimePriceItemPriceDataProductDataTaxDetails as OffSessionPaymentCreateParamsItemOneTimePriceItemPriceDataProductDataTaxDetails,
        OffSessionPaymentCreateParamsPaymentMethodData as OffSessionPaymentCreateParamsPaymentMethodData,
        OffSessionPaymentCreateParamsPaymentMethodDataBillingDetails as OffSessionPaymentCreateParamsPaymentMethodDataBillingDetails,
        OffSessionPaymentCreateParamsPaymentMethodDataBillingDetailsAddress as OffSessionPaymentCreateParamsPaymentMethodDataBillingDetailsAddress,
        OffSessionPaymentCreateParamsPaymentMethodDataCard as OffSessionPaymentCreateParamsPaymentMethodDataCard,
        OffSessionPaymentCreateParamsPaymentMethodDataCardNetworkToken as OffSessionPaymentCreateParamsPaymentMethodDataCardNetworkToken,
        OffSessionPaymentCreateParamsPaymentMethodOptions as OffSessionPaymentCreateParamsPaymentMethodOptions,
        OffSessionPaymentCreateParamsPaymentMethodOptionsCard as OffSessionPaymentCreateParamsPaymentMethodOptionsCard,
        OffSessionPaymentCreateParamsRawAmount as OffSessionPaymentCreateParamsRawAmount,
        OffSessionPaymentCreateParamsRetries as OffSessionPaymentCreateParamsRetries,
        OffSessionPaymentCreateParamsTransferData as OffSessionPaymentCreateParamsTransferData,
    )
    from stripe.params.v2.payments._off_session_payment_list_params import (
        OffSessionPaymentListParams as OffSessionPaymentListParams,
    )
    from stripe.params.v2.payments._off_session_payment_pause_params import (
        OffSessionPaymentPauseParams as OffSessionPaymentPauseParams,
    )
    from stripe.params.v2.payments._off_session_payment_resume_params import (
        OffSessionPaymentResumeParams as OffSessionPaymentResumeParams,
    )
    from stripe.params.v2.payments._off_session_payment_retrieve_params import (
        OffSessionPaymentRetrieveParams as OffSessionPaymentRetrieveParams,
    )
    from stripe.params.v2.payments._off_session_payment_update_params import (
        OffSessionPaymentUpdateParams as OffSessionPaymentUpdateParams,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "OffSessionPaymentCancelParams": (
        "stripe.params.v2.payments._off_session_payment_cancel_params",
        False,
    ),
    "OffSessionPaymentCreateParams": (
        "stripe.params.v2.payments._off_session_payment_create_params",
        False,
    ),
    "OffSessionPaymentCreateParamsAutomaticTax": (
        "stripe.params.v2.payments._off_session_payment_create_params",
        False,
    ),
    "OffSessionPaymentCreateParamsItem": (
        "stripe.params.v2.payments._off_session_payment_create_params",
        False,
    ),
    "OffSessionPaymentCreateParamsItemOneTimePrice": (
        "stripe.params.v2.payments._off_session_payment_create_params",
        False,
    ),
    "OffSessionPaymentCreateParamsItemOneTimePriceItem": (
        "stripe.params.v2.payments._off_session_payment_create_params",
        False,
    ),
    "OffSessionPaymentCreateParamsItemOneTimePriceItemPriceData": (
        "stripe.params.v2.payments._off_session_payment_create_params",
        False,
    ),
    "OffSessionPaymentCreateParamsItemOneTimePriceItemPriceDataProductData": (
        "stripe.params.v2.payments._off_session_payment_create_params",
        False,
    ),
    "OffSessionPaymentCreateParamsItemOneTimePriceItemPriceDataProductDataTaxDetails": (
        "stripe.params.v2.payments._off_session_payment_create_params",
        False,
    ),
    "OffSessionPaymentCreateParamsPaymentMethodData": (
        "stripe.params.v2.payments._off_session_payment_create_params",
        False,
    ),
    "OffSessionPaymentCreateParamsPaymentMethodDataBillingDetails": (
        "stripe.params.v2.payments._off_session_payment_create_params",
        False,
    ),
    "OffSessionPaymentCreateParamsPaymentMethodDataBillingDetailsAddress": (
        "stripe.params.v2.payments._off_session_payment_create_params",
        False,
    ),
    "OffSessionPaymentCreateParamsPaymentMethodDataCard": (
        "stripe.params.v2.payments._off_session_payment_create_params",
        False,
    ),
    "OffSessionPaymentCreateParamsPaymentMethodDataCardNetworkToken": (
        "stripe.params.v2.payments._off_session_payment_create_params",
        False,
    ),
    "OffSessionPaymentCreateParamsPaymentMethodOptions": (
        "stripe.params.v2.payments._off_session_payment_create_params",
        False,
    ),
    "OffSessionPaymentCreateParamsPaymentMethodOptionsCard": (
        "stripe.params.v2.payments._off_session_payment_create_params",
        False,
    ),
    "OffSessionPaymentCreateParamsRawAmount": (
        "stripe.params.v2.payments._off_session_payment_create_params",
        False,
    ),
    "OffSessionPaymentCreateParamsRetries": (
        "stripe.params.v2.payments._off_session_payment_create_params",
        False,
    ),
    "OffSessionPaymentCreateParamsTransferData": (
        "stripe.params.v2.payments._off_session_payment_create_params",
        False,
    ),
    "OffSessionPaymentListParams": (
        "stripe.params.v2.payments._off_session_payment_list_params",
        False,
    ),
    "OffSessionPaymentPauseParams": (
        "stripe.params.v2.payments._off_session_payment_pause_params",
        False,
    ),
    "OffSessionPaymentResumeParams": (
        "stripe.params.v2.payments._off_session_payment_resume_params",
        False,
    ),
    "OffSessionPaymentRetrieveParams": (
        "stripe.params.v2.payments._off_session_payment_retrieve_params",
        False,
    ),
    "OffSessionPaymentUpdateParams": (
        "stripe.params.v2.payments._off_session_payment_update_params",
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
