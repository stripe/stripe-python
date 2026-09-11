---
title: Update generated code
pr_link: https://github.com/stripe/stripe-python/pull/1369
is_breaking: true
is_stripe_api_change: true
released_in_version: 10.6.0
---

* Add support for resource `stripe.billing.Alert`
* ⚠️ Remove support for `authorization_code` on resource class `stripe.Charge.PaymentMethodDetails.Card`. This was accidentally released last week.
* Add support for `billing.alert.triggered` on enums `stripe.Event.type`, `stripe.WebhookEndpoint.CreateParams.enabled_events`, and `stripe.WebhookEndpoint.ModifyParams.enabled_events`
* Add support for `charge_exceeds_transaction_limit` on enums `stripe.Invoice.LastFinalizationError.code`, `stripe.PaymentIntent.LastPaymentError.code`, `stripe.SetupAttempt.SetupError.code`, and `stripe.SetupIntent.LastSetupError.code`
