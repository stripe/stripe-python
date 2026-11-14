---
title: Raise `APIConnectionError` and retry when `AIOHTTPClient` fails while reading a response body
semver_level: patch
github_issues_resolved:
- https://github.com/stripe/stripe-python/issues/1993
---

Previously a dropped connection or timeout after the response headers arrived surfaced as a raw `aiohttp.ClientPayloadError` or `TimeoutError` and was not retried.
