---
title: Update generated code for private-preview
pr_url: https://github.com/stripe/stripe-python/pull/1734
is_breaking: true
is_stripe_api_change: true
released_in_version: 14.4.0a4
---

* ⚠️ Add support for new value `spend_threshold` on enums `Billing.Alert.alert_type`, `billing.AlertCreateParams.alert_type`, and `billing.AlertListParams.alert_type`
* Add support for `spend_threshold` on `Billing.Alert` and `billing.AlertCreateParams`
* Add support for `invoice_item`, `proration_details`, `proration`, and `subscription` on `InvoiceLineItem.Parent.ScheduleDetail`
* Add support for `custom` on `PaymentMethodModifyParams`
* Add support for `payment_method_reference` and `usage` on `PaymentMethod.Custom`
* Add support for `outstanding_usage_through` and `unused_time_from` on `SubscriptionPauseParamsBillFor`
* ⚠️ Remove support for `outstanding_usage` and `unused_time` on `SubscriptionPauseParamsBillFor`
* ⚠️ Remove support for `payment_behavior` on `SubscriptionResumeParams`
