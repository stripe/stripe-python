---
title: Encode bools with lower case
pr_link: https://github.com/stripe/stripe-python/pull/1499
released_in_version: 12.0.1
---

- Serializes boolean query parameter values to `true`/`false` (lower case) before sending to the Stripe API for compatibility with Stripe V2 endpoints
