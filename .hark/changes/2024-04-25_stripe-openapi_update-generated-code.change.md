---
title: Update generated code
pr_url: https://github.com/stripe/stripe-python/pull/1316
is_stripe_api_change: true
released_in_version: 9.4.0
---

* Add support for `amazon_pay` on resource classes `stripe.Mandate.PaymentMethodDetails` and `stripe.SetupAttempt.PaymentMethodDetails`
* Add support for `revolut_pay` on resource classes `stripe.Mandate.PaymentMethodDetails` and `stripe.SetupAttempt.PaymentMethodDetails`
* Add support for `setup_future_usage` on resource classes `stripe.PaymentIntent.PaymentMethodOptions.AmazonPay`, `stripe.PaymentIntent.PaymentMethodOptions.RevolutPay`, `stripe.checkout.Session.PaymentMethodOptions.AmazonPay`, and `stripe.checkout.Session.PaymentMethodOptions.RevolutPay`
* Add support for `mobilepay` on parameter classes `stripe.PaymentMethodConfiguration.CreateParams` and `stripe.PaymentMethodConfiguration.ModifyParams` and resource `stripe.PaymentMethodConfiguration`
* Add support for `ending_before` on parameter class `stripe.PaymentMethodConfiguration.ListParams`
* Add support for `limit` on parameter class `stripe.PaymentMethodConfiguration.ListParams`
* Add support for `starting_after` on parameter class `stripe.PaymentMethodConfiguration.ListParams`
* Change type of `feature` on  `stripe.entitlements.ActiveEntitlement` from `str` to `ExpandableField[Feature]`
* Add support for `amazon_pay` on enums `stripe.Invoice.PaymentSettings.payment_method_types`, `stripe.Invoice.CreateParamsPaymentSettings.payment_method_types`, `stripe.Invoice.ModifyParamsPaymentSettings.payment_method_types`, `stripe.Subscription.PaymentSettings.payment_method_types`, `stripe.Subscription.CreateParamsPaymentSettings.payment_method_types`, and `stripe.Subscription.ModifyParamsPaymentSettings.payment_method_types`
* Add support for `revolut_pay` on enums `stripe.Invoice.PaymentSettings.payment_method_types`, `stripe.Invoice.CreateParamsPaymentSettings.payment_method_types`, `stripe.Invoice.ModifyParamsPaymentSettings.payment_method_types`, `stripe.Subscription.PaymentSettings.payment_method_types`, `stripe.Subscription.CreateParamsPaymentSettings.payment_method_types`, and `stripe.Subscription.ModifyParamsPaymentSettings.payment_method_types`
* Remove support for inadvertently released identity verification features `email` and `phone` on parameter classes `stripe.identity.VerificationSession.CreateParamsOptions` and `stripe.identity.VerificationSession.ModifyParamsOptions`
