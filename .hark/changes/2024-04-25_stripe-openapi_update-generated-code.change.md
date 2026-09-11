---
title: Update generated code for beta
pr_link: https://github.com/stripe/stripe-python/pull/1308
is_stripe_api_change: true
released_in_version: 9.5.0b1
---

* Add support for `payment_method_settings` on parameter class `stripe.AccountSession.CreateParamsComponents`
* Add support for `cancel_subscription_schedule` on parameter classes `stripe.Quote.CreateParamsLine` and `stripe.Quote.ModifyParamsLine` and resource `stripe.QuoteLine`
* Add support for `amazon_pay` on enum `stripe.QuotePreviewInvoice.PaymentSettings.payment_method_types`
* Add support for `revolut_pay` on enum `stripe.QuotePreviewInvoice.PaymentSettings.payment_method_types`
