# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.test_helpers.treasury._inbound_transfer_fail_params import (
        InboundTransferFailParams as InboundTransferFailParams,
        InboundTransferFailParamsFailureDetails as InboundTransferFailParamsFailureDetails,
    )
    from stripe.params.test_helpers.treasury._inbound_transfer_return_inbound_transfer_params import (
        InboundTransferReturnInboundTransferParams as InboundTransferReturnInboundTransferParams,
    )
    from stripe.params.test_helpers.treasury._inbound_transfer_succeed_params import (
        InboundTransferSucceedParams as InboundTransferSucceedParams,
    )
    from stripe.params.test_helpers.treasury._outbound_payment_fail_params import (
        OutboundPaymentFailParams as OutboundPaymentFailParams,
    )
    from stripe.params.test_helpers.treasury._outbound_payment_post_params import (
        OutboundPaymentPostParams as OutboundPaymentPostParams,
    )
    from stripe.params.test_helpers.treasury._outbound_payment_return_outbound_payment_params import (
        OutboundPaymentReturnOutboundPaymentParams as OutboundPaymentReturnOutboundPaymentParams,
        OutboundPaymentReturnOutboundPaymentParamsReturnedDetails as OutboundPaymentReturnOutboundPaymentParamsReturnedDetails,
    )
    from stripe.params.test_helpers.treasury._outbound_payment_update_params import (
        OutboundPaymentUpdateParams as OutboundPaymentUpdateParams,
        OutboundPaymentUpdateParamsTrackingDetails as OutboundPaymentUpdateParamsTrackingDetails,
        OutboundPaymentUpdateParamsTrackingDetailsAch as OutboundPaymentUpdateParamsTrackingDetailsAch,
        OutboundPaymentUpdateParamsTrackingDetailsUsDomesticWire as OutboundPaymentUpdateParamsTrackingDetailsUsDomesticWire,
    )
    from stripe.params.test_helpers.treasury._outbound_transfer_fail_params import (
        OutboundTransferFailParams as OutboundTransferFailParams,
    )
    from stripe.params.test_helpers.treasury._outbound_transfer_post_params import (
        OutboundTransferPostParams as OutboundTransferPostParams,
    )
    from stripe.params.test_helpers.treasury._outbound_transfer_return_outbound_transfer_params import (
        OutboundTransferReturnOutboundTransferParams as OutboundTransferReturnOutboundTransferParams,
        OutboundTransferReturnOutboundTransferParamsReturnedDetails as OutboundTransferReturnOutboundTransferParamsReturnedDetails,
    )
    from stripe.params.test_helpers.treasury._outbound_transfer_update_params import (
        OutboundTransferUpdateParams as OutboundTransferUpdateParams,
        OutboundTransferUpdateParamsTrackingDetails as OutboundTransferUpdateParamsTrackingDetails,
        OutboundTransferUpdateParamsTrackingDetailsAch as OutboundTransferUpdateParamsTrackingDetailsAch,
        OutboundTransferUpdateParamsTrackingDetailsUsDomesticWire as OutboundTransferUpdateParamsTrackingDetailsUsDomesticWire,
    )
    from stripe.params.test_helpers.treasury._received_credit_create_params import (
        ReceivedCreditCreateParams as ReceivedCreditCreateParams,
        ReceivedCreditCreateParamsInitiatingPaymentMethodDetails as ReceivedCreditCreateParamsInitiatingPaymentMethodDetails,
        ReceivedCreditCreateParamsInitiatingPaymentMethodDetailsUsBankAccount as ReceivedCreditCreateParamsInitiatingPaymentMethodDetailsUsBankAccount,
    )
    from stripe.params.test_helpers.treasury._received_debit_create_params import (
        ReceivedDebitCreateParams as ReceivedDebitCreateParams,
        ReceivedDebitCreateParamsInitiatingPaymentMethodDetails as ReceivedDebitCreateParamsInitiatingPaymentMethodDetails,
        ReceivedDebitCreateParamsInitiatingPaymentMethodDetailsUsBankAccount as ReceivedDebitCreateParamsInitiatingPaymentMethodDetailsUsBankAccount,
    )

_submodules = {
    "InboundTransferFailParams": "stripe.params.test_helpers.treasury._inbound_transfer_fail_params",
    "InboundTransferFailParamsFailureDetails": "stripe.params.test_helpers.treasury._inbound_transfer_fail_params",
    "InboundTransferReturnInboundTransferParams": "stripe.params.test_helpers.treasury._inbound_transfer_return_inbound_transfer_params",
    "InboundTransferSucceedParams": "stripe.params.test_helpers.treasury._inbound_transfer_succeed_params",
    "OutboundPaymentFailParams": "stripe.params.test_helpers.treasury._outbound_payment_fail_params",
    "OutboundPaymentPostParams": "stripe.params.test_helpers.treasury._outbound_payment_post_params",
    "OutboundPaymentReturnOutboundPaymentParams": "stripe.params.test_helpers.treasury._outbound_payment_return_outbound_payment_params",
    "OutboundPaymentReturnOutboundPaymentParamsReturnedDetails": "stripe.params.test_helpers.treasury._outbound_payment_return_outbound_payment_params",
    "OutboundPaymentUpdateParams": "stripe.params.test_helpers.treasury._outbound_payment_update_params",
    "OutboundPaymentUpdateParamsTrackingDetails": "stripe.params.test_helpers.treasury._outbound_payment_update_params",
    "OutboundPaymentUpdateParamsTrackingDetailsAch": "stripe.params.test_helpers.treasury._outbound_payment_update_params",
    "OutboundPaymentUpdateParamsTrackingDetailsUsDomesticWire": "stripe.params.test_helpers.treasury._outbound_payment_update_params",
    "OutboundTransferFailParams": "stripe.params.test_helpers.treasury._outbound_transfer_fail_params",
    "OutboundTransferPostParams": "stripe.params.test_helpers.treasury._outbound_transfer_post_params",
    "OutboundTransferReturnOutboundTransferParams": "stripe.params.test_helpers.treasury._outbound_transfer_return_outbound_transfer_params",
    "OutboundTransferReturnOutboundTransferParamsReturnedDetails": "stripe.params.test_helpers.treasury._outbound_transfer_return_outbound_transfer_params",
    "OutboundTransferUpdateParams": "stripe.params.test_helpers.treasury._outbound_transfer_update_params",
    "OutboundTransferUpdateParamsTrackingDetails": "stripe.params.test_helpers.treasury._outbound_transfer_update_params",
    "OutboundTransferUpdateParamsTrackingDetailsAch": "stripe.params.test_helpers.treasury._outbound_transfer_update_params",
    "OutboundTransferUpdateParamsTrackingDetailsUsDomesticWire": "stripe.params.test_helpers.treasury._outbound_transfer_update_params",
    "ReceivedCreditCreateParams": "stripe.params.test_helpers.treasury._received_credit_create_params",
    "ReceivedCreditCreateParamsInitiatingPaymentMethodDetails": "stripe.params.test_helpers.treasury._received_credit_create_params",
    "ReceivedCreditCreateParamsInitiatingPaymentMethodDetailsUsBankAccount": "stripe.params.test_helpers.treasury._received_credit_create_params",
    "ReceivedDebitCreateParams": "stripe.params.test_helpers.treasury._received_debit_create_params",
    "ReceivedDebitCreateParamsInitiatingPaymentMethodDetails": "stripe.params.test_helpers.treasury._received_debit_create_params",
    "ReceivedDebitCreateParamsInitiatingPaymentMethodDetailsUsBankAccount": "stripe.params.test_helpers.treasury._received_debit_create_params",
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
