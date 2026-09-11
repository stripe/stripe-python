---
title: Update generated code for private-preview
pr_link: https://github.com/stripe/stripe-python/pull/1884
is_breaking: true
is_stripe_api_change: true
released_in_version: 15.7.0a1
---

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
