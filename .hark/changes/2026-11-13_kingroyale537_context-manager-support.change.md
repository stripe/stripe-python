---
title: Add sync and async context manager support to StripeClient and HTTPClient
pr_url: https://github.com/stripe/stripe-python/pull/1990
semver_level: minor
---

Enables Python context managers (`with` and `async with`) on `StripeClient` and `HTTPClient`, allowing automatic cleanup and closing of underlying sessions upon block exit.
