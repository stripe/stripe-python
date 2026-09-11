---
title: Move `V2.Event` API resources to `V2.Core.Events`
pr_link: https://github.com/stripe/stripe-python/pull/1602
is_breaking: true
released_in_version: 13.0.0
---

- ⚠️ Move `stripe.v2._event` and `stripe.v2._event_destination` to `stripe.v2.core._event` and `stripe.v2.core._event_destination` respectively. They now correctly match their API path
