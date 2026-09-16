---
title: Make path parameters positional-only in all service methods
pr_url: https://github.com/stripe/stripe-python/pull/1910
semver_level: major
jira_tickets_closed:
- DEVSDK-3212
---

Path parameters must now be passed positionally. Passing them by keyword is no longer supported.
