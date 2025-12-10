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
        OffSessionPaymentCaptureParamsTransferData as OffSessionPaymentCaptureParamsTransferData,
    )
    from stripe.params.v2.payments._off_session_payment_create_params import (
        OffSessionPaymentCreateParams as OffSessionPaymentCreateParams,
        OffSessionPaymentCreateParamsAmount as OffSessionPaymentCreateParamsAmount,
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
    from stripe.params.v2.payments._settlement_allocation_intent_cancel_params import (
        SettlementAllocationIntentCancelParams as SettlementAllocationIntentCancelParams,
    )
    from stripe.params.v2.payments._settlement_allocation_intent_create_params import (
        SettlementAllocationIntentCreateParams as SettlementAllocationIntentCreateParams,
        SettlementAllocationIntentCreateParamsAmount as SettlementAllocationIntentCreateParamsAmount,
    )
    from stripe.params.v2.payments._settlement_allocation_intent_retrieve_params import (
        SettlementAllocationIntentRetrieveParams as SettlementAllocationIntentRetrieveParams,
    )
    from stripe.params.v2.payments._settlement_allocation_intent_submit_params import (
        SettlementAllocationIntentSubmitParams as SettlementAllocationIntentSubmitParams,
    )
    from stripe.params.v2.payments._settlement_allocation_intent_update_params import (
        SettlementAllocationIntentUpdateParams as SettlementAllocationIntentUpdateParams,
        SettlementAllocationIntentUpdateParamsAmount as SettlementAllocationIntentUpdateParamsAmount,
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
    "OffSessionPaymentCaptureParamsTransferData": (
        "stripe.params.v2.payments._off_session_payment_capture_params",
        False,
    ),
    "OffSessionPaymentCreateParams": (
        "stripe.params.v2.payments._off_session_payment_create_params",
        False,
    ),
    "OffSessionPaymentCreateParamsAmount": (
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
    "SettlementAllocationIntentCancelParams": (
        "stripe.params.v2.payments._settlement_allocation_intent_cancel_params",
        False,
    ),
    "SettlementAllocationIntentCreateParams": (
        "stripe.params.v2.payments._settlement_allocation_intent_create_params",
        False,
    ),
    "SettlementAllocationIntentCreateParamsAmount": (
        "stripe.params.v2.payments._settlement_allocation_intent_create_params",
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
    "SettlementAllocationIntentUpdateParamsAmount": (
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
