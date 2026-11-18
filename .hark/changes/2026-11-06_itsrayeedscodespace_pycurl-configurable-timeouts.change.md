---
title: Add configurable `timeout` and `connect_timeout` to `PycurlClient`
semver_level: minor
github_issues_resolved:
- https://github.com/stripe/stripe-python/issues/1962
---

`PycurlClient` now accepts keyword-only `timeout` (total request time, curl's `TIMEOUT`) and `connect_timeout` (curl's `CONNECTTIMEOUT`) arguments, in whole seconds. They default to the previous hardcoded values of 80 and 30 seconds.
