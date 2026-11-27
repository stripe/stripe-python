---
title: Fix `HTTPXClient` raising a network error when a proxy is configured
pr_url: https://github.com/stripe/stripe-python/pull/1997
semver_level: patch
released_in_version: 17.1.0
---

`HTTPXClient` passed `proxies` on each request, which httpx doesn't accept. Proxies are now configured on the client instead. Request bodies are also now sent as `content=`, which avoids httpx's deprecation warning for `data=`.
