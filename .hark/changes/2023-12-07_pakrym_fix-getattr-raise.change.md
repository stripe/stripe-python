---
title: Fix __getattr__ to raise AttributeError rather than returning None. This fixes a regression in 7.8.0 that caused `stripe.checkout`/`stripe.issuing` etc. to return `None`.
pr_url: https://github.com/stripe/stripe-python/pull/1159
released_in_version: 7.8.1
---
