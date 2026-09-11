---
title: Update generated code for beta
pr_link: https://github.com/stripe/stripe-python/pull/1858
is_breaking: true
is_stripe_api_change: true
released_in_version: 15.7.0b1
---

* Add support for new resources `v2.core.ApprovalRequest`, `v2.signals.AccountActivity`, `v2.signals.AccountEvaluation`, and `v2.signals.AccountSignal`
* Add support for `list` and `retrieve` methods on resource `v2.signals.AccountSignal`
* Add support for `create` and `retrieve` methods on resource `v2.signals.AccountEvaluation`
* Add support for `create`, `delete`, and `retrieve` methods on resource `v2.signals.AccountActivity`
* Add support for `cancel`, `list`, `modify`, and `retrieve` methods on resource `v2.core.ApprovalRequest`
* Add support for `disable` method on resource `v2.money_management.PayoutMethod`
* Add support for `disable_stripe_user_authentication` on `AccountSessionCreateParamsComponentPaymentMethodSettingFeature`
* ⚠️ Remove support for `payment_method_types` on `PaymentIntentConfirmParams`, `PaymentIntentCreateParams`, `PaymentIntentModifyParams`, `SetupIntentCreateParams`, and `SetupIntentModifyParams`
* ⚠️ Change type of `ProductCatalog.TrialOffer.EndBehavior.Transition.price` and `ProductCatalog.TrialOffer.price` from `$Price` to `deletable($Price)`
* Add support for `billie` on `QuotePreviewInvoice.PaymentSetting.PaymentMethodOption`
* Add support for new value `billie` on enum `QuotePreviewInvoice.PaymentSetting.payment_method_types`
* Add support for `payout_methods` on `V2.Core.Account.Default` and `v2.core.AccountModifyParamsDefault`
* Add support for `restricted` on `V2.Core.Vault.GbBankAccount` and `V2.Core.Vault.UsBankAccount`
* Add support for `enabled_delivery_schemes` on `V2.MoneyManagement.PayoutMethod.BankAccount`
* ⚠️ Remove support for `enabled_delivery_options` on `V2.MoneyManagement.PayoutMethod.BankAccount`
* ⚠️ Add support for new value `disabled` on enum `V2.MoneyManagement.PayoutMethod.UsageStatus.payments`
* ⚠️ Add support for new value `disabled` on enum `V2.MoneyManagement.PayoutMethod.UsageStatus.transfers`
* Add support for new value `disabled` on enum `v2.money_management.PayoutMethodListParamsUsageStatus.payments`
* Add support for new value `disabled` on enum `v2.money_management.PayoutMethodListParamsUsageStatus.transfers`
* Add support for event notifications `V2CoreApprovalRequestApprovedEvent`, `V2CoreApprovalRequestCanceledEvent`, `V2CoreApprovalRequestCreatedEvent`, `V2CoreApprovalRequestExpiredEvent`, `V2CoreApprovalRequestFailedEvent`, `V2CoreApprovalRequestRejectedEvent`, and `V2CoreApprovalRequestSucceededEvent` with related object `v2.core.ApprovalRequest`
* Add support for event notification `V2SignalsAccountEvaluationCompleteEvent` with related object `v2.signals.AccountEvaluation`
* Add support for error codes `authentication_failure`, `capability_not_active`, `expired_payment_method`, `incorrect_postal_code`, `invalid_canceled_subscription_fields`, and `payment_method_restricted` on `QuotePreviewInvoice.LastFinalizationError`
* Add support for error code `default_payout_method_cannot_be_disabled` on `CannotProceedError`
