# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.test_helpers.issuing._authorization_capture_params import (
        AuthorizationCaptureParams as AuthorizationCaptureParams,
        AuthorizationCaptureParamsPurchaseDetails as AuthorizationCaptureParamsPurchaseDetails,
        AuthorizationCaptureParamsPurchaseDetailsFleet as AuthorizationCaptureParamsPurchaseDetailsFleet,
        AuthorizationCaptureParamsPurchaseDetailsFleetCardholderPromptData as AuthorizationCaptureParamsPurchaseDetailsFleetCardholderPromptData,
        AuthorizationCaptureParamsPurchaseDetailsFleetReportedBreakdown as AuthorizationCaptureParamsPurchaseDetailsFleetReportedBreakdown,
        AuthorizationCaptureParamsPurchaseDetailsFleetReportedBreakdownFuel as AuthorizationCaptureParamsPurchaseDetailsFleetReportedBreakdownFuel,
        AuthorizationCaptureParamsPurchaseDetailsFleetReportedBreakdownNonFuel as AuthorizationCaptureParamsPurchaseDetailsFleetReportedBreakdownNonFuel,
        AuthorizationCaptureParamsPurchaseDetailsFleetReportedBreakdownTax as AuthorizationCaptureParamsPurchaseDetailsFleetReportedBreakdownTax,
        AuthorizationCaptureParamsPurchaseDetailsFlight as AuthorizationCaptureParamsPurchaseDetailsFlight,
        AuthorizationCaptureParamsPurchaseDetailsFlightSegment as AuthorizationCaptureParamsPurchaseDetailsFlightSegment,
        AuthorizationCaptureParamsPurchaseDetailsFuel as AuthorizationCaptureParamsPurchaseDetailsFuel,
        AuthorizationCaptureParamsPurchaseDetailsLodging as AuthorizationCaptureParamsPurchaseDetailsLodging,
        AuthorizationCaptureParamsPurchaseDetailsReceipt as AuthorizationCaptureParamsPurchaseDetailsReceipt,
    )
    from stripe.params.test_helpers.issuing._authorization_create_params import (
        AuthorizationCreateParams as AuthorizationCreateParams,
        AuthorizationCreateParamsAmountDetails as AuthorizationCreateParamsAmountDetails,
        AuthorizationCreateParamsFleet as AuthorizationCreateParamsFleet,
        AuthorizationCreateParamsFleetCardholderPromptData as AuthorizationCreateParamsFleetCardholderPromptData,
        AuthorizationCreateParamsFleetReportedBreakdown as AuthorizationCreateParamsFleetReportedBreakdown,
        AuthorizationCreateParamsFleetReportedBreakdownFuel as AuthorizationCreateParamsFleetReportedBreakdownFuel,
        AuthorizationCreateParamsFleetReportedBreakdownNonFuel as AuthorizationCreateParamsFleetReportedBreakdownNonFuel,
        AuthorizationCreateParamsFleetReportedBreakdownTax as AuthorizationCreateParamsFleetReportedBreakdownTax,
        AuthorizationCreateParamsFuel as AuthorizationCreateParamsFuel,
        AuthorizationCreateParamsMerchantData as AuthorizationCreateParamsMerchantData,
        AuthorizationCreateParamsNetworkData as AuthorizationCreateParamsNetworkData,
        AuthorizationCreateParamsRiskAssessment as AuthorizationCreateParamsRiskAssessment,
        AuthorizationCreateParamsRiskAssessmentCardTestingRisk as AuthorizationCreateParamsRiskAssessmentCardTestingRisk,
        AuthorizationCreateParamsRiskAssessmentMerchantDisputeRisk as AuthorizationCreateParamsRiskAssessmentMerchantDisputeRisk,
        AuthorizationCreateParamsVerificationData as AuthorizationCreateParamsVerificationData,
        AuthorizationCreateParamsVerificationDataAuthenticationExemption as AuthorizationCreateParamsVerificationDataAuthenticationExemption,
        AuthorizationCreateParamsVerificationDataThreeDSecure as AuthorizationCreateParamsVerificationDataThreeDSecure,
    )
    from stripe.params.test_helpers.issuing._authorization_expire_params import (
        AuthorizationExpireParams as AuthorizationExpireParams,
    )
    from stripe.params.test_helpers.issuing._authorization_finalize_amount_params import (
        AuthorizationFinalizeAmountParams as AuthorizationFinalizeAmountParams,
        AuthorizationFinalizeAmountParamsFleet as AuthorizationFinalizeAmountParamsFleet,
        AuthorizationFinalizeAmountParamsFleetCardholderPromptData as AuthorizationFinalizeAmountParamsFleetCardholderPromptData,
        AuthorizationFinalizeAmountParamsFleetReportedBreakdown as AuthorizationFinalizeAmountParamsFleetReportedBreakdown,
        AuthorizationFinalizeAmountParamsFleetReportedBreakdownFuel as AuthorizationFinalizeAmountParamsFleetReportedBreakdownFuel,
        AuthorizationFinalizeAmountParamsFleetReportedBreakdownNonFuel as AuthorizationFinalizeAmountParamsFleetReportedBreakdownNonFuel,
        AuthorizationFinalizeAmountParamsFleetReportedBreakdownTax as AuthorizationFinalizeAmountParamsFleetReportedBreakdownTax,
        AuthorizationFinalizeAmountParamsFuel as AuthorizationFinalizeAmountParamsFuel,
    )
    from stripe.params.test_helpers.issuing._authorization_increment_params import (
        AuthorizationIncrementParams as AuthorizationIncrementParams,
    )
    from stripe.params.test_helpers.issuing._authorization_respond_params import (
        AuthorizationRespondParams as AuthorizationRespondParams,
    )
    from stripe.params.test_helpers.issuing._authorization_reverse_params import (
        AuthorizationReverseParams as AuthorizationReverseParams,
    )
    from stripe.params.test_helpers.issuing._card_deliver_card_params import (
        CardDeliverCardParams as CardDeliverCardParams,
    )
    from stripe.params.test_helpers.issuing._card_fail_card_params import (
        CardFailCardParams as CardFailCardParams,
    )
    from stripe.params.test_helpers.issuing._card_return_card_params import (
        CardReturnCardParams as CardReturnCardParams,
    )
    from stripe.params.test_helpers.issuing._card_ship_card_params import (
        CardShipCardParams as CardShipCardParams,
    )
    from stripe.params.test_helpers.issuing._card_submit_card_params import (
        CardSubmitCardParams as CardSubmitCardParams,
    )
    from stripe.params.test_helpers.issuing._personalization_design_activate_params import (
        PersonalizationDesignActivateParams as PersonalizationDesignActivateParams,
    )
    from stripe.params.test_helpers.issuing._personalization_design_deactivate_params import (
        PersonalizationDesignDeactivateParams as PersonalizationDesignDeactivateParams,
    )
    from stripe.params.test_helpers.issuing._personalization_design_reject_params import (
        PersonalizationDesignRejectParams as PersonalizationDesignRejectParams,
        PersonalizationDesignRejectParamsRejectionReasons as PersonalizationDesignRejectParamsRejectionReasons,
    )
    from stripe.params.test_helpers.issuing._transaction_create_force_capture_params import (
        TransactionCreateForceCaptureParams as TransactionCreateForceCaptureParams,
        TransactionCreateForceCaptureParamsMerchantData as TransactionCreateForceCaptureParamsMerchantData,
        TransactionCreateForceCaptureParamsPurchaseDetails as TransactionCreateForceCaptureParamsPurchaseDetails,
        TransactionCreateForceCaptureParamsPurchaseDetailsFleet as TransactionCreateForceCaptureParamsPurchaseDetailsFleet,
        TransactionCreateForceCaptureParamsPurchaseDetailsFleetCardholderPromptData as TransactionCreateForceCaptureParamsPurchaseDetailsFleetCardholderPromptData,
        TransactionCreateForceCaptureParamsPurchaseDetailsFleetReportedBreakdown as TransactionCreateForceCaptureParamsPurchaseDetailsFleetReportedBreakdown,
        TransactionCreateForceCaptureParamsPurchaseDetailsFleetReportedBreakdownFuel as TransactionCreateForceCaptureParamsPurchaseDetailsFleetReportedBreakdownFuel,
        TransactionCreateForceCaptureParamsPurchaseDetailsFleetReportedBreakdownNonFuel as TransactionCreateForceCaptureParamsPurchaseDetailsFleetReportedBreakdownNonFuel,
        TransactionCreateForceCaptureParamsPurchaseDetailsFleetReportedBreakdownTax as TransactionCreateForceCaptureParamsPurchaseDetailsFleetReportedBreakdownTax,
        TransactionCreateForceCaptureParamsPurchaseDetailsFlight as TransactionCreateForceCaptureParamsPurchaseDetailsFlight,
        TransactionCreateForceCaptureParamsPurchaseDetailsFlightSegment as TransactionCreateForceCaptureParamsPurchaseDetailsFlightSegment,
        TransactionCreateForceCaptureParamsPurchaseDetailsFuel as TransactionCreateForceCaptureParamsPurchaseDetailsFuel,
        TransactionCreateForceCaptureParamsPurchaseDetailsLodging as TransactionCreateForceCaptureParamsPurchaseDetailsLodging,
        TransactionCreateForceCaptureParamsPurchaseDetailsReceipt as TransactionCreateForceCaptureParamsPurchaseDetailsReceipt,
    )
    from stripe.params.test_helpers.issuing._transaction_create_unlinked_refund_params import (
        TransactionCreateUnlinkedRefundParams as TransactionCreateUnlinkedRefundParams,
        TransactionCreateUnlinkedRefundParamsMerchantData as TransactionCreateUnlinkedRefundParamsMerchantData,
        TransactionCreateUnlinkedRefundParamsPurchaseDetails as TransactionCreateUnlinkedRefundParamsPurchaseDetails,
        TransactionCreateUnlinkedRefundParamsPurchaseDetailsFleet as TransactionCreateUnlinkedRefundParamsPurchaseDetailsFleet,
        TransactionCreateUnlinkedRefundParamsPurchaseDetailsFleetCardholderPromptData as TransactionCreateUnlinkedRefundParamsPurchaseDetailsFleetCardholderPromptData,
        TransactionCreateUnlinkedRefundParamsPurchaseDetailsFleetReportedBreakdown as TransactionCreateUnlinkedRefundParamsPurchaseDetailsFleetReportedBreakdown,
        TransactionCreateUnlinkedRefundParamsPurchaseDetailsFleetReportedBreakdownFuel as TransactionCreateUnlinkedRefundParamsPurchaseDetailsFleetReportedBreakdownFuel,
        TransactionCreateUnlinkedRefundParamsPurchaseDetailsFleetReportedBreakdownNonFuel as TransactionCreateUnlinkedRefundParamsPurchaseDetailsFleetReportedBreakdownNonFuel,
        TransactionCreateUnlinkedRefundParamsPurchaseDetailsFleetReportedBreakdownTax as TransactionCreateUnlinkedRefundParamsPurchaseDetailsFleetReportedBreakdownTax,
        TransactionCreateUnlinkedRefundParamsPurchaseDetailsFlight as TransactionCreateUnlinkedRefundParamsPurchaseDetailsFlight,
        TransactionCreateUnlinkedRefundParamsPurchaseDetailsFlightSegment as TransactionCreateUnlinkedRefundParamsPurchaseDetailsFlightSegment,
        TransactionCreateUnlinkedRefundParamsPurchaseDetailsFuel as TransactionCreateUnlinkedRefundParamsPurchaseDetailsFuel,
        TransactionCreateUnlinkedRefundParamsPurchaseDetailsLodging as TransactionCreateUnlinkedRefundParamsPurchaseDetailsLodging,
        TransactionCreateUnlinkedRefundParamsPurchaseDetailsReceipt as TransactionCreateUnlinkedRefundParamsPurchaseDetailsReceipt,
    )
    from stripe.params.test_helpers.issuing._transaction_refund_params import (
        TransactionRefundParams as TransactionRefundParams,
    )

_submodules = {
    "AuthorizationCaptureParams": "stripe.params.test_helpers.issuing._authorization_capture_params",
    "AuthorizationCaptureParamsPurchaseDetails": "stripe.params.test_helpers.issuing._authorization_capture_params",
    "AuthorizationCaptureParamsPurchaseDetailsFleet": "stripe.params.test_helpers.issuing._authorization_capture_params",
    "AuthorizationCaptureParamsPurchaseDetailsFleetCardholderPromptData": "stripe.params.test_helpers.issuing._authorization_capture_params",
    "AuthorizationCaptureParamsPurchaseDetailsFleetReportedBreakdown": "stripe.params.test_helpers.issuing._authorization_capture_params",
    "AuthorizationCaptureParamsPurchaseDetailsFleetReportedBreakdownFuel": "stripe.params.test_helpers.issuing._authorization_capture_params",
    "AuthorizationCaptureParamsPurchaseDetailsFleetReportedBreakdownNonFuel": "stripe.params.test_helpers.issuing._authorization_capture_params",
    "AuthorizationCaptureParamsPurchaseDetailsFleetReportedBreakdownTax": "stripe.params.test_helpers.issuing._authorization_capture_params",
    "AuthorizationCaptureParamsPurchaseDetailsFlight": "stripe.params.test_helpers.issuing._authorization_capture_params",
    "AuthorizationCaptureParamsPurchaseDetailsFlightSegment": "stripe.params.test_helpers.issuing._authorization_capture_params",
    "AuthorizationCaptureParamsPurchaseDetailsFuel": "stripe.params.test_helpers.issuing._authorization_capture_params",
    "AuthorizationCaptureParamsPurchaseDetailsLodging": "stripe.params.test_helpers.issuing._authorization_capture_params",
    "AuthorizationCaptureParamsPurchaseDetailsReceipt": "stripe.params.test_helpers.issuing._authorization_capture_params",
    "AuthorizationCreateParams": "stripe.params.test_helpers.issuing._authorization_create_params",
    "AuthorizationCreateParamsAmountDetails": "stripe.params.test_helpers.issuing._authorization_create_params",
    "AuthorizationCreateParamsFleet": "stripe.params.test_helpers.issuing._authorization_create_params",
    "AuthorizationCreateParamsFleetCardholderPromptData": "stripe.params.test_helpers.issuing._authorization_create_params",
    "AuthorizationCreateParamsFleetReportedBreakdown": "stripe.params.test_helpers.issuing._authorization_create_params",
    "AuthorizationCreateParamsFleetReportedBreakdownFuel": "stripe.params.test_helpers.issuing._authorization_create_params",
    "AuthorizationCreateParamsFleetReportedBreakdownNonFuel": "stripe.params.test_helpers.issuing._authorization_create_params",
    "AuthorizationCreateParamsFleetReportedBreakdownTax": "stripe.params.test_helpers.issuing._authorization_create_params",
    "AuthorizationCreateParamsFuel": "stripe.params.test_helpers.issuing._authorization_create_params",
    "AuthorizationCreateParamsMerchantData": "stripe.params.test_helpers.issuing._authorization_create_params",
    "AuthorizationCreateParamsNetworkData": "stripe.params.test_helpers.issuing._authorization_create_params",
    "AuthorizationCreateParamsRiskAssessment": "stripe.params.test_helpers.issuing._authorization_create_params",
    "AuthorizationCreateParamsRiskAssessmentCardTestingRisk": "stripe.params.test_helpers.issuing._authorization_create_params",
    "AuthorizationCreateParamsRiskAssessmentMerchantDisputeRisk": "stripe.params.test_helpers.issuing._authorization_create_params",
    "AuthorizationCreateParamsVerificationData": "stripe.params.test_helpers.issuing._authorization_create_params",
    "AuthorizationCreateParamsVerificationDataAuthenticationExemption": "stripe.params.test_helpers.issuing._authorization_create_params",
    "AuthorizationCreateParamsVerificationDataThreeDSecure": "stripe.params.test_helpers.issuing._authorization_create_params",
    "AuthorizationExpireParams": "stripe.params.test_helpers.issuing._authorization_expire_params",
    "AuthorizationFinalizeAmountParams": "stripe.params.test_helpers.issuing._authorization_finalize_amount_params",
    "AuthorizationFinalizeAmountParamsFleet": "stripe.params.test_helpers.issuing._authorization_finalize_amount_params",
    "AuthorizationFinalizeAmountParamsFleetCardholderPromptData": "stripe.params.test_helpers.issuing._authorization_finalize_amount_params",
    "AuthorizationFinalizeAmountParamsFleetReportedBreakdown": "stripe.params.test_helpers.issuing._authorization_finalize_amount_params",
    "AuthorizationFinalizeAmountParamsFleetReportedBreakdownFuel": "stripe.params.test_helpers.issuing._authorization_finalize_amount_params",
    "AuthorizationFinalizeAmountParamsFleetReportedBreakdownNonFuel": "stripe.params.test_helpers.issuing._authorization_finalize_amount_params",
    "AuthorizationFinalizeAmountParamsFleetReportedBreakdownTax": "stripe.params.test_helpers.issuing._authorization_finalize_amount_params",
    "AuthorizationFinalizeAmountParamsFuel": "stripe.params.test_helpers.issuing._authorization_finalize_amount_params",
    "AuthorizationIncrementParams": "stripe.params.test_helpers.issuing._authorization_increment_params",
    "AuthorizationRespondParams": "stripe.params.test_helpers.issuing._authorization_respond_params",
    "AuthorizationReverseParams": "stripe.params.test_helpers.issuing._authorization_reverse_params",
    "CardDeliverCardParams": "stripe.params.test_helpers.issuing._card_deliver_card_params",
    "CardFailCardParams": "stripe.params.test_helpers.issuing._card_fail_card_params",
    "CardReturnCardParams": "stripe.params.test_helpers.issuing._card_return_card_params",
    "CardShipCardParams": "stripe.params.test_helpers.issuing._card_ship_card_params",
    "CardSubmitCardParams": "stripe.params.test_helpers.issuing._card_submit_card_params",
    "PersonalizationDesignActivateParams": "stripe.params.test_helpers.issuing._personalization_design_activate_params",
    "PersonalizationDesignDeactivateParams": "stripe.params.test_helpers.issuing._personalization_design_deactivate_params",
    "PersonalizationDesignRejectParams": "stripe.params.test_helpers.issuing._personalization_design_reject_params",
    "PersonalizationDesignRejectParamsRejectionReasons": "stripe.params.test_helpers.issuing._personalization_design_reject_params",
    "TransactionCreateForceCaptureParams": "stripe.params.test_helpers.issuing._transaction_create_force_capture_params",
    "TransactionCreateForceCaptureParamsMerchantData": "stripe.params.test_helpers.issuing._transaction_create_force_capture_params",
    "TransactionCreateForceCaptureParamsPurchaseDetails": "stripe.params.test_helpers.issuing._transaction_create_force_capture_params",
    "TransactionCreateForceCaptureParamsPurchaseDetailsFleet": "stripe.params.test_helpers.issuing._transaction_create_force_capture_params",
    "TransactionCreateForceCaptureParamsPurchaseDetailsFleetCardholderPromptData": "stripe.params.test_helpers.issuing._transaction_create_force_capture_params",
    "TransactionCreateForceCaptureParamsPurchaseDetailsFleetReportedBreakdown": "stripe.params.test_helpers.issuing._transaction_create_force_capture_params",
    "TransactionCreateForceCaptureParamsPurchaseDetailsFleetReportedBreakdownFuel": "stripe.params.test_helpers.issuing._transaction_create_force_capture_params",
    "TransactionCreateForceCaptureParamsPurchaseDetailsFleetReportedBreakdownNonFuel": "stripe.params.test_helpers.issuing._transaction_create_force_capture_params",
    "TransactionCreateForceCaptureParamsPurchaseDetailsFleetReportedBreakdownTax": "stripe.params.test_helpers.issuing._transaction_create_force_capture_params",
    "TransactionCreateForceCaptureParamsPurchaseDetailsFlight": "stripe.params.test_helpers.issuing._transaction_create_force_capture_params",
    "TransactionCreateForceCaptureParamsPurchaseDetailsFlightSegment": "stripe.params.test_helpers.issuing._transaction_create_force_capture_params",
    "TransactionCreateForceCaptureParamsPurchaseDetailsFuel": "stripe.params.test_helpers.issuing._transaction_create_force_capture_params",
    "TransactionCreateForceCaptureParamsPurchaseDetailsLodging": "stripe.params.test_helpers.issuing._transaction_create_force_capture_params",
    "TransactionCreateForceCaptureParamsPurchaseDetailsReceipt": "stripe.params.test_helpers.issuing._transaction_create_force_capture_params",
    "TransactionCreateUnlinkedRefundParams": "stripe.params.test_helpers.issuing._transaction_create_unlinked_refund_params",
    "TransactionCreateUnlinkedRefundParamsMerchantData": "stripe.params.test_helpers.issuing._transaction_create_unlinked_refund_params",
    "TransactionCreateUnlinkedRefundParamsPurchaseDetails": "stripe.params.test_helpers.issuing._transaction_create_unlinked_refund_params",
    "TransactionCreateUnlinkedRefundParamsPurchaseDetailsFleet": "stripe.params.test_helpers.issuing._transaction_create_unlinked_refund_params",
    "TransactionCreateUnlinkedRefundParamsPurchaseDetailsFleetCardholderPromptData": "stripe.params.test_helpers.issuing._transaction_create_unlinked_refund_params",
    "TransactionCreateUnlinkedRefundParamsPurchaseDetailsFleetReportedBreakdown": "stripe.params.test_helpers.issuing._transaction_create_unlinked_refund_params",
    "TransactionCreateUnlinkedRefundParamsPurchaseDetailsFleetReportedBreakdownFuel": "stripe.params.test_helpers.issuing._transaction_create_unlinked_refund_params",
    "TransactionCreateUnlinkedRefundParamsPurchaseDetailsFleetReportedBreakdownNonFuel": "stripe.params.test_helpers.issuing._transaction_create_unlinked_refund_params",
    "TransactionCreateUnlinkedRefundParamsPurchaseDetailsFleetReportedBreakdownTax": "stripe.params.test_helpers.issuing._transaction_create_unlinked_refund_params",
    "TransactionCreateUnlinkedRefundParamsPurchaseDetailsFlight": "stripe.params.test_helpers.issuing._transaction_create_unlinked_refund_params",
    "TransactionCreateUnlinkedRefundParamsPurchaseDetailsFlightSegment": "stripe.params.test_helpers.issuing._transaction_create_unlinked_refund_params",
    "TransactionCreateUnlinkedRefundParamsPurchaseDetailsFuel": "stripe.params.test_helpers.issuing._transaction_create_unlinked_refund_params",
    "TransactionCreateUnlinkedRefundParamsPurchaseDetailsLodging": "stripe.params.test_helpers.issuing._transaction_create_unlinked_refund_params",
    "TransactionCreateUnlinkedRefundParamsPurchaseDetailsReceipt": "stripe.params.test_helpers.issuing._transaction_create_unlinked_refund_params",
    "TransactionRefundParams": "stripe.params.test_helpers.issuing._transaction_refund_params",
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
