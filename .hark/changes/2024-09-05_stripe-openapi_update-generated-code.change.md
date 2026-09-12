---
title: Update generated code
pr_url: https://github.com/stripe/stripe-python/pull/1376
is_stripe_api_change: true
released_in_version: 10.10.0
---

* Add support for `subscription` on parameter class `stripe.billing.Alert.CreateParamsFilter`
* Change type of `customer_consent_collected` on  `stripe.terminal.Reader.ProcessSetupIntentParams` from `bool` to `NotRequired[bool]`
