---
title: Handle non-ASCII signatures gracefully in WebhookSignature.verify_header
semver_level: patch
github_issues_resolved:
- https://github.com/stripe/stripe-python/issues/1991
---

Fix `WebhookSignature.verify_header` raising an unhandled `TypeError` when a signature contains non-ASCII characters, properly raising `SignatureVerificationError` instead.
