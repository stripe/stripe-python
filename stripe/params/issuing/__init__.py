# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.issuing._authorization_approve_params import (
        AuthorizationApproveParams as AuthorizationApproveParams,
    )
    from stripe.params.issuing._authorization_capture_params import (
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
    from stripe.params.issuing._authorization_create_params import (
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
    from stripe.params.issuing._authorization_decline_params import (
        AuthorizationDeclineParams as AuthorizationDeclineParams,
    )
    from stripe.params.issuing._authorization_expire_params import (
        AuthorizationExpireParams as AuthorizationExpireParams,
    )
    from stripe.params.issuing._authorization_finalize_amount_params import (
        AuthorizationFinalizeAmountParams as AuthorizationFinalizeAmountParams,
        AuthorizationFinalizeAmountParamsFleet as AuthorizationFinalizeAmountParamsFleet,
        AuthorizationFinalizeAmountParamsFleetCardholderPromptData as AuthorizationFinalizeAmountParamsFleetCardholderPromptData,
        AuthorizationFinalizeAmountParamsFleetReportedBreakdown as AuthorizationFinalizeAmountParamsFleetReportedBreakdown,
        AuthorizationFinalizeAmountParamsFleetReportedBreakdownFuel as AuthorizationFinalizeAmountParamsFleetReportedBreakdownFuel,
        AuthorizationFinalizeAmountParamsFleetReportedBreakdownNonFuel as AuthorizationFinalizeAmountParamsFleetReportedBreakdownNonFuel,
        AuthorizationFinalizeAmountParamsFleetReportedBreakdownTax as AuthorizationFinalizeAmountParamsFleetReportedBreakdownTax,
        AuthorizationFinalizeAmountParamsFuel as AuthorizationFinalizeAmountParamsFuel,
    )
    from stripe.params.issuing._authorization_increment_params import (
        AuthorizationIncrementParams as AuthorizationIncrementParams,
    )
    from stripe.params.issuing._authorization_list_params import (
        AuthorizationListParams as AuthorizationListParams,
        AuthorizationListParamsCreated as AuthorizationListParamsCreated,
    )
    from stripe.params.issuing._authorization_modify_params import (
        AuthorizationModifyParams as AuthorizationModifyParams,
    )
    from stripe.params.issuing._authorization_respond_params import (
        AuthorizationRespondParams as AuthorizationRespondParams,
    )
    from stripe.params.issuing._authorization_retrieve_params import (
        AuthorizationRetrieveParams as AuthorizationRetrieveParams,
    )
    from stripe.params.issuing._authorization_reverse_params import (
        AuthorizationReverseParams as AuthorizationReverseParams,
    )
    from stripe.params.issuing._authorization_update_params import (
        AuthorizationUpdateParams as AuthorizationUpdateParams,
    )
    from stripe.params.issuing._card_create_params import (
        CardCreateParams as CardCreateParams,
        CardCreateParamsPin as CardCreateParamsPin,
        CardCreateParamsShipping as CardCreateParamsShipping,
        CardCreateParamsShippingAddress as CardCreateParamsShippingAddress,
        CardCreateParamsShippingAddressValidation as CardCreateParamsShippingAddressValidation,
        CardCreateParamsShippingCustoms as CardCreateParamsShippingCustoms,
        CardCreateParamsSpendingControls as CardCreateParamsSpendingControls,
        CardCreateParamsSpendingControlsSpendingLimit as CardCreateParamsSpendingControlsSpendingLimit,
    )
    from stripe.params.issuing._card_deliver_card_params import (
        CardDeliverCardParams as CardDeliverCardParams,
    )
    from stripe.params.issuing._card_fail_card_params import (
        CardFailCardParams as CardFailCardParams,
    )
    from stripe.params.issuing._card_list_params import (
        CardListParams as CardListParams,
        CardListParamsCreated as CardListParamsCreated,
    )
    from stripe.params.issuing._card_modify_params import (
        CardModifyParams as CardModifyParams,
        CardModifyParamsPin as CardModifyParamsPin,
        CardModifyParamsShipping as CardModifyParamsShipping,
        CardModifyParamsShippingAddress as CardModifyParamsShippingAddress,
        CardModifyParamsShippingAddressValidation as CardModifyParamsShippingAddressValidation,
        CardModifyParamsShippingCustoms as CardModifyParamsShippingCustoms,
        CardModifyParamsSpendingControls as CardModifyParamsSpendingControls,
        CardModifyParamsSpendingControlsSpendingLimit as CardModifyParamsSpendingControlsSpendingLimit,
    )
    from stripe.params.issuing._card_retrieve_params import (
        CardRetrieveParams as CardRetrieveParams,
    )
    from stripe.params.issuing._card_return_card_params import (
        CardReturnCardParams as CardReturnCardParams,
    )
    from stripe.params.issuing._card_ship_card_params import (
        CardShipCardParams as CardShipCardParams,
    )
    from stripe.params.issuing._card_submit_card_params import (
        CardSubmitCardParams as CardSubmitCardParams,
    )
    from stripe.params.issuing._card_update_params import (
        CardUpdateParams as CardUpdateParams,
        CardUpdateParamsPin as CardUpdateParamsPin,
        CardUpdateParamsShipping as CardUpdateParamsShipping,
        CardUpdateParamsShippingAddress as CardUpdateParamsShippingAddress,
        CardUpdateParamsShippingAddressValidation as CardUpdateParamsShippingAddressValidation,
        CardUpdateParamsShippingCustoms as CardUpdateParamsShippingCustoms,
        CardUpdateParamsSpendingControls as CardUpdateParamsSpendingControls,
        CardUpdateParamsSpendingControlsSpendingLimit as CardUpdateParamsSpendingControlsSpendingLimit,
    )
    from stripe.params.issuing._cardholder_create_params import (
        CardholderCreateParams as CardholderCreateParams,
        CardholderCreateParamsBilling as CardholderCreateParamsBilling,
        CardholderCreateParamsBillingAddress as CardholderCreateParamsBillingAddress,
        CardholderCreateParamsCompany as CardholderCreateParamsCompany,
        CardholderCreateParamsIndividual as CardholderCreateParamsIndividual,
        CardholderCreateParamsIndividualCardIssuing as CardholderCreateParamsIndividualCardIssuing,
        CardholderCreateParamsIndividualCardIssuingUserTermsAcceptance as CardholderCreateParamsIndividualCardIssuingUserTermsAcceptance,
        CardholderCreateParamsIndividualDob as CardholderCreateParamsIndividualDob,
        CardholderCreateParamsIndividualVerification as CardholderCreateParamsIndividualVerification,
        CardholderCreateParamsIndividualVerificationDocument as CardholderCreateParamsIndividualVerificationDocument,
        CardholderCreateParamsSpendingControls as CardholderCreateParamsSpendingControls,
        CardholderCreateParamsSpendingControlsSpendingLimit as CardholderCreateParamsSpendingControlsSpendingLimit,
    )
    from stripe.params.issuing._cardholder_list_params import (
        CardholderListParams as CardholderListParams,
        CardholderListParamsCreated as CardholderListParamsCreated,
    )
    from stripe.params.issuing._cardholder_modify_params import (
        CardholderModifyParams as CardholderModifyParams,
        CardholderModifyParamsBilling as CardholderModifyParamsBilling,
        CardholderModifyParamsBillingAddress as CardholderModifyParamsBillingAddress,
        CardholderModifyParamsCompany as CardholderModifyParamsCompany,
        CardholderModifyParamsIndividual as CardholderModifyParamsIndividual,
        CardholderModifyParamsIndividualCardIssuing as CardholderModifyParamsIndividualCardIssuing,
        CardholderModifyParamsIndividualCardIssuingUserTermsAcceptance as CardholderModifyParamsIndividualCardIssuingUserTermsAcceptance,
        CardholderModifyParamsIndividualDob as CardholderModifyParamsIndividualDob,
        CardholderModifyParamsIndividualVerification as CardholderModifyParamsIndividualVerification,
        CardholderModifyParamsIndividualVerificationDocument as CardholderModifyParamsIndividualVerificationDocument,
        CardholderModifyParamsSpendingControls as CardholderModifyParamsSpendingControls,
        CardholderModifyParamsSpendingControlsSpendingLimit as CardholderModifyParamsSpendingControlsSpendingLimit,
    )
    from stripe.params.issuing._cardholder_retrieve_params import (
        CardholderRetrieveParams as CardholderRetrieveParams,
    )
    from stripe.params.issuing._cardholder_update_params import (
        CardholderUpdateParams as CardholderUpdateParams,
        CardholderUpdateParamsBilling as CardholderUpdateParamsBilling,
        CardholderUpdateParamsBillingAddress as CardholderUpdateParamsBillingAddress,
        CardholderUpdateParamsCompany as CardholderUpdateParamsCompany,
        CardholderUpdateParamsIndividual as CardholderUpdateParamsIndividual,
        CardholderUpdateParamsIndividualCardIssuing as CardholderUpdateParamsIndividualCardIssuing,
        CardholderUpdateParamsIndividualCardIssuingUserTermsAcceptance as CardholderUpdateParamsIndividualCardIssuingUserTermsAcceptance,
        CardholderUpdateParamsIndividualDob as CardholderUpdateParamsIndividualDob,
        CardholderUpdateParamsIndividualVerification as CardholderUpdateParamsIndividualVerification,
        CardholderUpdateParamsIndividualVerificationDocument as CardholderUpdateParamsIndividualVerificationDocument,
        CardholderUpdateParamsSpendingControls as CardholderUpdateParamsSpendingControls,
        CardholderUpdateParamsSpendingControlsSpendingLimit as CardholderUpdateParamsSpendingControlsSpendingLimit,
    )
    from stripe.params.issuing._dispute_create_params import (
        DisputeCreateParams as DisputeCreateParams,
        DisputeCreateParamsEvidence as DisputeCreateParamsEvidence,
        DisputeCreateParamsEvidenceCanceled as DisputeCreateParamsEvidenceCanceled,
        DisputeCreateParamsEvidenceDuplicate as DisputeCreateParamsEvidenceDuplicate,
        DisputeCreateParamsEvidenceFraudulent as DisputeCreateParamsEvidenceFraudulent,
        DisputeCreateParamsEvidenceMerchandiseNotAsDescribed as DisputeCreateParamsEvidenceMerchandiseNotAsDescribed,
        DisputeCreateParamsEvidenceNoValidAuthorization as DisputeCreateParamsEvidenceNoValidAuthorization,
        DisputeCreateParamsEvidenceNotReceived as DisputeCreateParamsEvidenceNotReceived,
        DisputeCreateParamsEvidenceOther as DisputeCreateParamsEvidenceOther,
        DisputeCreateParamsEvidenceServiceNotAsDescribed as DisputeCreateParamsEvidenceServiceNotAsDescribed,
        DisputeCreateParamsTreasury as DisputeCreateParamsTreasury,
    )
    from stripe.params.issuing._dispute_list_params import (
        DisputeListParams as DisputeListParams,
        DisputeListParamsCreated as DisputeListParamsCreated,
    )
    from stripe.params.issuing._dispute_modify_params import (
        DisputeModifyParams as DisputeModifyParams,
        DisputeModifyParamsEvidence as DisputeModifyParamsEvidence,
        DisputeModifyParamsEvidenceCanceled as DisputeModifyParamsEvidenceCanceled,
        DisputeModifyParamsEvidenceDuplicate as DisputeModifyParamsEvidenceDuplicate,
        DisputeModifyParamsEvidenceFraudulent as DisputeModifyParamsEvidenceFraudulent,
        DisputeModifyParamsEvidenceMerchandiseNotAsDescribed as DisputeModifyParamsEvidenceMerchandiseNotAsDescribed,
        DisputeModifyParamsEvidenceNoValidAuthorization as DisputeModifyParamsEvidenceNoValidAuthorization,
        DisputeModifyParamsEvidenceNotReceived as DisputeModifyParamsEvidenceNotReceived,
        DisputeModifyParamsEvidenceOther as DisputeModifyParamsEvidenceOther,
        DisputeModifyParamsEvidenceServiceNotAsDescribed as DisputeModifyParamsEvidenceServiceNotAsDescribed,
    )
    from stripe.params.issuing._dispute_retrieve_params import (
        DisputeRetrieveParams as DisputeRetrieveParams,
    )
    from stripe.params.issuing._dispute_submit_params import (
        DisputeSubmitParams as DisputeSubmitParams,
    )
    from stripe.params.issuing._dispute_update_params import (
        DisputeUpdateParams as DisputeUpdateParams,
        DisputeUpdateParamsEvidence as DisputeUpdateParamsEvidence,
        DisputeUpdateParamsEvidenceCanceled as DisputeUpdateParamsEvidenceCanceled,
        DisputeUpdateParamsEvidenceDuplicate as DisputeUpdateParamsEvidenceDuplicate,
        DisputeUpdateParamsEvidenceFraudulent as DisputeUpdateParamsEvidenceFraudulent,
        DisputeUpdateParamsEvidenceMerchandiseNotAsDescribed as DisputeUpdateParamsEvidenceMerchandiseNotAsDescribed,
        DisputeUpdateParamsEvidenceNoValidAuthorization as DisputeUpdateParamsEvidenceNoValidAuthorization,
        DisputeUpdateParamsEvidenceNotReceived as DisputeUpdateParamsEvidenceNotReceived,
        DisputeUpdateParamsEvidenceOther as DisputeUpdateParamsEvidenceOther,
        DisputeUpdateParamsEvidenceServiceNotAsDescribed as DisputeUpdateParamsEvidenceServiceNotAsDescribed,
    )
    from stripe.params.issuing._personalization_design_activate_params import (
        PersonalizationDesignActivateParams as PersonalizationDesignActivateParams,
    )
    from stripe.params.issuing._personalization_design_create_params import (
        PersonalizationDesignCreateParams as PersonalizationDesignCreateParams,
        PersonalizationDesignCreateParamsCarrierText as PersonalizationDesignCreateParamsCarrierText,
        PersonalizationDesignCreateParamsPreferences as PersonalizationDesignCreateParamsPreferences,
    )
    from stripe.params.issuing._personalization_design_deactivate_params import (
        PersonalizationDesignDeactivateParams as PersonalizationDesignDeactivateParams,
    )
    from stripe.params.issuing._personalization_design_list_params import (
        PersonalizationDesignListParams as PersonalizationDesignListParams,
        PersonalizationDesignListParamsPreferences as PersonalizationDesignListParamsPreferences,
    )
    from stripe.params.issuing._personalization_design_modify_params import (
        PersonalizationDesignModifyParams as PersonalizationDesignModifyParams,
        PersonalizationDesignModifyParamsCarrierText as PersonalizationDesignModifyParamsCarrierText,
        PersonalizationDesignModifyParamsPreferences as PersonalizationDesignModifyParamsPreferences,
    )
    from stripe.params.issuing._personalization_design_reject_params import (
        PersonalizationDesignRejectParams as PersonalizationDesignRejectParams,
        PersonalizationDesignRejectParamsRejectionReasons as PersonalizationDesignRejectParamsRejectionReasons,
    )
    from stripe.params.issuing._personalization_design_retrieve_params import (
        PersonalizationDesignRetrieveParams as PersonalizationDesignRetrieveParams,
    )
    from stripe.params.issuing._personalization_design_update_params import (
        PersonalizationDesignUpdateParams as PersonalizationDesignUpdateParams,
        PersonalizationDesignUpdateParamsCarrierText as PersonalizationDesignUpdateParamsCarrierText,
        PersonalizationDesignUpdateParamsPreferences as PersonalizationDesignUpdateParamsPreferences,
    )
    from stripe.params.issuing._physical_bundle_list_params import (
        PhysicalBundleListParams as PhysicalBundleListParams,
    )
    from stripe.params.issuing._physical_bundle_retrieve_params import (
        PhysicalBundleRetrieveParams as PhysicalBundleRetrieveParams,
    )
    from stripe.params.issuing._token_list_params import (
        TokenListParams as TokenListParams,
        TokenListParamsCreated as TokenListParamsCreated,
    )
    from stripe.params.issuing._token_modify_params import (
        TokenModifyParams as TokenModifyParams,
    )
    from stripe.params.issuing._token_retrieve_params import (
        TokenRetrieveParams as TokenRetrieveParams,
    )
    from stripe.params.issuing._token_update_params import (
        TokenUpdateParams as TokenUpdateParams,
    )
    from stripe.params.issuing._transaction_create_force_capture_params import (
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
    from stripe.params.issuing._transaction_create_unlinked_refund_params import (
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
    from stripe.params.issuing._transaction_list_params import (
        TransactionListParams as TransactionListParams,
        TransactionListParamsCreated as TransactionListParamsCreated,
    )
    from stripe.params.issuing._transaction_modify_params import (
        TransactionModifyParams as TransactionModifyParams,
    )
    from stripe.params.issuing._transaction_refund_params import (
        TransactionRefundParams as TransactionRefundParams,
    )
    from stripe.params.issuing._transaction_retrieve_params import (
        TransactionRetrieveParams as TransactionRetrieveParams,
    )
    from stripe.params.issuing._transaction_update_params import (
        TransactionUpdateParams as TransactionUpdateParams,
    )

_submodules = {
    "AuthorizationApproveParams": "stripe.params.issuing._authorization_approve_params",
    "AuthorizationCaptureParams": "stripe.params.issuing._authorization_capture_params",
    "AuthorizationCaptureParamsPurchaseDetails": "stripe.params.issuing._authorization_capture_params",
    "AuthorizationCaptureParamsPurchaseDetailsFleet": "stripe.params.issuing._authorization_capture_params",
    "AuthorizationCaptureParamsPurchaseDetailsFleetCardholderPromptData": "stripe.params.issuing._authorization_capture_params",
    "AuthorizationCaptureParamsPurchaseDetailsFleetReportedBreakdown": "stripe.params.issuing._authorization_capture_params",
    "AuthorizationCaptureParamsPurchaseDetailsFleetReportedBreakdownFuel": "stripe.params.issuing._authorization_capture_params",
    "AuthorizationCaptureParamsPurchaseDetailsFleetReportedBreakdownNonFuel": "stripe.params.issuing._authorization_capture_params",
    "AuthorizationCaptureParamsPurchaseDetailsFleetReportedBreakdownTax": "stripe.params.issuing._authorization_capture_params",
    "AuthorizationCaptureParamsPurchaseDetailsFlight": "stripe.params.issuing._authorization_capture_params",
    "AuthorizationCaptureParamsPurchaseDetailsFlightSegment": "stripe.params.issuing._authorization_capture_params",
    "AuthorizationCaptureParamsPurchaseDetailsFuel": "stripe.params.issuing._authorization_capture_params",
    "AuthorizationCaptureParamsPurchaseDetailsLodging": "stripe.params.issuing._authorization_capture_params",
    "AuthorizationCaptureParamsPurchaseDetailsReceipt": "stripe.params.issuing._authorization_capture_params",
    "AuthorizationCreateParams": "stripe.params.issuing._authorization_create_params",
    "AuthorizationCreateParamsAmountDetails": "stripe.params.issuing._authorization_create_params",
    "AuthorizationCreateParamsFleet": "stripe.params.issuing._authorization_create_params",
    "AuthorizationCreateParamsFleetCardholderPromptData": "stripe.params.issuing._authorization_create_params",
    "AuthorizationCreateParamsFleetReportedBreakdown": "stripe.params.issuing._authorization_create_params",
    "AuthorizationCreateParamsFleetReportedBreakdownFuel": "stripe.params.issuing._authorization_create_params",
    "AuthorizationCreateParamsFleetReportedBreakdownNonFuel": "stripe.params.issuing._authorization_create_params",
    "AuthorizationCreateParamsFleetReportedBreakdownTax": "stripe.params.issuing._authorization_create_params",
    "AuthorizationCreateParamsFuel": "stripe.params.issuing._authorization_create_params",
    "AuthorizationCreateParamsMerchantData": "stripe.params.issuing._authorization_create_params",
    "AuthorizationCreateParamsNetworkData": "stripe.params.issuing._authorization_create_params",
    "AuthorizationCreateParamsRiskAssessment": "stripe.params.issuing._authorization_create_params",
    "AuthorizationCreateParamsRiskAssessmentCardTestingRisk": "stripe.params.issuing._authorization_create_params",
    "AuthorizationCreateParamsRiskAssessmentMerchantDisputeRisk": "stripe.params.issuing._authorization_create_params",
    "AuthorizationCreateParamsVerificationData": "stripe.params.issuing._authorization_create_params",
    "AuthorizationCreateParamsVerificationDataAuthenticationExemption": "stripe.params.issuing._authorization_create_params",
    "AuthorizationCreateParamsVerificationDataThreeDSecure": "stripe.params.issuing._authorization_create_params",
    "AuthorizationDeclineParams": "stripe.params.issuing._authorization_decline_params",
    "AuthorizationExpireParams": "stripe.params.issuing._authorization_expire_params",
    "AuthorizationFinalizeAmountParams": "stripe.params.issuing._authorization_finalize_amount_params",
    "AuthorizationFinalizeAmountParamsFleet": "stripe.params.issuing._authorization_finalize_amount_params",
    "AuthorizationFinalizeAmountParamsFleetCardholderPromptData": "stripe.params.issuing._authorization_finalize_amount_params",
    "AuthorizationFinalizeAmountParamsFleetReportedBreakdown": "stripe.params.issuing._authorization_finalize_amount_params",
    "AuthorizationFinalizeAmountParamsFleetReportedBreakdownFuel": "stripe.params.issuing._authorization_finalize_amount_params",
    "AuthorizationFinalizeAmountParamsFleetReportedBreakdownNonFuel": "stripe.params.issuing._authorization_finalize_amount_params",
    "AuthorizationFinalizeAmountParamsFleetReportedBreakdownTax": "stripe.params.issuing._authorization_finalize_amount_params",
    "AuthorizationFinalizeAmountParamsFuel": "stripe.params.issuing._authorization_finalize_amount_params",
    "AuthorizationIncrementParams": "stripe.params.issuing._authorization_increment_params",
    "AuthorizationListParams": "stripe.params.issuing._authorization_list_params",
    "AuthorizationListParamsCreated": "stripe.params.issuing._authorization_list_params",
    "AuthorizationModifyParams": "stripe.params.issuing._authorization_modify_params",
    "AuthorizationRespondParams": "stripe.params.issuing._authorization_respond_params",
    "AuthorizationRetrieveParams": "stripe.params.issuing._authorization_retrieve_params",
    "AuthorizationReverseParams": "stripe.params.issuing._authorization_reverse_params",
    "AuthorizationUpdateParams": "stripe.params.issuing._authorization_update_params",
    "CardCreateParams": "stripe.params.issuing._card_create_params",
    "CardCreateParamsPin": "stripe.params.issuing._card_create_params",
    "CardCreateParamsShipping": "stripe.params.issuing._card_create_params",
    "CardCreateParamsShippingAddress": "stripe.params.issuing._card_create_params",
    "CardCreateParamsShippingAddressValidation": "stripe.params.issuing._card_create_params",
    "CardCreateParamsShippingCustoms": "stripe.params.issuing._card_create_params",
    "CardCreateParamsSpendingControls": "stripe.params.issuing._card_create_params",
    "CardCreateParamsSpendingControlsSpendingLimit": "stripe.params.issuing._card_create_params",
    "CardDeliverCardParams": "stripe.params.issuing._card_deliver_card_params",
    "CardFailCardParams": "stripe.params.issuing._card_fail_card_params",
    "CardListParams": "stripe.params.issuing._card_list_params",
    "CardListParamsCreated": "stripe.params.issuing._card_list_params",
    "CardModifyParams": "stripe.params.issuing._card_modify_params",
    "CardModifyParamsPin": "stripe.params.issuing._card_modify_params",
    "CardModifyParamsShipping": "stripe.params.issuing._card_modify_params",
    "CardModifyParamsShippingAddress": "stripe.params.issuing._card_modify_params",
    "CardModifyParamsShippingAddressValidation": "stripe.params.issuing._card_modify_params",
    "CardModifyParamsShippingCustoms": "stripe.params.issuing._card_modify_params",
    "CardModifyParamsSpendingControls": "stripe.params.issuing._card_modify_params",
    "CardModifyParamsSpendingControlsSpendingLimit": "stripe.params.issuing._card_modify_params",
    "CardRetrieveParams": "stripe.params.issuing._card_retrieve_params",
    "CardReturnCardParams": "stripe.params.issuing._card_return_card_params",
    "CardShipCardParams": "stripe.params.issuing._card_ship_card_params",
    "CardSubmitCardParams": "stripe.params.issuing._card_submit_card_params",
    "CardUpdateParams": "stripe.params.issuing._card_update_params",
    "CardUpdateParamsPin": "stripe.params.issuing._card_update_params",
    "CardUpdateParamsShipping": "stripe.params.issuing._card_update_params",
    "CardUpdateParamsShippingAddress": "stripe.params.issuing._card_update_params",
    "CardUpdateParamsShippingAddressValidation": "stripe.params.issuing._card_update_params",
    "CardUpdateParamsShippingCustoms": "stripe.params.issuing._card_update_params",
    "CardUpdateParamsSpendingControls": "stripe.params.issuing._card_update_params",
    "CardUpdateParamsSpendingControlsSpendingLimit": "stripe.params.issuing._card_update_params",
    "CardholderCreateParams": "stripe.params.issuing._cardholder_create_params",
    "CardholderCreateParamsBilling": "stripe.params.issuing._cardholder_create_params",
    "CardholderCreateParamsBillingAddress": "stripe.params.issuing._cardholder_create_params",
    "CardholderCreateParamsCompany": "stripe.params.issuing._cardholder_create_params",
    "CardholderCreateParamsIndividual": "stripe.params.issuing._cardholder_create_params",
    "CardholderCreateParamsIndividualCardIssuing": "stripe.params.issuing._cardholder_create_params",
    "CardholderCreateParamsIndividualCardIssuingUserTermsAcceptance": "stripe.params.issuing._cardholder_create_params",
    "CardholderCreateParamsIndividualDob": "stripe.params.issuing._cardholder_create_params",
    "CardholderCreateParamsIndividualVerification": "stripe.params.issuing._cardholder_create_params",
    "CardholderCreateParamsIndividualVerificationDocument": "stripe.params.issuing._cardholder_create_params",
    "CardholderCreateParamsSpendingControls": "stripe.params.issuing._cardholder_create_params",
    "CardholderCreateParamsSpendingControlsSpendingLimit": "stripe.params.issuing._cardholder_create_params",
    "CardholderListParams": "stripe.params.issuing._cardholder_list_params",
    "CardholderListParamsCreated": "stripe.params.issuing._cardholder_list_params",
    "CardholderModifyParams": "stripe.params.issuing._cardholder_modify_params",
    "CardholderModifyParamsBilling": "stripe.params.issuing._cardholder_modify_params",
    "CardholderModifyParamsBillingAddress": "stripe.params.issuing._cardholder_modify_params",
    "CardholderModifyParamsCompany": "stripe.params.issuing._cardholder_modify_params",
    "CardholderModifyParamsIndividual": "stripe.params.issuing._cardholder_modify_params",
    "CardholderModifyParamsIndividualCardIssuing": "stripe.params.issuing._cardholder_modify_params",
    "CardholderModifyParamsIndividualCardIssuingUserTermsAcceptance": "stripe.params.issuing._cardholder_modify_params",
    "CardholderModifyParamsIndividualDob": "stripe.params.issuing._cardholder_modify_params",
    "CardholderModifyParamsIndividualVerification": "stripe.params.issuing._cardholder_modify_params",
    "CardholderModifyParamsIndividualVerificationDocument": "stripe.params.issuing._cardholder_modify_params",
    "CardholderModifyParamsSpendingControls": "stripe.params.issuing._cardholder_modify_params",
    "CardholderModifyParamsSpendingControlsSpendingLimit": "stripe.params.issuing._cardholder_modify_params",
    "CardholderRetrieveParams": "stripe.params.issuing._cardholder_retrieve_params",
    "CardholderUpdateParams": "stripe.params.issuing._cardholder_update_params",
    "CardholderUpdateParamsBilling": "stripe.params.issuing._cardholder_update_params",
    "CardholderUpdateParamsBillingAddress": "stripe.params.issuing._cardholder_update_params",
    "CardholderUpdateParamsCompany": "stripe.params.issuing._cardholder_update_params",
    "CardholderUpdateParamsIndividual": "stripe.params.issuing._cardholder_update_params",
    "CardholderUpdateParamsIndividualCardIssuing": "stripe.params.issuing._cardholder_update_params",
    "CardholderUpdateParamsIndividualCardIssuingUserTermsAcceptance": "stripe.params.issuing._cardholder_update_params",
    "CardholderUpdateParamsIndividualDob": "stripe.params.issuing._cardholder_update_params",
    "CardholderUpdateParamsIndividualVerification": "stripe.params.issuing._cardholder_update_params",
    "CardholderUpdateParamsIndividualVerificationDocument": "stripe.params.issuing._cardholder_update_params",
    "CardholderUpdateParamsSpendingControls": "stripe.params.issuing._cardholder_update_params",
    "CardholderUpdateParamsSpendingControlsSpendingLimit": "stripe.params.issuing._cardholder_update_params",
    "DisputeCreateParams": "stripe.params.issuing._dispute_create_params",
    "DisputeCreateParamsEvidence": "stripe.params.issuing._dispute_create_params",
    "DisputeCreateParamsEvidenceCanceled": "stripe.params.issuing._dispute_create_params",
    "DisputeCreateParamsEvidenceDuplicate": "stripe.params.issuing._dispute_create_params",
    "DisputeCreateParamsEvidenceFraudulent": "stripe.params.issuing._dispute_create_params",
    "DisputeCreateParamsEvidenceMerchandiseNotAsDescribed": "stripe.params.issuing._dispute_create_params",
    "DisputeCreateParamsEvidenceNoValidAuthorization": "stripe.params.issuing._dispute_create_params",
    "DisputeCreateParamsEvidenceNotReceived": "stripe.params.issuing._dispute_create_params",
    "DisputeCreateParamsEvidenceOther": "stripe.params.issuing._dispute_create_params",
    "DisputeCreateParamsEvidenceServiceNotAsDescribed": "stripe.params.issuing._dispute_create_params",
    "DisputeCreateParamsTreasury": "stripe.params.issuing._dispute_create_params",
    "DisputeListParams": "stripe.params.issuing._dispute_list_params",
    "DisputeListParamsCreated": "stripe.params.issuing._dispute_list_params",
    "DisputeModifyParams": "stripe.params.issuing._dispute_modify_params",
    "DisputeModifyParamsEvidence": "stripe.params.issuing._dispute_modify_params",
    "DisputeModifyParamsEvidenceCanceled": "stripe.params.issuing._dispute_modify_params",
    "DisputeModifyParamsEvidenceDuplicate": "stripe.params.issuing._dispute_modify_params",
    "DisputeModifyParamsEvidenceFraudulent": "stripe.params.issuing._dispute_modify_params",
    "DisputeModifyParamsEvidenceMerchandiseNotAsDescribed": "stripe.params.issuing._dispute_modify_params",
    "DisputeModifyParamsEvidenceNoValidAuthorization": "stripe.params.issuing._dispute_modify_params",
    "DisputeModifyParamsEvidenceNotReceived": "stripe.params.issuing._dispute_modify_params",
    "DisputeModifyParamsEvidenceOther": "stripe.params.issuing._dispute_modify_params",
    "DisputeModifyParamsEvidenceServiceNotAsDescribed": "stripe.params.issuing._dispute_modify_params",
    "DisputeRetrieveParams": "stripe.params.issuing._dispute_retrieve_params",
    "DisputeSubmitParams": "stripe.params.issuing._dispute_submit_params",
    "DisputeUpdateParams": "stripe.params.issuing._dispute_update_params",
    "DisputeUpdateParamsEvidence": "stripe.params.issuing._dispute_update_params",
    "DisputeUpdateParamsEvidenceCanceled": "stripe.params.issuing._dispute_update_params",
    "DisputeUpdateParamsEvidenceDuplicate": "stripe.params.issuing._dispute_update_params",
    "DisputeUpdateParamsEvidenceFraudulent": "stripe.params.issuing._dispute_update_params",
    "DisputeUpdateParamsEvidenceMerchandiseNotAsDescribed": "stripe.params.issuing._dispute_update_params",
    "DisputeUpdateParamsEvidenceNoValidAuthorization": "stripe.params.issuing._dispute_update_params",
    "DisputeUpdateParamsEvidenceNotReceived": "stripe.params.issuing._dispute_update_params",
    "DisputeUpdateParamsEvidenceOther": "stripe.params.issuing._dispute_update_params",
    "DisputeUpdateParamsEvidenceServiceNotAsDescribed": "stripe.params.issuing._dispute_update_params",
    "PersonalizationDesignActivateParams": "stripe.params.issuing._personalization_design_activate_params",
    "PersonalizationDesignCreateParams": "stripe.params.issuing._personalization_design_create_params",
    "PersonalizationDesignCreateParamsCarrierText": "stripe.params.issuing._personalization_design_create_params",
    "PersonalizationDesignCreateParamsPreferences": "stripe.params.issuing._personalization_design_create_params",
    "PersonalizationDesignDeactivateParams": "stripe.params.issuing._personalization_design_deactivate_params",
    "PersonalizationDesignListParams": "stripe.params.issuing._personalization_design_list_params",
    "PersonalizationDesignListParamsPreferences": "stripe.params.issuing._personalization_design_list_params",
    "PersonalizationDesignModifyParams": "stripe.params.issuing._personalization_design_modify_params",
    "PersonalizationDesignModifyParamsCarrierText": "stripe.params.issuing._personalization_design_modify_params",
    "PersonalizationDesignModifyParamsPreferences": "stripe.params.issuing._personalization_design_modify_params",
    "PersonalizationDesignRejectParams": "stripe.params.issuing._personalization_design_reject_params",
    "PersonalizationDesignRejectParamsRejectionReasons": "stripe.params.issuing._personalization_design_reject_params",
    "PersonalizationDesignRetrieveParams": "stripe.params.issuing._personalization_design_retrieve_params",
    "PersonalizationDesignUpdateParams": "stripe.params.issuing._personalization_design_update_params",
    "PersonalizationDesignUpdateParamsCarrierText": "stripe.params.issuing._personalization_design_update_params",
    "PersonalizationDesignUpdateParamsPreferences": "stripe.params.issuing._personalization_design_update_params",
    "PhysicalBundleListParams": "stripe.params.issuing._physical_bundle_list_params",
    "PhysicalBundleRetrieveParams": "stripe.params.issuing._physical_bundle_retrieve_params",
    "TokenListParams": "stripe.params.issuing._token_list_params",
    "TokenListParamsCreated": "stripe.params.issuing._token_list_params",
    "TokenModifyParams": "stripe.params.issuing._token_modify_params",
    "TokenRetrieveParams": "stripe.params.issuing._token_retrieve_params",
    "TokenUpdateParams": "stripe.params.issuing._token_update_params",
    "TransactionCreateForceCaptureParams": "stripe.params.issuing._transaction_create_force_capture_params",
    "TransactionCreateForceCaptureParamsMerchantData": "stripe.params.issuing._transaction_create_force_capture_params",
    "TransactionCreateForceCaptureParamsPurchaseDetails": "stripe.params.issuing._transaction_create_force_capture_params",
    "TransactionCreateForceCaptureParamsPurchaseDetailsFleet": "stripe.params.issuing._transaction_create_force_capture_params",
    "TransactionCreateForceCaptureParamsPurchaseDetailsFleetCardholderPromptData": "stripe.params.issuing._transaction_create_force_capture_params",
    "TransactionCreateForceCaptureParamsPurchaseDetailsFleetReportedBreakdown": "stripe.params.issuing._transaction_create_force_capture_params",
    "TransactionCreateForceCaptureParamsPurchaseDetailsFleetReportedBreakdownFuel": "stripe.params.issuing._transaction_create_force_capture_params",
    "TransactionCreateForceCaptureParamsPurchaseDetailsFleetReportedBreakdownNonFuel": "stripe.params.issuing._transaction_create_force_capture_params",
    "TransactionCreateForceCaptureParamsPurchaseDetailsFleetReportedBreakdownTax": "stripe.params.issuing._transaction_create_force_capture_params",
    "TransactionCreateForceCaptureParamsPurchaseDetailsFlight": "stripe.params.issuing._transaction_create_force_capture_params",
    "TransactionCreateForceCaptureParamsPurchaseDetailsFlightSegment": "stripe.params.issuing._transaction_create_force_capture_params",
    "TransactionCreateForceCaptureParamsPurchaseDetailsFuel": "stripe.params.issuing._transaction_create_force_capture_params",
    "TransactionCreateForceCaptureParamsPurchaseDetailsLodging": "stripe.params.issuing._transaction_create_force_capture_params",
    "TransactionCreateForceCaptureParamsPurchaseDetailsReceipt": "stripe.params.issuing._transaction_create_force_capture_params",
    "TransactionCreateUnlinkedRefundParams": "stripe.params.issuing._transaction_create_unlinked_refund_params",
    "TransactionCreateUnlinkedRefundParamsMerchantData": "stripe.params.issuing._transaction_create_unlinked_refund_params",
    "TransactionCreateUnlinkedRefundParamsPurchaseDetails": "stripe.params.issuing._transaction_create_unlinked_refund_params",
    "TransactionCreateUnlinkedRefundParamsPurchaseDetailsFleet": "stripe.params.issuing._transaction_create_unlinked_refund_params",
    "TransactionCreateUnlinkedRefundParamsPurchaseDetailsFleetCardholderPromptData": "stripe.params.issuing._transaction_create_unlinked_refund_params",
    "TransactionCreateUnlinkedRefundParamsPurchaseDetailsFleetReportedBreakdown": "stripe.params.issuing._transaction_create_unlinked_refund_params",
    "TransactionCreateUnlinkedRefundParamsPurchaseDetailsFleetReportedBreakdownFuel": "stripe.params.issuing._transaction_create_unlinked_refund_params",
    "TransactionCreateUnlinkedRefundParamsPurchaseDetailsFleetReportedBreakdownNonFuel": "stripe.params.issuing._transaction_create_unlinked_refund_params",
    "TransactionCreateUnlinkedRefundParamsPurchaseDetailsFleetReportedBreakdownTax": "stripe.params.issuing._transaction_create_unlinked_refund_params",
    "TransactionCreateUnlinkedRefundParamsPurchaseDetailsFlight": "stripe.params.issuing._transaction_create_unlinked_refund_params",
    "TransactionCreateUnlinkedRefundParamsPurchaseDetailsFlightSegment": "stripe.params.issuing._transaction_create_unlinked_refund_params",
    "TransactionCreateUnlinkedRefundParamsPurchaseDetailsFuel": "stripe.params.issuing._transaction_create_unlinked_refund_params",
    "TransactionCreateUnlinkedRefundParamsPurchaseDetailsLodging": "stripe.params.issuing._transaction_create_unlinked_refund_params",
    "TransactionCreateUnlinkedRefundParamsPurchaseDetailsReceipt": "stripe.params.issuing._transaction_create_unlinked_refund_params",
    "TransactionListParams": "stripe.params.issuing._transaction_list_params",
    "TransactionListParamsCreated": "stripe.params.issuing._transaction_list_params",
    "TransactionModifyParams": "stripe.params.issuing._transaction_modify_params",
    "TransactionRefundParams": "stripe.params.issuing._transaction_refund_params",
    "TransactionRetrieveParams": "stripe.params.issuing._transaction_retrieve_params",
    "TransactionUpdateParams": "stripe.params.issuing._transaction_update_params",
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
