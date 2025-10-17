# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.v2.payments._off_session_payment_cancel_params import (
        OffSessionPaymentCancelParams as OffSessionPaymentCancelParams,
    )
    from stripe.params.v2.payments._off_session_payment_capture_params import (
        OffSessionPaymentCaptureParams as OffSessionPaymentCaptureParams,
        OffSessionPaymentCaptureParamsTransferData as OffSessionPaymentCaptureParamsTransferData,
    )
    from stripe.params.v2.payments._off_session_payment_create_params import (
        OffSessionPaymentCreateParams as OffSessionPaymentCreateParams,
        OffSessionPaymentCreateParamsAmountDetails as OffSessionPaymentCreateParamsAmountDetails,
        OffSessionPaymentCreateParamsAmountDetailsLineItem as OffSessionPaymentCreateParamsAmountDetailsLineItem,
        OffSessionPaymentCreateParamsAmountDetailsLineItemTax as OffSessionPaymentCreateParamsAmountDetailsLineItemTax,
        OffSessionPaymentCreateParamsAmountDetailsShipping as OffSessionPaymentCreateParamsAmountDetailsShipping,
        OffSessionPaymentCreateParamsAmountDetailsTax as OffSessionPaymentCreateParamsAmountDetailsTax,
        OffSessionPaymentCreateParamsCapture as OffSessionPaymentCreateParamsCapture,
        OffSessionPaymentCreateParamsPaymentMethodOptions as OffSessionPaymentCreateParamsPaymentMethodOptions,
        OffSessionPaymentCreateParamsPaymentMethodOptionsCard as OffSessionPaymentCreateParamsPaymentMethodOptionsCard,
        OffSessionPaymentCreateParamsPaymentsOrchestration as OffSessionPaymentCreateParamsPaymentsOrchestration,
        OffSessionPaymentCreateParamsRetryDetails as OffSessionPaymentCreateParamsRetryDetails,
        OffSessionPaymentCreateParamsTransferData as OffSessionPaymentCreateParamsTransferData,
    )
    from stripe.params.v2.payments._off_session_payment_list_params import (
        OffSessionPaymentListParams as OffSessionPaymentListParams,
    )
    from stripe.params.v2.payments._off_session_payment_retrieve_params import (
        OffSessionPaymentRetrieveParams as OffSessionPaymentRetrieveParams,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "OffSessionPaymentCancelParams": (
        "stripe.params.v2.payments._off_session_payment_cancel_params",
        False,
    ),
    "OffSessionPaymentCaptureParams": (
        "stripe.params.v2.payments._off_session_payment_capture_params",
        False,
    ),
    "OffSessionPaymentCaptureParamsTransferData": (
        "stripe.params.v2.payments._off_session_payment_capture_params",
        False,
    ),
    "OffSessionPaymentCreateParams": (
        "stripe.params.v2.payments._off_session_payment_create_params",
        False,
    ),
    "OffSessionPaymentCreateParamsAmountDetails": (
        "stripe.params.v2.payments._off_session_payment_create_params",
        False,
    ),
    "OffSessionPaymentCreateParamsAmountDetailsLineItem": (
        "stripe.params.v2.payments._off_session_payment_create_params",
        False,
    ),
    "OffSessionPaymentCreateParamsAmountDetailsLineItemTax": (
        "stripe.params.v2.payments._off_session_payment_create_params",
        False,
    ),
    "OffSessionPaymentCreateParamsAmountDetailsShipping": (
        "stripe.params.v2.payments._off_session_payment_create_params",
        False,
    ),
    "OffSessionPaymentCreateParamsAmountDetailsTax": (
        "stripe.params.v2.payments._off_session_payment_create_params",
        False,
    ),
    "OffSessionPaymentCreateParamsCapture": (
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
    "OffSessionPaymentCreateParamsPaymentsOrchestration": (
        "stripe.params.v2.payments._off_session_payment_create_params",
        False,
    ),
    "OffSessionPaymentCreateParamsRetryDetails": (
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
    "OffSessionPaymentRetrieveParams": (
        "stripe.params.v2.payments._off_session_payment_retrieve_params",
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
