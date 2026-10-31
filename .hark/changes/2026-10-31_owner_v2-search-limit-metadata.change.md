---
title: Keep custom search limits in the request body and use dedicated v2 search helpers
semver_level: patch
pr_url: https://github.com/stripe/stripe-python/pull/1960
---

Handwritten v2 search services should call `_request_v2_search` or `_request_v2_search_async` to send `limit` in the initial URL query. Ordinary requests no longer infer search behavior from the path.
