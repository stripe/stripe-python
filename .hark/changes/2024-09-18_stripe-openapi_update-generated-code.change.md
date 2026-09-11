---
title: Update generated code for beta
pr_link: https://github.com/stripe/stripe-python/pull/1395
is_stripe_api_change: true
released_in_version: 10.13.0b1
---

* Add support for `send_money` on parameter class `stripe.AccountSession.CreateParamsComponentsFinancialAccountFeatures`
* Add support for `transfer_balance` on parameter class `stripe.AccountSession.CreateParamsComponentsFinancialAccountFeatures`
* Add support for `automatically_finalizes_at` on resource `stripe.QuotePreviewInvoice`
* Remove support for resource `stripe.QuotePhase`
* Add support for `rechnung` on enums `stripe.PaymentLink.payment_method_types`, `stripe.PaymentLink.CreateParams.payment_method_types`, and `stripe.PaymentLink.ModifyParams.payment_method_types`
* Add support for `terminal_reader_invalid_location_for_activation` on enum `stripe.QuotePreviewInvoice.LastFinalizationError.code`
