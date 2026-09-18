---
title: Make path parameters positional-only in all service methods
pr_url: https://github.com/stripe/stripe-python/pull/1920
semver_level: major
---

Path parameters must now be passed positionally to service methods. Passing them by keyword is no longer supported.  Resource methods are unaffected by this change.
