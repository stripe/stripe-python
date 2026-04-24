# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.v2.payments import (
        settlement_allocation_intents as settlement_allocation_intents,
    )
    from stripe.params.v2.payments._off_session_payment_cancel_params import (
        OffSessionPaymentCancelParams as OffSessionPaymentCancelParams,
    )
    from stripe.params.v2.payments._off_session_payment_capture_params import (
        OffSessionPaymentCaptureParams as OffSessionPaymentCaptureParams,
        OffSessionPaymentCaptureParamsAmountDetails as OffSessionPaymentCaptureParamsAmountDetails,
        OffSessionPaymentCaptureParamsAmountDetailsLineItem as OffSessionPaymentCaptureParamsAmountDetailsLineItem,
        OffSessionPaymentCaptureParamsAmountDetailsLineItemTax as OffSessionPaymentCaptureParamsAmountDetailsLineItemTax,
        OffSessionPaymentCaptureParamsAmountDetailsShipping as OffSessionPaymentCaptureParamsAmountDetailsShipping,
        OffSessionPaymentCaptureParamsAmountDetailsTax as OffSessionPaymentCaptureParamsAmountDetailsTax,
        OffSessionPaymentCaptureParamsPaymentDetails as OffSessionPaymentCaptureParamsPaymentDetails,
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
        OffSessionPaymentCreateParamsPaymentDetails as OffSessionPaymentCreateParamsPaymentDetails,
        OffSessionPaymentCreateParamsPaymentMethodData as OffSessionPaymentCreateParamsPaymentMethodData,
        OffSessionPaymentCreateParamsPaymentMethodDataBillingDetails as OffSessionPaymentCreateParamsPaymentMethodDataBillingDetails,
        OffSessionPaymentCreateParamsPaymentMethodDataBillingDetailsAddress as OffSessionPaymentCreateParamsPaymentMethodDataBillingDetailsAddress,
        OffSessionPaymentCreateParamsPaymentMethodDataCard as OffSessionPaymentCreateParamsPaymentMethodDataCard,
        OffSessionPaymentCreateParamsPaymentMethodOptions as OffSessionPaymentCreateParamsPaymentMethodOptions,
        OffSessionPaymentCreateParamsPaymentMethodOptionsCard as OffSessionPaymentCreateParamsPaymentMethodOptionsCard,
        OffSessionPaymentCreateParamsPaymentsOrchestration as OffSessionPaymentCreateParamsPaymentsOrchestration,
        OffSessionPaymentCreateParamsRetryDetails as OffSessionPaymentCreateParamsRetryDetails,
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
    from stripe.params.v2.payments._settlement_allocation_intent_cancel_params import (
        SettlementAllocationIntentCancelParams as SettlementAllocationIntentCancelParams,
    )
    from stripe.params.v2.payments._settlement_allocation_intent_create_params import (
        SettlementAllocationIntentCreateParams as SettlementAllocationIntentCreateParams,
    )
    from stripe.params.v2.payments._settlement_allocation_intent_list_params import (
        SettlementAllocationIntentListParams as SettlementAllocationIntentListParams,
    )
    from stripe.params.v2.payments._settlement_allocation_intent_retrieve_params import (
        SettlementAllocationIntentRetrieveParams as SettlementAllocationIntentRetrieveParams,
    )
    from stripe.params.v2.payments._settlement_allocation_intent_submit_params import (
        SettlementAllocationIntentSubmitParams as SettlementAllocationIntentSubmitParams,
    )
    from stripe.params.v2.payments._settlement_allocation_intent_update_params import (
        SettlementAllocationIntentUpdateParams as SettlementAllocationIntentUpdateParams,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "settlement_allocation_intents": (
        "stripe.params.v2.payments.settlement_allocation_intents",
        True,
    ),
    "OffSessionPaymentCancelParams": (
        "stripe.params.v2.payments._off_session_payment_cancel_params",
        False,
    ),
    "OffSessionPaymentCaptureParams": (
        "stripe.params.v2.payments._off_session_payment_capture_params",
        False,
    ),
    "OffSessionPaymentCaptureParamsAmountDetails": (
        "stripe.params.v2.payments._off_session_payment_capture_params",
        False,
    ),
    "OffSessionPaymentCaptureParamsAmountDetailsLineItem": (
        "stripe.params.v2.payments._off_session_payment_capture_params",
        False,
    ),
    "OffSessionPaymentCaptureParamsAmountDetailsLineItemTax": (
        "stripe.params.v2.payments._off_session_payment_capture_params",
        False,
    ),
    "OffSessionPaymentCaptureParamsAmountDetailsShipping": (
        "stripe.params.v2.payments._off_session_payment_capture_params",
        False,
    ),
    "OffSessionPaymentCaptureParamsAmountDetailsTax": (
        "stripe.params.v2.payments._off_session_payment_capture_params",
        False,
    ),
    "OffSessionPaymentCaptureParamsPaymentDetails": (
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
    "OffSessionPaymentCreateParamsPaymentDetails": (
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
    "SettlementAllocationIntentCancelParams": (
        "stripe.params.v2.payments._settlement_allocation_intent_cancel_params",
        False,
    ),
    "SettlementAllocationIntentCreateParams": (
        "stripe.params.v2.payments._settlement_allocation_intent_create_params",
        False,
    ),
    "SettlementAllocationIntentListParams": (
        "stripe.params.v2.payments._settlement_allocation_intent_list_params",
        False,
    ),
    "SettlementAllocationIntentRetrieveParams": (
        "stripe.params.v2.payments._settlement_allocation_intent_retrieve_params",
        False,
    ),
    "SettlementAllocationIntentSubmitParams": (
        "stripe.params.v2.payments._settlement_allocation_intent_submit_params",
        False,
    ),
    "SettlementAllocationIntentUpdateParams": (
        "stripe.params.v2.payments._settlement_allocation_intent_update_params",
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
