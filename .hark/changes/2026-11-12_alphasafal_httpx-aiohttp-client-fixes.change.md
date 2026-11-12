---
title: "Fix proxies with `HTTPXClient` (every request failed with a hidden `TypeError` because proxies were passed per request, which httpx does not accept); honor `HTTPXClient(timeout=None)`; close both connection pools in `HTTPXClient.close_async()`; and accept a single-scheme proxy dict in `AIOHTTPClient`"
semver_level: patch
---
