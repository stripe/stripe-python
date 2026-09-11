---
title: Update generated code
pr_link: https://github.com/stripe/stripe-python/pull/1295
is_stripe_api_change: true
released_in_version: 8.11.0
---

* Add support for `fees`, `losses`, `requirement_collection` & `stripe_dashboard` on resource class `stripe.Account.Controller`
* Add support for `controller` on parameter class `stripe.Account.CreateParams`
* Add support for `create_feature`, `delete_feature`, `list_features`, `retrieve_feature` on resource `stripe.Product`
* Add support for resource `stripe.ProductFeature`
* Add support for `event_name` on parameter class `stripe.billing.MeterEventAdjustment.CreateParams` and resource `stripe.billing.MeterEventAdjustment`
* Add support for `cancel` and `type` on resource `stripe.billing.MeterEventAdjustment`
* Add support for resource `stripe.entitlements.ActiveEntitlement`
* Add support for resource `stripe.entitlements.Feature`
* Add support for `none` on enum `stripe.Account.type`
