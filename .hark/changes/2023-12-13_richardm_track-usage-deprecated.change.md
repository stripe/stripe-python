---
title: Track usage of deprecated `save`
pr_link: https://github.com/stripe/stripe-python/pull/1146
released_in_version: 7.9.0
---

* Reports uses of the deprecated `.save` in `X-Stripe-Client-Telemetry`. (You can disable telemetry via `stripe.enable_telemetry = false`, see the [README](https://github.com/stripe/stripe-python/blob/master/README.md#telemetry).)
