---
title: Update generated code
pr_url: https://github.com/stripe/stripe-python/pull/1186
is_stripe_api_change: true
released_in_version: 7.11.0
---

* Add support for `retrieve` on resource `tax.Registration`
* Change type from `Optional[PaymentDetails]` to `PaymentDetails` of `payment_details` on field `AccountSession.Components`
* Change type from `Optional[Payments]` to `Payments` of `payments` on field `AccountSession.Components`
* Change type from `Optional[Payouts]` to `Payouts` of `payouts` on field `AccountSession.Components`
* Change type from `Optional[Features]` to `Features` of `features` on fields `AccountSession.Components.PaymentDetails`, `AccountSession.Components.Payments`, and `AccountSession.Components.Payouts`
* Change type from `Optional[InvoiceSettings]` to `InvoiceSettings` of `invoice_settings` on field `SubscriptionSchedule.DefaultSettings`
