---
title: Update generated code
pr_url: https://github.com/stripe/stripe-python/pull/1323
is_stripe_api_change: true
released_in_version: 9.6.0
---

* Add support for `allow_redisplay` on resource class `stripe.ConfirmationToken.PaymentMethodPreview` and resource `stripe.PaymentMethod`
* Add support for `preview_mode` on parameter classes `stripe.Invoice.CreatePreviewParams`, `stripe.Invoice.UpcomingLinesParams`, and `stripe.Invoice.UpcomingParams`
* Add support for `_cls_update` on resources `stripe.treasury.OutboundPayment` and `stripe.treasury.OutboundTransfer`
* Add support for `tracking_details` on resources `stripe.treasury.OutboundPayment` and `stripe.treasury.OutboundTransfer`
* Add support for `update` on resources `stripe.treasury.OutboundPayment` and `stripe.treasury.OutboundTransfer`
* Add support for `treasury.outbound_payment.tracking_details_updated` on enums `stripe.Event.type`, `stripe.WebhookEndpoint.CreateParams.enabled_events`, and `stripe.WebhookEndpoint.ModifyParams.enabled_events`
* Add support for `treasury.outbound_transfer.tracking_details_updated` on enums `stripe.Event.type`, `stripe.WebhookEndpoint.CreateParams.enabled_events`, and `stripe.WebhookEndpoint.ModifyParams.enabled_events`
