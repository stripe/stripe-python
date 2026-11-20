---
title: "Fix response-header handling in `UrllibClient` and `PycurlClient`: `Stripe-Notice` warnings and request telemetry now work with their lower-cased header names; `PycurlClient` no longer loses every response header when an interim response (`100 Continue`, a proxy's `CONNECT` reply) precedes the final one; and a streaming request that receives an error status raises the API error instead of `NotImplementedError` on `UrllibClient` and the sync `HTTPXClient`"
semver_level: patch
---
