---
title: Update generated code for beta
pr_url: https://github.com/stripe/stripe-python/pull/1370
is_stripe_api_change: true
released_in_version: 10.7.0b1
---

* Add support for `app_install` on parameter class `stripe.AccountSession.CreateParamsComponents`
* Add support for `app_viewport` on parameter class `stripe.AccountSession.CreateParamsComponents`
* Add support for `_cls_attach_payment` on resource `stripe.Invoice`
* Add support for `attach_payment` on resource `stripe.Invoice`
* Add support for `lines_invalid` on resource class `stripe.Quote.StatusDetails.Stale.LastReason`
* Add support for `last_price_migration_error` on resources `stripe.QuotePreviewSubscriptionSchedule`, `stripe.Subscription`, and `stripe.SubscriptionSchedule`
* Remove support for `partner_rejected_details` on resource class `stripe.Dispute.EvidenceDetails.EnhancedEligibility.VisaCompellingEvidence3`
* Add support for `customer.subscription.price_migration_failed` on enums `stripe.Event.type`, `stripe.WebhookEndpoint.CreateParams.enabled_events`, and `stripe.WebhookEndpoint.ModifyParams.enabled_events`
* Add support for `subscription_schedule.price_migration_failed` on enums `stripe.Event.type`, `stripe.WebhookEndpoint.CreateParams.enabled_events`, and `stripe.WebhookEndpoint.ModifyParams.enabled_events`
* Add support for `lines_invalid` on enum `stripe.Quote.StatusDetails.Stale.LastReason.type`
* Add support for `charge_exceeds_transaction_limit` on enum `stripe.QuotePreviewInvoice.LastFinalizationError.code`
