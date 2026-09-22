---
title: Fix account scoping for event notification handler callback clients
pr_url: https://github.com/stripe/stripe-python/pull/1911
semver_level: patch
---

- Fix callback clients to use the event's Stripe context and preserve the original client's non-account configuration.
- Fix API errors when using an event notification handler with a client configured with a Stripe account.
