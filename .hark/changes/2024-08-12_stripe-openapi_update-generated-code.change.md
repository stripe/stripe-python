---
title: Update generated code for beta
pr_link: https://github.com/stripe/stripe-python/pull/1372
is_breaking: true
is_stripe_api_change: true
released_in_version: 10.8.0b1
---

* Add support for `capital_financing` on resource class `stripe.AccountSession.Components`
* Add support for `payto` on parameter class `stripe.checkout.Session.CreateParamsPaymentMethodOptions` and resource class `stripe.checkout.Session.PaymentMethodOptions`
* ⚠️  Remove support for `risk_correlation_id` on parameter classes `stripe.PaymentIntent.ConfirmParamsPaymentMethodOptionsRechnung`, `stripe.PaymentIntent.CreateParamsPaymentMethodOptionsRechnung`, and `stripe.PaymentIntent.ModifyParamsPaymentMethodOptionsRechnung` and resource class `stripe.PaymentIntent.PaymentMethodOptions.Rechnung`
* Add support for `custom` on enums `stripe.checkout.Session.ui_mode` and `stripe.checkout.Session.CreateParams.ui_mode`
* Add support for `payto` on enums `stripe.checkout.Session.CreateParams.payment_method_types`, `stripe.PaymentLink.payment_method_types`, `stripe.PaymentLink.CreateParams.payment_method_types`, and `stripe.PaymentLink.ModifyParams.payment_method_types`
* Add support for `invalid_mandate_reference_prefix_format` on enum `stripe.QuotePreviewInvoice.LastFinalizationError.code`
