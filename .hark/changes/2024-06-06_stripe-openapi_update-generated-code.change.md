---
title: Update generated code
pr_url: https://github.com/stripe/stripe-python/pull/1340
is_stripe_api_change: true
released_in_version: 9.10.0
---

* Add support for `gb_bank_transfer_payments`, `jp_bank_transfer_payments`, `mx_bank_transfer_payments`, `sepa_bank_transfer_payments`, `us_bank_transfer_payments` on resource class `stripe.Account.Capabilities` and parameter class `stripe.Account.CreateParamsCapabilities`
* Add support for `swish` on enums `stripe.Invoice.PaymentSettings.payment_method_types`, `stripe.Invoice.CreateParamsPaymentSettings.payment_method_types`, `stripe.Invoice.ModifyParamsPaymentSettings.payment_method_types`, `stripe.Subscription.PaymentSettings.payment_method_types`, `stripe.Subscription.CreateParamsPaymentSettings.payment_method_types`, and `stripe.Subscription.ModifyParamsPaymentSettings.payment_method_types`
