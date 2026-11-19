---
title: Support httpx2 for async requests, falling back to httpx when httpx2 isn't installed
pr_url: https://github.com/stripe/stripe-python/pull/1997
semver_level: minor
github_issues_resolved:
- https://github.com/stripe/stripe-python/issues/1886
released_in_version: 17.1.0
---

`HTTPXClient` and the default async client now use `httpx2` when it's installed and fall back to `httpx` otherwise. `httpx` support is deprecated and will be removed in the next major version; we recommend installing `httpx2` for async use.
