---
title: "Support httpx2 for async requests, falling back to httpx when httpx2 isn't installed"
semver_level: minor
---
`HTTPXClient` and the default async client now use `httpx2` when it's installed and fall back to `httpx` otherwise. Requests send their encoded body as `content=`, and proxies are configured on the client instead of per request.
