---
title: Update generated code for beta
pr_link: https://github.com/stripe/stripe-python/pull/1387
is_stripe_api_change: true
released_in_version: 10.11.0b1
---

* Add support for `recipients` on parameter class `stripe.AccountSession.CreateParamsComponents`
* Add support for resource `stripe.billing.MeterErrorReport`
* Add support for `business_name` on resource class `stripe.checkout.Session.CollectedInformation`
* Add support for `tax_ids` on resource class `stripe.checkout.Session.CollectedInformation`
* Add support for `billing.meter_error_report.triggered` on enums `stripe.Event.type`, `stripe.WebhookEndpoint.CreateParams.enabled_events`, and `stripe.WebhookEndpoint.ModifyParams.enabled_events`
* Add support for `mb_way` on enums `stripe.PaymentLink.payment_method_types`, `stripe.PaymentLink.CreateParams.payment_method_types`, and `stripe.PaymentLink.ModifyParams.payment_method_types`
