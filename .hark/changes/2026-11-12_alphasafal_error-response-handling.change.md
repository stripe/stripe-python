---
title: "Raise proper Stripe errors for unusual error responses: unrecognized OAuth error codes now raise `OAuthError` instead of `AttributeError`; a non-object `error` value raises `APIError` instead of `AttributeError`; malformed and non-JSON error bodies keep their response headers and `request_id`; and a non-UTF-8 body no longer raises `UnicodeDecodeError` from debug logging"
semver_level: patch
---
