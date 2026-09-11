---
title: Update generated code for private-preview
pr_link: https://github.com/stripe/stripe-python/pull/1893
is_breaking: true
is_stripe_api_change: true
released_in_version: 15.7.0a2
---

* Add support for new resources `radar.BillingEvaluation`, `v2.signals.PaymentRetryEvaluation`, `v2.signals.PaymentRetrySignal`, and `v2.tax.IntegrationConfiguration`
* Add support for `create` method on resource `radar.BillingEvaluation`
* Add support for `create`, `deactivate`, `list`, `modify`, and `retrieve` methods on resource `billing.FeedbackOption`
* Add support for `modify` and `retrieve` methods on resource `v2.tax.IntegrationConfiguration`
* Add support for `retrieve` method on resource `v2.signals.PaymentRetrySignal`
* Add support for `cancel`, `create`, `modify`, and `retrieve` methods on resource `v2.signals.PaymentRetryEvaluation`
* Add support for `disable` method on resource `v2.money_management.PayoutMethod`
* Add support for `modify` method on resource `v2.core.ApprovalRequest`
* ⚠️ Remove support for `execute` and `submit` methods on resource `v2.core.ApprovalRequest`
* Add support for `disable_stripe_user_authentication` on `AccountSessionCreateParamsComponentPaymentMethodSettingFeature`
* Add support for `capital_financing_manual_payment` on `AccountSession.Component`
* Add support for `sequra_payments` on `Account.Capability`
* Add support for `feedback_options` on `billing_portal.ConfigurationCreateParamsFeatureSubscriptionCancelCancellationReason` and `billing_portal.ConfigurationModifyParamsFeatureSubscriptionCancelCancellationReason`
* Add support for new value `fundbox_ca_financing` on enum `Capital.FinancingSummary.Detail.disclaimer_variant`
* Add support for `sequra` on `Charge.PaymentMethodDetail`, `Checkout.Session.PaymentMethodOption`, `ConfirmationToken.PaymentMethodPreview`, `PaymentAttemptRecord.PaymentMethodDetail`, `PaymentIntent.PaymentMethodOption`, and `PaymentRecord.PaymentMethodDetail`
* ⚠️ Remove support for value `data_share_only` from enums `Charge.PaymentMethodDetail.Card.ThreeDSecure.result`, `PaymentAttemptRecord.PaymentMethodDetail.Card.ThreeDSecure.result`, `PaymentRecord.PaymentMethodDetail.Card.ThreeDSecure.result`, and `SetupAttempt.PaymentMethodDetail.Card.ThreeDSecure.result`
* Add support for `funding_types_blocked` on `checkout.SessionCreateParamsPaymentMethodOptionCardRestriction`
* Add support for `payment_intent_data` on `checkout.SessionModifyParams`
* ⚠️ Change type of `Checkout.Session.PaymentMethodOption.Bancontact.setup_future_usage` from `literal('none')` to `enum('none'|'off_session')`
* Add support for new value `sequra` on enums `ConfirmationTokenCreateParamsPaymentMethodDatum.type`, `PaymentIntentConfirmParamsPaymentMethodDatum.type`, `PaymentIntentCreateParamsPaymentMethodDatum.type`, `PaymentIntentModifyParamsPaymentMethodDatum.type`, `SetupIntentConfirmParamsPaymentMethodDatum.type`, `SetupIntentCreateParamsPaymentMethodDatum.type`, and `SetupIntentModifyParamsPaymentMethodDatum.type`
* Add support for `metadata` on `ConfirmationToken`, `V2.Signals.AccountActivity`, and `v2.signals.AccountActivityCreateParams`
* Add support for new value `sequra` on enums `ConfirmationToken.PaymentMethodPreview.type` and `PaymentMethod.type`
* Add support for `active_entitlements` and `customer_portal` on `CustomerSessionCreateParamsComponent`
* Add support for new value `sequra` on enums `CustomerListPaymentMethodsParams.type`, `PaymentMethodCreateParams.type`, and `PaymentMethodListParams.type`
* Add support for `address_match_confidence` and `name_match_confidence` on `Identity.VerificationReport.Email` and `Identity.VerificationReport.Phone`
* Add support for `domain_country`, `email_exists_confidence`, `observed_domain_tenure_days`, `observed_email_tenure_days`, and `phone_match_confidence` on `Identity.VerificationReport.Email`
* Add support for new values `email_address_mismatch`, `email_name_mismatch`, `email_ownership_unverified`, `email_phone_mismatch`, and `email_short_tenure` on enum `Identity.VerificationReport.Email.Error.code`
* Add support for `carrier`, `line_type`, and `observed_phone_tenure_days` on `Identity.VerificationReport.Phone`
* Add support for new values `phone_address_mismatch`, `phone_invalid_line_type`, `phone_invalid`, `phone_name_mismatch`, `phone_ownership_unverified`, `phone_short_tenure`, and `phone_unsupported_country` on enum `Identity.VerificationReport.Phone.Error.code`
* Add support for new values `email_address_mismatch`, `email_name_mismatch`, `email_ownership_unverified`, `email_phone_mismatch`, `email_short_tenure`, `phone_address_mismatch`, `phone_invalid_line_type`, `phone_invalid`, `phone_name_mismatch`, `phone_ownership_unverified`, `phone_short_tenure`, and `phone_unsupported_country` on enum `Identity.VerificationSession.LastError.code`
* Add support for new value `truemoney` on enums `Invoice.PaymentSetting.payment_method_types`, `InvoiceCreateParamsPaymentSetting.payment_method_types`, `InvoiceModifyParamsPaymentSetting.payment_method_types`, `QuotePreviewInvoice.PaymentSetting.payment_method_types`, `Subscription.PaymentSetting.payment_method_types`, `SubscriptionCreateParamsPaymentSetting.payment_method_types`, and `SubscriptionModifyParamsPaymentSetting.payment_method_types`
* Add support for new value `merchant_canceled` on enums `PaymentAttemptRecordReportCanceledParams.reason` and `PaymentRecordReportPaymentAttemptCanceledParams.reason`
* ⚠️ Remove support for `payment_method_types` on `PaymentIntentConfirmParams`, `PaymentIntentCreateParams`, `PaymentIntentModifyParams`, `SetupIntentCreateParams`, and `SetupIntentModifyParams`
* Add support for new value `touch_n_go` on enums `PaymentIntent.allowed_payment_method_types`, `PaymentIntentConfirmParams.allowed_payment_method_types`, `PaymentIntentCreateParams.allowed_payment_method_types`, `PaymentIntentModifyParams.allowed_payment_method_types`, `SetupIntent.allowed_payment_method_types`, `SetupIntentConfirmParams.allowed_payment_method_types`, `SetupIntentCreateParams.allowed_payment_method_types`, and `SetupIntentModifyParams.allowed_payment_method_types`
* Add support for new value `sequra` on enums `PaymentIntent.excluded_payment_method_types`, `PaymentIntentConfirmParams.excluded_payment_method_types`, `PaymentIntentCreateParams.excluded_payment_method_types`, `PaymentIntentModifyParams.excluded_payment_method_types`, `SetupIntent.excluded_payment_method_types`, `SetupIntentCreateParams.excluded_payment_method_types`, and `SetupIntentModifyParams.excluded_payment_method_types`
* Add support for `verification_method` on `PaymentIntent.PaymentMethodOption.BacsDebit`, `PaymentIntentConfirmParamsPaymentMethodOptionBacsDebit`, `PaymentIntentCreateParamsPaymentMethodOptionBacsDebit`, `PaymentIntentModifyParamsPaymentMethodOptionBacsDebit`, `SetupIntent.PaymentMethodOption.BacsDebit`, `SetupIntentConfirmParamsPaymentMethodOptionBacsDebit`, `SetupIntentCreateParamsPaymentMethodOptionBacsDebit`, and `SetupIntentModifyParamsPaymentMethodOptionBacsDebit`
* Change `PaymentIntent.allowed_payment_method_types` and `SetupIntent.allowed_payment_method_types` to be required
* Add support for `application_fee_amount`, `application_fee_percent`, `on_behalf_of`, and `transfer_data` on `PaymentLinkModifyParams`
* Add support for `canceled` on `PaymentRecordReportPaymentAttemptParams` and `PaymentRecordReportPaymentParams`
* ⚠️ Change type of `ProductCatalog.TrialOffer.price` from `$Price` to `deletable($Price)`
* ⚠️ Change `ProductCatalog.TrialOffer.name` to be optional
* Add support for `recurring` on `SharedPayment.GrantedToken.UsageLimit`, `SharedPayment.IssuedToken.UsageLimit`, `shared_payment.GrantedTokenCreateParamsUsageLimit`, and `shared_payment.IssuedTokenCreateParamsUsageLimit`
* Add support for `feedback_option` on `SubscriptionCancelParamsCancellationDetail` and `SubscriptionModifyParamsCancellationDetail`
* Add support for `pricing_token` on `SubscriptionModifyParams`
* Add support for `igic` on `tax.RegistrationCreateParamsCountryOptionAt`, `tax.RegistrationCreateParamsCountryOptionBe`, `tax.RegistrationCreateParamsCountryOptionBg`, `tax.RegistrationCreateParamsCountryOptionCy`, `tax.RegistrationCreateParamsCountryOptionCz`, `tax.RegistrationCreateParamsCountryOptionDe`, `tax.RegistrationCreateParamsCountryOptionDk`, `tax.RegistrationCreateParamsCountryOptionE`, `tax.RegistrationCreateParamsCountryOptionEe`, `tax.RegistrationCreateParamsCountryOptionFi`, `tax.RegistrationCreateParamsCountryOptionFr`, `tax.RegistrationCreateParamsCountryOptionGr`, `tax.RegistrationCreateParamsCountryOptionHr`, `tax.RegistrationCreateParamsCountryOptionHu`, `tax.RegistrationCreateParamsCountryOptionIe`, `tax.RegistrationCreateParamsCountryOptionIt`, `tax.RegistrationCreateParamsCountryOptionLt`, `tax.RegistrationCreateParamsCountryOptionLu`, `tax.RegistrationCreateParamsCountryOptionLv`, `tax.RegistrationCreateParamsCountryOptionMt`, `tax.RegistrationCreateParamsCountryOptionNl`, `tax.RegistrationCreateParamsCountryOptionPl`, `tax.RegistrationCreateParamsCountryOptionPt`, `tax.RegistrationCreateParamsCountryOptionRo`, `tax.RegistrationCreateParamsCountryOptionSe`, `tax.RegistrationCreateParamsCountryOptionSi`, and `tax.RegistrationCreateParamsCountryOptionSk`
* Add support for new value `2026-08-26.dahlia` on enum `WebhookEndpointCreateParams.api_version`
* Add support for `one_time_fees` on `V2.Billing.Contract` and `v2.billing.ContractCreateParams`
* ⚠️ Remove support for `payment_method_collection` on `V2.Core.Account.Configuration.Merchant.GrossSettlement`, `v2.core.AccountCreateParamsConfigurationMerchantGrossSettlement`, and `v2.core.AccountModifyParamsConfigurationMerchantGrossSettlement`
* Add support for `payout_methods` on `V2.Core.Account.Default` and `v2.core.AccountModifyParamsDefault`
* Add support for `reason` on `V2.Core.ApprovalRequest`
* ⚠️ Remove support for `description` on `V2.Core.ApprovalRequest`
* Add support for `api_key`, `type`, and `user` on `V2.Core.ApprovalRequest.RequestedBy` and `V2.Core.ApprovalRequest.Review.ReviewedBy`
* ⚠️ Remove support for `id` and `name` on `V2.Core.ApprovalRequest.RequestedBy` and `V2.Core.ApprovalRequest.Review.ReviewedBy`
* Add support for `approved_at` on `V2.Core.ApprovalRequest.StatusTransition`
* ⚠️ Remove support for `requires_execution_at` on `V2.Core.ApprovalRequest.StatusTransition`
* Add support for `crypto_transaction` on `V2.Core.FeeBatch.CollectionRecord`
* Add support for new value `crypto_transaction` on enum `V2.Core.FeeBatch.CollectionRecord.type`
* Add support for `restricted` on `V2.Core.Vault.GbBankAccount` and `V2.Core.Vault.UsBankAccount`
* Add support for `savings` on `V2.MoneyManagement.FinancialAccount` and `v2.money_management.FinancialAccountCreateParams`
* ⚠️ Add support for new value `savings` on enum `V2.MoneyManagement.FinancialAccount.type`
* Add support for `enabled_delivery_schemes` on `V2.MoneyManagement.PayoutMethod.BankAccount`
* ⚠️ Remove support for `enabled_delivery_options` on `V2.MoneyManagement.PayoutMethod.BankAccount`
* ⚠️ Add support for new value `disabled` on enum `V2.MoneyManagement.PayoutMethod.UsageStatus.payments`
* ⚠️ Add support for new value `disabled` on enum `V2.MoneyManagement.PayoutMethod.UsageStatus.transfers`
* Add support for `to_account` on `V2.MoneyManagement.ReceivedDebit.BalanceTransfer`
* Add support for `account_restricted` and `account_suspended` on `V2.Signals.AccountActivity` and `v2.signals.AccountActivityCreateParams`
* Add support for new values `account_restricted` and `account_suspended` on enums `V2.Signals.AccountActivity.type`, `v2.signals.AccountActivityCreateParams.type`, and `v2.signals.AccountEvaluationCreateParamsAccountActivityDetailData.type`
* ⚠️ Remove support for value `not_assessed` from enums `V2.Signals.AccountEvaluation.EvaluatedSignal.FraudulentWebsite.risk_level`, `V2.Signals.AccountEvaluation.EvaluatedSignal.UserAccountSharing.risk_level`, `V2.Signals.AccountEvaluation.EvaluatedSignal.UserMultiAccounting.risk_level`, `V2.Signals.AccountSignal.FraudulentMerchant.risk_level`, `V2.Signals.AccountSignal.FraudulentWebsite.risk_level`, `V2.Signals.AccountSignal.MerchantDelinquency.risk_level`, `V2.Signals.AccountSignal.UserAccountSharing.risk_level`, and `V2.Signals.AccountSignal.UserMultiAccounting.risk_level`
* Add support for `additional_details` on `V2.Signals.AccountSignal.FraudulentMerchant` and `V2.Signals.AccountSignal.MerchantDelinquency`
* ⚠️ Remove support for `indicators` on `V2.Signals.AccountSignal.FraudulentMerchant` and `V2.Signals.AccountSignal.MerchantDelinquency`
* Add support for new value `disabled` on enum `v2.money_management.PayoutMethodListParamsUsageStatus.payments`
* Add support for new value `disabled` on enum `v2.money_management.PayoutMethodListParamsUsageStatus.transfers`
* Add support for new value `savings` on enum `v2.money_management.FinancialAccountListParams.types`
* Add support for new value `savings` on enum `v2.money_management.FinancialAccountCreateParams.type`
* Add support for `action`, `created`, and `status` on `v2.core.ApprovalRequestListParams`
* Add support for `one_time_fee_actions` on `v2.billing.ContractModifyParams`
* Add support for event notifications `V2CoreHealthMetronomeNotificationLatencyFiringEvent`, `V2CoreHealthMetronomeNotificationLatencyResolvedEvent`, and `V2SignalsPaymentRetryEvaluationsRetryRecommendedEvent`
* Add support for event notifications `V2MoneyManagementPayoutIntentCanceledEvent`, `V2MoneyManagementPayoutIntentCreatedEvent`, `V2MoneyManagementPayoutIntentPostedEvent`, `V2MoneyManagementPayoutIntentProcessingEvent`, and `V2MoneyManagementPayoutIntentRequiresActionEvent` with related object `v2.money_management.PayoutIntent`
* Add support for error codes `authentication_failure`, `capability_not_active`, `expired_payment_method`, `incorrect_postal_code`, `invalid_canceled_subscription_fields`, and `payment_method_restricted` on `Invoice.LastFinalizationError`, `PaymentIntent.LastPaymentError`, `QuotePreviewInvoice.LastFinalizationError`, `SetupAttempt.SetupError`, `SetupIntent.LastSetupError`, `StripeError`, and `Terminal.Reader.Action.ApiError`
* Add support for error code `contract_number_already_exists` on `AlreadyExistsError`
* Add support for error codes `default_payout_method_cannot_be_disabled`, `evaluation_not_monitoring`, `missing_payment_data_for_evaluation`, `one_time_fee_already_billed`, `payment_not_eligible`, and `webhook_endpoint_not_configured` on `CannotProceedError`
