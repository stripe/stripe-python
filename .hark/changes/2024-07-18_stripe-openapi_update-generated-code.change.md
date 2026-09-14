---
title: Update generated code
pr_url: https://github.com/stripe/stripe-python/pull/1362
is_stripe_api_change: true
released_in_version: 10.4.0
---

* Add support for `customer` on resource class `stripe.ConfirmationToken.PaymentMethodPreview`
* Add support for `issuing_dispute.funds_rescinded` on enums `stripe.Event.type`, `stripe.WebhookEndpoint.CreateParams.enabled_events`, and `stripe.WebhookEndpoint.ModifyParams.enabled_events`
* Add support for `multibanco` on enums `stripe.Invoice.PaymentSettings.payment_method_types`, `stripe.Invoice.CreateParamsPaymentSettings.payment_method_types`, `stripe.Invoice.ModifyParamsPaymentSettings.payment_method_types`, `stripe.Subscription.PaymentSettings.payment_method_types`, `stripe.Subscription.CreateParamsPaymentSettings.payment_method_types`, and `stripe.Subscription.ModifyParamsPaymentSettings.payment_method_types`
* Add support for `stripe_s700` on enums `stripe.terminal.Reader.device_type` and `stripe.terminal.Reader.ListParams.device_type`
