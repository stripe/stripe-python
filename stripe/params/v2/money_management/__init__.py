# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.v2.money_management._adjustment_list_params import (
        AdjustmentListParams as AdjustmentListParams,
    )
    from stripe.params.v2.money_management._adjustment_retrieve_params import (
        AdjustmentRetrieveParams as AdjustmentRetrieveParams,
    )
    from stripe.params.v2.money_management._currency_conversion_create_params import (
        CurrencyConversionCreateParams as CurrencyConversionCreateParams,
        CurrencyConversionCreateParamsFrom as CurrencyConversionCreateParamsFrom,
        CurrencyConversionCreateParamsFromAmount as CurrencyConversionCreateParamsFromAmount,
        CurrencyConversionCreateParamsTo as CurrencyConversionCreateParamsTo,
        CurrencyConversionCreateParamsToAmount as CurrencyConversionCreateParamsToAmount,
    )
    from stripe.params.v2.money_management._currency_conversion_list_params import (
        CurrencyConversionListParams as CurrencyConversionListParams,
    )
    from stripe.params.v2.money_management._currency_conversion_retrieve_params import (
        CurrencyConversionRetrieveParams as CurrencyConversionRetrieveParams,
    )
    from stripe.params.v2.money_management._financial_account_close_params import (
        FinancialAccountCloseParams as FinancialAccountCloseParams,
        FinancialAccountCloseParamsForwardingSettings as FinancialAccountCloseParamsForwardingSettings,
    )
    from stripe.params.v2.money_management._financial_account_create_params import (
        FinancialAccountCreateParams as FinancialAccountCreateParams,
        FinancialAccountCreateParamsStorage as FinancialAccountCreateParamsStorage,
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
        FinancialAddressCreateParamsSepaBankAccount as FinancialAddressCreateParamsSepaBankAccount,
    )
    from stripe.params.v2.money_management._financial_address_list_params import (
        FinancialAddressListParams as FinancialAddressListParams,
    )
    from stripe.params.v2.money_management._financial_address_retrieve_params import (
        FinancialAddressRetrieveParams as FinancialAddressRetrieveParams,
    )
    from stripe.params.v2.money_management._inbound_transfer_create_params import (
        InboundTransferCreateParams as InboundTransferCreateParams,
        InboundTransferCreateParamsAmount as InboundTransferCreateParamsAmount,
        InboundTransferCreateParamsFrom as InboundTransferCreateParamsFrom,
        InboundTransferCreateParamsTo as InboundTransferCreateParamsTo,
    )
    from stripe.params.v2.money_management._inbound_transfer_list_params import (
        InboundTransferListParams as InboundTransferListParams,
    )
    from stripe.params.v2.money_management._inbound_transfer_retrieve_params import (
        InboundTransferRetrieveParams as InboundTransferRetrieveParams,
    )
    from stripe.params.v2.money_management._outbound_payment_cancel_params import (
        OutboundPaymentCancelParams as OutboundPaymentCancelParams,
    )
    from stripe.params.v2.money_management._outbound_payment_create_params import (
        OutboundPaymentCreateParams as OutboundPaymentCreateParams,
        OutboundPaymentCreateParamsAmount as OutboundPaymentCreateParamsAmount,
        OutboundPaymentCreateParamsDeliveryOptions as OutboundPaymentCreateParamsDeliveryOptions,
        OutboundPaymentCreateParamsDeliveryOptionsPaperCheck as OutboundPaymentCreateParamsDeliveryOptionsPaperCheck,
        OutboundPaymentCreateParamsFrom as OutboundPaymentCreateParamsFrom,
        OutboundPaymentCreateParamsRecipientNotification as OutboundPaymentCreateParamsRecipientNotification,
        OutboundPaymentCreateParamsTo as OutboundPaymentCreateParamsTo,
    )
    from stripe.params.v2.money_management._outbound_payment_list_params import (
        OutboundPaymentListParams as OutboundPaymentListParams,
    )
    from stripe.params.v2.money_management._outbound_payment_quote_create_params import (
        OutboundPaymentQuoteCreateParams as OutboundPaymentQuoteCreateParams,
        OutboundPaymentQuoteCreateParamsAmount as OutboundPaymentQuoteCreateParamsAmount,
        OutboundPaymentQuoteCreateParamsDeliveryOptions as OutboundPaymentQuoteCreateParamsDeliveryOptions,
        OutboundPaymentQuoteCreateParamsFrom as OutboundPaymentQuoteCreateParamsFrom,
        OutboundPaymentQuoteCreateParamsTo as OutboundPaymentQuoteCreateParamsTo,
    )
    from stripe.params.v2.money_management._outbound_payment_quote_retrieve_params import (
        OutboundPaymentQuoteRetrieveParams as OutboundPaymentQuoteRetrieveParams,
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
        OutboundSetupIntentCreateParamsPayoutMethodDataCard as OutboundSetupIntentCreateParamsPayoutMethodDataCard,
        OutboundSetupIntentCreateParamsPayoutMethodDataCryptoWallet as OutboundSetupIntentCreateParamsPayoutMethodDataCryptoWallet,
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
        OutboundSetupIntentUpdateParamsPayoutMethodDataCard as OutboundSetupIntentUpdateParamsPayoutMethodDataCard,
    )
    from stripe.params.v2.money_management._outbound_transfer_cancel_params import (
        OutboundTransferCancelParams as OutboundTransferCancelParams,
    )
    from stripe.params.v2.money_management._outbound_transfer_create_params import (
        OutboundTransferCreateParams as OutboundTransferCreateParams,
        OutboundTransferCreateParamsAmount as OutboundTransferCreateParamsAmount,
        OutboundTransferCreateParamsDeliveryOptions as OutboundTransferCreateParamsDeliveryOptions,
        OutboundTransferCreateParamsFrom as OutboundTransferCreateParamsFrom,
        OutboundTransferCreateParamsTo as OutboundTransferCreateParamsTo,
    )
    from stripe.params.v2.money_management._outbound_transfer_list_params import (
        OutboundTransferListParams as OutboundTransferListParams,
    )
    from stripe.params.v2.money_management._outbound_transfer_retrieve_params import (
        OutboundTransferRetrieveParams as OutboundTransferRetrieveParams,
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
    )
    from stripe.params.v2.money_management._received_credit_retrieve_params import (
        ReceivedCreditRetrieveParams as ReceivedCreditRetrieveParams,
    )
    from stripe.params.v2.money_management._received_debit_list_params import (
        ReceivedDebitListParams as ReceivedDebitListParams,
    )
    from stripe.params.v2.money_management._received_debit_retrieve_params import (
        ReceivedDebitRetrieveParams as ReceivedDebitRetrieveParams,
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
    )
    from stripe.params.v2.money_management._transaction_entry_retrieve_params import (
        TransactionEntryRetrieveParams as TransactionEntryRetrieveParams,
    )
    from stripe.params.v2.money_management._transaction_list_params import (
        TransactionListParams as TransactionListParams,
    )
    from stripe.params.v2.money_management._transaction_retrieve_params import (
        TransactionRetrieveParams as TransactionRetrieveParams,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "AdjustmentListParams": (
        "stripe.params.v2.money_management._adjustment_list_params",
        False,
    ),
    "AdjustmentRetrieveParams": (
        "stripe.params.v2.money_management._adjustment_retrieve_params",
        False,
    ),
    "CurrencyConversionCreateParams": (
        "stripe.params.v2.money_management._currency_conversion_create_params",
        False,
    ),
    "CurrencyConversionCreateParamsFrom": (
        "stripe.params.v2.money_management._currency_conversion_create_params",
        False,
    ),
    "CurrencyConversionCreateParamsFromAmount": (
        "stripe.params.v2.money_management._currency_conversion_create_params",
        False,
    ),
    "CurrencyConversionCreateParamsTo": (
        "stripe.params.v2.money_management._currency_conversion_create_params",
        False,
    ),
    "CurrencyConversionCreateParamsToAmount": (
        "stripe.params.v2.money_management._currency_conversion_create_params",
        False,
    ),
    "CurrencyConversionListParams": (
        "stripe.params.v2.money_management._currency_conversion_list_params",
        False,
    ),
    "CurrencyConversionRetrieveParams": (
        "stripe.params.v2.money_management._currency_conversion_retrieve_params",
        False,
    ),
    "FinancialAccountCloseParams": (
        "stripe.params.v2.money_management._financial_account_close_params",
        False,
    ),
    "FinancialAccountCloseParamsForwardingSettings": (
        "stripe.params.v2.money_management._financial_account_close_params",
        False,
    ),
    "FinancialAccountCreateParams": (
        "stripe.params.v2.money_management._financial_account_create_params",
        False,
    ),
    "FinancialAccountCreateParamsStorage": (
        "stripe.params.v2.money_management._financial_account_create_params",
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
    "FinancialAddressCreateParamsSepaBankAccount": (
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
    "InboundTransferCreateParamsAmount": (
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
    "OutboundPaymentCreateParamsAmount": (
        "stripe.params.v2.money_management._outbound_payment_create_params",
        False,
    ),
    "OutboundPaymentCreateParamsDeliveryOptions": (
        "stripe.params.v2.money_management._outbound_payment_create_params",
        False,
    ),
    "OutboundPaymentCreateParamsDeliveryOptionsPaperCheck": (
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
    "OutboundPaymentListParams": (
        "stripe.params.v2.money_management._outbound_payment_list_params",
        False,
    ),
    "OutboundPaymentQuoteCreateParams": (
        "stripe.params.v2.money_management._outbound_payment_quote_create_params",
        False,
    ),
    "OutboundPaymentQuoteCreateParamsAmount": (
        "stripe.params.v2.money_management._outbound_payment_quote_create_params",
        False,
    ),
    "OutboundPaymentQuoteCreateParamsDeliveryOptions": (
        "stripe.params.v2.money_management._outbound_payment_quote_create_params",
        False,
    ),
    "OutboundPaymentQuoteCreateParamsFrom": (
        "stripe.params.v2.money_management._outbound_payment_quote_create_params",
        False,
    ),
    "OutboundPaymentQuoteCreateParamsTo": (
        "stripe.params.v2.money_management._outbound_payment_quote_create_params",
        False,
    ),
    "OutboundPaymentQuoteRetrieveParams": (
        "stripe.params.v2.money_management._outbound_payment_quote_retrieve_params",
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
    "OutboundSetupIntentCreateParamsPayoutMethodDataCard": (
        "stripe.params.v2.money_management._outbound_setup_intent_create_params",
        False,
    ),
    "OutboundSetupIntentCreateParamsPayoutMethodDataCryptoWallet": (
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
    "OutboundSetupIntentUpdateParamsPayoutMethodDataCard": (
        "stripe.params.v2.money_management._outbound_setup_intent_update_params",
        False,
    ),
    "OutboundTransferCancelParams": (
        "stripe.params.v2.money_management._outbound_transfer_cancel_params",
        False,
    ),
    "OutboundTransferCreateParams": (
        "stripe.params.v2.money_management._outbound_transfer_create_params",
        False,
    ),
    "OutboundTransferCreateParamsAmount": (
        "stripe.params.v2.money_management._outbound_transfer_create_params",
        False,
    ),
    "OutboundTransferCreateParamsDeliveryOptions": (
        "stripe.params.v2.money_management._outbound_transfer_create_params",
        False,
    ),
    "OutboundTransferCreateParamsFrom": (
        "stripe.params.v2.money_management._outbound_transfer_create_params",
        False,
    ),
    "OutboundTransferCreateParamsTo": (
        "stripe.params.v2.money_management._outbound_transfer_create_params",
        False,
    ),
    "OutboundTransferListParams": (
        "stripe.params.v2.money_management._outbound_transfer_list_params",
        False,
    ),
    "OutboundTransferRetrieveParams": (
        "stripe.params.v2.money_management._outbound_transfer_retrieve_params",
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
    "ReceivedCreditRetrieveParams": (
        "stripe.params.v2.money_management._received_credit_retrieve_params",
        False,
    ),
    "ReceivedDebitListParams": (
        "stripe.params.v2.money_management._received_debit_list_params",
        False,
    ),
    "ReceivedDebitRetrieveParams": (
        "stripe.params.v2.money_management._received_debit_retrieve_params",
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
    "TransactionEntryRetrieveParams": (
        "stripe.params.v2.money_management._transaction_entry_retrieve_params",
        False,
    ),
    "TransactionListParams": (
        "stripe.params.v2.money_management._transaction_list_params",
        False,
    ),
    "TransactionRetrieveParams": (
        "stripe.params.v2.money_management._transaction_retrieve_params",
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
