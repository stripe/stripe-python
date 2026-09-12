---
title: Update generated code
pr_url: https://github.com/stripe/stripe-python/pull/1332
is_stripe_api_change: true
released_in_version: 9.8.0
---

* Add support for `external_account_collection` on resource classes `stripe.AccountSession.Components.Balances.Features` and `stripe.AccountSession.Components.Payouts.Features` and parameter classes `stripe.AccountSession.CreateParamsComponentsBalancesFeatures` and `stripe.AccountSession.CreateParamsComponentsPayoutsFeatures`
* Add support for `payment_method_remove` on resource class `stripe.checkout.Session.SavedPaymentMethodOptions`
* Add support for `terminal_reader_invalid_location_for_payment` on enums `stripe.Invoice.LastFinalizationError.code`, `stripe.PaymentIntent.LastPaymentError.code`, `stripe.SetupAttempt.SetupError.code`, and `stripe.SetupIntent.LastSetupError.code`
