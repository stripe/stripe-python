# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.treasury._credit_reversal_create_params import (
        CreditReversalCreateParams as CreditReversalCreateParams,
    )
    from stripe.params.treasury._credit_reversal_list_params import (
        CreditReversalListParams as CreditReversalListParams,
    )
    from stripe.params.treasury._credit_reversal_retrieve_params import (
        CreditReversalRetrieveParams as CreditReversalRetrieveParams,
    )
    from stripe.params.treasury._debit_reversal_create_params import (
        DebitReversalCreateParams as DebitReversalCreateParams,
    )
    from stripe.params.treasury._debit_reversal_list_params import (
        DebitReversalListParams as DebitReversalListParams,
    )
    from stripe.params.treasury._debit_reversal_retrieve_params import (
        DebitReversalRetrieveParams as DebitReversalRetrieveParams,
    )
    from stripe.params.treasury._financial_account_close_params import (
        FinancialAccountCloseParams as FinancialAccountCloseParams,
        FinancialAccountCloseParamsForwardingSettings as FinancialAccountCloseParamsForwardingSettings,
    )
    from stripe.params.treasury._financial_account_create_params import (
        FinancialAccountCreateParams as FinancialAccountCreateParams,
        FinancialAccountCreateParamsFeatures as FinancialAccountCreateParamsFeatures,
        FinancialAccountCreateParamsFeaturesCardIssuing as FinancialAccountCreateParamsFeaturesCardIssuing,
        FinancialAccountCreateParamsFeaturesDepositInsurance as FinancialAccountCreateParamsFeaturesDepositInsurance,
        FinancialAccountCreateParamsFeaturesFinancialAddresses as FinancialAccountCreateParamsFeaturesFinancialAddresses,
        FinancialAccountCreateParamsFeaturesFinancialAddressesAba as FinancialAccountCreateParamsFeaturesFinancialAddressesAba,
        FinancialAccountCreateParamsFeaturesInboundTransfers as FinancialAccountCreateParamsFeaturesInboundTransfers,
        FinancialAccountCreateParamsFeaturesInboundTransfersAch as FinancialAccountCreateParamsFeaturesInboundTransfersAch,
        FinancialAccountCreateParamsFeaturesIntraStripeFlows as FinancialAccountCreateParamsFeaturesIntraStripeFlows,
        FinancialAccountCreateParamsFeaturesOutboundPayments as FinancialAccountCreateParamsFeaturesOutboundPayments,
        FinancialAccountCreateParamsFeaturesOutboundPaymentsAch as FinancialAccountCreateParamsFeaturesOutboundPaymentsAch,
        FinancialAccountCreateParamsFeaturesOutboundPaymentsUsDomesticWire as FinancialAccountCreateParamsFeaturesOutboundPaymentsUsDomesticWire,
        FinancialAccountCreateParamsFeaturesOutboundTransfers as FinancialAccountCreateParamsFeaturesOutboundTransfers,
        FinancialAccountCreateParamsFeaturesOutboundTransfersAch as FinancialAccountCreateParamsFeaturesOutboundTransfersAch,
        FinancialAccountCreateParamsFeaturesOutboundTransfersUsDomesticWire as FinancialAccountCreateParamsFeaturesOutboundTransfersUsDomesticWire,
        FinancialAccountCreateParamsPlatformRestrictions as FinancialAccountCreateParamsPlatformRestrictions,
    )
    from stripe.params.treasury._financial_account_features_retrieve_params import (
        FinancialAccountFeaturesRetrieveParams as FinancialAccountFeaturesRetrieveParams,
    )
    from stripe.params.treasury._financial_account_features_update_params import (
        FinancialAccountFeaturesUpdateParams as FinancialAccountFeaturesUpdateParams,
        FinancialAccountFeaturesUpdateParamsCardIssuing as FinancialAccountFeaturesUpdateParamsCardIssuing,
        FinancialAccountFeaturesUpdateParamsDepositInsurance as FinancialAccountFeaturesUpdateParamsDepositInsurance,
        FinancialAccountFeaturesUpdateParamsFinancialAddresses as FinancialAccountFeaturesUpdateParamsFinancialAddresses,
        FinancialAccountFeaturesUpdateParamsFinancialAddressesAba as FinancialAccountFeaturesUpdateParamsFinancialAddressesAba,
        FinancialAccountFeaturesUpdateParamsInboundTransfers as FinancialAccountFeaturesUpdateParamsInboundTransfers,
        FinancialAccountFeaturesUpdateParamsInboundTransfersAch as FinancialAccountFeaturesUpdateParamsInboundTransfersAch,
        FinancialAccountFeaturesUpdateParamsIntraStripeFlows as FinancialAccountFeaturesUpdateParamsIntraStripeFlows,
        FinancialAccountFeaturesUpdateParamsOutboundPayments as FinancialAccountFeaturesUpdateParamsOutboundPayments,
        FinancialAccountFeaturesUpdateParamsOutboundPaymentsAch as FinancialAccountFeaturesUpdateParamsOutboundPaymentsAch,
        FinancialAccountFeaturesUpdateParamsOutboundPaymentsUsDomesticWire as FinancialAccountFeaturesUpdateParamsOutboundPaymentsUsDomesticWire,
        FinancialAccountFeaturesUpdateParamsOutboundTransfers as FinancialAccountFeaturesUpdateParamsOutboundTransfers,
        FinancialAccountFeaturesUpdateParamsOutboundTransfersAch as FinancialAccountFeaturesUpdateParamsOutboundTransfersAch,
        FinancialAccountFeaturesUpdateParamsOutboundTransfersUsDomesticWire as FinancialAccountFeaturesUpdateParamsOutboundTransfersUsDomesticWire,
    )
    from stripe.params.treasury._financial_account_list_params import (
        FinancialAccountListParams as FinancialAccountListParams,
        FinancialAccountListParamsCreated as FinancialAccountListParamsCreated,
    )
    from stripe.params.treasury._financial_account_modify_params import (
        FinancialAccountModifyParams as FinancialAccountModifyParams,
        FinancialAccountModifyParamsFeatures as FinancialAccountModifyParamsFeatures,
        FinancialAccountModifyParamsFeaturesCardIssuing as FinancialAccountModifyParamsFeaturesCardIssuing,
        FinancialAccountModifyParamsFeaturesDepositInsurance as FinancialAccountModifyParamsFeaturesDepositInsurance,
        FinancialAccountModifyParamsFeaturesFinancialAddresses as FinancialAccountModifyParamsFeaturesFinancialAddresses,
        FinancialAccountModifyParamsFeaturesFinancialAddressesAba as FinancialAccountModifyParamsFeaturesFinancialAddressesAba,
        FinancialAccountModifyParamsFeaturesInboundTransfers as FinancialAccountModifyParamsFeaturesInboundTransfers,
        FinancialAccountModifyParamsFeaturesInboundTransfersAch as FinancialAccountModifyParamsFeaturesInboundTransfersAch,
        FinancialAccountModifyParamsFeaturesIntraStripeFlows as FinancialAccountModifyParamsFeaturesIntraStripeFlows,
        FinancialAccountModifyParamsFeaturesOutboundPayments as FinancialAccountModifyParamsFeaturesOutboundPayments,
        FinancialAccountModifyParamsFeaturesOutboundPaymentsAch as FinancialAccountModifyParamsFeaturesOutboundPaymentsAch,
        FinancialAccountModifyParamsFeaturesOutboundPaymentsUsDomesticWire as FinancialAccountModifyParamsFeaturesOutboundPaymentsUsDomesticWire,
        FinancialAccountModifyParamsFeaturesOutboundTransfers as FinancialAccountModifyParamsFeaturesOutboundTransfers,
        FinancialAccountModifyParamsFeaturesOutboundTransfersAch as FinancialAccountModifyParamsFeaturesOutboundTransfersAch,
        FinancialAccountModifyParamsFeaturesOutboundTransfersUsDomesticWire as FinancialAccountModifyParamsFeaturesOutboundTransfersUsDomesticWire,
        FinancialAccountModifyParamsForwardingSettings as FinancialAccountModifyParamsForwardingSettings,
        FinancialAccountModifyParamsPlatformRestrictions as FinancialAccountModifyParamsPlatformRestrictions,
    )
    from stripe.params.treasury._financial_account_retrieve_features_params import (
        FinancialAccountRetrieveFeaturesParams as FinancialAccountRetrieveFeaturesParams,
    )
    from stripe.params.treasury._financial_account_retrieve_params import (
        FinancialAccountRetrieveParams as FinancialAccountRetrieveParams,
    )
    from stripe.params.treasury._financial_account_update_features_params import (
        FinancialAccountUpdateFeaturesParams as FinancialAccountUpdateFeaturesParams,
        FinancialAccountUpdateFeaturesParamsCardIssuing as FinancialAccountUpdateFeaturesParamsCardIssuing,
        FinancialAccountUpdateFeaturesParamsDepositInsurance as FinancialAccountUpdateFeaturesParamsDepositInsurance,
        FinancialAccountUpdateFeaturesParamsFinancialAddresses as FinancialAccountUpdateFeaturesParamsFinancialAddresses,
        FinancialAccountUpdateFeaturesParamsFinancialAddressesAba as FinancialAccountUpdateFeaturesParamsFinancialAddressesAba,
        FinancialAccountUpdateFeaturesParamsInboundTransfers as FinancialAccountUpdateFeaturesParamsInboundTransfers,
        FinancialAccountUpdateFeaturesParamsInboundTransfersAch as FinancialAccountUpdateFeaturesParamsInboundTransfersAch,
        FinancialAccountUpdateFeaturesParamsIntraStripeFlows as FinancialAccountUpdateFeaturesParamsIntraStripeFlows,
        FinancialAccountUpdateFeaturesParamsOutboundPayments as FinancialAccountUpdateFeaturesParamsOutboundPayments,
        FinancialAccountUpdateFeaturesParamsOutboundPaymentsAch as FinancialAccountUpdateFeaturesParamsOutboundPaymentsAch,
        FinancialAccountUpdateFeaturesParamsOutboundPaymentsUsDomesticWire as FinancialAccountUpdateFeaturesParamsOutboundPaymentsUsDomesticWire,
        FinancialAccountUpdateFeaturesParamsOutboundTransfers as FinancialAccountUpdateFeaturesParamsOutboundTransfers,
        FinancialAccountUpdateFeaturesParamsOutboundTransfersAch as FinancialAccountUpdateFeaturesParamsOutboundTransfersAch,
        FinancialAccountUpdateFeaturesParamsOutboundTransfersUsDomesticWire as FinancialAccountUpdateFeaturesParamsOutboundTransfersUsDomesticWire,
    )
    from stripe.params.treasury._financial_account_update_params import (
        FinancialAccountUpdateParams as FinancialAccountUpdateParams,
        FinancialAccountUpdateParamsFeatures as FinancialAccountUpdateParamsFeatures,
        FinancialAccountUpdateParamsFeaturesCardIssuing as FinancialAccountUpdateParamsFeaturesCardIssuing,
        FinancialAccountUpdateParamsFeaturesDepositInsurance as FinancialAccountUpdateParamsFeaturesDepositInsurance,
        FinancialAccountUpdateParamsFeaturesFinancialAddresses as FinancialAccountUpdateParamsFeaturesFinancialAddresses,
        FinancialAccountUpdateParamsFeaturesFinancialAddressesAba as FinancialAccountUpdateParamsFeaturesFinancialAddressesAba,
        FinancialAccountUpdateParamsFeaturesInboundTransfers as FinancialAccountUpdateParamsFeaturesInboundTransfers,
        FinancialAccountUpdateParamsFeaturesInboundTransfersAch as FinancialAccountUpdateParamsFeaturesInboundTransfersAch,
        FinancialAccountUpdateParamsFeaturesIntraStripeFlows as FinancialAccountUpdateParamsFeaturesIntraStripeFlows,
        FinancialAccountUpdateParamsFeaturesOutboundPayments as FinancialAccountUpdateParamsFeaturesOutboundPayments,
        FinancialAccountUpdateParamsFeaturesOutboundPaymentsAch as FinancialAccountUpdateParamsFeaturesOutboundPaymentsAch,
        FinancialAccountUpdateParamsFeaturesOutboundPaymentsUsDomesticWire as FinancialAccountUpdateParamsFeaturesOutboundPaymentsUsDomesticWire,
        FinancialAccountUpdateParamsFeaturesOutboundTransfers as FinancialAccountUpdateParamsFeaturesOutboundTransfers,
        FinancialAccountUpdateParamsFeaturesOutboundTransfersAch as FinancialAccountUpdateParamsFeaturesOutboundTransfersAch,
        FinancialAccountUpdateParamsFeaturesOutboundTransfersUsDomesticWire as FinancialAccountUpdateParamsFeaturesOutboundTransfersUsDomesticWire,
        FinancialAccountUpdateParamsForwardingSettings as FinancialAccountUpdateParamsForwardingSettings,
        FinancialAccountUpdateParamsPlatformRestrictions as FinancialAccountUpdateParamsPlatformRestrictions,
    )
    from stripe.params.treasury._inbound_transfer_cancel_params import (
        InboundTransferCancelParams as InboundTransferCancelParams,
    )
    from stripe.params.treasury._inbound_transfer_create_params import (
        InboundTransferCreateParams as InboundTransferCreateParams,
    )
    from stripe.params.treasury._inbound_transfer_fail_params import (
        InboundTransferFailParams as InboundTransferFailParams,
        InboundTransferFailParamsFailureDetails as InboundTransferFailParamsFailureDetails,
    )
    from stripe.params.treasury._inbound_transfer_list_params import (
        InboundTransferListParams as InboundTransferListParams,
    )
    from stripe.params.treasury._inbound_transfer_retrieve_params import (
        InboundTransferRetrieveParams as InboundTransferRetrieveParams,
    )
    from stripe.params.treasury._inbound_transfer_return_inbound_transfer_params import (
        InboundTransferReturnInboundTransferParams as InboundTransferReturnInboundTransferParams,
    )
    from stripe.params.treasury._inbound_transfer_succeed_params import (
        InboundTransferSucceedParams as InboundTransferSucceedParams,
    )
    from stripe.params.treasury._outbound_payment_cancel_params import (
        OutboundPaymentCancelParams as OutboundPaymentCancelParams,
    )
    from stripe.params.treasury._outbound_payment_create_params import (
        OutboundPaymentCreateParams as OutboundPaymentCreateParams,
        OutboundPaymentCreateParamsDestinationPaymentMethodData as OutboundPaymentCreateParamsDestinationPaymentMethodData,
        OutboundPaymentCreateParamsDestinationPaymentMethodDataBillingDetails as OutboundPaymentCreateParamsDestinationPaymentMethodDataBillingDetails,
        OutboundPaymentCreateParamsDestinationPaymentMethodDataBillingDetailsAddress as OutboundPaymentCreateParamsDestinationPaymentMethodDataBillingDetailsAddress,
        OutboundPaymentCreateParamsDestinationPaymentMethodDataUsBankAccount as OutboundPaymentCreateParamsDestinationPaymentMethodDataUsBankAccount,
        OutboundPaymentCreateParamsDestinationPaymentMethodOptions as OutboundPaymentCreateParamsDestinationPaymentMethodOptions,
        OutboundPaymentCreateParamsDestinationPaymentMethodOptionsUsBankAccount as OutboundPaymentCreateParamsDestinationPaymentMethodOptionsUsBankAccount,
        OutboundPaymentCreateParamsEndUserDetails as OutboundPaymentCreateParamsEndUserDetails,
    )
    from stripe.params.treasury._outbound_payment_fail_params import (
        OutboundPaymentFailParams as OutboundPaymentFailParams,
    )
    from stripe.params.treasury._outbound_payment_list_params import (
        OutboundPaymentListParams as OutboundPaymentListParams,
        OutboundPaymentListParamsCreated as OutboundPaymentListParamsCreated,
    )
    from stripe.params.treasury._outbound_payment_post_params import (
        OutboundPaymentPostParams as OutboundPaymentPostParams,
    )
    from stripe.params.treasury._outbound_payment_retrieve_params import (
        OutboundPaymentRetrieveParams as OutboundPaymentRetrieveParams,
    )
    from stripe.params.treasury._outbound_payment_return_outbound_payment_params import (
        OutboundPaymentReturnOutboundPaymentParams as OutboundPaymentReturnOutboundPaymentParams,
        OutboundPaymentReturnOutboundPaymentParamsReturnedDetails as OutboundPaymentReturnOutboundPaymentParamsReturnedDetails,
    )
    from stripe.params.treasury._outbound_payment_update_params import (
        OutboundPaymentUpdateParams as OutboundPaymentUpdateParams,
        OutboundPaymentUpdateParamsTrackingDetails as OutboundPaymentUpdateParamsTrackingDetails,
        OutboundPaymentUpdateParamsTrackingDetailsAch as OutboundPaymentUpdateParamsTrackingDetailsAch,
        OutboundPaymentUpdateParamsTrackingDetailsUsDomesticWire as OutboundPaymentUpdateParamsTrackingDetailsUsDomesticWire,
    )
    from stripe.params.treasury._outbound_transfer_cancel_params import (
        OutboundTransferCancelParams as OutboundTransferCancelParams,
    )
    from stripe.params.treasury._outbound_transfer_create_params import (
        OutboundTransferCreateParams as OutboundTransferCreateParams,
        OutboundTransferCreateParamsDestinationPaymentMethodData as OutboundTransferCreateParamsDestinationPaymentMethodData,
        OutboundTransferCreateParamsDestinationPaymentMethodOptions as OutboundTransferCreateParamsDestinationPaymentMethodOptions,
        OutboundTransferCreateParamsDestinationPaymentMethodOptionsUsBankAccount as OutboundTransferCreateParamsDestinationPaymentMethodOptionsUsBankAccount,
    )
    from stripe.params.treasury._outbound_transfer_fail_params import (
        OutboundTransferFailParams as OutboundTransferFailParams,
    )
    from stripe.params.treasury._outbound_transfer_list_params import (
        OutboundTransferListParams as OutboundTransferListParams,
    )
    from stripe.params.treasury._outbound_transfer_post_params import (
        OutboundTransferPostParams as OutboundTransferPostParams,
    )
    from stripe.params.treasury._outbound_transfer_retrieve_params import (
        OutboundTransferRetrieveParams as OutboundTransferRetrieveParams,
    )
    from stripe.params.treasury._outbound_transfer_return_outbound_transfer_params import (
        OutboundTransferReturnOutboundTransferParams as OutboundTransferReturnOutboundTransferParams,
        OutboundTransferReturnOutboundTransferParamsReturnedDetails as OutboundTransferReturnOutboundTransferParamsReturnedDetails,
    )
    from stripe.params.treasury._outbound_transfer_update_params import (
        OutboundTransferUpdateParams as OutboundTransferUpdateParams,
        OutboundTransferUpdateParamsTrackingDetails as OutboundTransferUpdateParamsTrackingDetails,
        OutboundTransferUpdateParamsTrackingDetailsAch as OutboundTransferUpdateParamsTrackingDetailsAch,
        OutboundTransferUpdateParamsTrackingDetailsUsDomesticWire as OutboundTransferUpdateParamsTrackingDetailsUsDomesticWire,
    )
    from stripe.params.treasury._received_credit_create_params import (
        ReceivedCreditCreateParams as ReceivedCreditCreateParams,
        ReceivedCreditCreateParamsInitiatingPaymentMethodDetails as ReceivedCreditCreateParamsInitiatingPaymentMethodDetails,
        ReceivedCreditCreateParamsInitiatingPaymentMethodDetailsUsBankAccount as ReceivedCreditCreateParamsInitiatingPaymentMethodDetailsUsBankAccount,
    )
    from stripe.params.treasury._received_credit_list_params import (
        ReceivedCreditListParams as ReceivedCreditListParams,
        ReceivedCreditListParamsLinkedFlows as ReceivedCreditListParamsLinkedFlows,
    )
    from stripe.params.treasury._received_credit_retrieve_params import (
        ReceivedCreditRetrieveParams as ReceivedCreditRetrieveParams,
    )
    from stripe.params.treasury._received_debit_create_params import (
        ReceivedDebitCreateParams as ReceivedDebitCreateParams,
        ReceivedDebitCreateParamsInitiatingPaymentMethodDetails as ReceivedDebitCreateParamsInitiatingPaymentMethodDetails,
        ReceivedDebitCreateParamsInitiatingPaymentMethodDetailsUsBankAccount as ReceivedDebitCreateParamsInitiatingPaymentMethodDetailsUsBankAccount,
    )
    from stripe.params.treasury._received_debit_list_params import (
        ReceivedDebitListParams as ReceivedDebitListParams,
    )
    from stripe.params.treasury._received_debit_retrieve_params import (
        ReceivedDebitRetrieveParams as ReceivedDebitRetrieveParams,
    )
    from stripe.params.treasury._transaction_entry_list_params import (
        TransactionEntryListParams as TransactionEntryListParams,
        TransactionEntryListParamsCreated as TransactionEntryListParamsCreated,
        TransactionEntryListParamsEffectiveAt as TransactionEntryListParamsEffectiveAt,
    )
    from stripe.params.treasury._transaction_entry_retrieve_params import (
        TransactionEntryRetrieveParams as TransactionEntryRetrieveParams,
    )
    from stripe.params.treasury._transaction_list_params import (
        TransactionListParams as TransactionListParams,
        TransactionListParamsCreated as TransactionListParamsCreated,
        TransactionListParamsStatusTransitions as TransactionListParamsStatusTransitions,
        TransactionListParamsStatusTransitionsPostedAt as TransactionListParamsStatusTransitionsPostedAt,
    )
    from stripe.params.treasury._transaction_retrieve_params import (
        TransactionRetrieveParams as TransactionRetrieveParams,
    )

_submodules = {
    "CreditReversalCreateParams": "stripe.params.treasury._credit_reversal_create_params",
    "CreditReversalListParams": "stripe.params.treasury._credit_reversal_list_params",
    "CreditReversalRetrieveParams": "stripe.params.treasury._credit_reversal_retrieve_params",
    "DebitReversalCreateParams": "stripe.params.treasury._debit_reversal_create_params",
    "DebitReversalListParams": "stripe.params.treasury._debit_reversal_list_params",
    "DebitReversalRetrieveParams": "stripe.params.treasury._debit_reversal_retrieve_params",
    "FinancialAccountCloseParams": "stripe.params.treasury._financial_account_close_params",
    "FinancialAccountCloseParamsForwardingSettings": "stripe.params.treasury._financial_account_close_params",
    "FinancialAccountCreateParams": "stripe.params.treasury._financial_account_create_params",
    "FinancialAccountCreateParamsFeatures": "stripe.params.treasury._financial_account_create_params",
    "FinancialAccountCreateParamsFeaturesCardIssuing": "stripe.params.treasury._financial_account_create_params",
    "FinancialAccountCreateParamsFeaturesDepositInsurance": "stripe.params.treasury._financial_account_create_params",
    "FinancialAccountCreateParamsFeaturesFinancialAddresses": "stripe.params.treasury._financial_account_create_params",
    "FinancialAccountCreateParamsFeaturesFinancialAddressesAba": "stripe.params.treasury._financial_account_create_params",
    "FinancialAccountCreateParamsFeaturesInboundTransfers": "stripe.params.treasury._financial_account_create_params",
    "FinancialAccountCreateParamsFeaturesInboundTransfersAch": "stripe.params.treasury._financial_account_create_params",
    "FinancialAccountCreateParamsFeaturesIntraStripeFlows": "stripe.params.treasury._financial_account_create_params",
    "FinancialAccountCreateParamsFeaturesOutboundPayments": "stripe.params.treasury._financial_account_create_params",
    "FinancialAccountCreateParamsFeaturesOutboundPaymentsAch": "stripe.params.treasury._financial_account_create_params",
    "FinancialAccountCreateParamsFeaturesOutboundPaymentsUsDomesticWire": "stripe.params.treasury._financial_account_create_params",
    "FinancialAccountCreateParamsFeaturesOutboundTransfers": "stripe.params.treasury._financial_account_create_params",
    "FinancialAccountCreateParamsFeaturesOutboundTransfersAch": "stripe.params.treasury._financial_account_create_params",
    "FinancialAccountCreateParamsFeaturesOutboundTransfersUsDomesticWire": "stripe.params.treasury._financial_account_create_params",
    "FinancialAccountCreateParamsPlatformRestrictions": "stripe.params.treasury._financial_account_create_params",
    "FinancialAccountFeaturesRetrieveParams": "stripe.params.treasury._financial_account_features_retrieve_params",
    "FinancialAccountFeaturesUpdateParams": "stripe.params.treasury._financial_account_features_update_params",
    "FinancialAccountFeaturesUpdateParamsCardIssuing": "stripe.params.treasury._financial_account_features_update_params",
    "FinancialAccountFeaturesUpdateParamsDepositInsurance": "stripe.params.treasury._financial_account_features_update_params",
    "FinancialAccountFeaturesUpdateParamsFinancialAddresses": "stripe.params.treasury._financial_account_features_update_params",
    "FinancialAccountFeaturesUpdateParamsFinancialAddressesAba": "stripe.params.treasury._financial_account_features_update_params",
    "FinancialAccountFeaturesUpdateParamsInboundTransfers": "stripe.params.treasury._financial_account_features_update_params",
    "FinancialAccountFeaturesUpdateParamsInboundTransfersAch": "stripe.params.treasury._financial_account_features_update_params",
    "FinancialAccountFeaturesUpdateParamsIntraStripeFlows": "stripe.params.treasury._financial_account_features_update_params",
    "FinancialAccountFeaturesUpdateParamsOutboundPayments": "stripe.params.treasury._financial_account_features_update_params",
    "FinancialAccountFeaturesUpdateParamsOutboundPaymentsAch": "stripe.params.treasury._financial_account_features_update_params",
    "FinancialAccountFeaturesUpdateParamsOutboundPaymentsUsDomesticWire": "stripe.params.treasury._financial_account_features_update_params",
    "FinancialAccountFeaturesUpdateParamsOutboundTransfers": "stripe.params.treasury._financial_account_features_update_params",
    "FinancialAccountFeaturesUpdateParamsOutboundTransfersAch": "stripe.params.treasury._financial_account_features_update_params",
    "FinancialAccountFeaturesUpdateParamsOutboundTransfersUsDomesticWire": "stripe.params.treasury._financial_account_features_update_params",
    "FinancialAccountListParams": "stripe.params.treasury._financial_account_list_params",
    "FinancialAccountListParamsCreated": "stripe.params.treasury._financial_account_list_params",
    "FinancialAccountModifyParams": "stripe.params.treasury._financial_account_modify_params",
    "FinancialAccountModifyParamsFeatures": "stripe.params.treasury._financial_account_modify_params",
    "FinancialAccountModifyParamsFeaturesCardIssuing": "stripe.params.treasury._financial_account_modify_params",
    "FinancialAccountModifyParamsFeaturesDepositInsurance": "stripe.params.treasury._financial_account_modify_params",
    "FinancialAccountModifyParamsFeaturesFinancialAddresses": "stripe.params.treasury._financial_account_modify_params",
    "FinancialAccountModifyParamsFeaturesFinancialAddressesAba": "stripe.params.treasury._financial_account_modify_params",
    "FinancialAccountModifyParamsFeaturesInboundTransfers": "stripe.params.treasury._financial_account_modify_params",
    "FinancialAccountModifyParamsFeaturesInboundTransfersAch": "stripe.params.treasury._financial_account_modify_params",
    "FinancialAccountModifyParamsFeaturesIntraStripeFlows": "stripe.params.treasury._financial_account_modify_params",
    "FinancialAccountModifyParamsFeaturesOutboundPayments": "stripe.params.treasury._financial_account_modify_params",
    "FinancialAccountModifyParamsFeaturesOutboundPaymentsAch": "stripe.params.treasury._financial_account_modify_params",
    "FinancialAccountModifyParamsFeaturesOutboundPaymentsUsDomesticWire": "stripe.params.treasury._financial_account_modify_params",
    "FinancialAccountModifyParamsFeaturesOutboundTransfers": "stripe.params.treasury._financial_account_modify_params",
    "FinancialAccountModifyParamsFeaturesOutboundTransfersAch": "stripe.params.treasury._financial_account_modify_params",
    "FinancialAccountModifyParamsFeaturesOutboundTransfersUsDomesticWire": "stripe.params.treasury._financial_account_modify_params",
    "FinancialAccountModifyParamsForwardingSettings": "stripe.params.treasury._financial_account_modify_params",
    "FinancialAccountModifyParamsPlatformRestrictions": "stripe.params.treasury._financial_account_modify_params",
    "FinancialAccountRetrieveFeaturesParams": "stripe.params.treasury._financial_account_retrieve_features_params",
    "FinancialAccountRetrieveParams": "stripe.params.treasury._financial_account_retrieve_params",
    "FinancialAccountUpdateFeaturesParams": "stripe.params.treasury._financial_account_update_features_params",
    "FinancialAccountUpdateFeaturesParamsCardIssuing": "stripe.params.treasury._financial_account_update_features_params",
    "FinancialAccountUpdateFeaturesParamsDepositInsurance": "stripe.params.treasury._financial_account_update_features_params",
    "FinancialAccountUpdateFeaturesParamsFinancialAddresses": "stripe.params.treasury._financial_account_update_features_params",
    "FinancialAccountUpdateFeaturesParamsFinancialAddressesAba": "stripe.params.treasury._financial_account_update_features_params",
    "FinancialAccountUpdateFeaturesParamsInboundTransfers": "stripe.params.treasury._financial_account_update_features_params",
    "FinancialAccountUpdateFeaturesParamsInboundTransfersAch": "stripe.params.treasury._financial_account_update_features_params",
    "FinancialAccountUpdateFeaturesParamsIntraStripeFlows": "stripe.params.treasury._financial_account_update_features_params",
    "FinancialAccountUpdateFeaturesParamsOutboundPayments": "stripe.params.treasury._financial_account_update_features_params",
    "FinancialAccountUpdateFeaturesParamsOutboundPaymentsAch": "stripe.params.treasury._financial_account_update_features_params",
    "FinancialAccountUpdateFeaturesParamsOutboundPaymentsUsDomesticWire": "stripe.params.treasury._financial_account_update_features_params",
    "FinancialAccountUpdateFeaturesParamsOutboundTransfers": "stripe.params.treasury._financial_account_update_features_params",
    "FinancialAccountUpdateFeaturesParamsOutboundTransfersAch": "stripe.params.treasury._financial_account_update_features_params",
    "FinancialAccountUpdateFeaturesParamsOutboundTransfersUsDomesticWire": "stripe.params.treasury._financial_account_update_features_params",
    "FinancialAccountUpdateParams": "stripe.params.treasury._financial_account_update_params",
    "FinancialAccountUpdateParamsFeatures": "stripe.params.treasury._financial_account_update_params",
    "FinancialAccountUpdateParamsFeaturesCardIssuing": "stripe.params.treasury._financial_account_update_params",
    "FinancialAccountUpdateParamsFeaturesDepositInsurance": "stripe.params.treasury._financial_account_update_params",
    "FinancialAccountUpdateParamsFeaturesFinancialAddresses": "stripe.params.treasury._financial_account_update_params",
    "FinancialAccountUpdateParamsFeaturesFinancialAddressesAba": "stripe.params.treasury._financial_account_update_params",
    "FinancialAccountUpdateParamsFeaturesInboundTransfers": "stripe.params.treasury._financial_account_update_params",
    "FinancialAccountUpdateParamsFeaturesInboundTransfersAch": "stripe.params.treasury._financial_account_update_params",
    "FinancialAccountUpdateParamsFeaturesIntraStripeFlows": "stripe.params.treasury._financial_account_update_params",
    "FinancialAccountUpdateParamsFeaturesOutboundPayments": "stripe.params.treasury._financial_account_update_params",
    "FinancialAccountUpdateParamsFeaturesOutboundPaymentsAch": "stripe.params.treasury._financial_account_update_params",
    "FinancialAccountUpdateParamsFeaturesOutboundPaymentsUsDomesticWire": "stripe.params.treasury._financial_account_update_params",
    "FinancialAccountUpdateParamsFeaturesOutboundTransfers": "stripe.params.treasury._financial_account_update_params",
    "FinancialAccountUpdateParamsFeaturesOutboundTransfersAch": "stripe.params.treasury._financial_account_update_params",
    "FinancialAccountUpdateParamsFeaturesOutboundTransfersUsDomesticWire": "stripe.params.treasury._financial_account_update_params",
    "FinancialAccountUpdateParamsForwardingSettings": "stripe.params.treasury._financial_account_update_params",
    "FinancialAccountUpdateParamsPlatformRestrictions": "stripe.params.treasury._financial_account_update_params",
    "InboundTransferCancelParams": "stripe.params.treasury._inbound_transfer_cancel_params",
    "InboundTransferCreateParams": "stripe.params.treasury._inbound_transfer_create_params",
    "InboundTransferFailParams": "stripe.params.treasury._inbound_transfer_fail_params",
    "InboundTransferFailParamsFailureDetails": "stripe.params.treasury._inbound_transfer_fail_params",
    "InboundTransferListParams": "stripe.params.treasury._inbound_transfer_list_params",
    "InboundTransferRetrieveParams": "stripe.params.treasury._inbound_transfer_retrieve_params",
    "InboundTransferReturnInboundTransferParams": "stripe.params.treasury._inbound_transfer_return_inbound_transfer_params",
    "InboundTransferSucceedParams": "stripe.params.treasury._inbound_transfer_succeed_params",
    "OutboundPaymentCancelParams": "stripe.params.treasury._outbound_payment_cancel_params",
    "OutboundPaymentCreateParams": "stripe.params.treasury._outbound_payment_create_params",
    "OutboundPaymentCreateParamsDestinationPaymentMethodData": "stripe.params.treasury._outbound_payment_create_params",
    "OutboundPaymentCreateParamsDestinationPaymentMethodDataBillingDetails": "stripe.params.treasury._outbound_payment_create_params",
    "OutboundPaymentCreateParamsDestinationPaymentMethodDataBillingDetailsAddress": "stripe.params.treasury._outbound_payment_create_params",
    "OutboundPaymentCreateParamsDestinationPaymentMethodDataUsBankAccount": "stripe.params.treasury._outbound_payment_create_params",
    "OutboundPaymentCreateParamsDestinationPaymentMethodOptions": "stripe.params.treasury._outbound_payment_create_params",
    "OutboundPaymentCreateParamsDestinationPaymentMethodOptionsUsBankAccount": "stripe.params.treasury._outbound_payment_create_params",
    "OutboundPaymentCreateParamsEndUserDetails": "stripe.params.treasury._outbound_payment_create_params",
    "OutboundPaymentFailParams": "stripe.params.treasury._outbound_payment_fail_params",
    "OutboundPaymentListParams": "stripe.params.treasury._outbound_payment_list_params",
    "OutboundPaymentListParamsCreated": "stripe.params.treasury._outbound_payment_list_params",
    "OutboundPaymentPostParams": "stripe.params.treasury._outbound_payment_post_params",
    "OutboundPaymentRetrieveParams": "stripe.params.treasury._outbound_payment_retrieve_params",
    "OutboundPaymentReturnOutboundPaymentParams": "stripe.params.treasury._outbound_payment_return_outbound_payment_params",
    "OutboundPaymentReturnOutboundPaymentParamsReturnedDetails": "stripe.params.treasury._outbound_payment_return_outbound_payment_params",
    "OutboundPaymentUpdateParams": "stripe.params.treasury._outbound_payment_update_params",
    "OutboundPaymentUpdateParamsTrackingDetails": "stripe.params.treasury._outbound_payment_update_params",
    "OutboundPaymentUpdateParamsTrackingDetailsAch": "stripe.params.treasury._outbound_payment_update_params",
    "OutboundPaymentUpdateParamsTrackingDetailsUsDomesticWire": "stripe.params.treasury._outbound_payment_update_params",
    "OutboundTransferCancelParams": "stripe.params.treasury._outbound_transfer_cancel_params",
    "OutboundTransferCreateParams": "stripe.params.treasury._outbound_transfer_create_params",
    "OutboundTransferCreateParamsDestinationPaymentMethodData": "stripe.params.treasury._outbound_transfer_create_params",
    "OutboundTransferCreateParamsDestinationPaymentMethodOptions": "stripe.params.treasury._outbound_transfer_create_params",
    "OutboundTransferCreateParamsDestinationPaymentMethodOptionsUsBankAccount": "stripe.params.treasury._outbound_transfer_create_params",
    "OutboundTransferFailParams": "stripe.params.treasury._outbound_transfer_fail_params",
    "OutboundTransferListParams": "stripe.params.treasury._outbound_transfer_list_params",
    "OutboundTransferPostParams": "stripe.params.treasury._outbound_transfer_post_params",
    "OutboundTransferRetrieveParams": "stripe.params.treasury._outbound_transfer_retrieve_params",
    "OutboundTransferReturnOutboundTransferParams": "stripe.params.treasury._outbound_transfer_return_outbound_transfer_params",
    "OutboundTransferReturnOutboundTransferParamsReturnedDetails": "stripe.params.treasury._outbound_transfer_return_outbound_transfer_params",
    "OutboundTransferUpdateParams": "stripe.params.treasury._outbound_transfer_update_params",
    "OutboundTransferUpdateParamsTrackingDetails": "stripe.params.treasury._outbound_transfer_update_params",
    "OutboundTransferUpdateParamsTrackingDetailsAch": "stripe.params.treasury._outbound_transfer_update_params",
    "OutboundTransferUpdateParamsTrackingDetailsUsDomesticWire": "stripe.params.treasury._outbound_transfer_update_params",
    "ReceivedCreditCreateParams": "stripe.params.treasury._received_credit_create_params",
    "ReceivedCreditCreateParamsInitiatingPaymentMethodDetails": "stripe.params.treasury._received_credit_create_params",
    "ReceivedCreditCreateParamsInitiatingPaymentMethodDetailsUsBankAccount": "stripe.params.treasury._received_credit_create_params",
    "ReceivedCreditListParams": "stripe.params.treasury._received_credit_list_params",
    "ReceivedCreditListParamsLinkedFlows": "stripe.params.treasury._received_credit_list_params",
    "ReceivedCreditRetrieveParams": "stripe.params.treasury._received_credit_retrieve_params",
    "ReceivedDebitCreateParams": "stripe.params.treasury._received_debit_create_params",
    "ReceivedDebitCreateParamsInitiatingPaymentMethodDetails": "stripe.params.treasury._received_debit_create_params",
    "ReceivedDebitCreateParamsInitiatingPaymentMethodDetailsUsBankAccount": "stripe.params.treasury._received_debit_create_params",
    "ReceivedDebitListParams": "stripe.params.treasury._received_debit_list_params",
    "ReceivedDebitRetrieveParams": "stripe.params.treasury._received_debit_retrieve_params",
    "TransactionEntryListParams": "stripe.params.treasury._transaction_entry_list_params",
    "TransactionEntryListParamsCreated": "stripe.params.treasury._transaction_entry_list_params",
    "TransactionEntryListParamsEffectiveAt": "stripe.params.treasury._transaction_entry_list_params",
    "TransactionEntryRetrieveParams": "stripe.params.treasury._transaction_entry_retrieve_params",
    "TransactionListParams": "stripe.params.treasury._transaction_list_params",
    "TransactionListParamsCreated": "stripe.params.treasury._transaction_list_params",
    "TransactionListParamsStatusTransitions": "stripe.params.treasury._transaction_list_params",
    "TransactionListParamsStatusTransitionsPostedAt": "stripe.params.treasury._transaction_list_params",
    "TransactionRetrieveParams": "stripe.params.treasury._transaction_retrieve_params",
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
