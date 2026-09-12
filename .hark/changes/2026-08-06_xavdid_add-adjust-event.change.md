---
title: add/adjust event parsing helpers
pr_url: https://github.com/stripe/stripe-python/pull/1855
released_in_version: 15.5.0
---

- Added methods that return their respective `Event`/`EventNotification` class instances without verifying authenticity. Use them when you've previously verified an event (e.g. you verified, put the event in a queue, and are now processing). Supports events from [AWS EventBridge](https://docs.stripe.com/event-destinations/eventbridge) and [Azure Event Grid](https://docs.stripe.com/event-destinations/eventgrid) natively.
  - `Webhook.construct_event_without_verification(payload)`
  - `StripeClient.construct_event_without_verification(payload)`
  - `StripeClient.parse_event_notification_without_verification(payload)`
- Added `WebhookSignature.generate_signature_header(payload, secret, timestamp=None)`, which computes a full `Stripe-Signature` header for the given payload. Useful for unit tests!
