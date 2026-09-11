---
title: "fix: Paginate backwards if `starting_after == None`"
pr_link: https://github.com/stripe/stripe-python/pull/1563
released_in_version: 12.5.1
---

* Addresses an [issue](https://github.com/stripe/stripe-python/issues/1562) where List iteration would be forwards when `starting_after` was set to `None` but backwards if it was not set at all. Now, it will paginate backwards in both cases.
