---
title: Fix incorrect handling of additional request parameters
pr_url: https://github.com/stripe/stripe-python/pull/850
released_in_version: 4.0.1
---

* Fixes issue where using special parameter like `api_key`, `idempotency_key`, `stripe_version`, `stripe_account`, `headers` can cause a `Received unknown parameter error`.
