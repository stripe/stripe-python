---
title: Update generated code for beta
pr_url: https://github.com/stripe/stripe-python/pull/1535
is_stripe_api_change: true
released_in_version: 12.5.0b1
---

* Add support for new resources `billing.MeterUsageRow`, `billing.MeterUsage`, and `terminal.OnboardingLink`
* Add support for `retrieve` method on resource `billing.MeterUsage`
* Add support for `create` method on resource `terminal.OnboardingLink`
* Add support for `monthly_payout_days` and `weekly_payout_days` on `BalanceSettings.ModifyParamsPayoutSchedule` and `BalanceSettings.Payout.Schedule`
* Remove support for `monthly_anchor` and `weekly_anchor` on `BalanceSettings.ModifyParamsPayoutSchedule` and `BalanceSettings.Payout.Schedule`
* Add support for `delay_days_override` on `BalanceSettings.ModifyParamsSettlementTiming`
* Remove support for `delay_days` on `BalanceSettings.ModifyParamsSettlementTiming`
* Add support for `update_discounts` on `checkout.Session.CreateParamsPermission`
* Add support for `discounts` and `subscription_data` on `checkout.Session.ModifyParams`
* Add support for `smart_disputes` on `Dispute`
* Add support for `upi` on `Invoice.CreateParamsPaymentSettingPaymentMethodOption`, `Invoice.ModifyParamsPaymentSettingPaymentMethodOption`, `Invoice.PaymentSetting.PaymentMethodOption`, `QuotePreviewInvoice.PaymentSetting.PaymentMethodOption`, `Subscription.CreateParamsPaymentSettingPaymentMethodOption`, `Subscription.ModifyParamsPaymentSettingPaymentMethodOption`, and `Subscription.PaymentSetting.PaymentMethodOption`
* Add support for new value `upi` on enums `Invoice.CreateParamsPaymentSetting.payment_method_types`, `Invoice.ModifyParamsPaymentSetting.payment_method_types`, `Invoice.PaymentSetting.payment_method_types`, `QuotePreviewInvoice.PaymentSetting.payment_method_types`, `Subscription.CreateParamsPaymentSetting.payment_method_types`, `Subscription.ModifyParamsPaymentSetting.payment_method_types`, and `Subscription.PaymentSetting.payment_method_types`
* Add support for `transaction_id` on `PaymentAttemptRecord.PaymentMethodDetail.Cashapp` and `PaymentRecord.PaymentMethodDetail.Cashapp`
* Add support for `amount_details` on `PaymentIntent.CaptureParams`, `PaymentIntent.ConfirmParams`, `PaymentIntent.CreateParams`, `PaymentIntent.IncrementAuthorizationParams`, and `PaymentIntent.ModifyParams`
* Add support for `payment_details` on `PaymentIntent.IncrementAuthorizationParams`
* Add support for `storer` on `V2.Core.Account.Identity.Attestation.TermsOfService`, `v2.core.Account.CreateParamsIdentityAttestationTermsOfService`, and `v2.core.Account.ModifyParamsIdentityAttestationTermsOfService`
* Add support for `collection_options` on `V2.Core.AccountLink.UseCase.AccountOnboarding`, `V2.Core.AccountLink.UseCase.AccountUpdate`, `v2.core.AccountLink.CreateParamsUseCaseAccountOnboarding`, and `v2.core.AccountLink.CreateParamsUseCaseAccountUpdate`
* Change type of `V2.Core.AccountLink.UseCase.AccountOnboarding.configurations`, `V2.Core.AccountLink.UseCase.AccountUpdate.configurations`, `v2.core.AccountLink.CreateParamsUseCaseAccountOnboarding.configurations`, and `v2.core.AccountLink.CreateParamsUseCaseAccountUpdate.configurations` from `literal('recipient')` to `enum('customer'|'merchant'|'recipient'|'storer')`
* Add support for `bank_account_type` on `V2.MoneyManagement.PayoutMethod.BankAccount`
* Add support for thin event `V2CoreAccountLinkReturnedEvent`
* Add support for thin event `V2MoneyManagementPayoutMethodUpdatedEvent` with related object `v2.money_management.PayoutMethod`
* Remove support for thin event `V2CoreAccountLinkCompletedEvent`
* Remove support for thin event `V2OffSessionPaymentRequiresCaptureEvent` with related object `v2.payments.OffSessionPayment`
