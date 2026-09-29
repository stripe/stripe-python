---
title: Make path parameters positional-only in all service methods
pr_url: https://github.com/stripe/stripe-python/pull/1920
semver_level: major
---

Path parameters must now be passed positionally to service methods. Passing them by keyword is no longer supported. This prevents parameter names derived from the API specification from becoming part of the public interface.

 Resource methods are unaffected by this change.
