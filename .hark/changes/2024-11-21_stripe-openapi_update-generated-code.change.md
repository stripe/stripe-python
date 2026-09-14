---
title: Update generated code for beta
pr_url: https://github.com/stripe/stripe-python/pull/1425
is_stripe_api_change: true
released_in_version: 11.4.0b1
---

* Add support for `network_advice_code` on resource classes `stripe.Charge.Outcome`, `stripe.Invoice.LastFinalizationError`, `stripe.PaymentIntent.LastPaymentError`, `stripe.QuotePreviewInvoice.LastFinalizationError`, `stripe.SetupAttempt.SetupError`, and `stripe.SetupIntent.LastSetupError`
* Add support for `network_decline_code` on resource classes `stripe.Charge.Outcome`, `stripe.Invoice.LastFinalizationError`, `stripe.PaymentIntent.LastPaymentError`, `stripe.QuotePreviewInvoice.LastFinalizationError`, `stripe.SetupAttempt.SetupError`, and `stripe.SetupIntent.LastSetupError`
* Add support for `funding` on resource classes `stripe.Charge.PaymentMethodDetails.AmazonPay` and `stripe.Charge.PaymentMethodDetails.RevolutPay`
* Add support for `amount_requested` on resource class `stripe.Charge.PaymentMethodDetails.Card`
* Add support for `partial_authorization` on resource class `stripe.Charge.PaymentMethodDetails.Card`
* Add support for `adjustable_quantity` on resource `stripe.LineItem`
* Add support for `display` on resource `stripe.LineItem`
* Add support for `metadata` on resource `stripe.LineItem` and parameter class `stripe.checkout.Session.CreateParamsLineItem`
* Add support for `request_partial_authorization` on parameter classes `stripe.PaymentIntent.ConfirmParamsPaymentMethodOptionsCard`, `stripe.PaymentIntent.CreateParamsPaymentMethodOptionsCard`, and `stripe.PaymentIntent.ModifyParamsPaymentMethodOptionsCard` and resource class `stripe.PaymentIntent.PaymentMethodOptions.Card`
* Add support for `payment_method_options` on parameter class `stripe.PaymentIntent.IncrementAuthorizationParams`
* Add support for `line_items` on parameter classes `stripe.checkout.Session.CreateParamsPermissionsUpdate` and `stripe.checkout.Session.ModifyParams` and resource class `stripe.checkout.Session.Permissions.Update`
* Change type of `schedule_at_period_end` on  `stripe.billing_portal.Configuration.Features.SubscriptionUpdate` from `Optional[ScheduleAtPeriodEnd]` to `ScheduleAtPeriodEnd`
* Add support for `invoice.overpaid` on enums `stripe.Event.type`, `stripe.WebhookEndpoint.CreateParams.enabled_events`, and `stripe.WebhookEndpoint.ModifyParams.enabled_events`
