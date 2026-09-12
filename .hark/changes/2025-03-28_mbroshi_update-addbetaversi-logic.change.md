---
title: Update add_beta_version logic
pr_url: https://github.com/stripe/stripe-python/pull/1476
is_breaking: true
section: Changes
released_in_version: 12.1.0b1
---

* ⚠️ stripe.add_beta_version` will use the highest version number used for a beta feature instead of raising an `Exception` on a conflict as it had done previously.
