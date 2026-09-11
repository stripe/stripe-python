---
title: Update generated code
pr_link: https://github.com/stripe/stripe-python/pull/1364
is_stripe_api_change: true
released_in_version: 10.5.0
---

* Add support for `transaction_id` on resource class `stripe.Charge.PaymentMethodDetails.Affirm`
* Add support for `buyer_id` on resource class `stripe.Charge.PaymentMethodDetails.Blik`
* Add support for `authorization_code` on resource class `stripe.Charge.PaymentMethodDetails.Card`
* Add support for `brand_product` on resource classes `stripe.Charge.PaymentMethodDetails.CardPresent`, `stripe.ConfirmationToken.PaymentMethodPreview.Card.GeneratedFrom.PaymentMethodDetails.CardPresent`, `stripe.ConfirmationToken.PaymentMethodPreview.CardPresent`, `stripe.PaymentMethod.Card.GeneratedFrom.PaymentMethodDetails.CardPresent`, and `stripe.PaymentMethod.CardPresent`
* Add support for `network_transaction_id` on resource classes `stripe.Charge.PaymentMethodDetails.CardPresent`, `stripe.Charge.PaymentMethodDetails.InteracPresent`, `stripe.ConfirmationToken.PaymentMethodPreview.Card.GeneratedFrom.PaymentMethodDetails.CardPresent`, and `stripe.PaymentMethod.Card.GeneratedFrom.PaymentMethodDetails.CardPresent`
* Add support for `case_type` on resource class `stripe.Dispute.PaymentMethodDetails.Card`
* Add support for `twint` on parameter classes `stripe.PaymentMethodConfiguration.CreateParams` and `stripe.PaymentMethodConfiguration.ModifyParams` and resource `stripe.PaymentMethodConfiguration`
* Add support for `modify` on resource `stripe.checkout.Session`
* Add support for `invoice.overdue` on enums `stripe.Event.type`, `stripe.WebhookEndpoint.CreateParams.enabled_events`, and `stripe.WebhookEndpoint.ModifyParams.enabled_events`
* Add support for `invoice.will_be_due` on enums `stripe.Event.type`, `stripe.WebhookEndpoint.CreateParams.enabled_events`, and `stripe.WebhookEndpoint.ModifyParams.enabled_events`
