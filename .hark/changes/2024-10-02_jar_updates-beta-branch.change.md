---
title: Updates beta branch with changes in master & update generated code
pr_link: https://github.com/stripe/stripe-python/pull/1407
released_in_version: 11.2.0b1
---

* Add support for `reporting_chart` on parameter class `stripe.AccountSession.CreateParamsComponents`
* Add support for `total_pretax_credit_amounts` on resource `stripe.QuotePreviewInvoice`
* Add support for `allow_redisplay` on parameter class `stripe.terminal.Reader.CollectPaymentMethodParamsCollectConfig`
* Remove support for `from_schedule` on resource class `stripe.Quote.SubscriptionData`
* Move `raw_request` and related methods from `_raw_request` module to the `StripeClient` class
* Remove `_preview` module; use raw request methods in the `StripeClient` class instead
