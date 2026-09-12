---
title: Update generated code
pr_url: https://github.com/stripe/stripe-python/pull/1354
is_stripe_api_change: true
released_in_version: 10.2.0
---

* Add support for `_cls_add_lines`, `_cls_remove_lines`, `_cls_update_lines`, `add_lines`, `remove_lines`, `update_lines` on resource `stripe.Invoice`
* Add support for `posted_at` on parameter class `stripe.tax.Transaction.CreateFromCalculationParams` and resource `stripe.tax.Transaction`
* Add support for `payment_intent_fx_quote_invalid` on enums `stripe.Invoice.LastFinalizationError.code`, `stripe.PaymentIntent.LastPaymentError.code`, `stripe.SetupAttempt.SetupError.code`, and `stripe.SetupIntent.LastSetupError.code`
