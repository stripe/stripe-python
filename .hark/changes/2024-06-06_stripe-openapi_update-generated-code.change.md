---
title: Update generated code for beta
pr_url: https://github.com/stripe/stripe-python/pull/1339
is_stripe_api_change: true
released_in_version: 9.11.0b1
---

* Add support for `twint` on parameter classes `stripe.PaymentIntent.ConfirmParamsPaymentMethodOptions`, `stripe.PaymentIntent.CreateParamsPaymentMethodOptions`, and `stripe.PaymentIntent.ModifyParamsPaymentMethodOptions` and resource class `stripe.PaymentIntent.PaymentMethodOptions`
* Add support for `swish` on enum `stripe.QuotePreviewInvoice.PaymentSettings.payment_method_types`
