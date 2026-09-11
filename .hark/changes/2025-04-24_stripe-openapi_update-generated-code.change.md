---
title: Update generated code for beta
pr_link: https://github.com/stripe/stripe-python/pull/1501
is_stripe_api_change: true
released_in_version: 12.2.0b1
---

* Add support for `billing_mode` on `Invoice.CreatePreviewParamsScheduleDetail`, `Invoice.CreatePreviewParamsSubscriptionDetail`, `InvoiceService.CreatePreviewParamsScheduleDetail`, `InvoiceService.CreatePreviewParamsSubscriptionDetail`, `Quote.SubscriptionDatum`, `QuotePreviewSubscriptionSchedule`, `SubscriptionSchedule`, `Subscription`, `checkout.Session.CreateParamsSubscriptionDatum`, and `checkout.SessionService.CreateParamsSubscriptionDatum`
* Add support for new value `balance_settings.updated` on enum `Event.type`
* Add support for new value `balance_settings.updated` on enums `WebhookEndpoint.ModifyParams.enabled_events` and `WebhookEndpointService.UpdateParams.enabled_events`
