---
title: Make path parameters positional-only in all service methods
pr_url: https://github.com/stripe/stripe-python/pull/1924
semver_level: major
---

 Path parameters must now be passed positionally on resource methods that support both classmethod and instance-method call styles (e.g. Coupon.delete). Passing them by keyword is no longer supported. This closes the remaining gap left by the service-method change, and prevents parameter names derived from the API specification from becoming part of the public interface here as well.