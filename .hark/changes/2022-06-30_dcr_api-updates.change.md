---
title: API Updates
pr_link: https://github.com/stripe/stripe-python/pull/831
is_stripe_api_change: true
released_in_version: 3.5.0
---

* Add support for `deliver_card`, `fail_card`, `return_card`, and `ship_card` test helper methods on resource `Issuing.Card`
* Switch from using `instance_url` to computing method path in place for custom methods.
* Switch from using explicit class methods for test helpers instead of using meta-programming.
