---
title: Update generated code for beta
pr_url: https://github.com/stripe/stripe-python/pull/1389
is_stripe_api_change: true
released_in_version: 10.12.0b1
---

* Add support for `template` on resource class `stripe.QuotePreviewInvoice.Rendering`
* Add support for resource `stripe.issuing.DisputeSettlementDetail`
* Add support for resource `stripe.issuing.Settlement`
* Add support for `settlement` on parameter class `stripe.issuing.Transaction.ListParams` and resource `stripe.issuing.Transaction`
* Remove support for `list` on resource `stripe.QuotePhase`
* Add support for `rechnung` on enum `stripe.checkout.Session.CreateParams.payment_method_types`
* Add support for `issuing_dispute_settlement_detail.created` on enums `stripe.Event.type`, `stripe.WebhookEndpoint.CreateParams.enabled_events`, and `stripe.WebhookEndpoint.ModifyParams.enabled_events`
* Add support for `issuing_dispute_settlement_detail.updated` on enums `stripe.Event.type`, `stripe.WebhookEndpoint.CreateParams.enabled_events`, and `stripe.WebhookEndpoint.ModifyParams.enabled_events`
* Add support for `issuing_settlement.created` on enums `stripe.Event.type`, `stripe.WebhookEndpoint.CreateParams.enabled_events`, and `stripe.WebhookEndpoint.ModifyParams.enabled_events`
* Add support for `issuing_settlement.updated` on enums `stripe.Event.type`, `stripe.WebhookEndpoint.CreateParams.enabled_events`, and `stripe.WebhookEndpoint.ModifyParams.enabled_events`
