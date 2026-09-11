---
title: Update generated code for private-preview
pr_link: https://github.com/stripe/stripe-python/pull/1711
is_stripe_api_change: true
released_in_version: 14.2.0a2
---

* Add support for `tracking_details` on `V2.MoneyManagement.OutboundPayment`
* Add support for `paper_check` on `V2.MoneyManagement.OutboundPayment.DeliveryOption` and `v2.money_management.OutboundPaymentCreateParamsDeliveryOption`
* Add support for event notification `V2CoreAccountIncludingFutureRequirementsUpdatedEvent` with related object `v2.core.Account`
* Add support for error code `account_rate_limit_exceeded` on `RateLimitError`
