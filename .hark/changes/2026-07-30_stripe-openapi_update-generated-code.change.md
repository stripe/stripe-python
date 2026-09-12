---
title: Update generated code for private-preview
pr_url: https://github.com/stripe/stripe-python/pull/1854
is_breaking: true
is_stripe_api_change: true
released_in_version: 15.5.0a1
---

* Add support for new resources `v2.money_management.ReceivedDebitMandate`, `v2.risk.Inquiry`, `v2.signals.AccountActivity`, and `v2.signals.AccountEvaluation`
* Add support for `create` and `retrieve` methods on resource `v2.signals.AccountEvaluation`
* Add support for `create`, `delete`, and `retrieve` methods on resource `v2.signals.AccountActivity`
* Add support for `list`, `modify`, and `retrieve` methods on resource `v2.risk.Inquiry`
* Add support for `cancel`, `list`, and `retrieve` methods on resource `v2.money_management.ReceivedDebitMandate`
* Add support for `rate_cards` on `Billing.CreditGrant.ApplicabilityConfig.Scope`, `billing.CreditBalanceSummaryRetrieveParamsFilterApplicabilityScope`, and `billing.CreditGrantCreateParamsApplicabilityConfigScope`
* ⚠️ Change type of `ConfirmationToken.PaymentMethodPreview.GiftCard.brand`, `GiftCard.brand`, `GiftCardCreateParams.brand`, `PaymentMethod.GiftCard.brand`, `terminal.ReaderActivateGiftCardParams.brand`, `terminal.ReaderCashoutGiftCardParams.brand`, `terminal.ReaderCheckGiftCardBalanceParams.brand`, and `terminal.ReaderReloadGiftCardParams.brand` from `enum('fiserv_valuelink'|'givex'|'svs')` to `literal('svs')`
* Add support for new value `tempo` on enum `Crypto.CustomerConsumerWallet.network`
* Add support for new value `tempo` on enums `Crypto.OnrampSession.TransactionDetail.destination_network`, `crypto.OnrampSessionCreateParams.destination_network`, `crypto.OnrampSessionListParams.destination_network`, and `crypto.OnrampTransactionLimitsRetrieveParams.destination_network`
* Add support for new value `tempo` on enums `Crypto.OnrampSession.TransactionDetail.destination_networks` and `crypto.OnrampSessionCreateParams.destination_networks`
* Add support for `tempo` on `Crypto.OnrampSession.TransactionDetail.WalletAddress`
* Add support for new value `try_again_later` on enum `GiftCardOperation.failure_code`
* Add support for `healthcare` on `Issuing.Authorization`
* Add support for `product_code` on `Issuing.Card`, `issuing.CardCreateParams`, and `issuing.CardModifyParams`
* Add support for `product_graduation_state` on `Issuing.Card`
* Add support for `cvc` and `number` on `radar.PaymentEvaluationCreateParamsPaymentDetailPaymentMethodDetailCard`
* Change `radar.PaymentEvaluationCreateParamsPaymentDetailPaymentMethodDetailCard.first6` to be optional
* Change `radar.PaymentEvaluationCreateParamsPaymentDetailPaymentMethodDetailCard.last4` to be optional
* Add support for `card` on `Radar.PaymentEvaluation.PaymentDetail.PaymentMethodDetail`
* ⚠️ Change type of `terminal.ReaderCollectPaymentMethodParamsCollectConfig.gift_card_brand` and `terminal.ReaderProcessPaymentIntentParamsProcessConfig.gift_card_brand` from `enum('fiserv_valuelink'|'givex'|'svs')` to `literal('svs')`
* Add support for `gift_card` on `terminal.ReaderPresentPaymentMethodParams`
* Add support for new value `gift_card` on enum `terminal.ReaderPresentPaymentMethodParams.type`
* Add support for `amount_due` and `customer_balance_applied` on `V2.Billing.Intent.AmountDetail`
* ⚠️ Change type of `V2.Core.AccountEvaluation.evaluations_triggered` from `literal('fraudulent_website')` to `enum('fraudulent_website'|'user_account_sharing'|'user_multi_accounting')`
* Add support for `gross_settlement` on `V2.Core.Account.Configuration.Merchant`, `v2.core.AccountCreateParamsConfigurationMerchant`, and `v2.core.AccountModifyParamsConfigurationMerchant`
* ⚠️ Change type of `V2.MoneyManagement.DebitDispute.BankTransfer.network` from `literal('ach')` to `enum('ach'|'bacs')`
* Add support for new values `beneficiary_unrecognized`, `mandate_canceled_by_stripe`, `mandate_canceled`, `no_advance_notice`, `originator_requested`, and `signature_invalid` on enum `V2.MoneyManagement.DebitDispute.BankTransfer.reason`
* ⚠️ Remove support for `managed_by` on `V2.MoneyManagement.FinancialAccount`
* Add support for `payout_intent` on `V2.MoneyManagement.OutboundPayment`
* Add support for `settles_at` on `V2.MoneyManagement.ReceivedDebit`
* Add support for `gb_bank_account` on `V2.MoneyManagement.ReceivedDebit.BankTransfer`
* ⚠️ Change type of `V2.MoneyManagement.ReceivedDebit.BankTransfer.origin_type` from `literal('us_bank_account')` to `enum('gb_bank_account'|'us_bank_account')`
* ⚠️ Change type of `V2.MoneyManagement.ReceivedDebit.BankTransfer.payment_method_type` from `literal('us_bank_account')` to `enum('gb_bank_account'|'us_bank_account')`
* Add support for new value `scheduled` on enum `V2.MoneyManagement.ReceivedDebit.status`
* Add support for new value `no_mandate` on enum `V2.MoneyManagement.ReceivedDebit.StatusDetail.Failed.reason`
* Add support for `target_date` on `V2.Payments.OffSessionPayment` and `v2.payments.OffSessionPaymentCreateParams`
* Add support for `account_evaluation`, `fraudulent_website`, `payment_delinquency_exposure`, `user_account_sharing`, and `user_multi_accounting` on `V2.Signals.AccountSignal`
* Add support for new values `fraudulent_website`, `user_account_sharing`, and `user_multi_accounting` on enums `V2.Signals.AccountSignal.type` and `v2.signals.AccountSignalListParams.type`
* Change type of `v2.money_management.FinancialAddressDebitSimulationDebitParams.network` from `literal('ach')` to `enum('ach'|'bacs')`
* Add support for `received_debit_mandate` on `v2.money_management.ReceivedDebitListParams`
* ⚠️ Remove support for `payout_intent` on `v2.money_management.OutboundPaymentCreateParams`
* Change type of `v2.core.AccountEvaluationCreateParams.signals` from `literal('fraudulent_website')` to `enum('fraudulent_website'|'user_account_sharing'|'user_multi_accounting')`
* ⚠️ Remove support for `id` on `EventsV2SignalsAccountSignalFraudulentMerchantReadyEvent`
* Add support for event notifications `V2MoneyManagementReceivedDebitCreatedEvent` and `V2MoneyManagementReceivedDebitScheduledEvent` with related object `v2.money_management.ReceivedDebit`
* Add support for event notifications `V2MoneyManagementReceivedDebitMandateCanceledEvent`, `V2MoneyManagementReceivedDebitMandateCreatedEvent`, `V2MoneyManagementReceivedDebitMandateExpiredEvent`, `V2MoneyManagementReceivedDebitMandatePendingCancellationEvent`, and `V2MoneyManagementReceivedDebitMandateUpdatedEvent` with related object `v2.money_management.ReceivedDebitMandate`
* Add support for event notification `V2SignalsAccountEvaluationCompleteEvent` with related object `v2.signals.AccountEvaluation`
* Add support for event notifications `V2SignalsAccountSignalFraudulentWebsiteReadyEvent` and `V2SignalsAccountSignalPaymentDelinquencyExposureReadyEvent` with related object `v2.signals.AccountSignal`
