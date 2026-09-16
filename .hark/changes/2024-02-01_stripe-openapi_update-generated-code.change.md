---
title: Update generated code
pr_url: https://github.com/stripe/stripe-python/pull/1213
is_stripe_api_change: true
released_in_version: 8.1.0
---

* Add support for `swish` payment method throughout the API
* Add support for `relationship` on parameter classes `Account.CreateParamsIndividual` and `Token.CreateParamsAccountIndividual`
* Add support for `jurisdiction_level` on resource `TaxRate`
* Change type from `str` to `Literal["offline", "online"]` of `status` on field `terminal.Reader`
