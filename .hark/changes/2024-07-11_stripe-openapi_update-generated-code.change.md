---
title: Update generated code
pr_link: https://github.com/stripe/stripe-python/pull/1358
is_breaking: true
is_stripe_api_change: true
released_in_version: 10.3.0
---

* Add support for `payment_method_options` on resource `stripe.ConfirmationToken`
* Add support for `payment_element` on resource class `stripe.CustomerSession.Components` and parameter class `stripe.CustomerSession.CreateParamsComponents`
* Add support for `address_validation` on parameter class `stripe.issuing.Card.CreateParamsShipping` and resource class `stripe.issuing.Card.Shipping`
* Add support for `shipping` on parameter class `stripe.issuing.Card.ModifyParams`
* ⚠️ Remove support for `billing_policy_remote_function_response_invalid`, `billing_policy_remote_function_timeout`, `billing_policy_remote_function_unexpected_status_code`, and `billing_policy_remote_function_unreachable` on enums `stripe.Invoice.LastFinalizationError.code`, `stripe.PaymentIntent.LastPaymentError.code`, `stripe.SetupAttempt.SetupError.code`, and `stripe.SetupIntent.LastSetupError.code`
* ⚠️ Remove support for `payment_intent_fx_quote_invalid` on enums `stripe.Invoice.LastFinalizationError.code`, `stripe.PaymentIntent.LastPaymentError.code`, `stripe.SetupAttempt.SetupError.code`, and `stripe.SetupIntent.LastSetupError.code`. The property was mistakenly released last week.
* [#1357](https://github.com/stripe/stripe-python/pull/1357) don't auto-organize imports
