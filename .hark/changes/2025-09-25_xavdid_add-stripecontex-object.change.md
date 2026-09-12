---
title: Add `StripeContext` object
pr_url: https://github.com/stripe/stripe-python/pull/1589
is_breaking: true
released_in_version: 13.0.0
---

- Add the `StripeContext` class. Previously, one could only pass a string for `stripe_context`. You can now use the new class as well.
- ⚠️ Change `EventNotification` (formerly known as `ThinEvent`)'s `context` property from `string` to `StripeContext`
