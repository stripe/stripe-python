---
title: Remove deprecated `StripeObject.request()` method
pr_url: https://github.com/stripe/stripe-python/pull/1914
semver_level: major
section: ⚠️ Removed
---

The deprecated `StripeObject.request()` method has been removed. Use `StripeClient.raw_request()` to make custom API requests.
