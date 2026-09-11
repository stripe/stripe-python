---
title: Update generated code for beta
pr_link: https://github.com/stripe/stripe-python/pull/1270
is_stripe_api_change: true
released_in_version: 8.8.0b1
---

* Add support for new resources `Billing.MeterEventAdjustment`, `Billing.MeterEvent`, and `Billing.Meter`
* Add support for `create`, `deactivate`, `list`, `modify`, `reactivate`, and `retrieve` methods on resource `Meter`
* Add support for `create` method on resources `MeterEventAdjustment` and `MeterEvent`
* Add support for `create` test helper method on resource `ConfirmationToken`
* Add support for `add_lines`, `remove_lines`, and `update_lines` methods on resource `Invoice`
