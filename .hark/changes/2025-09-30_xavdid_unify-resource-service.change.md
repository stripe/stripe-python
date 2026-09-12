---
title: Unify resource and service method parameters into one class
pr_url: https://github.com/stripe/stripe-python/pull/1596
is_breaking: true
released_in_version: 13.0.0
---

* ⚠️ Resource and service request parameter types have been moved to the top-level and are shared, prepended with their related resource/service
  * For example, `_stripe._account.Account.CreateParams` and `_stripe._account_service.CreateParams` have moved to `_stripe.params._account_create_params.AccountCreateParams`
  * This change only affects users who explicitly refer to params types. No migration is necessary for users otherwise
