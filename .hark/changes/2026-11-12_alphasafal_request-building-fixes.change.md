---
title: "Fix several request-building edge cases: `raw_request` accepts upper-case HTTP methods; `Decimal` and float values are sent in plain notation instead of scientific (`0.0000001`, not `1E-7`); a V2 request body containing a `StripeObject` is serialized, and an unserializable value raises a clear `TypeError` instead of `Circular reference detected`; `stripe.OAuth.authorize_url` honors a `stripe.connect_api_base` set after import; and `client.oauth.authorize_url`, `client.oauth.deauthorize` and GET requests that merge `expand` no longer modify the caller's params dict"
semver_level: patch
---
