---
title: "`Webhook.construct_event` and `StripeClient.parse_event_notification` now decode the payload once and use that value for both signature verification and parsing"
semver_level: patch
---

- Webhook payloads passed as a `memoryview` are now decoded and verified, instead of failing signature verification.
