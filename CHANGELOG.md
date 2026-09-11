<!--
THIS IS A GENERATED FILE. Any changes you make to it directly will be blown away.
Instead, edit a corresponding `.change.md` file and run `hark build`.
-->

# Changelog

> This changelog only covers the **private preview** releases. Each release builds on the most recent GA release; see those notes in [the GA changelog](https://github.com/stripe/stripe-python/blob/master/CHANGELOG.md).

## 15.7.0a3 - 2026-09-09
* [#1901](https://github.com/stripe/stripe-python/pull/1901) Update generated code for private-preview
  * Add support for `customer_tax_exemption` on `Tax.Calculation.ShippingCost.TaxBreakdown`, `Tax.CalculationLineItem.TaxBreakdown`, and `Tax.Transaction.ShippingCost.TaxBreakdown`
  * Add support for new value `data_share_only` on enums `Charge.PaymentMethodDetail.Card.ThreeDSecure.result`, `PaymentAttemptRecord.PaymentMethodDetail.Card.ThreeDSecure.result`, `PaymentRecord.PaymentMethodDetail.Card.ThreeDSecure.result`, and `SetupAttempt.PaymentMethodDetail.Card.ThreeDSecure.result`
  * Add support for `backdate_start_date` on `Checkout.Session.Item.Subscription` and `checkout.SessionCreateParamsItemSubscription`
  * Add support for `signals` on `Identity.VerificationReport`
  * Add support for `network_response_code` on `Issuing.Authorization.RequestHistory`
  * Add support for `unit_cost_precision` on `PaymentIntentAmountDetailsLineItem`, `PaymentIntentCaptureParamsAmountDetailLineItem`, `PaymentIntentConfirmParamsAmountDetailLineItem`, `PaymentIntentCreateParamsAmountDetailLineItem`, `PaymentIntentDecrementAuthorizationParamsAmountDetailLineItem`, `PaymentIntentIncrementAuthorizationParamsAmountDetailLineItem`, and `PaymentIntentModifyParamsAmountDetailLineItem`
  * Change `PaymentIntent.payment_record` to be required
  * Add support for `active` on `product_catalog.TrialOfferListParams`
  * Change `Subscription.TrialSetting.EndBehavior.billing_cycle_anchor` to be required
  * Add support for new value `rtp` on enum `Treasury.FinancialAccount.FinancialAddress.supported_networks`
  * Add support for new value `blik_recurring_payments` on enums `V2.Core.Account.FutureRequirement.Entry.Impact.RestrictsCapability.capability` and `V2.Core.Account.Requirement.Entry.Impact.RestrictsCapability.capability`

## 15.7.0a2 - 2026-09-02
* ⚠️ [#1893](https://github.com/stripe/stripe-python/pull/1893) Update generated code for private-preview
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

## 15.7.0a1 - 2026-08-26
This release changes the pinned API version to `2026-08-26.preview`.

* [#1880](https://github.com/stripe/stripe-python/pull/1880) Add non-verified manged handlers
* ⚠️ [#1884](https://github.com/stripe/stripe-python/pull/1884) Update generated code for private-preview
  * Add support for new resource `CustomerTaxExemption`
  * Add support for `create`, `delete`, `list`, and `retrieve` methods on resource `CustomerTaxExemption`
  * Add support for `details` on `Account.FutureRequirement.Error`, `Account.Requirement.Error`, `BankAccount.FutureRequirement.Error`, `BankAccount.Requirement.Error`, `Capability.FutureRequirement.Error`, `Capability.Requirement.Error`, `Person.FutureRequirement.Error`, and `Person.Requirement.Error`
  * ⚠️ Remove support for `sequra_payments` on `Account.Capability`
  * Add support for `subscription_pause` on `billing_portal.SessionCreateParamsFlowDatum`
  * ⚠️ Remove support for `sequra` on `Charge.PaymentMethodDetail`, `Checkout.Session.PaymentMethodOption`, `ConfirmationToken.PaymentMethodPreview`, `PaymentAttemptRecord.PaymentMethodDetail`, `PaymentIntent.PaymentMethodOption`, and `PaymentRecord.PaymentMethodDetail`
  * Add support for `enablement_details` on `Checkout.Session.AutomaticTax`
  * ⚠️ Remove support for value `sequra` from enums `ConfirmationTokenCreateParamsPaymentMethodDatum.type`, `PaymentIntentConfirmParamsPaymentMethodDatum.type`, `PaymentIntentCreateParamsPaymentMethodDatum.type`, `PaymentIntentModifyParamsPaymentMethodDatum.type`, `SetupIntentConfirmParamsPaymentMethodDatum.type`, `SetupIntentCreateParamsPaymentMethodDatum.type`, and `SetupIntentModifyParamsPaymentMethodDatum.type`
  * ⚠️ Remove support for value `sequra` from enums `ConfirmationToken.PaymentMethodPreview.type` and `PaymentMethod.type`
  * ⚠️ Remove support for value `sequra` from enums `CustomerListPaymentMethodsParams.type`, `PaymentMethodCreateParams.type`, and `PaymentMethodListParams.type`
  * Add support for `credit` on `FinancialConnections.Transaction.Classification`
  * Change type of `FinancialConnections.Transaction.Classification.money_movement` from `nullable(BankConnectionsResourceTransactionResourceClassificationsLabels)` to `BankConnectionsResourceTransactionResourceClassificationsLabels`
  * Change type of `FinancialConnections.Transaction.Classification.personal_finance` from `nullable(BankConnectionsResourceTransactionResourceClassificationsLabels)` to `BankConnectionsResourceTransactionResourceClassificationsLabels`
  * ⚠️ Change `FinancialConnections.Transaction.Classification.money_movement` to be optional
  * ⚠️ Change `FinancialConnections.Transaction.Classification.personal_finance` to be optional
  * Add support for `user_consent` on `identity.VerificationSessionCreateParams` and `identity.VerificationSessionModifyParams`
  * Add support for `company_details` on `Invoice.PaymentSetting.PaymentMethodOption.Billie`, `PaymentIntent.PaymentMethodOption.Billie`, `PaymentIntentConfirmParamsPaymentMethodOptionBillie`, `PaymentIntentCreateParamsPaymentMethodOptionBillie`, `PaymentIntentModifyParamsPaymentMethodOptionBillie`, `QuotePreviewInvoice.PaymentSetting.PaymentMethodOption.Billie`, and `Subscription.PaymentSetting.PaymentMethodOption.Billie`
  * Add support for `reference` on `Invoice.PaymentSetting.PaymentMethodOption.Billie`, `PaymentIntent.PaymentMethodOption.Billie`, `PaymentIntentConfirmParamsPaymentMethodOptionBillie`, `PaymentIntentCreateParamsPaymentMethodOptionBillie`, `PaymentIntentModifyParamsPaymentMethodOptionBillie`, and `QuotePreviewInvoice.PaymentSetting.PaymentMethodOption.Billie`
  * Add support for `pos_condition` on `Issuing.Authorization` and `issuing.AuthorizationCreateParams`
  * Add support for `crypto_wallet` on `Issuing.Card`, `issuing.CardCreateParams`, and `issuing.CardModifyParams`
  * Add support for `payment_evaluations` and `payment_method_details` on `PaymentAttemptRecordReportAuthorizedParams`
  * Add support for `aade_data` on `PaymentIntentConfirmParamsPaymentMethodOptionCardPresent`, `PaymentIntentCreateParamsPaymentMethodOptionCardPresent`, and `PaymentIntentModifyParamsPaymentMethodOptionCardPresent`
  * ⚠️ Remove support for `cancel_at_period_end` on `Subscription.PendingUpdate`
  * Add support for `blik_recurring_payments` on `V2.Core.Account.Configuration.Merchant.Capability`, `v2.core.AccountCreateParamsConfigurationMerchantCapability`, and `v2.core.AccountModifyParamsConfigurationMerchantCapability`
  * Add support for `user_access` on `V2.Iam.ActivityLog.Detail`
  * Add support for new value `user_access` on enum `V2.Iam.ActivityLog.Detail.type`
  * Add support for new value `user_access_started` on enum `V2.Iam.ActivityLog.type`
  * Add support for new value `user_access` on enum `v2.iam.ActivityLogListParams.action_groups`
  * Add support for new value `user_access_started` on enum `v2.iam.ActivityLogListParams.actions`
  * Add support for new value `blik_recurring_payments` on enum `EventsV2CoreAccountIncludingConfigurationMerchantCapabilityStatusUpdatedEvent.updated_capability`

## 15.6.0a2 - 2026-08-19
* ⚠️ [#1875](https://github.com/stripe/stripe-python/pull/1875) Update generated code for private-preview
  * Add support for new resources `PaymentPlan` and `billing.FeedbackOption`
  * ⚠️ Remove support for resource `billing.FeedbackOptions`
  * Add support for `create`, `list`, `modify`, and `retrieve` methods on resource `PaymentPlan`
  * Add support for `modify` method on resource `v2.money_management.Transaction`
  * Add support for `wechat_pay_payments` on `Account.Setting`, `AccountCreateParamsSetting`, and `AccountModifyParamsSetting`
  * ⚠️ Change type of `BillingPortal.Configuration.Feature.SubscriptionCancel.CancellationReason.feedback_options` from `$Billing.FeedbackOptions` to `$Billing.FeedbackOption`
  * Change `BillingPortal.Configuration.Feature.SubscriptionCancel.CancellationReason.feedback_options` to be required
  * Add support for `subscription_pause` on `BillingPortal.Session.Flow`
  * Add support for new value `subscription_pause` on enum `BillingPortal.Session.Flow.type`
  * Add support for new value `usdt` on enums `Crypto.OnrampSession.TransactionDetail.destination_currency`, `crypto.OnrampSessionCreateParams.destination_currency`, and `crypto.OnrampSessionListParams.destination_currency`
  * Add support for new value `usdt` on enums `Crypto.OnrampSession.TransactionDetail.destination_currencies` and `crypto.OnrampSessionCreateParams.destination_currencies`
  * Add support for `active_entitlements` on `CustomerSession.Component`
  * Add support for `shared_payment_issued_token` on `delegated_checkout.RequestedSessionConfirmParams`
  * Add support for new values `payment_plan.created`, `payment_plan.installment_due`, `payment_plan.installment_paid`, `payment_plan.installment_will_be_due`, and `payment_plan.updated` on enum `Event.type`
  * Add support for `managed_payments` on `InvoiceCreateParams`, `InvoiceItemCreateParams`, `InvoiceItem`, `Invoice`, and `QuotePreviewInvoice`
  * Add support for `payment_plan` on `Invoice`
  * Add support for `estimated_fee_details` and `estimated_fee` on `Issuing.Authorization.PendingRequest.HoldAmountDetail` and `Issuing.Authorization.RequestHistory.HoldAmountDetail`
  * ⚠️ Remove support for `cryptogram` on `PaymentAttemptRecord.PaymentMethodDetail.Card.ThreeDSecure` and `PaymentRecord.PaymentMethodDetail.Card.ThreeDSecure`
  * ⚠️ Change type of `ProductCatalog.TrialOffer.EndBehavior.Transition.price` from `$Price` to `deletable($Price)`
  * ⚠️ Change type of `Subscription.CancellationDetail.feedback_option` from `$Billing.FeedbackOptions` to `$Billing.FeedbackOption`
  * Add support for `cancel_at_period_end` on `Subscription.PendingUpdate`
  * Change `Subscription.CancellationDetail.feedback_option` to be required
  * Add support for `igic` on `Tax.Registration.CountryOption.At`, `Tax.Registration.CountryOption.Be`, `Tax.Registration.CountryOption.Bg`, `Tax.Registration.CountryOption.Cy`, `Tax.Registration.CountryOption.Cz`, `Tax.Registration.CountryOption.De`, `Tax.Registration.CountryOption.Dk`, `Tax.Registration.CountryOption.E`, `Tax.Registration.CountryOption.Ee`, `Tax.Registration.CountryOption.Fi`, `Tax.Registration.CountryOption.Fr`, `Tax.Registration.CountryOption.Gr`, `Tax.Registration.CountryOption.Hr`, `Tax.Registration.CountryOption.Hu`, `Tax.Registration.CountryOption.Ie`, `Tax.Registration.CountryOption.It`, `Tax.Registration.CountryOption.Lt`, `Tax.Registration.CountryOption.Lu`, `Tax.Registration.CountryOption.Lv`, `Tax.Registration.CountryOption.Mt`, `Tax.Registration.CountryOption.Nl`, `Tax.Registration.CountryOption.Pl`, `Tax.Registration.CountryOption.Pt`, `Tax.Registration.CountryOption.Ro`, `Tax.Registration.CountryOption.Se`, `Tax.Registration.CountryOption.Si`, and `Tax.Registration.CountryOption.Sk`
  * Add support for `metadata` on `V2.Billing.Contract.PricingLine.Datum.Pricing.PriceDetail.PricingOverride.Datum`, `V2.Billing.Contract.PricingOverride.Datum`, `V2.MoneyManagement.Transaction`, `v2.billing.ContractCreateParamsPricingOverride`, `v2.billing.ContractModifyParamsPricingLineActionUpdate`, `v2.billing.ContractModifyParamsPricingOverrideActionAdd`, `v2.billing.ContractModifyParamsPricingOverrideActionUpdate`, and `v2.billing.ContractModifyParams`
  * Add support for `tax_amount` on `V2.MoneyManagement.OutboundPaymentQuote.EstimatedFee`
  * Add support for `payout_method_options` on `V2.MoneyManagement.OutboundPaymentQuote.To` and `v2.money_management.OutboundPaymentQuoteCreateParamsTo`
  * Change type of `v2.billing.ContractModifyParamsPricingLineActionUpdatePricingPriceDetailPricingOverrideActionUpdate.metadata` from `string` to `emptyable(string)`
  * Add support for snapshot events `payment_plan.created`, `payment_plan.installment_due`, `payment_plan.installment_paid`, `payment_plan.installment_will_be_due`, and `payment_plan.updated` with resource `PaymentPlan`

## 15.6.0a1 - 2026-08-12
This release changes the pinned API version to `2026-08-12.preview`.

* ⚠️ [#1873](https://github.com/stripe/stripe-python/pull/1873) Update generated code for private-preview
  * Add support for new resource `v2.tax.OperationsResolveAddressResult`
  * Add support for `resolve_address` method on resource `v2.tax.OperationsResolveAddressResult`
  * Add support for `confirm` and `fx_quote` methods on resource `v2.money_management.PayoutIntent`
  * ⚠️ Add support for new value `partner_disabled` on enums `Account.FutureRequirement.Error.code`, `Account.Requirement.Error.code`, `BankAccount.FutureRequirement.Error.code`, `BankAccount.Requirement.Error.code`, `Capability.FutureRequirement.Error.code`, `Capability.Requirement.Error.code`, `Person.FutureRequirement.Error.code`, and `Person.Requirement.Error.code`
  * ⚠️ Remove support for values `partner_disabled_dispute_rate`, `partner_disabled_responsibilities`, `partner_disabled_restricted_business`, and `partner_disabled_suspected_fraud` from enums `Account.FutureRequirement.Error.code`, `Account.Requirement.Error.code`, `BankAccount.FutureRequirement.Error.code`, `BankAccount.Requirement.Error.code`, `Capability.FutureRequirement.Error.code`, `Capability.Requirement.Error.code`, `Person.FutureRequirement.Error.code`, and `Person.Requirement.Error.code`
  * Add support for `customer_update` on `BillingPortal.Session.Flow`
  * Add support for new value `customer_update` on enum `BillingPortal.Session.Flow.type`
  * Add support for `funding_source_group` on `Charge.PaymentMethodDetail.Link`
  * ⚠️ Remove support for `pricing_group` on `Charge.PaymentMethodDetail.Link`
  * Add support for new value `celo` on enum `Crypto.CustomerConsumerWallet.network`
  * Add support for new value `celo` on enums `Crypto.OnrampSession.TransactionDetail.destination_network`, `crypto.OnrampSessionCreateParams.destination_network`, `crypto.OnrampSessionListParams.destination_network`, and `crypto.OnrampTransactionLimitsRetrieveParams.destination_network`
  * Add support for new value `celo` on enums `Crypto.OnrampSession.TransactionDetail.destination_networks` and `crypto.OnrampSessionCreateParams.destination_networks`
  * Add support for `celo` on `Crypto.OnrampSession.TransactionDetail.WalletAddress`
  * Add support for `customer_portal` on `CustomerSession.Component`
  * Add support for `applied_to_invoice` and `type` on `CustomerCreateCustomerBalanceTransactionParams`
  * Add support for `classification_state` and `enrichment_state` on `FinancialConnections.Account`
  * Add support for `country` on `FinancialConnections.Session.Filter`
  * Add support for `classifications` and `enrichments` on `FinancialConnections.Transaction`
  * Add support for new values `billie`, `paypay`, and `vipps` on enums `Invoice.PaymentSetting.payment_method_types`, `InvoiceCreateParamsPaymentSetting.payment_method_types`, `InvoiceModifyParamsPaymentSetting.payment_method_types`, `QuotePreviewInvoice.PaymentSetting.payment_method_types`, `Subscription.PaymentSetting.payment_method_types`, `SubscriptionCreateParamsPaymentSetting.payment_method_types`, and `SubscriptionModifyParamsPaymentSetting.payment_method_types`
  * Add support for `customer_balance` on `Invoice` and `QuotePreviewInvoice`
  * Add support for `billie` on `Invoice.PaymentSetting.PaymentMethodOption`, `QuotePreviewInvoice.PaymentSetting.PaymentMethodOption`, and `Subscription.PaymentSetting.PaymentMethodOption`
  * Add support for `hold_amount_details` and `hold_amount` on `Issuing.Authorization.PendingRequest` and `Issuing.Authorization.RequestHistory`
  * Add support for new values `hu` and `ro` on enums `Issuing.Cardholder.preferred_locales`, `issuing.CardholderCreateParams.preferred_locales`, and `issuing.CardholderModifyParams.preferred_locales`
  * Add support for new values `authentication_failure`, `expired_payment_method`, `incorrect_cvc`, `incorrect_number`, `incorrect_postal_code`, `insufficient_funds`, `payment_method_restricted`, and `processing_error` on enums `PaymentAttemptRecordReportFailedParams.failure_code`, `PaymentRecordReportPaymentAttemptFailedParams.failure_code`, `PaymentRecordReportPaymentAttemptParamsFailed.failure_code`, and `PaymentRecordReportPaymentParamsFailed.failure_code`
  * Add support for `network_decline_code` on `PaymentAttemptRecordReportFailedParamsPaymentMethodDetailCard` and `PaymentRecordReportPaymentAttemptFailedParamsPaymentMethodDetailCard`
  * Add support for `setup_future_usage` on `PaymentIntent.PaymentMethodOption.Sequra`
  * Add support for `status` on `QuotePreviewSubscriptionSchedule.PauseSchedule.Pause`, `QuotePreviewSubscriptionSchedule.PauseSchedule.Resume`, `SubscriptionSchedule.PauseSchedule.Pause`, and `SubscriptionSchedule.PauseSchedule.Resume`
  * Change `SubscriptionScheduleCreateParamsPauseSchedule.pause` to be optional
  * Change type of `SubscriptionScheduleModifyParamsPauseSchedule.resume` from `pause_schedule_update_resume_params` to `emptyable(pause_schedule_update_resume_params)`
  * Add support for `acquirer` on `EventsV2CoreHealthAuthorizationRateDropFiringEvent.Impact.Dimension`, `EventsV2CoreHealthAuthorizationRateDropResolvedEvent.Impact.Dimension`, `V2.Core.Health.Alert.AuthorizationRateDrop.Dimension`, and `V2.Core.Health.AlertHistoryEntry.AuthorizationRateDrop.Dimension`
  * ⚠️ Change type of `EventsV2CoreHealthAuthorizationRateDropFiringEvent.Impact.Dimension.type`, `EventsV2CoreHealthAuthorizationRateDropResolvedEvent.Impact.Dimension.type`, `V2.Core.Health.Alert.AuthorizationRateDrop.Dimension.type`, and `V2.Core.Health.AlertHistoryEntry.AuthorizationRateDrop.Dimension.type` from `literal('issuer')` to `enum('acquirer'|'issuer')`
  * Add support for `confirmation_method` on `V2.MoneyManagement.PayoutIntent` and `v2.money_management.PayoutIntentCreateParams`
  * Add support for `estimated_fees` and `fx_quote` on `V2.MoneyManagement.PayoutIntent`
  * Add support for `debited` on `V2.MoneyManagement.PayoutIntent.From`
  * Add support for `confirm` on `V2.MoneyManagement.PayoutIntent.NextAction`
  * ⚠️ Change type of `V2.MoneyManagement.PayoutIntent.NextAction.type` from `literal('handle_failure')` to `enum('confirm'|'handle_failure')`
  * Add support for `credited` on `V2.MoneyManagement.PayoutIntent.To`
  * Add support for new value `one_time_fees` on enums `v2.billing.ContractActivateParams.include`, `v2.billing.ContractCancelParams.include`, `v2.billing.ContractCreateParams.include`, `v2.billing.ContractListParams.include`, `v2.billing.ContractModifyParams.include`, and `v2.billing.ContractRetrieveParams.include`
  * Add support for event notification `V1BalanceSettingsUpdatedEvent` with related object `BalanceSettings`
  * Add support for event notification `V1BillingCreditBalanceTransactionCreatedEvent` with related object `billing.CreditBalanceTransaction`
  * Add support for event notifications `V1BillingCreditGrantCreatedEvent` and `V1BillingCreditGrantUpdatedEvent` with related object `billing.CreditGrant`
  * Add support for event notifications `V1BillingMeterCreatedEvent`, `V1BillingMeterDeactivatedEvent`, `V1BillingMeterReactivatedEvent`, and `V1BillingMeterUpdatedEvent` with related object `billing.Meter`
  * Add support for event notifications `V1FinancialConnectionsAccountAccountNumbersUpdatedEvent`, `V1FinancialConnectionsAccountExpectedDeactivationDateUpdatedEvent`, `V1FinancialConnectionsAccountSupportedPaymentMethodTypesUpdatedEvent`, `V1FinancialConnectionsAccountUpcomingAccountNumberExpiryEvent`, and `V1FinancialConnectionsAccountUpcomingDeactivationEvent` with related object `financial_connections.Account`
  * Add support for event notification `V1InvoicePaymentAttemptRequiredEvent` with related object `Invoice`
  * Add support for error type `FxQuoteNeedsRefreshError`

## 15.5.0a2 - 2026-08-05
* ⚠️ [#1859](https://github.com/stripe/stripe-python/pull/1859) Update generated code for private-preview
  * Add support for new resource `billing.FeedbackOptions`
  * Add support for `sequra_payments` on `Account.Capability`
  * Add support for `feedback_options` on `BillingPortal.Configuration.Feature.SubscriptionCancel.CancellationReason`
  * Add support for `sequra` on `Charge.PaymentMethodDetail`, `Checkout.Session.PaymentMethodOption`, `ConfirmationToken.PaymentMethodPreview`, `PaymentAttemptRecord.PaymentMethodDetail`, `PaymentIntent.PaymentMethodOption`, and `PaymentRecord.PaymentMethodDetail`
  * Add support for `retrieval_reference_number` on `Charge.PaymentMethodDetail.CardPresent`, `ConfirmationToken.PaymentMethodPreview.Card.GeneratedFrom.PaymentMethodDetail.CardPresent`, `PaymentAttemptRecord.PaymentMethodDetail.CardPresent`, `PaymentMethod.Card.GeneratedFrom.PaymentMethodDetail.CardPresent`, and `PaymentRecord.PaymentMethodDetail.CardPresent`
  * Add support for `pricing_group` on `Charge.PaymentMethodDetail.Link`
  * Add support for `tax_rates` on `Checkout.Session.ShippingOption`, `checkout.SessionCreateParamsShippingOption`, and `checkout.SessionModifyParamsShippingOption`
  * ⚠️ Add support for new value `daikin` on enums `Checkout.Session.AutomaticSurcharge.provider` and `PaymentLink.AutomaticSurcharge.provider`
  * Add support for `funding_types_blocked` on `Checkout.Session.PaymentMethodOption.Card.Restriction`
  * Add support for new value `sequra` on enums `ConfirmationTokenCreateParamsPaymentMethodDatum.type`, `PaymentIntentConfirmParamsPaymentMethodDatum.type`, `PaymentIntentCreateParamsPaymentMethodDatum.type`, `PaymentIntentModifyParamsPaymentMethodDatum.type`, `SetupIntentConfirmParamsPaymentMethodDatum.type`, `SetupIntentCreateParamsPaymentMethodDatum.type`, and `SetupIntentModifyParamsPaymentMethodDatum.type`
  * Add support for new value `sequra` on enums `ConfirmationToken.PaymentMethodPreview.type` and `PaymentMethod.type`
  * Add support for new value `sequra` on enums `CustomerListPaymentMethodsParams.type`, `PaymentMethodCreateParams.type`, and `PaymentMethodListParams.type`
  * Add support for `healthcare` on `issuing.AuthorizationCaptureParamsPurchaseDetail`, `issuing.AuthorizationCreateParams`, `issuing.TransactionCreateForceCaptureParamsPurchaseDetail`, and `issuing.TransactionCreateUnlinkedRefundParamsPurchaseDetail`
  * Change type of `Issuing.Authorization.Healthcare.verification_status` from `nullable(enum('iias_merchant_exempt'|'iias_merchant_not_certified'|'iias_verified'|'not_verified'))` to `enum('iias_merchant_exempt'|'iias_merchant_not_certified'|'iias_verified'|'not_verified')`
  * Add support for `is_anomalous` on `PaymentAttemptRecordReportGuaranteedParams`
  * Add support for new value `sequra` on enums `PaymentIntent.excluded_payment_method_types`, `PaymentIntentConfirmParams.excluded_payment_method_types`, `PaymentIntentCreateParams.excluded_payment_method_types`, `PaymentIntentModifyParams.excluded_payment_method_types`, `SetupIntent.excluded_payment_method_types`, `SetupIntentCreateParams.excluded_payment_method_types`, and `SetupIntentModifyParams.excluded_payment_method_types`
  * Add support for `aade_data` on `PaymentIntent.PaymentMethodOption.CardPresent`
  * Change `Radar.PaymentEvaluation.PaymentDetail.PaymentMethodDetail.Card.first6` to be required
  * Change `Radar.PaymentEvaluation.PaymentDetail.PaymentMethodDetail.Card.last4` to be required
  * Add support for `feedback_option` on `Subscription.CancellationDetail`
  * Add support for `application` on `V2.Payments.OffSessionPayment`
  * Add support for `status` on `v2.money_management.FinancialAccountStatementListParams`
  * Change `v2.billing.ContractCreateParams.pricing_lines` to be optional

## 15.5.0a1 - 2026-07-29
This release changes the pinned API version to `2026-07-29.preview`.

* ⚠️ [#1854](https://github.com/stripe/stripe-python/pull/1854) Update generated code for private-preview
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

## 15.4.0a5 - 2026-07-22
* ⚠️ [#1852](https://github.com/stripe/stripe-python/pull/1852) Update generated code for private-preview
  * Add support for new resources `billing.AlertNotification` and `crypto.DepositAddress`
  * Add support for `create`, `list`, and `retrieve` methods on resource `crypto.DepositAddress`
  * Add support for `list` method on resource `billing.AlertNotification`
  * ⚠️ Add support for new values `partner_disabled_dispute_rate`, `partner_disabled_responsibilities`, `partner_disabled_restricted_business`, and `partner_disabled_suspected_fraud` on enums `Account.FutureRequirement.Error.code`, `Account.Requirement.Error.code`, `BankAccount.FutureRequirement.Error.code`, `BankAccount.Requirement.Error.code`, `Capability.FutureRequirement.Error.code`, `Capability.Requirement.Error.code`, `Person.FutureRequirement.Error.code`, and `Person.Requirement.Error.code`
  * Add support for new value `data_share_only` on enums `Charge.PaymentMethodDetail.Card.ThreeDSecure.result`, `PaymentAttemptRecord.PaymentMethodDetail.Card.ThreeDSecure.result`, `PaymentRecord.PaymentMethodDetail.Card.ThreeDSecure.result`, and `SetupAttempt.PaymentMethodDetail.Card.ThreeDSecure.result`
  * Add support for `vipps` on `ConfirmationToken.PaymentMethodPreview`, `ConfirmationTokenCreateParamsPaymentMethodDatum`, `PaymentIntent.PaymentMethodOption`, `PaymentIntentConfirmParamsPaymentMethodDatum`, `PaymentIntentConfirmParamsPaymentMethodOption`, `PaymentIntentCreateParamsPaymentMethodDatum`, `PaymentIntentCreateParamsPaymentMethodOption`, `PaymentIntentModifyParamsPaymentMethodDatum`, `PaymentIntentModifyParamsPaymentMethodOption`, `PaymentMethodConfigurationCreateParams`, `PaymentMethodConfigurationModifyParams`, `PaymentMethodConfiguration`, `PaymentMethodCreateParams`, `PaymentMethod`, `SetupIntentConfirmParamsPaymentMethodDatum`, `SetupIntentCreateParamsPaymentMethodDatum`, and `SetupIntentModifyParamsPaymentMethodDatum`
  * Add support for new value `vipps` on enums `ConfirmationTokenCreateParamsPaymentMethodDatum.type`, `PaymentIntentConfirmParamsPaymentMethodDatum.type`, `PaymentIntentCreateParamsPaymentMethodDatum.type`, `PaymentIntentModifyParamsPaymentMethodDatum.type`, `SetupIntentConfirmParamsPaymentMethodDatum.type`, `SetupIntentCreateParamsPaymentMethodDatum.type`, and `SetupIntentModifyParamsPaymentMethodDatum.type`
  * Add support for new value `vipps` on enums `ConfirmationToken.PaymentMethodPreview.type` and `PaymentMethod.type`
  * Add support for new value `sui` on enum `Crypto.CustomerConsumerWallet.network`
  * Add support for new value `sui` on enums `Crypto.OnrampSession.TransactionDetail.destination_network`, `crypto.OnrampSessionCreateParams.destination_network`, `crypto.OnrampSessionListParams.destination_network`, and `crypto.OnrampTransactionLimitsRetrieveParams.destination_network`
  * Add support for new value `sui` on enums `Crypto.OnrampSession.TransactionDetail.destination_networks` and `crypto.OnrampSessionCreateParams.destination_networks`
  * Add support for `sui` on `Crypto.OnrampSession.TransactionDetail.WalletAddress`
  * Add support for new value `vipps` on enums `CustomerListPaymentMethodsParams.type`, `PaymentMethodCreateParams.type`, and `PaymentMethodListParams.type`
  * Add support for `use_stripe_sdk` on `delegated_checkout.RequestedSessionConfirmParams`
  * Add support for new value `mb_way` on enums `Invoice.PaymentSetting.payment_method_types`, `InvoiceCreateParamsPaymentSetting.payment_method_types`, `InvoiceModifyParamsPaymentSetting.payment_method_types`, `QuotePreviewInvoice.PaymentSetting.payment_method_types`, `Subscription.PaymentSetting.payment_method_types`, `SubscriptionCreateParamsPaymentSetting.payment_method_types`, and `SubscriptionModifyParamsPaymentSetting.payment_method_types`
  * Add support for `ev_charging` on `PaymentIntentAmountDetailsLineItem.PaymentMethodOption.Card`, `PaymentIntentCaptureParamsAmountDetailLineItemPaymentMethodOptionCard`, `PaymentIntentConfirmParamsAmountDetailLineItemPaymentMethodOptionCard`, `PaymentIntentCreateParamsAmountDetailLineItemPaymentMethodOptionCard`, `PaymentIntentDecrementAuthorizationParamsAmountDetailLineItemPaymentMethodOptionCard`, `PaymentIntentIncrementAuthorizationParamsAmountDetailLineItemPaymentMethodOptionCard`, and `PaymentIntentModifyParamsAmountDetailLineItemPaymentMethodOptionCard`
  * Add support for new values `ev_battery_exchanges`, `ev_charging_fee`, `evc_level_1`, `evc_level_2`, `evc_level_3`, `evc_level_4`, and `evc_level_5` on enums `PaymentIntentCaptureParamsAmountDetailLineItemPaymentMethodOptionCardFleetDatum.product_type`, `PaymentIntentConfirmParamsAmountDetailLineItemPaymentMethodOptionCardFleetDatum.product_type`, `PaymentIntentCreateParamsAmountDetailLineItemPaymentMethodOptionCardFleetDatum.product_type`, `PaymentIntentDecrementAuthorizationParamsAmountDetailLineItemPaymentMethodOptionCardFleetDatum.product_type`, `PaymentIntentIncrementAuthorizationParamsAmountDetailLineItemPaymentMethodOptionCardFleetDatum.product_type`, and `PaymentIntentModifyParamsAmountDetailLineItemPaymentMethodOptionCardFleetDatum.product_type`
  * Add support for new value `vipps` on enums `PaymentIntent.excluded_payment_method_types`, `PaymentIntentConfirmParams.excluded_payment_method_types`, `PaymentIntentCreateParams.excluded_payment_method_types`, `PaymentIntentModifyParams.excluded_payment_method_types`, `SetupIntent.excluded_payment_method_types`, `SetupIntentCreateParams.excluded_payment_method_types`, and `SetupIntentModifyParams.excluded_payment_method_types`
  * ⚠️ Change type of `PaymentIntent.allowed_payment_method_types` from `string` to `enum`
  * Add support for `tax_items` on `PaymentIntent.PaymentDetail.CarRentalDatum.Total.Tax`, `PaymentIntent.PaymentDetail.FlightDatum.Total.Tax`, and `PaymentIntent.PaymentDetail.LodgingDatum.Total.Tax`
  * ⚠️ Remove support for `taxes` on `PaymentIntent.PaymentDetail.CarRentalDatum.Total.Tax`, `PaymentIntent.PaymentDetail.FlightDatum.Total.Tax`, and `PaymentIntent.PaymentDetail.LodgingDatum.Total.Tax`
  * Change `PaymentRecordCreateParams.closed` to be optional
  * Change `PaymentRecordCreateParams.funded` to be optional
  * Add support for `card` on `radar.PaymentEvaluationCreateParamsPaymentDetailPaymentMethodDetail`
  * ⚠️ Remove support for `acss_debit`, `afterpay_clearpay`, `alipay`, `alma`, `amazon_pay`, `au_becs_debit`, `bacs_debit`, `bancontact`, `billie`, `bizum`, `blik`, `boleto`, `card_present`, `cashapp`, `crypto`, `customer_balance`, `eps`, `fpx`, `gift_card`, `giropay`, `gopay`, `grabpay`, `id_bank_transfer`, `ideal`, `interac_present`, `kakao_pay`, `konbini`, `kr_card`, `mb_way`, `mobilepay`, `multibanco`, `naver_pay`, `nz_bank_account`, `oxxo`, `p24`, `pay_by_bank`, `payco`, `paynow`, `paypal`, `paypay`, `payto`, `pix`, `promptpay`, `qris`, `rechnung`, `revolut_pay`, `samsung_pay`, `satispay`, `scalapay`, `sepa_debit`, `shopeepay`, `sofort`, `stripe_balance`, `sunbit`, `swish`, `tamara`, `twint`, `upi`, `us_bank_account`, `wechat_pay`, and `zip` on `SharedPayment.GrantedToken.PaymentMethodDetail`
  * ⚠️ Add support for new value `shop_pay` on enum `SharedPayment.GrantedToken.PaymentMethodDetail.type`
  * ⚠️ Remove support for values `acss_debit`, `afterpay_clearpay`, `alipay`, `alma`, `amazon_pay`, `au_becs_debit`, `bacs_debit`, `bancontact`, `billie`, `bizum`, `blik`, `boleto`, `card_present`, `cashapp`, `crypto`, `custom`, `customer_balance`, `eps`, `fpx`, `gift_card`, `giropay`, `gopay`, `grabpay`, `id_bank_transfer`, `ideal`, `interac_present`, `kakao_pay`, `konbini`, `kr_card`, `mb_way`, `mobilepay`, `multibanco`, `naver_pay`, `nz_bank_account`, `oxxo`, `p24`, `pay_by_bank`, `payco`, `paynow`, `paypal`, `paypay`, `payto`, `pix`, `promptpay`, `qris`, `rechnung`, `revolut_pay`, `samsung_pay`, `satispay`, `scalapay`, `sepa_debit`, `shopeepay`, `sofort`, `stripe_balance`, `sunbit`, `swish`, `tamara`, `twint`, `upi`, `us_bank_account`, `wechat_pay`, and `zip` from enum `SharedPayment.GrantedToken.PaymentMethodDetail.type`
  * Add support for `spend_card` on `V2.Core.Account.Configuration.CardCreator.Capability.Commercial.Stripe`, `v2.core.AccountCreateParamsConfigurationCardCreatorCapabilityCommercialStripe`, and `v2.core.AccountModifyParamsConfigurationCardCreatorCapabilityCommercialStripe`
  * Add support for new value `commercial.stripe.spend_card` on enums `V2.Core.Account.FutureRequirement.Entry.Impact.RestrictsCapability.capability` and `V2.Core.Account.Requirement.Entry.Impact.RestrictsCapability.capability`
  * Add support for new value `payment_delinquency_exposure` on enums `V2.Signals.AccountSignal.type` and `v2.signals.AccountSignalListParams.type`
  * Add support for new value `commercial.stripe.spend_card` on enum `EventsV2CoreAccountIncludingConfigurationCardCreatorCapabilityStatusUpdatedEvent.updated_capability`

## 15.4.0a4 - 2026-07-16
* ⚠️ [#1844](https://github.com/stripe/stripe-python/pull/1844) Update generated code for private-preview
  * ⚠️ Remove support for resource `FrMealVouchersOnboarding`
  * ⚠️ Remove support for `create`, `list`, `modify`, and `retrieve` methods on resource `FrMealVouchersOnboarding`
  * Add support for `create` method on resource `PaymentRecord`
  * Add support for new value `chaps` on enums `FundingInstructions.BankTransfer.FinancialAddress.supported_networks` and `PaymentIntent.NextAction.DisplayBankTransferInstruction.FinancialAddress.supported_networks`
  * ⚠️ Remove support for `financial_accounts_transactions`, `financial_accounts`, and `recipients_list` on `AccountSessionCreateParamsComponent`
  * Add support for `smart_disputes_management` on `AccountSession.Component.DisputesList.Feature`, `AccountSession.Component.Payment.Feature`, `AccountSession.Component.PaymentDetail.Feature`, and `AccountSession.Component.PaymentDispute.Feature`
  * ⚠️ Add support for new value `ic_nif` on enums `Checkout.Session.CollectedInformation.TaxId.type`, `Checkout.Session.CustomerDetail.TaxId.type`, `Invoice.CustomerTaxId.type`, `Order.TaxDetail.TaxId.type`, `QuotePreviewInvoice.CustomerTaxId.type`, `Tax.Calculation.CustomerDetail.TaxId.type`, and `Tax.Transaction.CustomerDetail.TaxId.type`
  * Add support for new values `financial_connections.account.expected_deactivation_date_updated`, `financial_connections.account.supported_payment_method_types_updated`, `financial_connections.account.upcoming_deactivation`, `financial_connections.authorization.expected_deactivation_date_updated`, and `financial_connections.authorization.upcoming_deactivation` on enum `Event.type`
  * Add support for `mode` on `FinancialConnections.Session.ManualEntry`
  * Add support for new values `alipay` and `sequra` on enums `Invoice.PaymentSetting.payment_method_types`, `InvoiceCreateParamsPaymentSetting.payment_method_types`, `InvoiceModifyParamsPaymentSetting.payment_method_types`, `QuotePreviewInvoice.PaymentSetting.payment_method_types`, `Subscription.PaymentSetting.payment_method_types`, `SubscriptionCreateParamsPaymentSetting.payment_method_types`, and `SubscriptionModifyParamsPaymentSetting.payment_method_types`
  * Add support for new value `stripe_internal_error` on enum `Issuing.Authorization.RequestHistory.reason`
  * Add support for `business_name` on `Issuing.Card.Shipping`
  * Add support for new value `correos` on enum `Issuing.Card.Shipping.carrier`
  * ⚠️ Change type of `Issuing.Transaction.NetworkDatum.trace_id` from `IssuingTransactionTraceId` to `nullable(IssuingTransactionTraceId)`
  * Add support for `pause_schedules` on `QuotePreviewSubscriptionSchedule`, `SubscriptionScheduleCreateParams`, `SubscriptionScheduleModifyParams`, and `SubscriptionSchedule`
  * Add support for `trial` on `QuotePreviewSubscriptionSchedule.Phase` and `SubscriptionSchedule.Phase`
  * Add support for `payment_record` on `RefundCreateParams`
  * Add support for `redirect_to_url` on `SharedPayment.IssuedToken.NextAction`
  * ⚠️ Change type of `SharedPayment.IssuedToken.NextAction.type` from `literal('use_stripe_sdk')` to `enum('redirect_to_url'|'use_stripe_sdk')`
  * Add support for new values `financial_connections.account.expected_deactivation_date_updated`, `financial_connections.account.supported_payment_method_types_updated`, `financial_connections.account.upcoming_deactivation`, `financial_connections.authorization.expected_deactivation_date_updated`, and `financial_connections.authorization.upcoming_deactivation` on enums `WebhookEndpointCreateParams.enabled_events` and `WebhookEndpointModifyParams.enabled_events`
  * Add support for snapshot events `financial_connections.account.expected_deactivation_date_updated`, `financial_connections.account.supported_payment_method_types_updated`, and `financial_connections.account.upcoming_deactivation` with resource `financial_connections.Account`
  * Add support for snapshot events `financial_connections.authorization.expected_deactivation_date_updated` and `financial_connections.authorization.upcoming_deactivation` with resource `financial_connections.Authorization`

## 15.4.0a3 - 2026-07-08
This release changes the pinned API version to `2026-07-08.preview`.

* ⚠️ [#1842](https://github.com/stripe/stripe-python/pull/1842) Update generated code for private-preview
  * Add support for `activate_gift_card`, `cashout_gift_card`, `check_gift_card_balance`, and `reload_gift_card` methods on resource `terminal.Reader`
  * Add support for `aggregation_period` on `Billing.AlertRecovered`
  * ⚠️ Add support for new values `mass_transit_parking_tax` and `parking_tax` on enums `Tax.Calculation.ShippingCost.TaxBreakdown.TaxRateDetail.tax_type`, `Tax.Calculation.TaxBreakdown.TaxRateDetail.tax_type`, `Tax.CalculationLineItem.TaxBreakdown.TaxRateDetail.tax_type`, and `Tax.Transaction.ShippingCost.TaxBreakdown.TaxRateDetail.tax_type`
  * Add support for `administrative_address` and `principal_place_of_business` on `Account.Company`
  * ⚠️ Add support for new values `bnp_paribas`, `citibank`, and `mbsb_bank` on enums `Charge.PaymentMethodDetail.Fpx.bank`, `ConfirmationToken.PaymentMethodPreview.Fpx.bank`, `PaymentAttemptRecord.PaymentMethodDetail.Fpx.bank`, `PaymentMethod.Fpx.bank`, `PaymentRecord.PaymentMethodDetail.Fpx.bank`, and `SharedPayment.GrantedToken.PaymentMethodDetail.Fpx.bank`
  * Add support for `address_collection_precision` on `Checkout.Session.AutomaticTax`
  * Add support for `tax_id` on `Checkout.Session.CollectedInformation`
  * ⚠️ Remove support for `tax_ids` on `Checkout.Session.CollectedInformation`
  * Add support for `setup_future_usage` on `Checkout.Session.PaymentMethodOption.Payco`, `Checkout.Session.PaymentMethodOption.SamsungPay`, `PaymentIntent.PaymentMethodOption.Payco`, `PaymentIntent.PaymentMethodOption.Paypay`, `PaymentIntent.PaymentMethodOption.SamsungPay`, `PaymentIntentConfirmParamsPaymentMethodOptionPaypay`, `PaymentIntentCreateParamsPaymentMethodOptionPaypay`, and `PaymentIntentModifyParamsPaymentMethodOptionPaypay`
  * Add support for `network` on `Dispute.PaymentMethodDetail.Card`
  * Add support for `require_payment_method_support` on `FinancialConnections.Session.Filter`
  * Add support for `network_data` on `Issuing.Authorization.RequestHistory`
  * Add support for `acquiring_institution_country`, `acquiring_institution_id`, `retrieval_reference_number`, `routed_network`, and `trace_id` on `Issuing.Transaction.NetworkDatum`
  * Add support for new values `boku_promptpay`, `capchase_pay`, `check_scan`, `click_to_pay`, `demo_pay`, `duitnow`, `dummy_auth_push`, `dummy_passthrough_card`, `edenred`, `gcash`, `getbalance`, `knet`, `kr_market`, `kriya`, `momo`, `mondu`, `netbanking`, `ng_bank_transfer`, `ng_bank`, `ng_card`, `ng_market`, `ng_ussd`, `ng_wallet`, `octopus`, `paper_check`, `sequra`, `shop_pay`, `south_korea_market`, `test_pay`, `truemoney`, `us_cash_voucher`, `vipps`, and `wero` on enums `PaymentIntentConfirmParams.allowed_payment_method_types`, `PaymentIntentCreateParams.allowed_payment_method_types`, and `PaymentIntentModifyParams.allowed_payment_method_types`
  * Add support for `custom_fields`, `description`, and `footer` on `Quote.InvoiceSetting`, `QuotePreviewSubscriptionSchedule.DefaultSetting.InvoiceSetting`, `QuotePreviewSubscriptionSchedule.Phase.InvoiceSetting`, `SubscriptionSchedule.DefaultSetting.InvoiceSetting`, and `SubscriptionSchedule.Phase.InvoiceSetting`
  * Add support for `paypay` on `SetupAttempt.PaymentMethodDetail`
  * Add support for new values `mass_transit_parking_tax` and `parking_tax` on enum `tax.RegistrationCreateParamsCountryOptionMe.type`
  * Add support for `mass_transit_parking_tax` and `parking_tax` on `Tax.Registration.CountryOption.Me`
  * ⚠️ Add support for new values `mass_transit_parking_tax` and `parking_tax` on enum `Tax.Registration.CountryOption.Me.type`
  * Add support for `gift_card_brand` on `terminal.ReaderCollectPaymentMethodParamsCollectConfig` and `terminal.ReaderProcessPaymentIntentParamsProcessConfig`
  * Add support for `activate_gift_card`, `cashout_gift_card`, `check_gift_card_balance`, `deactivate_gift_card`, and `reload_gift_card` on `Terminal.Reader.Action`
  * ⚠️ Add support for new values `activate_gift_card`, `cashout_gift_card`, `check_gift_card_balance`, `deactivate_gift_card`, and `reload_gift_card` on enum `Terminal.Reader.Action.type`
  * Add support for `status_transitions` on `V2.Billing.Contract`
  * ⚠️ Remove support for `one_time_fees` on `V2.Billing.Contract` and `v2.billing.ContractCreateParams`
  * ⚠️ Remove support for `status_details` on `V2.Billing.Contract`
  * Add support for `id` and `priority` on `V2.Billing.Contract.PricingLine.Datum.Pricing.PriceDetail.PricingOverride.Datum`
  * ⚠️ Remove support for `pricing_override` on `V2.Billing.Contract.PricingLine.Datum.Pricing.PriceDetail.PricingOverride.Datum`
  * ⚠️ Remove support for `tiering_mode` and `tiers` on `V2.Billing.Contract.PricingLine.Datum.Pricing.PriceDetail.PricingOverride.Datum.OverwritePrice`, `v2.billing.ContractCreateParamsPricingLinePricingPriceDetailPricingOverrideOverwritePrice`, `v2.billing.ContractModifyParamsPricingLineActionAddPricingPriceDetailPricingOverrideOverwritePrice`, `v2.billing.ContractModifyParamsPricingLineActionUpdatePricingPriceDetailPricingOverrideActionAddOverwritePrice`, and `v2.billing.ContractModifyParamsPricingOverrideActionAddOverwritePrice`
  * Add support for `multiply_pricing` on `V2.Billing.Contract.PricingOverride.Datum`, `v2.billing.ContractCreateParamsPricingOverride`, and `v2.billing.ContractModifyParamsPricingOverrideActionAdd`
  * ⚠️ Remove support for `multiplier` on `V2.Billing.Contract.PricingOverride.Datum`, `v2.billing.ContractCreateParamsPricingOverride`, and `v2.billing.ContractModifyParamsPricingOverrideActionAdd`
  * ⚠️ Change type of `V2.Billing.Contract.PricingOverride.Datum.type`, `v2.billing.ContractCreateParamsPricingOverride.type`, and `v2.billing.ContractModifyParamsPricingOverrideActionAdd.type` from `literal('multiplier')` to `literal('multiply_pricing')`
  * Add support for `related_network_object` on `V2.Core.Account` and `v2.core.AccountListParams`
  * ⚠️ Add support for new value `network_business_profile_wallet` on enum `V2.Core.Account.Configuration.Recipient.DefaultOutboundDestination.type`
  * Add support for `network_business_profile_wallet` on `V2.MoneyManagement.PayoutMethod`
  * Add support for new value `network_business_profile_wallet` on enums `V2.MoneyManagement.PayoutMethod.type`, `v2.money_management.OutboundSetupIntentCreateParamsPayoutMethodDatum.type`, and `v2.money_management.OutboundSetupIntentModifyParamsPayoutMethodDatum.type`
  * Add support for `stripe_network_transfer` on `V2.MoneyManagement.ReceivedCredit`
  * Add support for new value `stripe_network_transfer` on enum `V2.MoneyManagement.ReceivedCredit.type`
  * ⚠️ Remove support for value `one_time_fees` from enums `v2.billing.ContractActivateParams.include`, `v2.billing.ContractCancelParams.include`, `v2.billing.ContractCreateParams.include`, `v2.billing.ContractListParams.include`, `v2.billing.ContractModifyParams.include`, and `v2.billing.ContractRetrieveParams.include`
  * ⚠️ Change type of `v2.billing.ContractCreateParamsPricingLineEndsAt.type`, `v2.billing.ContractCreateParamsPricingLinePricingPriceDetailPricingOverrideEndsAt.type`, `v2.billing.ContractCreateParamsPricingOverrideEndsAt.type`, and `v2.billing.ContractModifyParamsPricingLineActionAddPricingPriceDetailPricingOverrideEndsAt.type` from `enum('contract_end'|'timestamp')` to `literal('timestamp')`
  * ⚠️ Change type of `v2.billing.ContractCreateParamsPricingLinePricingPriceDetailPricingOverrideStartsAt.type`, `v2.billing.ContractCreateParamsPricingLineStartsAt.type`, `v2.billing.ContractCreateParamsPricingOverrideStartsAt.type`, and `v2.billing.ContractModifyParamsPricingLineActionAddPricingPriceDetailPricingOverrideStartsAt.type` from `enum('contract_start'|'timestamp')` to `literal('timestamp')`
  * Change `v2.billing.ContractCreateParamsPricingOverride.priority` and `v2.billing.ContractModifyParamsPricingOverrideActionAdd.priority` to be optional
  * ⚠️ Change type of `v2.billing.ContractModifyParamsPricingLineActionAddEndsAt.type`, `v2.billing.ContractModifyParamsPricingLineActionUpdateEndsAt.type`, `v2.billing.ContractModifyParamsPricingLineActionUpdatePricingPriceDetailPricingOverrideActionAddEndsAt.type`, `v2.billing.ContractModifyParamsPricingLineActionUpdatePricingPriceDetailPricingOverrideActionUpdateEndsAt.type`, `v2.billing.ContractModifyParamsPricingOverrideActionAddEndsAt.type`, and `v2.billing.ContractModifyParamsPricingOverrideActionUpdateEndsAt.type` from `enum('billing_period_end'|'timestamp')` to `literal('timestamp')`
  * ⚠️ Change type of `v2.billing.ContractModifyParamsPricingLineActionAddStartsAt.type`, `v2.billing.ContractModifyParamsPricingLineActionUpdatePricingPriceDetailPricingOverrideActionAddStartsAt.type`, `v2.billing.ContractModifyParamsPricingLineActionUpdatePricingPriceDetailPricingOverrideActionUpdateStartsAt.type`, `v2.billing.ContractModifyParamsPricingLineActionUpdateStartsAt.type`, `v2.billing.ContractModifyParamsPricingOverrideActionAddStartsAt.type`, and `v2.billing.ContractModifyParamsPricingOverrideActionUpdateStartsAt.type` from `enum('billing_period_start'|'timestamp')` to `literal('timestamp')`
  * Add support for event notifications `V2BillingContractActivatedEvent`, `V2BillingContractCanceledEvent`, `V2BillingContractCreatedEvent`, `V2BillingContractEndedEvent`, and `V2BillingContractUpdatedEvent` with related object `v2.billing.Contract`

## 15.4.0a2 - 2026-07-01
This release changes the pinned API version to `2026-07-01.preview`.

* ⚠️ [#1839](https://github.com/stripe/stripe-python/pull/1839) Update generated code for private-preview
  * Add support for new resources `crypto.CustomerConsumerWallet`, `crypto.CustomerPaymentToken`, `crypto.Customer`, `crypto.OnrampSession`, and `crypto.OnrampTransactionLimits`
  * Add support for `list` and `retrieve` methods on resource `crypto.Customer`
  * Add support for `checkout`, `create`, `list`, `quote`, and `retrieve` methods on resource `crypto.OnrampSession`
  * Add support for `retrieve` method on resource `crypto.OnrampTransactionLimits`
  * Add support for `electronic_commerce_indicator` on `Charge.PaymentMethodDetail.Card`
  * Add support for `amount_received` and `amount_requested` on `Charge.PaymentMethodDetail.Crypto`, `PaymentAttemptRecord.PaymentMethodDetail.Crypto`, and `PaymentRecord.PaymentMethodDetail.Crypto`
  * Add support for `fingerprint` on `Charge.PaymentMethodDetail.GiftCard`, `PaymentAttemptRecord.PaymentMethodDetail.GiftCard`, and `PaymentRecord.PaymentMethodDetail.GiftCard`
  * Add support for `address_collection_precision` on `checkout.SessionCreateParamsAutomaticTax`
  * Add support for `subscription` on `Checkout.Session.Item`
  * ⚠️  Remove support for `deactivation` on `GiftCardOperation`
  * ⚠️  Remove support for value `deactivation` from enum `GiftCardOperation.type`
  * Add support for `merchant_amount_exchange_rate` on `Issuing.Authorization` and `Issuing.Transaction`
  * Add support for `device_id` on `Issuing.Authorization.TokenDetail.NetworkDatum.Device` and `Issuing.Token.NetworkDatum.Device`
  * Add support for `program` on `Issuing.Card`
  * Add support for `payment_method_details` on `PaymentAttemptRecordReportFailedParams` and `PaymentRecordReportPaymentAttemptFailedParams`
  * Add support for `reason` on `PaymentAttemptRecordReportRefundParams` and `PaymentRecordReportRefundParams`
  * Add support for `amount_reconciliation` on `PaymentIntent.PaymentMethodOption.Crypto`, `PaymentIntentConfirmParamsPaymentMethodOptionCrypto`, `PaymentIntentCreateParamsPaymentMethodOptionCrypto`, and `PaymentIntentModifyParamsPaymentMethodOptionCrypto`
  * Add support for `connect_permissions` and `permissions` on `V2.Iam.ApiKey`, `v2.iam.ApiKeyCreateParams`, and `v2.iam.ApiKeyModifyParams`
  * Add support for `credit` on `V2.MoneyManagement.FinancialAccount`
  * ⚠️  Add support for new value `credit` on enum `V2.MoneyManagement.FinancialAccount.type`
  * Add support for new value `currency_required` on enum `V2.MoneyManagement.PayoutIntent.NextAction.HandleFailure.failure_reason`
  * Add support for new values `issuing_authorization`, `issuing_transaction`, and `platform_funded_credit_transaction` on enums `V2.MoneyManagement.Transaction.category` and `V2.MoneyManagement.TransactionEntry.TransactionDetail.category`
  * Add support for `account`, `issuing_authorization`, `issuing_dispute`, and `issuing_transaction` on `V2.MoneyManagement.Transaction.Flow` and `V2.MoneyManagement.TransactionEntry.TransactionDetail.Flow`
  * Add support for new values `issuing_authorization`, `issuing_dispute`, and `issuing_transaction` on enums `V2.MoneyManagement.Transaction.Flow.type` and `V2.MoneyManagement.TransactionEntry.TransactionDetail.Flow.type`
  * Add support for new value `credit` on enum `v2.money_management.FinancialAccountListParams.types`
  * Change type of `v2.money_management.FinancialAccountCreateParams.type` from `literal('storage')` to `enum('credit'|'storage')`
  * Add support for `expires_at` on `v2.iam.ApiKeyCreateParams`

## 15.4.0a1 - 2026-06-24
This release changes the pinned API version to `2026-06-24.preview`.

* ⚠️ [#1833](https://github.com/stripe/stripe-python/pull/1833) Update generated code for private-preview
  * Add support for new resources `v2.billing.ContractPricingLineQuantityChange`, `v2.core.health.AlertHistoryEntry`, `v2.core.health.Alert`, `v2.money_management.FinancialAddressDebitSimulation`, and `v2.money_management.PayoutIntent`
  * ⚠️ Remove support for resource `v2.billing.ContractLicensePricingQuantityChange`
  * Add support for `report_offer_acceptance` method on resource `issuing.CreditUnderwritingRecord`
  * Add support for `provisional_credit` test helper method on resource `issuing.Dispute`
  * Add support for `report_early_fraud_warning` method on resource `PaymentAttemptRecord`
  * Add support for `search` method on resource `PaymentRecord`
  * Add support for `debit` method on resource `v2.money_management.FinancialAddressDebitSimulation`
  * Add support for `cancel`, `create`, `list`, `modify`, and `retrieve` methods on resource `v2.money_management.PayoutIntent`
  * Add support for `list` and `retrieve` methods on resource `v2.core.health.Alert`
  * Add support for `delete` method on resource `v2.billing.Contract`
  * ⚠️ Remove support for `performance_location_details` on `Tax.TransactionLineItem`
  * Add support for `financial_accounts_transactions`, `financial_accounts`, and `recipients_list` on `AccountSession.Component` and `AccountSessionCreateParamsComponent`
  * Add support for `location` and `reader` on `Charge.PaymentMethodDetail.GiftCard`, `GiftCardOperation`, `PaymentAttemptRecord.PaymentMethodDetail.GiftCard`, and `PaymentRecord.PaymentMethodDetail.GiftCard`
  * Add support for `subscription` on `checkout.SessionCreateParamsItem`
  * Add support for `items` on `Checkout.Session`
  * Add support for `brand` on `Checkout.Session.CurrentAttempt.PaymentMethodDetail.Card`
  * Add support for `network_data` on `issuing.AuthorizationCaptureParams` and `issuing.TransactionCreateForceCaptureParams`
  * Add support for `enriched_merchant_data` on `Issuing.Authorization`
  * Add support for `available_balance` and `current_balance` on `Issuing.Authorization.BalanceResponse`
  * ⚠️ Remove support for `amount` on `Issuing.Authorization.BalanceResponse`
  * Add support for `decision_deadline_updated_at` on `Issuing.CreditUnderwritingRecord`
  * Add support for `acquirer_reference_number` on `Issuing.Transaction.NetworkDatum`
  * Change `PaymentAttemptRecordReportRefundParams.outcome` and `PaymentRecordReportRefundParams.outcome` to be optional
  * Add support for `tip` on `PaymentIntentCaptureParamsAmountDetail`, `PaymentIntentConfirmParamsAmountDetail`, `PaymentIntentCreateParamsAmountDetail`, `PaymentIntentDecrementAuthorizationParamsAmountDetail`, `PaymentIntentIncrementAuthorizationParamsAmountDetail`, and `PaymentIntentModifyParamsAmountDetail`
  * ⚠️ Remove support for values `billing.alert.recovered` and `payment_intent.expired` from enums `WebhookEndpointCreateParams.enabled_events` and `WebhookEndpointModifyParams.enabled_events`
  * Add support for `billing_cycle_anchor` on `V2.Billing.Contract` and `v2.billing.ContractCreateParams`
  * ⚠️ Remove support for `contract_line_details`, `contract_value_details`, and `license_quantities` on `V2.Billing.Contract`
  * Add support for `bill_settings_details` on `V2.Billing.Contract.BillingSetting` and `v2.billing.ContractCreateParamsBillingSetting`
  * Add support for `billing_profile_details` and `collection_settings_details` on `V2.Billing.Contract.BillingSetting`
  * ⚠️ Remove support for `contract_billing_details` on `V2.Billing.Contract.BillingSetting` and `v2.billing.ContractCreateParamsBillingSetting`
  * ⚠️ Change type of `V2.Billing.Contract.one_time_fees` from `array(an object)` to `an object`
  * ⚠️ Change type of `V2.Billing.Contract.pricing_lines` from `array(an object)` to `an object`
  * ⚠️ Change type of `V2.Billing.Contract.pricing_overrides` from `array(an object)` to `an object`
  * ⚠️ Change `V2.Billing.Contract.pricing_lines` to be optional
  * ⚠️ Change `V2.Billing.Contract.pricing_overrides` to be optional
  * Add support for `mode` on `V2.Commerce.ProductCatalogImport`
  * Add support for new value `money_manager` on enums `EventsV2CoreAccountLinkReturnedEvent.configurations`, `V2.Core.AccountLink.UseCase.AccountOnboarding.configurations`, `V2.Core.AccountLink.UseCase.AccountUpdate.configurations`, `v2.core.AccountLinkCreateParamsUseCaseAccountOnboarding.configurations`, and `v2.core.AccountLinkCreateParamsUseCaseAccountUpdate.configurations`
  * ⚠️ Add support for new value `money_manager` on enums `V2.Core.Account.applied_configurations`, `v2.core.AccountCloseParams.applied_configurations`, and `v2.core.AccountListParams.applied_configurations`
  * ⚠️ Remove support for value `storer` from enums `V2.Core.Account.applied_configurations`, `v2.core.AccountCloseParams.applied_configurations`, and `v2.core.AccountListParams.applied_configurations`
  * Add support for `money_manager` on `V2.Core.Account.Configuration`, `V2.Core.Account.Identity.Attestation.TermsOfService`, `v2.core.AccountCreateParamsConfiguration`, `v2.core.AccountCreateParamsIdentityAttestationTermsOfService`, `v2.core.AccountModifyParamsConfiguration`, `v2.core.AccountModifyParamsIdentityAttestationTermsOfService`, and `v2.core.AccountTokenCreateParamsIdentityAttestationTermsOfService`
  * ⚠️ Remove support for `storer` on `V2.Core.Account.Configuration`, `V2.Core.Account.Identity.Attestation.TermsOfService`, `v2.core.AccountCreateParamsConfiguration`, `v2.core.AccountCreateParamsIdentityAttestationTermsOfService`, `v2.core.AccountModifyParamsConfiguration`, `v2.core.AccountModifyParamsIdentityAttestationTermsOfService`, and `v2.core.AccountTokenCreateParamsIdentityAttestationTermsOfService`
  * Add support for `sunbit_payments` on `V2.Core.Account.Configuration.Merchant.Capability`, `v2.core.AccountCreateParamsConfigurationMerchantCapability`, and `v2.core.AccountModifyParamsConfigurationMerchantCapability`
  * Add support for `ach`, `becs`, `eft`, `fedwire`, `fps`, `npp`, `rtp`, `sepa_credit`, `sepa_instant`, and `swift` on `V2.Core.Account.Configuration.Recipient.Capability.BankAccount`, `v2.core.AccountCreateParamsConfigurationRecipientCapabilityBankAccount`, and `v2.core.AccountModifyParamsConfigurationRecipientCapabilityBankAccount`
  * Add support for new values `bank_accounts.ach`, `bank_accounts.becs`, `bank_accounts.eft`, `bank_accounts.fedwire`, `bank_accounts.fps`, `bank_accounts.npp`, `bank_accounts.rtp`, `bank_accounts.sepa_credit`, `bank_accounts.sepa_instant`, `bank_accounts.swift`, `business_storage.inbound.eur`, `business_storage.inbound.gbp`, `business_storage.inbound.usd`, `business_storage.outbound.eur`, `business_storage.outbound.gbp`, `business_storage.outbound.usd`, `consumer_storage.inbound.usd`, `consumer_storage.outbound.usd`, `received_credits.bank_accounts`, and `received_debits.bank_accounts` on enums `V2.Core.Account.FutureRequirement.Entry.Impact.RestrictsCapability.capability` and `V2.Core.Account.Requirement.Entry.Impact.RestrictsCapability.capability`
  * Add support for new value `money_manager` on enums `V2.Core.Account.FutureRequirement.Entry.Impact.RestrictsCapability.configuration` and `V2.Core.Account.Requirement.Entry.Impact.RestrictsCapability.configuration`
  * Add support for `consumer_money_manager` on `V2.Core.Account.Identity.Attestation.TermsOfService`, `v2.core.AccountCreateParamsIdentityAttestationTermsOfService`, and `v2.core.AccountModifyParamsIdentityAttestationTermsOfService`
  * Add support for `crypto_money_manager` on `V2.Core.Account.Identity.Attestation.TermsOfService`, `v2.core.AccountCreateParamsIdentityAttestationTermsOfService`, `v2.core.AccountModifyParamsIdentityAttestationTermsOfService`, and `v2.core.AccountTokenCreateParamsIdentityAttestationTermsOfService`
  * ⚠️ Remove support for `consumer_storer` on `V2.Core.Account.Identity.Attestation.TermsOfService`, `v2.core.AccountCreateParamsIdentityAttestationTermsOfService`, and `v2.core.AccountModifyParamsIdentityAttestationTermsOfService`
  * ⚠️ Remove support for `crypto_storer` on `V2.Core.Account.Identity.Attestation.TermsOfService`, `v2.core.AccountCreateParamsIdentityAttestationTermsOfService`, `v2.core.AccountModifyParamsIdentityAttestationTermsOfService`, and `v2.core.AccountTokenCreateParamsIdentityAttestationTermsOfService`
  * ⚠️ Remove support for `maximum_rps` on `V2.Core.BatchJob` and `v2.core.BatchJobCreateParams`
  * Add support for `bic` on `V2.MoneyManagement.FinancialAddress.Credential.UsBankAccount`
  * ⚠️ Remove support for `swift_code` on `V2.MoneyManagement.FinancialAddress.Credential.UsBankAccount`
  * Add support for `attachment` on `V2.MoneyManagement.OutboundPayment.DeliveryOption.PaperCheck` and `v2.money_management.OutboundPaymentCreateParamsDeliveryOptionPaperCheck`
  * Add support for `processing` on `V2.MoneyManagement.OutboundPayment.StatusDetail` and `V2.MoneyManagement.OutboundTransfer.StatusDetail`
  * Add support for new values `fx_rate_drift_exceeded_after_review` and `review_rejected` on enum `V2.MoneyManagement.OutboundPayment.StatusDetail.Failed.reason`
  * Add support for `payout_method_options` on `V2.MoneyManagement.OutboundPayment.To`, `V2.MoneyManagement.OutboundTransfer.To`, `v2.money_management.OutboundPaymentCreateParamsTo`, and `v2.money_management.OutboundTransferCreateParamsTo`
  * Add support for new values `fx_rate_drift_exceeded_after_review` and `review_rejected` on enum `V2.MoneyManagement.OutboundTransfer.StatusDetail.Failed.reason`
  * Add support for `account_holder_name` on `V2.MoneyManagement.ReceivedCredit.BankTransfer.UsBankAccount`
  * Add support for `returned` on `V2.MoneyManagement.ReceivedDebit.StatusDetail`
  * Add support for new value `capability_inactive` on enum `V2.MoneyManagement.ReceivedDebit.StatusDetail.Failed.reason`
  * Add support for `returned_at` on `V2.MoneyManagement.ReceivedDebit.StatusTransition`
  * Add support for `payout_intent` on `v2.money_management.OutboundPaymentCreateParams`
  * Add support for `statuses` on `v2.money_management.FinancialAccountListParams`
  * ⚠️ Remove support for `status` on `v2.money_management.FinancialAccountListParams`
  * Change `v2.core.BatchJobCreateParams.metadata` to be optional
  * ⚠️ Add support for new value `configuration.money_manager` on enums `v2.core.AccountCreateParams.include`, `v2.core.AccountModifyParams.include`, and `v2.core.AccountRetrieveParams.include`
  * ⚠️ Remove support for value `configuration.storer` from enums `v2.core.AccountCreateParams.include`, `v2.core.AccountModifyParams.include`, and `v2.core.AccountRetrieveParams.include`
  * Add support for `include` on `v2.billing.ContractListParams`
  * ⚠️ Remove support for `contract_lines` on `v2.billing.ContractCreateParams`
  * ⚠️ Remove support for `license_quantity_actions` on `v2.billing.ContractCreateParams` and `v2.billing.ContractModifyParams`
  * ⚠️ Add support for `billing_profile_details` and `collection_settings_details` on `v2.billing.ContractCreateParamsBillingSetting`
  * ⚠️ Add support for new value `billing_settings` on enums `v2.billing.ContractActivateParams.include`, `v2.billing.ContractCancelParams.include`, `v2.billing.ContractCreateParams.include`, `v2.billing.ContractModifyParams.include`, and `v2.billing.ContractRetrieveParams.include`
  * ⚠️ Remove support for values `contract_line_details` and `license_quantities` from enums `v2.billing.ContractActivateParams.include`, `v2.billing.ContractCancelParams.include`, `v2.billing.ContractCreateParams.include`, `v2.billing.ContractModifyParams.include`, and `v2.billing.ContractRetrieveParams.include`
  * ⚠️ Add support for `amount`, `bill_at`, and `product` on `v2.billing.ContractCreateParamsOneTimeFee`
  * Add support for `lookup_key` on `v2.billing.ContractCreateParamsOneTimeFee`
  * ⚠️ Remove support for `bill_schedule`, `billable_item_type`, and `product_details` on `v2.billing.ContractCreateParamsOneTimeFee`
  * Add support for `pricing_overrides` and `quantity_changes` on `v2.billing.ContractCreateParamsPricingLinePricingPriceDetail` and `v2.billing.ContractModifyParamsPricingLineActionAddPricingPriceDetail`
  * ⚠️ Remove support for `quantity` on `v2.billing.ContractCreateParamsPricingLinePricingPriceDetail` and `v2.billing.ContractModifyParamsPricingLineActionAddPricingPriceDetail`
  * ⚠️ Remove support for `overwrite_price` on `v2.billing.ContractCreateParamsPricingOverride`
  * Add support for `pricing_line_ids` and `pricing_line_lookup_keys` on `v2.billing.ContractCreateParamsPricingOverrideMultiplierCriterion` and `v2.billing.ContractModifyParamsPricingOverrideActionAddMultiplierCriterion`
  * ⚠️ Remove support for `billable_item_ids`, `billable_item_lookup_keys`, `billable_item_types`, `metadata_conditions`, and `rate_card_ids` on `v2.billing.ContractCreateParamsPricingOverrideMultiplierCriterion` and `v2.billing.ContractModifyParamsPricingOverrideActionAddMultiplierCriterion`
  * ⚠️ Change type of `v2.billing.ContractCreateParamsPricingOverride.type` and `v2.billing.ContractModifyParamsPricingOverrideActionAdd.type` from `enum('multiplier'|'overwrite_price')` to `literal('multiplier')`
  * Change `v2.billing.ContractCreateParams.pricing_overrides` to be optional
  * Change `v2.billing.ContractCreateParamsPricingOverrideMultiplier.criteria` to be optional
  * Add support for `pricing` on `v2.billing.ContractModifyParamsPricingLineActionUpdate`
  * ⚠️ Remove support for `price` on `v2.billing.ContractModifyParamsPricingOverrideActionAddOverwritePrice`
  * Add support for `cancel_pricing_lines` and `proration_behavior` on `v2.billing.ContractCancelParams`
  * Add support for new value `sunbit_payments` on enum `EventsV2CoreAccountIncludingConfigurationMerchantCapabilityStatusUpdatedEvent.updated_capability`
  * Add support for new values `bank_accounts.ach`, `bank_accounts.becs`, `bank_accounts.eft`, `bank_accounts.fedwire`, `bank_accounts.fps`, `bank_accounts.npp`, `bank_accounts.rtp`, `bank_accounts.sepa_credit`, `bank_accounts.sepa_instant`, and `bank_accounts.swift` on enum `EventsV2CoreAccountIncludingConfigurationRecipientCapabilityStatusUpdatedEvent.updated_capability`
  * Add support for event notifications `V2CoreAccountIncludingConfigurationMoneyManagerCapabilityStatusUpdatedEvent` and `V2CoreAccountIncludingConfigurationMoneyManagerUpdatedEvent` with related object `v2.core.Account`
  * Add support for event notifications `V2MoneyManagementDebitDisputeFailedEvent`, `V2MoneyManagementDebitDisputeSubmittedEvent`, and `V2MoneyManagementDebitDisputeSucceededEvent` with related object `v2.money_management.DebitDispute`
  * Add support for event notification `V2MoneyManagementOutboundPaymentUnderReviewEvent` with related object `v2.money_management.OutboundPayment`
  * Add support for event notification `V2MoneyManagementOutboundTransferUnderReviewEvent` with related object `v2.money_management.OutboundTransfer`
  * ⚠️ Remove support for event notifications `V2CoreAccountIncludingConfigurationStorerCapabilityStatusUpdatedEvent` and `V2CoreAccountIncludingConfigurationStorerUpdatedEvent` with related object `v2.core.Account`
  * Add support for error codes `us_bank_account_microdeposits_cannot_be_confirmed` and `us_bank_account_microdeposits_cannot_be_sent` on `ControlledByAlternateResourceError`
  * Add support for error code `payout_intent_not_cancelable` on `NotCancelableError`

## 15.3.0a4 - 2026-06-17
* ⚠️ [#1828](https://github.com/stripe/stripe-python/pull/1828) Update generated code for private-preview
  * Add support for `retrieve` method on resource `radar.CustomerEvaluation`
  * Add support for `disable_stripe_user_authentication` on `AccountSession.Component.Bill.Feature`
  * Add support for `tamara` on `Charge.PaymentMethodDetail`, `ConfirmationToken.PaymentMethodPreview`, `ConfirmationTokenCreateParamsPaymentMethodDatum`, `PaymentAttemptRecord.PaymentMethodDetail`, `PaymentIntentConfirmParamsPaymentMethodDatum`, `PaymentIntentCreateParamsPaymentMethodDatum`, `PaymentIntentModifyParamsPaymentMethodDatum`, `PaymentMethodCreateParams`, `PaymentMethod`, `PaymentRecord.PaymentMethodDetail`, `SetupIntentConfirmParamsPaymentMethodDatum`, `SetupIntentCreateParamsPaymentMethodDatum`, `SetupIntentModifyParamsPaymentMethodDatum`, and `SharedPayment.GrantedToken.PaymentMethodDetail`
  * Add support for `status` on `Charge.PaymentMethodDetail.Card.AccountFunding`
  * ⚠️ Remove support for `processed_transaction_type` on `Charge.PaymentMethodDetail.Card.AccountFunding`
  * Add support for `items` on `checkout.SessionCreateParams`
  * ⚠️ Remove support for `brand` on `Checkout.Session.CurrentAttempt.PaymentMethodDetail.Card`
  * Add support for new value `tamara` on enums `ConfirmationTokenCreateParamsPaymentMethodDatum.type`, `PaymentIntentConfirmParamsPaymentMethodDatum.type`, `PaymentIntentCreateParamsPaymentMethodDatum.type`, `PaymentIntentModifyParamsPaymentMethodDatum.type`, `SetupIntentConfirmParamsPaymentMethodDatum.type`, `SetupIntentCreateParamsPaymentMethodDatum.type`, and `SetupIntentModifyParamsPaymentMethodDatum.type`
  * ⚠️ Remove support for `first6` on `ConfirmationToken.PaymentMethodPreview.GiftCard`, `PaymentMethod.GiftCard`, and `SharedPayment.GrantedToken.PaymentMethodDetail.GiftCard`
  * ⚠️ Add support for new value `tamara` on enums `ConfirmationToken.PaymentMethodPreview.type`, `PaymentMethod.type`, and `SharedPayment.GrantedToken.PaymentMethodDetail.type`
  * Add support for new value `tamara` on enums `CustomerListPaymentMethodsParams.type`, `PaymentMethodCreateParams.type`, and `PaymentMethodListParams.type`
  * Add support for `fingerprint` on `GiftCard`
  * Add support for `blik` on `Mandate.PaymentMethodDetail`
  * Add support for `buyer_id` on `Order.Payment.Setting.PaymentMethodOption.WechatPay`, `OrderCreateParamsPaymentSettingPaymentMethodOptionWechatPay`, `OrderModifyParamsPaymentSettingPaymentMethodOptionWechatPay`, `PaymentIntent.PaymentMethodOption.WechatPay`, `PaymentIntentConfirmParamsPaymentMethodOptionWechatPay`, `PaymentIntentCreateParamsPaymentMethodOptionWechatPay`, and `PaymentIntentModifyParamsPaymentMethodOptionWechatPay`
  * Add support for new value `mini_program` on enums `OrderCreateParamsPaymentSettingPaymentMethodOptionWechatPay.client`, `OrderModifyParamsPaymentSettingPaymentMethodOptionWechatPay.client`, `PaymentIntentConfirmParamsPaymentMethodOptionWechatPay.client`, `PaymentIntentCreateParamsPaymentMethodOptionWechatPay.client`, and `PaymentIntentModifyParamsPaymentMethodOptionWechatPay.client`
  * ⚠️ Add support for new value `mini_program` on enums `Order.Payment.Setting.PaymentMethodOption.WechatPay.client` and `PaymentIntent.PaymentMethodOption.WechatPay.client`
  * Add support for `payment_method_details` on `PaymentAttemptRecordReportGuaranteedParams` and `PaymentRecordReportPaymentAttemptGuaranteedParams`
  * Add support for `failed` and `refund_group` on `PaymentAttemptRecordReportRefundParams` and `PaymentRecordReportRefundParams`
  * Change type of `PaymentAttemptRecordReportRefundParams.outcome` and `PaymentRecordReportRefundParams.outcome` from `literal('refunded')` to `enum('failed'|'refunded')`
  * Add support for new value `tamara` on enums `PaymentIntentConfirmParams.allowed_payment_method_types`, `PaymentIntentCreateParams.allowed_payment_method_types`, and `PaymentIntentModifyParams.allowed_payment_method_types`
  * Add support for new value `tamara` on enums `PaymentIntentConfirmParams.excluded_payment_method_types`, `PaymentIntentCreateParams.excluded_payment_method_types`, `PaymentIntentModifyParams.excluded_payment_method_types`, `SetupIntentCreateParams.excluded_payment_method_types`, and `SetupIntentModifyParams.excluded_payment_method_types`
  * Add support for `beneficiary_details` on `PaymentIntent.PaymentDetail.MoneyService`, `PaymentIntentConfirmParamsPaymentDetailMoneyService`, `PaymentIntentCreateParamsPaymentDetailMoneyService`, and `PaymentIntentModifyParamsPaymentDetailMoneyService`
  * ⚠️ Remove support for `beneficiary_account` and `beneficiary_details` on `PaymentIntent.PaymentDetail.MoneyService.AccountFunding`, `PaymentIntentConfirmParamsPaymentDetailMoneyServiceAccountFunding`, `PaymentIntentCreateParamsPaymentDetailMoneyServiceAccountFunding`, and `PaymentIntentModifyParamsPaymentDetailMoneyServiceAccountFunding`
  * ⚠️ Remove support for `sender_account` on `PaymentIntentConfirmParamsPaymentDetailMoneyServiceAccountFunding`, `PaymentIntentCreateParamsPaymentDetailMoneyServiceAccountFunding`, and `PaymentIntentModifyParamsPaymentDetailMoneyServiceAccountFunding`
  * Add support for `given_name` and `surname` on `PaymentIntent.PaymentDetail.MoneyService.AccountFunding.SenderDetail`, `PaymentIntentConfirmParamsPaymentDetailMoneyServiceAccountFundingSenderDetail`, `PaymentIntentCreateParamsPaymentDetailMoneyServiceAccountFundingSenderDetail`, and `PaymentIntentModifyParamsPaymentDetailMoneyServiceAccountFundingSenderDetail`
  * ⚠️ Remove support for `name` on `PaymentIntent.PaymentDetail.MoneyService.AccountFunding.SenderDetail`, `PaymentIntentConfirmParamsPaymentDetailMoneyServiceAccountFundingSenderDetail`, `PaymentIntentCreateParamsPaymentDetailMoneyServiceAccountFundingSenderDetail`, and `PaymentIntentModifyParamsPaymentDetailMoneyServiceAccountFundingSenderDetail`
  * Change type of `PaymentIntentConfirmParamsPaymentMethodOptionCard.capture_method`, `PaymentIntentCreateParamsPaymentMethodOptionCard.capture_method`, and `PaymentIntentModifyParamsPaymentMethodOptionCard.capture_method` from `literal('manual')` to `enum('automatic_delayed'|'manual')`
  * ⚠️ Remove support for `wallet` on `PaymentIntentConfirmParamsPaymentMethodOptionCardPaymentDetailMoneyServiceAccountFunding`, `PaymentIntentConfirmParamsPaymentMethodOptionCardPresentPaymentDetailMoneyServiceAccountFunding`, `PaymentIntentCreateParamsPaymentMethodOptionCardPaymentDetailMoneyServiceAccountFunding`, `PaymentIntentCreateParamsPaymentMethodOptionCardPresentPaymentDetailMoneyServiceAccountFunding`, `PaymentIntentModifyParamsPaymentMethodOptionCardPaymentDetailMoneyServiceAccountFunding`, and `PaymentIntentModifyParamsPaymentMethodOptionCardPresentPaymentDetailMoneyServiceAccountFunding`
  * Add support for new value `automatic_delayed` on enums `PaymentIntentConfirmParamsPaymentMethodOptionCardPresent.capture_method`, `PaymentIntentCreateParamsPaymentMethodOptionCardPresent.capture_method`, and `PaymentIntentModifyParamsPaymentMethodOptionCardPresent.capture_method`
  * Add support for `transaction_verification_options` on `PaymentIntent.PaymentMethodOption.Crypto`, `PaymentIntentConfirmParamsPaymentMethodOptionCrypto`, `PaymentIntentCreateParamsPaymentMethodOptionCrypto`, and `PaymentIntentModifyParamsPaymentMethodOptionCrypto`
  * Add support for new values `ethereum` and `polygon` on enums `PaymentIntentConfirmParamsPaymentMethodOptionCryptoDepositOption.networks`, `PaymentIntentCreateParamsPaymentMethodOptionCryptoDepositOption.networks`, and `PaymentIntentModifyParamsPaymentMethodOptionCryptoDepositOption.networks`
  * Add support for new values `ethereum` and `polygon` on enum `PaymentIntentSimulateCryptoDepositParams.network`
  * Change type of `PaymentIntentSimulateCryptoDepositParams.token_currency` from `literal('usdc')` to `enum('usdc'|'usdg'|'usdp')`
  * Add support for `forced_capture` on `PaymentIntent.AdvancedFeatureDetail`
  * ⚠️ Add support for new value `tamara` on enums `PaymentIntent.excluded_payment_method_types` and `SetupIntent.excluded_payment_method_types`
  * Add support for `wechat_pay_handle_app_redirect` on `PaymentIntent.NextAction` and `SetupIntent.NextAction`
  * Add support for `ethereum` and `polygon` on `PaymentIntent.NextAction.CryptoDisplayDetail.DepositAddress`
  * ⚠️ Change type of `PaymentIntent.NextAction.CryptoDisplayDetail.DepositAddress.Base.SupportedToken.token_currency`, `PaymentIntent.NextAction.CryptoDisplayDetail.DepositAddress.Solana.SupportedToken.token_currency`, and `PaymentIntent.NextAction.CryptoDisplayDetail.DepositAddress.Tempo.SupportedToken.token_currency` from `literal('usdc')` to `enum('usdc'|'usdg'|'usdp')`
  * Add support for `beneficiary_account` on `PaymentIntent.PaymentDetail.MoneyService`
  * ⚠️ Change type of `PaymentIntent.PaymentMethodOption.Card.capture_method` from `literal('manual')` to `enum('automatic_delayed'|'manual')`
  * ⚠️ Add support for new value `automatic_delayed` on enum `PaymentIntent.PaymentMethodOption.CardPresent.capture_method`
  * ⚠️ Add support for new values `ethereum` and `polygon` on enum `PaymentIntent.PaymentMethodOption.Crypto.DepositOption.networks`
  * Change type of `PaymentLocationModifyParamsBusinessRegistration.siret` from `string` to `emptyable(string)`
  * Add support for `card` on `PaymentRecordReportPaymentAttemptParamsPaymentMethodDetail` and `PaymentRecordReportPaymentParamsPaymentMethodDetail`
  * Change type of `PaymentRecordReportPaymentAttemptParamsPaymentMethodDetail.type` and `PaymentRecordReportPaymentParamsPaymentMethodDetail.type` from `literal('custom')` to `enum('card'|'custom')`
  * Add support for `managed_payments` on `Product`
  * Add support for `payment_attempt_record` on `RefundCreateParams` and `RefundListParams`
  * Add support for `payment_record` on `RefundListParams`
  * Add support for `protections` on `V2.Core.Account.Configuration.CardCreator.Capability.Commercial.Celtic.ChargeCard`, `V2.Core.Account.Configuration.CardCreator.Capability.Commercial.Celtic.SpendCard`, `V2.Core.Account.Configuration.CardCreator.Capability.Commercial.CrossRiverBank.ChargeCard`, `V2.Core.Account.Configuration.CardCreator.Capability.Commercial.CrossRiverBank.PrepaidCard`, `V2.Core.Account.Configuration.CardCreator.Capability.Commercial.CrossRiverBank.SpendCard`, `V2.Core.Account.Configuration.CardCreator.Capability.Commercial.FifthThird.ChargeCard`, `V2.Core.Account.Configuration.CardCreator.Capability.Commercial.Lead.PrepaidCard`, `V2.Core.Account.Configuration.CardCreator.Capability.Commercial.Stripe.ChargeCard`, `V2.Core.Account.Configuration.CardCreator.Capability.Commercial.Stripe.PrepaidCard`, `V2.Core.Account.Configuration.CardCreator.Capability.Consumer.Celtic.RevolvingCreditCard`, `V2.Core.Account.Configuration.CardCreator.Capability.Consumer.CrossRiverBank.PrepaidCard`, `V2.Core.Account.Configuration.CardCreator.Capability.Consumer.Lead.DebitCard`, `V2.Core.Account.Configuration.CardCreator.Capability.Consumer.Lead.PrepaidCard`, `V2.Core.Account.Configuration.Customer.Capability.AutomaticIndirectTax`, `V2.Core.Account.Configuration.Merchant.Capability.AchDebitPayment`, `V2.Core.Account.Configuration.Merchant.Capability.AcssDebitPayment`, `V2.Core.Account.Configuration.Merchant.Capability.AffirmPayment`, `V2.Core.Account.Configuration.Merchant.Capability.AfterpayClearpayPayment`, `V2.Core.Account.Configuration.Merchant.Capability.AlmaPayment`, `V2.Core.Account.Configuration.Merchant.Capability.AmazonPayPayment`, `V2.Core.Account.Configuration.Merchant.Capability.AuBecsDebitPayment`, `V2.Core.Account.Configuration.Merchant.Capability.BacsDebitPayment`, `V2.Core.Account.Configuration.Merchant.Capability.BancontactPayment`, `V2.Core.Account.Configuration.Merchant.Capability.BlikPayment`, `V2.Core.Account.Configuration.Merchant.Capability.BoletoPayment`, `V2.Core.Account.Configuration.Merchant.Capability.CardPayment`, `V2.Core.Account.Configuration.Merchant.Capability.CartesBancairesPayment`, `V2.Core.Account.Configuration.Merchant.Capability.CashappPayment`, `V2.Core.Account.Configuration.Merchant.Capability.EpsPayment`, `V2.Core.Account.Configuration.Merchant.Capability.FpxPayment`, `V2.Core.Account.Configuration.Merchant.Capability.GbBankTransferPayment`, `V2.Core.Account.Configuration.Merchant.Capability.GrabpayPayment`, `V2.Core.Account.Configuration.Merchant.Capability.IdealPayment`, `V2.Core.Account.Configuration.Merchant.Capability.JcbPayment`, `V2.Core.Account.Configuration.Merchant.Capability.JpBankTransferPayment`, `V2.Core.Account.Configuration.Merchant.Capability.KakaoPayPayment`, `V2.Core.Account.Configuration.Merchant.Capability.KlarnaPayment`, `V2.Core.Account.Configuration.Merchant.Capability.KonbiniPayment`, `V2.Core.Account.Configuration.Merchant.Capability.KrCardPayment`, `V2.Core.Account.Configuration.Merchant.Capability.LinkPayment`, `V2.Core.Account.Configuration.Merchant.Capability.MobilepayPayment`, `V2.Core.Account.Configuration.Merchant.Capability.MultibancoPayment`, `V2.Core.Account.Configuration.Merchant.Capability.MxBankTransferPayment`, `V2.Core.Account.Configuration.Merchant.Capability.NaverPayPayment`, `V2.Core.Account.Configuration.Merchant.Capability.OxxoPayment`, `V2.Core.Account.Configuration.Merchant.Capability.P24Payment`, `V2.Core.Account.Configuration.Merchant.Capability.PayByBankPayment`, `V2.Core.Account.Configuration.Merchant.Capability.PaycoPayment`, `V2.Core.Account.Configuration.Merchant.Capability.PaynowPayment`, `V2.Core.Account.Configuration.Merchant.Capability.PromptpayPayment`, `V2.Core.Account.Configuration.Merchant.Capability.RevolutPayPayment`, `V2.Core.Account.Configuration.Merchant.Capability.SamsungPayPayment`, `V2.Core.Account.Configuration.Merchant.Capability.SepaBankTransferPayment`, `V2.Core.Account.Configuration.Merchant.Capability.SepaDebitPayment`, `V2.Core.Account.Configuration.Merchant.Capability.StripeBalance.Payout`, `V2.Core.Account.Configuration.Merchant.Capability.SwishPayment`, `V2.Core.Account.Configuration.Merchant.Capability.TwintPayment`, `V2.Core.Account.Configuration.Merchant.Capability.UsBankTransferPayment`, `V2.Core.Account.Configuration.Merchant.Capability.ZipPayment`, `V2.Core.Account.Configuration.Recipient.Capability.BankAccount.Instant`, `V2.Core.Account.Configuration.Recipient.Capability.BankAccount.Local`, `V2.Core.Account.Configuration.Recipient.Capability.BankAccount.Wire`, `V2.Core.Account.Configuration.Recipient.Capability.Card`, `V2.Core.Account.Configuration.Recipient.Capability.CryptoWallet`, `V2.Core.Account.Configuration.Recipient.Capability.PaperCheck`, `V2.Core.Account.Configuration.Recipient.Capability.StripeBalance.Payout`, `V2.Core.Account.Configuration.Recipient.Capability.StripeBalance.StripeTransfer`, `V2.Core.Account.Configuration.Storer.Capability.Consumer.HoldsCurrency.Usd`, `V2.Core.Account.Configuration.Storer.Capability.FinancialAddress.BankAccount`, `V2.Core.Account.Configuration.Storer.Capability.FinancialAddress.CryptoWallet`, `V2.Core.Account.Configuration.Storer.Capability.HoldsCurrency.Eur`, `V2.Core.Account.Configuration.Storer.Capability.HoldsCurrency.Gbp`, `V2.Core.Account.Configuration.Storer.Capability.HoldsCurrency.Usd`, `V2.Core.Account.Configuration.Storer.Capability.HoldsCurrency.Usdc`, `V2.Core.Account.Configuration.Storer.Capability.InboundTransfer.BankAccount`, `V2.Core.Account.Configuration.Storer.Capability.OutboundPayment.BankAccount`, `V2.Core.Account.Configuration.Storer.Capability.OutboundPayment.Card`, `V2.Core.Account.Configuration.Storer.Capability.OutboundPayment.CryptoWallet`, `V2.Core.Account.Configuration.Storer.Capability.OutboundPayment.FinancialAccount`, `V2.Core.Account.Configuration.Storer.Capability.OutboundPayment.PaperCheck`, `V2.Core.Account.Configuration.Storer.Capability.OutboundTransfer.BankAccount`, `V2.Core.Account.Configuration.Storer.Capability.OutboundTransfer.CryptoWallet`, `V2.Core.Account.Configuration.Storer.Capability.OutboundTransfer.FinancialAccount`, `v2.core.AccountCreateParamsConfigurationCardCreatorCapabilityCommercialCelticChargeCard`, `v2.core.AccountCreateParamsConfigurationCardCreatorCapabilityCommercialCelticSpendCard`, `v2.core.AccountCreateParamsConfigurationCardCreatorCapabilityCommercialCrossRiverBankChargeCard`, `v2.core.AccountCreateParamsConfigurationCardCreatorCapabilityCommercialCrossRiverBankPrepaidCard`, `v2.core.AccountCreateParamsConfigurationCardCreatorCapabilityCommercialCrossRiverBankSpendCard`, `v2.core.AccountCreateParamsConfigurationCardCreatorCapabilityCommercialFifthThirdChargeCard`, `v2.core.AccountCreateParamsConfigurationCardCreatorCapabilityCommercialLeadPrepaidCard`, `v2.core.AccountCreateParamsConfigurationCardCreatorCapabilityCommercialStripeChargeCard`, `v2.core.AccountCreateParamsConfigurationCardCreatorCapabilityCommercialStripePrepaidCard`, `v2.core.AccountCreateParamsConfigurationCardCreatorCapabilityConsumerCelticRevolvingCreditCard`, `v2.core.AccountCreateParamsConfigurationCardCreatorCapabilityConsumerCrossRiverBankPrepaidCard`, `v2.core.AccountCreateParamsConfigurationCardCreatorCapabilityConsumerLeadDebitCard`, `v2.core.AccountCreateParamsConfigurationCardCreatorCapabilityConsumerLeadPrepaidCard`, `v2.core.AccountCreateParamsConfigurationCustomerCapabilityAutomaticIndirectTax`, `v2.core.AccountCreateParamsConfigurationMerchantCapabilityAchDebitPayment`, `v2.core.AccountCreateParamsConfigurationMerchantCapabilityAcssDebitPayment`, `v2.core.AccountCreateParamsConfigurationMerchantCapabilityAffirmPayment`, `v2.core.AccountCreateParamsConfigurationMerchantCapabilityAfterpayClearpayPayment`, `v2.core.AccountCreateParamsConfigurationMerchantCapabilityAlmaPayment`, `v2.core.AccountCreateParamsConfigurationMerchantCapabilityAmazonPayPayment`, `v2.core.AccountCreateParamsConfigurationMerchantCapabilityAuBecsDebitPayment`, `v2.core.AccountCreateParamsConfigurationMerchantCapabilityBacsDebitPayment`, `v2.core.AccountCreateParamsConfigurationMerchantCapabilityBancontactPayment`, `v2.core.AccountCreateParamsConfigurationMerchantCapabilityBlikPayment`, `v2.core.AccountCreateParamsConfigurationMerchantCapabilityBoletoPayment`, `v2.core.AccountCreateParamsConfigurationMerchantCapabilityCardPayment`, `v2.core.AccountCreateParamsConfigurationMerchantCapabilityCartesBancairesPayment`, `v2.core.AccountCreateParamsConfigurationMerchantCapabilityCashappPayment`, `v2.core.AccountCreateParamsConfigurationMerchantCapabilityEpsPayment`, `v2.core.AccountCreateParamsConfigurationMerchantCapabilityFpxPayment`, `v2.core.AccountCreateParamsConfigurationMerchantCapabilityGbBankTransferPayment`, `v2.core.AccountCreateParamsConfigurationMerchantCapabilityGrabpayPayment`, `v2.core.AccountCreateParamsConfigurationMerchantCapabilityIdealPayment`, `v2.core.AccountCreateParamsConfigurationMerchantCapabilityJcbPayment`, `v2.core.AccountCreateParamsConfigurationMerchantCapabilityJpBankTransferPayment`, `v2.core.AccountCreateParamsConfigurationMerchantCapabilityKakaoPayPayment`, `v2.core.AccountCreateParamsConfigurationMerchantCapabilityKlarnaPayment`, `v2.core.AccountCreateParamsConfigurationMerchantCapabilityKonbiniPayment`, `v2.core.AccountCreateParamsConfigurationMerchantCapabilityKrCardPayment`, `v2.core.AccountCreateParamsConfigurationMerchantCapabilityLinkPayment`, `v2.core.AccountCreateParamsConfigurationMerchantCapabilityMobilepayPayment`, `v2.core.AccountCreateParamsConfigurationMerchantCapabilityMultibancoPayment`, `v2.core.AccountCreateParamsConfigurationMerchantCapabilityMxBankTransferPayment`, `v2.core.AccountCreateParamsConfigurationMerchantCapabilityNaverPayPayment`, `v2.core.AccountCreateParamsConfigurationMerchantCapabilityOxxoPayment`, `v2.core.AccountCreateParamsConfigurationMerchantCapabilityP24Payment`, `v2.core.AccountCreateParamsConfigurationMerchantCapabilityPayByBankPayment`, `v2.core.AccountCreateParamsConfigurationMerchantCapabilityPaycoPayment`, `v2.core.AccountCreateParamsConfigurationMerchantCapabilityPaynowPayment`, `v2.core.AccountCreateParamsConfigurationMerchantCapabilityPromptpayPayment`, `v2.core.AccountCreateParamsConfigurationMerchantCapabilityRevolutPayPayment`, `v2.core.AccountCreateParamsConfigurationMerchantCapabilitySamsungPayPayment`, `v2.core.AccountCreateParamsConfigurationMerchantCapabilitySepaBankTransferPayment`, `v2.core.AccountCreateParamsConfigurationMerchantCapabilitySepaDebitPayment`, `v2.core.AccountCreateParamsConfigurationMerchantCapabilitySwishPayment`, `v2.core.AccountCreateParamsConfigurationMerchantCapabilityTwintPayment`, `v2.core.AccountCreateParamsConfigurationMerchantCapabilityUsBankTransferPayment`, `v2.core.AccountCreateParamsConfigurationMerchantCapabilityZipPayment`, `v2.core.AccountCreateParamsConfigurationRecipientCapabilityBankAccountInstant`, `v2.core.AccountCreateParamsConfigurationRecipientCapabilityBankAccountLocal`, `v2.core.AccountCreateParamsConfigurationRecipientCapabilityBankAccountWire`, `v2.core.AccountCreateParamsConfigurationRecipientCapabilityCard`, `v2.core.AccountCreateParamsConfigurationRecipientCapabilityCryptoWallet`, `v2.core.AccountCreateParamsConfigurationRecipientCapabilityPaperCheck`, `v2.core.AccountCreateParamsConfigurationRecipientCapabilityStripeBalanceStripeTransfer`, `v2.core.AccountCreateParamsConfigurationStorerCapabilityConsumerHoldsCurrencyUsd`, `v2.core.AccountCreateParamsConfigurationStorerCapabilityFinancialAddressBankAccount`, `v2.core.AccountCreateParamsConfigurationStorerCapabilityFinancialAddressCryptoWallet`, `v2.core.AccountCreateParamsConfigurationStorerCapabilityHoldsCurrencyEur`, `v2.core.AccountCreateParamsConfigurationStorerCapabilityHoldsCurrencyGbp`, `v2.core.AccountCreateParamsConfigurationStorerCapabilityHoldsCurrencyUsd`, `v2.core.AccountCreateParamsConfigurationStorerCapabilityHoldsCurrencyUsdc`, `v2.core.AccountCreateParamsConfigurationStorerCapabilityInboundTransferBankAccount`, `v2.core.AccountCreateParamsConfigurationStorerCapabilityOutboundPaymentBankAccount`, `v2.core.AccountCreateParamsConfigurationStorerCapabilityOutboundPaymentCard`, `v2.core.AccountCreateParamsConfigurationStorerCapabilityOutboundPaymentCryptoWallet`, `v2.core.AccountCreateParamsConfigurationStorerCapabilityOutboundPaymentFinancialAccount`, `v2.core.AccountCreateParamsConfigurationStorerCapabilityOutboundPaymentPaperCheck`, `v2.core.AccountCreateParamsConfigurationStorerCapabilityOutboundTransferBankAccount`, `v2.core.AccountCreateParamsConfigurationStorerCapabilityOutboundTransferCryptoWallet`, `v2.core.AccountCreateParamsConfigurationStorerCapabilityOutboundTransferFinancialAccount`, `v2.core.AccountModifyParamsConfigurationCardCreatorCapabilityCommercialCelticChargeCard`, `v2.core.AccountModifyParamsConfigurationCardCreatorCapabilityCommercialCelticSpendCard`, `v2.core.AccountModifyParamsConfigurationCardCreatorCapabilityCommercialCrossRiverBankChargeCard`, `v2.core.AccountModifyParamsConfigurationCardCreatorCapabilityCommercialCrossRiverBankPrepaidCard`, `v2.core.AccountModifyParamsConfigurationCardCreatorCapabilityCommercialCrossRiverBankSpendCard`, `v2.core.AccountModifyParamsConfigurationCardCreatorCapabilityCommercialFifthThirdChargeCard`, `v2.core.AccountModifyParamsConfigurationCardCreatorCapabilityCommercialLeadPrepaidCard`, `v2.core.AccountModifyParamsConfigurationCardCreatorCapabilityCommercialStripeChargeCard`, `v2.core.AccountModifyParamsConfigurationCardCreatorCapabilityCommercialStripePrepaidCard`, `v2.core.AccountModifyParamsConfigurationCardCreatorCapabilityConsumerCelticRevolvingCreditCard`, `v2.core.AccountModifyParamsConfigurationCardCreatorCapabilityConsumerCrossRiverBankPrepaidCard`, `v2.core.AccountModifyParamsConfigurationCardCreatorCapabilityConsumerLeadDebitCard`, `v2.core.AccountModifyParamsConfigurationCardCreatorCapabilityConsumerLeadPrepaidCard`, `v2.core.AccountModifyParamsConfigurationCustomerCapabilityAutomaticIndirectTax`, `v2.core.AccountModifyParamsConfigurationMerchantCapabilityAchDebitPayment`, `v2.core.AccountModifyParamsConfigurationMerchantCapabilityAcssDebitPayment`, `v2.core.AccountModifyParamsConfigurationMerchantCapabilityAffirmPayment`, `v2.core.AccountModifyParamsConfigurationMerchantCapabilityAfterpayClearpayPayment`, `v2.core.AccountModifyParamsConfigurationMerchantCapabilityAlmaPayment`, `v2.core.AccountModifyParamsConfigurationMerchantCapabilityAmazonPayPayment`, `v2.core.AccountModifyParamsConfigurationMerchantCapabilityAuBecsDebitPayment`, `v2.core.AccountModifyParamsConfigurationMerchantCapabilityBacsDebitPayment`, `v2.core.AccountModifyParamsConfigurationMerchantCapabilityBancontactPayment`, `v2.core.AccountModifyParamsConfigurationMerchantCapabilityBlikPayment`, `v2.core.AccountModifyParamsConfigurationMerchantCapabilityBoletoPayment`, `v2.core.AccountModifyParamsConfigurationMerchantCapabilityCardPayment`, `v2.core.AccountModifyParamsConfigurationMerchantCapabilityCartesBancairesPayment`, `v2.core.AccountModifyParamsConfigurationMerchantCapabilityCashappPayment`, `v2.core.AccountModifyParamsConfigurationMerchantCapabilityEpsPayment`, `v2.core.AccountModifyParamsConfigurationMerchantCapabilityFpxPayment`, `v2.core.AccountModifyParamsConfigurationMerchantCapabilityGbBankTransferPayment`, `v2.core.AccountModifyParamsConfigurationMerchantCapabilityGrabpayPayment`, `v2.core.AccountModifyParamsConfigurationMerchantCapabilityIdealPayment`, `v2.core.AccountModifyParamsConfigurationMerchantCapabilityJcbPayment`, `v2.core.AccountModifyParamsConfigurationMerchantCapabilityJpBankTransferPayment`, `v2.core.AccountModifyParamsConfigurationMerchantCapabilityKakaoPayPayment`, `v2.core.AccountModifyParamsConfigurationMerchantCapabilityKlarnaPayment`, `v2.core.AccountModifyParamsConfigurationMerchantCapabilityKonbiniPayment`, `v2.core.AccountModifyParamsConfigurationMerchantCapabilityKrCardPayment`, `v2.core.AccountModifyParamsConfigurationMerchantCapabilityLinkPayment`, `v2.core.AccountModifyParamsConfigurationMerchantCapabilityMobilepayPayment`, `v2.core.AccountModifyParamsConfigurationMerchantCapabilityMultibancoPayment`, `v2.core.AccountModifyParamsConfigurationMerchantCapabilityMxBankTransferPayment`, `v2.core.AccountModifyParamsConfigurationMerchantCapabilityNaverPayPayment`, `v2.core.AccountModifyParamsConfigurationMerchantCapabilityOxxoPayment`, `v2.core.AccountModifyParamsConfigurationMerchantCapabilityP24Payment`, `v2.core.AccountModifyParamsConfigurationMerchantCapabilityPayByBankPayment`, `v2.core.AccountModifyParamsConfigurationMerchantCapabilityPaycoPayment`, `v2.core.AccountModifyParamsConfigurationMerchantCapabilityPaynowPayment`, `v2.core.AccountModifyParamsConfigurationMerchantCapabilityPromptpayPayment`, `v2.core.AccountModifyParamsConfigurationMerchantCapabilityRevolutPayPayment`, `v2.core.AccountModifyParamsConfigurationMerchantCapabilitySamsungPayPayment`, `v2.core.AccountModifyParamsConfigurationMerchantCapabilitySepaBankTransferPayment`, `v2.core.AccountModifyParamsConfigurationMerchantCapabilitySepaDebitPayment`, `v2.core.AccountModifyParamsConfigurationMerchantCapabilitySwishPayment`, `v2.core.AccountModifyParamsConfigurationMerchantCapabilityTwintPayment`, `v2.core.AccountModifyParamsConfigurationMerchantCapabilityUsBankTransferPayment`, `v2.core.AccountModifyParamsConfigurationMerchantCapabilityZipPayment`, `v2.core.AccountModifyParamsConfigurationRecipientCapabilityBankAccountInstant`, `v2.core.AccountModifyParamsConfigurationRecipientCapabilityBankAccountLocal`, `v2.core.AccountModifyParamsConfigurationRecipientCapabilityBankAccountWire`, `v2.core.AccountModifyParamsConfigurationRecipientCapabilityCard`, `v2.core.AccountModifyParamsConfigurationRecipientCapabilityCryptoWallet`, `v2.core.AccountModifyParamsConfigurationRecipientCapabilityPaperCheck`, `v2.core.AccountModifyParamsConfigurationRecipientCapabilityStripeBalanceStripeTransfer`, `v2.core.AccountModifyParamsConfigurationStorerCapabilityConsumerHoldsCurrencyUsd`, `v2.core.AccountModifyParamsConfigurationStorerCapabilityFinancialAddressBankAccount`, `v2.core.AccountModifyParamsConfigurationStorerCapabilityFinancialAddressCryptoWallet`, `v2.core.AccountModifyParamsConfigurationStorerCapabilityHoldsCurrencyEur`, `v2.core.AccountModifyParamsConfigurationStorerCapabilityHoldsCurrencyGbp`, `v2.core.AccountModifyParamsConfigurationStorerCapabilityHoldsCurrencyUsd`, `v2.core.AccountModifyParamsConfigurationStorerCapabilityHoldsCurrencyUsdc`, `v2.core.AccountModifyParamsConfigurationStorerCapabilityInboundTransferBankAccount`, `v2.core.AccountModifyParamsConfigurationStorerCapabilityOutboundPaymentBankAccount`, `v2.core.AccountModifyParamsConfigurationStorerCapabilityOutboundPaymentCard`, `v2.core.AccountModifyParamsConfigurationStorerCapabilityOutboundPaymentCryptoWallet`, `v2.core.AccountModifyParamsConfigurationStorerCapabilityOutboundPaymentFinancialAccount`, `v2.core.AccountModifyParamsConfigurationStorerCapabilityOutboundPaymentPaperCheck`, `v2.core.AccountModifyParamsConfigurationStorerCapabilityOutboundTransferBankAccount`, `v2.core.AccountModifyParamsConfigurationStorerCapabilityOutboundTransferCryptoWallet`, and `v2.core.AccountModifyParamsConfigurationStorerCapabilityOutboundTransferFinancialAccount`

## 15.3.0a3 - 2026-06-10
This release changes the pinned API version to `2026-06-10.preview`.

* ⚠️ [#1827](https://github.com/stripe/stripe-python/pull/1827) Update generated code for private-preview
  * Add support for new resources `GiftCardOperation`, `GiftCard`, and `TaxFund`
  * Add support for `retrieve` method on resource `GiftCardOperation`
  * Add support for `activate`, `cashout`, `check_balance`, `create`, `reload`, `retrieve`, and `void_operation` methods on resource `GiftCard`
  * Add support for `list` and `retrieve` methods on resource `TaxFund`
  * Add support for `update_crypto_refund_address` method on resource `PaymentIntent`
  * Add support for `performance_location_details` on `Tax.CalculationLineItem`, `Tax.TransactionLineItem`, and `tax.CalculationCreateParamsLineItem`
  * ⚠️ Remove support for `money_services` on `ChargeCaptureParamsPaymentDetail`, `ChargeModifyParamsPaymentDetail`, and `PaymentIntentCaptureParamsPaymentDetail`
  * Add support for `fr_meal_voucher` on `Charge.PaymentMethodDetail.Card.Benefit`
  * Add support for `multicapture` on `Charge.PaymentMethodDetail.CardPresent`, `ConfirmationToken.PaymentMethodPreview.Card.GeneratedFrom.PaymentMethodDetail.CardPresent`, `PaymentAttemptRecord.PaymentMethodDetail.CardPresent`, `PaymentMethod.Card.GeneratedFrom.PaymentMethodDetail.CardPresent`, and `PaymentRecord.PaymentMethodDetail.CardPresent`
  * Add support for `pix` on `Checkout.Session.CurrentAttempt.PaymentMethodDetail`
  * ⚠️ Add support for new value `jaywan` on enum `Checkout.Session.CurrentAttempt.PaymentMethodDetail.Card.brand`
  * Add support for `provisional_credit` on `Issuing.Dispute` and `issuing.DisputeModifyParams`
  * Add support for `reason` on `PaymentAttemptRecordReportCanceledParams` and `PaymentRecordReportPaymentAttemptCanceledParams`
  * Add support for `fiserv_valuelink`, `givex`, and `svs` on `PaymentAttemptRecord.ProcessorDetail` and `PaymentRecord.ProcessorDetail`
  * ⚠️ Change type of `PaymentAttemptRecord.ProcessorDetail.type` and `PaymentRecord.ProcessorDetail.type` from `literal('custom')` to `enum('custom'|'fiserv_valuelink'|'givex'|'svs')`
  * Add support for `capture_by` and `capture_delay` on `PaymentIntent.PaymentMethodOption.CardPresent`, `PaymentIntent.PaymentMethodOption.Card`, `PaymentIntentConfirmParamsPaymentMethodOptionCardPresent`, `PaymentIntentConfirmParamsPaymentMethodOptionCard`, `PaymentIntentCreateParamsPaymentMethodOptionCardPresent`, `PaymentIntentCreateParamsPaymentMethodOptionCard`, `PaymentIntentModifyParamsPaymentMethodOptionCardPresent`, and `PaymentIntentModifyParamsPaymentMethodOptionCard`
  * ⚠️ Remove support for `liquid_asset` on `PaymentIntentConfirmParamsPaymentMethodOptionCardPaymentDetailMoneyServiceAccountFunding`, `PaymentIntentConfirmParamsPaymentMethodOptionCardPresentPaymentDetailMoneyServiceAccountFunding`, `PaymentIntentCreateParamsPaymentMethodOptionCardPaymentDetailMoneyServiceAccountFunding`, `PaymentIntentCreateParamsPaymentMethodOptionCardPresentPaymentDetailMoneyServiceAccountFunding`, `PaymentIntentModifyParamsPaymentMethodOptionCardPaymentDetailMoneyServiceAccountFunding`, and `PaymentIntentModifyParamsPaymentMethodOptionCardPresentPaymentDetailMoneyServiceAccountFunding`
  * Add support for `request_multicapture` on `PaymentIntent.PaymentMethodOption.CardPresent`, `PaymentIntentConfirmParamsPaymentMethodOptionCardPresent`, `PaymentIntentCreateParamsPaymentMethodOptionCardPresent`, and `PaymentIntentModifyParamsPaymentMethodOptionCardPresent`
  * Add support for new value `transaction_verification` on enums `PaymentIntentConfirmParamsPaymentMethodOptionCrypto.mode`, `PaymentIntentCreateParamsPaymentMethodOptionCrypto.mode`, and `PaymentIntentModifyParamsPaymentMethodOptionCrypto.mode`
  * Add support for `ignore_application_fee`, `ignore_transfer_data`, and `request_partial_authorization` on `PaymentIntentConfirmParamsPaymentMethodOptionGiftCard`, `PaymentIntentCreateParamsPaymentMethodOptionGiftCard`, and `PaymentIntentModifyParamsPaymentMethodOptionGiftCard`
  * Change `PaymentIntentConfirmParamsPaymentDetailBenefitFrMealVoucher.siret`, `PaymentIntentCreateParamsPaymentDetailBenefitFrMealVoucher.siret`, `PaymentIntentModifyParamsPaymentDetailBenefitFrMealVoucher.siret`, `SetupIntentConfirmParamsSetupDetailBenefitFrMealVoucher.siret`, `SetupIntentCreateParamsSetupDetailBenefitFrMealVoucher.siret`, and `SetupIntentModifyParamsSetupDetailBenefitFrMealVoucher.siret` to be optional
  * Add support for `latest_payment_attempt_record` and `payment_record` on `PaymentIntent`
  * ⚠️ Remove support for `reauthorization` and `reauthorize_before` on `PaymentIntent.AdvancedFeatureDetail`
  * Add support for `refund_address` on `PaymentIntent.NextAction.CryptoDisplayDetail.DepositAddress.Base`, `PaymentIntent.NextAction.CryptoDisplayDetail.DepositAddress.Solana`, and `PaymentIntent.NextAction.CryptoDisplayDetail.DepositAddress.Tempo`
  * Add support for `location` on `PaymentIntent.PaymentDetail` and `SetupIntent.SetupDetail`
  * ⚠️ Add support for new value `transaction_verification` on enum `PaymentIntent.PaymentMethodOption.Crypto.mode`
  * Add support for `data` on `radar.AccountEvaluationCreateParamsLoginInitiatedClientDeviceMetadataDetail`, `radar.AccountEvaluationCreateParamsRegistrationInitiatedClientDeviceMetadataDetail`, and `radar.CustomerEvaluationCreateParamsEvaluationContextClientDetail`
  * Change `radar.AccountEvaluationCreateParamsLoginInitiatedClientDeviceMetadataDetail.radar_session`, `radar.AccountEvaluationCreateParamsRegistrationInitiatedClientDeviceMetadataDetail.radar_session`, and `radar.CustomerEvaluationCreateParamsEvaluationContextClientDetail.radar_session` to be optional
  * ⚠️ Add support for new value `promotion` on enum `V2.Commerce.ProductCatalogImport.feed_type`
  * ⚠️ Change type of `V2.Core.FeeBatch.Adjustment.tax_adjustment` from `amount` to `an object`
  * ⚠️ Change type of `V2.Core.FeeBatch.CollectionRecord.Tax.amount`, `V2.Core.FeeBatch.CollectionRecord.amount`, `V2.Core.FeeBatch.Tax.amount`, `V2.Core.FeeBatch.amount`, `V2.Core.FeeEntry.Tax.amount`, and `V2.Core.FeeEntry.amount` from `amount` to `an object`
  * ⚠️ Add support for new value `tax_fund` on enums `V2.MoneyManagement.Transaction.category` and `V2.MoneyManagement.TransactionEntry.TransactionDetail.category`
  * Add support for `tax_fund` on `V2.MoneyManagement.Transaction.Flow` and `V2.MoneyManagement.TransactionEntry.TransactionDetail.Flow`
  * ⚠️ Add support for new value `tax_fund` on enums `V2.MoneyManagement.Transaction.Flow.type` and `V2.MoneyManagement.TransactionEntry.TransactionDetail.Flow.type`
  * Add support for new value `promotion` on enum `v2.commerce.ProductCatalogImportCreateParams.feed_type`
  * Add support for error code `default_us_bank_account_cannot_be_archived` on `CannotProceedError`

## 15.3.0a2 - 2026-06-03
This release changes the pinned API version to `2026-06-03.preview`.

* ⚠️ [#1818](https://github.com/stripe/stripe-python/pull/1818) Update generated code for private-preview
  * Add support for new resources `delegated_checkout.OrderEvent`, `delegated_checkout.Order`, `v2.billing.ContractLicensePricingQuantityChange`, `v2.billing.Contract`, and `v2.signals.AccountSignal`
  * Add support for `retrieve` method on resource `delegated_checkout.Order`
  * Add support for `list_orders` method on resource `delegated_checkout.RequestedSession`
  * Add support for `list` and `retrieve` methods on resource `v2.signals.AccountSignal`
  * Add support for `activate`, `cancel`, `create`, `list`, `modify`, and `retrieve` methods on resource `v2.billing.Contract`
  * Add support for `birth_address` on `AccountCreateParamsIndividual`, `AccountCreatePersonParams`, `AccountModifyParamsIndividual`, `AccountModifyPersonParams`, `Person`, `TokenCreateParamsAccountIndividual`, and `TokenCreateParamsPerson`
  * Change type of `ChargeCaptureParamsPaymentDetailMoneyService.transaction_type`, `ChargeModifyParamsPaymentDetailMoneyService.transaction_type`, `PaymentIntentCaptureParamsPaymentDetailMoneyService.transaction_type`, `PaymentIntentConfirmParamsPaymentDetailMoneyService.transaction_type`, `PaymentIntentCreateParamsPaymentDetailMoneyService.transaction_type`, and `PaymentIntentModifyParamsPaymentDetailMoneyService.transaction_type` from `literal('account_funding')` to `enum('account_funding'|'debt_repayment')`
  * ⚠️ Add support for new value `proserv` on enums `Checkout.Session.AutomaticSurcharge.provider` and `PaymentLink.AutomaticSurcharge.provider`
  * Add support for `provisioning_decision` and `token_type` on `Issuing.Authorization.TokenDetail` and `Issuing.Token`
  * Add support for `token_decision_recommendation` on `Issuing.Authorization.TokenDetail.NetworkDatum.Visa` and `Issuing.Token.NetworkDatum.Visa`
  * Add support for `language` on `Issuing.Token.NetworkDatum.Device`
  * Add support for `digital_asset_category` on `PaymentIntentConfirmParamsPaymentMethodOptionCardPaymentDetailMoneyServiceAccountFunding`, `PaymentIntentConfirmParamsPaymentMethodOptionCardPresentPaymentDetailMoneyServiceAccountFunding`, `PaymentIntentCreateParamsPaymentMethodOptionCardPaymentDetailMoneyServiceAccountFunding`, `PaymentIntentCreateParamsPaymentMethodOptionCardPresentPaymentDetailMoneyServiceAccountFunding`, `PaymentIntentModifyParamsPaymentMethodOptionCardPaymentDetailMoneyServiceAccountFunding`, and `PaymentIntentModifyParamsPaymentMethodOptionCardPresentPaymentDetailMoneyServiceAccountFunding`
  * Add support for `static_address` on `PaymentIntent.PaymentMethodOption.Crypto.DepositOption`, `PaymentIntentConfirmParamsPaymentMethodOptionCryptoDepositOption`, `PaymentIntentCreateParamsPaymentMethodOptionCryptoDepositOption`, and `PaymentIntentModifyParamsPaymentMethodOptionCryptoDepositOption`
  * Add support for `payment_reference` on `PaymentIntentCreateParamsPaymentsOrchestration`
  * ⚠️ Remove support for `payment_details` on `PaymentIntentCreateParamsPaymentsOrchestration`
  * ⚠️ Change type of `PaymentIntent.PaymentDetail.MoneyService.transaction_type` from `literal('account_funding')` to `enum('account_funding'|'debt_repayment')`
  * Add support for `ending_before`, `limit`, and `starting_after` on `PaymentLocationListParams`
  * ⚠️ Change `radar.IssuingAuthorizationEvaluationCreateParamsCardDetail.last4` to be required
  * Add support for `schema` on `V2.Data.Reporting.QueryRun.Result.File` and `V2.Reporting.ReportRun.Result.File`
  * ⚠️ Add support for new value `payout_method_amount_limit_exceeded` on enum `V2.MoneyManagement.OutboundPayment.StatusDetail.Failed.reason`
  * Add support for `include` on `v2.data.reporting.QueryRunRetrieveParams` and `v2.reporting.ReportRunRetrieveParams`
  * Add support for `requirements_collector` on `v2.core.AccountCreateParamsDefaultResponsibility` and `v2.core.AccountModifyParamsDefaultResponsibility`
  * Add support for event notification `V2SignalsAccountSignalMerchantDelinquencyReadyEvent` with related object `v2.signals.AccountSignal`

## 15.3.0a1 - 2026-05-27
This release changes the pinned API version to `2026-05-27.preview`.

* ⚠️ [#1815](https://github.com/stripe/stripe-python/pull/1815) Update generated code for private-preview
  * Change type of `billing.AlertCreateParamsSpendThreshold.group_by` from `literal('pricing_plan_subscription')` to `enum('billing_cadence'|'pricing_plan_subscription')`
  * ⚠️ Change type of `Billing.Alert.SpendThreshold.group_by` from `literal('pricing_plan_subscription')` to `enum('billing_cadence'|'pricing_plan_subscription')`
  * Change `DelegatedCheckout.RequestedSession.affiliate_attributions` to be required
  * ⚠️ Add support for new value `institution_requirement` on enum `FinancialConnections.Account.StatusDetail.Inactive.cause`
  * Add support for `wechat_pay` on `Invoice.PaymentSetting.PaymentMethodOption`, `InvoiceCreateParamsPaymentSettingPaymentMethodOption`, `InvoiceModifyParamsPaymentSettingPaymentMethodOption`, `QuotePreviewInvoice.PaymentSetting.PaymentMethodOption`, `Subscription.PaymentSetting.PaymentMethodOption`, `SubscriptionCreateParamsPaymentSettingPaymentMethodOption`, and `SubscriptionModifyParamsPaymentSettingPaymentMethodOption`
  * Add support for `gift_card` on `PaymentIntent.PaymentMethodOption`, `PaymentIntentConfirmParamsPaymentMethodOption`, `PaymentIntentCreateParamsPaymentMethodOption`, and `PaymentIntentModifyParamsPaymentMethodOption`
  * Add support for `payment_details` on `PaymentIntentCreateParamsPaymentsOrchestration`
  * Add support for `enabled` on `PaymentIntent.PaymentDetail.Benefit.FrMealVoucher` and `SetupIntent.SetupDetail.Benefit.FrMealVoucher`
  * ⚠️ Remove support for `login_failed`, `registration_failed`, `registration_success`, and `type` on `radar.CustomerEvaluationModifyParams`
  * ⚠️ Remove support for `latest_version` on `V2.Billing.LicenseFee`, `V2.Billing.PricingPlan`, and `V2.Billing.RateCard`
  * ⚠️ Remove support for `service_interval_count` and `service_interval` on `V2.Billing.LicenseFee` and `V2.Billing.RateCard`
  * Add support for `debit_agreement` on `V2.MoneyManagement.ReceivedCredit.StripeBalancePayment`
  * Add support for new value `chaps` on enum `v2.FinancialAddressCreditSimulationCreditParams.network`
  * Add support for `canonical_path` on `EventsV2CoreHealthTrafficVolumeDropFiringEvent.Impact` and `EventsV2CoreHealthTrafficVolumeDropResolvedEvent.Impact`
  * Add support for snapshot event `payment_intent.expired` with resource `PaymentIntent`
  * Add support for event notifications `V2CoreHealthElementsErrorFiringEvent`, `V2CoreHealthElementsErrorResolvedEvent`, `V2CoreHealthInvoiceCountDroppedFiringEvent`, and `V2CoreHealthInvoiceCountDroppedResolvedEvent`

## 15.2.0a6 - 2026-05-20
* [#1811](https://github.com/stripe/stripe-python/pull/1811) remove unnecessary cast
* ⚠️ [#1809](https://github.com/stripe/stripe-python/pull/1809) Update generated code for private-preview
  * Add support for new resource `PaymentLocationCapability`
  * Add support for `list`, `modify`, and `retrieve` methods on resource `PaymentLocationCapability`
  * Add support for `close` and `simulate_network_lifecycle_dispute_response` test helper methods on resource `issuing.Dispute`
  * Change type of `delegated_checkout.RequestedSessionModifyParamsDiscount.codes` from `array(string)` to `emptyable(array(string))`
  * ⚠️ Remove support for `credited_items` on `InvoiceItem.ProrationDetail`
  * Add support for `balance_response` on `Issuing.Authorization`
  * Add support for `payment_evaluations` on `PaymentAttemptRecordReportCanceledParams`, `PaymentAttemptRecordReportFailedParams`, `PaymentRecordReportPaymentAttemptCanceledParams`, `PaymentRecordReportPaymentAttemptFailedParams`, `PaymentRecordReportPaymentAttemptParamsFailed`, and `PaymentRecordReportPaymentParamsFailed`
  * Add support for `enabled` on `PaymentIntentConfirmParamsPaymentDetailBenefitFrMealVoucher`, `PaymentIntentCreateParamsPaymentDetailBenefitFrMealVoucher`, `PaymentIntentModifyParamsPaymentDetailBenefitFrMealVoucher`, `SetupIntentConfirmParamsSetupDetailBenefitFrMealVoucher`, `SetupIntentCreateParamsSetupDetailBenefitFrMealVoucher`, and `SetupIntentModifyParamsSetupDetailBenefitFrMealVoucher`
  * Add support for `advanced_feature_details` and `allowed_payment_method_types` on `PaymentIntent`
  * Change type of `PaymentLocationModifyParamsAddress.city` from `string` to `emptyable(string)`
  * Change type of `PaymentLocationModifyParamsAddress.line1` from `string` to `emptyable(string)`
  * Change type of `PaymentLocationModifyParamsAddress.line2` from `string` to `emptyable(string)`
  * Change type of `PaymentLocationModifyParamsAddress.postal_code` from `string` to `emptyable(string)`
  * Change type of `PaymentLocationModifyParamsAddress.state` from `string` to `emptyable(string)`
  * Change `SubscriptionPauseParams.type` to be optional
  * ⚠️ Remove support for `payment_behavior` on `SubscriptionResumeParams`
  * ⚠️ Remove support for `status_details` on `Subscription`

## 15.2.0a5 - 2026-05-13
* ⚠️ [#1807](https://github.com/stripe/stripe-python/pull/1807) Update generated code for private-preview
  * Add support for new resources `v2.core.FeeBatch`, `v2.core.FeeEntry`, `v2.money_management.DebitDispute`, and `v2.money_management.FinancialAccountStatement`
  * Add support for `simulate_network_lifecycle_pre_arbitration_response` and `simulate_network_lifecycle_pre_arbitration_submission` test helper methods on resource `issuing.Dispute`
  * Add support for `list` method on resource `PaymentLocation`
  * Add support for `list` and `retrieve` methods on resources `v2.core.FeeBatch`, `v2.core.FeeEntry`, and `v2.money_management.FinancialAccountStatement`
  * Add support for `create`, `list`, and `retrieve` methods on resource `v2.money_management.DebitDispute`
  * Add support for `discounts` on `DelegatedCheckout.RequestedSession`, `delegated_checkout.RequestedSessionCreateParams`, and `delegated_checkout.RequestedSessionModifyParams`
  * Add support for `amount_sale` on `DelegatedCheckout.RequestedSession.LineItemDetail` and `DelegatedCheckout.RequestedSession.TotalDetail`
  * Add support for `amount_discount` and `breakdown` on `DelegatedCheckout.RequestedSession.TotalDetail`
  * ⚠️ Remove support for `check_deposit_address` on `Invoice.PaymentSetting.PaymentMethodOption.CheckScan`, `InvoiceCreateParamsPaymentSettingPaymentMethodOptionCheckScan`, `InvoiceModifyParamsPaymentSettingPaymentMethodOptionCheckScan`, `QuotePreviewInvoice.PaymentSetting.PaymentMethodOption.CheckScan`, `Subscription.PaymentSetting.PaymentMethodOption.CheckScan`, `SubscriptionCreateParamsPaymentSettingPaymentMethodOptionCheckScan`, and `SubscriptionModifyParamsPaymentSettingPaymentMethodOptionCheckScan`
  * Add support for `payment_evaluations` on `PaymentAttemptRecordReportGuaranteedParams`, `PaymentRecordReportPaymentAttemptGuaranteedParams`, `PaymentRecordReportPaymentAttemptParamsGuaranteed`, and `PaymentRecordReportPaymentParamsGuaranteed`
  * Add support for `location` on `PaymentIntentConfirmParamsPaymentDetail`, `PaymentIntentCreateParamsPaymentDetail`, `PaymentIntentModifyParamsPaymentDetail`, `SetupIntentConfirmParamsSetupDetail`, `SetupIntentCreateParamsSetupDetail`, and `SetupIntentModifyParamsSetupDetail`
  * Add support for `onboarding_data_update_acknowledged` on `PaymentLocationModifyParams`
  * Change `PaymentLocationCreateParamsAddress.country` and `PaymentLocationModifyParamsAddress.country` to be optional
  * Add support for `customer` on `radar.CustomerEvaluationModifyParams`
  * Add support for `status` on `Radar.CustomerEvaluation` and `radar.CustomerEvaluationModifyParams`
  * Change `radar.CustomerEvaluationModifyParams.type` to be optional
  * Add support for `payment_behavior` on `SubscriptionResumeParams`
  * Add support for `dispute_details` on `V2.MoneyManagement.ReceivedDebit`
  * ⚠️ Add support for new value `debit_dispute` on enums `V2.MoneyManagement.Transaction.category` and `V2.MoneyManagement.TransactionEntry.TransactionDetail.category`
  * Add support for `debit_dispute` on `V2.MoneyManagement.Transaction.Flow` and `V2.MoneyManagement.TransactionEntry.TransactionDetail.Flow`
  * ⚠️ Add support for new value `debit_dispute` on enums `V2.MoneyManagement.Transaction.Flow.type` and `V2.MoneyManagement.TransactionEntry.TransactionDetail.Flow.type`
  * Add support for `payment_attempt_record` on `EventsV2PaymentsOffSessionPaymentAttemptFailedEvent` and `EventsV2PaymentsOffSessionPaymentFailedEvent`
  * Add support for event notifications `V2MoneyManagementFinancialAccountStatementCreatedEvent` and `V2MoneyManagementFinancialAccountStatementRestatedEvent` with related object `v2.money_management.FinancialAccountStatement`

## 15.2.0a4 - 2026-05-06
* [#1805](https://github.com/stripe/stripe-python/pull/1805) Add EventNotificationHandler (private preview)
* ⚠️ [#1804](https://github.com/stripe/stripe-python/pull/1804) Update generated code for private-preview
  * Add support for new resource `PaymentLocation`
  * Add support for `create`, `delete`, `modify`, and `retrieve` methods on resource `PaymentLocation`
  * Add support for `protections` on `AccountCreateParamsCapabilityCardPayment`, `AccountModifyParamsCapabilityCardPayment`, and `Capability`
  * Add support for `gift_card` on `ConfirmationToken.PaymentMethodPreview`, `ConfirmationTokenCreateParamsPaymentMethodDatum`, `PaymentIntentConfirmParamsPaymentMethodDatum`, `PaymentIntentCreateParamsPaymentMethodDatum`, `PaymentIntentModifyParamsPaymentMethodDatum`, `PaymentMethodCreateParams`, `PaymentMethod`, `SetupIntentConfirmParamsPaymentMethodDatum`, `SetupIntentCreateParamsPaymentMethodDatum`, `SetupIntentModifyParamsPaymentMethodDatum`, and `SharedPayment.GrantedToken.PaymentMethodDetail`
  * Add support for new value `gift_card` on enums `ConfirmationTokenCreateParamsPaymentMethodDatum.type`, `PaymentIntentConfirmParamsPaymentMethodDatum.type`, `PaymentIntentCreateParamsPaymentMethodDatum.type`, `PaymentIntentModifyParamsPaymentMethodDatum.type`, `SetupIntentConfirmParamsPaymentMethodDatum.type`, `SetupIntentCreateParamsPaymentMethodDatum.type`, and `SetupIntentModifyParamsPaymentMethodDatum.type`
  * ⚠️ Add support for new value `gift_card` on enums `ConfirmationToken.PaymentMethodPreview.type`, `PaymentMethod.type`, and `SharedPayment.GrantedToken.PaymentMethodDetail.type`
  * Add support for new value `gift_card` on enums `CustomerListPaymentMethodsParams.type`, `PaymentMethodCreateParams.type`, and `PaymentMethodListParams.type`
  * Add support for `metadata` on `delegated_checkout.RequestedSessionConfirmParams`
  * Add support for `credited_items` on `InvoiceItem.ProrationDetail`
  * Add support for `network_lifecycle` on `Issuing.Dispute`
  * Add support for new value `gift_card` on enums `PaymentIntentConfirmParams.excluded_payment_method_types`, `PaymentIntentCreateParams.excluded_payment_method_types`, `PaymentIntentModifyParams.excluded_payment_method_types`, `SetupIntentCreateParams.excluded_payment_method_types`, and `SetupIntentModifyParams.excluded_payment_method_types`
  * ⚠️ Add support for new value `gift_card` on enums `PaymentIntent.excluded_payment_method_types` and `SetupIntent.excluded_payment_method_types`
  * Add support for `status_details` on `Subscription`

## 15.2.0a3 - 2026-04-28
* ⚠️ [#1802](https://github.com/stripe/stripe-python/pull/1802) Update generated code for private-preview
  * Add support for `debit_card` on `V2.Core.Account.Configuration.CardCreator.Capability.Consumer.Lead`, `V2.Core.Account.Identity.Attestation.TermsOfService.CardCreator.Consumer.Lead`, `v2.core.AccountCreateParamsConfigurationCardCreatorCapabilityConsumerLead`, `v2.core.AccountCreateParamsIdentityAttestationTermsOfServiceCardCreatorConsumerLead`, `v2.core.AccountModifyParamsConfigurationCardCreatorCapabilityConsumerLead`, and `v2.core.AccountModifyParamsIdentityAttestationTermsOfServiceCardCreatorConsumerLead`
  * ⚠️ Add support for new value `consumer.lead.debit_card` on enums `V2.Core.Account.FutureRequirement.Entry.Impact.RestrictsCapability.capability` and `V2.Core.Account.Requirement.Entry.Impact.RestrictsCapability.capability`
  * ⚠️ Add support for new value `consumer.lead.debit_card` on enum `EventsV2CoreAccountIncludingConfigurationCardCreatorCapabilityStatusUpdatedEvent.updated_capability`

## 15.2.0a2 - 2026-04-28
* ⚠️ [#1800](https://github.com/stripe/stripe-python/pull/1800) Update generated code for private-preview
  * Add support for new resource `v2.data.analytics.MetricQueryResult`
  * Add support for `create`, `retrieve`, and `revoke` methods on resource `shared_payment.IssuedToken`
  * Add support for `create` method on resource `v2.data.analytics.MetricQueryResult`
  * Add support for `balance_report` and `payout_reconciliation_report` on `AccountSession.Component` and `AccountSessionCreateParamsComponent`
  * Add support for `app_distribution` and `sunbit_payments` on `Account.Capability`, `AccountCreateParamsCapability`, and `AccountModifyParamsCapability`
  * ⚠️ Add support for new values `fee_credit_funding`, `inbound_transfer_reversal`, and `inbound_transfer` on enum `BalanceTransaction.type`
  * Add support for `sunbit` on `Charge.PaymentMethodDetail`, `ConfirmationToken.PaymentMethodPreview`, `ConfirmationTokenCreateParamsPaymentMethodDatum`, `PaymentAttemptRecord.PaymentMethodDetail`, `PaymentIntentConfirmParamsPaymentMethodDatum`, `PaymentIntentCreateParamsPaymentMethodDatum`, `PaymentIntentModifyParamsPaymentMethodDatum`, `PaymentMethodConfigurationCreateParams`, `PaymentMethodConfigurationModifyParams`, `PaymentMethodConfiguration`, `PaymentMethodCreateParams`, `PaymentMethod`, `PaymentRecord.PaymentMethodDetail`, `SetupIntentConfirmParamsPaymentMethodDatum`, `SetupIntentCreateParamsPaymentMethodDatum`, and `SetupIntentModifyParamsPaymentMethodDatum`
  * ⚠️ Add support for new values `phantom_cash` and `usdt` on enums `Charge.PaymentMethodDetail.Crypto.token_currency`, `PaymentAttemptRecord.PaymentMethodDetail.Crypto.token_currency`, and `PaymentRecord.PaymentMethodDetail.Crypto.token_currency`
  * Add support for `last4` on `Charge.PaymentMethodDetail.GiftCard`, `PaymentAttemptRecord.PaymentMethodDetail.GiftCard`, and `PaymentRecord.PaymentMethodDetail.GiftCard`
  * Add support for `location` and `reader` on `Charge.PaymentMethodDetail.Klarna`, `PaymentAttemptRecord.PaymentMethodDetail.Klarna`, and `PaymentRecord.PaymentMethodDetail.Klarna`
  * Add support for new value `sunbit` on enum `checkout.SessionCreateParams.excluded_payment_method_types`
  * Add support for `blik` on `Invoice.PaymentSetting.PaymentMethodOption`, `InvoiceCreateParamsPaymentSettingPaymentMethodOption`, `InvoiceModifyParamsPaymentSettingPaymentMethodOption`, `QuotePreviewInvoice.PaymentSetting.PaymentMethodOption`, `Subscription.PaymentSetting.PaymentMethodOption`, `SubscriptionCreateParamsPaymentSettingPaymentMethodOption`, `SubscriptionModifyParamsPaymentSettingPaymentMethodOption`, and `checkout.SessionCreateParamsPaymentMethodOption`
  * Add support for new value `sunbit` on enum `checkout.SessionCreateParams.payment_method_types`
  * ⚠️ Add support for new values `fo_vat`, `gi_tin`, `it_cf`, and `py_ruc` on enums `Checkout.Session.CollectedInformation.TaxId.type`, `Checkout.Session.CustomerDetail.TaxId.type`, `Invoice.CustomerTaxId.type`, `Order.TaxDetail.TaxId.type`, `QuotePreviewInvoice.CustomerTaxId.type`, `Tax.Calculation.CustomerDetail.TaxId.type`, `Tax.Transaction.CustomerDetail.TaxId.type`, and `TaxId.type`
  * Change `Checkout.Session.managed_payments`, `PaymentIntent.managed_payments`, `PaymentLink.managed_payments`, and `Subscription.managed_payments` to be required
  * Add support for `shared_payment_granted_token` on `ConfirmationTokenCreateParamsPaymentMethodDatum`, `PaymentIntentConfirmParamsPaymentMethodDatum`, `PaymentIntentCreateParamsPaymentMethodDatum`, `PaymentIntentModifyParamsPaymentMethodDatum`, `PaymentMethod`, `SetupIntentConfirmParamsPaymentMethodDatum`, `SetupIntentCreateParamsPaymentMethodDatum`, and `SetupIntentModifyParamsPaymentMethodDatum`
  * Add support for new value `sunbit` on enums `ConfirmationTokenCreateParamsPaymentMethodDatum.type`, `PaymentIntentConfirmParamsPaymentMethodDatum.type`, `PaymentIntentCreateParamsPaymentMethodDatum.type`, `PaymentIntentModifyParamsPaymentMethodDatum.type`, `SetupIntentConfirmParamsPaymentMethodDatum.type`, `SetupIntentCreateParamsPaymentMethodDatum.type`, and `SetupIntentModifyParamsPaymentMethodDatum.type`
  * ⚠️ Add support for new value `sunbit` on enums `ConfirmationToken.PaymentMethodPreview.type` and `PaymentMethod.type`
  * ⚠️ Change type of `CreditNote.TotalTax.TaxRateDetail.tax_rate`, `CreditNoteLineItem.Tax.TaxRateDetail.tax_rate`, `Invoice.TotalTax.TaxRateDetail.tax_rate`, `InvoiceLineItem.Tax.TaxRateDetail.tax_rate`, and `QuotePreviewInvoice.TotalTax.TaxRateDetail.tax_rate` from `string` to `expandable($TaxRate)`
  * Add support for new values `fo_vat`, `gi_tin`, `it_cf`, and `py_ruc` on enums `CustomerCreateParamsTaxIdDatum.type`, `CustomerCreateTaxIdParams.type`, `InvoiceCreatePreviewParamsCustomerDetailTaxId.type`, `OrderCreateParamsTaxDetailTaxId.type`, `OrderModifyParamsTaxDetailTaxId.type`, `TaxIdCreateParams.type`, and `tax.CalculationCreateParamsCustomerDetailTaxId.type`
  * Add support for new value `sunbit` on enums `CustomerListPaymentMethodsParams.type`, `PaymentMethodCreateParams.type`, and `PaymentMethodListParams.type`
  * Add support for `buyer_consents` on `delegated_checkout.RequestedSessionConfirmParams`
  * Add support for `consents` on `DelegatedCheckout.RequestedSession.BuyerConsent.Marketing`
  * Add support for new value `blik` on enums `InvoiceCreateParamsPaymentSetting.payment_method_types`, `InvoiceModifyParamsPaymentSetting.payment_method_types`, `SubscriptionCreateParamsPaymentSetting.payment_method_types`, and `SubscriptionModifyParamsPaymentSetting.payment_method_types`
  * ⚠️ Add support for new value `blik` on enums `Invoice.PaymentSetting.payment_method_types`, `QuotePreviewInvoice.PaymentSetting.payment_method_types`, and `Subscription.PaymentSetting.payment_method_types`
  * Change `Invoice.PaymentSetting.PaymentMethodOption.pix`, `QuotePreviewInvoice.PaymentSetting.PaymentMethodOption.pix`, and `Subscription.PaymentSetting.PaymentMethodOption.pix` to be required
  * Change `Invoice.PaymentSetting.PaymentMethodOption.upi`, `QuotePreviewInvoice.PaymentSetting.PaymentMethodOption.upi`, and `Subscription.PaymentSetting.PaymentMethodOption.upi` to be required
  * Add support for `payment_facilitator_id` and `sub_merchant_id` on `issuing.AuthorizationCreateParamsMerchantDatum`, `issuing.TransactionCreateForceCaptureParamsMerchantDatum`, and `issuing.TransactionCreateUnlinkedRefundParamsMerchantDatum`
  * Add support for `card_presence` on `Issuing.Authorization`
  * Add support for `allowed_card_presences` and `blocked_card_presences` on `Issuing.Card.SpendingControl`, `Issuing.Cardholder.SpendingControl`, `issuing.CardCreateParamsSpendingControl`, `issuing.CardModifyParamsSpendingControl`, `issuing.CardholderCreateParamsSpendingControl`, and `issuing.CardholderModifyParamsSpendingControl`
  * ⚠️ Add support for new value `fulfillment_error` on enum `Issuing.Card.cancellation_reason`
  * ⚠️ Add support for new value `fulfillment_error` on enum `Issuing.Card.replacement_reason`
  * ⚠️ Change type of `PaymentAttemptRecord.PaymentMethodDetail.GiftCard.balance` and `PaymentRecord.PaymentMethodDetail.GiftCard.balance` from `PaymentFlowsPrivatePaymentMethodsGiftCardDeprecatedDetailsResourceBalanceAmount` to `nullable(PaymentsPrimitivesPaymentRecordsResourcePaymentMethodGiftCardDetailsResourceBalance)`
  * ⚠️ Change type of `PaymentAttemptRecord.PaymentMethodDetail.GiftCard.brand` and `PaymentRecord.PaymentMethodDetail.GiftCard.brand` from `enum('fiserv_valuelink'|'givex'|'svs')` to `nullable(enum('fiserv_valuelink'|'givex'|'svs'))`
  * ⚠️ Change type of `PaymentAttemptRecord.PaymentMethodDetail.GiftCard.first6` and `PaymentRecord.PaymentMethodDetail.GiftCard.first6` from `string` to `nullable(string)`
  * ⚠️ Change type of `PaymentAttemptRecord.PaymentMethodDetail.GiftCard.transaction_id` and `PaymentRecord.PaymentMethodDetail.GiftCard.transaction_id` from `string` to `nullable(string)`
  * Add support for new value `sunbit` on enums `PaymentIntentConfirmParams.excluded_payment_method_types`, `PaymentIntentCreateParams.excluded_payment_method_types`, `PaymentIntentModifyParams.excluded_payment_method_types`, `SetupIntentCreateParams.excluded_payment_method_types`, and `SetupIntentModifyParams.excluded_payment_method_types`
  * Add support for `amount_to_confirm` on `PaymentIntentConfirmParams`
  * ⚠️ Add support for new value `sunbit` on enums `PaymentIntent.excluded_payment_method_types` and `SetupIntent.excluded_payment_method_types`
  * Add support for `klarna_display_qr_code` on `PaymentIntent.NextAction`
  * Add support for new value `sunbit` on enums `PaymentLinkCreateParams.payment_method_types` and `PaymentLinkModifyParams.payment_method_types`
  * ⚠️ Add support for new value `sunbit` on enum `PaymentLink.payment_method_types`
  * Add support for `validation_errors` on `Privacy.RedactionJob`
  * Add support for `tax_details` on `Product`
  * ⚠️ Change type of `Radar.PaymentEvaluation.ClientDeviceMetadataDetail.radar_session` from `string` to `nullable(string)`
  * ⚠️ Add support for new values `low`, `not_assessed`, and `unknown` on enum `Radar.PaymentEvaluation.Signal.FraudulentPayment.risk_level`
  * Add support for new value `account` on enum `radar.ValueListCreateParams.item_type`
  * ⚠️ Add support for new value `account` on enum `Radar.ValueList.item_type`
  * Add support for `moto` on `SetupAttempt.PaymentMethodDetail.Card`
  * Change `SetupIntent.NextAction.PixDisplayQrCode.data` to be required
  * Change `SetupIntent.NextAction.PixDisplayQrCode.expires_at` to be required
  * Change `SetupIntent.NextAction.PixDisplayQrCode.hosted_instructions_url` to be required
  * Change `SetupIntent.NextAction.PixDisplayQrCode.image_url_png` to be required
  * Change `SetupIntent.NextAction.PixDisplayQrCode.image_url_svg` to be required
  * Add support for `admissions_tax`, `attendance_tax`, `entertainment_tax`, `gross_receipts_tax`, `hospitality_tax`, `luxury_tax`, `resort_tax`, and `tourism_tax` on `tax.RegistrationCreateParamsCountryOptionMe`
  * Add support for `purpose` on `Treasury.OutboundPayment` and `treasury.OutboundPaymentCreateParams`
  * Add support for new value `2026-04-22.dahlia` on enum `WebhookEndpointCreateParams.api_version`
  * Add support for `crypto_wallet` on `V2.MoneyManagement.FinancialAddress.Credential`
  * Add support for `mx_bank_account` on `V2.MoneyManagement.FinancialAddress.Credential` and `V2.MoneyManagement.ReceivedCredit.BankTransfer`
  * ⚠️ Add support for new values `crypto_wallet` and `mx_bank_account` on enum `V2.MoneyManagement.FinancialAddress.Credential.type`
  * Add support for `crypto_wallet_transfer` on `V2.MoneyManagement.ReceivedCredit`
  * Add support for `eu_bank_account` on `V2.MoneyManagement.ReceivedCredit.BankTransfer`
  * ⚠️ Add support for new values `crypto_wallet`, `eu_bank_account`, and `mx_bank_account` on enum `V2.MoneyManagement.ReceivedCredit.BankTransfer.origin_type`
  * ⚠️ Add support for new value `crypto_wallet_transfer` on enum `V2.MoneyManagement.ReceivedCredit.type`
  * Change `v2.payments.OffSessionPaymentCaptureParams.metadata` and `v2.payments.OffSessionPaymentCreateParams.metadata` to be optional
  * Add support for `crypto_properties` and `settlement_currency` on `v2.money_management.FinancialAddressCreateParams`
  * Add support for new values `crypto_wallet` and `mx_bank_account` on enum `v2.money_management.FinancialAddressCreateParams.type`
  * Add support for event notifications `V2CoreApprovalRequestCreatedEvent` and `V2CoreApprovalRequestExpiredEvent` with related object `v2.core.ApprovalRequest`
  * Add support for event notification `V2ExtendExtensionRunFailedEvent`
  * Add support for error codes `action_blocked` and `approval_required` on `Invoice.LastFinalizationError`, `PaymentIntent.LastPaymentError`, `QuotePreviewInvoice.LastFinalizationError`, `SetupAttempt.SetupError`, `SetupIntent.LastSetupError`, and `StripeError`

## 15.2.0a1 - 2026-04-24
This release changes the pinned API version to `2026-04-22.preview`.

* ⚠️ [#1795](https://github.com/stripe/stripe-python/pull/1795) Update generated code for private-preview
  * Add support for new resources `v2.commerce.ProductCatalogImport`, `v2.core.ApprovalRequest`, `v2.extend.WorkflowRun`, `v2.extend.Workflow`, `v2.iam.ActivityLog`, `v2.network.BusinessProfile`, and `v2.orchestrated_commerce.Agreement`
  * ⚠️ Remove support for resources `v2.core.WorkflowRun` and `v2.core.Workflow`
  * Add support for `confirm`, `create`, `list`, `retrieve`, and `terminate` methods on resource `v2.orchestrated_commerce.Agreement`
  * Add support for `me` and `retrieve` methods on resource `v2.network.BusinessProfile`
  * Add support for `list` method on resource `v2.iam.ActivityLog`
  * Add support for `list` and `retrieve` methods on resource `v2.extend.WorkflowRun`
  * Add support for `invoke`, `list`, and `retrieve` methods on resource `v2.extend.Workflow`
  * Add support for `cancel`, `execute`, `list`, `retrieve`, and `submit` methods on resource `v2.core.ApprovalRequest`
  * Add support for `create` and `retrieve` methods on resource `v2.commerce.ProductCatalogImport`
  * ⚠️ Remove support for `list` and `retrieve` methods on resource `v2.core.WorkflowRun`
  * ⚠️ Remove support for `invoke`, `list`, and `retrieve` methods on resource `v2.core.Workflow`
  * Add support for `renew_onboarding_link` method on resource `v2.core.ClaimableSandbox`
  * ⚠️ Remove support for `customer` on `SharedPayment.IssuedToken`
  * Change type of `SharedPayment.IssuedToken.payment_method` from `nullable(string)` to `string`
  * Add support for `bill_management` and `send_money` on `AccountSession.Component.Bill.Feature`
  * Add support for `gift_card` on `Charge.PaymentMethodDetail`, `PaymentAttemptRecord.PaymentMethodDetail`, and `PaymentRecord.PaymentMethodDetail`
  * Add support for `custom_payment_method_types` on `Checkout.Session` and `checkout.SessionCreateParams`
  * Add support for `payment_record` on `Checkout.Session`
  * ⚠️ Remove support for `shared_payment_granted_token` on `ConfirmationTokenCreateParamsPaymentMethodDatum`, `PaymentIntentConfirmParamsPaymentMethodDatum`, `PaymentIntentCreateParamsPaymentMethodDatum`, `PaymentIntentModifyParamsPaymentMethodDatum`, `PaymentIntent`, `PaymentMethod`, `SetupIntentConfirmParamsPaymentMethodDatum`, `SetupIntentCreateParamsPaymentMethodDatum`, and `SetupIntentModifyParamsPaymentMethodDatum`
  * Add support for `payment_method` on `ConfirmationToken.PaymentMethodPreview.SepaDebit.GeneratedFrom`, `PaymentMethod.SepaDebit.GeneratedFrom`, and `SharedPayment.GrantedToken.PaymentMethodDetail.SepaDebit.GeneratedFrom`
  * ⚠️ Change type of `DelegatedCheckout.RequestedSession.FulfillmentDetail.FulfillmentOption.type`, `DelegatedCheckout.RequestedSession.FulfillmentDetail.SelectedFulfillmentOption.type`, `DelegatedCheckout.RequestedSession.FulfillmentDetail.SelectedFulfillmentOptionOverride.type`, `delegated_checkout.RequestedSessionModifyParamsFulfillmentDetailSelectedFulfillmentOption.type`, and `delegated_checkout.RequestedSessionModifyParamsFulfillmentDetailSelectedFulfillmentOptionOverride.type` from `string` to `enum('digital'|'shipping')`
  * Add support for `return_url` on `delegated_checkout.RequestedSessionConfirmParams`
  * Add support for `buyer_consents` on `DelegatedCheckout.RequestedSession`
  * Add support for `crypto_transactions` on `Issuing.Authorization`, `Issuing.Dispute`, and `Issuing.Transaction`
  * Add support for `payment_facilitator_id` and `sub_merchant_id` on `Issuing.Authorization.MerchantDatum` and `Issuing.Transaction.MerchantDatum`
  * Add support for `identifiers` on `OrderCreateParamsLineItemProductDatum`, `OrderModifyParamsLineItemProductDatum`, `ProductCreateParams`, `ProductModifyParams`, and `Product`
  * Add support for `agent_details` on `PaymentIntent`
  * Add support for `external_reference` on `PriceCreateParams` and `PriceModifyParams`
  * Add support for `login_succeeded` and `registration_succeeded` on `Radar.AccountEvaluation.Event` and `radar.AccountEvaluationModifyParams`
  * Add support for `print_content` on `Terminal.Reader.Action`
  * ⚠️ Add support for new value `print_content` on enum `Terminal.Reader.Action.type`
  * ⚠️ Add support for new values `cn_bank_account` and `jp_bank_account` on enum `V2.Core.Account.Configuration.Recipient.DefaultOutboundDestination.type`
  * ⚠️ Add support for new values `bm_crn`, `bo_tin`, `bt_tpn`, `co_nit`, `ec_ruc`, `eg_tin`, `gh_tin`, `gy_tin`, `hn_rtn`, `jm_trn`, `jo_crn`, `ke_pin`, `ky_crn`, `lk_tin`, `mo_tin`, `mv_tin`, `ng_tin`, `pa_ruc`, `ph_tin`, `py_ruc`, `sl_tin`, `sv_nit`, `uy_ruc`, `vg_cn`, and `za_tin` on enum `V2.Core.Account.Identity.BusinessDetail.IdNumber.type`
  * ⚠️ Add support for new values `bm_pp`, `bo_ci`, `bt_cid`, `eg_tin`, `gh_pin`, `gy_tin`, `hn_rtn`, `jm_trn`, `jo_pin`, `ky_pp`, `lk_nic`, `mo_bir`, `mt_nic`, `mv_tin`, `pa_ruc`, `ph_tin`, `py_ruc`, `si_pin`, `sv_nit`, and `vg_pp` on enums `V2.Core.Account.Identity.Individual.IdNumber.type` and `V2.Core.AccountPerson.IdNumber.type`
  * Add support for `app_channel` on `V2.Core.ClaimableSandbox` and `v2.core.ClaimableSandboxCreateParams`
  * Add support for `onboarding_link_details` and `owner_details` on `V2.Core.ClaimableSandbox`
  * ⚠️ Remove support for `claim_url` on `V2.Core.ClaimableSandbox`
  * ⚠️ Remove support for `owner_account` on `V2.Core.ClaimableSandbox.SandboxDetail`
  * ⚠️ Add support for new value `live` on enum `V2.Core.ClaimableSandbox.status`
  * Add support for `snapshot_event` on `V2.Core.Event`
  * ⚠️ Add support for new values `futsu` and `toza` on enums `V2.Core.Vault.GbBankAccount.bank_account_type` and `V2.MoneyManagement.PayoutMethod.BankAccount.bank_account_type`
  * ⚠️ Change `V2.MoneyManagement.CurrencyConversion.financial_account` to be optional
  * Add support for `multiprocessor_settlement` on `V2.MoneyManagement.FinancialAccount`
  * ⚠️ Add support for new value `multiprocessor_settlement` on enum `V2.MoneyManagement.FinancialAccount.type`
  * Add support for `ca_bank_account` on `V2.MoneyManagement.FinancialAddress.Credential` and `V2.MoneyManagement.ReceivedCredit.BankTransfer`
  * ⚠️ Add support for new value `ca_bank_account` on enum `V2.MoneyManagement.FinancialAddress.Credential.type`
  * ⚠️ Add support for new value `tempo` on enum `V2.MoneyManagement.PayoutMethod.CryptoWallet.network`
  * ⚠️ Add support for new value `ca_bank_account` on enum `V2.MoneyManagement.ReceivedCredit.BankTransfer.origin_type`
  * ⚠️ Remove support for value `return` from enums `V2.MoneyManagement.Transaction.category` and `V2.MoneyManagement.TransactionEntry.TransactionDetail.category`
  * Add support for `amount_details` and `payment_details` on `V2.Payments.OffSessionPayment`, `v2.payments.OffSessionPaymentCaptureParams`, and `v2.payments.OffSessionPaymentCreateParams`
  * Add support for `description` on `V2.Payments.OffSessionPayment` and `v2.payments.OffSessionPaymentCreateParams`
  * Add support for new value `acss` on enum `v2.FinancialAddressCreditSimulationCreditParams.network`
  * Add support for `mcc` on `v2.payments.OffSessionPaymentCreateParamsPaymentMethodOptionCard`
  * Change `v2.payments.OffSessionPaymentCreateParamsPaymentMethodOptionCard.network_transaction_id` to be optional
  * Add support for new values `futsu` and `toza` on enums `v2.core.vault.GbBankAccountCreateParams.bank_account_type`, `v2.money_management.OutboundSetupIntentCreateParamsPayoutMethodDatumBankAccount.bank_account_type`, and `v2.money_management.OutboundSetupIntentModifyParamsPayoutMethodDatumBankAccount.bank_account_type`
  * Add support for new value `tempo` on enum `v2.money_management.OutboundSetupIntentCreateParamsPayoutMethodDatumCryptoWallet.network`
  * Add support for new value `credentials.ca_bank_account.account_number` on enums `v2.money_management.FinancialAddressListParams.include` and `v2.money_management.FinancialAddressRetrieveParams.include`
  * Add support for new value `ca_bank_account` on enum `v2.money_management.FinancialAddressCreateParams.type`
  * Add support for new value `multiprocessor_settlement` on enum `v2.money_management.FinancialAccountListParams.types`
  * Add support for `storage` on `v2.money_management.FinancialAccountModifyParams`
  * Add support for `fx_quote` on `v2.money_management.CurrencyConversionCreateParams`
  * Change `v2.money_management.CurrencyConversionCreateParams.financial_account` to be optional
  * ⚠️ Add support for `onboarding_link_details` on `v2.core.ClaimableSandboxCreateParams`
  * Change type of `v2.core.BatchJobCreateParamsEndpoint.http_method` from `literal('post')` to `enum('delete'|'post')`
  * Add support for new values `bm_crn`, `bo_tin`, `bt_tpn`, `co_nit`, `ec_ruc`, `eg_tin`, `gh_tin`, `gy_tin`, `hn_rtn`, `jm_trn`, `jo_crn`, `ke_pin`, `ky_crn`, `lk_tin`, `mo_tin`, `mv_tin`, `ng_tin`, `pa_ruc`, `ph_tin`, `py_ruc`, `sl_tin`, `sv_nit`, `uy_ruc`, `vg_cn`, and `za_tin` on enums `v2.core.AccountCreateParamsIdentityBusinessDetailIdNumber.type`, `v2.core.AccountModifyParamsIdentityBusinessDetailIdNumber.type`, and `v2.core.AccountTokenCreateParamsIdentityBusinessDetailIdNumber.type`
  * Add support for new values `bm_pp`, `bo_ci`, `bt_cid`, `eg_tin`, `gh_pin`, `gy_tin`, `hn_rtn`, `jm_trn`, `jo_pin`, `ky_pp`, `lk_nic`, `mo_bir`, `mt_nic`, `mv_tin`, `pa_ruc`, `ph_tin`, `py_ruc`, `si_pin`, `sv_nit`, and `vg_pp` on enums `v2.core.AccountCreateParamsIdentityIndividualIdNumber.type`, `v2.core.AccountModifyParamsIdentityIndividualIdNumber.type`, `v2.core.AccountPersonCreateParamsIdNumber.type`, `v2.core.AccountPersonModifyParamsIdNumber.type`, `v2.core.AccountPersonTokenCreateParamsIdNumber.type`, and `v2.core.AccountTokenCreateParamsIdentityIndividualIdNumber.type`
  * ⚠️ Add support for new value `meter_event_value_too_many_digits` on enums `EventsV1BillingMeterErrorReportTriggeredEvent.Reason.ErrorType.code` and `EventsV1BillingMeterNoMeterFoundEvent.Reason.ErrorType.code`
  * Add support for `treasury_transaction` on `EventsV2MoneyManagementTransactionCreatedEvent`
  * Add support for event notifications `V1AccountApplicationAuthorizedEvent`, `V1AccountApplicationDeauthorizedEvent`, `V1AccountExternalAccountCreatedEvent`, `V1AccountExternalAccountDeletedEvent`, `V1AccountExternalAccountUpdatedEvent`, `V1BillingPortalSessionCreatedEvent`, `V1EntitlementsActiveEntitlementSummaryUpdatedEvent`, `V2CoreHealthMeterEventSummariesDelayedFiringEvent`, and `V2CoreHealthMeterEventSummariesDelayedResolvedEvent`
  * Add support for event notification `V1AccountUpdatedEvent` with related object `Account`
  * Add support for event notifications `V1ApplicationFeeCreatedEvent` and `V1ApplicationFeeRefundedEvent` with related object `ApplicationFee`
  * Add support for event notification `V1ApplicationFeeRefundUpdatedEvent` with related object `ApplicationFeeRefund`
  * Add support for event notification `V1BalanceAvailableEvent` with related object `Balance`
  * Add support for event notification `V1BillingAlertTriggeredEvent` with related object `billing.Alert`
  * Add support for event notifications `V1BillingPortalConfigurationCreatedEvent` and `V1BillingPortalConfigurationUpdatedEvent` with related object `billing_portal.Configuration`
  * Add support for event notification `V1CapabilityUpdatedEvent` with related object `Capability`
  * Add support for event notification `V1CashBalanceFundsAvailableEvent` with related object `CashBalance`
  * Add support for event notifications `V1ChargeCapturedEvent`, `V1ChargeExpiredEvent`, `V1ChargeFailedEvent`, `V1ChargePendingEvent`, `V1ChargeRefundedEvent`, `V1ChargeSucceededEvent`, and `V1ChargeUpdatedEvent` with related object `Charge`
  * Add support for event notifications `V1ChargeDisputeClosedEvent`, `V1ChargeDisputeCreatedEvent`, `V1ChargeDisputeFundsReinstatedEvent`, `V1ChargeDisputeFundsWithdrawnEvent`, and `V1ChargeDisputeUpdatedEvent` with related object `Dispute`
  * Add support for event notifications `V1ChargeRefundUpdatedEvent`, `V1RefundCreatedEvent`, `V1RefundFailedEvent`, and `V1RefundUpdatedEvent` with related object `Refund`
  * Add support for event notifications `V1CheckoutSessionAsyncPaymentFailedEvent`, `V1CheckoutSessionAsyncPaymentSucceededEvent`, `V1CheckoutSessionCompletedEvent`, and `V1CheckoutSessionExpiredEvent` with related object `checkout.Session`
  * Add support for event notifications `V1ClimateOrderCanceledEvent`, `V1ClimateOrderCreatedEvent`, `V1ClimateOrderDelayedEvent`, `V1ClimateOrderDeliveredEvent`, and `V1ClimateOrderProductSubstitutedEvent` with related object `climate.Order`
  * Add support for event notifications `V1ClimateProductCreatedEvent` and `V1ClimateProductPricingUpdatedEvent` with related object `climate.Product`
  * Add support for event notifications `V1CouponCreatedEvent`, `V1CouponDeletedEvent`, and `V1CouponUpdatedEvent` with related object `Coupon`
  * Add support for event notifications `V1CreditNoteCreatedEvent`, `V1CreditNoteUpdatedEvent`, and `V1CreditNoteVoidedEvent` with related object `CreditNote`
  * Add support for event notifications `V1CustomerCreatedEvent`, `V1CustomerDeletedEvent`, and `V1CustomerUpdatedEvent` with related object `Customer`
  * Add support for event notifications `V1CustomerSubscriptionCreatedEvent`, `V1CustomerSubscriptionDeletedEvent`, `V1CustomerSubscriptionPausedEvent`, `V1CustomerSubscriptionPendingUpdateAppliedEvent`, `V1CustomerSubscriptionPendingUpdateExpiredEvent`, `V1CustomerSubscriptionResumedEvent`, `V1CustomerSubscriptionTrialWillEndEvent`, and `V1CustomerSubscriptionUpdatedEvent` with related object `Subscription`
  * Add support for event notifications `V1CustomerTaxIdCreatedEvent`, `V1CustomerTaxIdDeletedEvent`, and `V1CustomerTaxIdUpdatedEvent` with related object `TaxId`
  * Add support for event notification `V1CustomerCashBalanceTransactionCreatedEvent` with related object `CustomerCashBalanceTransaction`
  * Add support for event notification `V1FileCreatedEvent` with related object `File`
  * Add support for event notifications `V1FinancialConnectionsAccountCreatedEvent`, `V1FinancialConnectionsAccountDeactivatedEvent`, `V1FinancialConnectionsAccountDisconnectedEvent`, `V1FinancialConnectionsAccountReactivatedEvent`, `V1FinancialConnectionsAccountRefreshedBalanceEvent`, `V1FinancialConnectionsAccountRefreshedOwnershipEvent`, and `V1FinancialConnectionsAccountRefreshedTransactionsEvent` with related object `financial_connections.Account`
  * Add support for event notifications `V1IdentityVerificationSessionCanceledEvent`, `V1IdentityVerificationSessionCreatedEvent`, `V1IdentityVerificationSessionProcessingEvent`, `V1IdentityVerificationSessionRedactedEvent`, `V1IdentityVerificationSessionRequiresInputEvent`, and `V1IdentityVerificationSessionVerifiedEvent` with related object `identity.VerificationSession`
  * Add support for event notifications `V1InvoiceCreatedEvent`, `V1InvoiceDeletedEvent`, `V1InvoiceFinalizationFailedEvent`, `V1InvoiceFinalizedEvent`, `V1InvoiceMarkedUncollectibleEvent`, `V1InvoiceOverdueEvent`, `V1InvoiceOverpaidEvent`, `V1InvoicePaidEvent`, `V1InvoicePaymentActionRequiredEvent`, `V1InvoicePaymentFailedEvent`, `V1InvoicePaymentSucceededEvent`, `V1InvoiceSentEvent`, `V1InvoiceUpcomingEvent`, `V1InvoiceUpdatedEvent`, `V1InvoiceVoidedEvent`, and `V1InvoiceWillBeDueEvent` with related object `Invoice`
  * Add support for event notification `V1InvoicePaymentPaidEvent` with related object `InvoicePayment`
  * Add support for event notifications `V1InvoiceitemCreatedEvent` and `V1InvoiceitemDeletedEvent` with related object `InvoiceItem`
  * Add support for event notifications `V1IssuingAuthorizationCreatedEvent`, `V1IssuingAuthorizationRequestEvent`, and `V1IssuingAuthorizationUpdatedEvent` with related object `issuing.Authorization`
  * Add support for event notifications `V1IssuingCardCreatedEvent` and `V1IssuingCardUpdatedEvent` with related object `issuing.Card`
  * Add support for event notifications `V1IssuingCardholderCreatedEvent` and `V1IssuingCardholderUpdatedEvent` with related object `issuing.Cardholder`
  * Add support for event notifications `V1IssuingDisputeClosedEvent`, `V1IssuingDisputeCreatedEvent`, `V1IssuingDisputeFundsReinstatedEvent`, `V1IssuingDisputeFundsRescindedEvent`, `V1IssuingDisputeSubmittedEvent`, and `V1IssuingDisputeUpdatedEvent` with related object `issuing.Dispute`
  * Add support for event notifications `V1IssuingPersonalizationDesignActivatedEvent`, `V1IssuingPersonalizationDesignDeactivatedEvent`, `V1IssuingPersonalizationDesignRejectedEvent`, and `V1IssuingPersonalizationDesignUpdatedEvent` with related object `issuing.PersonalizationDesign`
  * Add support for event notifications `V1IssuingTokenCreatedEvent` and `V1IssuingTokenUpdatedEvent` with related object `issuing.Token`
  * Add support for event notifications `V1IssuingTransactionCreatedEvent`, `V1IssuingTransactionPurchaseDetailsReceiptUpdatedEvent`, and `V1IssuingTransactionUpdatedEvent` with related object `issuing.Transaction`
  * Add support for event notification `V1MandateUpdatedEvent` with related object `Mandate`
  * Add support for event notifications `V1PaymentIntentAmountCapturableUpdatedEvent`, `V1PaymentIntentCanceledEvent`, `V1PaymentIntentCreatedEvent`, `V1PaymentIntentPartiallyFundedEvent`, `V1PaymentIntentPaymentFailedEvent`, `V1PaymentIntentProcessingEvent`, `V1PaymentIntentRequiresActionEvent`, and `V1PaymentIntentSucceededEvent` with related object `PaymentIntent`
  * Add support for event notifications `V1PaymentLinkCreatedEvent` and `V1PaymentLinkUpdatedEvent` with related object `PaymentLink`
  * Add support for event notifications `V1PaymentMethodAttachedEvent`, `V1PaymentMethodAutomaticallyUpdatedEvent`, `V1PaymentMethodDetachedEvent`, and `V1PaymentMethodUpdatedEvent` with related object `PaymentMethod`
  * Add support for event notifications `V1PayoutCanceledEvent`, `V1PayoutCreatedEvent`, `V1PayoutFailedEvent`, `V1PayoutPaidEvent`, `V1PayoutReconciliationCompletedEvent`, and `V1PayoutUpdatedEvent` with related object `Payout`
  * Add support for event notifications `V1PersonCreatedEvent`, `V1PersonDeletedEvent`, and `V1PersonUpdatedEvent` with related object `Person`
  * Add support for event notifications `V1PlanCreatedEvent`, `V1PlanDeletedEvent`, and `V1PlanUpdatedEvent` with related object `Plan`
  * Add support for event notifications `V1PriceCreatedEvent`, `V1PriceDeletedEvent`, and `V1PriceUpdatedEvent` with related object `Price`
  * Add support for event notifications `V1ProductCreatedEvent`, `V1ProductDeletedEvent`, and `V1ProductUpdatedEvent` with related object `Product`
  * Add support for event notifications `V1PromotionCodeCreatedEvent` and `V1PromotionCodeUpdatedEvent` with related object `PromotionCode`
  * Add support for event notifications `V1QuoteAcceptedEvent`, `V1QuoteCanceledEvent`, `V1QuoteCreatedEvent`, and `V1QuoteFinalizedEvent` with related object `Quote`
  * Add support for event notifications `V1RadarEarlyFraudWarningCreatedEvent` and `V1RadarEarlyFraudWarningUpdatedEvent` with related object `radar.EarlyFraudWarning`
  * Add support for event notifications `V1ReviewClosedEvent` and `V1ReviewOpenedEvent` with related object `Review`
  * Add support for event notifications `V1SetupIntentCanceledEvent`, `V1SetupIntentCreatedEvent`, `V1SetupIntentRequiresActionEvent`, `V1SetupIntentSetupFailedEvent`, and `V1SetupIntentSucceededEvent` with related object `SetupIntent`
  * Add support for event notification `V1SigmaScheduledQueryRunCreatedEvent` with related object `sigma.ScheduledQueryRun`
  * Add support for event notifications `V1SourceCanceledEvent`, `V1SourceChargeableEvent`, `V1SourceFailedEvent`, and `V1SourceRefundAttributesRequiredEvent` with related object `Source`
  * Add support for event notifications `V1SubscriptionScheduleAbortedEvent`, `V1SubscriptionScheduleCanceledEvent`, `V1SubscriptionScheduleCompletedEvent`, `V1SubscriptionScheduleCreatedEvent`, `V1SubscriptionScheduleExpiringEvent`, `V1SubscriptionScheduleReleasedEvent`, and `V1SubscriptionScheduleUpdatedEvent` with related object `SubscriptionSchedule`
  * Add support for event notification `V1TaxSettingsUpdatedEvent` with related object `tax.Settings`
  * Add support for event notifications `V1TaxRateCreatedEvent` and `V1TaxRateUpdatedEvent` with related object `TaxRate`
  * Add support for event notifications `V1TerminalReaderActionFailedEvent`, `V1TerminalReaderActionSucceededEvent`, and `V1TerminalReaderActionUpdatedEvent` with related object `terminal.Reader`
  * Add support for event notifications `V1TestHelpersTestClockAdvancingEvent`, `V1TestHelpersTestClockCreatedEvent`, `V1TestHelpersTestClockDeletedEvent`, `V1TestHelpersTestClockInternalFailureEvent`, and `V1TestHelpersTestClockReadyEvent` with related object `test_helpers.TestClock`
  * Add support for event notifications `V1TopupCanceledEvent`, `V1TopupCreatedEvent`, `V1TopupFailedEvent`, `V1TopupReversedEvent`, and `V1TopupSucceededEvent` with related object `Topup`
  * Add support for event notifications `V1TransferCreatedEvent`, `V1TransferReversedEvent`, and `V1TransferUpdatedEvent` with related object `Transfer`
  * Add support for event notifications `V2CommerceProductCatalogImportsFailedEvent`, `V2CommerceProductCatalogImportsProcessingEvent`, `V2CommerceProductCatalogImportsSucceededEvent`, and `V2CommerceProductCatalogImportsSucceededWithErrorsEvent` with related object `v2.commerce.ProductCatalogImport`
  * Add support for event notifications `V2CoreApprovalRequestApprovedEvent`, `V2CoreApprovalRequestCanceledEvent`, `V2CoreApprovalRequestFailedEvent`, `V2CoreApprovalRequestRejectedEvent`, and `V2CoreApprovalRequestSucceededEvent` with related object `v2.core.ApprovalRequest`
  * Add support for event notification `V2CoreClaimableSandboxUpdatedEvent` with related object `v2.core.ClaimableSandbox`
  * Add support for event notifications `V2ExtendWorkflowRunFailedEvent`, `V2ExtendWorkflowRunStartedEvent`, and `V2ExtendWorkflowRunSucceededEvent` with related object `v2.extend.WorkflowRun`
  * Add support for event notifications `V2OrchestratedCommerceAgreementConfirmedEvent`, `V2OrchestratedCommerceAgreementCreatedEvent`, `V2OrchestratedCommerceAgreementPartiallyConfirmedEvent`, and `V2OrchestratedCommerceAgreementTerminatedEvent` with related object `v2.orchestrated_commerce.Agreement`
  * ⚠️ Remove support for event notification `V2CoreClaimableSandboxSandboxDetailsOwnerAccountUpdatedEvent` with related object `v2.core.ClaimableSandbox`
  * Add support for error type `FxQuoteExpiredError`
  * Add support for error codes `invalid_workflow_input_parameters` and `workflow_not_invokable` on `CannotProceedError`

## 15.1.0a4 - 2026-04-15
* [#1794](https://github.com/stripe/stripe-python/pull/1794) Update generated code for private-preview
  * Add support for `latest_version` on `V2.Billing.LicenseFee`, `V2.Billing.PricingPlan`, and `V2.Billing.RateCard`
  * Add support for `service_interval_count` and `service_interval` on `V2.Billing.LicenseFee` and `V2.Billing.RateCard`
* ⚠️ [#1791](https://github.com/stripe/stripe-python/pull/1791) Update generated code for private-preview
  * Add support for new resources `v2.core.WorkflowRun` and `v2.core.Workflow`
  * Add support for `report_authorized` method on resource `PaymentAttemptRecord`
  * Add support for `list` and `retrieve` methods on resource `v2.core.WorkflowRun`
  * Add support for `invoke`, `list`, and `retrieve` methods on resource `v2.core.Workflow`
  * Add support for `next_action` and `status` on `SharedPayment.IssuedToken`
  * ⚠️ Remove support for `network_id` on `SharedPayment.IssuedToken.SellerDetail`
  * Add support for `bills` on `AccountSession.Component`
  * Add support for `settlement_currencies` on `BalanceSettings.Payment` and `BalanceSettingsModifyParamsPayment`
  * Add support for `default_settlement_currency` on `BalanceSettings.Payment`
  * Add support for `account_funding` on `Charge.PaymentMethodDetail.Card`
  * Add support for `automatic_surcharge` on `Checkout.Session`, `PaymentLinkCreateParams`, `PaymentLink`, and `checkout.SessionCreateParams`
  * Add support for `bizum` on `Checkout.Session.PaymentMethodOption` and `checkout.SessionCreateParamsPaymentMethodOption`
  * Add support for `surcharge_cost` on `Checkout.Session`
  * Add support for `amount_surcharge` on `Checkout.Session.TotalDetail`
  * Add support for `shared_payment_granted_token` on `ConfirmationTokenCreateParamsPaymentMethodDatum`, `PaymentIntentConfirmParamsPaymentMethodDatum`, `PaymentIntentCreateParamsPaymentMethodDatum`, `PaymentIntentModifyParamsPaymentMethodDatum`, `SetupIntentConfirmParamsPaymentMethodDatum`, `SetupIntentCreateParamsPaymentMethodDatum`, and `SetupIntentModifyParamsPaymentMethodDatum`
  * Add support for new value `email` on enums `identity.VerificationReportListParams.type`, `identity.VerificationSessionCreateParams.type`, and `identity.VerificationSessionModifyParams.type`
  * Add support for `details` on `Identity.VerificationReport.Email`
  * ⚠️ Add support for new value `email` on enums `Identity.VerificationReport.type` and `Identity.VerificationSession.type`
  * Add support for `confirm` on `identity.VerificationSessionCreateParams` and `identity.VerificationSessionModifyParams`
  * Add support for `subscription` on `InvoiceItem.Parent.ScheduleDetail`
  * ⚠️ Remove support for `shared_payment_granted_token` on `PaymentIntentConfirmParams` and `PaymentIntentCreateParams`
  * Add support for `money_services` on `PaymentIntent.PaymentDetail`
  * ⚠️ Remove support for `external_reference` on `Plan`
  * Change `SharedPayment.GrantedToken.PaymentMethodDetail.billing_details` to be required

## 15.1.0a3 - 2026-04-08
This release changes the pinned API version to `2026-04-08.preview`.

* ⚠️ [#1789](https://github.com/stripe/stripe-python/pull/1789) Update generated code for private-preview
  * Add support for `payment_record` on `ApplicationFee.FeeSource`
  * Add support for `fleet_data` on `ChargeCaptureParamsPaymentDetail`, `ChargeModifyParamsPaymentDetail`, `PaymentIntent.PaymentDetail`, `PaymentIntentAmountDetailsLineItem.PaymentMethodOption.Card`, `PaymentIntentCaptureParamsAmountDetailLineItemPaymentMethodOptionCard`, `PaymentIntentCaptureParamsPaymentDetail`, `PaymentIntentConfirmParamsAmountDetailLineItemPaymentMethodOptionCard`, `PaymentIntentConfirmParamsPaymentDetail`, `PaymentIntentCreateParamsAmountDetailLineItemPaymentMethodOptionCard`, `PaymentIntentCreateParamsPaymentDetail`, `PaymentIntentDecrementAuthorizationParamsAmountDetailLineItemPaymentMethodOptionCard`, `PaymentIntentIncrementAuthorizationParamsAmountDetailLineItemPaymentMethodOptionCard`, `PaymentIntentModifyParamsAmountDetailLineItemPaymentMethodOptionCard`, and `PaymentIntentModifyParamsPaymentDetail`
  * Add support for `beneficiary_account`, `beneficiary_details`, `sender_account`, and `sender_details` on `ChargeCaptureParamsPaymentDetailMoneyServiceAccountFunding`, `ChargeModifyParamsPaymentDetailMoneyServiceAccountFunding`, `PaymentIntentCaptureParamsPaymentDetailMoneyServiceAccountFunding`, `PaymentIntentConfirmParamsPaymentDetailMoneyServiceAccountFunding`, `PaymentIntentCreateParamsPaymentDetailMoneyServiceAccountFunding`, and `PaymentIntentModifyParamsPaymentDetailMoneyServiceAccountFunding`
  * Change type of `ChargeCaptureParamsPaymentDetailMoneyService.transaction_type`, `ChargeModifyParamsPaymentDetailMoneyService.transaction_type`, `PaymentIntentCaptureParamsPaymentDetailMoneyService.transaction_type`, `PaymentIntentConfirmParamsPaymentDetailMoneyService.transaction_type`, `PaymentIntentCreateParamsPaymentDetailMoneyService.transaction_type`, and `PaymentIntentModifyParamsPaymentDetailMoneyService.transaction_type` from `literal('account_funding')` to `emptyable(literal('account_funding'))`
  * ⚠️ Add support for new value `requires_action` on enum `DelegatedCheckout.RequestedSession.status`
  * Add support for `bizum` on `Invoice.PaymentSetting.PaymentMethodOption`, `InvoiceCreateParamsPaymentSettingPaymentMethodOption`, `InvoiceModifyParamsPaymentSettingPaymentMethodOption`, `QuotePreviewInvoice.PaymentSetting.PaymentMethodOption`, `Subscription.PaymentSetting.PaymentMethodOption`, `SubscriptionCreateParamsPaymentSettingPaymentMethodOption`, and `SubscriptionModifyParamsPaymentSettingPaymentMethodOption`
  * ⚠️ Add support for new value `bizum` on enums `Invoice.PaymentSetting.payment_method_types`, `InvoiceCreateParamsPaymentSetting.payment_method_types`, `InvoiceModifyParamsPaymentSetting.payment_method_types`, `QuotePreviewInvoice.PaymentSetting.payment_method_types`, `Subscription.PaymentSetting.payment_method_types`, `SubscriptionCreateParamsPaymentSetting.payment_method_types`, and `SubscriptionModifyParamsPaymentSetting.payment_method_types`
  * Add support for `quantity_precision` on `PaymentIntentAmountDetailsLineItem`, `PaymentIntentCaptureParamsAmountDetailLineItem`, `PaymentIntentConfirmParamsAmountDetailLineItem`, `PaymentIntentCreateParamsAmountDetailLineItem`, `PaymentIntentDecrementAuthorizationParamsAmountDetailLineItem`, `PaymentIntentIncrementAuthorizationParamsAmountDetailLineItem`, and `PaymentIntentModifyParamsAmountDetailLineItem`
  * Add support for `liquid_asset` and `wallet` on `PaymentIntentConfirmParamsPaymentMethodOptionCardPaymentDetailMoneyServiceAccountFunding`, `PaymentIntentConfirmParamsPaymentMethodOptionCardPresentPaymentDetailMoneyServiceAccountFunding`, `PaymentIntentCreateParamsPaymentMethodOptionCardPaymentDetailMoneyServiceAccountFunding`, `PaymentIntentCreateParamsPaymentMethodOptionCardPresentPaymentDetailMoneyServiceAccountFunding`, `PaymentIntentModifyParamsPaymentMethodOptionCardPaymentDetailMoneyServiceAccountFunding`, and `PaymentIntentModifyParamsPaymentMethodOptionCardPresentPaymentDetailMoneyServiceAccountFunding`
  * Add support for `shared_payment_granted_token` on `PaymentMethod`
  * ⚠️ Change type of `Radar.CustomerEvaluation.event_type` from `string` to `enum('login'|'registration')`
  * ⚠️ Change type of `Radar.CustomerEvaluation.Signal.AccountSharing.risk_level` and `Radar.CustomerEvaluation.Signal.MultiAccounting.risk_level` from `string` to `enum`
  * Add support for `data` on `Radar.PaymentEvaluation.ClientDeviceMetadataDetail` and `radar.PaymentEvaluationCreateParamsClientDeviceMetadataDetail`
  * Add support for `sunbit` on `SharedPayment.GrantedToken.PaymentMethodDetail`
  * ⚠️ Add support for new value `sunbit` on enum `SharedPayment.GrantedToken.PaymentMethodDetail.type`
  * ⚠️ Remove support for values `bm_crn`, `bo_tin`, `bt_tpn`, `co_nit`, `ec_ruc`, `eg_tin`, `gh_tin`, `gy_tin`, `hn_rtn`, `jm_trn`, `jo_crn`, `ke_pin`, `ky_crn`, `lk_tin`, `mo_tin`, `mv_tin`, `ng_tin`, `pa_ruc`, `ph_tin`, `py_ruc`, `sl_tin`, `sv_nit`, `uy_ruc`, `vg_cn`, and `za_tin` from enums `V2.Core.Account.Identity.BusinessDetail.IdNumber.type`, `v2.core.AccountCreateParamsIdentityBusinessDetailIdNumber.type`, `v2.core.AccountModifyParamsIdentityBusinessDetailIdNumber.type`, and `v2.core.AccountTokenCreateParamsIdentityBusinessDetailIdNumber.type`
  * ⚠️ Remove support for values `bm_pp`, `bo_ci`, `bt_cid`, `eg_tin`, `gh_pin`, `gy_tin`, `hn_rtn`, `jm_trn`, `jo_pin`, `ky_pp`, `lk_nic`, `mo_bir`, `mt_nic`, `mv_tin`, `pa_ruc`, `ph_tin`, `py_ruc`, `si_pin`, `sv_nit`, and `vg_pp` from enums `V2.Core.Account.Identity.Individual.IdNumber.type`, `V2.Core.AccountPerson.IdNumber.type`, `v2.core.AccountCreateParamsIdentityIndividualIdNumber.type`, `v2.core.AccountModifyParamsIdentityIndividualIdNumber.type`, `v2.core.AccountPersonCreateParamsIdNumber.type`, `v2.core.AccountPersonModifyParamsIdNumber.type`, `v2.core.AccountPersonTokenCreateParamsIdNumber.type`, and `v2.core.AccountTokenCreateParamsIdentityIndividualIdNumber.type`
  * Add support for error type `CannotProceedError`

## 15.1.0a2 - 2026-04-01
This release changes the pinned API version to `2026-04-01.preview`.

* Please refer to the changelog for [v15.0.1](https://github.com/stripe/stripe-python/blob/v15.0.1/CHANGELOG.md#1501---2026-04-01) for additional changes.
* See the changelog for [v15.0.1](https://github.com/stripe/stripe-python/blob/master/CHANGELOG.md#1501---2026-04-01) for additional changes
* ⚠️ [#1778](https://github.com/stripe/stripe-python/pull/1778) Update generated code for private-preview
  * Add support for new resources `shared_payment.IssuedToken` and `v2.data.reporting.QueryRun`
  * Add support for `create` and `retrieve` methods on resource `v2.data.reporting.QueryRun`
  * Add support for `pause` and `resume` methods on resource `v2.payments.OffSessionPayment`
  * Add support for `tenant_keys`, `tenant_operator`, and `tenant_values` on `billing.BillingMeterListMeterEventSummaryParams`
  * Add support for `money_services` on `ChargeCaptureParamsPaymentDetail`, `ChargeModifyParamsPaymentDetail`, `PaymentIntentCaptureParamsPaymentDetail`, `PaymentIntentConfirmParamsPaymentDetail`, `PaymentIntentCreateParamsPaymentDetail`, and `PaymentIntentModifyParamsPaymentDetail`
  * Add support for `payment_method_options` on `DelegatedCheckout.RequestedSession`, `delegated_checkout.RequestedSessionCreateParams`, and `delegated_checkout.RequestedSessionModifyParams`
  * ⚠️ Remove support for `payment_method_data` on `delegated_checkout.RequestedSessionConfirmParams`, `delegated_checkout.RequestedSessionCreateParams`, and `delegated_checkout.RequestedSessionModifyParams`
  * Add support for `card_brands` and `payment_method_types` on `DelegatedCheckout.RequestedSession.SellerDetail`
  * ⚠️ Change type of `DelegatedCheckout.RequestedSession.shared_payment_issued_token` from `string` to `expandable($SharedPayment.IssuedToken)`
  * Add support for `check_scan` on `Invoice.PaymentSetting.PaymentMethodOption`, `InvoiceCreateParamsPaymentSettingPaymentMethodOption`, `InvoiceModifyParamsPaymentSettingPaymentMethodOption`, `QuotePreviewInvoice.PaymentSetting.PaymentMethodOption`, `Subscription.PaymentSetting.PaymentMethodOption`, `SubscriptionCreateParamsPaymentSettingPaymentMethodOption`, and `SubscriptionModifyParamsPaymentSettingPaymentMethodOption`
  * ⚠️ Add support for new value `check_scan` on enums `Invoice.PaymentSetting.payment_method_types`, `InvoiceCreateParamsPaymentSetting.payment_method_types`, `InvoiceModifyParamsPaymentSetting.payment_method_types`, `QuotePreviewInvoice.PaymentSetting.payment_method_types`, `Subscription.PaymentSetting.payment_method_types`, `SubscriptionCreateParamsPaymentSetting.payment_method_types`, and `SubscriptionModifyParamsPaymentSetting.payment_method_types`
  * Add support for `processor_details` on `PaymentAttemptRecordReportFailedParams`, `PaymentAttemptRecordReportGuaranteedParams`, `PaymentRecordReportPaymentAttemptFailedParams`, `PaymentRecordReportPaymentAttemptGuaranteedParams`, `PaymentRecordReportPaymentAttemptParamsFailed`, `PaymentRecordReportPaymentAttemptParamsGuaranteed`, `PaymentRecordReportPaymentParamsFailed`, and `PaymentRecordReportPaymentParamsGuaranteed`
  * Add support for `payment_details` on `PaymentIntentConfirmParamsPaymentMethodOptionCardPresent`, `PaymentIntentConfirmParamsPaymentMethodOptionCard`, `PaymentIntentCreateParamsPaymentMethodOptionCardPresent`, `PaymentIntentCreateParamsPaymentMethodOptionCard`, `PaymentIntentModifyParamsPaymentMethodOptionCardPresent`, and `PaymentIntentModifyParamsPaymentMethodOptionCard`
  * ⚠️ Remove support for `bill_from` on `QuotePreviewSubscriptionSchedule.BillingSchedule`, `Subscription.BillingSchedule`, and `SubscriptionSchedule.BillingSchedule`
  * Add support for `agent_details`, `payment_method_details`, and `risk_details` on `SharedPayment.GrantedToken`
  * Add support for `paper_checks` on `V2.Account.Configuration.RecipientDatum.Feature`, `V2.Core.Account.Configuration.Recipient.Capability`, `V2.Core.Account.Configuration.Storer.Capability.OutboundPayment`, `v2.AccountCreateParamsConfigurationRecipientDatumFeature`, `v2.AccountModifyParamsConfigurationRecipientDatumFeature`, `v2.core.AccountCreateParamsConfigurationRecipientCapability`, `v2.core.AccountCreateParamsConfigurationStorerCapabilityOutboundPayment`, `v2.core.AccountModifyParamsConfigurationRecipientCapability`, and `v2.core.AccountModifyParamsConfigurationStorerCapabilityOutboundPayment`
  * ⚠️ Add support for new value `paper_checks` on enum `V2.Account.Configuration.SupportableFeature.recipient_data`
  * ⚠️ Add support for new value `paper_checks` on enum `V2.Account.Requirement.Impact.required_for_features`
  * ⚠️ Change type of `V2.Billing.Cadence.SettingsDatum.Collection.PaymentMethodOption.konbini`, `V2.Billing.CollectionSetting.PaymentMethodOption.konbini`, `V2.Billing.CollectionSettingVersion.PaymentMethodOption.konbini`, `v2.billing.CollectionSettingCreateParamsPaymentMethodOption.konbini`, and `v2.billing.CollectionSettingModifyParamsPaymentMethodOption.konbini` from `map(string: dynamic)` to `an object`
  * ⚠️ Change type of `V2.Billing.Cadence.SettingsDatum.Collection.PaymentMethodOption.sepa_debit`, `V2.Billing.CollectionSetting.PaymentMethodOption.sepa_debit`, `V2.Billing.CollectionSettingVersion.PaymentMethodOption.sepa_debit`, `v2.billing.CollectionSettingCreateParamsPaymentMethodOption.sepa_debit`, and `v2.billing.CollectionSettingModifyParamsPaymentMethodOption.sepa_debit` from `map(string: dynamic)` to `an object`
  * Add support for `id` on `V2.Billing.CadenceSpendModifier.MaxBillingPeriodSpend.Amount.CustomPricingUnit`, `V2.Billing.IntentAction.Apply.SpendModifierRule.MaxBillingPeriodSpend.Amount.CustomPricingUnit`, and `v2.billing.IntentCreateParamsActionApplySpendModifierRuleMaxBillingPeriodSpendAmountCustomPricingUnit`
  * ⚠️ Add support for new values `outbound_payments.paper_checks` and `paper_checks` on enums `V2.Core.Account.FutureRequirement.Entry.Impact.RestrictsCapability.capability` and `V2.Core.Account.Requirement.Entry.Impact.RestrictsCapability.capability`
  * ⚠️ Add support for new values `bm_crn`, `bo_tin`, `bt_tpn`, `co_nit`, `ec_ruc`, `eg_tin`, `gh_tin`, `gy_tin`, `hn_rtn`, `jm_trn`, `jo_crn`, `ke_pin`, `ky_crn`, `lk_tin`, `mo_tin`, `mv_tin`, `ng_tin`, `pa_ruc`, `ph_tin`, `py_ruc`, `sl_tin`, `sv_nit`, `uy_ruc`, `vg_cn`, and `za_tin` on enums `V2.Core.Account.Identity.BusinessDetail.IdNumber.type`, `v2.core.AccountCreateParamsIdentityBusinessDetailIdNumber.type`, `v2.core.AccountModifyParamsIdentityBusinessDetailIdNumber.type`, and `v2.core.AccountTokenCreateParamsIdentityBusinessDetailIdNumber.type`
  * ⚠️ Add support for new values `bm_pp`, `bo_ci`, `bt_cid`, `eg_tin`, `gh_pin`, `gy_tin`, `hn_rtn`, `jm_trn`, `jo_pin`, `ky_pp`, `lk_nic`, `mo_bir`, `mt_nic`, `mv_tin`, `pa_ruc`, `ph_tin`, `py_ruc`, `si_pin`, `sv_nit`, and `vg_pp` on enums `V2.Core.Account.Identity.Individual.IdNumber.type`, `V2.Core.AccountPerson.IdNumber.type`, `v2.core.AccountCreateParamsIdentityIndividualIdNumber.type`, `v2.core.AccountModifyParamsIdentityIndividualIdNumber.type`, `v2.core.AccountPersonCreateParamsIdNumber.type`, `v2.core.AccountPersonModifyParamsIdNumber.type`, `v2.core.AccountPersonTokenCreateParamsIdNumber.type`, and `v2.core.AccountTokenCreateParamsIdentityIndividualIdNumber.type`
  * ⚠️ Change type of `V2.Core.Event.Reason.Request.Client.stripe_action` from `map(string: dynamic)` to `an object`
  * ⚠️ Change type of `V2.MoneyManagement.InboundTransfer.TransferHistory.bank_debit_processing` from `map(string: dynamic)` to `an object`
  * ⚠️ Change type of `V2.MoneyManagement.InboundTransfer.TransferHistory.bank_debit_queued` from `map(string: dynamic)` to `an object`
  * ⚠️ Change type of `V2.MoneyManagement.InboundTransfer.TransferHistory.bank_debit_succeeded` from `map(string: dynamic)` to `an object`
  * ⚠️ Add support for new values `paper_check_attachment_too_large`, `paper_check_expired`, and `paper_check_undeliverable` on enum `V2.MoneyManagement.OutboundPayment.StatusDetail.Failed.reason`
  * ⚠️ Remove support for `town` on `V2.MoneyManagement.OutboundPayment.TrackingDetail.PaperCheck.MailingAddress`
  * Change `V2.MoneyManagement.OutboundPayment.DeliveryOption.PaperCheck.memo` to be required
  * ⚠️ Add support for new value `payout_method_amount_limit_exceeded` on enum `V2.MoneyManagement.OutboundTransfer.StatusDetail.Failed.reason`
  * Add support for `application_fee_amount_requested` on `V2.Payments.OffSessionPayment`
  * ⚠️ Remove support for `compartment_id` on `V2.Payments.OffSessionPayment`
  * ⚠️ Add support for new value `exceeded_retry_window` on enum `V2.Payments.OffSessionPayment.failure_reason`
  * Add support for `retry_until` on `V2.Payments.OffSessionPayment.RetryDetail`
  * ⚠️ Add support for new value `paused` on enum `V2.Payments.OffSessionPayment.status`
  * ⚠️ Change `V2.Reporting.ReportRun.Result.file` to be optional
  * Add support for `application_fee_amount` on `v2.payments.OffSessionPaymentCaptureParams` and `v2.payments.OffSessionPaymentCreateParams`
  * ⚠️ Add support for new value `paper_checks` on enum `EventsV2CoreAccountIncludingConfigurationRecipientCapabilityStatusUpdatedEvent.updated_capability`
  * ⚠️ Add support for new value `outbound_payments.paper_checks` on enum `EventsV2CoreAccountIncludingConfigurationStorerCapabilityStatusUpdatedEvent.updated_capability`
  * Add support for `alert_id` on `EventsV2CoreHealthApiErrorResolvedEvent`, `EventsV2CoreHealthApiLatencyResolvedEvent`, `EventsV2CoreHealthAuthorizationRateDropResolvedEvent`, `EventsV2CoreHealthIssuingAuthorizationRequestErrorsFiringEvent`, `EventsV2CoreHealthIssuingAuthorizationRequestErrorsResolvedEvent`, `EventsV2CoreHealthIssuingAuthorizationRequestTimeoutResolvedEvent`, `EventsV2CoreHealthPaymentMethodErrorResolvedEvent`, `EventsV2CoreHealthSepaDebitDelayedFiringEvent`, `EventsV2CoreHealthSepaDebitDelayedResolvedEvent`, `EventsV2CoreHealthTrafficVolumeDropResolvedEvent`, and `EventsV2CoreHealthWebhookLatencyResolvedEvent`
  * Add support for `api_key` on `EventsV2IamApiKeyCreatedEvent`, `EventsV2IamApiKeyDefaultSecretRevealedEvent`, `EventsV2IamApiKeyExpiredEvent`, `EventsV2IamApiKeyPermissionsUpdatedEvent`, `EventsV2IamApiKeyRotatedEvent`, and `EventsV2IamApiKeyUpdatedEvent`
  * Add support for `stripe_access_grant` on `EventsV2IamStripeAccessGrantApprovedEvent`, `EventsV2IamStripeAccessGrantCanceledEvent`, `EventsV2IamStripeAccessGrantDeniedEvent`, `EventsV2IamStripeAccessGrantRemovedEvent`, `EventsV2IamStripeAccessGrantRequestedEvent`, and `EventsV2IamStripeAccessGrantUpdatedEvent`
  * Add support for event notifications `V2DataReportingQueryRunCreatedEvent`, `V2DataReportingQueryRunFailedEvent`, `V2DataReportingQueryRunSucceededEvent`, and `V2DataReportingQueryRunUpdatedEvent` with related object `v2.data.reporting.QueryRun`
  * Add support for event notifications `V2PaymentsOffSessionPaymentPausedEvent` and `V2PaymentsOffSessionPaymentResumedEvent` with related object `v2.payments.OffSessionPayment`

## 15.1.0a1 - 2026-03-25
This release changes the pinned API version to `2026-03-25.preview`.

This release contains additional breaking changes. See the [GA changelog](https://github.com/stripe/stripe-python/blob/master/CHANGELOG.md#1500---2026-03-25) for more information.

* ⚠️ [#1776](https://github.com/stripe/stripe-python/pull/1776) Update generated code for private-preview
  * Add support for new resource `RiskSignals`
  * Add support for `financial_account_rewards` and `nesting_demo` on `AccountSession.Component`
  * Add support for `upi_payments` on `Account.Capability`, `AccountCreateParamsCapability`, and `AccountModifyParamsCapability`
  * Add support for `risk_signals` on `Account`
  * Add support for `fraud_intent` on `AccountSignals`
  * ⚠️ Add support for new value `related_accounts` on enum `AccountSignals.Delinquency.Indicator.indicator`
  * Add support for `risk_reserved` on `Balance`
  * ⚠️ Remove support for `billable_items` on `Billing.Alert.SpendThreshold.Filter`
  * Add support for `upi` on `Charge.PaymentMethodDetail`, `Checkout.Session.PaymentMethodOption`, `ConfirmationToken.PaymentMethodPreview`, `ConfirmationTokenCreateParamsPaymentMethodDatum`, `Mandate.PaymentMethodDetail`, `PaymentAttemptRecord.PaymentMethodDetail`, `PaymentIntent.PaymentMethodOption`, `PaymentIntentConfirmParamsPaymentMethodDatum`, `PaymentIntentConfirmParamsPaymentMethodOption`, `PaymentIntentCreateParamsPaymentMethodDatum`, `PaymentIntentCreateParamsPaymentMethodOption`, `PaymentIntentModifyParamsPaymentMethodDatum`, `PaymentIntentModifyParamsPaymentMethodOption`, `PaymentMethodConfigurationCreateParams`, `PaymentMethodConfigurationModifyParams`, `PaymentMethodConfiguration`, `PaymentMethodCreateParams`, `PaymentMethod`, `PaymentRecord.PaymentMethodDetail`, `SetupAttempt.PaymentMethodDetail`, `SetupIntent.PaymentMethodOption`, `SetupIntentConfirmParamsPaymentMethodDatum`, `SetupIntentConfirmParamsPaymentMethodOption`, `SetupIntentCreateParamsPaymentMethodDatum`, `SetupIntentCreateParamsPaymentMethodOption`, `SetupIntentModifyParamsPaymentMethodDatum`, `SetupIntentModifyParamsPaymentMethodOption`, and `checkout.SessionCreateParamsPaymentMethodOption`
  * ⚠️ Add support for new value `tempo` on enums `Charge.PaymentMethodDetail.Crypto.network`, `PaymentAttemptRecord.PaymentMethodDetail.Crypto.network`, and `PaymentRecord.PaymentMethodDetail.Crypto.network`
  * ⚠️ Remove support for `source_type` on `Charge.PaymentMethodDetail.StripeBalance`, `ConfirmationToken.PaymentMethodPreview.StripeBalance`, `ConfirmationTokenCreateParamsPaymentMethodDatumStripeBalance`, `PaymentAttemptRecord.PaymentMethodDetail.StripeBalance`, `PaymentIntentConfirmParamsPaymentMethodDatumStripeBalance`, `PaymentIntentCreateParamsPaymentMethodDatumStripeBalance`, `PaymentIntentModifyParamsPaymentMethodDatumStripeBalance`, `PaymentMethod.StripeBalance`, `PaymentMethodCreateParamsStripeBalance`, `PaymentRecord.PaymentMethodDetail.StripeBalance`, `SetupIntentConfirmParamsPaymentMethodDatumStripeBalance`, `SetupIntentCreateParamsPaymentMethodDatumStripeBalance`, and `SetupIntentModifyParamsPaymentMethodDatumStripeBalance`
  * Add support for `integration_identifier` on `Checkout.Session` and `checkout.SessionCreateParams`
  * ⚠️ Add support for new value `application` on enums `Checkout.Session.AutomaticTax.Liability.type`, `Checkout.Session.InvoiceCreation.InvoiceDatum.Issuer.type`, `Invoice.AutomaticTax.Liability.type`, `Invoice.Issuer.type`, `InvoiceCreateParamsAutomaticTaxLiability.type`, `InvoiceCreateParamsIssuer.type`, `InvoiceCreatePreviewParamsAutomaticTaxLiability.type`, `InvoiceCreatePreviewParamsIssuer.type`, `InvoiceCreatePreviewParamsScheduleDetailPhaseAutomaticTaxLiability.type`, `InvoiceCreatePreviewParamsScheduleDetailPhaseInvoiceSettingIssuer.type`, `InvoiceModifyParamsAutomaticTaxLiability.type`, `InvoiceModifyParamsIssuer.type`, `PaymentLink.AutomaticTax.Liability.type`, `PaymentLink.InvoiceCreation.InvoiceDatum.Issuer.type`, `PaymentLink.SubscriptionDatum.InvoiceSetting.Issuer.type`, `PaymentLinkCreateParamsAutomaticTaxLiability.type`, `PaymentLinkCreateParamsInvoiceCreationInvoiceDatumIssuer.type`, `PaymentLinkCreateParamsSubscriptionDatumInvoiceSettingIssuer.type`, `PaymentLinkModifyParamsAutomaticTaxLiability.type`, `PaymentLinkModifyParamsInvoiceCreationInvoiceDatumIssuer.type`, `PaymentLinkModifyParamsSubscriptionDatumInvoiceSettingIssuer.type`, `Quote.AutomaticTax.Liability.type`, `Quote.InvoiceSetting.Issuer.type`, `QuoteCreateParamsAutomaticTaxLiability.type`, `QuoteCreateParamsInvoiceSettingIssuer.type`, `QuoteModifyParamsAutomaticTaxLiability.type`, `QuoteModifyParamsInvoiceSettingIssuer.type`, `QuotePreviewInvoice.AutomaticTax.Liability.type`, `QuotePreviewInvoice.Issuer.type`, `QuotePreviewSubscriptionSchedule.DefaultSetting.AutomaticTax.Liability.type`, `QuotePreviewSubscriptionSchedule.DefaultSetting.InvoiceSetting.Issuer.type`, `QuotePreviewSubscriptionSchedule.Phase.AutomaticTax.Liability.type`, `QuotePreviewSubscriptionSchedule.Phase.InvoiceSetting.Issuer.type`, `Subscription.AutomaticTax.Liability.type`, `Subscription.InvoiceSetting.Issuer.type`, `SubscriptionCreateParamsAutomaticTaxLiability.type`, `SubscriptionCreateParamsInvoiceSettingIssuer.type`, `SubscriptionModifyParamsAutomaticTaxLiability.type`, `SubscriptionModifyParamsInvoiceSettingIssuer.type`, `SubscriptionSchedule.DefaultSetting.AutomaticTax.Liability.type`, `SubscriptionSchedule.DefaultSetting.InvoiceSetting.Issuer.type`, `SubscriptionSchedule.Phase.AutomaticTax.Liability.type`, `SubscriptionSchedule.Phase.InvoiceSetting.Issuer.type`, `SubscriptionScheduleCreateParamsDefaultSettingAutomaticTaxLiability.type`, `SubscriptionScheduleCreateParamsDefaultSettingInvoiceSettingIssuer.type`, `SubscriptionScheduleCreateParamsPhaseAutomaticTaxLiability.type`, `SubscriptionScheduleCreateParamsPhaseInvoiceSettingIssuer.type`, `SubscriptionScheduleModifyParamsDefaultSettingAutomaticTaxLiability.type`, `SubscriptionScheduleModifyParamsDefaultSettingInvoiceSettingIssuer.type`, `SubscriptionScheduleModifyParamsPhaseAutomaticTaxLiability.type`, `SubscriptionScheduleModifyParamsPhaseInvoiceSettingIssuer.type`, `checkout.SessionCreateParamsAutomaticTaxLiability.type`, `checkout.SessionCreateParamsInvoiceCreationInvoiceDatumIssuer.type`, `checkout.SessionCreateParamsSubscriptionDatumInvoiceSettingIssuer.type`, `checkout.SessionModifyParamsAutomaticTaxLiability.type`, `checkout.SessionModifyParamsInvoiceCreationInvoiceDatumIssuer.type`, and `checkout.SessionModifyParamsSubscriptionDatumInvoiceSettingIssuer.type`
  * Add support for new value `upi` on enum `checkout.SessionCreateParams.excluded_payment_method_types`
  * Change type of `InvoiceAddLinesParamsLinePriceDatumProductDatumTaxDetail.tax_code`, `InvoiceLineItemModifyParamsPriceDatumProductDatumTaxDetail.tax_code`, `InvoiceUpdateLinesParamsLinePriceDatumProductDatumTaxDetail.tax_code`, `PaymentLinkCreateParamsLineItemPriceDatumProductDatumTaxDetail.tax_code`, `PlanCreateParamsProductTaxDetail.tax_code`, `PriceCreateParamsProductDatumTaxDetail.tax_code`, `ProductCreateParamsTaxDetail.tax_code`, `ProductModifyParamsTaxDetail.tax_code`, `checkout.SessionCreateParamsLineItemPriceDatumProductDatumTaxDetail.tax_code`, and `checkout.SessionModifyParamsLineItemPriceDatumProductDatumTaxDetail.tax_code` from `string` to `emptyable(string)`
  * Add support for `crypto` on `checkout.SessionCreateParamsPaymentMethodOption`
  * Add support for new value `upi` on enum `checkout.SessionCreateParams.payment_method_types`
  * Add support for `pending_invoice_item_interval` on `checkout.SessionCreateParamsSubscriptionDatum` and `checkout.SessionModifyParamsSubscriptionDatum`
  * ⚠️ Add support for new values `elements`, `embedded_page`, `form`, and `hosted_page` on enums `Checkout.Session.ui_mode` and `checkout.SessionCreateParams.ui_mode`
  * ⚠️ Remove support for values `custom`, `embedded`, and `hosted` from enums `Checkout.Session.ui_mode` and `checkout.SessionCreateParams.ui_mode`
  * Change `InvoiceAddLinesParamsLinePriceDatumProductDatumTaxDetail.tax_code`, `InvoiceLineItemModifyParamsPriceDatumProductDatumTaxDetail.tax_code`, `InvoiceUpdateLinesParamsLinePriceDatumProductDatumTaxDetail.tax_code`, `PaymentLinkCreateParamsLineItemPriceDatumProductDatumTaxDetail.tax_code`, `PlanCreateParamsProductTaxDetail.tax_code`, `PriceCreateParamsProductDatumTaxDetail.tax_code`, `ProductCreateParamsTaxDetail.tax_code`, `ProductModifyParamsTaxDetail.tax_code`, `checkout.SessionCreateParamsLineItemPriceDatumProductDatumTaxDetail.tax_code`, and `checkout.SessionModifyParamsLineItemPriceDatumProductDatumTaxDetail.tax_code` to be optional
  * Add support for `au_becs_debit`, `bacs_debit`, `boleto`, `link`, `sepa_debit`, and `us_bank_account` on `Checkout.Session.CurrentAttempt.PaymentMethodDetail`
  * ⚠️ Add support for new value `marine_carbon_removal` on enum `Climate.Supplier.removal_pathway`
  * Add support for new value `upi` on enums `ConfirmationTokenCreateParamsPaymentMethodDatum.type`, `PaymentIntentConfirmParamsPaymentMethodDatum.type`, `PaymentIntentCreateParamsPaymentMethodDatum.type`, `PaymentIntentModifyParamsPaymentMethodDatum.type`, `SetupIntentConfirmParamsPaymentMethodDatum.type`, `SetupIntentCreateParamsPaymentMethodDatum.type`, and `SetupIntentModifyParamsPaymentMethodDatum.type`
  * ⚠️ Add support for new value `upi` on enums `ConfirmationToken.PaymentMethodPreview.type` and `PaymentMethod.type`
  * Add support for `metadata` on `CreditNoteCreateParamsLine`, `CreditNoteLineItem`, `CreditNotePreviewLinesParamsLine`, and `CreditNotePreviewParamsLine`
  * Add support for new value `upi` on enums `CustomerListPaymentMethodsParams.type`, `PaymentMethodCreateParams.type`, and `PaymentMethodListParams.type`
  * Add support for `selected_fulfillment_option_overrides` on `DelegatedCheckout.RequestedSession.FulfillmentDetail`
  * Add support for `line_item_keys` on `DelegatedCheckout.RequestedSession.FulfillmentDetail.FulfillmentOption.Digital.DigitalOption` and `DelegatedCheckout.RequestedSession.FulfillmentDetail.FulfillmentOption.Shipping.ShippingOption`
  * Add support for `quantity_decimal` on `InvoiceAddLinesParamsLine`, `InvoiceCreatePreviewParamsInvoiceItem`, `InvoiceItemCreateParams`, `InvoiceItemModifyParams`, `InvoiceItem`, `InvoiceLineItemModifyParams`, `InvoiceLineItem`, and `InvoiceUpdateLinesParamsLine`
  * Add support for `expires_after_seconds` on `Invoice.PaymentSetting.PaymentMethodOption.Pix`, `InvoiceCreateParamsPaymentSettingPaymentMethodOptionPix`, `InvoiceModifyParamsPaymentSettingPaymentMethodOptionPix`, `QuotePreviewInvoice.PaymentSetting.PaymentMethodOption.Pix`, `Subscription.PaymentSetting.PaymentMethodOption.Pix`, `SubscriptionCreateParamsPaymentSettingPaymentMethodOptionPix`, and `SubscriptionModifyParamsPaymentSettingPaymentMethodOptionPix`
  * ⚠️ Add support for `level` on `issuing.AuthorizationCreateParamsRiskAssessmentCardTestingRisk` and `issuing.AuthorizationCreateParamsRiskAssessmentMerchantDisputeRisk`
  * ⚠️ Remove support for `risk_level` on `issuing.AuthorizationCreateParamsRiskAssessmentCardTestingRisk` and `issuing.AuthorizationCreateParamsRiskAssessmentMerchantDisputeRisk`
  * ⚠️ Add support for new values `da`, `pl`, and `sv` on enums `Issuing.Cardholder.preferred_locales`, `issuing.CardholderCreateParams.preferred_locales`, and `issuing.CardholderModifyParams.preferred_locales`
  * Add support for `lifecycle_controls` on `Issuing.Card` and `issuing.CardCreateParams`
  * ⚠️ Change type of `Issuing.Token.NetworkDatum.Visa.card_reference_id` from `string` to `nullable(string)`
  * ⚠️ Change type of `PaymentAttemptRecord.PaymentMethodDetail.Card.brand` and `PaymentRecord.PaymentMethodDetail.Card.brand` from `enum` to `nullable(enum)`
  * ⚠️ Change type of `PaymentAttemptRecord.PaymentMethodDetail.Card.exp_month` and `PaymentRecord.PaymentMethodDetail.Card.exp_month` from `longInteger` to `nullable(longInteger)`
  * ⚠️ Change type of `PaymentAttemptRecord.PaymentMethodDetail.Card.exp_year` and `PaymentRecord.PaymentMethodDetail.Card.exp_year` from `longInteger` to `nullable(longInteger)`
  * ⚠️ Change type of `PaymentAttemptRecord.PaymentMethodDetail.Card.funding` and `PaymentRecord.PaymentMethodDetail.Card.funding` from `enum('credit'|'debit'|'prepaid'|'unknown')` to `nullable(enum('credit'|'debit'|'prepaid'|'unknown'))`
  * ⚠️ Change type of `PaymentAttemptRecord.PaymentMethodDetail.Card.last4` and `PaymentRecord.PaymentMethodDetail.Card.last4` from `string` to `nullable(string)`
  * ⚠️ Change type of `PaymentAttemptRecord.PaymentMethodDetail.Card.moto` and `PaymentRecord.PaymentMethodDetail.Card.moto` from `boolean` to `nullable(boolean)`
  * Add support for `cryptogram`, `electronic_commerce_indicator`, `exemption_indicator_applied`, and `exemption_indicator` on `PaymentAttemptRecord.PaymentMethodDetail.Card.ThreeDSecure` and `PaymentRecord.PaymentMethodDetail.Card.ThreeDSecure`
  * Add support for `surcharge` on `PaymentIntent.AmountDetail`, `PaymentIntentCaptureParamsAmountDetail`, `PaymentIntentConfirmParamsAmountDetail`, `PaymentIntentCreateParamsAmountDetail`, `PaymentIntentIncrementAuthorizationParamsAmountDetail`, and `PaymentIntentModifyParamsAmountDetail`
  * ⚠️ Add support for new value `upi` on enums `PaymentIntent.excluded_payment_method_types`, `PaymentIntentConfirmParams.excluded_payment_method_types`, `PaymentIntentCreateParams.excluded_payment_method_types`, `PaymentIntentModifyParams.excluded_payment_method_types`, `SetupIntent.excluded_payment_method_types`, `SetupIntentCreateParams.excluded_payment_method_types`, and `SetupIntentModifyParams.excluded_payment_method_types`
  * Add support for `mandate_options` on `PaymentIntent.PaymentMethodOption.StripeBalance`, `PaymentIntentConfirmParamsPaymentMethodOptionStripeBalance`, `PaymentIntentCreateParamsPaymentMethodOptionStripeBalance`, and `PaymentIntentModifyParamsPaymentMethodOptionStripeBalance`
  * Add support for `amount_details` and `payment_details` on `PaymentIntentDecrementAuthorizationParams`
  * Add support for `upi_handle_redirect_or_display_qr_code` on `PaymentIntent.NextAction` and `SetupIntent.NextAction`
  * Add support for `managed_payments` on `PaymentLinkCreateParams` and `PaymentLink`
  * ⚠️ Add support for new value `upi` on enums `PaymentLink.payment_method_types`, `PaymentLinkCreateParams.payment_method_types`, and `PaymentLinkModifyParams.payment_method_types`
  * Add support for `recommended_action` and `signals` on `Radar.PaymentEvaluation`
  * ⚠️ Remove support for `insights` on `Radar.PaymentEvaluation`
  * ⚠️ Add support for new value `crypto_fingerprint` on enums `Radar.ValueList.item_type` and `radar.ValueListCreateParams.item_type`
  * Add support for `stripe_balance` on `SetupIntent.PaymentMethodOption`, `SetupIntentConfirmParamsPaymentMethodOption`, `SetupIntentCreateParamsPaymentMethodOption`, and `SetupIntentModifyParamsPaymentMethodOption`
  * ⚠️ Add support for new value `resolved` on enum `SharedPayment.GrantedToken.deactivated_reason`
  * Add support for `recurring_interval` on `SharedPayment.GrantedToken.UsageLimit`
  * ⚠️ Change type of `SharedPayment.GrantedToken.UsageLimit.expires_at` from `DateTime` to `nullable(DateTime)`
  * Add support for `presentment_details` on `Subscription`
  * ⚠️ Add support for new value `canceled_by_retention_policy` on enum `Subscription.CancellationDetail.reason`
  * Add support for new value `2026-03-25.dahlia` on enum `WebhookEndpointCreateParams.api_version`
  * ⚠️ Remove support for `invoice_resources` on `V2.Billing.Intent`
  * ⚠️ Remove support for `amount_due` and `customer_balance_applied` on `V2.Billing.Intent.AmountDetail`
  * Add support for `recurring_credit_grant` on `V2.Billing.IntentAction.Modify.PricingPlanSubscriptionDetail.Override.PartialPeriodBehavior`, `V2.Billing.IntentAction.Subscribe.PricingPlanSubscriptionDetail.Override.PartialPeriodBehavior`, `v2.billing.IntentCreateParamsActionModifyPricingPlanSubscriptionDetailOverridePartialPeriodBehavior`, and `v2.billing.IntentCreateParamsActionSubscribePricingPlanSubscriptionDetailOverridePartialPeriodBehavior`
  * Add support for `consumer_privacy_disclosures` and `consumer_storer` on `V2.Core.Account.Identity.Attestation.TermsOfService`, `v2.core.AccountCreateParamsIdentityAttestationTermsOfService`, and `v2.core.AccountModifyParamsIdentityAttestationTermsOfService`
  * ⚠️ Remove support for `include` on `v2.billing.IntentCreateParams` and `v2.billing.IntentReserveParams`
  * Add support for error code `service_period_coupon_with_metered_tiered_item_unsupported` on `Invoice.LastFinalizationError`, `PaymentIntent.LastPaymentError`, `QuotePreviewInvoice.LastFinalizationError`, `SetupAttempt.SetupError`, `SetupIntent.LastSetupError`, and `StripeError`
* ⚠️ [#1763](https://github.com/stripe/stripe-python/pull/1763) Update generated code for private-preview
  * Add support for new resource `v2.core.AccountEvaluation`
  * ⚠️ Remove support for resources `v2.billing.LicenseFeeSubscription` and `v2.billing.PricingPlanSubscriptionComponents`
  * Add support for `create` method on resource `v2.core.AccountEvaluation`
  * ⚠️ Remove support for `retrieve` method on resources `v2.billing.LicenseFeeSubscription` and `v2.billing.PricingPlanSubscriptionComponents`
  * Add support for `modify_rates` method on resource `v2.billing.RateCard`
  * Add support for `remove_discounts` method on resource `v2.billing.PricingPlanSubscription`
  * ⚠️ Add support for new value `eg_bank_account` on enum `V2.Account.Configuration.RecipientDatum.DefaultOutboundDestination.type`
  * Add support for `invoice_resources` on `V2.Billing.Intent`
  * Add support for `amount_due` and `customer_balance_applied` on `V2.Billing.Intent.AmountDetail`
  * Add support for `expires_at` on `V2.Billing.Intent.StatusTransition`
  * Add support for `discount` on `V2.Billing.IntentAction.Apply` and `v2.billing.IntentCreateParamsActionApply`
  * Add support for `timestamp` on `V2.Billing.IntentAction.Apply.EffectiveAt` and `v2.billing.IntentCreateParamsActionApplyEffectiveAt`
  * ⚠️ Add support for new values `current_billing_period_start` and `timestamp` on enums `V2.Billing.IntentAction.Apply.EffectiveAt.type` and `v2.billing.IntentCreateParamsActionApplyEffectiveAt.type`
  * ⚠️ Add support for new value `discount` on enums `V2.Billing.IntentAction.Apply.type` and `v2.billing.IntentCreateParamsActionApply.type`
  * ⚠️ Change type of `V2.Billing.IntentAction.Deactivate.PricingPlanSubscriptionDetail.Override.PartialPeriodBehavior.type`, `V2.Billing.IntentAction.Modify.PricingPlanSubscriptionDetail.Override.PartialPeriodBehavior.type`, `V2.Billing.IntentAction.Subscribe.PricingPlanSubscriptionDetail.Override.PartialPeriodBehavior.type`, `v2.billing.IntentCreateParamsActionDeactivatePricingPlanSubscriptionDetailOverridePartialPeriodBehavior.type`, `v2.billing.IntentCreateParamsActionModifyPricingPlanSubscriptionDetailOverridePartialPeriodBehavior.type`, and `v2.billing.IntentCreateParamsActionSubscribePricingPlanSubscriptionDetailOverridePartialPeriodBehavior.type` from `literal('license_fee')` to `enum('license_fee'|'recurring_credit_grant')`
  * Add support for `service_cycle` on `V2.Billing.LicenseFee` and `V2.Billing.RateCard`
  * ⚠️ Remove support for `latest_version` on `V2.Billing.LicenseFee`, `V2.Billing.PricingPlan`, and `V2.Billing.RateCard`
  * ⚠️ Remove support for `service_interval_count` and `service_interval` on `V2.Billing.LicenseFee` and `V2.Billing.RateCard`
  * ⚠️ Change type of `V2.Billing.LicenseFee.TransformQuantity.divide_by`, `V2.Billing.LicenseFeeVersion.TransformQuantity.divide_by`, `V2.Billing.RateCardRate.TransformQuantity.divide_by`, `v2.billing.LicenseFeeCreateParamsTransformQuantity.divide_by`, `v2.billing.LicenseFeeModifyParamsTransformQuantity.divide_by`, and `v2.billing.RateCardRateCreateParamsTransformQuantity.divide_by` from `longInteger` to `int64_string`
  * Add support for `discount_details` and `pricing_plan_component_details` on `V2.Billing.PricingPlanSubscription`
  * ⚠️ Add support for new value `crypto_wallets` on enums `V2.Core.Account.FutureRequirement.Entry.Impact.RestrictsCapability.capability` and `V2.Core.Account.Requirement.Entry.Impact.RestrictsCapability.capability`
  * ⚠️ Remove support for value `crypto` from enums `V2.Core.Account.FutureRequirement.Entry.Impact.RestrictsCapability.capability` and `V2.Core.Account.Requirement.Entry.Impact.RestrictsCapability.capability`
  * Add support for `balance_by_funds_type` on `V2.MoneyManagement.FinancialAccount.Payment`
  * ⚠️ Add support for new value `next_day_payout_fee` on enum `V2.MoneyManagement.OutboundPaymentQuote.EstimatedFee.type`
  * Add support for `treasury_transaction_entry` on `V2.MoneyManagement.TransactionEntry`
  * Add support for `treasury_credit_reversal`, `treasury_debit_reversal`, `treasury_inbound_transfer`, `treasury_issuing_authorization`, `treasury_outbound_payment`, `treasury_outbound_transfer`, `treasury_received_credit`, and `treasury_received_debit` on `V2.MoneyManagement.Transaction.Flow` and `V2.MoneyManagement.TransactionEntry.TransactionDetail.Flow`
  * ⚠️ Add support for new values `treasury_credit_reversal`, `treasury_debit_reversal`, `treasury_inbound_transfer`, `treasury_issuing_authorization`, `treasury_other`, `treasury_outbound_payment`, `treasury_outbound_transfer`, `treasury_received_credit`, and `treasury_received_debit` on enums `V2.MoneyManagement.Transaction.Flow.type` and `V2.MoneyManagement.TransactionEntry.TransactionDetail.Flow.type`
  * Add support for `treasury_transaction` on `V2.MoneyManagement.Transaction`
  * ⚠️ Add support for new value `no_valid_payment_method` on enum `V2.Payments.OffSessionPayment.failure_reason`
  * Add support for `metadata` on `V2.Payments.SettlementAllocationIntentSplit`
  * ⚠️ Change type of `V2.Reporting.ReportRun.Result.File.size` from `longInteger` to `int64_string`
  * Add support for `statement_descriptor` on `v2.money_management.OutboundPaymentCreateParams` and `v2.money_management.OutboundTransferCreateParams`
  * Add support for `include` on `v2.billing.IntentCreateParams`, `v2.billing.IntentReserveParams`, `v2.billing.PricingPlanSubscriptionListParams`, `v2.billing.PricingPlanSubscriptionRetrieveParams`, `v2.money_management.FinancialAccountListParams`, and `v2.money_management.FinancialAccountRetrieveParams`
  * Add support for event notifications `V1AccountSignalsIncludingDelinquencyCreatedEvent`, `V2CoreAccountSignalsFraudulentWebsiteReadyEvent`, and `V2SignalsAccountSignalFraudulentMerchantReadyEvent`

## 14.5.0a4 - 2026-03-18
* ⚠️ [#1755](https://github.com/stripe/stripe-python/pull/1755) Update generated code for private-preview
  * Add support for new resources `orchestration.PaymentAttempt` and `radar.CustomerEvaluation`
  * Add support for `retrieve` method on resource `orchestration.PaymentAttempt`
  * Add support for `create` and `modify` methods on resource `radar.CustomerEvaluation`
  * Add support for `approve` method on resource `checkout.Session`
  * Add support for `report_authenticated`, `report_canceled`, `report_failed`, `report_guaranteed`, `report_informational`, and `report_refund` methods on resource `PaymentAttemptRecord`
  * Add support for `create_us_paper_check_on_application` on `AccountSessionCreateParamsComponentCheckScanningFeature`
  * ⚠️ Change `AccountSignals.delinquency` to be optional
  * Add support for `approval_method` on `Checkout.Session` and `checkout.SessionCreateParams`
  * Add support for `current_attempt` on `Checkout.Session`
  * Add support for `selected_fulfillment_option_overrides` on `delegated_checkout.RequestedSessionModifyParamsFulfillmentDetail`
  * Add support for `pricing_plan_subscription_details` on `InvoiceItem.Parent` and `InvoiceLineItem.Parent`
  * ⚠️ Remove support for `license_fee_subscription_details` on `InvoiceItem.Parent` and `InvoiceLineItem.Parent`
  * ⚠️ Remove support for `pricing_plan_subscription` and `pricing_plan_version` on `InvoiceItem.Parent.RateCardSubscriptionDetail` and `InvoiceLineItem.Parent.RateCardSubscriptionDetail`
  * Add support for new value `pricing_plan_subscription_details` on enum `InvoiceItem.Parent.type`
  * ⚠️ Remove support for value `license_fee_subscription_details` from enum `InvoiceItem.Parent.type`
  * Add support for new value `discounts` on enum `InvoiceItem.frozen_fields`
  * Add support for new value `pricing_plan_subscription_details` on enum `InvoiceLineItem.Parent.type`
  * ⚠️ Remove support for value `license_fee_subscription_details` from enum `InvoiceLineItem.Parent.type`
  * Add support for `token_details` on `Issuing.Authorization`
  * Add support for `failure_code` on `PaymentRecordReportPaymentAttemptFailedParams`, `PaymentRecordReportPaymentAttemptParamsFailed`, and `PaymentRecordReportPaymentParamsFailed`
  * Change `PaymentRecordReportPaymentAttemptCanceledParams.canceled_at` to be optional
  * Change `PaymentRecordReportPaymentAttemptFailedParams.failed_at` to be optional
  * Change `PaymentRecordReportPaymentAttemptGuaranteedParams.guaranteed_at` to be optional
  * Change `PaymentRecordReportRefundParams.refunded` to be optional
  * ⚠️ Remove support for value `now` from enums `QuoteCreateParamsSubscriptionDataOverrideBillingScheduleBillFrom.type`, `QuoteCreateParamsSubscriptionDatumBillingScheduleBillFrom.type`, `QuoteModifyParamsSubscriptionDataOverrideBillingScheduleBillFrom.type`, and `QuoteModifyParamsSubscriptionDatumBillingScheduleBillFrom.type`
  * ⚠️ Change `radar.IssuingAuthorizationEvaluationCreateParamsCardDetail.bin_country` to be required
  * Add support for `recurring_interval` on `shared_payment.GrantedTokenCreateParamsUsageLimit`
  * Change `shared_payment.GrantedTokenCreateParamsUsageLimit.expires_at` to be optional
  * Add support for `home_rule_tax` on `Tax.Registration.CountryOption.Me` and `tax.RegistrationCreateParamsCountryOptionMe`
  * Add support for new value `home_rule_tax` on enums `Tax.Registration.CountryOption.Me.type` and `tax.RegistrationCreateParamsCountryOptionMe.type`
* [#1760](https://github.com/stripe/stripe-python/pull/1760) Update generated code for private-preview
  * Add support for `simulate_crypto_deposit` test helper method on resource `PaymentIntent`
  * Add support for `deposit_options` and `mode` on `PaymentIntent.PaymentMethodOption.Crypto`, `PaymentIntentConfirmParamsPaymentMethodOptionCrypto`, `PaymentIntentCreateParamsPaymentMethodOptionCrypto`, and `PaymentIntentModifyParamsPaymentMethodOptionCrypto`
  * Add support for `crypto_display_details` on `PaymentIntent.NextAction`

## 14.5.0a3 - 2026-03-11
* ⚠️ [#1750](https://github.com/stripe/stripe-python/pull/1750) Update generated code for private-preview
  * Add support for new resource `radar.IssuingAuthorizationEvaluation`
  * Add support for `create` method on resource `radar.IssuingAuthorizationEvaluation`
  * Add support for new value `fee_credits` on enum `BalanceTransaction.balance_type`
  * ⚠️ Rename `affiliate_attributions` to `affiliate_attribution` on `delegated_checkout.RequestedSessionConfirmParams` and `delegated_checkout.RequestedSessionCreateParams`
  * Add support for `amount_to_counter` on `Dispute`
  * Add support for `frozen_fields` on `InvoiceItem`
  * Add support for new value `next_billing_period_start` on enums `V2.Billing.IntentAction.Apply.EffectiveAt.type` and `v2.billing.IntentCreateParamsActionApplyEffectiveAt.type`
  * Add support for `consumer` on `V2.Core.Account.Configuration.CardCreator.Capability`, `V2.Core.Account.Identity.Attestation.TermsOfService.CardCreator`, `v2.core.AccountCreateParamsConfigurationCardCreatorCapability`, `v2.core.AccountCreateParamsIdentityAttestationTermsOfServiceCardCreator`, `v2.core.AccountModifyParamsConfigurationCardCreatorCapability`, and `v2.core.AccountModifyParamsIdentityAttestationTermsOfServiceCardCreator`
  * Add support for `fifth_third` on `V2.Core.Account.Configuration.CardCreator.Capability.Commercial`, `V2.Core.Account.Identity.Attestation.TermsOfService.CardCreator.Commercial`, `v2.core.AccountCreateParamsConfigurationCardCreatorCapabilityCommercial`, `v2.core.AccountCreateParamsIdentityAttestationTermsOfServiceCardCreatorCommercial`, `v2.core.AccountModifyParamsConfigurationCardCreatorCapabilityCommercial`, and `v2.core.AccountModifyParamsIdentityAttestationTermsOfServiceCardCreatorCommercial`
  * Add support for `prepaid_card` on `V2.Core.Account.Configuration.CardCreator.Capability.Commercial.CrossRiverBank`, `V2.Core.Account.Identity.Attestation.TermsOfService.CardCreator.Commercial.CrossRiverBank`, `v2.core.AccountCreateParamsConfigurationCardCreatorCapabilityCommercialCrossRiverBank`, `v2.core.AccountCreateParamsIdentityAttestationTermsOfServiceCardCreatorCommercialCrossRiverBank`, `v2.core.AccountModifyParamsConfigurationCardCreatorCapabilityCommercialCrossRiverBank`, and `v2.core.AccountModifyParamsIdentityAttestationTermsOfServiceCardCreatorCommercialCrossRiverBank`
  * Add support for new values `commercial.cross_river_bank.prepaid_card`, `commercial.fifth_third.charge_card`, `consumer.celtic.revolving_credit_card`, `consumer.cross_river_bank.prepaid_card`, and `consumer.lead.prepaid_card` on enums `V2.Core.Account.FutureRequirement.Entry.Impact.RestrictsCapability.capability` and `V2.Core.Account.Requirement.Entry.Impact.RestrictsCapability.capability`
  * Add support for `payment_method_data` on `v2.payments.OffSessionPaymentCreateParams`
  * Change `v2.payments.OffSessionPaymentCreateParams.payment_method` to be optional
  * Add support for new values `commercial.cross_river_bank.prepaid_card`, `commercial.fifth_third.charge_card`, `consumer.celtic.revolving_credit_card`, `consumer.cross_river_bank.prepaid_card`, and `consumer.lead.prepaid_card` on enum `EventsV2CoreAccountIncludingConfigurationCardCreatorCapabilityStatusUpdatedEvent.updated_capability`

## 14.5.0a2 - 2026-03-04
This release changes the pinned API version to `2026-03-04.preview`.

* ⚠️ [#1741](https://github.com/stripe/stripe-python/pull/1741) Update generated code for private-preview
  * Add support for new resources `Profile` and `billing.AlertRecovered`
  * Add support for `reauthorize` method on resource `PaymentIntent`
  * Add support for `settings` on `QuoteLine.Action.AddDiscount`, `QuoteLine.Action.AddItem.Discount`, `QuoteLine.Action.SetDiscount`, `QuoteLine.Action.SetItem.Discount`, `QuotePreviewSubscriptionSchedule.Phase.Discount`, `QuotePreviewSubscriptionSchedule.Phase.Item.Discount`, `SubscriptionSchedule.Phase.Discount`, and `SubscriptionSchedule.Phase.Item.Discount`
  * Add support for `smart_disputes` on `Account.Setting`, `AccountCreateParamsSetting`, `AccountModifyParamsSetting`, `V2.Core.Account.Configuration.Merchant`, `v2.core.AccountCreateParamsConfigurationMerchant`, and `v2.core.AccountModifyParamsConfigurationMerchant`
  * Add support for `email_customers_on_successful_payment` on `Account.Setting.Payment`, `AccountCreateParamsSettingPayment`, and `AccountModifyParamsSettingPayment`
  * Add support for `balance_update_details` on `Billing.CreditBalanceSummary.Balance`
  * Add support for `reauthorization` and `reauthorize_before` on `Charge.PaymentMethodDetail.CardPresent`, `Charge.PaymentMethodDetail.Card`, `ConfirmationToken.PaymentMethodPreview.Card.GeneratedFrom.PaymentMethodDetail.CardPresent`, `PaymentAttemptRecord.PaymentMethodDetail.CardPresent`, `PaymentMethod.Card.GeneratedFrom.PaymentMethodDetail.CardPresent`, and `PaymentRecord.PaymentMethodDetail.CardPresent`
  * Add support for `location` and `reader` on `Charge.PaymentMethodDetail.CardPresent`, `Charge.PaymentMethodDetail.InteracPresent`, `ConfirmationToken.PaymentMethodPreview.Card.GeneratedFrom.PaymentMethodDetail.CardPresent`, `PaymentAttemptRecord.PaymentMethodDetail.CardPresent`, `PaymentAttemptRecord.PaymentMethodDetail.InteracPresent`, `PaymentMethod.Card.GeneratedFrom.PaymentMethodDetail.CardPresent`, `PaymentRecord.PaymentMethodDetail.CardPresent`, and `PaymentRecord.PaymentMethodDetail.InteracPresent`
  * Add support for `managed_payments` on `Checkout.Session`, `PaymentIntent`, `SetupIntent`, `Subscription`, and `checkout.SessionCreateParams`
  * Add support for new value `lk_vat` on enums `Checkout.Session.CollectedInformation.TaxId.type`, `Checkout.Session.CustomerDetail.TaxId.type`, `Invoice.CustomerTaxId.type`, `Order.TaxDetail.TaxId.type`, `QuotePreviewInvoice.CustomerTaxId.type`, `Tax.Calculation.CustomerDetail.TaxId.type`, `Tax.Transaction.CustomerDetail.TaxId.type`, and `TaxId.type`
  * Add support for new value `lk_vat` on enums `CustomerCreateParamsTaxIdDatum.type`, `CustomerCreateTaxIdParams.type`, `InvoiceCreatePreviewParamsCustomerDetailTaxId.type`, `OrderCreateParamsTaxDetailTaxId.type`, `OrderModifyParamsTaxDetailTaxId.type`, `TaxIdCreateParams.type`, and `tax.CalculationCreateParamsCustomerDetailTaxId.type`
  * Add support for `digital` on `DelegatedCheckout.RequestedSession.FulfillmentDetail.FulfillmentOption`, `DelegatedCheckout.RequestedSession.FulfillmentDetail.SelectedFulfillmentOption`, and `delegated_checkout.RequestedSessionModifyParamsFulfillmentDetailSelectedFulfillmentOption`
  * Change `delegated_checkout.RequestedSessionModifyParamsFulfillmentDetailSelectedFulfillmentOption.shipping` to be optional
  * Add support for `affiliate_attributions` on `DelegatedCheckout.RequestedSession`, `delegated_checkout.RequestedSessionConfirmParams`, and `delegated_checkout.RequestedSessionCreateParams`
  * Add support for `fulfillment_type` on `DelegatedCheckout.RequestedSession.LineItemDetail`
  * Add support for `marketplace_seller_details`, `network_profile`, `privacy_notice_url`, `return_policy_url`, `store_policy_url`, and `terms_of_service_url` on `DelegatedCheckout.RequestedSession.SellerDetail`
  * Add support for `amount_to_counter` on `DisputeModifyParams`
  * Add support for new values `reserve.hold.created`, `reserve.hold.updated`, `reserve.plan.created`, `reserve.plan.disabled`, `reserve.plan.expired`, `reserve.plan.updated`, and `reserve.release.created` on enum `Event.type`
  * Add support for new values `terminal_wifi_certificate` and `terminal_wifi_private_key` on enums `File.purpose` and `FileListParams.purpose`
  * Add support for new values `terminal_wifi_certificate` and `terminal_wifi_private_key` on enum `FileCreateParams.purpose`
  * Add support for new value `pay_by_bank` on enums `Invoice.PaymentSetting.payment_method_types`, `InvoiceCreateParamsPaymentSetting.payment_method_types`, `InvoiceModifyParamsPaymentSetting.payment_method_types`, `QuotePreviewInvoice.PaymentSetting.payment_method_types`, `Subscription.PaymentSetting.payment_method_types`, `SubscriptionCreateParamsPaymentSetting.payment_method_types`, and `SubscriptionModifyParamsPaymentSetting.payment_method_types`
  * Add support for `display_name` and `service_user_number` on `Mandate.PaymentMethodDetail.BacsDebit`
  * ⚠️ Change type of `PaymentAttemptRecord.PaymentMethodDetail.Boleto.tax_id` and `PaymentRecord.PaymentMethodDetail.Boleto.tax_id` from `string` to `nullable(string)`
  * Change type of `PaymentAttemptRecord.PaymentMethodDetail.UsBankAccount.expected_debit_date` and `PaymentRecord.PaymentMethodDetail.UsBankAccount.expected_debit_date` from `nullable(string)` to `string`
  * Add support for `request_reauthorization` on `PaymentIntent.PaymentMethodOption.CardPresent`, `PaymentIntent.PaymentMethodOption.Card`, `PaymentIntentConfirmParamsPaymentMethodOptionCardPresent`, `PaymentIntentConfirmParamsPaymentMethodOptionCard`, `PaymentIntentCreateParamsPaymentMethodOptionCardPresent`, `PaymentIntentCreateParamsPaymentMethodOptionCard`, `PaymentIntentModifyParamsPaymentMethodOptionCardPresent`, and `PaymentIntentModifyParamsPaymentMethodOptionCard`
  * Add support for `transaction_purpose` on `PaymentIntent.PaymentMethodOption.UsBankAccount`, `PaymentIntentConfirmParamsPaymentMethodOptionUsBankAccount`, `PaymentIntentCreateParamsPaymentMethodOptionUsBankAccount`, and `PaymentIntentModifyParamsPaymentMethodOptionUsBankAccount`
  * Add support for new value `requires_reauthorization` on enum `PaymentIntent.status`
  * Add support for `optional_items` on `PaymentLinkModifyParams`
  * Add support for new value `billing_schedules_invalid` on enum `Quote.StatusDetail.Stale.LastReason.type`
  * ⚠️ Remove support for `card_issuer_decline` on `Radar.PaymentEvaluation.Insight`
  * Add support for `payment_behavior` on `SubscriptionItemDeleteParams`
  * Add support for `billing_cycle_anchor` on `Subscription.TrialSetting.EndBehavior`
  * Add support for `lk` on `Tax.Registration.CountryOption` and `tax.RegistrationCreateParamsCountryOption`
  * Add support for `cellular` and `stripe_s710` on `Terminal.Configuration`, `terminal.ConfigurationCreateParams`, and `terminal.ConfigurationModifyParams`
  * Add support for new values `simulated_stripe_s710` and `stripe_s710` on enums `Terminal.Reader.device_type` and `terminal.ReaderListParams.device_type`
  * Add support for new values `reserve.hold.created`, `reserve.hold.updated`, `reserve.plan.created`, `reserve.plan.disabled`, `reserve.plan.expired`, `reserve.plan.updated`, and `reserve.release.created` on enums `WebhookEndpointCreateParams.enabled_events` and `WebhookEndpointModifyParams.enabled_events`
  * Add support for new value `2026-02-25.clover` on enum `WebhookEndpointCreateParams.api_version`
  * Add support for new values `ar_bank_account`, `bt_bank_account`, `co_bank_account`, `cr_bank_account`, `do_bank_account`, `gt_bank_account`, `md_bank_account`, `mk_bank_account`, `mo_bank_account`, `mz_bank_account`, `pe_bank_account`, `pk_bank_account`, `tw_bank_account`, and `uz_bank_account` on enums `V2.Account.Configuration.RecipientDatum.DefaultOutboundDestination.type` and `V2.Core.Account.Configuration.Recipient.DefaultOutboundDestination.type`
  * Add support for `recipient_onboarding` and `recipient_update` on `V2.Core.AccountLink.UseCase` and `v2.core.AccountLinkCreateParamsUseCase`
  * Add support for new values `recipient_onboarding` and `recipient_update` on enums `V2.Core.AccountLink.UseCase.type` and `v2.core.AccountLinkCreateParamsUseCase.type`
  * Add support for `consumer` on `V2.Core.Account.Configuration.Storer.Capability`, `v2.core.AccountCreateParamsConfigurationStorerCapability`, and `v2.core.AccountModifyParamsConfigurationStorerCapability`
  * Add support for new value `consumer.holds_currencies.usd` on enums `V2.Core.Account.FutureRequirement.Entry.Impact.RestrictsCapability.capability` and `V2.Core.Account.Requirement.Entry.Impact.RestrictsCapability.capability`
  * Add support for `funds_usage_type` on `V2.MoneyManagement.FinancialAccount.Storage` and `v2.money_management.FinancialAccountCreateParamsStorage`
  * Add support for `purpose` on `V2.MoneyManagement.OutboundPayment` and `v2.money_management.OutboundPaymentCreateParams`
  * Add support for `branch_number` and `swift_code` on `V2.MoneyManagement.PayoutMethod.BankAccount`
  * Add support for new values `dispute`, `inbound_payment_failure`, `inbound_payment`, `india_mdr_processing_fee`, `payment_method_passthrough_fee`, `refund`, and `tax_withholding` on enums `V2.MoneyManagement.Transaction.category` and `V2.MoneyManagement.TransactionEntry.TransactionDetail.category`
  * ⚠️ Remove support for values `charge_failure` and `charge` from enums `V2.MoneyManagement.Transaction.category` and `V2.MoneyManagement.TransactionEntry.TransactionDetail.category`
  * ⚠️ Change `V2.MoneyManagement.Transaction.flow` and `V2.MoneyManagement.TransactionEntry.TransactionDetail.flow` to be optional
  * Add support for new value `consumer.holds_currencies.usd` on enum `EventsV2CoreAccountIncludingConfigurationStorerCapabilityStatusUpdatedEvent.updated_capability`
  * Add support for snapshot event `billing.alert.recovered` with resource `billing.AlertRecovered`
  * Add support for snapshot events `reserve.hold.created` and `reserve.hold.updated` with resource `reserve.Hold`
  * Add support for snapshot events `reserve.plan.created`, `reserve.plan.disabled`, `reserve.plan.expired`, and `reserve.plan.updated` with resource `reserve.Plan`
  * Add support for snapshot event `reserve.release.created` with resource `reserve.Release`
  * Add support for event notification `V2BillingRateCardCustomPricingUnitOverageRateCreatedEvent` with related object `v2.billing.RateCardCustomPricingUnitOverageRate`
  * Add support for event notifications `V2IamStripeAccessGrantApprovedEvent`, `V2IamStripeAccessGrantCanceledEvent`, `V2IamStripeAccessGrantDeniedEvent`, `V2IamStripeAccessGrantRemovedEvent`, `V2IamStripeAccessGrantRequestedEvent`, and `V2IamStripeAccessGrantUpdatedEvent`
  * Add support for error codes `storer_capability_missing` and `storer_capability_not_active` on `Invoice.LastFinalizationError`, `PaymentIntent.LastPaymentError`, `QuotePreviewInvoice.LastFinalizationError`, `SetupAttempt.SetupError`, `SetupIntent.LastSetupError`, and `StripeError`

## 14.5.0a1 - 2026-02-25
This release uses the API version `2026-01-28.preview`.

* [#1735](https://github.com/stripe/stripe-python/pull/1735) Update generated code for private-preview
  * Add support for new resource `AccountSignals`
  * Add support for `retrieve` method on resource `AccountSignals`
  * Add support for `aggregation_period`, `group_by`, and `triggered_at` on `Billing.AlertTriggered`
  * Add support for `external_account_collection` on `AccountLinkCreateParamsCollectionOption`
  * Add support for `funding_source` on `ApplicationFee`
  * Change `delegated_checkout.RequestedSessionConfirmParamsPaymentMethodDatumBillingDetailAddress.line1`, `delegated_checkout.RequestedSessionCreateParamsFulfillmentDetailAddress.line1`, `delegated_checkout.RequestedSessionCreateParamsPaymentMethodDatumBillingDetailAddress.line1`, `delegated_checkout.RequestedSessionModifyParamsFulfillmentDetailAddress.line1`, and `delegated_checkout.RequestedSessionModifyParamsPaymentMethodDatumBillingDetailAddress.line1` to be optional
  * Add support for `hosted` and `ui_mode` on `FinancialConnections.Session` and `financial_connections.SessionCreateParams`
  * Add support for `url` on `FinancialConnections.Session`
  * Add support for `billing_cycle_anchor` on `SubscriptionCreateParamsTrialSettingEndBehavior` and `SubscriptionModifyParamsTrialSettingEndBehavior`

## 14.4.0a4 - 2026-02-19
* ⚠️ [#1734](https://github.com/stripe/stripe-python/pull/1734) Update generated code for private-preview
  * ⚠️ Add support for new value `spend_threshold` on enums `Billing.Alert.alert_type`, `billing.AlertCreateParams.alert_type`, and `billing.AlertListParams.alert_type`
  * Add support for `spend_threshold` on `Billing.Alert` and `billing.AlertCreateParams`
  * Add support for `invoice_item`, `proration_details`, `proration`, and `subscription` on `InvoiceLineItem.Parent.ScheduleDetail`
  * Add support for `custom` on `PaymentMethodModifyParams`
  * Add support for `payment_method_reference` and `usage` on `PaymentMethod.Custom`
  * Add support for `outstanding_usage_through` and `unused_time_from` on `SubscriptionPauseParamsBillFor`
  * ⚠️ Remove support for `outstanding_usage` and `unused_time` on `SubscriptionPauseParamsBillFor`
  * ⚠️ Remove support for `payment_behavior` on `SubscriptionResumeParams`

## 14.4.0a3 - 2026-02-11
* [#1730](https://github.com/stripe/stripe-python/pull/1730) Update generated code for private-preview
  * Add support for new resources `v2.billing.CadenceSpendModifier`, `v2.billing.OneTimeItem`, and `v2.billing.RateCardCustomPricingUnitOverageRate`
  * Add support for `create`, `delete`, `list`, and `retrieve` methods on resource `v2.billing.RateCardCustomPricingUnitOverageRate`
  * Add support for `create`, `list`, `modify`, and `retrieve` methods on resource `v2.billing.OneTimeItem`
  * Add support for `retrieve` method on resource `v2.billing.CadenceSpendModifier`
  * Change `EventsV2CoreHealthFraudRateIncreasedEvent.Impact.RealizedFraudAmount.value`, `EventsV2CoreHealthIssuingAuthorizationRequestErrorsFiringEvent.Impact.ApprovedAmount.value`, `EventsV2CoreHealthIssuingAuthorizationRequestErrorsFiringEvent.Impact.DeclinedAmount.value`, `EventsV2CoreHealthIssuingAuthorizationRequestErrorsResolvedEvent.Impact.ApprovedAmount.value`, `EventsV2CoreHealthIssuingAuthorizationRequestErrorsResolvedEvent.Impact.DeclinedAmount.value`, `EventsV2CoreHealthIssuingAuthorizationRequestTimeoutFiringEvent.Impact.ApprovedAmount.value`, `EventsV2CoreHealthIssuingAuthorizationRequestTimeoutFiringEvent.Impact.DeclinedAmount.value`, `EventsV2CoreHealthIssuingAuthorizationRequestTimeoutResolvedEvent.Impact.ApprovedAmount.value`, `EventsV2CoreHealthIssuingAuthorizationRequestTimeoutResolvedEvent.Impact.DeclinedAmount.value`, `V2.Billing.ServiceAction.CreditGrant.Amount.Monetary.value`, `V2.Billing.ServiceAction.CreditGrantPerTenant.Amount.Monetary.value`, `V2.Core.Account.Identity.BusinessDetail.AnnualRevenue.Amount.value`, `V2.Core.Account.Identity.BusinessDetail.MonthlyEstimatedRevenue.Amount.value`, `V2.FinancialAddressGeneratedMicrodeposits.Amount.value`, `V2.MoneyManagement.Adjustment.Amount.value`, `V2.MoneyManagement.CurrencyConversion.From.Amount.value`, `V2.MoneyManagement.CurrencyConversion.To.Amount.value`, `V2.MoneyManagement.FinancialAccount.Balance.Available.value`, `V2.MoneyManagement.FinancialAccount.Balance.InboundPending.value`, `V2.MoneyManagement.FinancialAccount.Balance.OutboundPending.value`, `V2.MoneyManagement.FinancialAccount.Payment.StartingBalance.Available.value`, `V2.MoneyManagement.InboundTransfer.Amount.value`, `V2.MoneyManagement.InboundTransfer.From.Debited.value`, `V2.MoneyManagement.InboundTransfer.To.Credited.value`, `V2.MoneyManagement.OutboundPayment.Amount.value`, `V2.MoneyManagement.OutboundPayment.From.Debited.value`, `V2.MoneyManagement.OutboundPayment.To.Credited.value`, `V2.MoneyManagement.OutboundPaymentQuote.Amount.value`, `V2.MoneyManagement.OutboundPaymentQuote.EstimatedFee.Amount.value`, `V2.MoneyManagement.OutboundPaymentQuote.From.Debited.value`, `V2.MoneyManagement.OutboundPaymentQuote.To.Credited.value`, `V2.MoneyManagement.OutboundTransfer.Amount.value`, `V2.MoneyManagement.OutboundTransfer.From.Debited.value`, `V2.MoneyManagement.OutboundTransfer.To.Credited.value`, `V2.MoneyManagement.ReceivedCredit.Amount.value`, `V2.MoneyManagement.ReceivedCredit.ExternalAmount.value`, `V2.MoneyManagement.ReceivedDebit.Amount.value`, `V2.MoneyManagement.ReceivedDebit.CardSpend.Authorization.Amount.value`, `V2.MoneyManagement.ReceivedDebit.CardSpend.CardTransaction.Amount.value`, `V2.MoneyManagement.ReceivedDebit.ExternalAmount.value`, `V2.MoneyManagement.Transaction.Amount.value`, `V2.MoneyManagement.Transaction.BalanceImpact.Available.value`, `V2.MoneyManagement.Transaction.BalanceImpact.InboundPending.value`, `V2.MoneyManagement.Transaction.BalanceImpact.OutboundPending.value`, `V2.MoneyManagement.TransactionEntry.BalanceImpact.Available.value`, `V2.MoneyManagement.TransactionEntry.BalanceImpact.InboundPending.value`, `V2.MoneyManagement.TransactionEntry.BalanceImpact.OutboundPending.value`, `V2.Payments.OffSessionPayment.AmountCapturable.value`, `V2.Payments.OffSessionPayment.AmountRequested.value`, `V2.Payments.SettlementAllocationIntent.Amount.value`, `V2.Payments.SettlementAllocationIntentSplit.Amount.value`, `v2.FinancialAddressCreditSimulationCreditParamsAmount.value`, `v2.billing.ServiceActionCreateParamsCreditGrantAmountMonetary.value`, `v2.billing.ServiceActionCreateParamsCreditGrantPerTenantAmountMonetary.value`, `v2.core.AccountCreateParamsIdentityBusinessDetailAnnualRevenueAmount.value`, `v2.core.AccountCreateParamsIdentityBusinessDetailMonthlyEstimatedRevenueAmount.value`, `v2.core.AccountModifyParamsIdentityBusinessDetailAnnualRevenueAmount.value`, `v2.core.AccountModifyParamsIdentityBusinessDetailMonthlyEstimatedRevenueAmount.value`, `v2.core.AccountTokenCreateParamsIdentityBusinessDetailAnnualRevenueAmount.value`, `v2.core.AccountTokenCreateParamsIdentityBusinessDetailMonthlyEstimatedRevenueAmount.value`, `v2.money_management.CurrencyConversionCreateParamsFromAmount.value`, `v2.money_management.CurrencyConversionCreateParamsToAmount.value`, `v2.money_management.InboundTransferCreateParamsAmount.value`, `v2.money_management.OutboundPaymentCreateParamsAmount.value`, `v2.money_management.OutboundPaymentQuoteCreateParamsAmount.value`, `v2.money_management.OutboundTransferCreateParamsAmount.value`, `v2.payments.OffSessionPaymentCreateParamsAmount.value`, `v2.payments.SettlementAllocationIntentCreateParamsAmount.value`, `v2.payments.SettlementAllocationIntentModifyParamsAmount.value`, and `v2.payments.SettlementAllocationIntentSplitCreateParamsAmount.value` to be required
  * Change `EventsV2CoreHealthFraudRateIncreasedEvent.Impact.RealizedFraudAmount.currency`, `EventsV2CoreHealthIssuingAuthorizationRequestErrorsFiringEvent.Impact.ApprovedAmount.currency`, `EventsV2CoreHealthIssuingAuthorizationRequestErrorsFiringEvent.Impact.DeclinedAmount.currency`, `EventsV2CoreHealthIssuingAuthorizationRequestErrorsResolvedEvent.Impact.ApprovedAmount.currency`, `EventsV2CoreHealthIssuingAuthorizationRequestErrorsResolvedEvent.Impact.DeclinedAmount.currency`, `EventsV2CoreHealthIssuingAuthorizationRequestTimeoutFiringEvent.Impact.ApprovedAmount.currency`, `EventsV2CoreHealthIssuingAuthorizationRequestTimeoutFiringEvent.Impact.DeclinedAmount.currency`, `EventsV2CoreHealthIssuingAuthorizationRequestTimeoutResolvedEvent.Impact.ApprovedAmount.currency`, `EventsV2CoreHealthIssuingAuthorizationRequestTimeoutResolvedEvent.Impact.DeclinedAmount.currency`, `V2.Billing.ServiceAction.CreditGrant.Amount.Monetary.currency`, `V2.Billing.ServiceAction.CreditGrantPerTenant.Amount.Monetary.currency`, `V2.Core.Account.Identity.BusinessDetail.AnnualRevenue.Amount.currency`, `V2.Core.Account.Identity.BusinessDetail.MonthlyEstimatedRevenue.Amount.currency`, `V2.FinancialAddressGeneratedMicrodeposits.Amount.currency`, `V2.MoneyManagement.Adjustment.Amount.currency`, `V2.MoneyManagement.CurrencyConversion.From.Amount.currency`, `V2.MoneyManagement.CurrencyConversion.To.Amount.currency`, `V2.MoneyManagement.FinancialAccount.Balance.Available.currency`, `V2.MoneyManagement.FinancialAccount.Balance.InboundPending.currency`, `V2.MoneyManagement.FinancialAccount.Balance.OutboundPending.currency`, `V2.MoneyManagement.FinancialAccount.Payment.StartingBalance.Available.currency`, `V2.MoneyManagement.InboundTransfer.Amount.currency`, `V2.MoneyManagement.InboundTransfer.From.Debited.currency`, `V2.MoneyManagement.InboundTransfer.To.Credited.currency`, `V2.MoneyManagement.OutboundPayment.Amount.currency`, `V2.MoneyManagement.OutboundPayment.From.Debited.currency`, `V2.MoneyManagement.OutboundPayment.To.Credited.currency`, `V2.MoneyManagement.OutboundPaymentQuote.Amount.currency`, `V2.MoneyManagement.OutboundPaymentQuote.EstimatedFee.Amount.currency`, `V2.MoneyManagement.OutboundPaymentQuote.From.Debited.currency`, `V2.MoneyManagement.OutboundPaymentQuote.To.Credited.currency`, `V2.MoneyManagement.OutboundTransfer.Amount.currency`, `V2.MoneyManagement.OutboundTransfer.From.Debited.currency`, `V2.MoneyManagement.OutboundTransfer.To.Credited.currency`, `V2.MoneyManagement.ReceivedCredit.Amount.currency`, `V2.MoneyManagement.ReceivedCredit.ExternalAmount.currency`, `V2.MoneyManagement.ReceivedDebit.Amount.currency`, `V2.MoneyManagement.ReceivedDebit.CardSpend.Authorization.Amount.currency`, `V2.MoneyManagement.ReceivedDebit.CardSpend.CardTransaction.Amount.currency`, `V2.MoneyManagement.ReceivedDebit.ExternalAmount.currency`, `V2.MoneyManagement.Transaction.Amount.currency`, `V2.MoneyManagement.Transaction.BalanceImpact.Available.currency`, `V2.MoneyManagement.Transaction.BalanceImpact.InboundPending.currency`, `V2.MoneyManagement.Transaction.BalanceImpact.OutboundPending.currency`, `V2.MoneyManagement.TransactionEntry.BalanceImpact.Available.currency`, `V2.MoneyManagement.TransactionEntry.BalanceImpact.InboundPending.currency`, `V2.MoneyManagement.TransactionEntry.BalanceImpact.OutboundPending.currency`, `V2.Payments.OffSessionPayment.AmountCapturable.currency`, `V2.Payments.OffSessionPayment.AmountRequested.currency`, `V2.Payments.SettlementAllocationIntent.Amount.currency`, `V2.Payments.SettlementAllocationIntentSplit.Amount.currency`, `v2.FinancialAddressCreditSimulationCreditParamsAmount.currency`, `v2.billing.ServiceActionCreateParamsCreditGrantAmountMonetary.currency`, `v2.billing.ServiceActionCreateParamsCreditGrantPerTenantAmountMonetary.currency`, `v2.core.AccountCreateParamsIdentityBusinessDetailAnnualRevenueAmount.currency`, `v2.core.AccountCreateParamsIdentityBusinessDetailMonthlyEstimatedRevenueAmount.currency`, `v2.core.AccountModifyParamsIdentityBusinessDetailAnnualRevenueAmount.currency`, `v2.core.AccountModifyParamsIdentityBusinessDetailMonthlyEstimatedRevenueAmount.currency`, `v2.core.AccountTokenCreateParamsIdentityBusinessDetailAnnualRevenueAmount.currency`, `v2.core.AccountTokenCreateParamsIdentityBusinessDetailMonthlyEstimatedRevenueAmount.currency`, `v2.money_management.CurrencyConversionCreateParamsFromAmount.currency`, `v2.money_management.CurrencyConversionCreateParamsToAmount.currency`, `v2.money_management.InboundTransferCreateParamsAmount.currency`, `v2.money_management.OutboundPaymentCreateParamsAmount.currency`, `v2.money_management.OutboundPaymentQuoteCreateParamsAmount.currency`, `v2.money_management.OutboundTransferCreateParamsAmount.currency`, `v2.payments.OffSessionPaymentCreateParamsAmount.currency`, `v2.payments.SettlementAllocationIntentCreateParamsAmount.currency`, `v2.payments.SettlementAllocationIntentModifyParamsAmount.currency`, and `v2.payments.SettlementAllocationIntentSplitCreateParamsAmount.currency` to be required
  * Add support for `settlement_type` on `ApplicationFee`
  * Add support for `rate_card_custom_pricing_unit_overage_rate_details` on `InvoiceItem.Pricing` and `InvoiceLineItem.Pricing`
  * Add support for new value `rate_card_custom_pricing_unit_overage_rate_details` on enums `InvoiceItem.Pricing.type` and `InvoiceLineItem.Pricing.type`
  * Add support for `default_settings` on `InvoiceCreatePreviewParamsScheduleDetail`
  * Change type of `QuoteModifyParamsSubscriptionDataOverride.billing_schedules` from `emptyable(array(billing_schedules_update_specs))` to `array(billing_schedules_update_specs)`
  * Add support for `payment_behavior` on `SubscriptionResumeParams`
  * Add support for `effective_at` and `spend_modifier_rule` on `V2.Billing.IntentAction.Apply`, `V2.Billing.IntentAction.Remove`, `v2.billing.IntentCreateParamsActionApply`, and `v2.billing.IntentCreateParamsActionRemove`
  * Change type of `V2.Billing.IntentAction.Apply.type`, `V2.Billing.IntentAction.Remove.type`, `v2.billing.IntentCreateParamsActionApply.type`, and `v2.billing.IntentCreateParamsActionRemove.type` from `literal('invoice_discount_rule')` to `enum('invoice_discount_rule'|'spend_modifier_rule')`

## 14.4.0a2 - 2026-02-04
* [#1728](https://github.com/stripe/stripe-python/pull/1728) Update generated code for private-preview
  * Add support for new resource `v2.core.ConnectionSession`
  * Add support for `create` and `retrieve` methods on resource `v2.core.ConnectionSession`
  * Add support for `list` method on resources `v2.payments.SettlementAllocationIntentSplit` and `v2.payments.SettlementAllocationIntent`
  * Add support for `agentic_commerce_settings` on `AccountSessionCreateParamsComponent`
  * Add support for `terminal_hardware_orders` and `terminal_hardware_shop` on `AccountSession.Component` and `AccountSessionCreateParamsComponent`
  * Add support for `network_cost_passthrough_report` on `AccountSession.Component`
  * Add support for new values `ae_bank_account`, `ag_bank_account`, `bh_bank_account`, `gm_bank_account`, `hk_bank_account`, `kh_bank_account`, `lc_bank_account`, `mc_bank_account`, `mg_bank_account`, `my_bank_account`, `qa_bank_account`, `rw_bank_account`, `th_bank_account`, `tt_bank_account`, and `vn_bank_account` on enums `V2.Account.Configuration.RecipientDatum.DefaultOutboundDestination.type` and `V2.Core.Account.Configuration.Recipient.DefaultOutboundDestination.type`
  * Add support for `cadence_data` on `V2.Billing.Intent` and `v2.billing.IntentCreateParams`
  * Add support for `cancellation_details` on `V2.Billing.IntentAction.Deactivate`, `V2.Billing.PricingPlanSubscription`, and `v2.billing.IntentCreateParamsActionDeactivate`
  * Add support for `contact_phone` on `V2.Core.Account`, `v2.core.AccountCreateParams`, `v2.core.AccountModifyParams`, and `v2.core.AccountTokenCreateParams`
  * Add support for `registration_date` on `V2.Core.Account.Identity.BusinessDetail`, `v2.core.AccountCreateParamsIdentityBusinessDetail`, `v2.core.AccountModifyParamsIdentityBusinessDetail`, and `v2.core.AccountTokenCreateParamsIdentityBusinessDetail`
  * Add support for new value `gb_vat` on enums `V2.Core.Account.Identity.BusinessDetail.IdNumber.type`, `v2.core.AccountCreateParamsIdentityBusinessDetailIdNumber.type`, `v2.core.AccountModifyParamsIdentityBusinessDetailIdNumber.type`, and `v2.core.AccountTokenCreateParamsIdentityBusinessDetailIdNumber.type`
  * Add support for `reference` on `V2.MoneyManagement.Adjustment`
  * Add support for `accrued_fees` on `V2.MoneyManagement.FinancialAccount`
  * Add support for `starting_balance` on `V2.MoneyManagement.FinancialAccount.Payment`
  * Add support for new value `accrued_fees` on enum `V2.MoneyManagement.FinancialAccount.type`
  * Add support for `account_holder_address` and `account_holder_name` on `V2.MoneyManagement.FinancialAddress.Credential.UsBankAccount`
  * Add support for `fingerprint` on `V2.MoneyManagement.PayoutMethod.Card`
  * Add support for `card_spend` on `V2.MoneyManagement.ReceivedCredit` and `V2.MoneyManagement.ReceivedDebit`
  * Add support for new value `card_spend` on enum `V2.MoneyManagement.ReceivedCredit.type`
  * Add support for new value `card_spend` on enum `V2.MoneyManagement.ReceivedDebit.type`
  * Add support for new values `advance`, `anticipation_repayment`, `balance_transfer`, `charge_failure`, `charge`, `climate_order_purchase`, `climate_order_refund`, `connect_collection_transfer`, `connect_reserved_funds`, `contribution`, `dispute_reversal`, `financing_paydown_reversal`, `financing_paydown`, `inbound_transfer_reversal`, `issuing_dispute_fraud_liability_debit`, `issuing_dispute_provisional_credit_reversal`, `issuing_dispute_provisional_credit`, `issuing_dispute`, `minimum_balance_hold`, `network_cost`, `obligation`, `outbound_payment_reversal`, `outbound_transfer_reversal`, `partial_capture_reversal`, `payment_network_reserved_funds`, `platform_earning_refund`, `platform_earning`, `platform_fee`, `received_credit_reversal`, `received_debit_reversal`, `refund_failure`, `risk_reserved_funds`, `stripe_balance_payment_debit_reversal`, `stripe_balance_payment_debit`, `stripe_fee_tax`, `transfer_reversal`, and `unreconciled_customer_funds` on enums `V2.MoneyManagement.Transaction.category` and `V2.MoneyManagement.TransactionEntry.TransactionDetail.category`
  * Add support for `application_fee_refund`, `application_fee`, `charge`, `dispute`, `payout`, `refund`, `reserve_hold`, `reserve_release`, `topup`, `transfer_reversal`, and `transfer` on `V2.MoneyManagement.Transaction.Flow` and `V2.MoneyManagement.TransactionEntry.TransactionDetail.Flow`
  * Add support for new values `application_fee_refund`, `application_fee`, `charge`, `dispute`, `payout`, `refund`, `reserve_hold`, `reserve_release`, `topup`, `transfer_reversal`, and `transfer` on enums `V2.MoneyManagement.Transaction.Flow.type` and `V2.MoneyManagement.TransactionEntry.TransactionDetail.Flow.type`
  * Change `V2.Payments.SettlementAllocationIntentSplit.flow` to be optional
  * Add support for new value `accrued_fees` on enum `v2.money_management.FinancialAccountListParams.types`
  * Change `v2.billing.RateCardRateCreateParams.metered_item` to be required
  * Add support for error codes `blocked_payout_method` and `unsupported_payout_method` on `BlockedByStripeError`
  * Add support for error code `invalid_payout_method_data` on `InvalidPayoutMethodError`
  * Add support for error code `limit_payout_method` on `QuotaExceededError`

## 14.4.0a1 - 2026-01-28
This release changes the pinned API version to `2026-01-28.preview`.

* [#1726](https://github.com/stripe/stripe-python/pull/1726) Update generated code for private-preview
  * Add support for new resources `FrMealVouchersOnboarding`, `reserve.Hold`, `reserve.Plan`, and `reserve.Release`
  * Add support for `create`, `list`, `modify`, and `retrieve` methods on resource `FrMealVouchersOnboarding`
  * Add support for `list` and `retrieve` methods on resources `reserve.Hold` and `reserve.Release`
  * Add support for `retrieve` method on resource `reserve.Plan`
  * Add support for `pause` method on resource `Subscription`
  * Add support for `service_period_details` on `Discount`
  * Add support for `agentic_commerce_settings` on `AccountSession.Component`
  * Add support for new value `risk_reserved` on enum `BalanceTransaction.balance_type`
  * Add support for new value `service_period` on enums `Coupon.duration`, `CouponCreateParams.duration`, `checkout.SessionCreateParamsDiscountCouponDatum.duration`, and `checkout.SessionModifyParamsDiscountCouponDatum.duration`
  * Add support for `service_period` on `CouponCreateParams` and `Coupon`
  * Change type of `InvoiceItem.Pricing.PriceDetail.price` and `InvoiceLineItem.Pricing.PriceDetail.price` from `string` to `expandable($Price)`
  * Add support for `settings` on `InvoiceCreatePreviewParamsDiscount`, `InvoiceCreatePreviewParamsScheduleDetailAmendmentDiscountActionAdd`, `InvoiceCreatePreviewParamsScheduleDetailAmendmentDiscountActionSet`, `InvoiceCreatePreviewParamsScheduleDetailAmendmentItemActionAddDiscount`, `InvoiceCreatePreviewParamsScheduleDetailAmendmentItemActionSetDiscount`, `InvoiceCreatePreviewParamsScheduleDetailPhaseDiscount`, `InvoiceCreatePreviewParamsScheduleDetailPhaseItemDiscount`, `InvoiceCreatePreviewParamsSubscriptionDetailItemDiscount`, `QuoteCreateParamsLineActionAddDiscount`, `QuoteCreateParamsLineActionAddItemDiscount`, `QuoteCreateParamsLineActionSetDiscount`, `QuoteCreateParamsLineActionSetItemDiscount`, `QuoteModifyParamsLineActionAddDiscount`, `QuoteModifyParamsLineActionAddItemDiscount`, `QuoteModifyParamsLineActionSetDiscount`, `QuoteModifyParamsLineActionSetItemDiscount`, `SubscriptionCreateParamsDiscount`, `SubscriptionCreateParamsItemDiscount`, `SubscriptionItemCreateParamsDiscount`, `SubscriptionItemModifyParamsDiscount`, `SubscriptionModifyParamsDiscount`, `SubscriptionModifyParamsItemDiscount`, `SubscriptionScheduleAmendParamsAmendmentDiscountActionAdd`, `SubscriptionScheduleAmendParamsAmendmentDiscountActionSet`, `SubscriptionScheduleAmendParamsAmendmentItemActionAddDiscount`, `SubscriptionScheduleAmendParamsAmendmentItemActionSetDiscount`, `SubscriptionScheduleCreateParamsPhaseDiscount`, `SubscriptionScheduleCreateParamsPhaseItemDiscount`, `SubscriptionScheduleModifyParamsPhaseDiscount`, and `SubscriptionScheduleModifyParamsPhaseItemDiscount`
  * Add support for `subtotal` on `InvoiceLineItem`
  * Add support for `billing_cadence` on `SubscriptionListParams`

## 14.3.0a1 - 2026-01-21
* [#1723](https://github.com/stripe/stripe-python/pull/1723) Update generated code for private-preview
  * Remove support for `pause` method on resource `Subscription`
  * Change type of `Quote.SubscriptionDataOverride.phase_effective_at` and `Quote.SubscriptionDatum.phase_effective_at` from `enum('billing_period_start'|'phase_start')` to `nullable(enum('billing_period_start'|'phase_start'))`

## 14.2.0a3 - 2026-01-14
* [#1718](https://github.com/stripe/stripe-python/pull/1718) Update generated code for private-preview
  * Add support for `risk_details` on `DelegatedCheckout.RequestedSession`
  * Remove support for `description`, `images`, and `name` on `DelegatedCheckout.RequestedSession.LineItemDetail`
  * Add support for `name` on `ProductCatalog.TrialOffer` and `product_catalog.TrialOfferCreateParams`
  * Add support for `login_failed` and `registration_failed` on `Radar.AccountEvaluation.Event` and `radar.AccountEvaluationModifyParams`
  * Change type of `radar.AccountEvaluationModifyParams.type` from `literal('registration_succeeded')` to `enum('login_failed'|'login_succeeded'|'registration_failed'|'registration_succeeded')`

## 14.2.0a2 - 2026-01-07
* [#1698](https://github.com/stripe/stripe-python/pull/1698) Update generated code for private-preview
  * Add support for new resource `tax.Location`
  * Add support for `create`, `list`, and `retrieve` methods on resource `tax.Location`
  * Add support for `pause` method on resource `Subscription`
  * Add support for `performance_location` on `InvoiceAddLinesParamsLinePriceDatumProductDatumTaxDetail`, `InvoiceLineItemModifyParamsPriceDatumProductDatumTaxDetail`, `InvoiceUpdateLinesParamsLinePriceDatumProductDatumTaxDetail`, `PaymentLinkCreateParamsLineItemPriceDatumProductDatumTaxDetail`, `ProductCreateParamsTaxDetail`, `ProductModifyParamsTaxDetail`, `Tax.CalculationLineItem`, `checkout.SessionCreateParamsLineItemPriceDatumProductDatumTaxDetail`, `checkout.SessionModifyParamsLineItemPriceDatumProductDatumTaxDetail`, and `tax.CalculationCreateParamsLineItem`
  * Add support for new value `performance` on enums `Tax.Calculation.ShippingCost.TaxBreakdown.sourcing`, `Tax.CalculationLineItem.TaxBreakdown.sourcing`, and `Tax.Transaction.ShippingCost.TaxBreakdown.sourcing`
  * Add support for new values `admissions_tax`, `attendance_tax`, `entertainment_tax`, `gross_receipts_tax`, `hospitality_tax`, `luxury_tax`, `resort_tax`, and `tourism_tax` on enums `Tax.Calculation.ShippingCost.TaxBreakdown.TaxRateDetail.tax_type`, `Tax.Calculation.TaxBreakdown.TaxRateDetail.tax_type`, `Tax.CalculationLineItem.TaxBreakdown.TaxRateDetail.tax_type`, and `Tax.Transaction.ShippingCost.TaxBreakdown.TaxRateDetail.tax_type`
  * Change type of `delegated_checkout.RequestedSessionModifyParams.metadata` from `map(string: string)` to `emptyable(map(string: string))`
  * Change type of `delegated_checkout.RequestedSessionModifyParams.payment_method_data` from `payment_method_data` to `emptyable(payment_method_data)`
  * Change type of `delegated_checkout.RequestedSessionModifyParams.shared_metadata` from `map(string: string)` to `emptyable(map(string: string))`
  * Add support for `subscription` on `Invoice.Parent.ScheduleDetail` and `QuotePreviewInvoice.Parent.ScheduleDetail`
  * Change type of `PaymentIntentConfirmParamsPaymentDetailBenefit.fr_meal_voucher`, `PaymentIntentCreateParamsPaymentDetailBenefit.fr_meal_voucher`, `PaymentIntentModifyParamsPaymentDetailBenefit.fr_meal_voucher`, `SetupIntentConfirmParamsSetupDetailBenefit.fr_meal_voucher`, `SetupIntentCreateParamsSetupDetailBenefit.fr_meal_voucher`, and `SetupIntentModifyParamsSetupDetailBenefit.fr_meal_voucher` from `payment_details_benefit_fr_meal_voucher` to `emptyable(payment_details_benefit_fr_meal_voucher)`
  * Add support for `tax_details` on `PlanCreateParamsProduct` and `PriceCreateParamsProductDatum`
  * Add support for `external_reference` on `Plan` and `Price`
  * Add support for new value `phase_start` on enums `Quote.SubscriptionDataOverride.phase_effective_at`, `Quote.SubscriptionDatum.phase_effective_at`, `QuoteCreateParamsSubscriptionDataOverride.phase_effective_at`, `QuoteCreateParamsSubscriptionDatum.phase_effective_at`, `QuoteModifyParamsSubscriptionDataOverride.phase_effective_at`, and `QuoteModifyParamsSubscriptionDatum.phase_effective_at`
  * Remove support for value `line_start` from enums `Quote.SubscriptionDataOverride.phase_effective_at`, `Quote.SubscriptionDatum.phase_effective_at`, `QuoteCreateParamsSubscriptionDataOverride.phase_effective_at`, `QuoteCreateParamsSubscriptionDatum.phase_effective_at`, `QuoteModifyParamsSubscriptionDataOverride.phase_effective_at`, and `QuoteModifyParamsSubscriptionDatum.phase_effective_at`
  * Add support for new values `admissions_tax`, `attendance_tax`, `entertainment_tax`, `gross_receipts_tax`, `hospitality_tax`, `luxury_tax`, `resort_tax`, and `tourism_tax` on enums `Tax.Registration.CountryOption.Me.type` and `tax.RegistrationCreateParamsCountryOptionMe.type`
  * Add support for `admissions_tax`, `attendance_tax`, `entertainment_tax`, `gross_receipts_tax`, `hospitality_tax`, `luxury_tax`, `resort_tax`, and `tourism_tax` on `Tax.Registration.CountryOption.Me`
  * Add support for `requirements` on `TaxCode`
* [#1711](https://github.com/stripe/stripe-python/pull/1711) Update generated code for private-preview
  * Add support for `tracking_details` on `V2.MoneyManagement.OutboundPayment`
  * Add support for `paper_check` on `V2.MoneyManagement.OutboundPayment.DeliveryOption` and `v2.money_management.OutboundPaymentCreateParamsDeliveryOption`
  * Add support for event notification `V2CoreAccountIncludingFutureRequirementsUpdatedEvent` with related object `v2.core.Account`
  * Add support for error code `account_rate_limit_exceeded` on `RateLimitError`

## 14.2.0a1 - 2025-12-14
This release changes the pinned API version to `2025-12-15.preview`.

* [#1693](https://github.com/stripe/stripe-python/pull/1693) Update generated code for private-preview
  * Add support for new resources `shared_payment.GrantedToken`, `v2.iam.ApiKey`, `v2.payments.SettlementAllocationIntentSplit`, `v2.payments.SettlementAllocationIntent`, and `v2.tax.ManualRule`
  * Add support for `retrieve` method on resource `shared_payment.GrantedToken`
  * Add support for `create` and `modify` test helper methods on resource `shared_payment.GrantedToken`
  * Add support for `create`, `deactivate`, `list`, `modify`, and `retrieve` methods on resource `v2.tax.ManualRule`
  * Add support for `cancel`, `create`, `modify`, `retrieve`, and `submit` methods on resource `v2.payments.SettlementAllocationIntent`
  * Add support for `cancel`, `create`, and `retrieve` methods on resource `v2.payments.SettlementAllocationIntentSplit`
  * Add support for `create`, `expire`, `list`, `modify`, `retrieve`, and `rotate` methods on resource `v2.iam.ApiKey`
  * Add support for `check_scanning` on `AccountSessionCreateParamsComponent`
  * Add support for `tax_details` on `InvoiceAddLinesParamsLinePriceDatumProductDatum`, `InvoiceLineItemModifyParamsPriceDatumProductDatum`, `InvoiceUpdateLinesParamsLinePriceDatumProductDatum`, `PaymentLinkCreateParamsLineItemPriceDatumProductDatum`, `ProductCreateParams`, `ProductModifyParams`, `checkout.SessionCreateParamsLineItemPriceDatumProductDatum`, and `checkout.SessionModifyParamsLineItemPriceDatumProductDatum`
  * Add support for `payment_method_data` on `delegated_checkout.RequestedSessionConfirmParams`
  * Add support for `product_details` on `DelegatedCheckout.RequestedSession.LineItemDetail`
  * Add support for `wallets` on `issuing.CardListParams`
  * Add support for `primary_account_identifier` on `Issuing.Card.Wallet.ApplePay` and `Issuing.Card.Wallet.GooglePay`
  * Add support for `shared_payment_granted_token` on `PaymentIntentConfirmParams`, `PaymentIntentCreateParams`, and `PaymentIntent`
  * Change `ProductCatalog.TrialOffer.Duration.relative` to be optional
  * Add support for new values `al_bank_account`, `am_bank_account`, `bn_bank_account`, `bw_bank_account`, `dz_bank_account`, `gy_bank_account`, `jm_bank_account`, `jo_bank_account`, `kw_bank_account`, `lk_bank_account`, `ma_bank_account`, `om_bank_account`, and `tz_bank_account` on enum `V2.Account.Configuration.RecipientDatum.DefaultOutboundDestination.type`
  * Add support for `instant` on `V2.Account.Configuration.RecipientDatum.Feature.BankAccount`, `V2.Core.Account.Configuration.Recipient.Capability.BankAccount`, `v2.AccountCreateParamsConfigurationRecipientDatumFeatureBankAccount`, `v2.AccountModifyParamsConfigurationRecipientDatumFeatureBankAccount`, `v2.core.AccountCreateParamsConfigurationRecipientCapabilityBankAccount`, and `v2.core.AccountModifyParamsConfigurationRecipientCapabilityBankAccount`
  * Add support for new value `bank_accounts.instant` on enum `V2.Account.Requirement.Impact.required_for_features`
  * Add support for `collect_at` on `V2.Billing.IntentAction.Deactivate`, `V2.Billing.IntentAction.Modify`, `V2.Billing.IntentAction.Subscribe`, `v2.billing.IntentCreateParamsActionDeactivate`, `v2.billing.IntentCreateParamsActionModify`, and `v2.billing.IntentCreateParamsActionSubscribe`
  * Remove support for `billing_details` on `V2.Billing.IntentAction.Deactivate`, `V2.Billing.IntentAction.Modify`, `V2.Billing.IntentAction.Subscribe`, `v2.billing.IntentCreateParamsActionDeactivate`, `v2.billing.IntentCreateParamsActionModify`, and `v2.billing.IntentCreateParamsActionSubscribe`
  * Add support for `overrides` on `V2.Billing.IntentAction.Deactivate.PricingPlanSubscriptionDetail`, `V2.Billing.IntentAction.Modify.PricingPlanSubscriptionDetail`, `V2.Billing.IntentAction.Subscribe.PricingPlanSubscriptionDetail`, `v2.billing.IntentCreateParamsActionDeactivatePricingPlanSubscriptionDetail`, `v2.billing.IntentCreateParamsActionModifyPricingPlanSubscriptionDetail`, and `v2.billing.IntentCreateParamsActionSubscribePricingPlanSubscriptionDetail`
  * Remove support for `requested` on `V2.Core.Account.Configuration.CardCreator.Capability.Commercial.Celtic.ChargeCard`, `V2.Core.Account.Configuration.CardCreator.Capability.Commercial.Celtic.SpendCard`, `V2.Core.Account.Configuration.CardCreator.Capability.Commercial.CrossRiverBank.ChargeCard`, `V2.Core.Account.Configuration.CardCreator.Capability.Commercial.CrossRiverBank.SpendCard`, `V2.Core.Account.Configuration.CardCreator.Capability.Commercial.Lead.PrepaidCard`, `V2.Core.Account.Configuration.CardCreator.Capability.Commercial.Stripe.ChargeCard`, `V2.Core.Account.Configuration.CardCreator.Capability.Commercial.Stripe.PrepaidCard`, `V2.Core.Account.Configuration.Recipient.Capability.CryptoWallet`, `V2.Core.Account.Configuration.Storer.Capability.FinancialAddress.CryptoWallet`, `V2.Core.Account.Configuration.Storer.Capability.HoldsCurrency.Usdc`, `V2.Core.Account.Configuration.Storer.Capability.OutboundPayment.CryptoWallet`, and `V2.Core.Account.Configuration.Storer.Capability.OutboundTransfer.CryptoWallet`
  * Add support for new value `bank_accounts.instant` on enums `V2.Core.Account.FutureRequirement.Entry.Impact.RestrictsCapability.capability` and `V2.Core.Account.Requirement.Entry.Impact.RestrictsCapability.capability`
  * Add support for `alternative_reference` on `V2.Core.Vault.GbBankAccount`, `V2.Core.Vault.UsBankAccount`, and `V2.MoneyManagement.PayoutMethod`
  * Add support for `managed_by` and `payments` on `V2.MoneyManagement.FinancialAccount`
  * Add support for new value `payments` on enum `V2.MoneyManagement.FinancialAccount.type`
  * Add support for `speed` on `V2.MoneyManagement.OutboundPayment.DeliveryOption`, `V2.MoneyManagement.OutboundPaymentQuote.DeliveryOption`, `v2.money_management.OutboundPaymentCreateParamsDeliveryOption`, and `v2.money_management.OutboundPaymentQuoteCreateParamsDeliveryOption`
  * Add support for new value `real_time_payout_fee` on enum `V2.MoneyManagement.OutboundPaymentQuote.EstimatedFee.type`
  * Add support for `types` on `v2.money_management.FinancialAccountListParams`
  * Change type of `v2.core.AccountListParams.applied_configurations` from `string` to `enum`
  * Add support for new value `bank_accounts.instant` on enum `EventsV2CoreAccountIncludingConfigurationRecipientCapabilityStatusUpdatedEvent.updated_capability`
  * Add support for `top_impacted_accounts` on `EventsV2CoreHealthApiErrorFiringEvent.Impact`, `EventsV2CoreHealthApiErrorResolvedEvent.Impact`, `EventsV2CoreHealthApiLatencyFiringEvent.Impact`, `EventsV2CoreHealthApiLatencyResolvedEvent.Impact`, `EventsV2CoreHealthPaymentMethodErrorFiringEvent.Impact`, and `EventsV2CoreHealthPaymentMethodErrorResolvedEvent.Impact`
  * Add support for event notifications `V2CoreHealthSepaDebitDelayedFiringEvent`, `V2CoreHealthSepaDebitDelayedResolvedEvent`, and `V2PaymentsSettlementAllocationIntentNotFoundEvent`
  * Add support for event notifications `V2PaymentsSettlementAllocationIntentCanceledEvent`, `V2PaymentsSettlementAllocationIntentCreatedEvent`, `V2PaymentsSettlementAllocationIntentErroredEvent`, `V2PaymentsSettlementAllocationIntentFundsNotReceivedEvent`, `V2PaymentsSettlementAllocationIntentMatchedEvent`, `V2PaymentsSettlementAllocationIntentSettledEvent`, and `V2PaymentsSettlementAllocationIntentSubmittedEvent` with related object `v2.payments.SettlementAllocationIntent`
  * Add support for event notifications `V2PaymentsSettlementAllocationIntentSplitCanceledEvent`, `V2PaymentsSettlementAllocationIntentSplitCreatedEvent`, and `V2PaymentsSettlementAllocationIntentSplitSettledEvent` with related object `v2.payments.SettlementAllocationIntentSplit`
  * Remove support for error code `account_rate_limit_exceeded` on `RateLimitError`

## 14.1.0a4 - 2025-12-04
* [#1691](https://github.com/stripe/stripe-python/pull/1691) Update generated code for private-preview
  * Add support for event notifications `V2IamApiKeyCreatedEvent`, `V2IamApiKeyDefaultSecretRevealedEvent`, `V2IamApiKeyExpiredEvent`, `V2IamApiKeyPermissionsUpdatedEvent`, `V2IamApiKeyRotatedEvent`, and `V2IamApiKeyUpdatedEvent`
* [#1686](https://github.com/stripe/stripe-python/pull/1686) Update generated code for private-preview
  * Add support for `check_scanning` on `AccountSession.Component`
  * Add support for `client` on `V2.Core.Event.Reason.Request`
  * Add support for `stripe_balance_payment` on `V2.MoneyManagement.ReceivedCredit` and `V2.MoneyManagement.ReceivedDebit`
  * Add support for new value `stripe_balance_payment` on enum `V2.MoneyManagement.ReceivedCredit.type`
  * Add support for `balance_transfer` on `V2.MoneyManagement.ReceivedDebit`
  * Add support for new values `balance_transfer` and `stripe_balance_payment` on enum `V2.MoneyManagement.ReceivedDebit.type`
  * Add support for `include` on `v2.core.EventListParams` and `v2.core.EventRetrieveParams`

## 14.1.0a3 - 2025-11-24
* [#1685](https://github.com/stripe/stripe-python/pull/1685) Update generated code for private-preview
  * Add support for new resource `product_catalog.TrialOffer`
  * Add support for `create` method on resource `product_catalog.TrialOffer`
  * Remove support for `amount_subtotal_after_discount` on `DelegatedCheckout.RequestedSession.LineItemDetail` and `DelegatedCheckout.RequestedSession.TotalDetail`
  * Remove support for `amount_total`, `unit_amount_after_discount`, and `unit_discount` on `DelegatedCheckout.RequestedSession.LineItemDetail`
  * Add support for `amount_cart_discount` and `amount_items_discount` on `DelegatedCheckout.RequestedSession.TotalDetail`
  * Remove support for `amount_discount` on `DelegatedCheckout.RequestedSession.TotalDetail`
  * Add support for `payments_orchestration` on `PaymentIntentCreateParams` and `PaymentIntent`

## 14.1.0a2 - 2025-11-20
This release changes the pinned API version to `2025-11-17.preview`.

* [#1679](https://github.com/stripe/stripe-python/pull/1679) Update generated code for private-preview
  * Add support for new resources `v2.core.AccountPersonToken`, `v2.core.AccountToken`, and `v2.money_management.CurrencyConversion`
  * Add support for `create`, `list`, and `retrieve` methods on resource `v2.money_management.CurrencyConversion`
  * Add support for `create` and `retrieve` methods on resources `v2.core.AccountPersonToken` and `v2.core.AccountToken`
  * Add support for `effective_at` on `InvoiceCreatePreviewParamsScheduleDetailAmendment`, `InvoiceCreatePreviewParamsScheduleDetailPhase`, `QuoteCreateParamsLine`, `QuoteLine`, `QuoteModifyParamsLine`, `QuotePreviewSubscriptionSchedule.Phase`, `SubscriptionSchedule.Phase`, `SubscriptionScheduleAmendParamsAmendment`, `SubscriptionScheduleCreateParamsPhase`, and `SubscriptionScheduleModifyParamsPhase`
  * Add support for `trial_offer` on `InvoiceCreatePreviewParamsScheduleDetailAmendmentItemActionAdd`, `InvoiceCreatePreviewParamsScheduleDetailAmendmentItemActionSet`, `InvoiceCreatePreviewParamsScheduleDetailPhaseItem`, `QuoteCreateParamsLineActionAddItem`, `QuoteCreateParamsLineActionSetItem`, `QuoteLine.Action.AddItem`, `QuoteLine.Action.SetItem`, `QuoteModifyParamsLineActionAddItem`, `QuoteModifyParamsLineActionSetItem`, `QuotePreviewSubscriptionSchedule.Phase.Item`, `SubscriptionSchedule.Phase.Item`, `SubscriptionScheduleAmendParamsAmendmentItemActionAdd`, `SubscriptionScheduleAmendParamsAmendmentItemActionSet`, `SubscriptionScheduleCreateParamsPhaseItem`, and `SubscriptionScheduleModifyParamsPhaseItem`
  * Change type of `DelegatedCheckout.RequestedSession.amount_subtotal` from `longInteger` to `nullable(longInteger)`
  * Change type of `DelegatedCheckout.RequestedSession.amount_total` from `longInteger` to `nullable(longInteger)`
  * Add support for `amount_discount`, `amount_subtotal`, `amount_total`, `unit_amount_after_discount`, and `unit_discount` on `DelegatedCheckout.RequestedSession.LineItemDetail`
  * Add support for `amount_subtotal_after_discount` on `DelegatedCheckout.RequestedSession.LineItemDetail` and `DelegatedCheckout.RequestedSession.TotalDetail`
  * Change type of `InvoiceCreatePreviewParamsScheduleDetail.billing_schedules` from `array(billing_schedules_update_params)` to `emptyable(array(billing_schedules_update_params))`
  * Remove support for values `amendment_end`, `line_ends_at`, `schedule_end`, and `upcoming_invoice` from enums `InvoiceCreatePreviewParamsSubscriptionDetailBillingScheduleBillUntil.type`, `Subscription.BillingSchedule.BillUntil.type`, `SubscriptionCreateParamsBillingScheduleBillUntil.type`, `SubscriptionModifyParamsBillingScheduleBillUntil.type`, `SubscriptionScheduleCreateParamsBillingScheduleBillUntil.type`, and `SubscriptionScheduleModifyParamsBillingScheduleBillUntil.type`
  * Add support for `current_trial` on `InvoiceCreatePreviewParamsSubscriptionDetailItem`, `SubscriptionCreateParamsItem`, `SubscriptionItemCreateParams`, `SubscriptionItemModifyParams`, `SubscriptionItem`, and `SubscriptionModifyParamsItem`
  * Change type of `QuoteCreateParamsSubscriptionDataOverride.billing_schedules` and `QuoteCreateParamsSubscriptionDatum.billing_schedules` from `emptyable(array(billing_schedules_create_specs))` to `array(billing_schedules_create_specs)`
  * Add support for new value `line_start` on enums `QuoteCreateParamsSubscriptionDataOverride.phase_effective_at`, `QuoteCreateParamsSubscriptionDatum.phase_effective_at`, `QuoteModifyParamsSubscriptionDataOverride.phase_effective_at`, and `QuoteModifyParamsSubscriptionDatum.phase_effective_at`
  * Remove support for value `phase_start` from enums `QuoteCreateParamsSubscriptionDataOverride.phase_effective_at`, `QuoteCreateParamsSubscriptionDatum.phase_effective_at`, `QuoteModifyParamsSubscriptionDataOverride.phase_effective_at`, and `QuoteModifyParamsSubscriptionDatum.phase_effective_at`
  * Change type of `Quote.SubscriptionDataOverride.billing_schedules` and `Quote.SubscriptionDatum.billing_schedules` from `nullable(array(SubscriptionsResourceBillingSchedules))` to `array(QuotesResourceSubscriptionDataBillingSchedules)`
  * Change type of `Quote.SubscriptionDataOverride.phase_effective_at` and `Quote.SubscriptionDatum.phase_effective_at` from `nullable(enum('billing_period_start'|'phase_start'))` to `enum('billing_period_start'|'line_start')`
  * Change type of `QuotePreviewSubscriptionSchedule.DefaultSetting.phase_effective_at` and `SubscriptionSchedule.DefaultSetting.phase_effective_at` from `nullable(enum('billing_period_start'|'phase_start'))` to `enum('billing_period_start'|'phase_start')`
  * Change type of `QuotePreviewSubscriptionSchedule.billing_schedules` and `SubscriptionSchedule.billing_schedules` from `nullable(array(SubscriptionsResourceBillingSchedules))` to `array(SubscriptionsResourceBillingSchedules)`
  * Remove support for `amendment_start`, `line_starts_at`, and `relative` on `Subscription.BillingSchedule.BillFrom`
  * Change type of `Subscription.BillingSchedule.BillFrom.computed_timestamp` from `nullable(DateTime)` to `DateTime`
  * Change type of `Subscription.BillingSchedule.BillFrom.type` from `enum` to `literal('timestamp')`
  * Remove support for `amendment_end` and `line_ends_at` on `Subscription.BillingSchedule.BillUntil`
  * Change type of `V2.Billing.ServiceAction.CreditGrant.Amount.monetary`, `V2.Billing.ServiceAction.CreditGrantPerTenant.Amount.monetary`, `v2.billing.ServiceActionCreateParamsCreditGrantAmount.monetary`, and `v2.billing.ServiceActionCreateParamsCreditGrantPerTenantAmount.monetary` from `amount` to `an object`
  * Add support for `future_requirements` on `V2.Core.Account`
  * Add support for `konbini_payments` and `script_statement_descriptor` on `V2.Core.Account.Configuration.Merchant`, `v2.core.AccountCreateParamsConfigurationMerchant`, and `v2.core.AccountModifyParamsConfigurationMerchant`
  * Add support for `eur` on `V2.Core.Account.Configuration.Storer.Capability.HoldsCurrency`, `v2.core.AccountCreateParamsConfigurationStorerCapabilityHoldsCurrency`, and `v2.core.AccountModifyParamsConfigurationStorerCapabilityHoldsCurrency`
  * Add support for `requirements_collector` on `V2.Core.Account.Default.Responsibility`
  * Add support for new value `ar_cuit` on enums `V2.Core.Account.Identity.BusinessDetail.IdNumber.type`, `v2.core.AccountCreateParamsIdentityBusinessDetailIdNumber.type`, and `v2.core.AccountModifyParamsIdentityBusinessDetailIdNumber.type`
  * Add support for new value `ar_dni` on enums `V2.Core.Account.Identity.Individual.IdNumber.type`, `V2.Core.AccountPerson.IdNumber.type`, `v2.core.AccountCreateParamsIdentityIndividualIdNumber.type`, `v2.core.AccountModifyParamsIdentityIndividualIdNumber.type`, `v2.core.AccountPersonCreateParamsIdNumber.type`, and `v2.core.AccountPersonModifyParamsIdNumber.type`
  * Remove support for `collector` on `V2.Core.Account.Requirement`
  * Add support for new value `holds_currencies.eur` on enum `V2.Core.Account.Requirement.Entry.Impact.RestrictsCapability.capability`
  * Add support for new values `payment_method` and `person` on enum `V2.Core.Account.Requirement.Entry.Reference.type`
  * Remove support for value `resource` from enum `V2.Core.Account.Requirement.Entry.Reference.type`
  * Remove support for value `future_requirements` from enum `V2.Core.Account.Requirement.Entry.RequestedReason.code`
  * Remove support for `v1_event_id` on `V2.Core.Event`
  * Remove support for `amount_details` and `capture_method` on `V2.Payments.OffSessionPayment` and `v2.payments.OffSessionPaymentCreateParams`
  * Change type of `V2.Payments.OffSessionPayment.amount_capturable` from `amount` to `an object`
  * Change type of `V2.Payments.OffSessionPayment.amount_requested` from `amount` to `an object`
  * Change type of `v2.payments.OffSessionPaymentCreateParams.amount` from `amount` to `an object`
  * Add support for new value `best_available` on enum `v2.payments.OffSessionPaymentCreateParamsRetryDetail.retry_strategy`
  * Remove support for values `heuristic`, `scheduled`, and `smart` from enum `v2.payments.OffSessionPaymentCreateParamsRetryDetail.retry_strategy`
  * Change `v2.payments.OffSessionPaymentCreateParamsRetryDetail.retry_strategy` to be optional
  * Remove support for `destination` on `v2.payments.OffSessionPaymentCaptureParamsTransferDatum`
  * Change `v2.payments.OffSessionPaymentCaptureParams.amount_to_capture` to be optional
  * Add support for `created` on `v2.core.EventListParams`
  * Remove support for `gt`, `gte`, `lt`, and `lte` on `v2.core.EventListParams`
  * Add support for `account_token` on `v2.core.AccountCreateParams` and `v2.core.AccountModifyParams`
  * Add support for new value `future_requirements` on enums `v2.core.AccountCreateParams.include`, `v2.core.AccountModifyParams.include`, and `v2.core.AccountRetrieveParams.include`
  * Add support for `person_token` on `v2.core.AccountPersonCreateParams` and `v2.core.AccountPersonModifyParams`
  * Add support for `impacted_requests_percentage` on `EventsV2CoreHealthApiErrorFiringEvent.Impact`, `EventsV2CoreHealthApiErrorResolvedEvent.Impact`, `EventsV2CoreHealthApiLatencyFiringEvent.Impact`, `EventsV2CoreHealthApiLatencyResolvedEvent.Impact`, `EventsV2CoreHealthPaymentMethodErrorFiringEvent.Impact`, and `EventsV2CoreHealthPaymentMethodErrorResolvedEvent.Impact`
  * Add support for `context` and `related_object` on `EventsV2CoreHealthEventGenerationFailureResolvedEvent.Impact`
  * Remove support for `account`, `livemode`, `missing_delivery_attempts`, and `related_object_id` on `EventsV2CoreHealthEventGenerationFailureResolvedEvent.Impact`
  * Change type of `EventsV2CoreHealthFraudRateIncreasedEvent.Impact.realized_fraud_amount` from `amount` to `an object`
  * Change type of `EventsV2CoreHealthIssuingAuthorizationRequestErrorsFiringEvent.Impact.approved_amount`, `EventsV2CoreHealthIssuingAuthorizationRequestErrorsResolvedEvent.Impact.approved_amount`, `EventsV2CoreHealthIssuingAuthorizationRequestTimeoutFiringEvent.Impact.approved_amount`, and `EventsV2CoreHealthIssuingAuthorizationRequestTimeoutResolvedEvent.Impact.approved_amount` from `amount` to `an object`
  * Change type of `EventsV2CoreHealthIssuingAuthorizationRequestErrorsFiringEvent.Impact.declined_amount`, `EventsV2CoreHealthIssuingAuthorizationRequestErrorsResolvedEvent.Impact.declined_amount`, `EventsV2CoreHealthIssuingAuthorizationRequestTimeoutFiringEvent.Impact.declined_amount`, and `EventsV2CoreHealthIssuingAuthorizationRequestTimeoutResolvedEvent.Impact.declined_amount` from `amount` to `an object`
  * Add support for thin events `V2PaymentsOffSessionPaymentAttemptFailedEvent` and `V2PaymentsOffSessionPaymentAttemptStartedEvent` with related object `v2.payments.OffSessionPayment`
  * Remove support for thin event `V1AccountUpdatedEvent` with related object `Account`
  * Remove support for thin events `V1ApplicationFeeCreatedEvent` and `V1ApplicationFeeRefundedEvent` with related object `ApplicationFee`
  * Remove support for thin events `V1BillingPortalConfigurationCreatedEvent` and `V1BillingPortalConfigurationUpdatedEvent` with related object `billing_portal.Configuration`
  * Remove support for thin event `V1CapabilityUpdatedEvent` with related object `Capability`
  * Remove support for thin events `V1ChargeCapturedEvent`, `V1ChargeExpiredEvent`, `V1ChargeFailedEvent`, `V1ChargePendingEvent`, `V1ChargeRefundedEvent`, `V1ChargeSucceededEvent`, and `V1ChargeUpdatedEvent` with related object `Charge`
  * Remove support for thin events `V1ChargeDisputeClosedEvent`, `V1ChargeDisputeCreatedEvent`, `V1ChargeDisputeFundsReinstatedEvent`, `V1ChargeDisputeFundsWithdrawnEvent`, and `V1ChargeDisputeUpdatedEvent` with related object `Dispute`
  * Remove support for thin events `V1ChargeRefundUpdatedEvent`, `V1RefundCreatedEvent`, `V1RefundFailedEvent`, and `V1RefundUpdatedEvent` with related object `Refund`
  * Remove support for thin events `V1CheckoutSessionAsyncPaymentFailedEvent`, `V1CheckoutSessionAsyncPaymentSucceededEvent`, `V1CheckoutSessionCompletedEvent`, and `V1CheckoutSessionExpiredEvent` with related object `checkout.Session`
  * Remove support for thin events `V1ClimateOrderCanceledEvent`, `V1ClimateOrderCreatedEvent`, `V1ClimateOrderDelayedEvent`, `V1ClimateOrderDeliveredEvent`, and `V1ClimateOrderProductSubstitutedEvent` with related object `climate.Order`
  * Remove support for thin events `V1ClimateProductCreatedEvent` and `V1ClimateProductPricingUpdatedEvent` with related object `climate.Product`
  * Remove support for thin events `V1CouponCreatedEvent`, `V1CouponDeletedEvent`, and `V1CouponUpdatedEvent` with related object `Coupon`
  * Remove support for thin events `V1CreditNoteCreatedEvent`, `V1CreditNoteUpdatedEvent`, and `V1CreditNoteVoidedEvent` with related object `CreditNote`
  * Remove support for thin events `V1CustomerCreatedEvent`, `V1CustomerDeletedEvent`, and `V1CustomerUpdatedEvent` with related object `Customer`
  * Remove support for thin events `V1CustomerSubscriptionCreatedEvent`, `V1CustomerSubscriptionDeletedEvent`, `V1CustomerSubscriptionPausedEvent`, `V1CustomerSubscriptionPendingUpdateAppliedEvent`, `V1CustomerSubscriptionPendingUpdateExpiredEvent`, `V1CustomerSubscriptionResumedEvent`, `V1CustomerSubscriptionTrialWillEndEvent`, and `V1CustomerSubscriptionUpdatedEvent` with related object `Subscription`
  * Remove support for thin events `V1CustomerTaxIdCreatedEvent`, `V1CustomerTaxIdDeletedEvent`, and `V1CustomerTaxIdUpdatedEvent` with related object `TaxId`
  * Remove support for thin event `V1FileCreatedEvent` with related object `File`
  * Remove support for thin events `V1FinancialConnectionsAccountCreatedEvent`, `V1FinancialConnectionsAccountDeactivatedEvent`, `V1FinancialConnectionsAccountDisconnectedEvent`, `V1FinancialConnectionsAccountReactivatedEvent`, `V1FinancialConnectionsAccountRefreshedBalanceEvent`, `V1FinancialConnectionsAccountRefreshedOwnershipEvent`, and `V1FinancialConnectionsAccountRefreshedTransactionsEvent` with related object `financial_connections.Account`
  * Remove support for thin events `V1IdentityVerificationSessionCanceledEvent`, `V1IdentityVerificationSessionCreatedEvent`, `V1IdentityVerificationSessionProcessingEvent`, `V1IdentityVerificationSessionRedactedEvent`, `V1IdentityVerificationSessionRequiresInputEvent`, and `V1IdentityVerificationSessionVerifiedEvent` with related object `identity.VerificationSession`
  * Remove support for thin events `V1InvoiceCreatedEvent`, `V1InvoiceDeletedEvent`, `V1InvoiceFinalizationFailedEvent`, `V1InvoiceFinalizedEvent`, `V1InvoiceMarkedUncollectibleEvent`, `V1InvoiceOverdueEvent`, `V1InvoiceOverpaidEvent`, `V1InvoicePaidEvent`, `V1InvoicePaymentActionRequiredEvent`, `V1InvoicePaymentFailedEvent`, `V1InvoicePaymentSucceededEvent`, `V1InvoiceSentEvent`, `V1InvoiceUpcomingEvent`, `V1InvoiceUpdatedEvent`, `V1InvoiceVoidedEvent`, and `V1InvoiceWillBeDueEvent` with related object `Invoice`
  * Remove support for thin event `V1InvoicePaymentPaidEvent` with related object `InvoicePayment`
  * Remove support for thin events `V1InvoiceitemCreatedEvent` and `V1InvoiceitemDeletedEvent` with related object `InvoiceItem`
  * Remove support for thin events `V1IssuingAuthorizationCreatedEvent`, `V1IssuingAuthorizationRequestEvent`, and `V1IssuingAuthorizationUpdatedEvent` with related object `issuing.Authorization`
  * Remove support for thin events `V1IssuingCardCreatedEvent` and `V1IssuingCardUpdatedEvent` with related object `issuing.Card`
  * Remove support for thin events `V1IssuingCardholderCreatedEvent` and `V1IssuingCardholderUpdatedEvent` with related object `issuing.Cardholder`
  * Remove support for thin events `V1IssuingDisputeClosedEvent`, `V1IssuingDisputeCreatedEvent`, `V1IssuingDisputeFundsReinstatedEvent`, `V1IssuingDisputeFundsRescindedEvent`, `V1IssuingDisputeSubmittedEvent`, and `V1IssuingDisputeUpdatedEvent` with related object `issuing.Dispute`
  * Remove support for thin events `V1IssuingPersonalizationDesignActivatedEvent`, `V1IssuingPersonalizationDesignDeactivatedEvent`, `V1IssuingPersonalizationDesignRejectedEvent`, and `V1IssuingPersonalizationDesignUpdatedEvent` with related object `issuing.PersonalizationDesign`
  * Remove support for thin events `V1IssuingTokenCreatedEvent` and `V1IssuingTokenUpdatedEvent` with related object `issuing.Token`
  * Remove support for thin events `V1IssuingTransactionCreatedEvent`, `V1IssuingTransactionPurchaseDetailsReceiptUpdatedEvent`, and `V1IssuingTransactionUpdatedEvent` with related object `issuing.Transaction`
  * Remove support for thin event `V1MandateUpdatedEvent` with related object `Mandate`
  * Remove support for thin events `V1PaymentIntentAmountCapturableUpdatedEvent`, `V1PaymentIntentCanceledEvent`, `V1PaymentIntentCreatedEvent`, `V1PaymentIntentPartiallyFundedEvent`, `V1PaymentIntentPaymentFailedEvent`, `V1PaymentIntentProcessingEvent`, `V1PaymentIntentRequiresActionEvent`, and `V1PaymentIntentSucceededEvent` with related object `PaymentIntent`
  * Remove support for thin events `V1PaymentLinkCreatedEvent` and `V1PaymentLinkUpdatedEvent` with related object `PaymentLink`
  * Remove support for thin events `V1PaymentMethodAttachedEvent`, `V1PaymentMethodAutomaticallyUpdatedEvent`, `V1PaymentMethodDetachedEvent`, and `V1PaymentMethodUpdatedEvent` with related object `PaymentMethod`
  * Remove support for thin events `V1PayoutCanceledEvent`, `V1PayoutCreatedEvent`, `V1PayoutFailedEvent`, `V1PayoutPaidEvent`, `V1PayoutReconciliationCompletedEvent`, and `V1PayoutUpdatedEvent` with related object `Payout`
  * Remove support for thin events `V1PersonCreatedEvent`, `V1PersonDeletedEvent`, and `V1PersonUpdatedEvent` with related object `Person`
  * Remove support for thin events `V1PlanCreatedEvent`, `V1PlanDeletedEvent`, and `V1PlanUpdatedEvent` with related object `Plan`
  * Remove support for thin events `V1PriceCreatedEvent`, `V1PriceDeletedEvent`, and `V1PriceUpdatedEvent` with related object `Price`
  * Remove support for thin events `V1ProductCreatedEvent`, `V1ProductDeletedEvent`, and `V1ProductUpdatedEvent` with related object `Product`
  * Remove support for thin events `V1PromotionCodeCreatedEvent` and `V1PromotionCodeUpdatedEvent` with related object `PromotionCode`
  * Remove support for thin events `V1QuoteAcceptedEvent`, `V1QuoteCanceledEvent`, `V1QuoteCreatedEvent`, and `V1QuoteFinalizedEvent` with related object `Quote`
  * Remove support for thin events `V1RadarEarlyFraudWarningCreatedEvent` and `V1RadarEarlyFraudWarningUpdatedEvent` with related object `radar.EarlyFraudWarning`
  * Remove support for thin events `V1ReviewClosedEvent` and `V1ReviewOpenedEvent` with related object `Review`
  * Remove support for thin events `V1SetupIntentCanceledEvent`, `V1SetupIntentCreatedEvent`, `V1SetupIntentRequiresActionEvent`, `V1SetupIntentSetupFailedEvent`, and `V1SetupIntentSucceededEvent` with related object `SetupIntent`
  * Remove support for thin event `V1SigmaScheduledQueryRunCreatedEvent` with related object `sigma.ScheduledQueryRun`
  * Remove support for thin events `V1SourceCanceledEvent`, `V1SourceChargeableEvent`, `V1SourceFailedEvent`, and `V1SourceRefundAttributesRequiredEvent` with related object `Source`
  * Remove support for thin events `V1SubscriptionScheduleAbortedEvent`, `V1SubscriptionScheduleCanceledEvent`, `V1SubscriptionScheduleCompletedEvent`, `V1SubscriptionScheduleCreatedEvent`, `V1SubscriptionScheduleExpiringEvent`, `V1SubscriptionScheduleReleasedEvent`, and `V1SubscriptionScheduleUpdatedEvent` with related object `SubscriptionSchedule`
  * Remove support for thin events `V1TaxRateCreatedEvent` and `V1TaxRateUpdatedEvent` with related object `TaxRate`
  * Remove support for thin events `V1TerminalReaderActionFailedEvent`, `V1TerminalReaderActionSucceededEvent`, and `V1TerminalReaderActionUpdatedEvent` with related object `terminal.Reader`
  * Remove support for thin events `V1TestHelpersTestClockAdvancingEvent`, `V1TestHelpersTestClockCreatedEvent`, `V1TestHelpersTestClockDeletedEvent`, `V1TestHelpersTestClockInternalFailureEvent`, and `V1TestHelpersTestClockReadyEvent` with related object `test_helpers.TestClock`
  * Remove support for thin events `V1TopupCanceledEvent`, `V1TopupCreatedEvent`, `V1TopupFailedEvent`, `V1TopupReversedEvent`, and `V1TopupSucceededEvent` with related object `Topup`
  * Remove support for thin events `V1TransferCreatedEvent`, `V1TransferReversedEvent`, and `V1TransferUpdatedEvent` with related object `Transfer`

## 14.1.0a1 - 2025-11-18
This release changes the pinned API version to `2025-11-17.preview`.

* [#1674](https://github.com/stripe/stripe-python/pull/1674) Update generated code for private-preview
  * Add support for new resources `BalanceTransfer` and `radar.AccountEvaluation`
  * Add support for `create` method on resource `BalanceTransfer`
  * Add support for `create`, `modify`, and `retrieve` methods on resource `radar.AccountEvaluation`
  * Change `Tax.Association.tax_transaction_attempts` to be required
  * Add support for `specified_commercial_transactions_act_url` on `Account.BusinessProfile`, `AccountCreateParamsBusinessProfile`, and `AccountModifyParamsBusinessProfile`
  * Add support for `paypay_payments` on `Account.Setting`, `AccountCreateParamsSetting`, and `AccountModifyParamsSetting`
  * Change type of `billing.analytics.MeterUsageRetrieveParamsMeter.dimension_filters` from `string` to `array(string)`
  * Change type of `billing.analytics.MeterUsageRetrieveParamsMeter.tenant_filters` from `string` to `array(string)`
  * Add support for `payment_method_configuration` on `BillingPortal.Configuration.Feature.PaymentMethodUpdate`
  * Add support for `car_rental_data`, `flight_data`, and `lodging_data` on `ChargeCaptureParamsPaymentDetail`, `ChargeModifyParamsPaymentDetail`, `PaymentIntentCaptureParamsPaymentDetail`, `PaymentIntentConfirmParamsPaymentDetail`, `PaymentIntentCreateParamsPaymentDetail`, and `PaymentIntentModifyParamsPaymentDetail`
  * Add support for `transaction_id` on `Charge.PaymentMethodDetail.Ideal`, `PaymentAttemptRecord.PaymentMethodDetail.Ideal`, and `PaymentRecord.PaymentMethodDetail.Ideal`
  * Add support for new value `finom` on enums `Charge.PaymentMethodDetail.Ideal.bank`, `ConfirmationToken.PaymentMethodPreview.Ideal.bank`, `ConfirmationTokenCreateParamsPaymentMethodDatumIdeal.bank`, `PaymentAttemptRecord.PaymentMethodDetail.Ideal.bank`, `PaymentIntentConfirmParamsPaymentMethodDatumIdeal.bank`, `PaymentIntentCreateParamsPaymentMethodDatumIdeal.bank`, `PaymentIntentModifyParamsPaymentMethodDatumIdeal.bank`, `PaymentMethod.Ideal.bank`, `PaymentMethodCreateParamsIdeal.bank`, `PaymentRecord.PaymentMethodDetail.Ideal.bank`, `SetupAttempt.PaymentMethodDetail.Ideal.bank`, `SetupIntentConfirmParamsPaymentMethodDatumIdeal.bank`, `SetupIntentCreateParamsPaymentMethodDatumIdeal.bank`, and `SetupIntentModifyParamsPaymentMethodDatumIdeal.bank`
  * Add support for new value `FNOMNL22` on enums `Charge.PaymentMethodDetail.Ideal.bic`, `ConfirmationToken.PaymentMethodPreview.Ideal.bic`, `PaymentAttemptRecord.PaymentMethodDetail.Ideal.bic`, `PaymentMethod.Ideal.bic`, `PaymentRecord.PaymentMethodDetail.Ideal.bic`, and `SetupAttempt.PaymentMethodDetail.Ideal.bic`
  * Add support for new value `tokenized_account_number_deactivated` on enums `ConfirmationToken.PaymentMethodPreview.UsBankAccount.StatusDetail.Blocked.reason` and `PaymentMethod.UsBankAccount.StatusDetail.Blocked.reason`
  * Add support for `created` on `CustomerListCustomerBalanceTransactionParams` and `InvoicePaymentListParams`
  * Add support for new values `capital.financing_offer.accepted_other_offer`, `financial_connections.account.account_numbers_updated`, and `financial_connections.account.upcoming_account_number_expiry` on enum `Event.type`
  * Add support for `account_numbers` on `FinancialConnections.Account`
  * Change type of `FinancialConnections.Session.client_secret` from `string` to `nullable(string)`
  * Add support for `fraud_risk` on `issuing.AuthorizationCreateParamsRiskAssessment`
  * Add support for `latest_fraud_warning` on `Issuing.Card`
  * Add support for `supplementary_purchase_data` on `OrderCreateParamsPaymentSettingPaymentMethodOptionKlarna`, `OrderModifyParamsPaymentSettingPaymentMethodOptionKlarna`, `PaymentIntentConfirmParamsPaymentMethodOptionKlarna`, `PaymentIntentCreateParamsPaymentMethodOptionKlarna`, and `PaymentIntentModifyParamsPaymentMethodOptionKlarna`
  * Add support for `capture_method` on `PaymentIntent.PaymentMethodOption.CardPresent`, `PaymentIntentConfirmParamsPaymentMethodOptionCardPresent`, `PaymentIntentCreateParamsPaymentMethodOptionCardPresent`, and `PaymentIntentModifyParamsPaymentMethodOptionCardPresent`
  * Add support for `allow_redisplay` and `customer_account` on `PaymentMethodListParams`
  * Add support for `mb_way` and `twint` on `Refund.DestinationDetail`
  * Change type of `SubscriptionScheduleModifyParams.billing_schedules` from `array(billing_schedules_update_params)` to `emptyable(array(billing_schedules_update_params))`
  * Add support for new values `capital.financing_offer.accepted_other_offer`, `financial_connections.account.account_numbers_updated`, and `financial_connections.account.upcoming_account_number_expiry` on enums `WebhookEndpointCreateParams.enabled_events` and `WebhookEndpointModifyParams.enabled_events`
  * Add support for new value `2025-11-17.clover` on enum `WebhookEndpointCreateParams.api_version`
  * Add support for snapshot events `financial_connections.account.account_numbers_updated` and `financial_connections.account.upcoming_account_number_expiry` with resource `financial_connections.Account`
* [#1675](https://github.com/stripe/stripe-python/pull/1675) Update generated code for private-preview
  * Add support for `billing_schedules_actions` on `InvoiceCreatePreviewParamsScheduleDetailAmendment` and `SubscriptionScheduleAmendParamsAmendment`

## 13.3.0a2 - 2025-11-13
This release changes the pinned API version to `2025-10-29.preview`.

* [#1666](https://github.com/stripe/stripe-python/pull/1666) Update generated code for private-preview
  * Remove support for resource `v2.tax.AutomaticRule`
  * Remove support for `create`, `deactivate`, `find`, `modify`, and `retrieve` methods on resource `v2.tax.AutomaticRule`
  * Add support for `self_reported_income` and `self_reported_monthly_housing_payment` on `AccountCreateParamsIndividual`, `AccountCreatePersonParams`, `AccountModifyParamsIndividual`, `AccountModifyPersonParams`, `Person`, `TokenCreateParamsAccountIndividual`, and `TokenCreateParamsPerson`
  * Add support for new values `amendment_end`, `line_ends_at`, `schedule_end`, and `upcoming_invoice` on enums `InvoiceCreatePreviewParamsSubscriptionDetailBillingScheduleBillUntil.type`, `Subscription.BillingSchedule.BillUntil.type`, `SubscriptionCreateParamsBillingScheduleBillUntil.type`, and `SubscriptionModifyParamsBillingScheduleBillUntil.type`
  * Add support for `billing_schedules` and `phase_effective_at` on `Quote.SubscriptionDataOverride`, `Quote.SubscriptionDatum`, `QuoteCreateParamsSubscriptionDataOverride`, `QuoteCreateParamsSubscriptionDatum`, `QuoteModifyParamsSubscriptionDataOverride`, and `QuoteModifyParamsSubscriptionDatum`
  * Add support for `bill_from` on `Subscription.BillingSchedule`
  * Add support for `amendment_end` and `line_ends_at` on `Subscription.BillingSchedule.BillUntil`
  * Remove support for `data` and `related_object` on `V2.Core.Event`
* [#1672](https://github.com/stripe/stripe-python/pull/1672) Update generated code for private-preview
  * Add support for new resource `issuing.Program`
  * Add support for `create`, `list`, `modify`, and `retrieve` methods on resource `issuing.Program`
  * Add support for `schedule` on `Discount`
  * Add support for `applicable_fees` on `DelegatedCheckout.RequestedSession.TotalDetail`
  * Add support for `schedule_details` on `Invoice.Parent`, `InvoiceItem.Parent`, `InvoiceLineItem.Parent`, and `QuotePreviewInvoice.Parent`
  * Add support for new value `schedule_details` on enum `InvoiceItem.Parent.type`
  * Add support for `billing_schedules` on `InvoiceCreatePreviewParamsScheduleDetail`, `QuotePreviewSubscriptionSchedule`, `SubscriptionScheduleCreateParams`, `SubscriptionScheduleModifyParams`, and `SubscriptionSchedule`
  * Add support for new value `schedule_details` on enums `Invoice.Parent.type` and `QuotePreviewInvoice.Parent.type`
  * Add support for new value `schedule_details` on enum `InvoiceLineItem.Parent.type`
  * Add support for `latest_invoice` on `QuotePreviewSubscriptionSchedule` and `SubscriptionSchedule`
  * Add support for `phase_effective_at` on `QuotePreviewSubscriptionSchedule.DefaultSetting`, `SubscriptionSchedule.DefaultSetting`, `SubscriptionScheduleCreateParamsDefaultSetting`, and `SubscriptionScheduleModifyParamsDefaultSetting`

## 13.3.0a1 - 2025-11-06
* [#1664](https://github.com/stripe/stripe-python/pull/1664) Update generated code for private-preview
  * Add support for new resources `TransitBalance`, `v2.reporting.ReportRun`, `v2.reporting.Report`
  * Add support for `create` and `retrieve` methods on resource `v2.reporting.ReportRun`
  * Add support for `retrieve` method on resource `v2.reporting.Report`
  * Add support for `create` and `refill` test helper methods on resource `capital.FinancingOffer`
  * Add support for `allocated_funds` on `Charge`, `PaymentIntentConfirmParams`, `PaymentIntentCreateParams`, and `PaymentIntentModifyParams`
  * Add support for thin events `V2ReportingReportRunCreatedEvent`, `V2ReportingReportRunFailedEvent`, `V2ReportingReportRunSucceededEvent`, and `V2ReportingReportRunUpdatedEvent` with related object `v2.reporting.ReportRun`

## 13.2.0a2 - 2025-10-30
* [#1659](https://github.com/stripe/stripe-python/pull/1659) Update generated code for private-preview
  * Change `delegated_checkout.RequestedSessionModifyParamsLineItemDetail.quantity` to be required
  * Add support for `payment_method_preview` on `DelegatedCheckout.RequestedSession`
  * Add support for `order_id` on `DelegatedCheckout.RequestedSession.OrderDetail`
  * Add support for `lead` on `V2.Core.Account.Configuration.CardCreator.Capability.Commercial`, `V2.Core.Account.Identity.Attestation.TermsOfService.CardCreator.Commercial`, `v2.core.AccountCreateParamsConfigurationCardCreatorCapabilityCommercial`, `v2.core.AccountCreateParamsIdentityAttestationTermsOfServiceCardCreatorCommercial`, `v2.core.AccountModifyParamsConfigurationCardCreatorCapabilityCommercial`, and `v2.core.AccountModifyParamsIdentityAttestationTermsOfServiceCardCreatorCommercial`
  * Add support for `global_account_holder` on `V2.Core.Account.Identity.Attestation.TermsOfService.CardCreator.Commercial`, `v2.core.AccountCreateParamsIdentityAttestationTermsOfServiceCardCreatorCommercial`, and `v2.core.AccountModifyParamsIdentityAttestationTermsOfServiceCardCreatorCommercial`
  * Add support for new value `commercial.lead.prepaid_card` on enum `V2.Core.Account.Requirement.Entry.Impact.RestrictsCapability.capability`
  * Add support for new value `commercial.lead.prepaid_card` on enum `EventsV2CoreAccountIncludingConfigurationCardCreatorCapabilityStatusUpdatedEvent.updated_capability`

## 13.2.0a1 - 2025-10-29
* [#1654](https://github.com/stripe/stripe-python/pull/1654) Update generated code for private-preview
  * Add support for `report_refund` method on resource `PaymentRecord`
  * Add support for new value `verification_data_not_found` on enums `Account.FutureRequirement.Error.code`, `Account.Requirement.Error.code`, `BankAccount.FutureRequirement.Error.code`, `BankAccount.Requirement.Error.code`, `Capability.FutureRequirement.Error.code`, `Capability.Requirement.Error.code`, `Person.FutureRequirement.Error.code`, and `Person.Requirement.Error.code`
  * Add support for `tenants` on `Billing.Analytics.MeterUsageRow`
  * Add support for `representative_declaration` on `Account.Company`, `AccountCreateParamsCompany`, `AccountModifyParamsCompany`, and `TokenCreateParamsAccountCompany`
  * Add support for `transfer` on `ApplicationFee.FeeSource`
  * Add support for new value `transfer` on enum `ApplicationFee.FeeSource.type`
  * Add support for `transit_balances_total` on `Balance`
  * Add support for new value `transit` on enum `BalanceTransaction.balance_type`
  * Add support for `tenant_group_by_keys` on `billing.analytics.MeterUsageRetrieveParamsMeter`
  * Change `billing.CreditGrantCreateParams.category` to be optional
  * Add support for `payment_method_configuration` on `billing_portal.ConfigurationCreateParamsFeaturePaymentMethodUpdate` and `billing_portal.ConfigurationModifyParamsFeaturePaymentMethodUpdate`
  * Add support for new value `solana` on enums `Charge.PaymentMethodDetail.Crypto.network`, `PaymentAttemptRecord.PaymentMethodDetail.Crypto.network`, and `PaymentRecord.PaymentMethodDetail.Crypto.network`
  * Add support for `payment_portal_url` on `Charge.PaymentMethodDetail.Rechnung`, `PaymentAttemptRecord.PaymentMethodDetail.Rechnung`, and `PaymentRecord.PaymentMethodDetail.Rechnung`
  * Add support for `twint` on `Checkout.Session.PaymentMethodOption` and `checkout.SessionCreateParamsPaymentMethodOption`
  * Add support for new value `custom` on enums `ConfirmationToken.PaymentMethodPreview.type` and `PaymentMethod.type`
  * Change `CreditNote.Refund.payment_record_refund` to be required
  * Change `CreditNote.Refund.type` to be required
  * Add support for `customer_sheet`, `mobile_payment_element`, and `tax_id_element` on `CustomerSession.Component` and `CustomerSessionCreateParamsComponent`
  * Add support for new value `custom` on enums `CustomerListPaymentMethodsParams.type`, `PaymentMethodCreateParams.type`, and `PaymentMethodListParams.type`
  * Add support for `provider` on `Customer.Tax`
  * Remove support for `risk_details` on `delegated_checkout.RequestedSessionCreateParams`
  * Add support for `risk_details` on `delegated_checkout.RequestedSessionConfirmParams`
  * Add support for new value `platform_terms_of_service` on enums `File.purpose` and `FileListParams.purpose`
  * Add support for new value `platform_terms_of_service` on enum `FileCreateParams.purpose`
  * Add support for `starting_after` on `PaymentAttemptRecordListParams`
  * Add support for `reference` on `PaymentIntentAmountDetailsLineItem.PaymentMethodOption.Klarna`, `PaymentIntentCaptureParamsAmountDetailLineItemPaymentMethodOptionKlarna`, `PaymentIntentConfirmParamsAmountDetailLineItemPaymentMethodOptionKlarna`, `PaymentIntentCreateParamsAmountDetailLineItemPaymentMethodOptionKlarna`, `PaymentIntentIncrementAuthorizationParamsAmountDetailLineItemPaymentMethodOptionKlarna`, and `PaymentIntentModifyParamsAmountDetailLineItemPaymentMethodOptionKlarna`
  * Add support for `allocated_funds` on `PaymentIntent`
  * Change `PaymentIntent.PaymentDetail.customer_reference` to be required
  * Change `PaymentIntent.PaymentDetail.order_reference` to be required
  * Add support for `subscription_reference` on `PaymentIntentAmountDetailsLineItem.PaymentMethodOption.Klarna`
  * Add support for `name_collection` on `PaymentLinkCreateParams`, `PaymentLinkModifyParams`, and `PaymentLink`
  * Add support for `crypto` on `PaymentMethodConfigurationCreateParams`, `PaymentMethodConfigurationModifyParams`, `PaymentMethodConfiguration`, and `Refund.DestinationDetail`
  * Add support for `mb_way` on `PaymentMethodConfigurationCreateParams`, `PaymentMethodConfigurationModifyParams`, and `PaymentMethodConfiguration`
  * Add support for `custom` on `PaymentMethodCreateParams` and `PaymentMethod`
  * Add support for `excluded_payment_method_types` on `SetupIntentCreateParams`, `SetupIntentModifyParams`, and `SetupIntent`
  * Change `SetupIntent.flow_directions` to be optional
  * Add support for `tw` on `Tax.Registration.CountryOption` and `tax.RegistrationCreateParamsCountryOption`
  * Add support for `gip` on `Terminal.Configuration.Tipping`, `terminal.ConfigurationCreateParamsTipping`, and `terminal.ConfigurationModifyParamsTipping`
  * Add support for `last_seen_at` on `Terminal.Reader`
  * Add support for `application_fee_amount` on `TransferCreateParams` and `Transfer`
  * Add support for `application_fee` on `Transfer`
  * Add support for new value `2025-10-29.clover` on enum `WebhookEndpointCreateParams.api_version`
  * Add support for `high_risk_activities_description`, `high_risk_activities`, `money_services_description`, `operates_in_prohibited_countries`, `participates_in_regulated_activity`, `purpose_of_funds_description`, `purpose_of_funds`, `regulated_activity`, `source_of_funds_description`, and `source_of_funds` on `V2.Core.Account.Configuration.Storer`, `v2.core.AccountCreateParamsConfigurationStorer`, and `v2.core.AccountModifyParamsConfigurationStorer`
  * Add support for `crypto_wallets` on `V2.Core.Account.Configuration.Storer.Capability.FinancialAddress`, `V2.Core.Account.Configuration.Storer.Capability.OutboundPayment`, `V2.Core.Account.Configuration.Storer.Capability.OutboundTransfer`, `v2.core.AccountCreateParamsConfigurationStorerCapabilityFinancialAddress`, `v2.core.AccountCreateParamsConfigurationStorerCapabilityOutboundPayment`, `v2.core.AccountCreateParamsConfigurationStorerCapabilityOutboundTransfer`, `v2.core.AccountModifyParamsConfigurationStorerCapabilityFinancialAddress`, `v2.core.AccountModifyParamsConfigurationStorerCapabilityOutboundPayment`, and `v2.core.AccountModifyParamsConfigurationStorerCapabilityOutboundTransfer`
  * Add support for `usdc` on `V2.Core.Account.Configuration.Storer.Capability.HoldsCurrency`, `v2.core.AccountCreateParamsConfigurationStorerCapabilityHoldsCurrency`, and `v2.core.AccountModifyParamsConfigurationStorerCapabilityHoldsCurrency`
  * Add support for `crypto_storer` on `V2.Core.Account.Identity.Attestation.TermsOfService` and `v2.core.AccountCreateParamsIdentityAttestationTermsOfService`
  * Add support for `compliance_screening_description` on `V2.Core.Account.Identity.BusinessDetail`, `v2.core.AccountCreateParamsIdentityBusinessDetail`, and `v2.core.AccountModifyParamsIdentityBusinessDetail`
  * Add support for `external_amount` on `V2.MoneyManagement.ReceivedCredit` and `V2.MoneyManagement.ReceivedDebit`
  * Add support for error code `payment_intent_rate_limit_exceeded` on `Invoice.LastFinalizationError`, `PaymentIntent.LastPaymentError`, `QuotePreviewInvoice.LastFinalizationError`, `SetupAttempt.SetupError`, `SetupIntent.LastSetupError`, and `StripeError`

## 13.1.0a4 - 2025-10-23
* [#1649](https://github.com/stripe/stripe-python/pull/1649) Update generated code for private-preview
  * Add support for new resource `v2.billing.PricingPlanSubscriptionComponents`
  * Add support for `retrieve` method on resource `v2.billing.PricingPlanSubscriptionComponents`
  * Add support for `dimension_payload_keys` on `Billing.Meter` and `billing.MeterCreateParams`
  * Add support for `dimension_filters` and `dimension_group_by_keys` on `billing.BillingMeterListMeterEventSummaryParams`
  * Add support for `dimensions` on `Billing.MeterEventSummary`
  * Add support for `fulfillment_details` and `payment_method_data` on `delegated_checkout.RequestedSessionCreateParams` and `delegated_checkout.RequestedSessionModifyParams`
  * Add support for `line_item_details`, `metadata`, `payment_method`, and `shared_metadata` on `DelegatedCheckout.RequestedSession`, `delegated_checkout.RequestedSessionCreateParams`, and `delegated_checkout.RequestedSessionModifyParams`
  * Add support for `currency`, `customer`, and `risk_details` on `delegated_checkout.RequestedSessionCreateParams`
  * Add support for `seller_details` and `setup_future_usage` on `DelegatedCheckout.RequestedSession` and `delegated_checkout.RequestedSessionCreateParams`
  * Add support for `amount_subtotal`, `amount_total`, `created_at`, `expires_at`, `order_details`, `shared_payment_issued_token`, `status`, `total_details`, and `updated_at` on `DelegatedCheckout.RequestedSession`
  * Add support for `address`, `email`, `fulfillment_options`, `name`, `phone`, and `selected_fulfillment_option` on `DelegatedCheckout.RequestedSession.FulfillmentDetail`
  * Add support for new values `billie`, `crypto`, `kr_card`, `kriya`, `mb_way`, `mondu`, `ng_bank_transfer`, `ng_bank`, `ng_card`, `ng_market`, `ng_ussd`, `ng_wallet`, `payco`, `paypay`, `rechnung`, `samsung_pay`, `satispay`, `scalapay`, `sequra`, `sunbit`, `us_bank_account`, and `vipps` on enums `EventsV2CoreHealthAuthorizationRateDropFiringEvent.Impact.payment_method_type`, `EventsV2CoreHealthAuthorizationRateDropResolvedEvent.Impact.payment_method_type`, `EventsV2CoreHealthPaymentMethodErrorFiringEvent.Impact.payment_method_type`, and `EventsV2CoreHealthPaymentMethodErrorResolvedEvent.Impact.payment_method_type`

## 13.1.0a3 - 2025-10-17
* [#1643](https://github.com/stripe/stripe-python/pull/1643) Update generated code for private-preview
  * Add support for new resources `delegated_checkout.RequestedSession` and `identity.BlocklistEntry`
  * Add support for `confirm`, `create`, `expire`, `modify`, and `retrieve` methods on resource `delegated_checkout.RequestedSession`
  * Add support for `create`, `disable`, `list`, and `retrieve` methods on resource `identity.BlocklistEntry`
  * Add support for `blocked_by_entry` on `Identity.VerificationReport.Document`, `Identity.VerificationReport.Selfie`, and `identity.VerificationReportListParams`

## 13.1.0a2 - 2025-10-09
* [#1629](https://github.com/stripe/stripe-python/pull/1629) Update generated code for private-preview
  * Add support for new resource `PaymentMethodBalance`
  * Add support for `check_balance` method on resource `PaymentMethod`
  * Add support for `benefits` on `Card`, `Charge.PaymentMethodDetail.Card`, `ConfirmationToken.PaymentMethodPreview.Card`, and `PaymentMethod.Card`
  * Add support for `benefit` on `PaymentIntent.PaymentDetail`, `PaymentIntentConfirmParamsPaymentDetail`, `PaymentIntentCreateParamsPaymentDetail`, and `PaymentIntentModifyParamsPaymentDetail`
  * Add support for `setup_details` on `SetupIntentConfirmParams`, `SetupIntentCreateParams`, `SetupIntentModifyParams`, and `SetupIntent`
  * Add support for new value `card_creator` on enums `V2.Core.Account.applied_configurations` and `v2.core.AccountCloseParams.applied_configurations`
  * Add support for `card_creator` on `V2.Core.Account.Configuration`, `V2.Core.Account.Identity.Attestation.TermsOfService`, `v2.core.AccountCreateParamsConfiguration`, `v2.core.AccountCreateParamsIdentityAttestationTermsOfService`, `v2.core.AccountModifyParamsConfiguration`, and `v2.core.AccountModifyParamsIdentityAttestationTermsOfService`
  * Add support for new values `commercial.celtic.charge_card`, `commercial.celtic.spend_card`, `commercial.cross_river_bank.charge_card`, `commercial.cross_river_bank.spend_card`, `commercial.stripe.charge_card`, and `commercial.stripe.prepaid_card` on enum `V2.Core.Account.Requirement.Entry.Impact.RestrictsCapability.capability`
  * Add support for new value `card_creator` on enum `V2.Core.Account.Requirement.Entry.Impact.RestrictsCapability.configuration`
  * Add support for new value `configuration.card_creator` on enums `v2.core.AccountCreateParams.include`, `v2.core.AccountModifyParams.include`, and `v2.core.AccountRetrieveParams.include`
  * Add support for thin events `V2CoreAccountIncludingConfigurationCardCreatorCapabilityStatusUpdatedEvent` and `V2CoreAccountIncludingConfigurationCardCreatorUpdatedEvent` with related object `v2.core.Account`
  * Remove support for thin events `V1CustomerDiscountCreatedEvent`, `V1CustomerDiscountDeletedEvent`, and `V1CustomerDiscountUpdatedEvent` with related object `Discount`

## 13.1.0a1 - 2025-10-01
This release changes the pinned API version to `2025-09-30.preview`.

It is built on top of SDK version 13.0.0 and 13.1.0-beta.1 which contain breaking changes. Please review the changelog for these versions if upgrading from older SDK versions.

* [#1587](https://github.com/stripe/stripe-python/pull/1587) Update generated code for private-preview
  * Add support for new resource `v2.money_management.RecipientVerification`
  * Add support for `acknowledge`, `create`, `recipient_verifications`, and `retrieve` methods on resource `v2.money_management.RecipientVerification`
  * Add support for `modify` method on resources `v2.billing.PricingPlanSubscription` and `v2.billing.ServiceAction`
  * Add support for `crypto_wallets` on `V2.Account.Configuration.RecipientDatum.Feature`, `V2.Core.Account.Configuration.Recipient.Capability`, `v2.Account.CreateParamsConfigurationRecipientDatumFeature`, `v2.Account.ModifyParamsConfigurationRecipientDatumFeature`, `v2.core.Account.CreateParamsConfigurationRecipientCapability`, and `v2.core.Account.ModifyParamsConfigurationRecipientCapability`
  * Add support for new value `crypto` on enum `V2.Core.Account.Requirement.Entry.Impact.RestrictsCapability.capability`
  * Add support for new value `crypto_wallet` on enum `V2.Account.Configuration.RecipientDatum.DefaultOutboundDestination.type`
  * Add support for new value `crypto_wallets` on enum `V2.Account.Configuration.SupportableFeature.recipient_data`
  * Add support for new value `crypto_wallets` on enum `V2.Account.Requirement.Impact.required_for_features`
  * Add support for `lookup_key` on `V2.Billing.Cadence`, `v2.billing.Cadence.CreateParams`, and `v2.billing.Cadence.ModifyParams`
  * Add support for `settings_data` on `V2.Billing.Cadence`
  * Change type of `V2.Billing.Cadence.Payer.billing_profile` from `nullable(string)` to `string`
  * Add support for `v1_event_id` on `V2.Core.Event`
  * Add support for `recipient_verification` on `V2.MoneyManagement.OutboundPayment`, `V2.MoneyManagement.OutboundTransfer`, `v2.money_management.OutboundPayment.CreateParams`, and `v2.money_management.OutboundTransfer.CreateParams`
  * Add support for `crypto_wallet` on `V2.MoneyManagement.PayoutMethod` and `v2.money_management.OutboundSetupIntent.CreateParamsPayoutMethodDatum`
  * Add support for `custom_pricing_unit_details` on `V2.Billing.RateCardRate.CustomPricingUnitAmount`, `V2.Billing.ServiceAction.CreditGrant.Amount.CustomPricingUnit`, and `V2.Billing.ServiceAction.CreditGrantPerTenant.Amount.CustomPricingUnit`
  * Add support for `origin_type` on `V2.MoneyManagement.ReceivedDebit.BankTransfer`
  * Add support for new value `sepa_credit_transfer` on enum `v2.FinancialAddressCreditSimulation.CreditParams.network`
  * Add support for new value `credentials.sepa_bank_account.iban` on enums `v2.money_management.FinancialAddress.ListParams.include` and `v2.money_management.FinancialAddress.RetrieveParams.include`
  * Add support for `sepa_bank_account` on `v2.money_management.FinancialAddress.CreateParams`
  * Remove support for `price` on `v2.billing.RateCardRate.CreateParams`
  * Add support for `lookup_keys` on `v2.billing.Cadence.ListParams`
  * Change type of `v2.billing.Cadence.CancelParams.include`, `v2.billing.Cadence.CreateParams.include`, `v2.billing.Cadence.ListParams.include`, `v2.billing.Cadence.ModifyParams.include`, and `v2.billing.Cadence.RetrieveParams.include` from `literal('invoice_discount_rules')` to `enum('invoice_discount_rules'|'settings_data')`
  * Remove support for `customer` and `type` on `v2.billing.Cadence.CreateParamsPayer`
  * Change `v2.billing.Cadence.CreateParamsPayer.billing_profile` to be required
  * Add support for new value `crypto_wallets` on enum `EventsAccountConfigurationRecipientDataFeatureStatusUpdatedEvent.feature_name`
  * Add support for new value `crypto_wallets_v2` on enum `EventsV2CoreAccountIncludingConfigurationRecipientCapabilityStatusUpdatedEvent.updated_capability`
  * Remove support for `alert_id` on `EventsV2CoreHealthApiErrorResolvedEvent`, `EventsV2CoreHealthApiLatencyResolvedEvent`, `EventsV2CoreHealthAuthorizationRateDropResolvedEvent`, `EventsV2CoreHealthIssuingAuthorizationRequestTimeoutResolvedEvent`, `EventsV2CoreHealthPaymentMethodErrorResolvedEvent`, `EventsV2CoreHealthTrafficVolumeDropResolvedEvent`, and `EventsV2CoreHealthWebhookLatencyResolvedEvent`
  * Add support for thin event `V1AccountUpdatedEvent` with related object `v2.Account`
  * Add support for thin events `V1ApplicationFeeCreatedEvent`, `V1ApplicationFeeRefundedEvent`, `V1BillingPortalConfigurationCreatedEvent`, `V1BillingPortalConfigurationUpdatedEvent`, `V1CapabilityUpdatedEvent`, `V1ChargeCapturedEvent`, `V1ChargeDisputeClosedEvent`, `V1ChargeDisputeCreatedEvent`, `V1ChargeDisputeFundsReinstatedEvent`, `V1ChargeDisputeFundsWithdrawnEvent`, `V1ChargeDisputeUpdatedEvent`, `V1ChargeExpiredEvent`, `V1ChargeFailedEvent`, `V1ChargePendingEvent`, `V1ChargeRefundUpdatedEvent`, `V1ChargeRefundedEvent`, `V1ChargeSucceededEvent`, `V1ChargeUpdatedEvent`, `V1CheckoutSessionAsyncPaymentFailedEvent`, `V1CheckoutSessionAsyncPaymentSucceededEvent`, `V1CheckoutSessionCompletedEvent`, `V1CheckoutSessionExpiredEvent`, `V1ClimateOrderCanceledEvent`, `V1ClimateOrderCreatedEvent`, `V1ClimateOrderDelayedEvent`, `V1ClimateOrderDeliveredEvent`, `V1ClimateOrderProductSubstitutedEvent`, `V1ClimateProductCreatedEvent`, `V1ClimateProductPricingUpdatedEvent`, `V1CouponCreatedEvent`, `V1CouponDeletedEvent`, `V1CouponUpdatedEvent`, `V1CreditNoteCreatedEvent`, `V1CreditNoteUpdatedEvent`, `V1CreditNoteVoidedEvent`, `V1CustomerCreatedEvent`, `V1CustomerDeletedEvent`, `V1CustomerDiscountCreatedEvent`, `V1CustomerDiscountDeletedEvent`, `V1CustomerDiscountUpdatedEvent`, `V1CustomerSubscriptionCreatedEvent`, `V1CustomerSubscriptionDeletedEvent`, `V1CustomerSubscriptionPausedEvent`, `V1CustomerSubscriptionPendingUpdateAppliedEvent`, `V1CustomerSubscriptionPendingUpdateExpiredEvent`, `V1CustomerSubscriptionResumedEvent`, `V1CustomerSubscriptionTrialWillEndEvent`, `V1CustomerSubscriptionUpdatedEvent`, `V1CustomerTaxIdCreatedEvent`, `V1CustomerTaxIdDeletedEvent`, `V1CustomerTaxIdUpdatedEvent`, `V1CustomerUpdatedEvent`, `V1FileCreatedEvent`, `V1FinancialConnectionsAccountCreatedEvent`, `V1FinancialConnectionsAccountDeactivatedEvent`, `V1FinancialConnectionsAccountDisconnectedEvent`, `V1FinancialConnectionsAccountReactivatedEvent`, `V1FinancialConnectionsAccountRefreshedBalanceEvent`, `V1FinancialConnectionsAccountRefreshedOwnershipEvent`, `V1FinancialConnectionsAccountRefreshedTransactionsEvent`, `V1IdentityVerificationSessionCanceledEvent`, `V1IdentityVerificationSessionCreatedEvent`, `V1IdentityVerificationSessionProcessingEvent`, `V1IdentityVerificationSessionRedactedEvent`, `V1IdentityVerificationSessionRequiresInputEvent`, `V1IdentityVerificationSessionVerifiedEvent`, `V1InvoiceCreatedEvent`, `V1InvoiceDeletedEvent`, `V1InvoiceFinalizationFailedEvent`, `V1InvoiceFinalizedEvent`, `V1InvoiceMarkedUncollectibleEvent`, `V1InvoiceOverdueEvent`, `V1InvoiceOverpaidEvent`, `V1InvoicePaidEvent`, `V1InvoicePaymentActionRequiredEvent`, `V1InvoicePaymentFailedEvent`, `V1InvoicePaymentPaidEvent`, `V1InvoicePaymentSucceededEvent`, `V1InvoiceSentEvent`, `V1InvoiceUpcomingEvent`, `V1InvoiceUpdatedEvent`, `V1InvoiceVoidedEvent`, `V1InvoiceWillBeDueEvent`, `V1InvoiceitemCreatedEvent`, `V1InvoiceitemDeletedEvent`, `V1IssuingAuthorizationCreatedEvent`, `V1IssuingAuthorizationRequestEvent`, `V1IssuingAuthorizationUpdatedEvent`, `V1IssuingCardCreatedEvent`, `V1IssuingCardUpdatedEvent`, `V1IssuingCardholderCreatedEvent`, `V1IssuingCardholderUpdatedEvent`, `V1IssuingDisputeClosedEvent`, `V1IssuingDisputeCreatedEvent`, `V1IssuingDisputeFundsReinstatedEvent`, `V1IssuingDisputeFundsRescindedEvent`, `V1IssuingDisputeSubmittedEvent`, `V1IssuingDisputeUpdatedEvent`, `V1IssuingPersonalizationDesignActivatedEvent`, `V1IssuingPersonalizationDesignDeactivatedEvent`, `V1IssuingPersonalizationDesignRejectedEvent`, `V1IssuingPersonalizationDesignUpdatedEvent`, `V1IssuingTokenCreatedEvent`, `V1IssuingTokenUpdatedEvent`, `V1IssuingTransactionCreatedEvent`, `V1IssuingTransactionPurchaseDetailsReceiptUpdatedEvent`, `V1IssuingTransactionUpdatedEvent`, `V1MandateUpdatedEvent`, `V1PaymentIntentAmountCapturableUpdatedEvent`, `V1PaymentIntentCanceledEvent`, `V1PaymentIntentCreatedEvent`, `V1PaymentIntentPartiallyFundedEvent`, `V1PaymentIntentPaymentFailedEvent`, `V1PaymentIntentProcessingEvent`, `V1PaymentIntentRequiresActionEvent`, `V1PaymentIntentSucceededEvent`, `V1PaymentLinkCreatedEvent`, `V1PaymentLinkUpdatedEvent`, `V1PaymentMethodAttachedEvent`, `V1PaymentMethodAutomaticallyUpdatedEvent`, `V1PaymentMethodDetachedEvent`, `V1PaymentMethodUpdatedEvent`, `V1PayoutCanceledEvent`, `V1PayoutCreatedEvent`, `V1PayoutFailedEvent`, `V1PayoutPaidEvent`, `V1PayoutReconciliationCompletedEvent`, `V1PayoutUpdatedEvent`, `V1PersonCreatedEvent`, `V1PersonDeletedEvent`, `V1PersonUpdatedEvent`, `V1PlanCreatedEvent`, `V1PlanDeletedEvent`, `V1PlanUpdatedEvent`, `V1PriceCreatedEvent`, `V1PriceDeletedEvent`, `V1PriceUpdatedEvent`, `V1ProductCreatedEvent`, `V1ProductDeletedEvent`, `V1ProductUpdatedEvent`, `V1PromotionCodeCreatedEvent`, `V1PromotionCodeUpdatedEvent`, `V1QuoteAcceptedEvent`, `V1QuoteCanceledEvent`, `V1QuoteCreatedEvent`, `V1QuoteFinalizedEvent`, `V1RadarEarlyFraudWarningCreatedEvent`, `V1RadarEarlyFraudWarningUpdatedEvent`, `V1RefundCreatedEvent`, `V1RefundFailedEvent`, `V1RefundUpdatedEvent`, `V1ReviewClosedEvent`, `V1ReviewOpenedEvent`, `V1SetupIntentCanceledEvent`, `V1SetupIntentCreatedEvent`, `V1SetupIntentRequiresActionEvent`, `V1SetupIntentSetupFailedEvent`, `V1SetupIntentSucceededEvent`, `V1SigmaScheduledQueryRunCreatedEvent`, `V1SourceCanceledEvent`, `V1SourceChargeableEvent`, `V1SourceFailedEvent`, `V1SourceRefundAttributesRequiredEvent`, `V1SubscriptionScheduleAbortedEvent`, `V1SubscriptionScheduleCanceledEvent`, `V1SubscriptionScheduleCompletedEvent`, `V1SubscriptionScheduleCreatedEvent`, `V1SubscriptionScheduleExpiringEvent`, `V1SubscriptionScheduleReleasedEvent`, `V1SubscriptionScheduleUpdatedEvent`, `V1TaxRateCreatedEvent`, `V1TaxRateUpdatedEvent`, `V1TerminalReaderActionFailedEvent`, `V1TerminalReaderActionSucceededEvent`, `V1TerminalReaderActionUpdatedEvent`, `V1TestHelpersTestClockAdvancingEvent`, `V1TestHelpersTestClockCreatedEvent`, `V1TestHelpersTestClockDeletedEvent`, `V1TestHelpersTestClockInternalFailureEvent`, `V1TestHelpersTestClockReadyEvent`, `V1TopupCanceledEvent`, `V1TopupCreatedEvent`, `V1TopupFailedEvent`, `V1TopupReversedEvent`, `V1TopupSucceededEvent`, `V1TransferCreatedEvent`, `V1TransferReversedEvent`, `V1TransferUpdatedEvent`, `V2CoreHealthIssuingAuthorizationRequestErrorsFiringEvent`, and `V2CoreHealthIssuingAuthorizationRequestErrorsResolvedEvent`
  * Add support for thin event `V2CoreClaimableSandboxCreatedEvent` with related object `v2.core.ClaimableSandbox`
  * Add support for thin events `V2MoneyManagementRecipientVerificationCreatedEvent` and `V2MoneyManagementRecipientVerificationUpdatedEvent` with related object `v2.money_management.RecipientVerification`
  * Add support for error code `account_rate_limit_exceeded` on `RateLimitError`
  * Remove support for resources `v2.reporting.ReportRun`, `v2.reporting.Report`
  * Remove support for thin events `V2ReportingReportRunCreatedEvent`, `V2ReportingReportRunFailedEvent`, `V2ReportingReportRunSucceededEvent`, and `V2ReportingReportRunUpdatedEvent` with related object `v2.reporting.ReportRun`

## 12.6.0a2 - 2025-09-17
This release changes the pinned API version to `2025-08-04.preview`.

* [#1571](https://github.com/stripe/stripe-python/pull/1571) generate private-preview SDK w/ mid Sept changes
  * Add support for `retrieve` method on resource `v2.core.ClaimableSandbox`
  * Add support for `month_of_year` on `V2.Billing.Cadence.BillingCycle.Month` and `v2.billing.Cadence.CreateParamsBillingCycleMonth`
  * Add support for `claimed_at`, `expires_at`, `sandbox_details`, and `status` on `V2.Core.ClaimableSandbox`
  * Remove support for `api_keys` on `V2.Core.ClaimableSandbox`
  * Change type of `V2.Core.ClaimableSandbox.claim_url` from `string` to `nullable(string)`
  * Add support for new value `current_billing_period_end` on enums `V2.Billing.IntentAction.Deactivate.EffectiveAt.type` and `v2.billing.Intent.CreateParamsActionDeactivateEffectiveAt.type`
  * Add support for `will_activate_at` and `will_cancel_at` on `V2.Billing.PricingPlanSubscription.ServicingStatusTransition` and `V2.Billing.RateCardSubscription.ServicingStatusTransition`
  * Add support for `category` and `priority` on `V2.Billing.ServiceAction.CreditGrantPerTenant`, `V2.Billing.ServiceAction.CreditGrant`, `v2.billing.ServiceAction.CreateParamsCreditGrantPerTenant`, and `v2.billing.ServiceAction.CreateParamsCreditGrant`
  * Change `v2.billing.LicenseFee.ModifyParams.display_name` to be optional
  * Add support for `invoices` on `EventsV2BillingCadenceBilledEvent`
  * Add support for thin events `V2CoreClaimableSandboxClaimedEvent`, `V2CoreClaimableSandboxExpiredEvent`, `V2CoreClaimableSandboxExpiringEvent`, and `V2CoreClaimableSandboxSandboxDetailsOwnerAccountUpdatedEvent` with related object `V2.core.ClaimableSandbox`
  * Remove support for thin event `V2BillingCadenceErroredEvent` with related object `V2.billing.Cadence`

## 12.6.0a1 - 2025-08-27
* [#1556](https://github.com/stripe/stripe-python/pull/1556) Use the right API version 2025-08-27.preview
* [#1552](https://github.com/stripe/stripe-python/pull/1552) Update generated code for private-preview
  * Add support for `attach_cadence` method on resource `Subscription`
  * Add support for `currency` and `external_customer_id` on `Billing.AlertTriggered`
  * Add support for `custom_pricing_unit` on `Billing.AlertTriggered`, `Billing.CreditBalanceSummary.Balance.AvailableBalance`, `Billing.CreditBalanceSummary.Balance.LedgerBalance`, `Billing.CreditBalanceTransaction.Credit.Amount`, `Billing.CreditBalanceTransaction.Debit.Amount`, `Billing.CreditGrant.Amount`, and `billing.CreditGrant.CreateParamsAmount`
  * Add support for `customer` on `billing.Alert.ListParams`
  * Change type of `Billing.Alert.alert_type`, `billing.Alert.CreateParams.alert_type`, and `billing.Alert.ListParams.alert_type` from `literal('usage_threshold')` to `enum('credit_balance_threshold'|'usage_threshold')`
  * Add support for `credit_balance_threshold` on `Billing.Alert` and `billing.Alert.CreateParams`
  * Add support for `billable_items` on `Billing.CreditGrant.ApplicabilityConfig.Scope`, `billing.CreditBalanceSummary.RetrieveParamsFilterApplicabilityScope`, and `billing.CreditGrant.CreateParamsApplicabilityConfigScope`
  * Change type of `Billing.CreditBalanceSummary.Balance.AvailableBalance.type`, `Billing.CreditBalanceSummary.Balance.LedgerBalance.type`, `Billing.CreditBalanceTransaction.Credit.Amount.type`, `Billing.CreditBalanceTransaction.Debit.Amount.type`, `Billing.CreditGrant.Amount.type`, and `billing.CreditGrant.CreateParamsAmount.type` from `literal('monetary')` to `enum('custom_pricing_unit'|'monetary')`
  * Add support for `license_fee_subscription_details` and `rate_card_subscription_details` on `InvoiceItem.Parent` and `InvoiceLineItem.Parent`
  * Change type of `InvoiceItem.Parent.type` from `literal('subscription_details')` to `enum('license_fee_subscription_details'|'rate_card_subscription_details'|'subscription_details')`
  * Add support for `license_fee_details` and `rate_card_rate_details` on `InvoiceItem.Pricing` and `InvoiceLineItem.Pricing`
  * Change type of `InvoiceItem.Pricing.type` and `InvoiceLineItem.Pricing.type` from `literal('price_details')` to `enum('license_fee_details'|'price_details'|'rate_card_rate_details')`
  * Add support for `billing_cadence` on `Invoice.CreatePreviewParams`, `Subscription.CreateParams`, and `Subscription`
  * Add support for `billing_cadence_details` on `Invoice.Parent` and `QuotePreviewInvoice.Parent`
  * Add support for new value `billing_cadence_details` on enums `Invoice.Parent.type` and `QuotePreviewInvoice.Parent.type`
  * Add support for new values `license_fee_subscription_details` and `rate_card_subscription_details` on enum `InvoiceLineItem.Parent.type`
  * Add support for new resources `v2.billing.BillSettingVersion`, `v2.billing.BillSetting`, `v2.billing.Cadence`, `v2.billing.CollectionSettingVersion`, `v2.billing.CollectionSetting`, `v2.billing.CustomPricingUnit`, `v2.billing.IntentAction`, `v2.billing.Intent`, `v2.billing.LicenseFeeSubscription`, `v2.billing.LicenseFeeVersion`, `v2.billing.LicenseFee`, `v2.billing.LicensedItem`, `v2.billing.MeteredItem`, `v2.billing.PricingPlanComponent`, `v2.billing.PricingPlanSubscription`, `v2.billing.PricingPlanVersion`, `v2.billing.PricingPlan`, `v2.billing.Profile`, `v2.billing.RateCardRate`, `v2.billing.RateCardSubscription`, `v2.billing.RateCardVersion`, `v2.billing.RateCard`, `v2.billing.ServiceAction`, `v2.core.ClaimableSandbox`, `v2.reporting.ReportRun`, `v2.reporting.Report`, and `v2.tax.AutomaticRule`
  * Add support for `create`, `deactivate`, `find`, `modify`, and `retrieve` methods on resource `v2.tax.AutomaticRule`
  * Add support for `create` and `retrieve` methods on resources `v2.billing.ServiceAction` and `v2.reporting.ReportRun`
  * Add support for `retrieve` method on resources `v2.billing.LicenseFeeSubscription` and `v2.reporting.Report`
  * Add support for `create` method on resource `v2.core.ClaimableSandbox`
  * Add support for `cancel`, `create`, `list`, `modify`, and `retrieve` methods on resources `v2.billing.Cadence` and `v2.billing.RateCardSubscription`
  * Add support for `create`, `list`, `modify`, and `retrieve` methods on resources `v2.billing.BillSetting`, `v2.billing.CollectionSetting`, `v2.billing.CustomPricingUnit`, `v2.billing.LicenseFee`, `v2.billing.LicensedItem`, `v2.billing.MeteredItem`, `v2.billing.PricingPlan`, `v2.billing.Profile`, and `v2.billing.RateCard`
  * Add support for `list` and `retrieve` methods on resources `v2.billing.BillSettingVersion`, `v2.billing.CollectionSettingVersion`, `v2.billing.IntentAction`, `v2.billing.LicenseFeeVersion`, `v2.billing.PricingPlanSubscription`, `v2.billing.PricingPlanVersion`, and `v2.billing.RateCardVersion`
  * Add support for `create`, `delete`, `list`, and `retrieve` methods on resource `v2.billing.RateCardRate`
  * Add support for `create`, `delete`, `list`, `modify`, and `retrieve` methods on resource `v2.billing.PricingPlanComponent`
  * Add support for `cancel`, `commit`, `create`, `list`, `release_reservation`, `reserve`, and `retrieve` methods on resource `v2.billing.Intent`
  * Add support for `changes` on `V2.Event`
  * Add support for thin events `V2BillingCadenceBilledEvent`, `V2BillingCadenceCanceledEvent`, `V2BillingCadenceCreatedEvent`, and `V2BillingCadenceErroredEvent` with related object `v2.billing.Cadence`
  * Add support for thin events `V2BillingLicenseFeeCreatedEvent` and `V2BillingLicenseFeeUpdatedEvent` with related object `v2.billing.LicenseFee`
  * Add support for thin event `V2BillingLicenseFeeVersionCreatedEvent` with related object `v2.billing.LicenseFeeVersion`
  * Add support for thin events `V2BillingLicensedItemCreatedEvent` and `V2BillingLicensedItemUpdatedEvent` with related object `v2.billing.LicensedItem`
  * Add support for thin events `V2BillingMeteredItemCreatedEvent` and `V2BillingMeteredItemUpdatedEvent` with related object `v2.billing.MeteredItem`
  * Add support for thin events `V2BillingPricingPlanCreatedEvent` and `V2BillingPricingPlanUpdatedEvent` with related object `v2.billing.PricingPlan`
  * Add support for thin events `V2BillingPricingPlanComponentCreatedEvent` and `V2BillingPricingPlanComponentUpdatedEvent` with related object `v2.billing.PricingPlanComponent`
  * Add support for thin events `V2BillingPricingPlanSubscriptionCollectionAwaitingCustomerActionEvent`, `V2BillingPricingPlanSubscriptionCollectionCurrentEvent`, `V2BillingPricingPlanSubscriptionCollectionPastDueEvent`, `V2BillingPricingPlanSubscriptionCollectionPausedEvent`, `V2BillingPricingPlanSubscriptionCollectionUnpaidEvent`, `V2BillingPricingPlanSubscriptionServicingActivatedEvent`, `V2BillingPricingPlanSubscriptionServicingCanceledEvent`, and `V2BillingPricingPlanSubscriptionServicingPausedEvent` with related object `v2.billing.PricingPlanSubscription`
  * Add support for thin event `V2BillingPricingPlanVersionCreatedEvent` with related object `v2.billing.PricingPlanVersion`
  * Add support for thin events `V2BillingRateCardCreatedEvent` and `V2BillingRateCardUpdatedEvent` with related object `v2.billing.RateCard`
  * Add support for thin event `V2BillingRateCardRateCreatedEvent` with related object `v2.billing.RateCardRate`
  * Add support for thin events `V2BillingRateCardSubscriptionActivatedEvent`, `V2BillingRateCardSubscriptionCanceledEvent`, `V2BillingRateCardSubscriptionCollectionAwaitingCustomerActionEvent`, `V2BillingRateCardSubscriptionCollectionCurrentEvent`, `V2BillingRateCardSubscriptionCollectionPastDueEvent`, `V2BillingRateCardSubscriptionCollectionPausedEvent`, `V2BillingRateCardSubscriptionCollectionUnpaidEvent`, `V2BillingRateCardSubscriptionServicingActivatedEvent`, `V2BillingRateCardSubscriptionServicingCanceledEvent`, and `V2BillingRateCardSubscriptionServicingPausedEvent` with related object `v2.billing.RateCardSubscription`
  * Add support for thin event `V2BillingRateCardVersionCreatedEvent` with related object `v2.billing.RateCardVersion`
  * Add support for thin events `V2CoreHealthApiErrorFiringEvent`, `V2CoreHealthApiErrorResolvedEvent`, `V2CoreHealthApiLatencyFiringEvent`, `V2CoreHealthApiLatencyResolvedEvent`, `V2CoreHealthAuthorizationRateDropFiringEvent`, `V2CoreHealthAuthorizationRateDropResolvedEvent`, `V2CoreHealthEventGenerationFailureResolvedEvent`, `V2CoreHealthFraudRateIncreasedEvent`, `V2CoreHealthIssuingAuthorizationRequestTimeoutFiringEvent`, `V2CoreHealthIssuingAuthorizationRequestTimeoutResolvedEvent`, `V2CoreHealthPaymentMethodErrorFiringEvent`, `V2CoreHealthPaymentMethodErrorResolvedEvent`, `V2CoreHealthTrafficVolumeDropFiringEvent`, `V2CoreHealthTrafficVolumeDropResolvedEvent`, `V2CoreHealthWebhookLatencyFiringEvent`, and `V2CoreHealthWebhookLatencyResolvedEvent`
  * Add support for thin events `V2ReportingReportRunCreatedEvent`, `V2ReportingReportRunFailedEvent`, `V2ReportingReportRunSucceededEvent`, and `V2ReportingReportRunUpdatedEvent` with related object `v2.reporting.ReportRun`
  * Add support for error type `RateLimitError`
