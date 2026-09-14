---
title: Fix StripeError http_body
pr_url: https://github.com/stripe/stripe-python/pull/1435
released_in_version: 11.4.0
---

- Fixes an issue where `StripeError.http_body` may be None even when `json_body` is a valid dictionary.
