---
title: Omit API keys from pickled StripeObjects
semver_level: major
---
StripeObject pickles no longer preserve API keys. Before making requests through an unpickled object, call `object.reattach_api_key(api_key)` with a key from secure configuration. This also reattaches api keys to nested objects while preserving their connected accounts and API versions. Global and per-call keys cannot bypass this requirement; reattachment is rejected for normal objects and objects already reattached. See the [v17 migration guide](https://github.com/stripe/stripe-python/blob/master/.hark/migration-guides/v17.md#api-keys-are-no-longer-preserved-in-pickled-stripeobjects).
