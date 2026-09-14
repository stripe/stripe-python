---
title: Update generated code for beta
pr_url: https://github.com/stripe/stripe-python/pull/1597
is_stripe_api_change: true
released_in_version: 13.1.0b1
---

* Add support for `attach_cadence` method on resource `Subscription`
* Add support for `billing_cadence` on `Invoice.CreatePreviewParams`, `Subscription.CreateParams`, `Subscription.ModifyParams`, and `Subscription`
* Add support for `billing_cadence_details` on `Invoice.Parent` and `QuotePreviewInvoice.Parent`
* Add support for new value `billing_cadence_details` on enums `Invoice.Parent.type` and `QuotePreviewInvoice.Parent.type`
