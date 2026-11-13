# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.v2.money_management import test_helpers as test_helpers
    from stripe.params.v2.money_management._adjustment_list_params import (
        AdjustmentListParams as AdjustmentListParams,
        AdjustmentListParamsCreated as AdjustmentListParamsCreated,
    )
    from stripe.params.v2.money_management._adjustment_retrieve_params import (
        AdjustmentRetrieveParams as AdjustmentRetrieveParams,
    )
    from stripe.params.v2.money_management._financial_account_list_params import (
        FinancialAccountListParams as FinancialAccountListParams,
    )
    from stripe.params.v2.money_management._financial_account_retrieve_params import (
        FinancialAccountRetrieveParams as FinancialAccountRetrieveParams,
    )
    from stripe.params.v2.money_management._financial_account_update_params import (
        FinancialAccountUpdateParams as FinancialAccountUpdateParams,
    )
    from stripe.params.v2.money_management._financial_address_create_params import (
        FinancialAddressCreateParams as FinancialAddressCreateParams,
        FinancialAddressCreateParamsBankAccount as FinancialAddressCreateParamsBankAccount,
    )
    from stripe.params.v2.money_management._financial_address_list_params import (
        FinancialAddressListParams as FinancialAddressListParams,
    )
    from stripe.params.v2.money_management._financial_address_retrieve_params import (
        FinancialAddressRetrieveParams as FinancialAddressRetrieveParams,
    )
    from stripe.params.v2.money_management._inbound_transfer_create_params import (
        InboundTransferCreateParams as InboundTransferCreateParams,
        InboundTransferCreateParamsFrom as InboundTransferCreateParamsFrom,
        InboundTransferCreateParamsTo as InboundTransferCreateParamsTo,
    )
    from stripe.params.v2.money_management._inbound_transfer_list_params import (
        InboundTransferListParams as InboundTransferListParams,
        InboundTransferListParamsCreated as InboundTransferListParamsCreated,
    )
    from stripe.params.v2.money_management._inbound_transfer_retrieve_params import (
        InboundTransferRetrieveParams as InboundTransferRetrieveParams,
    )
    from stripe.params.v2.money_management._outbound_payment_cancel_params import (
        OutboundPaymentCancelParams as OutboundPaymentCancelParams,
    )
    from stripe.params.v2.money_management._outbound_payment_create_params import (
        OutboundPaymentCreateParams as OutboundPaymentCreateParams,
        OutboundPaymentCreateParamsFrom as OutboundPaymentCreateParamsFrom,
        OutboundPaymentCreateParamsRecipientNotification as OutboundPaymentCreateParamsRecipientNotification,
        OutboundPaymentCreateParamsTo as OutboundPaymentCreateParamsTo,
        OutboundPaymentCreateParamsToPayoutMethodOptions as OutboundPaymentCreateParamsToPayoutMethodOptions,
        OutboundPaymentCreateParamsToPayoutMethodOptionsBankAccount as OutboundPaymentCreateParamsToPayoutMethodOptionsBankAccount,
        OutboundPaymentCreateParamsToPayoutMethodOptionsBankAccountPreferredNetworkOptions as OutboundPaymentCreateParamsToPayoutMethodOptionsBankAccountPreferredNetworkOptions,
        OutboundPaymentCreateParamsToPayoutMethodOptionsBankAccountPreferredNetworkOptionsAch as OutboundPaymentCreateParamsToPayoutMethodOptionsBankAccountPreferredNetworkOptionsAch,
    )
    from stripe.params.v2.money_management._outbound_payment_list_params import (
        OutboundPaymentListParams as OutboundPaymentListParams,
        OutboundPaymentListParamsCreated as OutboundPaymentListParamsCreated,
    )
    from stripe.params.v2.money_management._outbound_payment_retrieve_params import (
        OutboundPaymentRetrieveParams as OutboundPaymentRetrieveParams,
    )
    from stripe.params.v2.money_management._outbound_setup_intent_cancel_params import (
        OutboundSetupIntentCancelParams as OutboundSetupIntentCancelParams,
    )
    from stripe.params.v2.money_management._outbound_setup_intent_create_params import (
        OutboundSetupIntentCreateParams as OutboundSetupIntentCreateParams,
        OutboundSetupIntentCreateParamsPayoutMethodData as OutboundSetupIntentCreateParamsPayoutMethodData,
        OutboundSetupIntentCreateParamsPayoutMethodDataBankAccount as OutboundSetupIntentCreateParamsPayoutMethodDataBankAccount,
    )
    from stripe.params.v2.money_management._outbound_setup_intent_list_params import (
        OutboundSetupIntentListParams as OutboundSetupIntentListParams,
    )
    from stripe.params.v2.money_management._outbound_setup_intent_retrieve_params import (
        OutboundSetupIntentRetrieveParams as OutboundSetupIntentRetrieveParams,
    )
    from stripe.params.v2.money_management._outbound_setup_intent_update_params import (
        OutboundSetupIntentUpdateParams as OutboundSetupIntentUpdateParams,
        OutboundSetupIntentUpdateParamsPayoutMethodData as OutboundSetupIntentUpdateParamsPayoutMethodData,
        OutboundSetupIntentUpdateParamsPayoutMethodDataBankAccount as OutboundSetupIntentUpdateParamsPayoutMethodDataBankAccount,
    )
    from stripe.params.v2.money_management._payout_intent_cancel_params import (
        PayoutIntentCancelParams as PayoutIntentCancelParams,
    )
    from stripe.params.v2.money_management._payout_intent_confirm_params import (
        PayoutIntentConfirmParams as PayoutIntentConfirmParams,
    )
    from stripe.params.v2.money_management._payout_intent_create_params import (
        PayoutIntentCreateParams as PayoutIntentCreateParams,
        PayoutIntentCreateParamsFrom as PayoutIntentCreateParamsFrom,
        PayoutIntentCreateParamsRecipientNotification as PayoutIntentCreateParamsRecipientNotification,
        PayoutIntentCreateParamsScheduleOptions as PayoutIntentCreateParamsScheduleOptions,
        PayoutIntentCreateParamsTo as PayoutIntentCreateParamsTo,
        PayoutIntentCreateParamsToPayoutMethodOptions as PayoutIntentCreateParamsToPayoutMethodOptions,
        PayoutIntentCreateParamsToPayoutMethodOptionsBankAccount as PayoutIntentCreateParamsToPayoutMethodOptionsBankAccount,
        PayoutIntentCreateParamsToPayoutMethodOptionsBankAccountPreferredNetworkOptions as PayoutIntentCreateParamsToPayoutMethodOptionsBankAccountPreferredNetworkOptions,
        PayoutIntentCreateParamsToPayoutMethodOptionsBankAccountPreferredNetworkOptionsAch as PayoutIntentCreateParamsToPayoutMethodOptionsBankAccountPreferredNetworkOptionsAch,
    )
    from stripe.params.v2.money_management._payout_intent_list_params import (
        PayoutIntentListParams as PayoutIntentListParams,
    )
    from stripe.params.v2.money_management._payout_intent_refresh_fx_quote_params import (
        PayoutIntentRefreshFxQuoteParams as PayoutIntentRefreshFxQuoteParams,
    )
    from stripe.params.v2.money_management._payout_intent_refresh_recipient_verification_params import (
        PayoutIntentRefreshRecipientVerificationParams as PayoutIntentRefreshRecipientVerificationParams,
    )
    from stripe.params.v2.money_management._payout_intent_retrieve_params import (
        PayoutIntentRetrieveParams as PayoutIntentRetrieveParams,
    )
    from stripe.params.v2.money_management._payout_intent_update_params import (
        PayoutIntentUpdateParams as PayoutIntentUpdateParams,
        PayoutIntentUpdateParamsRecipientNotification as PayoutIntentUpdateParamsRecipientNotification,
        PayoutIntentUpdateParamsScheduleOptions as PayoutIntentUpdateParamsScheduleOptions,
        PayoutIntentUpdateParamsTo as PayoutIntentUpdateParamsTo,
        PayoutIntentUpdateParamsToPayoutMethodOptions as PayoutIntentUpdateParamsToPayoutMethodOptions,
        PayoutIntentUpdateParamsToPayoutMethodOptionsBankAccount as PayoutIntentUpdateParamsToPayoutMethodOptionsBankAccount,
        PayoutIntentUpdateParamsToPayoutMethodOptionsBankAccountPreferredNetworkOptions as PayoutIntentUpdateParamsToPayoutMethodOptionsBankAccountPreferredNetworkOptions,
        PayoutIntentUpdateParamsToPayoutMethodOptionsBankAccountPreferredNetworkOptionsAch as PayoutIntentUpdateParamsToPayoutMethodOptionsBankAccountPreferredNetworkOptionsAch,
    )
    from stripe.params.v2.money_management._payout_method_archive_params import (
        PayoutMethodArchiveParams as PayoutMethodArchiveParams,
    )
    from stripe.params.v2.money_management._payout_method_list_params import (
        PayoutMethodListParams as PayoutMethodListParams,
        PayoutMethodListParamsUsageStatus as PayoutMethodListParamsUsageStatus,
    )
    from stripe.params.v2.money_management._payout_method_retrieve_params import (
        PayoutMethodRetrieveParams as PayoutMethodRetrieveParams,
    )
    from stripe.params.v2.money_management._payout_method_unarchive_params import (
        PayoutMethodUnarchiveParams as PayoutMethodUnarchiveParams,
    )
    from stripe.params.v2.money_management._payout_methods_bank_account_spec_retrieve_params import (
        PayoutMethodsBankAccountSpecRetrieveParams as PayoutMethodsBankAccountSpecRetrieveParams,
    )
    from stripe.params.v2.money_management._received_credit_list_params import (
        ReceivedCreditListParams as ReceivedCreditListParams,
        ReceivedCreditListParamsCreated as ReceivedCreditListParamsCreated,
    )
    from stripe.params.v2.money_management._received_credit_retrieve_params import (
        ReceivedCreditRetrieveParams as ReceivedCreditRetrieveParams,
    )
    from stripe.params.v2.money_management._recipient_verification_acknowledge_params import (
        RecipientVerificationAcknowledgeParams as RecipientVerificationAcknowledgeParams,
    )
    from stripe.params.v2.money_management._recipient_verification_create_params import (
        RecipientVerificationCreateParams as RecipientVerificationCreateParams,
    )
    from stripe.params.v2.money_management._recipient_verification_retrieve_params import (
        RecipientVerificationRetrieveParams as RecipientVerificationRetrieveParams,
    )
    from stripe.params.v2.money_management._transaction_entry_list_params import (
        TransactionEntryListParams as TransactionEntryListParams,
        TransactionEntryListParamsCreated as TransactionEntryListParamsCreated,
    )
    from stripe.params.v2.money_management._transaction_entry_retrieve_params import (
        TransactionEntryRetrieveParams as TransactionEntryRetrieveParams,
    )
    from stripe.params.v2.money_management._transaction_list_params import (
        TransactionListParams as TransactionListParams,
        TransactionListParamsCreated as TransactionListParamsCreated,
    )
    from stripe.params.v2.money_management._transaction_refresh_regulatory_receipt_params import (
        TransactionRefreshRegulatoryReceiptParams as TransactionRefreshRegulatoryReceiptParams,
    )
    from stripe.params.v2.money_management._transaction_retrieve_params import (
        TransactionRetrieveParams as TransactionRetrieveParams,
    )
    from stripe.params.v2.money_management._transaction_update_params import (
        TransactionUpdateParams as TransactionUpdateParams,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "test_helpers": ("stripe.params.v2.money_management.test_helpers", True),
    "AdjustmentListParams": (
        "stripe.params.v2.money_management._adjustment_list_params",
        False,
    ),
    "AdjustmentListParamsCreated": (
        "stripe.params.v2.money_management._adjustment_list_params",
        False,
    ),
    "AdjustmentRetrieveParams": (
        "stripe.params.v2.money_management._adjustment_retrieve_params",
        False,
    ),
    "FinancialAccountListParams": (
        "stripe.params.v2.money_management._financial_account_list_params",
        False,
    ),
    "FinancialAccountRetrieveParams": (
        "stripe.params.v2.money_management._financial_account_retrieve_params",
        False,
    ),
    "FinancialAccountUpdateParams": (
        "stripe.params.v2.money_management._financial_account_update_params",
        False,
    ),
    "FinancialAddressCreateParams": (
        "stripe.params.v2.money_management._financial_address_create_params",
        False,
    ),
    "FinancialAddressCreateParamsBankAccount": (
        "stripe.params.v2.money_management._financial_address_create_params",
        False,
    ),
    "FinancialAddressListParams": (
        "stripe.params.v2.money_management._financial_address_list_params",
        False,
    ),
    "FinancialAddressRetrieveParams": (
        "stripe.params.v2.money_management._financial_address_retrieve_params",
        False,
    ),
    "InboundTransferCreateParams": (
        "stripe.params.v2.money_management._inbound_transfer_create_params",
        False,
    ),
    "InboundTransferCreateParamsFrom": (
        "stripe.params.v2.money_management._inbound_transfer_create_params",
        False,
    ),
    "InboundTransferCreateParamsTo": (
        "stripe.params.v2.money_management._inbound_transfer_create_params",
        False,
    ),
    "InboundTransferListParams": (
        "stripe.params.v2.money_management._inbound_transfer_list_params",
        False,
    ),
    "InboundTransferListParamsCreated": (
        "stripe.params.v2.money_management._inbound_transfer_list_params",
        False,
    ),
    "InboundTransferRetrieveParams": (
        "stripe.params.v2.money_management._inbound_transfer_retrieve_params",
        False,
    ),
    "OutboundPaymentCancelParams": (
        "stripe.params.v2.money_management._outbound_payment_cancel_params",
        False,
    ),
    "OutboundPaymentCreateParams": (
        "stripe.params.v2.money_management._outbound_payment_create_params",
        False,
    ),
    "OutboundPaymentCreateParamsFrom": (
        "stripe.params.v2.money_management._outbound_payment_create_params",
        False,
    ),
    "OutboundPaymentCreateParamsRecipientNotification": (
        "stripe.params.v2.money_management._outbound_payment_create_params",
        False,
    ),
    "OutboundPaymentCreateParamsTo": (
        "stripe.params.v2.money_management._outbound_payment_create_params",
        False,
    ),
    "OutboundPaymentCreateParamsToPayoutMethodOptions": (
        "stripe.params.v2.money_management._outbound_payment_create_params",
        False,
    ),
    "OutboundPaymentCreateParamsToPayoutMethodOptionsBankAccount": (
        "stripe.params.v2.money_management._outbound_payment_create_params",
        False,
    ),
    "OutboundPaymentCreateParamsToPayoutMethodOptionsBankAccountPreferredNetworkOptions": (
        "stripe.params.v2.money_management._outbound_payment_create_params",
        False,
    ),
    "OutboundPaymentCreateParamsToPayoutMethodOptionsBankAccountPreferredNetworkOptionsAch": (
        "stripe.params.v2.money_management._outbound_payment_create_params",
        False,
    ),
    "OutboundPaymentListParams": (
        "stripe.params.v2.money_management._outbound_payment_list_params",
        False,
    ),
    "OutboundPaymentListParamsCreated": (
        "stripe.params.v2.money_management._outbound_payment_list_params",
        False,
    ),
    "OutboundPaymentRetrieveParams": (
        "stripe.params.v2.money_management._outbound_payment_retrieve_params",
        False,
    ),
    "OutboundSetupIntentCancelParams": (
        "stripe.params.v2.money_management._outbound_setup_intent_cancel_params",
        False,
    ),
    "OutboundSetupIntentCreateParams": (
        "stripe.params.v2.money_management._outbound_setup_intent_create_params",
        False,
    ),
    "OutboundSetupIntentCreateParamsPayoutMethodData": (
        "stripe.params.v2.money_management._outbound_setup_intent_create_params",
        False,
    ),
    "OutboundSetupIntentCreateParamsPayoutMethodDataBankAccount": (
        "stripe.params.v2.money_management._outbound_setup_intent_create_params",
        False,
    ),
    "OutboundSetupIntentListParams": (
        "stripe.params.v2.money_management._outbound_setup_intent_list_params",
        False,
    ),
    "OutboundSetupIntentRetrieveParams": (
        "stripe.params.v2.money_management._outbound_setup_intent_retrieve_params",
        False,
    ),
    "OutboundSetupIntentUpdateParams": (
        "stripe.params.v2.money_management._outbound_setup_intent_update_params",
        False,
    ),
    "OutboundSetupIntentUpdateParamsPayoutMethodData": (
        "stripe.params.v2.money_management._outbound_setup_intent_update_params",
        False,
    ),
    "OutboundSetupIntentUpdateParamsPayoutMethodDataBankAccount": (
        "stripe.params.v2.money_management._outbound_setup_intent_update_params",
        False,
    ),
    "PayoutIntentCancelParams": (
        "stripe.params.v2.money_management._payout_intent_cancel_params",
        False,
    ),
    "PayoutIntentConfirmParams": (
        "stripe.params.v2.money_management._payout_intent_confirm_params",
        False,
    ),
    "PayoutIntentCreateParams": (
        "stripe.params.v2.money_management._payout_intent_create_params",
        False,
    ),
    "PayoutIntentCreateParamsFrom": (
        "stripe.params.v2.money_management._payout_intent_create_params",
        False,
    ),
    "PayoutIntentCreateParamsRecipientNotification": (
        "stripe.params.v2.money_management._payout_intent_create_params",
        False,
    ),
    "PayoutIntentCreateParamsScheduleOptions": (
        "stripe.params.v2.money_management._payout_intent_create_params",
        False,
    ),
    "PayoutIntentCreateParamsTo": (
        "stripe.params.v2.money_management._payout_intent_create_params",
        False,
    ),
    "PayoutIntentCreateParamsToPayoutMethodOptions": (
        "stripe.params.v2.money_management._payout_intent_create_params",
        False,
    ),
    "PayoutIntentCreateParamsToPayoutMethodOptionsBankAccount": (
        "stripe.params.v2.money_management._payout_intent_create_params",
        False,
    ),
    "PayoutIntentCreateParamsToPayoutMethodOptionsBankAccountPreferredNetworkOptions": (
        "stripe.params.v2.money_management._payout_intent_create_params",
        False,
    ),
    "PayoutIntentCreateParamsToPayoutMethodOptionsBankAccountPreferredNetworkOptionsAch": (
        "stripe.params.v2.money_management._payout_intent_create_params",
        False,
    ),
    "PayoutIntentListParams": (
        "stripe.params.v2.money_management._payout_intent_list_params",
        False,
    ),
    "PayoutIntentRefreshFxQuoteParams": (
        "stripe.params.v2.money_management._payout_intent_refresh_fx_quote_params",
        False,
    ),
    "PayoutIntentRefreshRecipientVerificationParams": (
        "stripe.params.v2.money_management._payout_intent_refresh_recipient_verification_params",
        False,
    ),
    "PayoutIntentRetrieveParams": (
        "stripe.params.v2.money_management._payout_intent_retrieve_params",
        False,
    ),
    "PayoutIntentUpdateParams": (
        "stripe.params.v2.money_management._payout_intent_update_params",
        False,
    ),
    "PayoutIntentUpdateParamsRecipientNotification": (
        "stripe.params.v2.money_management._payout_intent_update_params",
        False,
    ),
    "PayoutIntentUpdateParamsScheduleOptions": (
        "stripe.params.v2.money_management._payout_intent_update_params",
        False,
    ),
    "PayoutIntentUpdateParamsTo": (
        "stripe.params.v2.money_management._payout_intent_update_params",
        False,
    ),
    "PayoutIntentUpdateParamsToPayoutMethodOptions": (
        "stripe.params.v2.money_management._payout_intent_update_params",
        False,
    ),
    "PayoutIntentUpdateParamsToPayoutMethodOptionsBankAccount": (
        "stripe.params.v2.money_management._payout_intent_update_params",
        False,
    ),
    "PayoutIntentUpdateParamsToPayoutMethodOptionsBankAccountPreferredNetworkOptions": (
        "stripe.params.v2.money_management._payout_intent_update_params",
        False,
    ),
    "PayoutIntentUpdateParamsToPayoutMethodOptionsBankAccountPreferredNetworkOptionsAch": (
        "stripe.params.v2.money_management._payout_intent_update_params",
        False,
    ),
    "PayoutMethodArchiveParams": (
        "stripe.params.v2.money_management._payout_method_archive_params",
        False,
    ),
    "PayoutMethodListParams": (
        "stripe.params.v2.money_management._payout_method_list_params",
        False,
    ),
    "PayoutMethodListParamsUsageStatus": (
        "stripe.params.v2.money_management._payout_method_list_params",
        False,
    ),
    "PayoutMethodRetrieveParams": (
        "stripe.params.v2.money_management._payout_method_retrieve_params",
        False,
    ),
    "PayoutMethodUnarchiveParams": (
        "stripe.params.v2.money_management._payout_method_unarchive_params",
        False,
    ),
    "PayoutMethodsBankAccountSpecRetrieveParams": (
        "stripe.params.v2.money_management._payout_methods_bank_account_spec_retrieve_params",
        False,
    ),
    "ReceivedCreditListParams": (
        "stripe.params.v2.money_management._received_credit_list_params",
        False,
    ),
    "ReceivedCreditListParamsCreated": (
        "stripe.params.v2.money_management._received_credit_list_params",
        False,
    ),
    "ReceivedCreditRetrieveParams": (
        "stripe.params.v2.money_management._received_credit_retrieve_params",
        False,
    ),
    "RecipientVerificationAcknowledgeParams": (
        "stripe.params.v2.money_management._recipient_verification_acknowledge_params",
        False,
    ),
    "RecipientVerificationCreateParams": (
        "stripe.params.v2.money_management._recipient_verification_create_params",
        False,
    ),
    "RecipientVerificationRetrieveParams": (
        "stripe.params.v2.money_management._recipient_verification_retrieve_params",
        False,
    ),
    "TransactionEntryListParams": (
        "stripe.params.v2.money_management._transaction_entry_list_params",
        False,
    ),
    "TransactionEntryListParamsCreated": (
        "stripe.params.v2.money_management._transaction_entry_list_params",
        False,
    ),
    "TransactionEntryRetrieveParams": (
        "stripe.params.v2.money_management._transaction_entry_retrieve_params",
        False,
    ),
    "TransactionListParams": (
        "stripe.params.v2.money_management._transaction_list_params",
        False,
    ),
    "TransactionListParamsCreated": (
        "stripe.params.v2.money_management._transaction_list_params",
        False,
    ),
    "TransactionRefreshRegulatoryReceiptParams": (
        "stripe.params.v2.money_management._transaction_refresh_regulatory_receipt_params",
        False,
    ),
    "TransactionRetrieveParams": (
        "stripe.params.v2.money_management._transaction_retrieve_params",
        False,
    ),
    "TransactionUpdateParams": (
        "stripe.params.v2.money_management._transaction_update_params",
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
