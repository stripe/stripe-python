---
title: Omit API keys from pickled StripeObjects
semver_level: major
---

StripeObject pickles no longer preserve SDK-held API keys. Applications making object-based requests after cache or queue round trips must explicitly bind receiving-process credentials with `set_api_key()`. This is a breaking authentication change. See the [v16 migration guide](https://github.com/stripe/stripe-python/blob/master/.hark/migration-guides/v16.md#api-keys-are-no-longer-preserved-in-pickled-stripeobjects).
