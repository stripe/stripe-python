---
title: Inner resource classes
pr_link: https://github.com/stripe/stripe-python/pull/1103
is_breaking: true
released_in_version: 7.1.0
---

* Behavior change: nested json objects will now deserialize into instances of specific classes that subclass `StripeObject`, instead of into generic `StripeObject` instances.
* ⚠️  Behavior change: `PromotionCode.restrictions.currency_options` will now deserialize into `dict` and not `StripeObject`.
