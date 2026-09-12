---
title: Update generated code for private-preview
pr_url: https://github.com/stripe/stripe-python/pull/1809
is_breaking: true
is_stripe_api_change: true
released_in_version: 15.2.0a6
---

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
