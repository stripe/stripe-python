---
title: Make the new nested params classes correctly importable
pr_link: https://github.com/stripe/stripe-python/pull/1626
released_in_version: 13.0.1
---

- For example, In SDK `v13.0.0`, `from stripe.params.checkout import SessionCreateParamsDiscount` would raise an error when it shouldn't have. This is fixed.
- Reported in https://github.com/stripe/stripe-python/issues/1625
