---
title: Make path parameters positional-only in all service methods
pr_url: https://github.com/stripe/stripe-python/pull/1924
semver_level: major
released_in_version: 16.0.0
---

Path parameters must now be passed positionally on resource methods that support both classmethod and instance-method call styles (e.g. Coupon.delete). Passing them by keyword is no longer supported.
