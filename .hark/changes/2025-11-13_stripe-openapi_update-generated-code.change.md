---
title: Update generated code for private-preview
pr_link: https://github.com/stripe/stripe-python/pull/1672
is_stripe_api_change: true
released_in_version: 13.3.0a2
---

* Add support for new resource `issuing.Program`
* Add support for `create`, `list`, `modify`, and `retrieve` methods on resource `issuing.Program`
* Add support for `schedule` on `Discount`
* Add support for `applicable_fees` on `DelegatedCheckout.RequestedSession.TotalDetail`
* Add support for `schedule_details` on `Invoice.Parent`, `InvoiceItem.Parent`, `InvoiceLineItem.Parent`, and `QuotePreviewInvoice.Parent`
* Add support for new value `schedule_details` on enum `InvoiceItem.Parent.type`
* Add support for `billing_schedules` on `InvoiceCreatePreviewParamsScheduleDetail`, `QuotePreviewSubscriptionSchedule`, `SubscriptionScheduleCreateParams`, `SubscriptionScheduleModifyParams`, and `SubscriptionSchedule`
* Add support for new value `schedule_details` on enums `Invoice.Parent.type` and `QuotePreviewInvoice.Parent.type`
* Add support for new value `schedule_details` on enum `InvoiceLineItem.Parent.type`
* Add support for `latest_invoice` on `QuotePreviewSubscriptionSchedule` and `SubscriptionSchedule`
* Add support for `phase_effective_at` on `QuotePreviewSubscriptionSchedule.DefaultSetting`, `SubscriptionSchedule.DefaultSetting`, `SubscriptionScheduleCreateParamsDefaultSetting`, and `SubscriptionScheduleModifyParamsDefaultSetting`
