---
title: Update generated code
pr_url: https://github.com/stripe/stripe-python/pull/1952
semver_level: major
is_stripe_api_change: true
released_in_version: 16.2.0a1
---

* Add support for new resources `v2.billing.ContractTermQuantityChange`, `v2.billing.ContractTerm`, `v2.core.AccountSession`, `v2.money_management.FundingIntent`, `v2.money_management.InboundFunding`, `v2.money_management.RewardProgramEnrollment`, `v2.money_management.RewardProgramRule`, `v2.money_management.RewardProgram`, and `v2.risk.Form`
* ⚠️ Remove support for resource `v2.risk.Inquiry`
* Add support for `modify` and `retrieve` methods on resource `v2.risk.Form`
* Add support for `activate`, `create`, `deactivate`, `list`, and `retrieve` methods on resource `v2.money_management.RewardProgramEnrollment`
* Add support for `activate`, `create`, `deactivate`, `list`, `modify`, and `retrieve` methods on resources `v2.money_management.RewardProgramRule` and `v2.money_management.RewardProgram`
* Add support for `list` and `retrieve` methods on resource `v2.money_management.InboundFunding`
* Add support for `cancel`, `confirm`, `create`, `list`, `modify`, and `retrieve` methods on resource `v2.money_management.FundingIntent`
* Add support for `create` method on resource `v2.core.AccountSession`
* Add support for `list_contract_terms` and `retrieve_contract_term` methods on resource `v2.billing.ContractTerm`
* ⚠️ Remove support for `list`, `modify`, and `retrieve` methods on resource `v2.risk.Inquiry`
* ⚠️ Remove support for `fx_quote` method on resource `v2.money_management.PayoutIntent`
* Add support for `reject` and `unreject` methods on resource `v2.core.Account`
* Add support for `billing_group` on `Billing.Alert.SpendThreshold.Filter`, `Billing.AlertNotification`, `Billing.AlertTriggered.GroupBy`, `billing.AlertCreateParamsSpendThresholdFilter`, and `billing.BillingAlertListAlertNotificationParams`
* Add support for `toss_pay` on `Charge.PaymentMethodDetail`, `ConfirmationToken.PaymentMethodPreview`, `ConfirmationTokenCreateParamsPaymentMethodDatum`, `PaymentAttemptRecord.PaymentMethodDetail`, `PaymentIntent.PaymentMethodOption`, `PaymentIntentConfirmParamsPaymentMethodDatum`, `PaymentIntentConfirmParamsPaymentMethodOption`, `PaymentIntentCreateParamsPaymentMethodDatum`, `PaymentIntentCreateParamsPaymentMethodOption`, `PaymentIntentModifyParamsPaymentMethodDatum`, `PaymentIntentModifyParamsPaymentMethodOption`, `PaymentMethodCreateParams`, `PaymentMethod`, `PaymentRecord.PaymentMethodDetail`, `SetupIntentConfirmParamsPaymentMethodDatum`, `SetupIntentCreateParamsPaymentMethodDatum`, and `SetupIntentModifyParamsPaymentMethodDatum`
* Add support for `mandate` on `Charge.PaymentMethodDetail.Paypay`, `PaymentAttemptRecord.PaymentMethodDetail.Paypay`, `PaymentRecord.PaymentMethodDetail.Paypay`, `Subscription.PaymentSetting`, `SubscriptionCreateParamsPaymentSetting`, and `SubscriptionModifyParamsPaymentSetting`
* Add support for `automatic_pass_through_fee` on `Checkout.Session` and `checkout.SessionCreateParams`
* Add support for `paypay` on `Checkout.Session.PaymentMethodOption` and `checkout.SessionCreateParamsPaymentMethodOption`
* Change `checkout.SessionCreateParamsMarketingAttribution.ad_conversion` to be optional
* Add support for `adjustable_quantity` on `Checkout.Session.Item.Subscription.Item`
* ⚠️ Change `Checkout.Session.MarketingAttribution.ad_conversion` to be optional
* Add support for `marketing_attributions` on `CustomerCreateParams` and `Customer`
* Add support for `merchant_of_record` on `PaymentIntent.PaymentDetail.MoneyService.AccountFunding`, `PaymentIntentConfirmParamsPaymentDetailMoneyServiceAccountFunding`, `PaymentIntentCreateParamsPaymentDetailMoneyServiceAccountFunding`, and `PaymentIntentModifyParamsPaymentDetailMoneyServiceAccountFunding`
* ⚠️ Change type of `Radar.PaymentEvaluation.Signal.early_fraud_warning` from `Payment Evaluation Signal` to `nullable(Payment Evaluation Signal)`
* Change `Radar.PaymentEvaluation.Signal.early_fraud_warning` to be required
* Add support for `payment_method_data` and `payment_method_options` on `RefundCreateParams`
* Add support for new value `toss_pay` on enum `SetupIntentConfirmParams.allowed_payment_method_types`
* Add support for `debit_behavior` on `Subscription.PaymentSetting.PaymentMethodOption.SepaDebit`, `SubscriptionCreateParamsPaymentSettingPaymentMethodOptionSepaDebit`, and `SubscriptionModifyParamsPaymentSettingPaymentMethodOptionSepaDebit`
* Add support for `terms` on `V2.Billing.Contract`, `v2.billing.ContractCancelParams`, and `v2.billing.ContractCreateParams`
* ⚠️ Add support for new value `user_affinity` on enum `V2.Core.AccountEvaluation.evaluations_triggered`
* ⚠️ Remove support for value `user_merchant_fit` from enum `V2.Core.AccountEvaluation.evaluations_triggered`
* Add support for `rejection` on `V2.Core.Account`
* Add support for `alipay_payments`, `scalapay_payments`, and `upi_payments` on `V2.Core.Account.Configuration.Merchant.Capability`, `v2.core.AccountCreateParamsConfigurationMerchantCapability`, and `v2.core.AccountModifyParamsConfigurationMerchantCapability`
* Add support for `inbound_fundings` on `V2.Core.Account.Configuration.MoneyManager.Capability`, `v2.core.AccountCreateParamsConfigurationMoneyManagerCapability`, and `v2.core.AccountModifyParamsConfigurationMoneyManagerCapability`
* ⚠️ Remove support for `instant` and `sepa_credit` on `V2.Core.Account.Configuration.Recipient.Capability.BankAccount`, `v2.core.AccountCreateParamsConfigurationRecipientCapabilityBankAccount`, and `v2.core.AccountModifyParamsConfigurationRecipientCapabilityBankAccount`
* Add support for `compression` on `V2.Data.QueryRun.ResultOption`, `V2.Data.ReportRun.ResultOption`, `v2.data.QueryRunCreateParamsResultOption`, and `v2.data.ReportRunCreateParamsResultOption`
* ⚠️ Remove support for `compress_file` on `V2.Data.QueryRun.ResultOption`, `V2.Data.ReportRun.ResultOption`, `v2.data.QueryRunCreateParamsResultOption`, and `v2.data.ReportRunCreateParamsResultOption`
* Add support for `query_errors` on `V2.Data.QueryRun.StatusDetail` and `V2.Data.ReportRun.StatusDetail`
* Add support for new values `execution_failed` and `resource_limit_exceeded` on enums `V2.Data.QueryRun.StatusDetail.code` and `V2.Data.ReportRun.StatusDetail.code`
* Add support for `format` on `V2.Data.ReportRun`
* Add support for `refreshed_at` on `V2.Data.Report`
* Add support for `schema_name` on `V2.Data.Schema.Column.ForeignKeysFrom` and `V2.Data.Schema.Column.ForeignKeysTo`
* ⚠️ Remove support for `authentication` and `session_fingerprint` on `V2.Iam.ActivityLog.Detail.UserAccess`
* Add support for `user_agent` on `V2.Iam.ActivityLog.Detail.UserAccess.DashboardClient`
* ⚠️ Remove support for `browser_version`, `browser`, `device_type`, and `os` on `V2.Iam.ActivityLog.Detail.UserAccess.DashboardClient`
* ⚠️ Remove support for `level` on `V2.Iam.ActivityLog.Detail.UserAccess.Risk`
* Add support for `reference` on `V2.MoneyManagement.FinancialAddress.BankAccount.Iban`
* Add support for new value `sepa` on enums `V2.MoneyManagement.OutboundPayment.To.PayoutMethodOption.BankAccount.preferred_networks`, `V2.MoneyManagement.OutboundPaymentQuote.To.PayoutMethodOption.BankAccount.preferred_networks`, `V2.MoneyManagement.OutboundTransfer.To.PayoutMethodOption.BankAccount.preferred_networks`, `V2.MoneyManagement.PayoutIntent.To.PayoutMethodOption.BankAccount.preferred_networks`, `v2.money_management.OutboundPaymentCreateParamsToPayoutMethodOptionBankAccount.preferred_networks`, `v2.money_management.OutboundPaymentQuoteCreateParamsToPayoutMethodOptionBankAccount.preferred_networks`, `v2.money_management.OutboundTransferCreateParamsToPayoutMethodOptionBankAccount.preferred_networks`, `v2.money_management.PayoutIntentCreateParamsToPayoutMethodOptionBankAccount.preferred_networks`, and `v2.money_management.PayoutIntentModifyParamsToPayoutMethodOptionBankAccount.preferred_networks`
* ⚠️ Change `V2.MoneyManagement.OutboundPayment.To.PayoutMethodOption.BankAccount.preferred_networks`, `V2.MoneyManagement.OutboundPaymentQuote.To.PayoutMethodOption.BankAccount.preferred_networks`, and `V2.MoneyManagement.PayoutIntent.To.PayoutMethodOption.BankAccount.preferred_networks` to be optional
* Add support for `bank_account`, `card`, `crypto_wallet`, `status`, and `type` on `V2.MoneyManagement.OutboundPayment.TrackingDetail`
* Add support for `recipient_verification` on `V2.MoneyManagement.PayoutIntent`
* Add support for `fields_to_review` on `V2.MoneyManagement.PayoutIntent.NextAction.Confirm`
* ⚠️ Add support for new values `payout_method_invalid` and `recipient_capability_not_active` on enum `V2.MoneyManagement.PayoutIntent.NextAction.HandleFailure.failure_reason`
* ⚠️ Remove support for value `currency_required` from enum `V2.MoneyManagement.PayoutIntent.NextAction.HandleFailure.failure_reason`
* ⚠️ Change `V2.MoneyManagement.PayoutIntent.latest_payout` to be optional
* ⚠️ Remove support for `ca_bank_account`, `eu_bank_account`, and `mx_bank_account` on `V2.MoneyManagement.ReceivedCredit.BankTransfer`
* ⚠️ Remove support for `network` on `V2.MoneyManagement.ReceivedCredit.BankTransfer.OriginatingBankAccount.Aba`, `V2.MoneyManagement.ReceivedCredit.BankTransfer.OriginatingBankAccount.BreB`, `V2.MoneyManagement.ReceivedCredit.BankTransfer.OriginatingBankAccount.Clabe`, `V2.MoneyManagement.ReceivedCredit.BankTransfer.OriginatingBankAccount.Cpa`, `V2.MoneyManagement.ReceivedCredit.BankTransfer.OriginatingBankAccount.Iban`, `V2.MoneyManagement.ReceivedCredit.BankTransfer.OriginatingBankAccount.Nip`, `V2.MoneyManagement.ReceivedCredit.BankTransfer.OriginatingBankAccount.Pix`, and `V2.MoneyManagement.ReceivedCredit.BankTransfer.OriginatingBankAccount.SortCode`
* Add support for `payout_method`, `recipient`, and `verification_type` on `V2.MoneyManagement.RecipientVerification`
* ⚠️ Change type of `V2.MoneyManagement.RecipientVerification.consumed_by` from `string` to `an object`
* Add support for `matched_business_type` and `provided_business_type` on `V2.MoneyManagement.RecipientVerification.MatchResultDetail`
* ⚠️ Change `V2.MoneyManagement.RecipientVerification.expires_at` to be optional
* ⚠️ Remove support for value `requires_capture` from enum `V2.Payments.OffSessionPayment.status`
* Add support for `configuration` on `V2.Provisioning.Resource`
* Add support for `custom_marketing_action` and `triggering_signal` on `V2.Signals.AccountActivity` and `v2.signals.AccountActivityCreateParams`
* Add support for `mfa_challenges` on `V2.Signals.AccountActivity.LoginDecision` and `v2.signals.AccountActivityCreateParamsLoginDecision`
* Add support for new value `custom_marketing_action` on enums `V2.Signals.AccountActivity.type`, `v2.signals.AccountActivityCreateParams.type`, and `v2.signals.AccountEvaluationCreateParamsAccountActivityDetailData.type`
* Add support for `user_affinity` on `V2.Signals.AccountEvaluation.EvaluatedSignal` and `V2.Signals.AccountSignal`
* ⚠️ Remove support for `user_merchant_fit` on `V2.Signals.AccountEvaluation.EvaluatedSignal` and `V2.Signals.AccountSignal`
* ⚠️ Add support for new value `user_affinity` on enum `V2.Signals.AccountEvaluation.pending_signals`
* ⚠️ Remove support for value `user_merchant_fit` from enum `V2.Signals.AccountEvaluation.pending_signals`
* ⚠️ Add support for new value `user_affinity` on enums `V2.Signals.AccountEvaluation.requested_signals` and `v2.signals.AccountEvaluationCreateParams.requested_signals`
* ⚠️ Remove support for value `user_merchant_fit` from enums `V2.Signals.AccountEvaluation.requested_signals` and `v2.signals.AccountEvaluationCreateParams.requested_signals`
* Add support for `additional_details` on `V2.Signals.AccountSignal.CustomerRisk`
* ⚠️ Add support for new value `user_affinity` on enums `V2.Signals.AccountSignal.type` and `v2.signals.AccountSignalListParams.type`
* ⚠️ Remove support for value `user_merchant_fit` from enums `V2.Signals.AccountSignal.type` and `v2.signals.AccountSignalListParams.type`
* Add support for `subscriptions` on `V2.Tax.IntegrationConfiguration` and `v2.tax.IntegrationConfigurationModifyParams`
* Add support for `include` on `v2.provisioning.ResourceRetrieveParams`
* Change `v2.money_management.OutboundPaymentCreateParamsToPayoutMethodOptionBankAccount.preferred_networks`, `v2.money_management.OutboundPaymentQuoteCreateParamsToPayoutMethodOptionBankAccount.preferred_networks`, `v2.money_management.PayoutIntentCreateParamsToPayoutMethodOptionBankAccount.preferred_networks`, and `v2.money_management.PayoutIntentModifyParamsToPayoutMethodOptionBankAccount.preferred_networks` to be optional
* ⚠️ Remove support for `amount` and `from` on `v2.money_management.PayoutIntentModifyParams`
* Add support for new value `pln` on enum `v2.money_management.FinancialAddressCreateParamsBankAccount.currency`
* Add support for `parameters` on `v2.data.QueryRunCreateParams`
* Add support for new value `dynamic_cvc` on enum `v2.core.vault.NetworkTokenGenerateCryptogramParams.type`
* ⚠️ Add support for new value `user_affinity` on enum `v2.core.AccountEvaluationCreateParams.signals`
* ⚠️ Remove support for value `user_merchant_fit` from enum `v2.core.AccountEvaluationCreateParams.signals`
* Add support for new value `terms` on enums `v2.billing.ContractActivateParams.include`, `v2.billing.ContractCancelParams.include`, `v2.billing.ContractCreateParams.include`, `v2.billing.ContractListParams.include`, `v2.billing.ContractModifyParams.include`, and `v2.billing.ContractRetrieveParams.include`
* Add support for `actions` on `v2.billing.ContractModifyParams`
* Add support for new values `alipay_payments`, `scalapay_payments`, and `upi_payments` on enum `EventsV2CoreAccountIncludingConfigurationMerchantCapabilityStatusUpdatedEvent.updated_capability`
* Add support for new value `inbound_fundings.paper_checks` on enum `EventsV2CoreAccountIncludingConfigurationMoneyManagerCapabilityStatusUpdatedEvent.updated_capability`
* Add support for `severity` on `EventsV2CoreHealthApiErrorFiringEvent`, `EventsV2CoreHealthApiErrorResolvedEvent`, `EventsV2CoreHealthApiLatencyFiringEvent`, `EventsV2CoreHealthApiLatencyResolvedEvent`, `EventsV2CoreHealthAuthorizationRateDropFiringEvent`, `EventsV2CoreHealthAuthorizationRateDropResolvedEvent`, `EventsV2CoreHealthElementsErrorFiringEvent`, `EventsV2CoreHealthElementsErrorResolvedEvent`, `EventsV2CoreHealthFraudRateIncreasedEvent`, `EventsV2CoreHealthInvoiceCountDroppedFiringEvent`, `EventsV2CoreHealthInvoiceCountDroppedResolvedEvent`, `EventsV2CoreHealthIssuingAuthorizationRequestErrorsFiringEvent`, `EventsV2CoreHealthIssuingAuthorizationRequestErrorsResolvedEvent`, `EventsV2CoreHealthIssuingAuthorizationRequestTimeoutFiringEvent`, `EventsV2CoreHealthIssuingAuthorizationRequestTimeoutResolvedEvent`, `EventsV2CoreHealthMeterEventSummariesDelayedFiringEvent`, `EventsV2CoreHealthMeterEventSummariesDelayedResolvedEvent`, `EventsV2CoreHealthMetronomeNotificationLatencyFiringEvent`, `EventsV2CoreHealthMetronomeNotificationLatencyResolvedEvent`, `EventsV2CoreHealthPaymentMethodErrorFiringEvent`, `EventsV2CoreHealthPaymentMethodErrorResolvedEvent`, `EventsV2CoreHealthSepaDebitDelayedFiringEvent`, `EventsV2CoreHealthSepaDebitDelayedResolvedEvent`, `EventsV2CoreHealthTrafficVolumeDropFiringEvent`, `EventsV2CoreHealthTrafficVolumeDropResolvedEvent`, `EventsV2CoreHealthWebhookLatencyFiringEvent`, and `EventsV2CoreHealthWebhookLatencyResolvedEvent`
* Add support for event notifications `V2BillingContractTermCreatedEvent`, `V2BillingContractTermDeletedEvent`, and `V2BillingContractTermUpdatedEvent` with related object `v2.billing.ContractTerm`
* Add support for event notifications `V2MoneyManagementFundingIntentCanceledEvent`, `V2MoneyManagementFundingIntentCreatedEvent`, `V2MoneyManagementFundingIntentProcessingEvent`, `V2MoneyManagementFundingIntentRequiresActionEvent`, `V2MoneyManagementFundingIntentRequiresConfirmationEvent`, `V2MoneyManagementFundingIntentSucceededEvent`, `V2MoneyManagementFundingIntentUpdatedEvent`, and `V2MoneyManagementFundingIntentValidatingEvent` with related object `v2.money_management.FundingIntent`
* Add support for event notifications `V2MoneyManagementInboundFundingAvailableEvent`, `V2MoneyManagementInboundFundingCheckFailedEvent`, `V2MoneyManagementInboundFundingCheckProcessingEvent`, `V2MoneyManagementInboundFundingCheckQueuedEvent`, `V2MoneyManagementInboundFundingCheckReturnedEvent`, `V2MoneyManagementInboundFundingCheckSucceededEvent`, `V2MoneyManagementInboundFundingCreatedEvent`, and `V2MoneyManagementInboundFundingUpdatedEvent` with related object `v2.money_management.InboundFunding`
* Add support for event notifications `V2MoneyManagementRewardProgramRewardEarnedEvent` and `V2MoneyManagementRewardProgramRewardReversedEvent` with related object `v2.money_management.RewardProgram`
* ⚠️ Remove support for event notifications `V2PaymentsOffSessionPaymentAuthorizationAttemptFailedEvent` and `V2PaymentsOffSessionPaymentAuthorizationAttemptStartedEvent` with related object `v2.payments.OffSessionPayment`
* Add support for error codes `check_funding_intent_confirmation_method_cannot_be_updated`, `check_funding_intent_details_cannot_be_updated`, `check_funding_intent_too_large`, `funding_intent_cannot_be_canceled`, and `funding_intent_cannot_be_confirmed` on `CannotProceedError`
* Add support for error code `funding_intent_settlement_timing_not_available_for_account_type` on `FeatureNotEnabledError`
